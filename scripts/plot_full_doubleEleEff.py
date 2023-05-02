import argparse
import os
import array as ar
from ROOT import *

gROOT.SetBatch(True)
gStyle.SetOptStat(0)
parser = argparse.ArgumentParser(description='Plot global efficiencies for different triggers')
parser.add_argument('-i', '--fitResultsFile', dest='fitResultsFile'  , help = 'input file with T&P fit results for doubleEle trigger (probe leg)')
parser.add_argument('-r', '--refEffFile'    , dest='refEffFile'      , help = 'input file with T&P fit results for singleEle ref trigger')
parser.add_argument('-v', '--var'           , dest='var'             , help = 'Variable Name: nvtx, JpsiKE_e2_pt, JpsiKE_elesDr')
#parser.add_argument('-o', '--outputdir', dest='outputdir' , help = 'output directory with plot')

args = parser.parse_args()

varConfig = {
    'nvtx'         : { 'minvalue':00, 'maxvalue':70 , 'axis_label':'N_{vtx}'},
    'JpsiKE_e2_pt' : { 'minvalue':05, 'maxvalue':20 , 'axis_label':'Probe Pt [GeV]'},
    'JpsiKE_e2_eta': { 'minvalue':-2.5, 'maxvalue':2.5 , 'axis_label':'Probe Eta'},
    'JpsiKE_elesDr': { 'minvalue':00, 'maxvalue':0.9, 'axis_label':'#DeltaR(e_{1},e_{2})' },
}
var = varConfig[args.var]

fitResultsFileName = args.fitResultsFile

inputdir  = fitResultsFileName.replace(args.fitResultsFile.split("/")[-1], '')
fitResultsFile = TFile.Open(fitResultsFileName)

inputHistoFileName = fitResultsFileName.replace("nominalFit.","")
inputHistoFile = TFile.Open(inputHistoFileName)

# if !args.refEffFile:
#     print 'File with T&P fit results for singleEle reference trigger required'
#     return
RefEffFile = TFile.Open(args.refEffFile)

tag = args.fitResultsFile.split("/")[-2]
outdir = args.fitResultsFile.split("/")[-3]

# Create list of bin names and edges for doubleEle trigger
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

binedges_ar = ar.array('f',binedges)
#print binedges_ar 

### Create histogram to evaluate doubleEle eff (probe leg) and singleEle eff
htrig_diEleProbe = TH1F("htrig_diEleProbe", "htrig_diEleProbe", len(binedges)-1, binedges_ar)
htot_diEleProbe  = TH1F("htot_diEleProbe" , "htot_diEleProbe" , len(binedges)-1, binedges_ar)

htrig_ref = TH1F("htrig_ref", "htrig_ref", len(binedges)-1, binedges_ar)
htot_ref  = TH1F("htot_ref" , "htot_ref" , len(binedges)-1, binedges_ar)

nEvtAllBins = 0
for ibin in range(len(resPlist)):

    # print ''
    # print ibin
    ### Get Pass/Fail events for doubleEle trigger
    ##  bin-by-bin
    FitResultPass = fitResultsFile.Get(resPlist[ibin])
    FitResultFail = fitResultsFile.Get(resFlist[ibin])

    nSigP     = FitResultPass.floatParsFinal().find("nSigP").getVal()                                                                                            
    nSigP_err = FitResultPass.floatParsFinal().find("nSigP").getError()

    nSigF     = FitResultFail.floatParsFinal().find("nSigF").getVal()
    nSigF_err = FitResultFail.floatParsFinal().find("nSigF").getError()

    nSigTot     = nSigP+nSigF
    nSigTot_err = TMath.Sqrt( TMath.Power(nSigP_err, 2) + TMath.Power(nSigF_err, 2) )
    # print "nSigP, nSigTot, nSigP/nSigTot, nSigP_err, nSigTot_err"
    # print nSigP, nSigTot, nSigP/nSigTot, nSigP_err, nSigTot_err
    
    # check if number of events in data is enough to evaluate efficiency (~100 evt)
    inputHistoPass = inputHistoFile.Get(resPlist[ibin].replace("resP","Pass"))
    inputHistoFail = inputHistoFile.Get(resFlist[ibin].replace("resF","Fail"))
    EvtBins = inputHistoPass.GetEntries() + inputHistoFail.GetEntries()
    
    if EvtBins < 50:
        continue

    # Num e den of double ele probe leg efficiency
    htrig_diEleProbe.SetBinContent(ibin+1, nSigP)
    htrig_diEleProbe.SetBinError  (ibin+1, nSigP_err)

    htot_diEleProbe.SetBinContent(ibin+1, nSigTot)
    htot_diEleProbe.SetBinError  (ibin+1, nSigTot_err)

# Evaluate doubleEle (probe leg) efficiency
heff_diEleProbe = TEfficiency(htrig_diEleProbe, htot_diEleProbe)
heff_diEleProbe.SetStatisticOption(TEfficiency.kFCP);
heff_diEleProbe.SetConfidenceLevel(0.68);
geff_diEleProbe = heff_diEleProbe.CreateGraph()


npoints = geff_diEleProbe.GetN()
geff_diEle = TGraphErrors(npoints)
x_diEleProbe  = ar.array('d', [0.])
y_diEleProbe  = ar.array('d', [0.])
x_ref        = ar.array('d', [0.])
y_ref        = ar.array('d', [0.])
#print ''
geff_ref = RefEffFile.Get("htot_clone").CreateGraph()
for i in range(npoints):

    geff_diEleProbe.GetPoint(i, x_diEleProbe, y_diEleProbe)
    geff_ref.GetPoint(i, x_ref, y_ref)
    ey_diEleProbe = geff_diEleProbe.GetErrorY(i)
    ex_diEleProbe = geff_diEleProbe.GetErrorX(i)
    ey_ref        = geff_ref       .GetErrorY(i)

    #print x_diEleProbe, y_diEleProbe, x_ref, y_ref

    e_diEleProbe = y_diEleProbe[0]
    e2_ref       = y_ref[0]
    e1_ref       = e2_ref

    e_ref_e1e2     = 1 - ( (1-e1_ref) * (1-e2_ref)  ) # eff of singleEle ref trigger is assumed 0.84 for e_tag with pt>11.0
    e_ref_e1e2_err = 2 * (1-e2_ref) * ey_ref

    eff_diEle = e_diEleProbe * e_ref_e1e2
    eff_diEle_err = eff_diEle * TMath.Sqrt( TMath.Power(ey_diEleProbe/e_diEleProbe, 2) + TMath.Power(e_ref_e1e2_err/e_ref_e1e2, 2) )

    geff_diEle.SetPoint(i, x_diEleProbe[0], eff_diEle)
    geff_diEle.SetPointError(i, ex_diEleProbe, eff_diEle_err)

 #   print ''

geff_diEle.SetMarkerStyle(22)
geff_diEle.SetMarkerSize(1.2)

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

hset.Draw()
#htrig.Draw("SAME")
geff_diEle.Draw("PSAME")
canvas.SaveAs("/afs/cern.ch/user/c/cquarant/www/DoubleEleTriggerStudy/tnpPlots_2022_final/"+outdir+"/"+tag+"/FullDoubleEleEff_"+tag+".png")

outrootdir  = inputdir
outrootfilename = inputdir+"/"+"/FullDoubleEleEff_"+tag+".root"
outrootfile = TFile.Open(outrootfilename, "RECREATE")

outrootfile.cd()
geff_diEle.Write()
outrootfile.Write()
outrootfile.Save()
