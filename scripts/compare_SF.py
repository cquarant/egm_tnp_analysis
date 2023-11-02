import os
import sys
import argparse
import array as ar
import json

from collections import OrderedDict

from ROOT import *

gROOT.SetBatch(True)
gStyle.SetOptStat(0)
gStyle.SetLegendBorderSize(0)
gStyle.SetLegendFillColor(0)
gStyle.SetErrorX(0)
maindir = '/afs/cern.ch/work/c/cquarant/RKanalysis/CMSSW_10_6_29/src/egm_tnp_analysis/results/'

parser = argparse.ArgumentParser(description='Plot global efficiencies for different triggers')
parser.add_argument('-v', '--var', dest='var', help = 'x axis variable')
parser.add_argument('-t', '--tag', dest='tag', help = 'output tag')

args = parser.parse_args()

varConfig = {
    'nvtx'         : { 'minvalue':00, 'maxvalue':70, 'axis_label':'N_{vtx}' },
    'JpsiKE_e2_pt' : { 'minvalue':05, 'maxvalue':20, 'axis_label':'Probe Pt [GeV]' },
    'JpsiKE_elesDr': { 'minvalue':00, 'maxvalue':0.6, 'axis_label':'#DeltaR(e_{1},e_{2})' },
}
var = varConfig[args.var]
tag = args.tag

flaglist = OrderedDict([
            # ('doubleEle4BothMatchedL1_4p5_Match'   ,{'alias':'L1_4p5_HLT_4p0_Incl'}),
            # ('doubleEle4BothMatchedL1_5p0_Match'   ,{'alias':'L1_5p0_HLT_4p0_Incl'}),
            # ('doubleEle4BothMatchedL1_5p5_Match'   ,{'alias':'L1_5p5_HLT_4p0_Incl'}),
            ('doubleEle4BothMatchedL1_6p0_Match'   ,{'alias':'L1_6p0_HLT_4p0_Incl'}),
            ('doubleEle4p5BothMatchedL1_6p5_Match' ,{'alias':'L1_6p5_HLT_4p5_Incl'}),
            ('doubleEle5BothMatchedL1_7p0_Match'   ,{'alias':'L1_7p0_HLT_5p0_Incl'}),
            ('doubleEle5BothMatchedL1_7p5_Match'   ,{'alias':'L1_7p5_HLT_5p0_Incl'}),
            ('doubleEle5BothMatchedL1_8p0_Match'   ,{'alias':'L1_8p0_HLT_5p0_Incl'}),
            ('doubleEle5BothMatchedL1_8p5_Match'   ,{'alias':'L1_8p5_HLT_5p0_Incl'}),
            ('doubleEle5BothMatchedL1_10p5_Match'  ,{'alias':'L1_10p5_HLT_5p0_Incl'}),
            ('doubleEle5p5BothMatchedL1_8p5_Match' ,{'alias':'L1_8p5_HLT_5p5_Incl'}),
            ('doubleEle6BothMatchedL1_5p5_Match'   ,{'alias':'L1_5p5_HLT_6p0_Incl'}),
            ('doubleEle6BothMatchedL1_9p0_Match'   ,{'alias':'L1_9p0_HLT_6p0_Incl'}),
            ('doubleEle6p5BothMatchedL1_10p5_Match',{'alias':'L1_10p5_HLT_6p5_Incl'}),
            ('doubleEle6p5BothMatchedL1_11p0_Match',{'alias':'L1_11p0_HLT_6p5_Incl'}),
           # ('doubleEle6p5BothMatchedL1_9p5_Match' :{'alias':'L1_9p5_HLT_6p5_Incl'}),
])

samplesDict = OrderedDict([

    # Eff vs Probe Pt Noah's binning
    # ('MC'                 , { 'dir':'Eff_vs_Probe_Pt_MC_NoahBins'                   , 'col':kBlack, 'mrk':kFullCircle    , 'source':'root'}),
    # ('Ele8 + Jet30'       , { 'dir':'Eff_vs_Probe_Pt_ElePlusJet_NoahBins'           , 'col':kRed  , 'mrk':kFullSquare    , 'source':'root'}),
    # ('SingleEleSingleEGL1', { 'dir':'Eff_vs_Probe_Pt_SingleEle_SingleEGL1_NoahBins' , 'col':kBlue , 'mrk':kFullTriangleUp, 'source':'root'}),
    # ('DoubleMu'           , { 'dir':'Noah_results/TrigSFs_Incl_2_9_23_ptbinned.json', 'col':kGreen , 'mrk':kFullTriangleUp, 'source':'json'}),
    # ('SingleEle (DoubleEGL1)', { 'dir':('doubleEleFired_SingleEle_DiEleEGL1_2022FG_final' , 'col':kGreen , 'mr)k':kFullTriangleDown }),

    # # Eff vs PU
    # ('MC'                    , { 'dir':'Eff_vs_PU_MC', 'col':kBlack, 'mrk':kFullCircle }),
    # ('Ele8 + Jet30'          , { 'dir':'Eff_vs_PU_ElePlusJet'       , 'col':kRed  , 'mrk':kFullSquare }),
    # ('SingleEleSingleEGL1'   , { 'dir':'Eff_vs_PU_SingleEleSingleEGL1', 'col':kBlue, 'mrk':kFullTriangleUp }),
    # # ('SingleEle (DoubleEGL1)', { 'dir':'Eff_vs_PU_SingleEleDieleEGL1' , 'col':kGreen , 'mrk':kFullTriangleDown }),

    # # Eff vs elesDr
    # ('MC'                    , { 'dir':'Eff_vs_elesDr_MC', 'col':kBlack, 'mrk':kFullCircle }),
    # ('Ele8 + Jet30'          , { 'dir':'Eff_vs_elesDr_ElePlusJet'       , 'col':kRed  , 'mrk':kFullSquare }),
    # ('SingleEleSingleEGL1'   , { 'dir':'Eff_vs_elesDr_SingleEleSingleEGL1', 'col':kBlue, 'mrk':kFullTriangleUp }),
    # ('SingleEle (DoubleEGL1)', { 'dir':'Eff_vs_elesDr_SingleEleDieleEGL1_rebinned' , 'col':kGreen , 'mrk':kFullTriangleDown }),

    # Eff vs elesDr rebinned
    # ('MC'                    , { 'dir':'Eff_vs_elesDr_MC_rebinned', 'col':kBlack, 'mrk':kFullCircle }),
    # ('SingleEleSingleEGL1'   , { 'dir':'Eff_vs_elesDr_SingleEleSingleEGL1_rebinned', 'col':kBlue, 'mrk':kFullTriangleUp }),

    # HLTeff vs Probe Pt 
    # ('MC'                    , { 'dir':'HLTeff_vs_Probe_Pt_MC', 'col':kBlack, 'mrk':kFullCircle }),
    # # ('Ele8 + Jet30'          , { 'dir':'HLTeff_vs_Probe_Pt_ElePlusJet'       , 'col':kRed  , 'mrk':kFullSquare }),
    # ('SingleEleSingleEGL1'   , { 'dir':'HLTeff_vs_Probe_Pt_SingleEle_SingleEGL1', 'col':kGreen, 'mrk':kFullTriangleUp }),
    # ('SingleEle (DoubleEGL1)', { 'dir':'HLTeff_vs_Probe_Pt_SingleEleDieleEGL1' , 'col':kBlue , 'mrk':kFullTriangleDown }),

    # Eff vs elesDr BothLegs
    # ('MC'                    , { 'dir':'EffBothLegs_vs_elesDr_MC'                 , 'col':kBlack, 'mrk':kFullCircle }),
    # ('Ele8 + Jet30'          , { 'dir':'EffBothLegs_vs_elesDr_ElePlusJet'         , 'col':kRed  , 'mrk':kFullSquare }),
    # ('SingleEleSingleEGL1'   , { 'dir':'EffBothLegs_vs_elesDr_SingleEleSingleEGL1', 'col':kBlue , 'mrk':kFullTriangleUp }),
    # # ('SingleEle (DoubleEGL1)', { 'dir':('doubleEleFired_SingleEle_DiEleEGL1_2022FG_final' , 'col':kGreen , 'mr)k':kFullTriangleDown }),

    # SF vs Nvtx
    ('SingleEleRef'         , { 'dir':'resutls/testSF'                 , 'col':kBlack, 'mrk':kFullCircle, source='root' }),
    ('DoubleMuRef'          , { 'dir':'EffBothLegs_vs_Nvtx_ElePlusJet' , 'col':kRed  , 'mrk':kFullSquare, source='json' }),
    # ('SingleEleSingleEGL1'   , { 'dir':'EffBothLegs_vs_Nvtx_SingleEleSingleEGL1', 'col':kBlue , 'mrk':kFullTriangleUp }),
    # ('SingleEle (DoubleEGL1)', { 'dir':('doubleEleFired_SingleEle_DiEleEGL1_2022FG_final' , 'col':kGreen , 'mr)k':kFullTriangleDown }

])

canvas = TCanvas("c1", "", 500, 400)
canvas.cd()

canvas.SetLeftMargin(0.16)
canvas.SetRightMargin(0.06)

hset = TH1F("hset","", 100, var['minvalue'], var['maxvalue'])
#hset.GetXaxis().SetTitle(var['axis_label'])
hset.GetXaxis().SetTitle('')
hset.GetXaxis().SetTitleSize( 0.06 )
hset.GetXaxis().SetTitleOffset( 0.75 )
hset.GetXaxis().SetLabelSize( 0.06 )
hset.GetXaxis().SetNdivisions( 505 )

#hset.GetYaxis().SetTitle( "efficiency" )
hset.GetYaxis().SetTitle('')
hset.GetYaxis().SetTitleSize( 0.055 )
hset.GetYaxis().SetTitleOffset( 0.95 )
hset.GetYaxis().SetLabelSize( 0.06 )
hset.GetYaxis().SetRangeUser( 0.0, 10.0 )
hset.GetYaxis().SetNdivisions( 505 )

legend_top = TLegend(0.35, 0.55, 0.88, 0.88)
# legend_top = TLegend(0.65, 0.65, 0.88, 0.88)
legend_top.SetFillStyle(0)
legend_bot = TLegend(0.35, 0.15, 0.88, 0.28)
legend_bot.SetFillStyle(0)

box = TBox(0.5,0.5,0.9,0.9)
box.SetFillColor(kWhite)

eff_max = 0
for flag in flaglist:

    legend_top.Clear()
    legend_bot.Clear()
    hset.Draw()

    histoSF = {}

    for isample, sample in enumerate(samplesDict.keys()):

        if samplesDict[sample]['source'] == 'root':
            
            if 'MC' in samplesDict[sample]["dir"]:
                inputfilename = maindir+"/"+samplesDict[sample]["dir"]+"/"+flag+"/differential_eff_"+flag+".root"
                inputfile = TFile.Open(inputfilename)
                teff = inputfile.Get("htot_clone")
                heff = teff.CreateGraph()
                histoSF['MC'] = heff
            else:
                inputfilename = maindir+"/"+samplesDict[sample]["dir"]+"/"+flag+"/FullDoubleEleEff_"+flag+".root"
                inputfile = TFile.Open(inputfilename)
                heff = inputfile.Get("Graph")
                histoSF[sample] = heff
                for point in range(histoSF[sample].GetN()):
                    histoSF[sample].SetPointY( point, histoSF[sample].GetPointY(point)/histoSF['MC'].GetPointY(point) )
                    histoSF[sample].SetPointError( point, 0, histoSF[sample].GetErrorY(point)/histoSF['MC'].GetPointY(point) )

        elif samplesDict[sample]['source'] == 'json':
            inputjson = open('results/'+samplesDict[sample]['dir'])
            inputdata = json.load(inputjson)   
            
            trigger_data = inputdata[flaglist[flag]['alias']]

            xbins = ar.array('f',trigger_data['pT'])
            print xbins

            histoSF[sample] = TH1F(sample,'',len(xbins),xbins)
            for bin in range(len(xbins)):
                print bin, histoSF[sample].GetBinLowEdge(bin+1), trigger_data['effs'][bin]
                histoSF[sample].SetBinContent(bin, trigger_data['effs'][bin][0])

        print ""
        print "Opening file ", inputfilename
        
        histoSF[sample].SetMarkerStyle(samplesDict[sample]["mrk"])
        histoSF[sample].SetMarkerColor(samplesDict[sample]["col"])
        histoSF[sample].SetMarkerSize(1)
        histoSF[sample].SetLineColor(samplesDict[sample]["col"])
        histoSF[sample].SetLineWidth(1)

        # for ipoint in range(histoSF[sample].GetN()):
        #     histoSF[sample].SetPointEXlow(ipoint, 0) 
        #     histoSF[sample].SetPointEXhigh(ipoint, 0) 

        if sample != 'MC':
            histoSF[sample].Draw("same P")

            # eff_lastbin = histoSF[sample].GetEfficiency(5)
            # print eff_lastbin
            # if eff_lastbin>eff_max:
            #     eff_max = eff_lastbin

            legend_top.AddEntry(histoSF[sample], sample, "pl")
            legend_bot.AddEntry(histoSF[sample], sample, "pl")

    # if eff_max <= 0.5:
    #     legend_top.Draw("same")
    # else:
    # box.Draw("same")
    # legend_bot.Draw("same")
    legend_top.Draw("same")

    outputdir = "/afs/cern.ch/user/c/cquarant/www/DoubleEleTriggerStudy/tnpPlots_2022_final/"+tag
    os.system("mkdir -p "+outputdir)
    canvas.SaveAs(outputdir+"/"+flag+"_"+tag+".png")
    os.system("cp /afs/cern.ch/user/c/cquarant/www/DoubleEleTriggerStudy/index.php "+outputdir)
