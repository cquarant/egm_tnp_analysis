from libPython.tnpClassUtils import tnpSample

### samples
cquarantTnp = '/pnfs/roma1.infn.it/data/cms/store/user/cquarant/'
crovelliTnp = '/pnfs/roma1.infn.it/data/cms/store/user/crovelli/'
cmsswbase = '~/CMSSW_10_6_29/src/'

eosTnp = '/eos/cms/store/user/crovelli/LowPtEle/TnpData/March21noRegression/'

#cquarantlxplus  = '/afs/cern.ch/work/c/cquarant/RKanalysis/data/merged/'
#cquarantlxplus  = '/afs/cern.ch/work/c/cquarant/RKanalysis/data/merged_3Nov2022/'
cquarantlxplus221107 = '/afs/cern.ch/work/c/cquarant/RKanalysis/data/merged_7Nov2022/'
cquarantlxplus221212 = '/afs/cern.ch/work/c/cquarant/RKanalysis/data/merged_12Dec2022/'
cquarantlxplusmc = '/afs/cern.ch/work/c/cquarant/RKanalysis/mc/merged_BuToJpsiKEE/'

Parking_doubleEle_run3 = {
    'BuToKJpsi'          : tnpSample('BuToKJpsi',
                                     cquarantlxplusmc + 'Jpsi_BuToJpsiKEE_MC.root',
                                     isMC = True, nEvts =  -1 ),

    'BuToKJpsi_realisticPU': tnpSample('BuToKJpsi_realisticPU',
                                       cquarantlxplusmc + 'Jpsi_BuToJpsiKEE_realisticPU_MC.root',
                                       isMC = True, nEvts =  -1 ),

    'data_Run2022C-Prompt' : tnpSample('data_Run2022C-Prompt' , 
                                       cquarantTnp + 'EGamma2022/crab_doubleele/crab_doubleelemisseddataset/EGamma/Run2022C-PromptReco-v1/JPsi_ElePlusJet_controlTrigger_merged.root' ,
                                       lumi = 1.), 

    'data_Run2022CD-Prompt': tnpSample('data_Run2022CD-Prompt' , 
                                       cquarantlxplus221107 + 'JPsi_ElePlusJet_controlTrigger_merged_2022CD.root' ,
                                       lumi = 7.), 

    'data_Run2022EF-Prompt': tnpSample('data_Run2022EF-Prompt' , 
                                       cquarantlxplus221107 + 'JPsi_ElePlusJet_controlTrigger_merged_2022EF.root' ,
                                       lumi = 1.), 

    'data_Run2022CDEF-Prompt': tnpSample('data_Run2022CDEF-Prompt' , 
                                         cquarantlxplus221107 + 'JPsi_ElePlusJet_controlTrigger_merged_2022CDEF.root' ,
                                         lumi = 24.), 

    'data_Run2022CDEFG-Prompt': tnpSample('data_Run2022CDEFG-Prompt' , 
                                          cquarantlxplus221212 + 'JPsi_ElePlusJet_controlTrigger_merged_2022CDEFG.root' ,
                                          lumi = 24.), 

    'data_SingleEle_Run2022F-Prompt': tnpSample('data_SingleEle_Run2022F-Prompt' , 
                                                cquarantlxplus221107 + 'JPsi_SingleEle_controlTrigger_2022F.root' ,
                                                lumi = 1.), 

    'data_SingleEle_Run2022FG-Prompt': tnpSample('data_SingleEle_Run2022FG-Prompt' , 
                                                cquarantlxplus221212 + 'JPsi_SingleEle_controlTrigger_2022FG.root' ,
                                                lumi = 1.), 

    'data_SingleEleSingleEGL1_Run2022F-Prompt': tnpSample('data_SingleEleSingleEGL1_Run2022F-Prompt' , 
                                                          cquarantlxplus221107 + 'JPsi_SingleEle_SingleEGL1_controlTrigger_2022F.root' ,
                                                          lumi = 1.), 

    'data_SingleEleSingleEGL1_Run2022FG-Prompt': tnpSample('data_SingleEleSingleEGL1_Run2022FG-Prompt' , 
                                                           cquarantlxplus221212 + 'JPsi_SingleEle_SingleEGL1_controlTrigger_2022FG.root' ,
                                                           lumi = 1.), 
    }
