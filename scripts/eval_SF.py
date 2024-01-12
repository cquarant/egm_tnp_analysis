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
    'Nvtx'         : { 'minvalue':0    , 'maxvalue':70  , 'bins': [0, 22, 27, 31, 36, 70], 'axis_label':'N_{vtx}'             , 'alias':'npv' },
    'JpsiKE_e2_pt' : { 'minvalue':5    , 'maxvalue':20  , 'bins': [5.0,  7.0,  9.0, 10.0, 11.0, 12.0, 13.0, 20.0], 'axis_label':'Probe Pt [GeV]'      , 'alias':'pt' },
    'JpsiKE_e2_eta': { 'minvalue':-1.22, 'maxvalue':1.22, 'bins': [-1.22, -0.70, -0.20, 0.20, 0.70, 1.22], 'axis_label':'Probe Eta'           , 'alias':'eta' },
    'JpsiKE_elesDr': { 'minvalue':0    , 'maxvalue':0.6 , 'bins': [0.0, 0.12, 0.20, 0.28, 0.44, 0.6], 'axis_label':'#DeltaR(e_{1},e_{2})', 'alias':'dr' },
}
var = varConfig[args.var]
tag = args.tag

flaglist = OrderedDict([
            # ('probe_fired', {'alias':'probe_fired'}),
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
            ('doubleEle6p5BothMatchedL1_9p5_Match' ,{'alias':'L1_9p5_HLT_6p5_Incl'}),
])

samplesDictAll = OrderedDict([

    # Eff vs ProbePt Noah's binning
    ('JpsiKE_e2_pt' , OrderedDict([
        ('SingleEle_ref', {'dir':'Eff_vs_e2Pt_SingleEleSingleEGL1_NoahBins_eprbCorr', 'col':kBlue , 'mrk':kFullTriangleUp  , 'source':'root', 'type':'Data', 'effType':'FullEff', 'cat':1}),
        ('MC_FullEff'   , { 'dir':'EffBothLegs_vs_e2Pt_MC_NoahBins', 'col':kBlue , 'mrk':kOpenSquare  , 'source':'root','type':'MC', 'effType':'FullEff','cat':1}),
        ('DoubleMu_ref' , { 'dir':'Noah_results_new/TrigEffs_Data_Incl_6_13_23_ptbinned.json'  , 'col':kRed, 'mrk':kFullTriangleDown, 'source':'json','type':'Data', 'effType':'FullEff','cat':2}),
        ('MC'   , { 'dir':'Noah_results_new/TrigEffs_MC_Incl_6_13_23_ptbinned.json', 'col':kBlue , 'mrk':kOpenSquare  , 'source':'json','type':'MC', 'effType':'FullEff','cat':2}),
        ])
    ),

    # Eff vs ProbeEta Noah's binning
    ('JpsiKE_e2_eta', OrderedDict([
        ('SingleEle_ref', { 'dir':'Eff_vs_e2Eta_SingleEleSingleEGL1_NoahBins_eprbCorr', 'col':kBlue , 'mrk':kFullTriangleUp  , 'source':'root', 'type':'Data', 'effType':'FullEff','cat':1}),
        ('MC_FullEff'   , { 'dir':'EffBothLegs_vs_e2Eta_MC_NoahBins', 'col':kBlue , 'mrk':kOpenSquare  , 'source':'root','type':'MC', 'effType':'FullEff','cat':1}),
        ('DoubleMu_ref' , { 'dir':'Noah_results_new/TrigEffs_Data_Incl_6_13_23_etabinned.json'  , 'col':kRed, 'mrk':kFullTriangleDown, 'source':'json','type':'Data', 'effType':'FullEff','cat':2}),
        ('MC'   , { 'dir':'Noah_results_new/TrigEffs_MC_Incl_6_13_23_etabinned.json', 'col':kBlue , 'mrk':kOpenSquare  , 'source':'json','type':'MC', 'effType':'FullEff','cat':2}),
        ])
    ),

    # Eff vs elesDr Noah's binning
    ('JpsiKE_elesDr', OrderedDict([
        ('SingleEle_ref', { 'dir':'Eff_vs_elesDr_SingleEleSingleEGL1_NoahBins_eprbCorr', 'col':kBlue , 'mrk':kFullTriangleUp  , 'source':'root', 'type':'Data', 'effType':'FullEff','cat':1}),
        ('MC_FullEff'   , { 'dir':'EffBothLegs_vs_elesDr_MC_NoahBins', 'col':kBlue , 'mrk':kOpenSquare  , 'source':'root','type':'MC', 'effType':'FullEff','cat':1}),
        ('DoubleMu_ref' , { 'dir':'Noah_results_new/TrigEffs_Data_Incl_6_13_23_drbinned.json'  , 'col':kRed, 'mrk':kFullTriangleDown, 'source':'json','type':'Data', 'effType':'FullEff','cat':2}),
        ('MC'   , { 'dir':'Noah_results_new/TrigEffs_MC_Incl_6_13_23_drbinned.json', 'col':kBlue , 'mrk':kOpenSquare  , 'source':'json','type':'MC', 'effType':'FullEff','cat':2}),])
    ),

    # Eff vs Nvtx Noah's binning
    ('Nvtx', OrderedDict([
        ('SingleEle_ref', { 'dir':'Eff_vs_Nvtx_SingleEleSingleEGL1_NoahBins_eprbCorr', 'col':kBlue , 'mrk':kFullTriangleUp  , 'source':'root', 'type':'Data', 'effType':'FullEff','cat':1}),
        ('MC_FullEff'   , { 'dir':'EffBothLegs_vs_Nvtx_MC_NoahBins', 'col':kBlue , 'mrk':kOpenSquare  , 'source':'root','type':'MC', 'effType':'FullEff','cat':1}),
        ('DoubleMu_ref' , { 'dir':'Noah_results_new/TrigEffs_Data_Incl_6_13_23_npvbinned.json'  , 'col':kRed, 'mrk':kFullTriangleDown, 'source':'json','type':'Data', 'effType':'FullEff','cat':2}),
        ('MC'   , { 'dir':'Noah_results_new/TrigEffs_MC_Incl_6_13_23_npvbinned.json', 'col':kBlue , 'mrk':kOpenSquare  , 'source':'json','type':'MC', 'effType':'FullEff','cat':2}),
        ])
    ),

    # # RefEff data vs MC
    # ('RefNvtx', OrderedDict([
    #     'SingleEle_ref': { 'dir':'RefEff_vs_Nvtx_SingleEleSingleEGL1_NoahBins', 'col':kRed , 'mrk':kFullTriangleUp  , 'source':'root','type':'Data', 'effType':'ProbeEff'},
    #     'MC'           : { 'dir':'RefEff_vs_Nvtx_MC_NoahBins', 'col':kBlue , 'mrk':kOpenSquare  , 'source':'root','type':'MC', 'effType':'ProbeEff'},
    #     ])
    # ),
])
samplesDict = samplesDictAll[args.var]
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
yupp = 3.0
hset.GetYaxis().SetTitle('')
hset.GetYaxis().SetTitleSize( 0.055 )
hset.GetYaxis().SetTitleOffset( 0.95 )
hset.GetYaxis().SetLabelSize( 0.06 )
hset.GetYaxis().SetRangeUser( 0.01, yupp )
hset.GetYaxis().SetNdivisions( 505 )

legend_top = TLegend(0.4, 0.7, 0.95, 0.88)
# legend_top = TLegend(0.65, 0.65, 0.88, 0.88)
legend_top.SetFillStyle(0)
# legend_top.SetNColumns(2)
legend_bot = TLegend(0.35, 0.15, 0.88, 0.28)
legend_bot.SetFillStyle(0)

box = TBox(0.5,0.5,0.9,0.9)
box.SetFillColor(kWhite)

inputjson = {}
heff_temp = {}
teff = {}
inputfile ={}
eff_max = 0

rootoutputdir = "results/"+tag
os.system("mkdir -p "+rootoutputdir)
rootfile = TFile.Open(rootoutputdir+'/scale_factors.root', 'RECREATE')
rootfile.cd()
    
for flag in flaglist:

    print('\n\n'+flag)
    heffData = {}
    heffMC = {}
    hSF = OrderedDict()
    geff = {}

    legend_top.Clear()
    legend_bot.Clear()
    hset.Draw()

    histoSF = {}

    for isample, sample in enumerate(samplesDict.keys()):
        if samplesDict[sample]['source'] == 'root':
            if samplesDict[sample]['type']=='MC':
                print('Adding ',sample, ' to MCSamples')
                inputfilename = maindir+"/"+samplesDict[sample]["dir"]+"/"+flag+"/differential_eff_"+flag+".root"
                inputfile[sample] = TFile.Open(inputfilename)
                teff[sample] = inputfile[sample].Get("htot_clone")
                heff_temp[sample] = teff[sample].CreateGraph()

                xbins = ar.array('d',var['bins'])
                print xbins
                heffMC[sample] = TH1D(sample,'',len(xbins)-1,xbins)

                x = ar.array('d', [0.])
                y = ar.array('d', [0.])
                for ipoint in range(heff_temp[sample].GetN()):
                    heff_temp[sample].GetPoint(ipoint, x, y)
                    heffMC[sample].SetBinContent( heffMC[sample].FindBin(x[0]),  y[0] )
                    heffMC[sample].SetBinError( heffMC[sample].FindBin(x[0]),  heff_temp[sample].GetErrorY(ipoint) )
                    print( 'heffMC', ipoint, x[0],y[0] )
            
            elif samplesDict[sample]['type']=='Data':
                print('Adding ',sample, ' to DataSamples')

                if samplesDict[sample]['effType']=='FullEff':
                    inputfilename = maindir+"/"+samplesDict[sample]["dir"]+"/"+flag+"/FullDoubleEleEff_"+flag+".root"
                    inputfile[sample] = TFile.Open(inputfilename)
                    heff_temp[sample] = inputfile[sample].Get("Graph")
                else:
                    inputfilename = maindir+"/"+samplesDict[sample]["dir"]+"/"+flag+"/differential_eff_"+flag+".root"
                    inputfile[sample] = TFile.Open(inputfilename)
                    teff[sample] = inputfile[sample].Get("htot_clone")
                    heff_temp[sample] = teff[sample].CreateGraph()

                xbins = ar.array('d',var['bins'])
                print(xbins)
                heffData[sample] = TH1D(sample,'',len(xbins)-1,xbins)

                x = ar.array('d', [0.])
                y = ar.array('d', [0.])
                for ipoint in range(heff_temp[sample].GetN()):
                    heff_temp[sample].GetPoint(ipoint, x, y)
                    heffData[sample].SetBinContent( heffData[sample].FindBin(x[0]),  y[0] )
                    heffData[sample].SetBinError( heffData[sample].FindBin(x[0]),  heff_temp[sample].GetErrorY(ipoint) )
                    # print( x[0],y[0] )
                
        elif samplesDict[sample]['source'] == 'json':
            
            if samplesDict[sample]['type'] == 'MC':
                print('Adding ',sample, ' to MCSamples')
                inputjson[sample] = open('results/'+samplesDict[sample]['dir'])
                inputdata = json.load(inputjson[sample])
                trigger_data = inputdata[flaglist[flag]['alias']]

                xbins = ar.array('d',trigger_data[var['alias']])
                xbins.append(var['maxvalue'])

                heffMC[sample] = TH1F(sample,'',len(xbins)-1,xbins)
                for bin in range(len(xbins)-1):
                    # print bin, heff[sample].GetBinLowEdge(bin+1), trigger_data['effs'][bin]
                    if len(trigger_data['effs'][bin])==2:
                        if trigger_data['effs'][bin][0] >0:
                            heffMC[sample].SetBinContent(bin+1, trigger_data['effs'][bin][0])
                            heffMC[sample].SetBinError(bin+1, trigger_data['effs'][bin][1])
                    elif len(trigger_data['effs'][bin])==1:
                        if trigger_data['effs'][bin] >0:
                            heffMC[sample].SetBinContent(bin+1, trigger_data['effs'][bin])
                    print('heffMC', bin, heffMC[sample].GetBinCenter(bin), heffMC[sample].GetBinContent(bin))
                inputjson[sample].close()

            elif samplesDict[sample]['type'] == 'Data':
                print('Adding ',sample, ' to DataSamples')
                inputjson[sample] = open('results/'+samplesDict[sample]['dir'])
                inputdata = json.load(inputjson[sample])
                trigger_data = inputdata[flaglist[flag]['alias']]

                xbins = ar.array('d',trigger_data[var['alias']])
                xbins.append(var['maxvalue'])
                print(xbins)
                heffData[sample] = TH1F(sample,'',len(xbins)-1,xbins)
                for bin in range(len(xbins)-1):
                    # print bin, heff[sample].GetBinLowEdge(bin+1), trigger_data['effs'][bin]
                    if len(trigger_data['effs'][bin])==2:
                        if trigger_data['effs'][bin][0] >0:
                            heffData[sample].SetBinContent(bin+1, trigger_data['effs'][bin][0])
                            heffData[sample].SetBinError(bin+1, trigger_data['effs'][bin][1])
                    elif len(trigger_data['effs'][bin])==1:
                        if trigger_data['effs'][bin] >0:
                            heffData[sample].SetBinContent(bin+1, trigger_data['effs'][bin])
                    print('heffDataNoah', bin+1, heffData[sample].GetBinCenter(bin+1), heffData[sample].GetBinContent(bin+1))
                inputjson[sample].close()

            
    for DataSample in heffData.keys():
        # print('Eval SF for ',DataSample)
        for MCSample in heffMC.keys():
            
            if samplesDict[DataSample]['cat'] != samplesDict[MCSample]['cat']:
                continue
            
            heffData[DataSample].Divide(heffMC[MCSample])
            hSF[flag+"_"+DataSample+"_vs_"+MCSample+"_"+args.var] = heffData[DataSample].Clone('h_'+flag+"_"+DataSample+"_vs_"+MCSample+"_"+args.var)
            # print(hSF)    
            for bin in range(len(xbins)-1):
                print('hsf', bin, hSF[flag+"_"+DataSample+"_vs_"+MCSample+"_"+args.var].GetBinCenter(bin), hSF[flag+"_"+DataSample+"_vs_"+MCSample+"_"+args.var].GetBinContent(bin))
                

    arrows_sample = []
    for isample, sample in enumerate(hSF.keys()):
        print(sample)   

        X = ar.array('d',[0.])
        Y = ar.array('d',[0.])
        geff[sample] = TGraphErrors(hSF[sample].GetNbinsX()+1)
        arrows_sample.append([])
        for ibin in range(hSF[sample].GetNbinsX()+1):

            geff[sample].SetPoint(ibin, hSF[sample].GetBinCenter(ibin), hSF[sample].GetBinContent(ibin))
            geff[sample].SetPointError(ibin, hSF[sample].GetBinWidth(ibin)*0.5, hSF[sample].GetBinError(ibin))

            geff[sample].GetPoint(ibin,X,Y)
            
            if Y[0] > yupp:
                print("Y gtr than yupp ",Y)
                arrows_sample[-1].append(TArrow(X[0]*(1+isample*0.03), yupp*0.95, X[0]*(1+isample*0.03), yupp, 0.02, ">"))
                print arrows_sample
                print arrows_sample[-1][-1]
                arrows_sample[-1][-1].SetAngle(60)
                arrows_sample[-1][-1].SetLineColor(isample+1)
                arrows_sample[-1][-1].SetLineWidth(2)
                arrows_sample[-1][-1].Draw()
                # arrow = TArrow(X[0], yupp*0.95, X[0], yupp, 0.02, ">")
                # arrow.SetAngle(60)
                # arrow.SetLineColor(isample+1)
                # arrow.SetLineWidth(2)
                # arrow.Draw()

        geff_name = sample.replace('h_','')        
        geff_name = sample.replace('_'+args.var,'')        
        geff_name = geff_name.replace(flag+'_', '')
        geff_name = geff_name.replace('_FullEff', '')
        geff_name = geff_name.replace('_ref', 'Ref')
        # for flag_tmp in flaglist:
        #     if flag in geff_name:
        #         geff_name = geff_name.replace(flag+'_', '')

        geff[sample].SetName(geff_name)
        geff[sample].SetMarkerStyle(isample+8)
        geff[sample].SetMarkerColor(isample+1)
        geff[sample].SetMarkerSize(1)
        geff[sample].SetLineColor(isample+1)
        # geff[sample].SetLineWidth(2)

        # for ipoint in range(hSF[sample].GetN()):
        #     hSF[sample].SetPointEXlow(ipoint, 0) 
        #     hSF[sample].SetPointEXhigh(ipoint, 0) 

        geff[sample].Draw("same P")
        rootfile.cd()
        geff[sample].Write()
        # eff_lastbin = hSF[sample].GetEfficiency(5)
        # print eff_lastbin
        # if eff_lastbin>eff_max:
        #     eff_max = eff_lastbin

        legend_top.AddEntry(geff[sample], geff[sample].GetName(), "pl")
        legend_bot.AddEntry(geff[sample], geff[sample].GetName(), "pl")

    legend_top.Draw("same")

    outputdir = "/afs/cern.ch/user/c/cquarant/www/DoubleEleTriggerStudy/tnpPlots_2022_final/"+tag
    os.system("mkdir -p "+outputdir)
    canvas.SaveAs(outputdir+"/"+flag+"_"+tag+".png")
    os.system("cp /afs/cern.ch/user/c/cquarant/www/DoubleEleTriggerStudy/index.php "+outputdir)

rootfile.Write()
rootfile.Close()

    
    