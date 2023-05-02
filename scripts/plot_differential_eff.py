import argparse
import os
import array as ar
from ROOT import *

gROOT.SetBatch(True)
gStyle.SetOptStat(0)
parser = argparse.ArgumentParser(description='Plot global efficiencies for different triggers')
parser.add_argument('-i', '--fitResultsFile', dest='fitResultsFile'  , help = 'input directory with tnp fit results')
parser.add_argument('-v', '--var'           , dest='var'       , help = 'common trigger tag (ex. Fired or ProbeMatched')
#parser.add_argument('-o', '--outputdir', dest='outputdir' , help = 'output directory with plot')

args = parser.parse_args()

varConfig = {
    'nvtx'         : { 'minvalue':00, 'maxvalue':70 , 'axis_label':'N_{vtx}' },
    'JpsiKE_e2_pt' : { 'minvalue':05, 'maxvalue':20 , 'axis_label':'Probe Pt [GeV]' },
    'JpsiKE_e2_eta': { 'minvalue':-1.22, 'maxvalue':1.22 , 'axis_label':'Probe Eta' },
    'JpsiKE_elesDr': { 'minvalue':00, 'maxvalue':0.9, 'axis_label':'#DeltaR(e_{1},e_{2})' },
}
var = varConfig[args.var]

fitResultsFileName = args.fitResultsFile

inputdir  = fitResultsFileName.replace(args.fitResultsFile.split("/")[-1], '')
fitResultsFile = TFile.Open(fitResultsFileName)

inputHistoFileName = fitResultsFileName.replace("nominalFit.","")
inputHistoFile = TFile.Open(inputHistoFileName)

tag = args.fitResultsFile.split("/")[-2]
outdir = args.fitResultsFile.split("/")[-3]
resPlist = []
resFlist = []
binedges = []
for obj in fitResultsFile.GetListOfKeys():
    objname = obj.GetName()
    if "bin" in objname:
        if "resP" in objname:
            resPlist.append(objname)
            for string in objname.split("_"):
                if "To" in string:
                    bin_min_edge = float( string.split("To")[0].replace("p",".").replace("m","-") )
            binedges.append(bin_min_edge)
        if "resF" in objname:
            resFlist.append(objname)
binedges.append(var['maxvalue'])

binedges.sort()
resPlist.sort()
resFlist.sort()

print binedges
print resPlist
print resFlist

binedges_ar = ar.array('f',binedges)
print binedges_ar 
htrig = TH1F("htrig", "htrig", len(binedges)-1, binedges_ar)
htot  = TH1F("htot" , "htot" , len(binedges)-1, binedges_ar)

nEvtAllBins = 0
for ibin in range(len(resPlist)):

    # Get number of signal events from fit for Pass and Fail categories for each bin
    FitResultPass = fitResultsFile.Get(resPlist[ibin])
    FitResultFail = fitResultsFile.Get(resFlist[ibin])

    nSigP = FitResultPass.floatParsFinal().find("nSigP").getVal()                                                                                            
    nSigP_err = FitResultPass.floatParsFinal().find("nSigP").getError()

    nSigF = FitResultFail.floatParsFinal().find("nSigF").getVal()
    nSigF_err = FitResultFail.floatParsFinal().find("nSigF").getError()

    nSigTot = nSigP+nSigF
    nSigTot_err = TMath.Sqrt( TMath.Power(nSigP_err, 2) + TMath.Power(nSigF_err, 2) )
    print nSigP, nSigTot, nSigP/nSigTot, nSigP_err, nSigTot_err
    
    # if nSigP_err > 3*nSigP:
    #     nSigP_err=nSigP*0.5
    # if nSigTot_err > 3*nSigTot:
    #     nSigTot_err=nSigTot*0.3

    # Add number of events (prefit) in ibin to total number of events
    inputHistoPass = inputHistoFile.Get(resPlist[ibin].replace("resP","Pass"))
    inputHistoFail = inputHistoFile.Get(resFlist[ibin].replace("resF","Fail"))

    print resPlist[ibin].replace("resP","Pass"), inputHistoPass.GetName()
    nEvtAllBins += inputHistoPass.GetEntries() + inputHistoFail.GetEntries()
    print nEvtAllBins

    if inputHistoPass.GetEntries() + inputHistoFail.GetEntries() < 50:
        continue

    htrig.SetBinContent(ibin+1, nSigP)
    htrig.SetBinError( ibin+1, nSigP_err)
    
    htot.SetBinContent(ibin+1, nSigP+nSigF)
    htot.SetBinError(ibin+1, nSigTot_err)

heff = TEfficiency(htrig, htot)
heff.SetStatisticOption(TEfficiency.kFCP);
heff.SetConfidenceLevel(0.68);
heff.SetMarkerStyle(22)
heff.SetMarkerSize(1.2)

hset = TH2F( "hset", "", 100, var['minvalue'],   var['maxvalue'], 100, 0, 1)
hset.GetXaxis().SetTitle(var['axis_label'])
hset.GetXaxis().SetTitleSize( 0.06 )
hset.GetXaxis().SetTitleOffset( 0.75 )
hset.GetXaxis().SetLabelSize( 0.04 )

hset.GetYaxis().SetTitle( "trigger efficiency" )
hset.GetYaxis().SetTitleSize( 0.06 )
hset.GetYaxis().SetTitleOffset( 0.80 )
hset.GetYaxis().SetLabelSize( 0.04 )
hset.GetYaxis().SetRangeUser( 0.0, 1.0 )


canvas = TCanvas("c1","c1")
canvas.cd()

t = TLatex(35,.9,"N_{evt} = "+str(int(nEvtAllBins)));
#t.SetTextAlign(22);
t.SetTextFont(43);
t.SetTextSize(24);

hset.Draw()
#htrig.Draw("SAME")
heff.Draw("SAME")
t.Draw("same");
canvas.SaveAs("/afs/cern.ch/user/c/cquarant/www/DoubleEleTriggerStudy/tnpPlots_2022_final/"+outdir+"/"+tag+"/differential_eff_"+tag+".png")

outrootdir  = inputdir
outrootfilename = inputdir+"/"+"/differential_eff_"+tag+".root"
outrootfile = TFile.Open(outrootfilename, "RECREATE")

outrootfile.cd()
heff.Write()
outrootfile.Write()
outrootfile.Save()
