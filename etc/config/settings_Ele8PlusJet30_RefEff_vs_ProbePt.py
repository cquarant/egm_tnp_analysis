#############################################################
# General settings

# flag to be Tested
probe_fired = 'JpsiKE_e2_alsotag==1'

# flag to be Tested
flags = {
    'probe_fired': probe_fired,
    }

# Output directory
baseOutDir = 'results/RefEff_vs_Probe_Pt_ElePlusJet'

#############################################################
# Samples definition  - preparing the samples

### samples are defined in etc/inputs/tnpSampleDef.py
### not: you can setup another sampleDef File in inputs
import etc.inputs.tnpSampleDef as tnpSamples
tnpTreeDir = 'nano_'

samplesDef = {
    'data' : tnpSamples.Parking_doubleEle_run3['data_Run2022CDEFG-Prompt'].clone(),

    'mcNom'  : tnpSamples.Parking_doubleEle_run3['BuToKJpsi'].clone(),
    'mcAlt'  : tnpSamples.Parking_doubleEle_run3['BuToKJpsi'].clone(),
    'tagSel' : tnpSamples.Parking_doubleEle_run3['BuToKJpsi'].clone(),
}

## set MC weight
weightName = 'weight'    # 1 for data; pu_weight for MC   

#############################################################
# Bining definition  [can be nD bining]
biningDef = [
    #{ 'var' : 'JpsiKE_e2_pt', 'type': 'float', 'bins': [5.0, 999.0] }, #no binning

    # Probe Pt binning
    # { 'var' : 'JpsiKE_e2_pt', 'type': 'float', 'bins': [5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 9999999.0] }, #standard_2022_final
    { 'var' : 'JpsiKE_e2_pt', 'type': 'float', 'bins': [5.0, 6.0,  7.0,  8.0,  9.0, 11.0, 13.0, 19.0, 9999999.0] }, #standard_2022_final
    # { 'var' : 'JpsiKE_e2_pt', 'type': 'float', 'bins': [5.0, 9.0, 11.0, 13.0, 9999999.0] }, #e1 eff
    
]

#############################################################

# Cuts definition for all samples
cutBase = 'JpsiKE_Jpsi_mass_nofit>2.10001 && JpsiKE_Jpsi_mass_nofit<3.61 && abs(JpsiKE_e1_eta)<2.5 & abs(JpsiKE_e2_eta)<2.5 & JpsiKE_e1_pt>4.0 & JpsiKE_e2_pt>4.0 & JpsiKE_e1_passMVA==1 & JpsiKE_e2_passMVA==1'

specialCut = {
    'probe_fired': '',
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
    'doubleEle4BothMatchedL1_4p5_Match'   : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_4p5_HLT_4p0_Incl_Final.json',
    'doubleEle4BothMatchedL1_5p0_Match'   : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_5p0_HLT_4p0_Incl_Final.json',
    'doubleEle4BothMatchedL1_5p5_Match'   : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_5p5_HLT_4p0_Incl_Final.json',
    'doubleEle4BothMatchedL1_6p0_Match'   : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_6p0_HLT_4p0_Incl_Final.json',
    'doubleEle4p5BothMatchedL1_6p5_Match' : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_6p5_HLT_4p5_Incl_Final.json',
    'doubleEle5BothMatchedL1_7p0_Match'   : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_7p0_HLT_5p0_Incl_Final.json',
    'doubleEle5BothMatchedL1_7p5_Match'   : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_7p5_HLT_5p0_Incl_Final.json',
    'doubleEle5BothMatchedL1_8p0_Match'   : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_8p0_HLT_5p0_Incl_Final.json',
    'doubleEle5BothMatchedL1_8p5_Match'   : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_8p5_HLT_5p0_Incl_Final.json',
    'doubleEle5BothMatchedL1_10p5_Match'  : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_10p5_HLT_5p0_Incl_Final.json',
    'doubleEle5p5BothMatchedL1_8p5_Match' : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_8p5_HLT_5p5_Incl_Final.json',
    'doubleEle6BothMatchedL1_5p5_Match'   : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_5p5_HLT_6p0_Incl_Final.json',
    'doubleEle6BothMatchedL1_9p0_Match'   : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_9p0_HLT_6p0_Incl_Final.json',
    #'doubleEle6p5BothMatchedL1_9p5_Match' : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_9p5_HLT_6p5_Incl_Final.json',
    'doubleEle6p5BothMatchedL1_9p5_Match' : '',
    'doubleEle6p5BothMatchedL1_10p5_Match': '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_10p5_HLT_6p5_Incl_Final.json',
    'doubleEle6p5BothMatchedL1_11p0_Match': '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_11p0_HLT_6p5_Incl_Final.json',
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
    # "meanP[3.096, 3.0, 3.15]","sigmaP[0.055, 0.045, 0.1]" , "alphaLP[0.5, 0.2, 0.7]" , "alphaRP[0.9, 0.8, 1.5]" , "nLP[14, 10, 16]","nRP[5, 4, 8]",
    # "meanF[3.096, 3.0, 3.15]","sigmaF[0.055, 0.045, 0.1]" , "alphaLF[0.6, 0.5, 0.7]" , "alphaRF[1.0, 0.8, 1.2]" , "nLF[14, 10, 16]","nRF[5, 4, 8]",
    # "expalphaP[-0.7, -2.0, 0]",
    # "expalphaF[-0.75, -2.0, 0]",   

    # to be edited for selected bins bins
    "meanP[3.096, 3.0, 3.11]","sigmaP[0.055, 0.045, 0.065]" , "alphaLP[0.5, 0.2, 0.7]" , "alphaRP[0.9, 0.8, 1.5]" , "nLP[14, 10, 16]","nRP[5, 4, 8]",
    "meanF[3.096, 3.0, 3.11]","sigmaF[0.055, 0.045, 0.065]" , "alphaLF[0.6, 0.5, 0.7]" , "alphaRF[1.0, 0.8, 1.2]" , "nLF[14, 10, 16]","nRF[5, 4, 8]",
    "expalphaP[-0.70, -2.0, 0.0]",
    "expalphaF[-0.75, -2.0, 0.0]",   
]
     
tnpParAltBkgFitJPsi = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.1,0.01,3.0]",      
    "meanF[-0.0,-0.5,0.5]","sigmaF[0.1,0.01,1.0]",
    "cP[0.,-100.,100.]",
    "cF[0.,-100.,500.]",
    ]

