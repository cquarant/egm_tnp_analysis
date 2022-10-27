import os
import sys

# flaglist = ['doubleEle10Fired', 'doubleEle9p5Fired', 'doubleEle9Fired', 'doubleEle8p5Fired', 'doubleEle8Fired', 'doubleEle7p5Fired', 'doubleEle7Fired', 'doubleEle6p5Fired', 'doubleEle6Fired', 'doubleEle5p5Fired', 'doubleEle5Fired', 'doubleEle4p5Fired', 'doubleEle4Fired']

# flaglist = ['doubleEle10ProbeMatched' , 'doubleEle10BothMatched' ,
#             'doubleEle9p5ProbeMatched', 'doubleEle9p5BothMatched',
#             'doubleEle9ProbeMatched'  , 'doubleEle9BothMatched'  ,
#             'doubleEle8p5ProbeMatched', 'doubleEle8p5BothMatched',
#             'doubleEle8ProbeMatched'  , 'doubleEle8BothMatched'  ,
#             'doubleEle7p5ProbeMatched', 'doubleEle7p5BothMatched',
#             'doubleEle7ProbeMatched'  , 'doubleEle7BothMatched'  ,
#             'doubleEle6p5ProbeMatched', 'doubleEle6p5BothMatched',
#             'doubleEle6ProbeMatched'  , 'doubleEle6BothMatched'  ,
#             'doubleEle5p5ProbeMatched', 'doubleEle5p5BothMatched',
#             'doubleEle5ProbeMatched'  , 'doubleEle5BothMatched'  ,
#             'doubleEle4p5ProbeMatched', 'doubleEle4p5BothMatched',
#             'doubleEle4ProbeMatched'  , 'doubleEle4BothMatched'  ,
# ]

flaglist = ['doubleEle10Fired' , 'doubleEle10ProbeMatched' , 'doubleEle10BothMatched' ,
            'doubleEle9p5Fired', 'doubleEle9p5ProbeMatched', 'doubleEle9p5BothMatched',
            'doubleEle9Fired'  , 'doubleEle9ProbeMatched'  , 'doubleEle9BothMatched'  ,
            'doubleEle8p5Fired', 'doubleEle8p5ProbeMatched', 'doubleEle8p5BothMatched',
            'doubleEle8Fired'  , 'doubleEle8ProbeMatched'  , 'doubleEle8BothMatched'  ,
            'doubleEle7p5Fired', 'doubleEle7p5ProbeMatched', 'doubleEle7p5BothMatched',
            'doubleEle7Fired'  , 'doubleEle7ProbeMatched'  , 'doubleEle7BothMatched'  ,
            'doubleEle6p5Fired', 'doubleEle6p5ProbeMatched', 'doubleEle6p5BothMatched',
            'doubleEle6Fired'  , 'doubleEle6ProbeMatched'  , 'doubleEle6BothMatched'  ,
            'doubleEle5p5Fired', 'doubleEle5p5ProbeMatched', 'doubleEle5p5BothMatched',
            'doubleEle5Fired'  , 'doubleEle5ProbeMatched'  , 'doubleEle5BothMatched'  ,
            'doubleEle4p5Fired', 'doubleEle4p5ProbeMatched', 'doubleEle4p5BothMatched',
            'doubleEle4Fired'  , 'doubleEle4ProbeMatched'  , 'doubleEle4BothMatched'  ,
]

# flaglist = ['doubleEle6p5Fired', 
#             'doubleEle6p5ProbeMatched', 
#             'doubleEle6p5BothMatched'
# ]

flaglist = ['doubleEle10Fired']

#data_tag = "data_Run2022CD-Prompt"
#settings = "settings_CD.py"

#data_tag = "data_Run2022EF-Prompt"
#settings = "settings_EF.py"

outdir   = "doubleEleFired_24Oct2022_noEtaCut"
data_tag = "data_Run2022CDEF-Prompt"
settings = "settings_CDEF_noEtaCut.py"

#os.system("cd ~/CMSSW_10_6_29/src/JPsiFit/")

for flag in flaglist:
    os.system("python tnpEGM_fitter.py etc/config/"+settings+" --flag "+flag+" --createBins")
    os.system("python tnpEGM_fitter.py etc/config/"+settings+" --flag "+flag+" --createHists")
    os.system("python tnpEGM_fitter.py etc/config/"+settings+" --flag "+flag+" --doFit")
    os.system("mkdir -p /afs/cern.ch/user/c/cquarant/www/DoubleEleTriggerStudy/tnpPlots/"+outdir+"/"+flag)
    os.system("cp /afs/cern.ch/user/c/cquarant/www/index.php /afs/cern.ch/user/c/cquarant/www/DoubleEleTriggerStudy/tnpPlots/"+outdir)
    os.system("cp /afs/cern.ch/user/c/cquarant/www/index.php /afs/cern.ch/user/c/cquarant/www/DoubleEleTriggerStudy/tnpPlots/"+outdir+"/"+flag)
    os.system("cp results/"+outdir+"/"+flag+"/plots/"+data_tag+"/nominalFit/bin*.png /afs/cern.ch/user/c/cquarant/www/DoubleEleTriggerStudy/tnpPlots/"+outdir+"/"+flag)
