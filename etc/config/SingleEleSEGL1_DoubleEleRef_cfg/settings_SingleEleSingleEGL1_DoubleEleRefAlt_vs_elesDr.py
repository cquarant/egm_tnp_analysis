#############################################################
# General settings

# flag to be Tested
singleEle_fired_L1_4p5_HLT_4p0  = 'JpsiKE_e2_alsotag==1'
singleEle_fired_L1_5p0_HLT_4p0  = 'JpsiKE_e2_alsotag==1'
singleEle_fired_L1_5p5_HLT_4p0  = 'JpsiKE_e2_alsotag==1'
singleEle_fired_L1_6p0_HLT_4p0  = 'JpsiKE_e2_alsotag==1'
singleEle_fired_L1_6p5_HLT_4p5  = 'JpsiKE_e2_alsotag==1'
singleEle_fired_L1_7p0_HLT_5p0  = 'JpsiKE_e2_alsotag==1'
singleEle_fired_L1_7p5_HLT_5p0  = 'JpsiKE_e2_alsotag==1'
singleEle_fired_L1_8p0_HLT_5p0  = 'JpsiKE_e2_alsotag==1'
singleEle_fired_L1_8p5_HLT_5p0  = 'JpsiKE_e2_alsotag==1'
singleEle_fired_L1_10p5_HLT_5p0 = 'JpsiKE_e2_alsotag==1'
singleEle_fired_L1_8p5_HLT_5p5  = 'JpsiKE_e2_alsotag==1'
singleEle_fired_L1_5p5_HLT_6p0  = 'JpsiKE_e2_alsotag==1'
singleEle_fired_L1_9p0_HLT_6p0  = 'JpsiKE_e2_alsotag==1'
singleEle_fired_L1_9p5_HLT_6p5  = 'JpsiKE_e2_alsotag==1'
singleEle_fired_L1_10p5_HLT_6p5 = 'JpsiKE_e2_alsotag==1'
singleEle_fired_L1_11p0_HLT_6p5 = 'JpsiKE_e2_alsotag==1'

# flag to be Tested
flags = {
    'singleEle_fired_L1_4p5_HLT_4p0' : singleEle_fired_L1_4p5_HLT_4p0,
    'singleEle_fired_L1_5p0_HLT_4p0' : singleEle_fired_L1_5p0_HLT_4p0,
    'singleEle_fired_L1_5p5_HLT_4p0' : singleEle_fired_L1_5p5_HLT_4p0,
    'singleEle_fired_L1_6p0_HLT_4p0' : singleEle_fired_L1_6p0_HLT_4p0,
    'singleEle_fired_L1_6p5_HLT_4p5' : singleEle_fired_L1_6p5_HLT_4p5,
    'singleEle_fired_L1_7p0_HLT_5p0' : singleEle_fired_L1_7p0_HLT_5p0,
    'singleEle_fired_L1_7p5_HLT_5p0' : singleEle_fired_L1_7p5_HLT_5p0,
    'singleEle_fired_L1_8p0_HLT_5p0' : singleEle_fired_L1_8p0_HLT_5p0,
    'singleEle_fired_L1_8p5_HLT_5p0' : singleEle_fired_L1_8p5_HLT_5p0,
    'singleEle_fired_L1_10p5_HLT_5p0': singleEle_fired_L1_10p5_HLT_5p0,
    'singleEle_fired_L1_8p5_HLT_5p5' : singleEle_fired_L1_8p5_HLT_5p5,
    'singleEle_fired_L1_5p5_HLT_6p0' : singleEle_fired_L1_5p5_HLT_6p0,
    'singleEle_fired_L1_9p0_HLT_6p0' : singleEle_fired_L1_9p0_HLT_6p0,
    'singleEle_fired_L1_9p5_HLT_6p5' : singleEle_fired_L1_9p5_HLT_6p5,
    'singleEle_fired_L1_10p5_HLT_6p5': singleEle_fired_L1_10p5_HLT_6p5,
    'singleEle_fired_L1_11p0_HLT_6p5': singleEle_fired_L1_11p0_HLT_6p5,
    }

# Output directory
# baseOutDir = 'results/SingleEleSingleEGL1_DoubleEleRefAlt_vs_elesDr'
baseOutDir = 'results/SingleEleSingleEGL1_DoubleEleRefAlt_vs_elesDr_nobins'

#############################################################
# Samples definition  - preparing the samples

### samples are defined in etc/inputs/tnpSampleDef.py
### not: you can setup another sampleDef File in inputs
import etc.inputs.tnpSampleDef as tnpSamples
tnpTreeDir = 'nano_'

samplesDef = {
    'data' : tnpSamples.Parking_doubleEle_run3['data_SingleEleSingleEGL1_Run2022FG-Prompt'].clone(),

    'mcNom'  : tnpSamples.Parking_doubleEle_run3['BuToKJpsi'].clone(),
    'mcAlt'  : tnpSamples.Parking_doubleEle_run3['BuToKJpsi'].clone(),
    'tagSel' : tnpSamples.Parking_doubleEle_run3['BuToKJpsi'].clone(),
}

## set MC weight
weightName = 'weight'    # 1 for data; pu_weight for MC   

#############################################################
# Bining definition  [can be nD bining]
biningDef = [
    # elesDr binning
    # { 'var' : 'JpsiKE_elesDr', 'type': 'float', 'bins': [0, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.6, 0.9] }, #elesDr_standard
    # { 'var' : 'JpsiKE_elesDr', 'type': 'float', 'bins': [0, 0.12, 0.20, 0.28, 0.44, 1.5] }, # Noah Bins
    { 'var' : 'JpsiKE_elesDr', 'type': 'float', 'bins': [0, 2] }, # no bins
]

#############################################################

# Cuts definition for all samples
cutBase = 'JpsiKE_Jpsi_mass_nofit>2.10001 && JpsiKE_Jpsi_mass_nofit<3.61 && abs(JpsiKE_e1_eta)<1.22 & abs(JpsiKE_e2_eta)<1.22 & JpsiKE_e1_pt>4.0 & JpsiKE_e2_pt>4.0 & JpsiKE_e1_passMVA==1 & JpsiKE_e2_passMVA==1'

specialCut = {
    'singleEle_fired_L1_4p5_HLT_4p0' : ' & JpsiKE_e1_pt>4.5 & JpsiKE_e2_pt>4.5 & DoubleEle4_fired==1   & (JpsiKE_e1_Ele4_match==1   & JpsiKE_e2_Ele4_match==1)   & JpsiKE_e1_bestL1pt>4.5  & JpsiKE_e2_bestL1pt>4.5  & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.001 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.001',
    'singleEle_fired_L1_5p0_HLT_4p0' : ' & JpsiKE_e1_pt>5.0 & JpsiKE_e2_pt>5.0 & DoubleEle4_fired==1   & (JpsiKE_e1_Ele4_match==1   & JpsiKE_e2_Ele4_match==1)   & JpsiKE_e1_bestL1pt>5.0  & JpsiKE_e2_bestL1pt>5.0  & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.001 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.001',
    'singleEle_fired_L1_5p5_HLT_4p0' : ' & JpsiKE_e1_pt>5.5 & JpsiKE_e2_pt>5.5 & DoubleEle4_fired==1   & (JpsiKE_e1_Ele4_match==1   & JpsiKE_e2_Ele4_match==1)   & JpsiKE_e1_bestL1pt>5.5  & JpsiKE_e2_bestL1pt>5.5  & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.001 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.001',
    'singleEle_fired_L1_6p0_HLT_4p0' : ' & JpsiKE_e1_pt>6.0 & JpsiKE_e2_pt>6.0 & DoubleEle4_fired==1   & (JpsiKE_e1_Ele4_match==1   & JpsiKE_e2_Ele4_match==1)   & JpsiKE_e1_bestL1pt>6.0  & JpsiKE_e2_bestL1pt>6.0  & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.001 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.001',
    'singleEle_fired_L1_6p5_HLT_4p5' : ' & JpsiKE_e1_pt>6.5 & JpsiKE_e2_pt>6.5 & DoubleEle4p5_fired==1 & (JpsiKE_e1_Ele4p5_match==1 & JpsiKE_e2_Ele4p5_match==1) & JpsiKE_e1_bestL1pt>6.5  & JpsiKE_e2_bestL1pt>6.5  & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.001 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.001',
    'singleEle_fired_L1_7p0_HLT_5p0' : ' & JpsiKE_e1_pt>7.0 & JpsiKE_e2_pt>7.0 & DoubleEle5_fired==1   & (JpsiKE_e1_Ele5_match==1   & JpsiKE_e2_Ele5_match==1)   & JpsiKE_e1_bestL1pt>7.0  & JpsiKE_e2_bestL1pt>7.0  & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.001 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.001',
    'singleEle_fired_L1_7p5_HLT_5p0' : ' & JpsiKE_e1_pt>7.5 & JpsiKE_e2_pt>7.5 & DoubleEle5_fired==1   & (JpsiKE_e1_Ele5_match==1   & JpsiKE_e2_Ele5_match==1)   & JpsiKE_e1_bestL1pt>7.5  & JpsiKE_e2_bestL1pt>7.5  & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.001 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.001',
    'singleEle_fired_L1_8p0_HLT_5p0' : ' & JpsiKE_e1_pt>8.0 & JpsiKE_e2_pt>8.0 & DoubleEle5_fired==1   & (JpsiKE_e1_Ele5_match==1   & JpsiKE_e2_Ele5_match==1)   & JpsiKE_e1_bestL1pt>8.0  & JpsiKE_e2_bestL1pt>8.0  & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.001 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.001',
    'singleEle_fired_L1_8p5_HLT_5p0' : ' & JpsiKE_e1_pt>8.5 & JpsiKE_e2_pt>8.5 & DoubleEle5_fired==1   & (JpsiKE_e1_Ele5_match==1   & JpsiKE_e2_Ele5_match==1)   & JpsiKE_e1_bestL1pt>8.5  & JpsiKE_e2_bestL1pt>8.5  & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.001 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.001',
    'singleEle_fired_L1_10p5_HLT_5p0': ' & JpsiKE_e1_pt>10.5 & JpsiKE_e2_pt>10.5 & DoubleEle5_fired==1   & (JpsiKE_e1_Ele5_match==1   & JpsiKE_e2_Ele5_match==1)   & JpsiKE_e1_bestL1pt>10.5 & JpsiKE_e2_bestL1pt>10.5 & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.001 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.001',
    'singleEle_fired_L1_8p5_HLT_5p5' : ' & JpsiKE_e1_pt>8.5 & JpsiKE_e2_pt>8.5 & DoubleEle5p5_fired==1 & (JpsiKE_e1_Ele5p5_match==1 & JpsiKE_e2_Ele5p5_match==1) & JpsiKE_e1_bestL1pt>8.5  & JpsiKE_e2_bestL1pt>8.5  & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.001 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.001',
    'singleEle_fired_L1_5p5_HLT_6p0' : ' & JpsiKE_e1_pt>5.5 & JpsiKE_e2_pt>5.5 & DoubleEle6_fired==1   & (JpsiKE_e1_Ele6_match==1   & JpsiKE_e2_Ele6_match==1)   & JpsiKE_e1_bestL1pt>5.5  & JpsiKE_e2_bestL1pt>5.5  & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.001 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.001',
    'singleEle_fired_L1_9p0_HLT_6p0' : ' & JpsiKE_e1_pt>9.0 & JpsiKE_e2_pt>9.0 & DoubleEle6_fired==1   & (JpsiKE_e1_Ele6_match==1   & JpsiKE_e2_Ele6_match==1)   & JpsiKE_e1_bestL1pt>9.0  & JpsiKE_e2_bestL1pt>9.0  & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.001 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.001',
    'singleEle_fired_L1_9p5_HLT_6p5' : ' & JpsiKE_e1_pt>9.5 & JpsiKE_e2_pt>9.5 & DoubleEle6p5_fired==1 & (JpsiKE_e1_Ele6p5_match==1 & JpsiKE_e2_Ele6p5_match==1) & JpsiKE_e1_bestL1pt>9.5  & JpsiKE_e2_bestL1pt>9.5  & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.001 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.001',
    'singleEle_fired_L1_10p5_HLT_6p5': ' & JpsiKE_e1_pt>10.5 & JpsiKE_e2_pt>10.5 & DoubleEle6p5_fired==1 & (JpsiKE_e1_Ele6p5_match==1 & JpsiKE_e2_Ele6p5_match==1) & JpsiKE_e1_bestL1pt>10.5 & JpsiKE_e2_bestL1pt>10.5 & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.001 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.001',
    'singleEle_fired_L1_11p0_HLT_6p5': ' & JpsiKE_e1_pt>11.0 & JpsiKE_e2_pt>11.0 & DoubleEle6p5_fired==1 & (JpsiKE_e1_Ele6p5_match==1 & JpsiKE_e2_Ele6p5_match==1) & JpsiKE_e1_bestL1pt>11.5 & JpsiKE_e2_bestL1pt>11.5 & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.001 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.001',
}

# can add addtionnal cuts for some bins (first check bin number using tnpEGM --checkBins)
#additionalCuts = { 
#    0 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45'
#}

# or remove any additional cut (default)
additionalCuts = None

### Add filtering on input json file
# if jsonfilter == True, filter data using json in jsonfileDict
jsonfilter = False

jsonfileDict = {
    'singleEle_fired_L1_4p5_HLT_4p0'   : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_4p5_HLT_4p0_Incl_Final.json',
    'singleEle_fired_L1_5p0_HLT_4p0'   : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_5p0_HLT_4p0_Incl_Final.json',
    'singleEle_fired_L1_5p5_HLT_4p0'   : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_5p5_HLT_4p0_Incl_Final.json',
    'singleEle_fired_L1_6p0_HLT_4p0'   : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_6p0_HLT_4p0_Incl_Final.json',
    'singleEle_fired_L1_6p5_HLT_4p5' : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_6p5_HLT_4p5_Incl_Final.json',
    'singleEle_fired_L1_7p0_HLT_5p0'   : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_7p0_HLT_5p0_Incl_Final.json',
    'singleEle_fired_L1_7p5_HLT_5p0'   : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_7p5_HLT_5p0_Incl_Final.json',
    'singleEle_fired_L1_8p0_HLT_5p0'   : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_8p0_HLT_5p0_Incl_Final.json',
    'singleEle_fired_L1_8p5_HLT_5p0'   : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_8p5_HLT_5p0_Incl_Final.json',
    'singleEle_fired_L1_10p5_HLT_5p0'  : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_10p5_HLT_5p0_Incl_Final.json',
    'singleEle_fired_L1_8p5_HLT_5p5' : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_8p5_HLT_5p5_Incl_Final.json',
    'singleEle_fired_L1_5p5_HLT_6p0'   : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_5p5_HLT_6p0_Incl_Final.json',
    'singleEle_fired_L1_9p0_HLT_6p0'   : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_9p0_HLT_6p0_Incl_Final.json',
    #'doubleEle6p5BothMatchedL1_9p5_Match' : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_9p5_HLT_6p5_Incl_Final.json',
    'singleEle_fired_L1_9p5_HLT_6p5' : '',
    'singleEle_fired_L1_10p5_HLT_6p5': '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_10p5_HLT_6p5_Incl_Final.json',
    'singleEle_fired_L1_11p0_HLT_6p5': '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_11p0_HLT_6p5_Incl_Final.json',
}

#############################################################
# Fitting params to tune fit by hand if necessary
tnpParAltSigFitJPsi = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.1,0.01,3.0]",      
    "meanF[-0.0,-0.5,0.5]","sigmaF[0.1,0.01,1.0]",
    "alphaP[0.5, 0.2, 0.8]",
    "alphaF[0.5, 0.2, 0.8]",    
    ]

tnpParNomFitJPsi = [
    # DoubleCB signal + Bkg Exp on DATA
    "meanP[3.096, 3.0, 3.15]","sigmaP[0.055, 0.045, 0.1]" , "alphaLP[0.5, 0.2, 0.7]" , "alphaRP[0.9, 0.8, 1.5]" , "nLP[14, 10, 16]","nRP[5, 4, 8]",
    "meanF[3.096, 3.0, 3.15]","sigmaF[0.055, 0.045, 0.1]" , "alphaLF[0.6, 0.5, 0.7]" , "alphaRF[1.0, 0.8, 1.2]" , "nLF[14, 10, 16]","nRF[5, 4, 8]",
    "expalphaP[-0.7, -2.0, 0]",
    "expalphaF[-0.75, -2.0, 0]",   

    # to be edited for selected bins bins
    # "meanP[3.096, 3.0, 3.11]","sigmaP[0.055, 0.045, 0.065]" , "alphaLP[0.5, 0.2, 0.7]" , "alphaRP[0.9, 0.8, 1.5]" , "nLP[14, 10, 16]","nRP[5, 4, 8]",
    # "meanF[3.096, 3.0, 3.11]","sigmaF[0.055, 0.045, 0.065]" , "alphaLF[0.6, 0.5, 0.7]" , "alphaRF[1.0, 0.8, 1.2]" , "nLF[14, 10, 16]","nRF[5, 4, 8]",
    # "expalphaP[-0.70, -2.0, 0.0]",
    # "expalphaF[-0.75, -2.0, 0.0]",   
]
     
tnpParAltBkgFitJPsi = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.1,0.01,3.0]",      
    "meanF[-0.0,-0.5,0.5]","sigmaF[0.1,0.01,1.0]",
    "cP[0.,-100.,100.]",
    "cF[0.,-100.,500.]",
    ]

