#############################################################
# General settings

# flag to be Tested
idbdtlppassEB = '(probeIsLowPt==1) && probeAbsEta<1.5 && (probeMvaId > %f )' % 1.5
idbdtlppassEE = '(probeIsLowPt==1) && probeAbsEta>1.5 && (probeMvaId > %f )' % 1.5
doubleEle10Fired  = 'DoubleEle10_fired==1' 
doubleEle9p5Fired = 'DoubleEle9p5_fired==1' 
doubleEle9Fired   = 'DoubleEle9_fired==1' 
doubleEle8p5Fired = 'DoubleEle8p5_fired==1' 
doubleEle8Fired   = 'DoubleEle8_fired==1' 
doubleEle7p5Fired = 'DoubleEle7p5_fired==1' 
doubleEle7Fired   = 'DoubleEle7_fired==1' 
doubleEle6p5Fired = 'DoubleEle6p5_fired==1' 
doubleEle6Fired   = 'DoubleEle6_fired==1' 
doubleEle5p5Fired = 'DoubleEle5p5_fired==1' 
doubleEle5Fired   = 'DoubleEle5_fired==1' 
doubleEle4p5Fired = 'DoubleEle4p5_fired==1' 
doubleEle4Fired   = 'DoubleEle4_fired==1' 

doubleEle10ProbeMatched  = 'DoubleEle10_fired==1 & ((JpsiKE_e1_trgobj_pt<0 & JpsiKE_e1_Ele10_match==1) || (JpsiKE_e2_trgobj_pt<0 & JpsiKE_e2_Ele10_match==1) || (JpsiKE_e1_trgobj_pt>0 & JpsiKE_e2_trgobj_pt>0 & JpsiKE_e1_Ele10_match+JpsiKE_e2_Ele10_match>0))'
doubleEle10BothMatched = 'DoubleEle10_fired==1 && (  JpsiKE_e1_Ele10_match==1 && JpsiKE_e2_Ele10_match==1 )'

doubleEle9p5ProbeMatched  = 'DoubleEle9p5_fired==1 && ( (JpsiKE_e1_trgobj_pt<0 && JpsiKE_e1_Ele9p5_match==1) || (JpsiKE_e2_trgobj_pt<0 && JpsiKE_e2_Ele9p5_match==1)|| (JpsiKE_e1_trgobj_pt>0 & JpsiKE_e2_trgobj_pt>0 & JpsiKE_e1_Ele9p5_match+JpsiKE_e2_Ele9p5_match>0))'
doubleEle9p5BothMatched = 'DoubleEle9p5_fired==1 && (  JpsiKE_e1_Ele9p5_match==1 && JpsiKE_e2_Ele9p5_match==1 )'

doubleEle9ProbeMatched  = 'DoubleEle9_fired==1 && ( (JpsiKE_e1_trgobj_pt<0 && JpsiKE_e1_Ele9_match==1) || (JpsiKE_e2_trgobj_pt<0 && JpsiKE_e2_Ele9_match==1)|| (JpsiKE_e1_trgobj_pt>0 & JpsiKE_e2_trgobj_pt>0 & JpsiKE_e1_Ele9_match+JpsiKE_e2_Ele9_match>0))'
doubleEle9BothMatched = 'DoubleEle9_fired==1 && (  JpsiKE_e1_Ele9_match==1 && JpsiKE_e2_Ele9_match==1 )'

doubleEle8p5ProbeMatched  = 'DoubleEle8p5_fired==1 && ( (JpsiKE_e1_trgobj_pt<0 && JpsiKE_e1_Ele8p5_match==1) || (JpsiKE_e2_trgobj_pt<0 && JpsiKE_e2_Ele8p5_match==1)|| (JpsiKE_e1_trgobj_pt>0 & JpsiKE_e2_trgobj_pt>0 & JpsiKE_e1_Ele8p5_match+JpsiKE_e2_Ele8p5_match>0))'
doubleEle8p5BothMatched = 'DoubleEle8p5_fired==1 && (  JpsiKE_e1_Ele8p5_match==1 && JpsiKE_e2_Ele8p5_match==1 )'

doubleEle8ProbeMatched  = 'DoubleEle8_fired==1 && ( (JpsiKE_e1_trgobj_pt<0 && JpsiKE_e1_Ele8_match==1) || (JpsiKE_e2_trgobj_pt<0 && JpsiKE_e2_Ele8_match==1)|| (JpsiKE_e1_trgobj_pt>0 & JpsiKE_e2_trgobj_pt>0 & JpsiKE_e1_Ele8_match+JpsiKE_e2_Ele8_match>0))'
doubleEle8BothMatched = 'DoubleEle8_fired==1 && (  JpsiKE_e1_Ele8_match==1 && JpsiKE_e2_Ele8_match==1 )'

doubleEle7p5ProbeMatched  = 'DoubleEle7p5_fired==1 && ( (JpsiKE_e1_trgobj_pt<0 && JpsiKE_e1_Ele7p5_match==1) || (JpsiKE_e2_trgobj_pt<0 && JpsiKE_e2_Ele7p5_match==1)|| (JpsiKE_e1_trgobj_pt>0 & JpsiKE_e2_trgobj_pt>0 & JpsiKE_e1_Ele7p5_match+JpsiKE_e2_Ele7p5_match>0))'
doubleEle7p5BothMatched = 'DoubleEle7p5_fired==1 && (  JpsiKE_e1_Ele7p5_match==1 && JpsiKE_e2_Ele7p5_match==1 )'

doubleEle7ProbeMatched  = 'DoubleEle7_fired==1 && ( (JpsiKE_e1_trgobj_pt<0 && JpsiKE_e1_Ele7_match==1) || (JpsiKE_e2_trgobj_pt<0 && JpsiKE_e2_Ele7_match==1)|| (JpsiKE_e1_trgobj_pt>0 & JpsiKE_e2_trgobj_pt>0 & JpsiKE_e1_Ele7_match+JpsiKE_e2_Ele7_match>0))'
doubleEle7BothMatched = 'DoubleEle7_fired==1 && (  JpsiKE_e1_Ele7_match==1 && JpsiKE_e2_Ele7_match==1 )'

doubleEle6p5ProbeMatched  = 'DoubleEle6p5_fired==1 && ( (JpsiKE_e1_trgobj_pt<0 && JpsiKE_e1_Ele6p5_match==1) || (JpsiKE_e2_trgobj_pt<0 && JpsiKE_e2_Ele6p5_match==1)|| (JpsiKE_e1_trgobj_pt>0 & JpsiKE_e2_trgobj_pt>0 & JpsiKE_e1_Ele6p5_match+JpsiKE_e2_Ele6p5_match>0))'
doubleEle6p5BothMatched = 'DoubleEle6p5_fired==1 && (  JpsiKE_e1_Ele6p5_match==1 && JpsiKE_e2_Ele6p5_match==1 )'

doubleEle6ProbeMatched  = 'DoubleEle6_fired==1 && ( (JpsiKE_e1_trgobj_pt<0 && JpsiKE_e1_Ele6_match==1) || (JpsiKE_e2_trgobj_pt<0 && JpsiKE_e2_Ele6_match==1)|| (JpsiKE_e1_trgobj_pt>0 & JpsiKE_e2_trgobj_pt>0 & JpsiKE_e1_Ele6_match+JpsiKE_e2_Ele6_match>0))'
doubleEle6BothMatched = 'DoubleEle6_fired==1 && (  JpsiKE_e1_Ele6_match==1 && JpsiKE_e2_Ele6_match==1 )'

doubleEle5p5ProbeMatched  = 'DoubleEle5p5_fired==1 && ( (JpsiKE_e1_trgobj_pt<0 && JpsiKE_e1_Ele5p5_match==1) || (JpsiKE_e2_trgobj_pt<0 && JpsiKE_e2_Ele5p5_match==1)|| (JpsiKE_e1_trgobj_pt>0 & JpsiKE_e2_trgobj_pt>0 & JpsiKE_e1_Ele5p5_match+JpsiKE_e2_Ele5p5_match>0))'
doubleEle5p5BothMatched = 'DoubleEle5p5_fired==1 && (  JpsiKE_e1_Ele5p5_match==1 && JpsiKE_e2_Ele5p5_match==1 )'

doubleEle5ProbeMatched  = 'DoubleEle5_fired==1 && ( (JpsiKE_e1_trgobj_pt<0 && JpsiKE_e1_Ele5_match==1) || (JpsiKE_e2_trgobj_pt<0 && JpsiKE_e2_Ele5_match==1)|| (JpsiKE_e1_trgobj_pt>0 & JpsiKE_e2_trgobj_pt>0 & JpsiKE_e1_Ele5_match+JpsiKE_e2_Ele5_match>0))'
doubleEle5BothMatched = 'DoubleEle5_fired==1 && (  JpsiKE_e1_Ele5_match==1 && JpsiKE_e2_Ele5_match==1 )'

doubleEle4p5ProbeMatched  = 'DoubleEle4p5_fired==1 && ( (JpsiKE_e1_trgobj_pt<0 && JpsiKE_e1_Ele4p5_match==1) || (JpsiKE_e2_trgobj_pt<0 && JpsiKE_e2_Ele4p5_match==1)|| (JpsiKE_e1_trgobj_pt>0 & JpsiKE_e2_trgobj_pt>0 & JpsiKE_e1_Ele4p5_match+JpsiKE_e2_Ele4p5_match>0))'
doubleEle4p5BothMatched = 'DoubleEle4p5_fired==1 && (  JpsiKE_e1_Ele4p5_match==1 && JpsiKE_e2_Ele4p5_match==1 )'

doubleEle4ProbeMatched  = 'DoubleEle4_fired==1 && ( (JpsiKE_e1_trgobj_pt<0 && JpsiKE_e1_Ele4_match==1) || (JpsiKE_e2_trgobj_pt<0 && JpsiKE_e2_Ele4_match==1)|| (JpsiKE_e1_trgobj_pt>0 & JpsiKE_e2_trgobj_pt>0 & JpsiKE_e1_Ele4_match+JpsiKE_e2_Ele4_match>0))'
doubleEle4BothMatched = 'DoubleEle4_fired==1 && (  JpsiKE_e1_Ele4_match==1 && JpsiKE_e2_Ele4_match==1 )'

# flag to be Tested
flags = {
    'passingIdLPEB'  : idbdtlppassEB,
    'passingIdLPEE'  : idbdtlppassEE,
    'doubleEle10Fired' : doubleEle10Fired,
    'doubleEle9p5Fired': doubleEle9p5Fired,
    'doubleEle9Fired'  : doubleEle9Fired,
    'doubleEle8p5Fired': doubleEle8p5Fired,
    'doubleEle8Fired'  : doubleEle8Fired,
    'doubleEle7p5Fired': doubleEle7p5Fired,
    'doubleEle7Fired'  : doubleEle7Fired,
    'doubleEle6p5Fired': doubleEle6p5Fired,
    'doubleEle6Fired'  : doubleEle6Fired,
    'doubleEle5p5Fired': doubleEle5p5Fired,
    'doubleEle5Fired'  : doubleEle5Fired,
    'doubleEle4p5Fired': doubleEle4p5Fired,
    'doubleEle4Fired'  : doubleEle4Fired,

    'doubleEle10ProbeMatched' : doubleEle10ProbeMatched,
    'doubleEle10BothMatched': doubleEle10BothMatched,

    'doubleEle9p5ProbeMatched' : doubleEle9p5ProbeMatched,
    'doubleEle9p5BothMatched': doubleEle9p5BothMatched,

    'doubleEle9ProbeMatched' : doubleEle9ProbeMatched,
    'doubleEle9BothMatched': doubleEle9BothMatched,

    'doubleEle8p5ProbeMatched' : doubleEle8p5ProbeMatched,
    'doubleEle8p5BothMatched': doubleEle8p5BothMatched,

    'doubleEle8ProbeMatched' : doubleEle8ProbeMatched,
    'doubleEle8BothMatched': doubleEle8BothMatched,

    'doubleEle7p5ProbeMatched' : doubleEle7p5ProbeMatched,
    'doubleEle7p5BothMatched': doubleEle7p5BothMatched,

    'doubleEle6p5ProbeMatched' : doubleEle6p5ProbeMatched,
    'doubleEle6p5BothMatched': doubleEle6p5BothMatched,

    'doubleEle6ProbeMatched' : doubleEle6ProbeMatched,
    'doubleEle6BothMatched': doubleEle6BothMatched,

    'doubleEle5p5ProbeMatched' : doubleEle5p5ProbeMatched,
    'doubleEle5p5BothMatched': doubleEle5p5BothMatched,

    'doubleEle5ProbeMatched' : doubleEle5ProbeMatched,
    'doubleEle5BothMatched': doubleEle5BothMatched,

    'doubleEle4p5ProbeMatched' : doubleEle4p5ProbeMatched,
    'doubleEle4p5BothMatched': doubleEle4p5BothMatched,

    'doubleEle4ProbeMatched' : doubleEle4ProbeMatched,
    'doubleEle4BothMatched': doubleEle4BothMatched,
    }
baseOutDir = 'results/doubleEleFired/'

#############################################################
# Samples definition  - preparing the samples

### samples are defined in etc/inputs/tnpSampleDef.py
### not: you can setup another sampleDef File in inputs
import etc.inputs.tnpSampleDef as tnpSamples
tnpTreeDir = 'nano_'

samplesDef = {
    #'data'   : tnpSamples.Parking_Jan16['data_Run2022C-Prompt'].clone(),
    'data'   : tnpSamples.Parking_Jan16['data_Run2022CD-Prompt'].clone(),
    'mcNom'  : tnpSamples.Parking_Jan16['BuToKJpsi'].clone(),
    'mcAlt'  : tnpSamples.Parking_Jan16['BuToKJpsi'].clone(),
    'tagSel' : tnpSamples.Parking_Jan16['BuToKJpsi'].clone(),
}

## if you need to use 2 times the same sample, then rename the second one
# if not samplesDef['mcAlt'] is None:
#     samplesDef['mcAlt'].rename('BuToKJpsi_mcAlt')
# if not samplesDef['tagSel'] is None:
#     samplesDef['tagSel'].rename('BuToKJpsi_tagSel')

## set MC weight
weightName = 'weight'    # 1 for data; pu_weight for MC   
# if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
# if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
# if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_weight(weightName)

#############################################################
# Bining definition  [can be nD bining]
biningDef = [
    # EB
    #{ 'var' : 'probeAbsEta' , 'type': 'float', 'bins': [0, 1.5] },
    #{ 'var' : 'probePt' , 'type': 'float', 'bins': [0.5,1.5,2.0,5.0,20.0] },
    # EE
    # { 'var' : 'probeAbsEta' , 'type': 'float', 'bins': [1.5, 2.5] },
    # { 'var' : 'probePt' , 'type': 'float', 'bins': [0.5,2.0,5.0,20.0] },
    { 'var' : 'JpsiKE_e2_pt', 'type': 'float', 'bins': [3.0, 999.0] },
]

#############################################################
# Cuts definition for all samples
# EB
#cutBase = 'probePt>0.5 && probePt<20 && probeIsLowPt==1 && hlt_9 && probeAbsEta<1.5'
# EE
cutBase = 'JpsiKE_Jpsi_mass>2.2999 && JpsiKE_Jpsi_mass<3.61'

# can add addtionnal cuts for some bins (first check bin number using tnpEGM --checkBins)
#additionalCuts = { 
#    0 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45'
#}

# or remove any additional cut (default)
additionalCuts = None

#############################################################
# Fitting params to tune fit by hand if necessary
tnpParAltSigFitJPsi = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.1,0.01,3.0]",      
    "meanF[-0.0,-0.5,0.5]","sigmaF[0.1,0.01,1.0]",
    "alphaP[0.5, 0.2, 0.8]",
    "alphaF[0.5, 0.2, 0.8]",    
    ]

tnpParNomFitJPsi = [

    # EB with pT 0.5-1.5 
    # with fix sigmaF, meanF, alphaLF, alphaRF, nLF, nRF to those for passing
    # 26 bin, 2.3-3.6
    #"meanP[3.0969, 3.095, 3.098]","sigmaP[0.05, 0.03, 0.1]","alphaLP[0.6, 0.2, 0.7]","alphaRP[1.2, 1.0, 1.5]","nLP[3.6, 3.56, 3.64]","nRP[1.85, 1.80, 1.95]",
    #"meanF[3.0969, 3.09, 3.10]","sigmaF[0.05, 0.03, 0.1]","alphaLF[0.6, 0.2, 0.7]","alphaRF[1.2, 0.8, 1.5]","nLF[3.6, 3.56, 3.64]","nRF[1.85, 1.80, 1.95]",
    #"expalphaP[0.5, 0.2, 0.8]",
    #"expalphaF[0.5, 0.2, 0.8]",   

    # EB with pT 1.5-2 
    # with fix sigmaF=sigmaP  
    # 26 bin, 2.3-3.6  
    #"meanP[3.0969, 3.08, 3.10]","sigmaP[0.05, 0.03, 0.1]","alphaLP[0.6, 0.2, 0.7]","alphaRP[1.2, 1.0, 1.5]","nLP[3.6, 3.56, 3.64]","nRP[1.85, 1.80, 1.95]",
    #"meanF[3.0969, 3.09, 3.10]","sigmaF[0.05, 0.03, 0.1]","alphaLF[0.6, 0.2, 0.7]","alphaRF[1.2, 1.0, 1.5]","nLF[3.6, 3.56, 3.64]","nRF[1.85, 1.80, 1.95]",
    #"expalphaP[0.5, -0.2, 0.8]",
    #"expalphaF[0.5, 0.2, 0.8]",   

    # EB with pT 2-5 and pT>5
    # with fix sigmaF, alphaLF, alphaRF, nLF, nRF to those for passing. NB: meanF free
    # 18 bin, 2.6-3.5   
    # "meanP[3.09, 3.085, 3.095]","sigmaP[0.05, 0.03, 0.1]",  "alphaLP[0.6, 0.2, 0.7]","alphaRP[1.2, 1.0, 1.5]","nLP[3.6, 3.56, 3.64]","nRP[1.80, 1.70, 1.95]",
    # "meanF[3.15, 3.07, 3.2]","sigmaF[0.01, 0.001, 0.03]_","alphaLF[0.6, 0.2, 0.7]","alphaRF[1.2, 1.0, 1.5]","nLF[3.6, 3., 4.]","nRF[1.85, 1.60, 2.05]",
    # "expalphaP[-0.75, -1., -0.5]",
    # "expalphaF[-0.75, -1., -0.5]",       

    # EE with pT<5
    # with fix sigmaF, meanF, alphaLF, alphaRF, nLF, nRF to those for passing
    # 26 bin, 2.3-3.6
    #"meanP[3.0969, 3.095, 3.1]","sigmaP[0.05, 0.03, 0.12]","alphaLP[0.6, 0.2, 0.7]","alphaRP[0.75, 0.4, 1.]","nLP[3.4, 3.3, 3.60]","nRP[1.85, 1.80, 1.95]",
    #"meanF[3.0969, 3.095, 3.098]","sigmaF[0.05, 0.03, 0.1]","alphaLF[0.6, 0.2, 0.7]","alphaRF[1.2, 1.0, 1.5]","nLF[3.6, 3.56, 3.64]","nRF[1.85, 1.80, 1.95]",
    #"expalphaP[0.6, 0.5, 1.]",
    #"expalphaF[0., -0.2, 0.8]",   

    # Gaussian Signal
    "meanP[3.0969, 3.09, 3.11]","sigmaP[0.07, 0.05, 0.1]",
    "meanF[3.1, 3.09, 3.18]","sigmaF[0.03, 0.05, 0.1]",
    "expalphaP[-0.75, -1., 0]",
    "expalphaF[-0.75, -1.0, 0]",   
    
    # EE with pT>5 
    # with fix sigmaF, meanF, alphaLF, alphaRF, nLF, nRF to those for passing
    # 26 bin, 2.3-3.6
    # "meanP[3.0969, 3.09, 3.11]","sigmaP[0.05, 0.03, 0.08]",  "alphaLP[0.6, 0.2, 0.95]","alphaRP[1.2, 0.5, 1.5]","nLP[3.6, 3.56, 3.64]","nRP[1.85, 1.80, 1.95]",
    # "meanF[3.2, 3.09, 3.3]","sigmaF[0.03, 0.03, 0.08]","alphaLF[0.6, 0.2, 0.7]","alphaRF[1.2, 0.8, 1.5]","nLF[3.6, 3.0, 3.8]","nRF[1.85, 1.60, 2.05]",
    # "expalphaP[-0.75, -1., 0]",
    # "expalphaF[-0.75, -1.0, 0]",   
    #"shiftF[0,3.]", 
    #"betaF[0.,10.]", 
    #"c0[0.,0.]", 
]
     
tnpParAltBkgFitJPsi = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.1,0.01,3.0]",      
    "meanF[-0.0,-0.5,0.5]","sigmaF[0.1,0.01,1.0]",
    "cP[0.,-100.,100.]",
    "cF[0.,-100.,500.]",
    ]

