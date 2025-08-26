# Script to calculate shape systematics of photon and electron
# * https://twiki.cern.ch/twiki/bin/view/CMS/EgammaMiniAODV2#Energy_Scale_and_Smearing
# * Run script once per category, loops over signal processes.
# * photon shape: uncertainties of standard EGM calibration
# * merged electron shape: uncertainties of dedicated HDALITZ calibration
# * resolved electron shape: uncertainties of standard EGM calibration
# * Outputs are pandas dataframes for scale and resolutions respectively @ all mass points

import os, sys
sys.path.append("./tools")

import ROOT
import pickle
import numpy as np
import pandas as pd
from argparse import ArgumentParser
from commonObjects import productionModes, inputWSName__, swd__, massBaseList, decayMode
from commonTools import color
from effSigma import effSigma


def get_parser():
    parser = ArgumentParser(description="Script to calculate effect of the shape systematic uncertainties")
    parser.add_argument("-c",   "--category",        help="RECO category",                                           default="",     type=str)
    parser.add_argument("-y",   "--year",            help="year",                                                    default="",     type=str)
    parser.add_argument("-i",   "--inputWSDir",      help="Input WS directory",                                      default="",     type=str)
    parser.add_argument("-tm",  "--thresholdMean",   help="Reject mean variations if larger than thresholdMean",     default=0.5,   type=float)
    parser.add_argument("-ts",  "--thresholdSigma",  help="Reject mean variations if larger than thresholdSigma",    default=0.5,    type=float)
    parser.add_argument("-pn",  "--preventNegative", help="set the negative bin content of mass histograms to 0.",       default=False,action="store_true")

    return parser


# Function to extact hists of systematics from WS
def getDataHists(_ws, _nominalDataName, _sname, _var):
    hname_nominal = _nominalDataName.replace("set", "hist_nominal_{}".format(_sname))
    hname_up = hname_nominal.replace("nominal", "up")
    hname_do = hname_nominal.replace("nominal", "do")
    
    _hists = {
        "nominal": ROOT.TH1F(hname_nominal, "", 60, 110, 170),
        "up"     : ROOT.TH1F(hname_up, "", 60, 110, 170),
        "do"     : ROOT.TH1F(hname_do, "", 60, 110, 170)
    }
    
    # get data
    ds_nominal = _ws.data(_nominalDataName)
    dh_name = _nominalDataName.replace("set", "dh")
    dh_up = _ws.data("%s_%sUp" %(dh_name, _sname))
    if "SigmaPhi" in _sname:
        dh_do = dh_up
    else:
        dh_do = _ws.data("%s_%sDo" %(dh_name, _sname))
    
    # convert to TH1
    ds_nominal.fillHistogram(_hists["nominal"], ROOT.RooArgList(_var))                    
    dh_up.fillHistogram(_hists["up"], ROOT.RooArgList(_var))
    dh_do.fillHistogram(_hists["do"], ROOT.RooArgList(_var))
    
    if args.preventNegative: # set the negative bin content to 0.
        for b in range(_hists["nominal"].GetNbinsX()+1): 
            if _hists["nominal"].GetBinContent(b+1) < 0:
                _hists["nominal"].SetBinContent(b+1, 0)
            if _hists["up"].GetBinContent(b+1) < 0:
                _hists["up"].SetBinContent(b+1, 0)
            if _hists["do"].GetBinContent(b+1) < 0:
                _hists["do"].SetBinContent(b+1, 0)

    return _hists


# Functions to extract mean and sigma variations
def getMeanVar(_hists):
    mu, muVar = {}, {}
    for htype, h in _hists.items():
        mu[htype] = h.GetMean()
    
    if (mu["nominal"] == 0.):
        return 0.
    
    for htype in ["up", "do"]:
        muVar[htype] = (mu[htype] - mu["nominal"]) / mu["nominal"]
    
    x = np.float64((abs(muVar["up"]) + abs(muVar["do"])) / 2)
    if (np.isnan(x)):
        print("Get NaN mean variation")
        sys.exit(1)
    return min(x, args.thresholdMean)


def getSigmaVar(_hists):
    sigma, sigmaVar = {}, {}
    for htype, h in _hists.items():
        sigma[htype] = effSigma(h)

    if (sigma["nominal"] == 0.):
        return 0.
    
    for htype in ["up", "do"]:
        sigmaVar[htype] = (sigma[htype] - sigma["nominal"]) / sigma["nominal"]
    
    x = np.float64((abs(sigmaVar["up"]) + abs(sigmaVar["do"])) / 2) # average
    if (np.isnan(x)):
        print("Get NaN sigma variation")
        sys.exit(1)
    return min(x, args.thresholdSigma)


def main(mass):
    shape_variations = [
        "PhoScaleStat",
        "PhoScaleSyst",
        "PhoScaleGain",
        "PhoSigmaPhi",
        "PhoSigmaRho",
    ]
    if "Resolved" in args.category:
        shape_variations = shape_variations + [
            "EleScaleStat",
            "EleScaleSyst",
            "EleScaleGain",
            "EleSigmaPhi",
            "EleSigmaRho"
        ]
    else:
        shape_variations = shape_variations + [
            "EleHDALScale",
            "EleHDALSmear"
        ]
    

    # Define dataFrame
    columns_data_scale = ["proc", "cat", "mass", "year", "inputWSFile", "nominalDataName"]
    columns_data_resol = ["proc", "cat", "mass", "year", "inputWSFile", "nominalDataName"]
    shape_scale = []
    shape_resol = []
    for s in shape_variations:
        for x in ["scale", "resol"]:
            if (x == "scale" and "Scale" in s):
                columns_data_scale.append(s)
                
                shape_scale.append(s)
            elif (x == "resol" and ("Sigma" in s or "Smear" in s)):
                columns_data_resol.append(s)
                shape_resol.append(s)
    data_scale = pd.DataFrame(columns=columns_data_scale)
    data_resol = pd.DataFrame(columns=columns_data_resol)

    # Loop over processes and add row to dataframe
    for _proc in productionModes:
        _WSFileName = "%s/signal_%s_%s.root" %(args.inputWSDir, _proc, mass)
        _nominalDataName = "set_%s_%s" %(mass, args.category)
        
        data_scale_proc = pd.DataFrame({"proc":_proc, "cat":args.category, "mass":mass, "year":args.year, "inputWSFile":_WSFileName, "nominalDataName":_nominalDataName}, index=[0])
        data_scale = pd.concat([data_scale, data_scale_proc], ignore_index=True, sort=False)
        
        data_resol_proc = pd.DataFrame({"proc":_proc, "cat":args.category, "mass":mass, "year":args.year, "inputWSFile":_WSFileName, "nominalDataName":_nominalDataName}, index=[0])
        data_resol = pd.concat([data_resol, data_resol_proc], ignore_index=True, sort=False)

    # add the scale unc to dataframe
    for ir, r in data_scale.iterrows():
        print(" --> Processing ({proc:>4}, {cat}, {m}, {y:<5}) scale uncertainties".format(proc=r["proc"], cat=args.category, m=r["mass"], y=r["year"]))
        # Open ROOT file and extract workspace
        f = ROOT.TFile(r["inputWSFile"], "READ")
        if f.IsZombie():
            sys.exit(1)
        inputWS = f.Get(inputWSName__)
        if not inputWS:
            print("Fail to get workspace %s" %(inputWSName__))
            sys.exit(1)
        # Add values to dataFrame
        for s in shape_scale:
            hists = getDataHists(inputWS, r["nominalDataName"], s, inputWS.var("CMS_higgs_mass"))
            _meanVar = getMeanVar(hists)
            data_scale.at[ir, s] = _meanVar
            for var, h in hists.items():
                h.Delete()
        # close file
        f.Close()
    
    shape_scale_ele = [s for s in shape_scale if "Ele" in s]
    shape_scale_pho = [s for s in shape_scale if "Pho" in s]
    if (len(shape_scale_ele) != 1):
        data_scale["EleTotalScale"] = np.sqrt(np.power(data_scale[shape_scale_ele], 2).sum(axis=1))
    else:
        data_scale["EleTotalScale"] = data_scale[shape_scale_ele[0]]
    if (len(shape_scale_pho) != 1):
        data_scale["PhoTotalScale"] = np.sqrt(np.power(data_scale[shape_scale_pho], 2).sum(axis=1))
    else:
        data_scale["PhoTotalScale"] = data_scale[shape_scale_pho[0]]
    # root of quadrature sum electron and photon
    data_scale["TotalScale"] = np.sqrt(np.power(data_scale[["EleTotalScale", "PhoTotalScale"]], 2).sum(axis=1))

    # add the resolution unc to dataframe
    for ir, r in data_resol.iterrows():
        print(" --> Processing ({proc:>4}, {cat}, {m}, {y:<5}) resol uncertainties".format(proc=r["proc"], cat=args.category, m=r["mass"], y=r["year"]))
        # Open ROOT file and extract workspace
        f = ROOT.TFile(r["inputWSFile"])
        if f.IsZombie():
            sys.exit(1)
        inputWS = f.Get(inputWSName__)
        if not inputWS:
            print("Fail to get workspace %s" %(inputWSName__))
            sys.exit(1)
        # Add values to dataFrame
        for s in shape_resol:
            hists = getDataHists(inputWS, r["nominalDataName"], s, inputWS.var("CMS_higgs_mass"))
            _sigmaVar = getSigmaVar(hists)
            data_resol.at[ir, s] = _sigmaVar
        # close file
        f.Close()
    
    shape_resol_ele = [s for s in shape_resol if "Ele" in s]
    shape_resol_pho = [s for s in shape_resol if "Pho" in s]
    if (len(shape_resol_ele) != 1):
        data_resol["EleTotalResol"] = np.sqrt(np.power(data_resol[shape_resol_ele], 2).sum(axis=1))
    else:
        data_resol["EleTotalResol"] = data_resol[shape_resol_ele[0]]
    if (len(shape_resol_pho) != 1):
        data_resol["PhoTotalResol"] = np.sqrt(np.power(data_resol[shape_resol_pho], 2).sum(axis=1))
    else:
        data_resol["PhoTotalResol"] = data_resol[shape_resol_pho[0]]
    # root of quadrature sum electron and photon
    data_resol["TotalResol"] = np.sqrt(np.power(data_resol[["EleTotalResol", "PhoTotalResol"]], 2).sum(axis=1))

    return data_scale, data_resol


def calcFactory(df, shape=""):
    if shape not in ["scale", "resol"]:
        print("Error: unknown shape type: {}, available type [scale, resol]".format(shape))
        sys.exit(1)

    mass_interp = np.linspace(massBaseList[0], massBaseList[-1], 11, endpoint=True).astype(int)
    column_title = ["proc", "cat", "mass", "year", "factory", "value"]
    df_data = pd.DataFrame(columns=column_title)

    for proc in df["proc"].unique():
        unc = []
        for ir, r in df.iterrows():
            if proc != r["proc"]:
                continue
            if shape == "scale":
                unc.append(r["TotalScale"])
            else:
                unc.append(r["TotalResol"])
        unc_interp = np.interp(mass_interp, np.array(massBaseList), np.array(unc))

        for i, _mp in enumerate(mass_interp):
            factory_name = "CMS_{}_{}_{}_{}_{}_{}".format(decayMode, shape, proc, _mp, args.category, args.year)
            df_data.loc[len(df_data)] = [proc, args.category, _mp, args.year, factory_name, unc_interp[i]]

    # Output dataFrame as pickle file
    if not os.path.exists("{}/syst".format(swd__)):
        os.system("mkdir -p {}/syst".format(swd__))
    with open("{}/syst/shape_syst_{}_{}_{}.pkl".format(swd__, shape, args.category, args.year), "wb") as f:
        pickle.dump(df_data, f)
    print(" --> Successfully saved {} systematics as pkl file: {}/syst/shape_syst_{}_{}_{}.pkl".format(shape, swd__, shape, args.category, args.year))


if __name__ == "__main__" :
    parser = get_parser()
    args = parser.parse_args()
    
    # PyROOT does not display any graphics(root "-b" option)
    ROOT.gROOT.SetBatch()
    ROOT.gErrorIgnoreLevel = ROOT.kWarning

    df_scale_list, df_resol_list = [], []
    for _m in massBaseList:
        df_scale, df_resol = main(_m)
        df_scale_list.append(df_scale)
        df_resol_list.append(df_resol)

    df_scale_mass = pd.concat(df_scale_list, ignore_index=True, axis=0, sort=False)
    cols_scale = [i for i in list(df_scale_mass.columns) if i != "inputWSFile"]
    print(df_scale_mass[cols_scale].to_string())

    df_resol_mass = pd.concat(df_resol_list, ignore_index=True, axis=0, sort=False)
    cols_resol = [i for i in list(df_resol_mass.columns) if i != "inputWSFile"]
    print(df_resol_mass[cols_resol].to_string())

    calcFactory(df_scale_mass, shape="scale")
    calcFactory(df_resol_mass, shape="resol")