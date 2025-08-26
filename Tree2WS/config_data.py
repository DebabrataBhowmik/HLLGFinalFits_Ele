from commonObjects import twd__

trees2ws_cfg = {
    # Input root files which contain TTree
    "inputTreeFiles": [
        "/data4/chenghan/electron/miniTree_merged/UL2016preVFP/miniTree_DoubleEG_Run2016B_UL2016preVFP.root",
        "/data4/chenghan/electron/miniTree_merged/UL2016preVFP/miniTree_DoubleEG_Run2016C_UL2016preVFP.root",
        "/data4/chenghan/electron/miniTree_merged/UL2016preVFP/miniTree_DoubleEG_Run2016D_UL2016preVFP.root",
        "/data4/chenghan/electron/miniTree_merged/UL2016preVFP/miniTree_DoubleEG_Run2016E_UL2016preVFP.root",
        "/data4/chenghan/electron/miniTree_merged/UL2016preVFP/miniTree_DoubleEG_Run2016F1_UL2016preVFP.root",

        "/data4/chenghan/electron/miniTree_merged/UL2016postVFP/miniTree_DoubleEG_Run2016F2_UL2016postVFP.root",
        "/data4/chenghan/electron/miniTree_merged/UL2016postVFP/miniTree_DoubleEG_Run2016G_UL2016postVFP.root",
        "/data4/chenghan/electron/miniTree_merged/UL2016postVFP/miniTree_DoubleEG_Run2016H_UL2016postVFP.root",

        "/data4/chenghan/electron/miniTree_merged/UL2017/miniTree_DoubleEG_Run2017B_UL2017.root",
        "/data4/chenghan/electron/miniTree_merged/UL2017/miniTree_DoubleEG_Run2017C_UL2017.root",
        "/data4/chenghan/electron/miniTree_merged/UL2017/miniTree_DoubleEG_Run2017D_UL2017.root",
        "/data4/chenghan/electron/miniTree_merged/UL2017/miniTree_DoubleEG_Run2017E_UL2017.root",
        "/data4/chenghan/electron/miniTree_merged/UL2017/miniTree_DoubleEG_Run2017F_UL2017.root",

        "/data4/chenghan/electron/miniTree_merged/UL2018/miniTree_EGamma_Run2018A_UL2018.root",
        "/data4/chenghan/electron/miniTree_merged/UL2018/miniTree_EGamma_Run2018B_UL2018.root",
        "/data4/chenghan/electron/miniTree_merged/UL2018/miniTree_EGamma_Run2018C_UL2018.root",
        "/data4/chenghan/electron/miniTree_merged/UL2018/miniTree_EGamma_Run2018D_UL2018.root",
        
        
        "/data4/chenghan/electron/miniTree_resolved/UL2016preVFP/miniTree_SingleEle_Run2016B_UL2016preVFP.root",
        "/data4/chenghan/electron/miniTree_resolved/UL2016preVFP/miniTree_SingleEle_Run2016C_UL2016preVFP.root",
        "/data4/chenghan/electron/miniTree_resolved/UL2016preVFP/miniTree_SingleEle_Run2016D_UL2016preVFP.root",
        "/data4/chenghan/electron/miniTree_resolved/UL2016preVFP/miniTree_SingleEle_Run2016E_UL2016preVFP.root",
        "/data4/chenghan/electron/miniTree_resolved/UL2016preVFP/miniTree_SingleEle_Run2016F1_UL2016preVFP.root",

        "/data4/chenghan/electron/miniTree_resolved/UL2016postVFP/miniTree_SingleEle_Run2016F2_UL2016postVFP.root",
        "/data4/chenghan/electron/miniTree_resolved/UL2016postVFP/miniTree_SingleEle_Run2016G_UL2016postVFP.root",
        "/data4/chenghan/electron/miniTree_resolved/UL2016postVFP/miniTree_SingleEle_Run2016H_UL2016postVFP.root",

        "/data4/chenghan/electron/miniTree_resolved/UL2017/miniTree_SingleEle_Run2017B_UL2017.root",
        "/data4/chenghan/electron/miniTree_resolved/UL2017/miniTree_SingleEle_Run2017C_UL2017.root",
        "/data4/chenghan/electron/miniTree_resolved/UL2017/miniTree_SingleEle_Run2017D_UL2017.root",
        "/data4/chenghan/electron/miniTree_resolved/UL2017/miniTree_SingleEle_Run2017E_UL2017.root",
        "/data4/chenghan/electron/miniTree_resolved/UL2017/miniTree_SingleEle_Run2017F_UL2017.root",

        "/data4/chenghan/electron/miniTree_resolved/UL2018/miniTree_EGamma_Run2018A_UL2018.root",
        "/data4/chenghan/electron/miniTree_resolved/UL2018/miniTree_EGamma_Run2018B_UL2018.root",
        "/data4/chenghan/electron/miniTree_resolved/UL2018/miniTree_EGamma_Run2018C_UL2018.root",
        "/data4/chenghan/electron/miniTree_resolved/UL2018/miniTree_EGamma_Run2018D_UL2018.root"
    ],

    # Name of the input tree
    "inputTreeName":  "miniTree",

    "outputWSFile": "{}/WS/data_obs.root".format(twd__)
}