import os

aliaslist = {
    'e2Pt' : 'JpsiKE_e2_pt',
    'e2Eta': 'JpsiKE_e2_eta',
    'elesDr' : 'JpsiKE_elesDr',
    'Nvtx' : 'Nvtx',
}

for var in ['e2Pt','Nvtx','elesDr','e2Eta']:#
# for var in ['Nvtx','ProbePt','ProbeEta','elesDr']:
    # os.system(f'python scripts/set_and_launch_fit.py -s etc/config/SingleEleSEGL1_cfg/settings_SingleEleSingleEGL1_{var}.py')
    # os.system(f'python scripts/set_and_launch_fit.py -s etc/config/MC_cfg/settings_MC_RefEff_eprb_vs_{var}.py')
    # os.system(f'python scripts/compare_eff.py -v {aliaslist[var]} -t Comparison_FullEff_MC_Data_Noah_{var}' )
    os.system(f'python scripts/eval_SF.py -v {aliaslist[var]} -t SF_FullEffDataOverMCSeparateCat_{var}' )