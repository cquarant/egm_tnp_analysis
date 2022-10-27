import argparse
import os
from ROOT import *

gROOT.SetBatch(True)
gStyle.SetOptStat(0)
parser = argparse.ArgumentParser(description='Plot global efficiencies for different triggers')
parser.add_argument('-i', '--inputdir' , dest='inputdir'  , help = 'input directory with tnp fit results')
parser.add_argument('-t', '--tag'      , dest='tag'       , help = 'common trigger tag (ex. Fired or ProbeMatched')
#parser.add_argument('-o', '--outputdir', dest='outputdir' , help = 'output directory with plot')

args = parser.parse_args()

#os.system("mkdir -p "+outputdir)
#os.system("cp -r "+outputdir+" /afs/cern.ch/user/c/cquarant/www/DoubleEleTriggerStudy/tnpPlots/")

inputdir = args.inputdir
if inputdir.endswith("/"):
    outputdir = "/afs/cern.ch/user/c/cquarant/www/DoubleEleTriggerStudy/tnpPlots/"+inputdir.split("/")[-2]
else:
    outputdir = "/afs/cern.ch/user/c/cquarant/www/DoubleEleTriggerStudy/tnpPlots/"+inputdir.split("/")[-1]
triggerlist = next(os.walk(inputdir))[1]

htrig = TH1F("htrig", "htrig", 13, -0.5, 12.5)
htot  = TH1F("htot" , "htot" , 13, -0.5, 12.5)

map_trig={
    "doubleEle10" :12,
    "doubleEle9p5":11,
    "doubleEle9"  :10,
    "doubleEle8p5":9,
    "doubleEle8"  :8,
    "doubleEle7p5":7,
    "doubleEle7"  :6,
    "doubleEle6p5":5,
    "doubleEle6"  :4,
    "doubleEle5p5":3,
    "doubleEle5"  :2,
    "doubleEle4p5":1,
    "doubleEle4"  :0
}

for subdir in triggerlist:
    
    if args.tag not in subdir:
        continue
    print subdir, args.tag
    triggername = subdir.replace(args.tag, "")
    print subdir, triggername
    rootfile = TFile.Open(inputdir+"/"+subdir+"/data_Run2022CDEF-Prompt_%s.nominalFit.root" % subdir)
    
    FitResultPassName = rootfile.GetListOfKeys().At(5).GetName()
    FitResultPass = rootfile.Get(FitResultPassName)
    nSigP = FitResultPass.floatParsFinal().find("nSigP").getVal()
    nSigP_err = FitResultPass.floatParsFinal().find("nSigP").getError()

    FitResultFailName = rootfile.GetListOfKeys().At(7).GetName()
    FitResultFail = rootfile.Get(FitResultFailName)
    nSigF = FitResultFail.floatParsFinal().find("nSigF").getVal()
    nSigF_err = FitResultFail.floatParsFinal().find("nSigF").getError()

    nSigTot = nSigP+nSigF
    nSigTot_err = TMath.Sqrt( TMath.Power(nSigP_err, 2) + TMath.Power(nSigF_err, 2) )

    print triggername, nSigP/nSigTot, nSigP_err, nSigF_err, nSigTot_err 

    htrig.SetBinContent(htrig.FindBin(map_trig[triggername]), nSigP)
    htrig.SetBinError( htrig.FindBin(map_trig[triggername]), nSigP_err)

    htot.SetBinContent(htrig.FindBin(map_trig[triggername]), nSigP+nSigF)
    htot.SetBinError(htrig.FindBin(map_trig[triggername]), nSigTot_err)

    print ""

heff = TEfficiency(htrig, htot)
heff.SetStatisticOption(TEfficiency.kFCP);
heff.SetConfidenceLevel(0.68);

hset = TH2F( "hset", "", 13, -0.5, 12.5, 1100, 0, 1.1 )

labels = ["doubleEle4",
          "doubleEle4p5",
          "doubleEle5",
          "doubleEle5p5",
          "doubleEle6",
          "doubleEle6p5",
          "doubleEle7",
          "doubleEle7p5",
          "doubleEle8",
          "doubleEle8p5",
          "doubleEle9",
          "doubleEle9p5",
          "doubleEle10"
]

for ibin in range(hset.GetNbinsX()):
    hset.GetXaxis().SetBinLabel(ibin+1, labels[ibin])
hset.GetXaxis().SetTitleSize( 0.06 )
hset.GetXaxis().SetTitleOffset( 0.9 )
hset.GetXaxis().SetLabelSize( 0.04 )

hset.GetYaxis().SetTitle( "trigger efficiency" )
hset.GetYaxis().SetTitleSize( 0.06 )
hset.GetYaxis().SetTitleOffset( 0.90 )
hset.GetYaxis().SetLabelSize( 0.04 )
hset.GetYaxis().SetRangeUser( 0.0, 0.75 )

canvas = TCanvas("c1","c1")
hset.Draw()
#htrig.Draw("SAME")
heff.Draw("SAME")
canvas.SaveAs(outputdir+"/eff_by_trigger"+args.tag+".png")
