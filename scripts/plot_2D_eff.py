import argparse
import os
import array as ar
from ROOT import *
import re

###############################################################################

def findcorrespondingy(gr, x_l, x_r):
    x_point = ar.array('d', [0.])
    y_point = ar.array('d', [0.])
    for i in range(gr.GetN()):
        gr.GetPoint(i, x_point, y_point)
        #print x, x_point[0]
        if x_point[0] >= x_l and x_point[0] < x_r:
            #print 'match found'
            return y_point[0]

###############################################################################

gROOT.SetBatch(True)
gStyle.SetOptStat(0)
parser = argparse.ArgumentParser(description='Plot global efficiencies for different triggers')
parser.add_argument('-i', '--fitResultsFile', dest='fitResultsFile'  , help = 'input file with T&P fit results for doubleEle trigger (probe leg)')
parser.add_argument('-r', '--refEffFile'    , dest='refEffFile'      , default=0, help = 'input file with T&P fit results for singleEle ref trigger')

args = parser.parse_args()

varConfig = {
    'JpsiKE_e1_pt' : { 'minvalue':08., 'maxvalue':30. , 'axis_label':'Tag Pt [GeV]' , 'ref_eff_file': 'results/RefEff_vs_Probe_Pt_SingleEleSingleEGL1'},
    'JpsiKE_e2_pt' : { 'minvalue':05., 'maxvalue':30. , 'axis_label':'Probe Pt [GeV]' , 'ref_eff_file': 'results/RefEff_vs_Probe_Pt_SingleEleSingleEGL1'},
    'JpsiKE_e1_eta': { 'minvalue':-1.22, 'maxvalue':1.22 , 'axis_label':'Tag Eta' , 'ref_eff_file': 'results/RefEff_vs_Probe_Eta_SingleEleSingleEGL1'},
    'JpsiKE_e2_eta': { 'minvalue':-1.22, 'maxvalue':1.22 , 'axis_label':'Probe Eta' , 'ref_eff_file': 'results/RefEff_vs_Probe_Eta_SingleEleSingleEGL1'},
}

fitResultsFileName = args.fitResultsFile

inputdir  = fitResultsFileName.replace(args.fitResultsFile.split("/")[-1], '')
fitResultsFile = TFile.Open(fitResultsFileName)

inputHistoFileName = fitResultsFileName.replace("nominalFit.","")
inputHistoFile = TFile.Open(inputHistoFileName)

tag = args.fitResultsFile.split("/")[-2]
outdir = args.fitResultsFile.split("/")[-3]

outrootdir  = inputdir
outrootfilename = inputdir+"/"+"/FullDoubleEleEff_"+tag+".root"
outrootfile = TFile.Open(outrootfilename, "RECREATE")
outrootfile.cd()

if not args.refEffFile:
    print 'File with T&P fit results for singleEle reference trigger not provided'
    print 'Only Probe leg efficiency will be plotted'
    print 'If you are running on MC sample, this efficiency corresponds to the whole efficiency'

###################################################################
# Create list of bin names and edges for doubleEle trigger
###################################################################

resPlist = []
resFlist = []
var1_binedges = []
var2_binedges = []
pattern = r"(JpsiKE_[a-zA-Z0-9]+_[a-zA-Z0-9]+)_(m*[0-9]+p[0-9]+)To(m*[0-9]+p[0-9]+)_(JpsiKE_[a-zA-Z0-9]+_[a-zA-Z0-9]+)_(m*[0-9]+p[0-9]+)To(m*[0-9]+p[0-9]+)"
for obj in fitResultsFile.GetListOfKeys():
    objname = obj.GetName()
    if "bin" in objname:
        if "resP" in objname:
            resPlist.append(objname)

            # Define the regular expression pattern
            matches = re.search(pattern, objname)

            # Extract the relevant groups from the match object
            var1 = varConfig[matches.group(1)]
            var1_min = float(matches.group(2).replace("p",".").replace("m","-"))
            var1_binedges.append(var1_min)
            
            var2 = varConfig[matches.group(4)]
            var2_min = float(matches.group(5).replace("p",".").replace("m","-"))
            var2_binedges.append(var2_min)

        if "resF" in objname:
            resFlist.append(objname)

var1_binedges.append(var1['maxvalue'])
var2_binedges.append(var2['maxvalue'])

var1_binedges = sorted(list(set(var1_binedges)))
var2_binedges = sorted(list(set(var2_binedges)))

resPlist.sort()
resFlist.sort()

var1_binedges_ar = ar.array('f',var1_binedges)
var2_binedges_ar = ar.array('f',var2_binedges)

#############################################################
### Create histogram of doubleEle Probe leg efficiency
#############################################################

htrig_diEleProbe = TH2F("htrig_diEleProbe", "htrig_diEleProbe", len(var2_binedges)-1, var2_binedges_ar, len(var1_binedges)-1, var1_binedges_ar)
htot_diEleProbe  = TH2F("htot_diEleProbe" , "htot_diEleProbe" , len(var2_binedges)-1, var2_binedges_ar, len(var1_binedges)-1, var1_binedges_ar)

nEvtAllBins = 0
for ibin in range(len(resPlist)):
    
    y_index = int(ibin / (len(var2_binedges)-1))
    x_index = (ibin % (len(var2_binedges)-1))

    print ibin, len(var1_binedges), len(var2_binedges), x_index, y_index

    ### Get Pass/Fail events for doubleEle trigger bin-by-bin
    FitResultPass = fitResultsFile.Get(resPlist[ibin])
    FitResultFail = fitResultsFile.Get(resFlist[ibin])

    nSigP     = FitResultPass.floatParsFinal().find("nSigP").getVal()                                                                                            
    nSigP_err = FitResultPass.floatParsFinal().find("nSigP").getError()

    nSigF     = FitResultFail.floatParsFinal().find("nSigF").getVal()
    nSigF_err = FitResultFail.floatParsFinal().find("nSigF").getError()

    nSigTot     = nSigP+nSigF
    nSigTot_err = TMath.Sqrt( TMath.Power(nSigP_err, 2) + TMath.Power(nSigF_err, 2) )

    # check if number of events in data is enough to evaluate efficiency (~100 evt)
    inputHistoPass = inputHistoFile.Get(resPlist[ibin].replace("resP","Pass"))
    inputHistoFail = inputHistoFile.Get(resFlist[ibin].replace("resF","Fail"))
    EvtBins = inputHistoPass.GetEntries() + inputHistoFail.GetEntries()
    
    if EvtBins < 50:
        nSigP = 0.
        nSigP_err = 0.
        nSigTot_err = 0.

    # Num e den of double ele probe leg efficiency
    htrig_diEleProbe.SetBinContent(x_index+1, y_index+1, nSigP)
    htrig_diEleProbe.SetBinError  (x_index+1, y_index+1, nSigP_err)

    htot_diEleProbe.SetBinContent(x_index+1, y_index+1, nSigTot)
    htot_diEleProbe.SetBinError  (x_index+1, y_index+1, nSigTot_err)
    
    print x_index, y_index, nSigP, nSigTot, nSigP_err, nSigTot_err
#############################################################
# Evaluate and plot doubleEle (probe leg) efficiency
#############################################################

heff_diEleProbe = htrig_diEleProbe.Clone("heff_diEleProbe")
heff_diEleProbe.Divide(htot_diEleProbe)

hset = TH2F( "hset", "", 100, var2['minvalue'], var2['maxvalue'], 100, var1['minvalue'], var1['maxvalue'])
hset.GetXaxis().SetTitle(var2['axis_label'])
hset.GetXaxis().SetTitleSize( 0.06 )
hset.GetXaxis().SetTitleOffset( 0.75 )
hset.GetXaxis().SetLabelSize( 0.04 )

hset.GetYaxis().SetTitle(var1['axis_label'])
hset.GetYaxis().SetTitleSize( 0.06 )
hset.GetYaxis().SetTitleOffset( 0.80 )
hset.GetYaxis().SetLabelSize( 0.04 )

hset.GetZaxis().SetRangeUser( 0, 100)

gStyle.SetPaintTextFormat("2.1f")
canvas = TCanvas("c1","c1")
canvas.SetRightMargin(0.14)
canvas.cd()

heff_diEleProbe.Scale(100)
heff_diEleProbe.SetMarkerSize(1.6)

heff_diEleProbe.GetXaxis().SetRangeUser( var2['minvalue'], var2['maxvalue'] )
heff_diEleProbe.GetYaxis().SetRangeUser( var1['minvalue'], var1['maxvalue'] )

heff_diEleProbe.GetZaxis().SetTitle("efficiency (%)")
heff_diEleProbe.GetZaxis().SetTitleSize( 0.06 )
heff_diEleProbe.GetZaxis().SetTitleOffset( 0.7 )
heff_diEleProbe.GetZaxis().SetRangeUser( 0.0, 20.0 )

hset.GetZaxis().SetRangeUser( 0, 20)
hset.Draw()
heff_diEleProbe.Draw("SAMECOLZtext45")

canvas.SaveAs("/afs/cern.ch/user/c/cquarant/www/DoubleEleTriggerStudy/tnpPlots_2022_final/"+outdir+"/"+tag+"/EffProbeLeg_"+tag+".png")



# Draw error plots
heff_diEleProbe_err = heff_diEleProbe.Clone("heff_diEleProbe_err")
for ibin in range(heff_diEleProbe.GetNbinsY()+1):
    for jbin in range(heff_diEleProbe.GetNbinsX()+1):
        heff_diEleProbe_err.SetBinContent(ibin, jbin, heff_diEleProbe.GetBinError(ibin,jbin))

heff_diEleProbe_err.GetXaxis().SetRangeUser( var2['minvalue'], var2['maxvalue'] )
heff_diEleProbe_err.GetYaxis().SetRangeUser( var1['minvalue'], var1['maxvalue'] )

heff_diEleProbe_err.GetZaxis().SetTitle("Error on efficiency (%)")
heff_diEleProbe_err.GetZaxis().SetTitleSize( 0.06 )
heff_diEleProbe_err.GetZaxis().SetTitleOffset( 0.7 )
heff_diEleProbe_err.GetZaxis().SetRangeUser( 0.0, 20.0 )

gStyle.SetPalette(kInvertedDarkBodyRadiator)
hset.GetZaxis().SetRangeUser( 0, 20 )
hset.Draw()
heff_diEleProbe_err.Draw("SAMECOLZtext45")

canvas.SaveAs("/afs/cern.ch/user/c/cquarant/www/DoubleEleTriggerStudy/tnpPlots_2022_final/"+outdir+"/"+tag+"/EffProbeLeg_"+tag+"_error.png")

#############################################################
### Unroll TH2 in a set of TH1
#############################################################

# setup canvas
canvas.SetRightMargin(0.1)
canvas.cd()
hset_1d = TH2F( "hset_1d_probeleg", "", 100, var2['minvalue'], var2['maxvalue'], 100, 0, 100)
hset_1d.GetXaxis().SetTitle(var2['axis_label'])
hset_1d.GetXaxis().SetTitleSize( 0.06 )
hset_1d.GetXaxis().SetTitleOffset( 0.75 )
hset_1d.GetXaxis().SetLabelSize( 0.04 )

hset_1d.GetYaxis().SetTitle("efficiency (%)")
hset_1d.GetYaxis().SetTitleSize( 0.06 )
hset_1d.GetYaxis().SetTitleOffset( 0.80 )
hset_1d.GetYaxis().SetLabelSize( 0.04 )

hset_1d.Draw()

legend = TLegend( 0.6, 0.5, 0.88, 0.88 )
legend.SetBorderSize(0)

# fill and plot TH2 slices
markers = [20,21,22,23,29,33,34]

heff_diEleProbe_slices = {}
for jbin in range(heff_diEleProbe.GetNbinsY()):

    if heff_diEleProbe.GetYaxis().GetBinCenter(jbin+1) < var1['minvalue'] or heff_diEleProbe.GetYaxis().GetBinCenter(jbin+1) > var1['maxvalue']:
        continue

    hname = "heff_diEleProbe_Ybin"+str(jbin)
    heff_diEleProbe_slices[hname] = TH1F("heff_diEleProbe_Ybin"+str(jbin), "", len(var2_binedges)-1, var2_binedges_ar)
    
    for ibin in range(heff_diEleProbe.GetNbinsX()):
        heff_diEleProbe_slices[hname].SetBinContent( ibin+1, heff_diEleProbe.GetBinContent(ibin+1,jbin+1) )
        heff_diEleProbe_slices[hname].SetBinError  ( ibin+1, heff_diEleProbe_err.GetBinContent(ibin+1,jbin+1) )

    heff_diEleProbe_slices[hname].SetMarkerStyle( markers[ jbin % len(markers) ] )
    heff_diEleProbe_slices[hname].SetMarkerColor( (jbin+5) % 9 + 1 )
    heff_diEleProbe_slices[hname].SetLineColor( (jbin+5) % 9 + 1 )
    heff_diEleProbe_slices[hname].Draw("same")
    
    legend.AddEntry( heff_diEleProbe_slices[hname], "e_{tag} p_{T} #in [%.1f,%.1f]" %(var1_binedges[jbin],var1_binedges[jbin+1]) )

legend.Draw("same")

canvas.SaveAs("/afs/cern.ch/user/c/cquarant/www/DoubleEleTriggerStudy/tnpPlots_2022_final/"+outdir+"/"+tag+"/EffProbeLeg_"+tag+"_unrolled.png")

heff_diEleProbe.Write()
for slice in heff_diEleProbe_slices.keys():
    heff_diEleProbe_slices[slice].Write
outrootfile.Write()
outrootfile.Save()

###################################################################
### Create 2D histogram of eff(singleEle|e1e2)
###################################################################

if not args.refEffFile:
    exit()

tag = args.fitResultsFile.split("/")[-2]
outdir = args.fitResultsFile.split("/")[-3]

RefEffFile = TFile.Open(args.refEffFile)
g1_ref = RefEffFile.Get("htot_clone").CreateGraph()
h2_ref = TH2F("h2_ref" , "h2_ref" , len(var2_binedges)-1, var2_binedges_ar, len(var1_binedges)-1, var1_binedges_ar)

print var1_binedges
print var2_binedges
for ibin in range(len(var1_binedges)-1):
    for jbin in range(len(var2_binedges)-1):

        var1_l = h2_ref.GetYaxis().GetBinLowEdge(ibin+1)
        var1_r = h2_ref.GetYaxis().GetBinUpEdge(ibin+1)
        var2_l = h2_ref.GetXaxis().GetBinLowEdge(jbin+1)
        var2_r = h2_ref.GetXaxis().GetBinUpEdge(jbin+1)

        print var2_l, var2_r

        var1_e_ref = findcorrespondingy(g1_ref, var1_l, var1_r)
        var2_e_ref = findcorrespondingy(g1_ref, var2_l, var2_r)

        print var1_e_ref

        e_singleEle_e1e2 = 1 - (1 - var1_e_ref) * (1 - var2_e_ref)
        h2_ref.SetBinContent( jbin+1, ibin+1, e_singleEle_e1e2*100)
        print jbin+1, ibin+1, e_singleEle_e1e2*100


canvas.cd()

gStyle.SetPalette(kBird)
hset.GetZaxis().SetRangeUser(0,100)
hset.Draw()

h2_ref.GetXaxis().SetRangeUser( var2['minvalue'], var2['maxvalue'] )
h2_ref.GetYaxis().SetRangeUser( var1['minvalue'], var1['maxvalue'] )

h2_ref.GetZaxis().SetTitle("efficiency (%)")
h2_ref.GetZaxis().SetTitleSize( 0.06 )
h2_ref.GetZaxis().SetTitleOffset( 0.7 )
h2_ref.GetZaxis().SetRangeUser( 0.0, 100.0 )

h2_ref.SetMarkerSize(1.6)
h2_ref.Draw("sameCOLZtext45")

canvas.SaveAs("/afs/cern.ch/user/c/cquarant/www/DoubleEleTriggerStudy/tnpPlots_2022_final/"+outdir+"/"+tag+"/RefEff_"+tag+".png")


#############################################################
### Evaluate and plot doubleEle trigger efficiency
#############################################################

heff_diEle = heff_diEleProbe.Clone('eff_diEle')
heff_diEle_err = heff_diEleProbe.Clone('eff_diEle')
print ""
print "Full efficiency TH2"
print ""
for ibin in range(heff_diEle.GetNbinsY()):
    for jbin in range(heff_diEle.GetNbinsX()):

        e_diEle = heff_diEle.GetBinContent(ibin+1, jbin+1)
        e_diEle_err = heff_diEle.GetBinError(ibin+1, jbin+1)
        e_singleEle_e1e2 = h2_ref.GetBinContent(ibin+1, jbin+1)
        
        heff_diEle.SetBinContent( ibin+1, jbin+1, e_diEle * e_singleEle_e1e2 * 0.01)
        heff_diEle_err.SetBinContent( ibin+1, jbin+1, e_diEle_err * e_singleEle_e1e2 * 0.01)
    
heff_diEle.SetMarkerStyle(22)
heff_diEle.SetMarkerSize(1.2)

canvas.cd()

heff_diEle.GetXaxis().SetRangeUser( var2['minvalue'], var2['maxvalue'] )
heff_diEle.GetYaxis().SetRangeUser( var1['minvalue'], var1['maxvalue'] )

heff_diEle.GetZaxis().SetTitle("efficiency (%)")
heff_diEle.GetZaxis().SetTitleSize( 0.06 )
heff_diEle.GetZaxis().SetTitleOffset( 0.7 )
heff_diEle.GetZaxis().SetRangeUser( 0.0, 20.0 )

heff_diEle.SetMarkerSize(1.6)

gStyle.SetPalette(kBird)
hset.GetZaxis().SetRangeUser( 0, 20.0 )
hset.Draw()
heff_diEle.Draw("sameCOLZtext45")

canvas.SaveAs("/afs/cern.ch/user/c/cquarant/www/DoubleEleTriggerStudy/tnpPlots_2022_final/"+outdir+"/"+tag+"/FullDoubleEleEff_"+tag+".png")

# Draw error plots
heff_diEle_err = heff_diEle.Clone("heff_diEle_err")
for ibin in range(heff_diEle.GetNbinsY()+1):
    for jbin in range(heff_diEle.GetNbinsX()+1):
        heff_diEle_err.SetBinContent(ibin, jbin, heff_diEle.GetBinError(ibin,jbin))

heff_diEle_err.GetXaxis().SetRangeUser( var2['minvalue'], var2['maxvalue'] )
heff_diEle_err.GetYaxis().SetRangeUser( var1['minvalue'], var1['maxvalue'] )

heff_diEle_err.GetZaxis().SetTitle("Error on efficiency (%)")
heff_diEle_err.GetZaxis().SetTitleSize( 0.06 )
heff_diEle_err.GetZaxis().SetTitleOffset( 0.7 )
heff_diEle_err.GetZaxis().SetRangeUser( 0.0, 20.0 )

gStyle.SetPalette(kInvertedDarkBodyRadiator)
hset.GetZaxis().SetRangeUser( 0, 20)
hset.Draw()
heff_diEle_err.Draw("SAMECOLZtext45")

canvas.SaveAs("/afs/cern.ch/user/c/cquarant/www/DoubleEleTriggerStudy/tnpPlots_2022_final/"+outdir+"/"+tag+"/FullDoubleEleEff_"+tag+"_error.png")

#############################################################
### Unroll TH2 in a set of TH1
#############################################################
outrootfile.cd()
# setup canvas
canvas.SetRightMargin(0.1)
canvas.cd()
hset_1d = TH2F( "hset_1d", "", 100, var2['minvalue'], var2['maxvalue'], 100, 0, 100)
hset_1d.GetXaxis().SetTitle(var2['axis_label'])
hset_1d.GetXaxis().SetTitleSize( 0.06 )
hset_1d.GetXaxis().SetTitleOffset( 0.75 )
hset_1d.GetXaxis().SetLabelSize( 0.04 )

hset_1d.GetYaxis().SetTitle("efficiency (%)")
hset_1d.GetYaxis().SetTitleSize( 0.06 )
hset_1d.GetYaxis().SetTitleOffset( 0.80 )
hset_1d.GetYaxis().SetLabelSize( 0.04 )

hset_1d.Draw()

legend = TLegend( 0.6, 0.5, 0.88, 0.88 )
legend.SetBorderSize(0)

# fill and plot TH2 slices
markers = [20,21,22,23,29,33,34]

heff_diEle_slices = {}
for jbin in range(heff_diEle.GetNbinsY()):

    if heff_diEle.GetYaxis().GetBinCenter(jbin+1) < var1['minvalue'] or heff_diEle.GetYaxis().GetBinCenter(jbin+1) > var1['maxvalue']:
        continue

    hname = "heff_diEle_Ybin"+str(jbin)
    heff_diEle_slices[hname] = TH1F("heff_diEle_Ybin"+str(jbin), "", len(var2_binedges)-1, var2_binedges_ar)
    
    for ibin in range(heff_diEle.GetNbinsX()):
        heff_diEle_slices[hname].SetBinContent( ibin+1, heff_diEle.GetBinContent(ibin+1,jbin+1) )
        heff_diEle_slices[hname].SetBinError  ( ibin+1, heff_diEle_err.GetBinContent(ibin+1,jbin+1) )

    heff_diEle_slices[hname].SetMarkerStyle( markers[ jbin % len(markers) ] )
    heff_diEle_slices[hname].SetMarkerColor( (jbin+5) % 9 + 1 )
    heff_diEle_slices[hname].SetLineColor( (jbin+5) % 9 + 1 )
    heff_diEle_slices[hname].Draw("same")
    
    legend.AddEntry( heff_diEle_slices[hname], "e_{tag} p_{T} #in [%.1f,%.1f]" %(var2_binedges[jbin],var2_binedges[jbin+1]) )

legend.Draw("same")

canvas.SaveAs("/afs/cern.ch/user/c/cquarant/www/DoubleEleTriggerStudy/tnpPlots_2022_final/"+outdir+"/"+tag+"/FullDoubleEleEff_"+tag+"_unrolled.png")


#############################################################
### Save to file
#############################################################

h2_ref.Write()
heff_diEle.Write()
for slice in heff_diEle_slices.keys():
    heff_diEle_slices[slice].Write()

outrootfile.Write()
outrootfile.Save()

