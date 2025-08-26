# Script to perform the signal fit
# * Run script once per category per year, loops over signal processes and mass points(120, 125, 130)

import sys
sys.path.append("./tools")

import ROOT
from simpleFit import simpleFit
from Interpolation import Interpolator
from argparse import ArgumentParser
from collections import OrderedDict as od
from commonObjects import inputWSName__, productionModes, swd__, massBaseList, outputWSName__, category__ 
from commonTools import cprint


def get_parser():
    parser = ArgumentParser(description="Script to perform the signal fit")
    parser.add_argument("-c",   "--category",        help="RECO category",                                   default="",     type=str)
    parser.add_argument("-y",   "--year",            help="Year",                                            default="",     type=str)
    parser.add_argument("-i",   "--inputWSDir",      help="Input WS directory",                              default="",     type=str)
    parser.add_argument("-ds",  "--doSystematics",   help="Estimate the shape uncertainties",                default=False,  action="store_true")
    parser.add_argument("-di",  "--doInterpolation", help="Do the interpolation(intermediate signal model)", default=False,  action="store_true")
    parser.add_argument("-pn",  "--preventNegative", help="set the negative bin content of mass histograms to 0.",       default=False,action="store_true")

    return parser


def main():
    for proc in productionModes:
        yields, fitres = od(), od()
        for mass in massBaseList:
            cprint("--> Performing the nominal signal fitting of {} @ {}GeV".format(proc, mass), colorStr="green")
            # Open ROOT file and extract workspace
            WSFileName = "{}/signal_{}_{}.root".format(args.inputWSDir, proc, mass)
            print(WSFileName)
            f = ROOT.TFile(WSFileName)
            if f.IsZombie():
                sys.exit(1)
            inputWS = f.Get(inputWSName__)
            if not inputWS:
                cprint("Fail to get workspace {}".format(inputWSName__))
                sys.exit(1)
                
            if args.category not in list(category__.keys()):
                cprint("category: {} is not in ".format(args.category))
                cprint("{}".format(list(category__.keys())))
                sys.exit(1)

            # Get dataset and var from workspace
            nominalDataName = "set_%d_%s"%(mass, args.category)
            xvar = inputWS.var("CMS_higgs_mass")
            data = inputWS.data(nominalDataName)
            
            hist = ROOT.TH1F("h", "", 60, 110, 170)
            data.fillHistogram(hist, ROOT.RooArgList(xvar))
            if args.preventNegative: # set the negative bin content to 0.
                for b in range(hist.GetNbinsX()+1): 
                    if hist.GetBinContent(b+1) < 0:
                        hist.SetBinContent(b+1, 0)
            sumw = 0
            for b in range(hist.GetNbinsX()+1): 
                sumw += hist.GetBinContent(b+1)
            dh = ROOT.RooDataHist(nominalDataName, nominalDataName, xvar, ROOT.RooFit.Import(hist))
            
            # FIT: binned ML fit
            fit = simpleFit(dh, xvar, mass, 110, 170)
            fit.buildDCBplusGaussian()
            # fit.buildDCB()
            # sumw = data.sumEntries()
            fitres[mass] = fit.runFit()
            fitres[mass].Print()
            yields[mass] = sumw if sumw > 0. else 0.

            # VISUALIZATION: draw the fitting
            outName = "{}/plots/signalFit/{}/CMS_HLLG_sigfit_{}_{}_{}_{}.pdf".format(swd__, args.year, mass, proc, args.year, args.category)
            fit.visualize(args.year, args.category, proc, outName)

            # Close the input workspace file
            f.Close()
            cprint("")

        if args.doInterpolation:
            # INTERPOLATRION: The signal models are gotten from the interpolation of the fittings pdfs @ 120, 125 and 130 GeV
            # specify save=True to save the final signal models
            outWSDir = "{}/WS/Interpolation/{}".format(swd__, args.year)
            interp = Interpolator(yields, fitres, 110, 170, args.year, proc, args.category, False) #!_useDCB=False if buildDCBplusGaussian, false, else true
            # interp = Interpolator(yields, fitres, 110, 170, args.year, proc, args.category, True)
            interp.calcPolation()
            interp.buildFinalPdfs(
                save=True,
                outWS=outputWSName__, outWSDir=outWSDir,
                doSystematics=args.doSystematics
            )

            # VISUALIZATION: draw the fitting
            outPlotName = "{}/plots/Interpolation/{}/CMS_HLLG_Interp_{}_{}_{}.pdf".format(swd__, args.year, proc, args.year, args.category)
            interp.visualize(outPlotName)


if __name__ == "__main__" :
    # Extract information from config file:
    parser = get_parser()
    args = parser.parse_args()

    # PyROOT does not display any graphics(root "-b" option)
    ROOT.gROOT.SetBatch()
    ROOT.gErrorIgnoreLevel = ROOT.kWarning
    
    main()