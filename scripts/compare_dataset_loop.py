import os
import sys

import ROOT

ROOT.gStyle.SetOptStat(0)

dirname = 'Distributions_e1Pt_gtr_10'

varlist = {
    'DeltaR'        : {'name' : 'JpsiKE_elesDr', 'xmin' : 0, 'xmax' : 0.75},
    'nvtx'          : {'name' : 'nvtx'         , 'xmin' : 0, 'xmax' : 73},
    'JpsiKE_e1_pt'  : {'name' : 'JpsiKE_e1_pt' , 'xmin' : 0, 'xmax' : 60}, 
    'JpsiKE_e2_pt'  : {'name' : 'JpsiKE_e2_pt' , 'xmin' : 0, 'xmax' : 60}, 
    'JpsiKE_e1_eta' : {'name' : 'JpsiKE_e1_eta', 'xmin' : -1.25, 'xmax' : 1.25}, 
    'JpsiKE_e2_eta' : {'name' : 'JpsiKE_e1_eta', 'xmin' : -1.25, 'xmax' : 1.25}
    }
# varlist = ['JpsiKE_elesDr']

datasetlist = {
    'MC_new' : { 'file' : '/afs/cern.ch/work/c/cquarant/RKanalysis/mc/merged_BuToJpsiKEE/Jpsi_BuToJpsiKEE_SingleEleIncluded.root',
                 'col'  : ROOT.kRed
    },
    
    'MC_old' : {'file' : '/afs/cern.ch/work/c/cquarant/RKanalysis/mc/merged_BuToJpsiKEE/Jpsi_BuToJpsiKEE_realisticPU_MC.root',
                'col'  : ROOT.kGreen
    },

    'Data_SingleEle' : {'file' : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/merged_12Dec2022/JPsi_SingleEle_controlTrigger_2022FG.root',
                        'col'  : ROOT.kBlack
    },
    
}

rf = {}
tree = {}
hist = {}


for var in varlist:
    
    for tag in datasetlist.keys():
        
        rf[tag] = ROOT.TFile.Open(datasetlist[tag]['file'])
        tree[tag] = rf[tag].Get('nano_/tree')
        
        selection = ('JpsiKE_Jpsi_mass_nofit>2.10001 && JpsiKE_Jpsi_mass_nofit<3.61'
                    ' & abs(JpsiKE_e1_eta)<1.22 & abs(JpsiKE_e2_eta)<1.22 '
                    ' & JpsiKE_e1_pt>10.0 & JpsiKE_e2_pt>5.0 & JpsiKE_e1_passMVA==1 & JpsiKE_e2_passMVA==1'
                    )
        
        # Create two histograms
        xmin = str(varlist[var]['xmin'])
        xmax = str(varlist[var]['xmax'])
        if var == 'nvtx':
            tree[tag].Draw(varlist[var]['name'],selection)
            hist[tag] = ROOT.gPad.GetPrimitive('htemp').Clone('h_'+var+'_'+tag)
        else:
            tree[tag].Draw(varlist[var]['name']+'>>h(45,'+xmin+','+xmax+')',selection)
            hist[tag] = ROOT.gPad.GetPrimitive('h').Clone('h_'+var+'_'+tag)
        hist[tag].Scale(1.0/hist[tag].Integral())
        
        # Set histogram colors and styles
        hist[tag].SetTitle('')
        hist[tag].SetLineColor(datasetlist[tag]['col'])
        hist[tag].SetLineWidth(2)

    
    # Create a ROOT canvas
    canvas = ROOT.TCanvas(var+"_Distribution_Comparison", var+"_Distribution_Comparison", 800, 600)
    canvas.cd()
    count = 0
    
    # Create a legend
    legend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)

    ymax = 0
    for tag in hist.keys():
        if hist[tag].GetMaximum() > ymax:
            ymax = hist[tag].GetMaximum()

    for tag in hist.keys():
        # Draw the first histogram
        legend.AddEntry(hist[tag], tag, "l")
        if count == 0: 
            print('first hist')
            hist[tag].Draw('h')
            hist[tag].GetXaxis().SetTitle(var)
            hist[tag].GetYaxis().SetTitle("Entries")
            if 'pt' in var:
                hist[tag].GetXaxis().SetRangeUser(0,60)
            hist[tag].GetYaxis().SetRangeUser(0,ymax*1.1)
            # hist[tag].GetYaxis().SetTitleOffset(1.2)
            count = 1
        # Draw the second histogram on the same canvas
        else:
            print('other hist')
            hist[tag].Draw("hsame")
    
    legend.Draw('same')
    
    # Keep the canvas open
    # canvas.Modified()
    canvas.Update()
    canvas.SaveAs(var+"_histogram_comparison.png")

    os.system('mkdir -p /afs/cern.ch/user/c/cquarant/www/DoubleEleTriggerStudy/'+dirname)
    os.system('cp /afs/cern.ch/user/c/cquarant/www/DoubleEleTriggerStudy/index.php /afs/cern.ch/user/c/cquarant/www/DoubleEleTriggerStudy/'+dirname)
    os.system('mv *histogram_comparison.png /afs/cern.ch/user/c/cquarant/www/DoubleEleTriggerStudy/'+dirname)