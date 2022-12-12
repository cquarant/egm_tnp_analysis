import os
import sys

from collections import OrderedDict

from ROOT import *

gROOT.SetBatch(True)
gStyle.SetOptStat(0)
gStyle.SetLegendBorderSize(0)
gStyle.SetLegendFillColor(0)
maindir = '/afs/cern.ch/work/c/cquarant/RKanalysis/CMSSW_10_6_29/src/egm_tnp_analysis/results/'

flaglist = [# 'doubleEle4BothMatched',
            # 'doubleEle4p5BothMatched',
            # 'doubleEle5BothMatched',
            # 'doubleEle6BothMatched',
            # 'doubleEle6p5BothMatched',
            # 'doubleEle6p5Fired',
            'doubleEle4BothMatchedL1_5p5_Match',
            'doubleEle4BothMatchedL1_6p0_Match',
            'doubleEle4p5BothMatchedL1_6p5_Match',
            'doubleEle5BothMatchedL1_7p0_Match',
            'doubleEle5BothMatchedL1_8p0_Match',
            'doubleEle5BothMatchedL1_8p5_Match',
            'doubleEle5BothMatchedL1_10p5_Match',
            'doubleEle6BothMatchedL1_5p5_Match',
            'doubleEle6p5BothMatchedL1_10p5_Match',
            'doubleEle6p5BothMatchedL1_11p0_Match',
]

samplesDict = OrderedDict([
    #('MC'          , { 'dir' : 'doubleEleFired_MC_BuTOjpsiKEE_L1match'        , 'col':kBlack }),
    #('MC'          , { 'dir' : 'doubleEleFired_MC_BuTOjpsiKEE_passMVA_binned'        , 'col':kBlack }),
    #('MC'          , { 'dir' : 'doubleEleFired_MC_BuTOjpsiKEE_passMVA_binnedMC'      , 'col':kBlack }),
    #('Ele8 + Jet30' , { 'dir' : 'doubleEleFired_ElePlusJet_2022CDEF_L1match'    , 'col':kRed   }),
    ('Ele8 + Jet30' , { 'dir' : 'doubleEleFired_ElePlusJet_2022CDEF_L1match_json', 'col':kRed   }),
    #('Ele8 + Jet30' , { 'dir' : 'doubleEleFired_ElePlusJet_2022CDEF_passMVA_binned'   , 'col':kRed   }),
    #('Ele8 + Jet30' , { 'dir' : 'doubleEleFired_ElePlusJet_2022CDEF_passMVA_binnedMC'   , 'col':kRed   }),
    #('SingleEleSingleEGL1' , { 'dir' : 'doubleEleFired_SingleEle_2022F_L1match'       , 'col':kGreen }),
    ('SingleEleSingleEGL1' , { 'dir' : 'doubleEleFired_SingleEle_2022F_L1match_json'  , 'col':kGreen }),
    #('SingleEleSingleEGL1' , { 'dir' : 'doubleEleFired_SingleEle_2022F_passMVA_binned'       , 'col':kGreen }),
    #('SingleEleSingleEGL1' , { 'dir' : 'doubleEleFired_SingleEle_2022F_passMVA_binnedMC'       , 'col':kGreen }),
    #('SingleEle (DoubleEGL1)' , { 'dir' : 'doubleEleFired_SingleEleDiEleL1_2022F_L1match', 'col':kBlue  }),
    ('SingleEle (DoubleEGL1)' , { 'dir' : 'doubleEleFired_SingleEleDiEleL1_2022F_L1match_json', 'col':kBlue  }),
    #('SingleEle (DoubleEGL1)' , { 'dir' : 'doubleEleFired_SingleEleDiEleL1_2022F_passMVA_binned', 'col':kBlue  }),
    #('SingleEle (DoubleEGL1)' , { 'dir' : 'doubleEleFired_SingleEleDiEleL1_2022F_passMVA_binnedMC', 'col':kBlue  }),
])



tag = "L1match_json"

canvas = TCanvas("c1", "", 700, 800)
canvas.cd()

hset = TH2F("hset","", 100, 0, 50, 100, 0, 1.0)
hset.GetXaxis().SetTitle("Probe Pt [GeV]")
hset.GetXaxis().SetTitle("")
hset.GetXaxis().SetTitleSize( 0.06 )
hset.GetXaxis().SetTitleOffset( 0.75 )
hset.GetXaxis().SetLabelSize( 0.04 )

hset.GetYaxis().SetTitle( "trigger efficiency" )
hset.GetYaxis().SetTitle( "" )
hset.GetYaxis().SetTitleSize( 0.06 )
hset.GetYaxis().SetTitleOffset( 0.75 )
hset.GetYaxis().SetLabelSize( 0.04 )
hset.GetYaxis().SetRangeUser( 0.0, 1.0 )

legend_top = TLegend(0.35, 0.65, 0.88, 0.88)
legend_bot = TLegend(0.65, 0.15, 0.9, 0.15)

eff_max = 0
for flag in flaglist:

    legend_top.Clear()
    legend_bot.Clear()
    hset.Draw()

    for isample, sample in enumerate(samplesDict.keys()):

        inputfilename = maindir+"/"+samplesDict[sample]["dir"]+"/"+flag+"/differential_eff_"+flag+".root"
        print ""
        print "Opening file ", inputfilename
        inputfile = TFile.Open(inputfilename)

        heff = inputfile.Get("htot_clone")
        heff.SetMarkerColor(samplesDict[sample]["col"])
        heff.SetLineColor(samplesDict[sample]["col"])
        heff.Draw("same")

        eff_lastbin = heff.GetEfficiency(5)
        print eff_lastbin
        if eff_lastbin>eff_max:
            eff_max = eff_lastbin

        legend_top.AddEntry(heff, sample, "pl")
        legend_bot.AddEntry(heff, sample, "pl")

    # if eff_max <= 0.5:
    #     legend_top.Draw("same")
    # else:
    #     legend_bot.Draw("same")
    #legend_top.Draw("same")
    canvas.SaveAs("/afs/cern.ch/user/c/cquarant/www/DoubleEleTriggerStudy/tnpPlots_2022_full/merged/"+flag+"_"+tag+".png")
