import argparse
import os
import array as ar
from ROOT import *
import re

DEBUG = True

#############################################################################################################################
# Functions
def getObjNameMatchingString (rfile,regex):
    nMatch = 0
    for obj in rfile.GetListOfKeys():

        # print(regex)
        # print(obj.GetName())
        # print(re.search(obj.GetName(), regex))

        if (re.search(regex, obj.GetName())):
            obj.Print()
            nMatch+=1
        continue 
    
    if nMatch == 0:
        print('WARNING: No obj matching '+flag+' in '+rfile.GetName())
    elif nMatch == 1:
        print('Found One object matching flag '+obj.GetName())
        return obj.GetName()
    elif nMatch > 1:
        print('WARNING: Found Multiple objects matching '+flag+' !!!')
    print('')

#############################################################################################################################

# Main
gROOT.SetBatch(True)
gStyle.SetOptStat(0)
parser = argparse.ArgumentParser(description='Plot global efficiencies for different triggers')
parser.add_argument('-i', '--fitResultsFile', dest='fitResultsFile'  , help = 'input file with T&P fit results for doubleEle trigger (probe leg)')
parser.add_argument('-r', '--sfFile'    , dest='sfFile'      , help = 'input file with T&P fit results for singleEle ref trigger')
parser.add_argument('-v', '--var'           , dest='var'             , help = 'Variable Name: nvtx, JpsiKE_e2_pt, JpsiKE_elesDr')
parser.add_argument('-f', '--flag'          , dest='flag'            , help = 'doubleEle trigger flag')
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

sfFile = TFile.Open(args.sfFile)
flag = args.flag
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
heff_diEleProbe.SetStatisticOption(TEfficiency.kFCP)
heff_diEleProbe.SetConfidenceLevel(0.68)
geff_diEleProbe = heff_diEleProbe.CreateGraph()

gSF_name = getObjNameMatchingString(sfFile, flag)
gSF = sfFile.Get(gSF_name)
print(gSF_name,gSF)

npoints = geff_diEleProbe.GetN()
geff_diEle = TGraphErrors(npoints)
x_diEleProbe  = ar.array('d', [0.])
y_diEleProbe  = ar.array('d', [0.])
x_sf  = ar.array('d', [0.])
y_sf  = ar.array('d', [0.])
for i in range(0, npoints):

    geff_diEleProbe.GetPoint(i, x_diEleProbe, y_diEleProbe)
    ey_diEleProbe = geff_diEleProbe.GetErrorY(i)
    ex_diEleProbe = geff_diEleProbe.GetErrorX(i)
    
    sf_point      = gSF.GetPoint(i+1, x_sf, y_sf)
    e_sf          = gSF.GetErrorY(i+1)

    print(ey_diEleProbe, y_diEleProbe[0], y_sf[0], e_sf)
    eff_diEle = y_diEleProbe[0] * y_sf[0]
    err_diEle = eff_diEle * TMath.Sqrt( TMath.Power(ey_diEleProbe/y_diEleProbe[0], 2) + TMath.Power(e_sf/y_sf[0], 2) )

    print(i)
    print('e_diEleProbe= ', y_diEleProbe[0]) 
    print('sf ', y_sf) 
    print('eff_diEle= ', eff_diEle)
    print('')

    geff_diEle.SetPoint(i, x_diEleProbe[0], eff_diEle)
    geff_diEle.SetPointError(i, ex_diEleProbe, err_diEle)


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
canvas.SaveAs("/afs/cern.ch/user/c/cquarant/www/DoubleEleTriggerStudy/tnpPlots_2022_final/"+outdir+"/"+tag+"/FullDoubleEleEffFromSF_"+tag+".png")

outrootdir  = inputdir
outrootfilename = inputdir+"/"+"/FullDoubleEleEff_"+tag+".root"
outrootfile = TFile.Open(outrootfilename, "RECREATE")

outrootfile.cd()
geff_diEle.Write()
outrootfile.Write()
outrootfile.Save()
