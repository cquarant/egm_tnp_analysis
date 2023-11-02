#############################################################
# General settings

# flag to be Tested
doubleEle4BothMatchedL1_4p5_Match = 'DoubleEle4_fired==1 && (JpsiKE_e1_Ele4_match==1 && JpsiKE_e2_Ele4_match==1) '
doubleEle4BothMatchedL1_5p0_Match = 'DoubleEle4_fired==1 && (JpsiKE_e1_Ele4_match==1 && JpsiKE_e2_Ele4_match==1) ' 
doubleEle4BothMatchedL1_5p5_Match = 'DoubleEle4_fired==1 && (JpsiKE_e1_Ele4_match==1 && JpsiKE_e2_Ele4_match==1) ' 
doubleEle4BothMatchedL1_6p0_Match = 'DoubleEle4_fired==1 && (JpsiKE_e1_Ele4_match==1 && JpsiKE_e2_Ele4_match==1) ' 
doubleEle4p5BothMatchedL1_6p5_Match = 'DoubleEle4p5_fired==1 && (JpsiKE_e1_Ele4p5_match==1 && JpsiKE_e2_Ele4p5_match==1) ' 
doubleEle5BothMatchedL1_7p0_Match = 'DoubleEle5_fired==1 && (JpsiKE_e1_Ele5_match==1 && JpsiKE_e2_Ele5_match==1) '
doubleEle5BothMatchedL1_7p5_Match = 'DoubleEle5_fired==1 && (JpsiKE_e1_Ele5_match==1 && JpsiKE_e2_Ele5_match==1) ' 
doubleEle5BothMatchedL1_8p0_Match = 'DoubleEle5_fired==1 && (JpsiKE_e1_Ele5_match==1 && JpsiKE_e2_Ele5_match==1) ' 
doubleEle5BothMatchedL1_8p5_Match = 'DoubleEle5_fired==1 && (JpsiKE_e1_Ele5_match==1 && JpsiKE_e2_Ele5_match==1) ' 
doubleEle5BothMatchedL1_10p5_Match= 'DoubleEle5_fired==1 && (JpsiKE_e1_Ele5_match==1 && JpsiKE_e2_Ele5_match==1) ' 
doubleEle5p5BothMatchedL1_8p5_Match= 'DoubleEle5p5_fired==1 && (JpsiKE_e1_Ele5p5_match==1 && JpsiKE_e2_Ele5p5_match==1) ' 
doubleEle6BothMatchedL1_5p5_Match = 'DoubleEle6_fired==1 && (JpsiKE_e1_Ele6_match==1 && JpsiKE_e2_Ele6_match==1) ' 
doubleEle6BothMatchedL1_9p0_Match = 'DoubleEle6_fired==1 && (JpsiKE_e1_Ele6_match==1 && JpsiKE_e2_Ele6_match==1) ' 
doubleEle6p5BothMatchedL1_9p5_Match = 'DoubleEle6p5_fired==1 && (JpsiKE_e1_Ele6p5_match==1 && JpsiKE_e2_Ele6p5_match==1) '  
doubleEle6p5BothMatchedL1_10p5_Match = 'DoubleEle6p5_fired==1 && (JpsiKE_e1_Ele6p5_match==1 && JpsiKE_e2_Ele6p5_match==1) ' 
doubleEle6p5BothMatchedL1_11p0_Match = 'DoubleEle6p5_fired==1 && (JpsiKE_e1_Ele6p5_match==1 && JpsiKE_e2_Ele6p5_match==1) ' 

# flag to be Tested
flags = {
    'doubleEle4BothMatchedL1_4p5_Match'   : doubleEle4BothMatchedL1_4p5_Match,
    'doubleEle4BothMatchedL1_5p0_Match'   : doubleEle4BothMatchedL1_5p0_Match,
    'doubleEle4BothMatchedL1_5p5_Match'   : doubleEle4BothMatchedL1_5p5_Match,
    'doubleEle4BothMatchedL1_6p0_Match'   : doubleEle4BothMatchedL1_6p0_Match,
    'doubleEle4p5BothMatchedL1_6p5_Match' : doubleEle4p5BothMatchedL1_6p5_Match,
    'doubleEle5BothMatchedL1_7p0_Match'   : doubleEle5BothMatchedL1_7p0_Match,
    'doubleEle5BothMatchedL1_7p5_Match'   : doubleEle5BothMatchedL1_7p5_Match,
    'doubleEle5BothMatchedL1_8p0_Match'   : doubleEle5BothMatchedL1_8p0_Match,
    'doubleEle5BothMatchedL1_8p5_Match'   : doubleEle5BothMatchedL1_8p5_Match,
    'doubleEle5BothMatchedL1_10p5_Match'  : doubleEle5BothMatchedL1_10p5_Match,
    'doubleEle5p5BothMatchedL1_8p5_Match' : doubleEle5p5BothMatchedL1_8p5_Match,
    'doubleEle6BothMatchedL1_5p5_Match'   : doubleEle6BothMatchedL1_5p5_Match,
    'doubleEle6BothMatchedL1_9p0_Match'   : doubleEle6BothMatchedL1_9p0_Match,
    'doubleEle6p5BothMatchedL1_9p5_Match' : doubleEle6p5BothMatchedL1_9p5_Match,
    'doubleEle6p5BothMatchedL1_10p5_Match': doubleEle6p5BothMatchedL1_10p5_Match,
    'doubleEle6p5BothMatchedL1_11p0_Match': doubleEle6p5BothMatchedL1_11p0_Match,
    }

# FINAL EFFICIENCY DEFINITION
baseOutDir = 'results/HLTeff_vs_Probe_Pt_MC'
#baseOutDir = 'results/Eff_vs_PU_MC'
#baseOutDir = 'results/Eff_vs_elesDr_MC'
#baseOutDir = 'results/Eff_vs_elesDr_MC_rebinned'

#############################################################
# Samples definition  - preparing the samples

### samples are defined in etc/inputs/tnpSampleDef.py
### not: you can setup another sampleDef File in inputs
import etc.inputs.tnpSampleDef as tnpSamples
tnpTreeDir = 'nano_'

samplesDef = {
    #'data'   : tnpSamples.Parking_doubleEle_run3['BuToKJpsi'].clone(),
    'data'   : tnpSamples.Parking_doubleEle_run3['BuToKJpsi_realisticPU'].clone(),

    'mcNom'  : tnpSamples.Parking_doubleEle_run3['BuToKJpsi'].clone(),
    'mcAlt'  : tnpSamples.Parking_doubleEle_run3['BuToKJpsi'].clone(),
    'tagSel' : tnpSamples.Parking_doubleEle_run3['BuToKJpsi'].clone(),
}

## set MC weight
weightName = 'weight'    # 1 for data; pu_weight for MC   
# if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
# if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
# if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_weight(weightName)

#############################################################
# Bining definition  [can be nD bining]
biningDef = [
    #{ 'var' : 'JpsiKE_e2_pt', 'type': 'float', 'bins': [5.0, 999.0] }, #no binning


    # Probe Pt binning
    { 'var' : 'JpsiKE_e2_pt', 'type': 'float', 'bins': [5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 13.0, 19.0, 9999999.0] }, #standard_2022_final
    # { 'var' : 'JpsiKE_e2_pt', 'type': 'float', 'bins': [5.0, 7.0, 9.0, 13.0, 9999999.0] }, #standard_2022_final
    # { 'var' : 'JpsiKE_e2_pt', 'type': 'float', 'bins': [5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 13.0, 9999999.0] }, #rebinned_2022_final_Ele+Jet

    # Nvtx binning
    # { 'var' : 'nvtx', 'type': 'float', 'bins': [0, 25, 35, 9999999.0] }, #Nvtx_standard

    # elesDR (electrons angular separation) binning
    # { 'var' : 'JpsiKE_elesDr', 'type': 'float', 'bins': [0.0, 0.15, 0.2, 0.25, 0.3, 0.35, 0.6] }, #elesDr_standard

]

#############################################################

# MC cutbase
#cutBase = 'JpsiKE_Jpsi_mass_nofit>2.10001 && JpsiKE_Jpsi_mass_nofit<3.61 && abs(JpsiKE_e1_eta)<1.22 & abs(JpsiKE_e2_eta)<1.22 & JpsiKE_e1_pt>5.0 & JpsiKE_e2_pt>5.0 & JpsiKE_elesDr<0.6 & JpsiKE_e1_passMVA==1'
# Cuts definition for all samples
cutBase = 'JpsiKE_Jpsi_mass_nofit>2.10001 && JpsiKE_Jpsi_mass_nofit<3.61 && abs(JpsiKE_e1_eta)<1.22 & abs(JpsiKE_e2_eta)<1.22 & JpsiKE_e1_pt>5.0 & JpsiKE_e2_pt>5.0 & JpsiKE_e1_passMVA==1'

specialCut = {
    'doubleEle4BothMatchedL1_4p5_Match'   : ' & JpsiKE_elesDr<0.9 && JpsiKE_e1_bestL1pt>4.5 && JpsiKE_e2_bestL1pt>4.5  & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.01 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.01',
    'doubleEle4BothMatchedL1_5p0_Match'   : ' & JpsiKE_elesDr<0.9 && JpsiKE_e1_bestL1pt>5.0 && JpsiKE_e2_bestL1pt>5.0  & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.01 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.01',
    'doubleEle4BothMatchedL1_5p5_Match'   : ' & JpsiKE_elesDr<0.8 && JpsiKE_e1_bestL1pt>5.5 && JpsiKE_e2_bestL1pt>5.5  & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.01 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.01',
    'doubleEle4BothMatchedL1_6p0_Match'   : ' & JpsiKE_elesDr<0.8 && JpsiKE_e1_bestL1pt>6.0 && JpsiKE_e2_bestL1pt>6.0  & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.01 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.01',
    'doubleEle4p5BothMatchedL1_6p5_Match' : ' & JpsiKE_elesDr<0.8 && JpsiKE_e1_bestL1pt>6.5 && JpsiKE_e2_bestL1pt>6.5  & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.01 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.01',
    'doubleEle5BothMatchedL1_7p0_Match'   : ' & JpsiKE_elesDr<0.8 && JpsiKE_e1_bestL1pt>7.0 && JpsiKE_e2_bestL1pt>7.0  & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.01 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.01',
    'doubleEle5BothMatchedL1_7p5_Match'   : ' & JpsiKE_elesDr<0.7 && JpsiKE_e1_bestL1pt>7.5 && JpsiKE_e2_bestL1pt>7.5  & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.01 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.01',
    'doubleEle5BothMatchedL1_8p0_Match'   : ' & JpsiKE_elesDr<0.7 && JpsiKE_e1_bestL1pt>8.0 && JpsiKE_e2_bestL1pt>8.0  & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.01 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.01',
    'doubleEle5BothMatchedL1_8p5_Match'   : ' & JpsiKE_elesDr<0.7 && JpsiKE_e1_bestL1pt>8.5 && JpsiKE_e2_bestL1pt>8.5  & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.01 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.01',
    'doubleEle5BothMatchedL1_10p5_Match'  : ' & JpsiKE_elesDr<0.6 && JpsiKE_e1_bestL1pt>10.5 && JpsiKE_e2_bestL1pt>10.5  & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.01 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.01',
    'doubleEle5p5BothMatchedL1_8p5_Match' : ' & JpsiKE_elesDr<0.7 && JpsiKE_e1_bestL1pt>8.5 && JpsiKE_e2_bestL1pt>8.5  & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.01 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.01',
    'doubleEle6BothMatchedL1_5p5_Match'   : ' & JpsiKE_elesDr<0.8 && JpsiKE_e1_bestL1pt>5.5 && JpsiKE_e2_bestL1pt>5.5  & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.01 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.01',
    'doubleEle6BothMatchedL1_9p0_Match'   : ' & JpsiKE_elesDr<0.7 && JpsiKE_e1_bestL1pt>9.0 && JpsiKE_e2_bestL1pt>9.0  & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.01 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.01',
    'doubleEle6p5BothMatchedL1_9p5_Match' : ' & JpsiKE_elesDr<0.7 && JpsiKE_e1_bestL1pt>8.5 && JpsiKE_e2_bestL1pt>8.5  & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.01 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.01',
    'doubleEle6p5BothMatchedL1_10p5_Match': ' & JpsiKE_elesDr<0.6 && JpsiKE_e1_bestL1pt>10.5 && JpsiKE_e2_bestL1pt>10.5  & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.01 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.01',
    'doubleEle6p5BothMatchedL1_11p0_Match': ' & JpsiKE_elesDr<0.6 && JpsiKE_e1_bestL1pt>11.0 && JpsiKE_e2_bestL1pt>11.0  & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.01 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.01',
}

# can add addtionnal cuts for some bins (first check bin number using tnpEGM --checkBins)
#additionalCuts = { 
#    0 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45'
#}

# or remove any additional cut (default)
additionalCuts = None

### Add filtering on input json file
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

    ### DoubleCB signal single pt bin MC
    # nominal fit
    "meanP[3.096, 3.06, 3.12]","sigmaP[0.05, 0.045, 0.055]" , "alphaLP[0.5, 0.4, 0.7]" , "alphaRP[0.9, 0.8, 1.5]" , "nLP[14, 0, 16]","nRP[3, 2, 4]",
    "meanF[3.096, 3.06, 3.12]","sigmaF[0.05, 0.045, 0.055]" , "alphaLF[0.5, 0.4, 0.6]" , "alphaRF[0.9, 0.8, 1.5]" , "nLF[14, 0, 16]","nRF[3, 2, 4]",
    "expalphaP[0, 0, 0]",
    "expalphaF[0, 0, 0]",   
    # to be edited for special bins
    # "meanP[3.110, 3.0, 3.2]","sigmaP[0.05, 0.04, 0.10]" , "alphaLP[0.5, 0.4, 0.7]" , "alphaRP[0.9, 0.8, 1.5]" , "nLP[14, 0, 16]","nRP[5, 3, 8]",
    # "meanF[3.096, 3.0, 3.2]","sigmaF[0.05, 0.04, 0.06]" , "alphaLF[0.563, 0.4, 0.7]" , "alphaRF[0.9, 0.8, 1.5]" , "nLF[8, 4, 10]","nRF[5, 3, 8]",
]
     
tnpParAltBkgFitJPsi = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.1,0.01,3.0]",      
    "meanF[-0.0,-0.5,0.5]","sigmaF[0.1,0.01,1.0]",
    "cP[0.,-100.,100.]",
    "cF[0.,-100.,500.]",
    ]

