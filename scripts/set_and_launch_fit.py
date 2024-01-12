import os
import sys
import argparse

from ROOT import *

gROOT.SetBatch(True)
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../")

parser = argparse.ArgumentParser(description='Plot global efficiencies for different triggers')
parser.add_argument('-s', '--settings' , dest='settings'  , help = 'input settings file')
parser.add_argument('-o', '--outputdir', dest='outputdir' , help = 'output directory with plots')
parser.add_argument('-f', '--fitonly'  , action='store_true' , help = 'skip bin/hist creation and do fit+plot')
parser.add_argument('-p', '--plotonly' , action='store_true' , help = 'skip bin creation and fit and do only plots')
parser.add_argument('-b', '--bin_idx'  , dest='bin_index' , default=False, help = 're-do the fit for selected bin')

args = parser.parse_args()

flaglist = [
    'probe_fired',
    # 'singleEle_fired',
    # 'doubleEle4BothMatchedL1_4p5_Match',
    # 'doubleEle4BothMatchedL1_5p0_Match',
    # 'doubleEle4BothMatchedL1_5p5_Match',
    # 'doubleEle4BothMatchedL1_6p0_Match',
    # 'doubleEle4p5BothMatchedL1_6p5_Match',
    # 'doubleEle5BothMatchedL1_7p0_Match',
    # 'doubleEle5BothMatchedL1_7p5_Match',
    # 'doubleEle5BothMatchedL1_8p0_Match',
    # 'doubleEle5BothMatchedL1_8p5_Match',
    # 'doubleEle5BothMatchedL1_10p5_Match',
    # 'doubleEle5p5BothMatchedL1_8p5_Match',
    # 'doubleEle6BothMatchedL1_5p5_Match',
    # 'doubleEle6BothMatchedL1_9p0_Match',
    # 'doubleEle6p5BothMatchedL1_10p5_Match',
    # 'doubleEle6p5BothMatchedL1_11p0_Match',
    # 'doubleEle6p5BothMatchedL1_9p5_Match',
]

print '===> settings %s <===' % args.settings
importSetting = 'import %s as tnpConf' % args.settings.replace('/','.').split('.py')[0]
print importSetting
exec(importSetting)

data_tag = tnpConf.samplesDef['data'].name
settings = args.settings
outdir   = tnpConf.baseOutDir.split("/")[-1]
print ''

for flag in flaglist:
    # skip bin/hist creation if fitonly option is selected
    if not args.fitonly and not args.plotonly:
        os.system("python tnpEGM_fitter.py "+settings+" --flag "+flag+" --createBins")
        os.system("python tnpEGM_fitter.py "+settings+" --flag "+flag+" --createHists")

    # skip fit if plotonly option is selected
    if not args.plotonly:
        if args.bin_index:
            os.system("python tnpEGM_fitter.py "+settings+" --flag "+flag+" --doFit --iBin "+args.bin_index)
        else:
            os.system("python tnpEGM_fitter.py "+settings+" --flag "+flag+" --doFit")

    os.system("mkdir -p /afs/cern.ch/user/c/cquarant/www/DoubleEleTriggerStudy/tnpPlots_2022_final/"+outdir+"/"+flag)
    os.system("cp /afs/cern.ch/user/c/cquarant/www/index.php /afs/cern.ch/user/c/cquarant/www/DoubleEleTriggerStudy/tnpPlots_2022_final/"+outdir)
    os.system("cp /afs/cern.ch/user/c/cquarant/www/index.php /afs/cern.ch/user/c/cquarant/www/DoubleEleTriggerStudy/tnpPlots_2022_final/"+outdir+"/"+flag)
    os.system("cp results/"+outdir+"/"+flag+"/plots/"+data_tag+"/nominalFit/bin*.png /afs/cern.ch/user/c/cquarant/www/DoubleEleTriggerStudy/tnpPlots_2022_final/"+outdir+"/"+flag)

    # evaluate full doubleEle trigger efficiency if ref trigger efficiency file is provided
    if len(tnpConf.biningDef)==1:
        os.system("python scripts/plot_differential_eff.py -i results/"+outdir+"/"+flag+"/"+data_tag+"_"+flag+".nominalFit.root -v "+tnpConf.biningDef[0]['var'])
        if hasattr(tnpConf, 'refEffFile'):
            os.system("python scripts/plot_full_doubleEleEff.py -i results/"+outdir+"/"+flag+"/"+data_tag+"_"+flag+".nominalFit.root -r "+tnpConf.refEffFile+" -v "+tnpConf.biningDef[0]['var'])
        if hasattr(tnpConf, 'sfFile'):
            print("python scripts/plot_full_doubleEleEff_fromSF.py -i results/"+outdir+"/"+flag+"/"+data_tag+"_"+flag+".nominalFit.root -f "+flag+" -r "+tnpConf.sfFile+" -v "+tnpConf.biningDef[0]['var'])
            os.system("python scripts/plot_full_doubleEleEff_fromSF.py -i results/"+outdir+"/"+flag+"/"+data_tag+"_"+flag+".nominalFit.root -f "+flag+" -r "+tnpConf.sfFile+" -v "+tnpConf.biningDef[0]['var'])
    elif hasattr(tnpConf, 'refEffFile'):
        os.system("python scripts/plot_2D_eff.py -i results/"+outdir+"/"+flag+"/"+data_tag+"_"+flag+".nominalFit.root -r "+tnpConf.refEffFile)
    else:
        os.system("python scripts/plot_2D_eff.py -i results/"+outdir+"/"+flag+"/"+data_tag+"_"+flag+".nominalFit.root")