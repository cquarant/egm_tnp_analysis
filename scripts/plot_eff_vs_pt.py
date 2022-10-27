import argparse
import os
import array as ar
from ROOT import *

gROOT.SetBatch(True)
gStyle.SetOptStat(0)
parser = argparse.ArgumentParser(description='Plot global efficiencies for different triggers')
parser.add_argument('-i', '--inputfile' , dest='inputfile'  , help = 'input directory with tnp fit results')
#parser.add_argument('-t', '--tag'      , dest='tag'       , help = 'common trigger tag (ex. Fired or ProbeMatched')
#parser.add_argument('-o', '--outputdir', dest='outputdir' , help = 'output directory with plot')

args = parser.parse_args()

inputfile = TFile.Open(args.inputfile)

tag = args.inputfile.split("/")[-2]
outdir = args.inputfile.split("/")[-3]
resPlist = []
resFlist = []
binedges = []
for obj in inputfile.GetListOfKeys():
    objname = obj.GetName()
    if "bin" in objname:
        if "resP" in objname:
            resPlist.append(inputfile.Get(objname))
            bin_min_edge = float( (objname.split("_")[4]).split("To")[0].replace("p",".") )
            binedges.append(bin_min_edge)
        if "resF" in objname:
            resFlist.append(inputfile.Get(objname))
binedges.append(50.0)

print binedges
print resPlist
print resFlist

binedges_ar = ar.array('f',binedges)
print binedges_ar 
htrig = TH1F("htrig", "htrig", len(binedges)-1, binedges_ar)
htot  = TH1F("htot" , "htot" , len(binedges)-1, binedges_ar)

for ibin in range(len(resPlist)):
    FitResultPass = resPlist[ibin]
    FitResultFail = resFlist[ibin]

    nSigP = FitResultPass.floatParsFinal().find("nSigP").getVal()                                                                                            
    nSigP_err = FitResultPass.floatParsFinal().find("nSigP").getError()

    nSigF = FitResultFail.floatParsFinal().find("nSigF").getVal()
    nSigF_err = FitResultFail.floatParsFinal().find("nSigF").getError()

    nSigTot = nSigP+nSigF
    nSigTot_err = TMath.Sqrt( TMath.Power(nSigP_err, 2) + TMath.Power(nSigF_err, 2) )
    print nSigP, nSigTot, nSigP/nSigTot, nSigP_err, nSigTot_err
    
    if nSigP_err > 10000:
        nSigP_err=nSigP*0.5
    if nSigTot_err > 10000:
        nSigTot_err=nSigTot*0.3


    htrig.SetBinContent(ibin+1, nSigP)
    htrig.SetBinError( ibin+1, nSigP_err)
    
    htot.SetBinContent(ibin+1, nSigP+nSigF)
    htot.SetBinError(ibin+1, nSigTot_err)


heff = TEfficiency(htrig, htot)
heff.SetStatisticOption(TEfficiency.kFCP);
heff.SetConfidenceLevel(0.68);
heff.SetMarkerStyle(22)
heff.SetMarkerSize(1.2)
hset = TH2F( "hset", "", 100, 3, 50, 100, 0, 1)

hset.GetXaxis().SetTitle("Probe Pt [GeV]")
hset.GetXaxis().SetTitleSize( 0.06 )
hset.GetXaxis().SetTitleOffset( 0.9 )
hset.GetXaxis().SetLabelSize( 0.04 )

hset.GetYaxis().SetTitle( "trigger efficiency" )
hset.GetYaxis().SetTitleSize( 0.06 )
hset.GetYaxis().SetTitleOffset( 0.90 )
hset.GetYaxis().SetLabelSize( 0.04 )
hset.GetYaxis().SetRangeUser( 0.0, 1.0 )

canvas = TCanvas("c1","c1")
hset.Draw()
#htrig.Draw("SAME")
heff.Draw("SAME")
canvas.SaveAs("/afs/cern.ch/user/c/cquarant/www/DoubleEleTriggerStudy/tnpPlots/"+outdir+"/eff_vs_probe_pt_"+tag+".png")

# for subdir in triggerlist:
    
#     if args.tag not in subdir:
#         continue
#     print subdir, args.tag
#     triggername = subdir.replace(args.tag, "")
#     print subdir, triggername
#     rootfile = TFile.Open(inputfile+"/"+subdir+"/data_Run2022CDEF-Prompt_%s.nominalFit.root" % subdir)
    
#     FitResultPassName = rootfile.GetListOfKeys().At(1).GetName()
#     FitResultPass = rootfile.Get(FitResultPassName)
#     nSigP = FitResultPass.floatParsFinal().find("nSigP").getVal()
#     nSigP_err = FitResultPass.floatParsFinal().find("nSigP").getError()

#     FitResultFailName = rootfile.GetListOfKeys().At(3).GetName()
#     FitResultFail = rootfile.Get(FitResultFailName)
#     nSigF = FitResultFail.floatParsFinal().find("nSigF").getVal()
#     nSigF_err = FitResultFail.floatParsFinal().find("nSigF").getError()

#     nSigTot = nSigP+nSigF
#     nSigTot_err = TMath.Sqrt( TMath.Power(nSigP_err, 2) + TMath.Power(nSigF_err, 2) )

#     print triggername, nSigP/nSigTot, nSigP_err, nSigF_err, nSigTot_err 

#     htrig.SetBinContent(htrig.FindBin(map_trig[triggername]), nSigP)
#     htrig.SetBinError( htrig.FindBin(map_trig[triggername]), nSigP_err)

#     htot.SetBinContent(htrig.FindBin(map_trig[triggername]), nSigP+nSigF)
#     htot.SetBinError(htrig.FindBin(map_trig[triggername]), nSigTot_err)

#     print ""

# heff = TEfficiency(htrig, htot)

# hset = TH2F( "hset", "", 13, -0.5, 12.5, 1100, 0, 1.1 )

# labels = ["doubleEle4",
#           "doubleEle4p5",
#           "doubleEle5",
#           "doubleEle5p5",
#           "doubleEle6",
#           "doubleEle6p5",
#           "doubleEle7",
#           "doubleEle7p5",
#           "doubleEle8",
#           "doubleEle8p5",
#           "doubleEle9",
#           "doubleEle9p5",
#           "doubleEle10"
# ]

# for ibin in range(hset.GetNbinsX()):
#     hset.GetXaxis().SetBinLabel(ibin+1, labels[ibin])
# hset.GetXaxis().SetTitleSize( 0.06 )
# hset.GetXaxis().SetTitleOffset( 0.9 )
# hset.GetXaxis().SetLabelSize( 0.04 )

# hset.GetYaxis().SetTitle( "trigger efficiency" )
# hset.GetYaxis().SetTitleSize( 0.06 )
# hset.GetYaxis().SetTitleOffset( 0.90 )
# hset.GetYaxis().SetLabelSize( 0.04 )
# hset.GetYaxis().SetRangeUser( 0.0, 0.25 )

# canvas = TCanvas("c1","c1")
# hset.Draw()
# #htrig.Draw("SAME")
# heff.Draw("SAME")
# canvas.SaveAs("test.png")
