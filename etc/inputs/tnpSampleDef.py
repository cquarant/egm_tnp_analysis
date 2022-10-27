from libPython.tnpClassUtils import tnpSample

### samples
cquarantTnp = '/pnfs/roma1.infn.it/data/cms/store/user/cquarant/'
crovelliTnp = '/pnfs/roma1.infn.it/data/cms/store/user/crovelli/'
cmsswbase = '~/CMSSW_10_6_29/src/'

eosTnp = '/eos/cms/store/user/crovelli/LowPtEle/TnpData/March21noRegression/'

cquarantlxplus = '/afs/cern.ch/work/c/cquarant/RKanalysis/data/'

Parking_Jan16 = {
    'BuToKJpsi'          : tnpSample('BuToKJpsi',
                                    # eosTnp + 'Formatted_TnP_March21_BuToKJpsiToeeV2_PUweightsRunAll__probeLowPt.root',                                               
                                     eosTnp + 'Formatted_March21_NoRegr_BuToKJpsi_Toee_v2_probePF__withPuWeights.root',
                                     isMC = True, nEvts =  -1 ),

    'data_Run2022C-Prompt' : tnpSample('data_Run2022C-Prompt' , 
                                  cquarantTnp + 'EGamma2022/crab_doubleele/crab_doubleelemisseddataset/EGamma/Run2022C-PromptReco-v1/JPsi_ElePlusJet_controlTrigger_merged.root' ,
                                  lumi = 1.), 

    'data_Run2022CD-Prompt': tnpSample('data_Run2022CD-Prompt' , 
                                  cquarantlxplus + 'JPsi_ElePlusJet_controlTrigger_merged_2022CD.root' ,
                                  lumi = 7.), 

    'data_Run2022EF-Prompt': tnpSample('data_Run2022EF-Prompt' , 
                                  cquarantlxplus + 'JPsi_ElePlusJet_controlTrigger_merged_2022EF.root' ,
                                  lumi = 1.), 

    'data_Run2022CDEF-Prompt': tnpSample('data_Run2022CDEF-Prompt' , 
                                  cquarantlxplus + 'JPsi_ElePlusJet_controlTrigger_merged_2022CDEF_24Oct2022.root' ,
                                  lumi = 1.), 
    'data_SingleEle_Run2022F-Prompt': tnpSample('data_SingleEle_Run2022F-Prompt' , 
                                  cquarantlxplus + 'JPsi_SingleEle_controlTrigger_merged_2022F.root' ,
                                  lumi = 1.), 
    }

# eosTnp = '/eos/cms/store/user/crovelli/LowPtEle/TnpData/Sept/Jan16/'

# Parking_Jan16 = {
#     ### NanoAOD TnP for IDs scale factors
#     'BuToKJpsi'          : tnpSample('BuToKJpsi',
#                                      eosTnp + 'Formatted_BuToKJpsi_Toee_BParkNANO_mc_2020May16_ext_probeLowPt__tagIdCutsAt0__withNvtxWeights.root',
#                                      isMC = True, nEvts =  -1 ),

#     'data_Run2018ALL' : tnpSample('data_Run2018ALL' , eosTnp + 'Formatted_Parking_Run2018ALL_probeLowPt__tagIdCutsAt0.root' , lumi = 20.), 
#     }

