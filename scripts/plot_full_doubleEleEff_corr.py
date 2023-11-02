import argparse
import os
import array as ar
from ROOT import *

gROOT.SetBatch(True)
gStyle.SetOptStat(0)
parser = argparse.ArgumentParser(description='Plot global efficiencies for different triggers')
parser.add_argument('-i', '--fitResultsFile', dest='fitResultsFile'  , help = 'input file with T&P fit results for doubleEle trigger (probe leg)')
parser.add_argument('-r', '--refEffFile'    , dest='refEffFile'      , help = 'input file with T&P fit results for singleEle ref trigger')
parser.add_argument('-s', '--singleEleEff_DoubleEleRef'   , dest='singleEleRef_DoubleEleRef' , help = 'input file with singleEle trigger efficiency using DoubleEleX as reference')
parser.add_argument('-z', '--singleEleEff_DoubleEleRef_nobins'   , dest='singleEleRef_DoubleEleRef_nobins' , help = 'input file with singleEle trigger efficiency using DoubleEleX as reference for e1')
parser.add_argument('-v', '--var'           , dest='var'             , help = 'Variable Name: nvtx, JpsiKE_e2_pt, JpsiKE_elesDr')
#parser.add_argument('-o', '--outputdir', dest='outputdir' , help = 'output directory with plot')

args = parser.parse_args()

varConfig = {
    'nvtx'         : { 'minvalue':00, 'maxvalue':70 , 'axis_label':'N_{vtx}'},
    'JpsiKE_e2_pt' : { 'minvalue':05, 'maxvalue':20 , 'axis_label':'Probe Pt [GeV]'},
    'JpsiKE_e2_eta': { 'minvalue':-1.22, 'maxvalue':1.22 , 'axis_label':'Probe Eta'},
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
SingleEleEff_DoubleEleRef_File = TFile.Open(args.singleEleRef_DoubleEleRef)
SingleEleEff_DoubleEleRef_File_nobins = TFile.Open(args.singleEleRef_DoubleEleRef_nobins)

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

#print ''
geff_ref = RefEffFile.Get("htot_clone").CreateGraph()
geff_singleEleEff_doubleEleRef = SingleEleEff_DoubleEleRef_File.Get("htot_clone").CreateGraph()
geff_singleEleEff_doubleEleRef_nobins = SingleEleEff_DoubleEleRef_File_nobins.Get("htot_clone").CreateGraph()
for i in range(npoints):

    x_diEleProbe  = ar.array('d', [0.])
    y_diEleProbe  = ar.array('d', [0.])
    x_ref        = ar.array('d', [0.])
    y_ref        = ar.array('d', [0.])
    x_singleEleEff_doubleEleRef = ar.array('d', [0.])
    y_singleEleEff_doubleEleRef = ar.array('d', [-1.])
    x_singleEleEff_doubleEleRef_nobins = ar.array('d', [0.])
    y_singleEleEff_doubleEleRef_nobins = ar.array('d', [0.])    
    ex_diEleProbe_ = 0.
    ey_diEleProbe_ = 0.
    
    geff_diEleProbe.GetPoint(i, x_diEleProbe, y_diEleProbe)
    ey_diEleProbe_ = geff_diEleProbe.GetErrorY(i)
    ex_diEleProbe_ = geff_diEleProbe.GetErrorX(i)
    
    x_tmp  = ar.array('d', [0.])
    y_tmp  = ar.array('d', [0.])
    ey_ref_ = 0.
    for j in range(npoints):
        geff_ref.GetPoint(j, x_tmp, y_tmp)
        print('x_tmp= ', x_tmp[0])
        print('x_diEleProbe= ', x_diEleProbe[0])
        if x_tmp[0] == x_diEleProbe[0]:
            geff_ref.GetPoint(j, x_ref, y_ref)
            ey_ref_ = geff_ref.GetErrorY(j)


    x_tmp  = ar.array('d', [0.])
    y_tmp  = ar.array('d', [0.])
    ey_singleEleEff_doubleEleRef = 0.
    for j in range(npoints):
        geff_singleEleEff_doubleEleRef.GetPoint(j, x_tmp, y_tmp)
        if x_tmp[0] == x_diEleProbe[0]:
            geff_singleEleEff_doubleEleRef.GetPoint(j, x_singleEleEff_doubleEleRef, y_singleEleEff_doubleEleRef)
            ey_singleEleEff_doubleEleRef = geff_singleEleEff_doubleEleRef.GetErrorY(j)
            break
    
    geff_singleEleEff_doubleEleRef_nobins.GetPoint(0, x_singleEleEff_doubleEleRef_nobins, y_singleEleEff_doubleEleRef_nobins)
    ey_singleEleEff_doubleEleRef_nobins = geff_singleEleEff_doubleEleRef_nobins.GetErrorY(0)

    print x_diEleProbe[0], y_diEleProbe[0], x_ref[0], y_ref[0], x_singleEleEff_doubleEleRef[0], y_singleEleEff_doubleEleRef[0]
    print ey_diEleProbe_, ey_ref_, ey_singleEleEff_doubleEleRef, ey_singleEleEff_doubleEleRef_nobins

    e_diEleProbe = y_diEleProbe[0]
    e2_ref       = y_ref[0]
    # e1_ref       = 0.44 # Tag Pt
    e1_ref       = 0.3966 # Tag Eta 
    
    e1_singleEleEff_doubleEleRef = y_singleEleEff_doubleEleRef_nobins[0]
    e2_singleEleEff_doubleEleRef_ = y_singleEleEff_doubleEleRef[0]

    e_ref_e1e2     = 1 - ( (1-e1_ref) * (1-e2_ref)  )
    e_ref_e1e2_err = (1-e2_ref) * ey_ref_

    e_singleEleEff_doubleEleRef = 1 - ( (1-e1_singleEleEff_doubleEleRef) * (1-e2_singleEleEff_doubleEleRef_) )
    e_singleEleEff_doubleEleRef_err = TMath.Sqrt( (1-e1_singleEleEff_doubleEleRef)*ey_singleEleEff_doubleEleRef*(1-e1_singleEleEff_doubleEleRef)*ey_singleEleEff_doubleEleRef + (1-e2_singleEleEff_doubleEleRef_)*ey_singleEleEff_doubleEleRef_nobins*(1-e2_singleEleEff_doubleEleRef_)*ey_singleEleEff_doubleEleRef_nobins )

    eff_diEle = e_diEleProbe * e_ref_e1e2 / e_singleEleEff_doubleEleRef
    
    if y_singleEleEff_doubleEleRef[0] != -1. :
        eff_diEle = e_diEleProbe * e_ref_e1e2 / e_singleEleEff_doubleEleRef
        eff_diEle_err = eff_diEle * TMath.Sqrt( TMath.Power(ey_diEleProbe_/e_diEleProbe, 2) + TMath.Power(e_ref_e1e2_err/e_ref_e1e2, 2) + TMath.Power(e_singleEleEff_doubleEleRef_err/e_singleEleEff_doubleEleRef, 2))
    else:
        eff_diEle = -1
        eff_diEle_err = 0

    print(i)
    print('e1_ref= ', e1_ref)
    print('e2_ref= ', e2_ref)
    print('e_ref_e1e2= ', e_ref_e1e2)
    print('e1_singleEleEff_doubleEleRef= ', e1_singleEleEff_doubleEleRef)
    print('e2_singleEleEff_doubleEleRef= ', e2_singleEleEff_doubleEleRef_)
    print('e_singleEleEff_doubleEleRef= ' , e_singleEleEff_doubleEleRef )
    print('e_diEleProbe= ', e_diEleProbe)
    print('eff_diEle= ', eff_diEle)
    print('')
    print('e1_singleEleEff_doubleEleRef= ', e1_singleEleEff_doubleEleRef)
    print('ey1_singleEleEff_doubleEleRef= ', ey_singleEleEff_doubleEleRef_nobins)
    print('e2_singleEleEff_doubleEleRef= ', e2_singleEleEff_doubleEleRef_)
    print('ey2_singleEleEff_doubleEleRef= ', ey_singleEleEff_doubleEleRef)
    print('e_singleEleEff_doubleEleRef_err= ', e_singleEleEff_doubleEleRef_err)


    geff_diEle.SetPoint(i, x_diEleProbe[0], eff_diEle)
    geff_diEle.SetPointError(i, ex_diEleProbe_, eff_diEle_err)

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
canvas.SaveAs("/afs/cern.ch/user/c/cquarant/www/DoubleEleTriggerStudy/tnpPlots_2022_final/"+outdir+"/"+tag+"/FullDoubleEleEffCorr_"+tag+".png")

outrootdir  = inputdir
outrootfilename = inputdir+"/"+"/FullDoubleEleEffCorr_"+tag+".root"
outrootfile = TFile.Open(outrootfilename, "RECREATE")

outrootfile.cd()
geff_diEle.Write()
outrootfile.Write()
outrootfile.Save()