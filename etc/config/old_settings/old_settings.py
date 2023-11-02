#############################################################
# General settings

# flag to be Tested
doubleEle10Fired  = 'DoubleEle10_fired==1' 
doubleEle10ProbeMatched  = 'DoubleEle10_fired==1 & ((JpsiKE_e1_trgobj_pt<0 & JpsiKE_e1_Ele10_match==1) || (JpsiKE_e2_trgobj_pt<0 & JpsiKE_e2_Ele10_match==1) || (JpsiKE_e1_trgobj_pt>0 & JpsiKE_e2_trgobj_pt>0 & JpsiKE_e1_Ele10_match+JpsiKE_e2_Ele10_match>0))'
doubleEle10BothMatched = 'DoubleEle10_fired==1 && (  JpsiKE_e1_Ele10_match==1 && JpsiKE_e2_Ele10_match==1 )'

doubleEle9p5Fired = 'DoubleEle9p5_fired==1' 
doubleEle9p5ProbeMatched  = 'DoubleEle9p5_fired==1 && ( (JpsiKE_e1_trgobj_pt<0 && JpsiKE_e1_Ele9p5_match==1) || (JpsiKE_e2_trgobj_pt<0 && JpsiKE_e2_Ele9p5_match==1)|| (JpsiKE_e1_trgobj_pt>0 & JpsiKE_e2_trgobj_pt>0 & JpsiKE_e1_Ele9p5_match+JpsiKE_e2_Ele9p5_match>0))'
doubleEle9p5BothMatched = 'DoubleEle9p5_fired==1 && (  JpsiKE_e1_Ele9p5_match==1 && JpsiKE_e2_Ele9p5_match==1 )'

doubleEle9Fired   = 'DoubleEle9_fired==1' 
doubleEle9ProbeMatched  = 'DoubleEle9_fired==1 && ( (JpsiKE_e1_trgobj_pt<0 && JpsiKE_e1_Ele9_match==1) || (JpsiKE_e2_trgobj_pt<0 && JpsiKE_e2_Ele9_match==1)|| (JpsiKE_e1_trgobj_pt>0 & JpsiKE_e2_trgobj_pt>0 & JpsiKE_e1_Ele9_match+JpsiKE_e2_Ele9_match>0))'
doubleEle9BothMatched = 'DoubleEle9_fired==1 && (  JpsiKE_e1_Ele9_match==1 && JpsiKE_e2_Ele9_match==1 )'

doubleEle8p5Fired = 'DoubleEle8p5_fired==1' 
doubleEle8p5ProbeMatched  = 'DoubleEle8p5_fired==1 && ( (JpsiKE_e1_trgobj_pt<0 && JpsiKE_e1_Ele8p5_match==1) || (JpsiKE_e2_trgobj_pt<0 && JpsiKE_e2_Ele8p5_match==1)|| (JpsiKE_e1_trgobj_pt>0 & JpsiKE_e2_trgobj_pt>0 & JpsiKE_e1_Ele8p5_match+JpsiKE_e2_Ele8p5_match>0))'
doubleEle8p5BothMatched = 'DoubleEle8p5_fired==1 && (  JpsiKE_e1_Ele8p5_match==1 && JpsiKE_e2_Ele8p5_match==1 )'

doubleEle8Fired   = 'DoubleEle8_fired==1' 
doubleEle8ProbeMatched  = 'DoubleEle8_fired==1 && ( (JpsiKE_e1_trgobj_pt<0 && JpsiKE_e1_Ele8_match==1) || (JpsiKE_e2_trgobj_pt<0 && JpsiKE_e2_Ele8_match==1)|| (JpsiKE_e1_trgobj_pt>0 & JpsiKE_e2_trgobj_pt>0 & JpsiKE_e1_Ele8_match+JpsiKE_e2_Ele8_match>0))'
doubleEle8BothMatched = 'DoubleEle8_fired==1 && (  JpsiKE_e1_Ele8_match==1 && JpsiKE_e2_Ele8_match==1 )'

doubleEle7p5Fired = 'DoubleEle7p5_fired==1' 
doubleEle7p5ProbeMatched  = 'DoubleEle7p5_fired==1 && ( (JpsiKE_e1_trgobj_pt<0 && JpsiKE_e1_Ele7p5_match==1) || (JpsiKE_e2_trgobj_pt<0 && JpsiKE_e2_Ele7p5_match==1)|| (JpsiKE_e1_trgobj_pt>0 & JpsiKE_e2_trgobj_pt>0 & JpsiKE_e1_Ele7p5_match+JpsiKE_e2_Ele7p5_match>0))'
doubleEle7p5BothMatched = 'DoubleEle7p5_fired==1 && (  JpsiKE_e1_Ele7p5_match==1 && JpsiKE_e2_Ele7p5_match==1 )'

doubleEle7Fired   = 'DoubleEle7_fired==1' 
doubleEle7ProbeMatched  = 'DoubleEle7_fired==1 && ( (JpsiKE_e1_trgobj_pt<0 && JpsiKE_e1_Ele7_match==1) || (JpsiKE_e2_trgobj_pt<0 && JpsiKE_e2_Ele7_match==1)|| (JpsiKE_e1_trgobj_pt>0 & JpsiKE_e2_trgobj_pt>0 & JpsiKE_e1_Ele7_match+JpsiKE_e2_Ele7_match>0))'
doubleEle7BothMatched = 'DoubleEle7_fired==1 && (  JpsiKE_e1_Ele7_match==1 && JpsiKE_e2_Ele7_match==1 )'

doubleEle6p5Fired = 'DoubleEle6p5_fired==1' 
doubleEle6p5ProbeMatched  = 'DoubleEle6p5_fired==1 && ( (JpsiKE_e1_trgobj_pt<0 && JpsiKE_e1_Ele6p5_match==1) || (JpsiKE_e2_trgobj_pt<0 && JpsiKE_e2_Ele6p5_match==1)|| (JpsiKE_e1_trgobj_pt>0 & JpsiKE_e2_trgobj_pt>0 & JpsiKE_e1_Ele6p5_match+JpsiKE_e2_Ele6p5_match>0))'
doubleEle6p5BothMatched = 'DoubleEle6p5_fired==1 && (  JpsiKE_e1_Ele6p5_match==1 && JpsiKE_e2_Ele6p5_match==1 )'

doubleEle6p5FiredL1_11p0_Match = 'DoubleEle6p5_fired==1 && JpsiKE_e1_bestL1pt>11.0 && JpsiKE_e2_bestL1pt > 11.0' 
doubleEle6p5ProbeMatchedL1_11p0_Match  = 'DoubleEle6p5_fired==1 && ( (JpsiKE_e1_trgobj_pt<0 && JpsiKE_e1_Ele6p5_match==1) || (JpsiKE_e2_trgobj_pt<0 && JpsiKE_e2_Ele6p5_match==1)|| (JpsiKE_e1_trgobj_pt>0 & JpsiKE_e2_trgobj_pt>0 & JpsiKE_e1_Ele6p5_match+JpsiKE_e2_Ele6p5_match>0))  && JpsiKE_e1_bestL1pt>11.0 && JpsiKE_e2_bestL1pt > 11.0'
doubleEle6p5BothMatchedL1_11p0_Match = 'DoubleEle6p5_fired==1 && (  JpsiKE_e1_Ele6p5_match==1 && JpsiKE_e2_Ele6p5_match==1 )  && JpsiKE_e1_bestL1pt>11.0 && JpsiKE_e2_bestL1pt > 11.0'

doubleEle6p5FiredL1_10p5_Match = 'DoubleEle6p5_fired==1 && JpsiKE_e1_bestL1pt>10.5 && JpsiKE_e2_bestL1pt > 10.5' 
doubleEle6p5ProbeMatchedL1_10p5_Match  = 'DoubleEle6p5_fired==1 && ( (JpsiKE_e1_trgobj_pt<0 && JpsiKE_e1_Ele6p5_match==1) || (JpsiKE_e2_trgobj_pt<0 && JpsiKE_e2_Ele6p5_match==1)|| (JpsiKE_e1_trgobj_pt>0 & JpsiKE_e2_trgobj_pt>0 & JpsiKE_e1_Ele6p5_match+JpsiKE_e2_Ele6p5_match>0))  && JpsiKE_e1_bestL1pt>10.5 && JpsiKE_e2_bestL1pt > 10.5'
doubleEle6p5BothMatchedL1_10p5_Match = 'DoubleEle6p5_fired==1 && (  JpsiKE_e1_Ele6p5_match==1 && JpsiKE_e2_Ele6p5_match==1 )  && JpsiKE_e1_bestL1pt>10.5 && JpsiKE_e2_bestL1pt > 10.5'

doubleEle6p5FiredL1_9p5_Match = 'DoubleEle6p5_fired==1 && JpsiKE_e1_bestL1pt>9.5 && JpsiKE_e2_bestL1pt > 9.5' 
doubleEle6p5ProbeMatchedL1_9p5_Match  = 'DoubleEle6p5_fired==1 && ( (JpsiKE_e1_trgobj_pt<0 && JpsiKE_e1_Ele6p5_match==1) || (JpsiKE_e2_trgobj_pt<0 && JpsiKE_e2_Ele6p5_match==1)|| (JpsiKE_e1_trgobj_pt>0 & JpsiKE_e2_trgobj_pt>0 & JpsiKE_e1_Ele6p5_match+JpsiKE_e2_Ele6p5_match>0))  && JpsiKE_e1_bestL1pt>9.5 && JpsiKE_e2_bestL1pt > 9.5'

doubleEle6Fired   = 'DoubleEle6_fired==1' 
doubleEle6ProbeMatched  = 'DoubleEle6_fired==1 && ( (JpsiKE_e1_trgobj_pt<0 && JpsiKE_e1_Ele6_match==1) || (JpsiKE_e2_trgobj_pt<0 && JpsiKE_e2_Ele6_match==1)|| (JpsiKE_e1_trgobj_pt>0 & JpsiKE_e2_trgobj_pt>0 & JpsiKE_e1_Ele6_match+JpsiKE_e2_Ele6_match>0))'
doubleEle6BothMatched = 'DoubleEle6_fired==1 && (  JpsiKE_e1_Ele6_match==1 && JpsiKE_e2_Ele6_match==1 )'

doubleEle5p5Fired = 'DoubleEle5p5_fired==1' 
doubleEle5p5ProbeMatched  = 'DoubleEle5p5_fired==1 && ( (JpsiKE_e1_trgobj_pt<0 && JpsiKE_e1_Ele5p5_match==1) || (JpsiKE_e2_trgobj_pt<0 && JpsiKE_e2_Ele5p5_match==1)|| (JpsiKE_e1_trgobj_pt>0 & JpsiKE_e2_trgobj_pt>0 & JpsiKE_e1_Ele5p5_match+JpsiKE_e2_Ele5p5_match>0))'
doubleEle5p5BothMatched = 'DoubleEle5p5_fired==1 && (  JpsiKE_e1_Ele5p5_match==1 && JpsiKE_e2_Ele5p5_match==1 )'

doubleEle5Fired   = 'DoubleEle5_fired==1' 
doubleEle5ProbeMatched  = 'DoubleEle5_fired==1 && ( (JpsiKE_e1_trgobj_pt<0 && JpsiKE_e1_Ele5_match==1) || (JpsiKE_e2_trgobj_pt<0 && JpsiKE_e2_Ele5_match==1)|| (JpsiKE_e1_trgobj_pt>0 & JpsiKE_e2_trgobj_pt>0 & JpsiKE_e1_Ele5_match+JpsiKE_e2_Ele5_match>0))'
doubleEle5BothMatched = 'DoubleEle5_fired==1 && (  JpsiKE_e1_Ele5_match==1 && JpsiKE_e2_Ele5_match==1 )'

doubleEle4p5Fired = 'DoubleEle4p5_fired==1' 
doubleEle4p5ProbeMatched  = 'DoubleEle4p5_fired==1 && ( (JpsiKE_e1_trgobj_pt<0 && JpsiKE_e1_Ele4p5_match==1) || (JpsiKE_e2_trgobj_pt<0 && JpsiKE_e2_Ele4p5_match==1)|| (JpsiKE_e1_trgobj_pt>0 & JpsiKE_e2_trgobj_pt>0 & JpsiKE_e1_Ele4p5_match+JpsiKE_e2_Ele4p5_match>0))'
doubleEle4p5BothMatched = 'DoubleEle4p5_fired==1 && (  JpsiKE_e1_Ele4p5_match==1 && JpsiKE_e2_Ele4p5_match==1 )'

doubleEle4Fired   = 'DoubleEle4_fired==1' 
doubleEle4ProbeMatched  = 'DoubleEle4_fired==1 && ( (JpsiKE_e1_trgobj_pt<0 && JpsiKE_e1_Ele4_match==1) || (JpsiKE_e2_trgobj_pt<0 && JpsiKE_e2_Ele4_match==1)|| (JpsiKE_e1_trgobj_pt>0 & JpsiKE_e2_trgobj_pt>0 & JpsiKE_e1_Ele4_match+JpsiKE_e2_Ele4_match>0))'
doubleEle4BothMatched = 'DoubleEle4_fired==1 && (  JpsiKE_e1_Ele4_match==1 && JpsiKE_e2_Ele4_match==1 )'


doubleEle4BothMatchedL1_4p5_Match = 'DoubleEle4_fired==1 && (JpsiKE_e1_Ele4_match==1 && JpsiKE_e2_Ele4_match==1) && JpsiKE_e1_bestL1pt>4.5 && JpsiKE_e2_bestL1pt>4.5 & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.001 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.001'
doubleEle4BothMatchedL1_5p0_Match = 'DoubleEle4_fired==1 && (JpsiKE_e1_Ele4_match==1 && JpsiKE_e2_Ele4_match==1) && JpsiKE_e1_bestL1pt>5.0 && JpsiKE_e2_bestL1pt>5.0 & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.001 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.001'
doubleEle4BothMatchedL1_5p5_Match = 'DoubleEle4_fired==1 && (JpsiKE_e1_Ele4_match==1 && JpsiKE_e2_Ele4_match==1) && JpsiKE_e1_bestL1pt>5.5 && JpsiKE_e2_bestL1pt>5.5 & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.001 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.001'
doubleEle4BothMatchedL1_6p0_Match = 'DoubleEle4_fired==1 && (JpsiKE_e1_Ele4_match==1 && JpsiKE_e2_Ele4_match==1) && JpsiKE_e1_bestL1pt>6.0 && JpsiKE_e2_bestL1pt>6.0 & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.001 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.001'
doubleEle4p5BothMatchedL1_6p5_Match = 'DoubleEle4p5_fired==1 && (JpsiKE_e1_Ele4p5_match==1 && JpsiKE_e2_Ele4p5_match==1)  && JpsiKE_e1_bestL1pt>6.5 && JpsiKE_e2_bestL1pt>6.5 & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.001 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.001'
doubleEle5BothMatchedL1_7p0_Match = 'DoubleEle5_fired==1 && (JpsiKE_e1_Ele5_match==1 && JpsiKE_e2_Ele5_match==1) && JpsiKE_e1_bestL1pt>7.0  && JpsiKE_e2_bestL1pt>7.0 & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.001 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.001'
doubleEle5BothMatchedL1_7p5_Match = 'DoubleEle5_fired==1 && (JpsiKE_e1_Ele5_match==1 && JpsiKE_e2_Ele5_match==1) && JpsiKE_e1_bestL1pt>7.5  && JpsiKE_e2_bestL1pt>7.5 & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.001 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.001'
doubleEle5BothMatchedL1_8p0_Match = 'DoubleEle5_fired==1 && (JpsiKE_e1_Ele5_match==1 && JpsiKE_e2_Ele5_match==1) && JpsiKE_e1_bestL1pt>8.0  && JpsiKE_e2_bestL1pt>8.0 & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.001 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.001'
doubleEle5BothMatchedL1_8p5_Match = 'DoubleEle5_fired==1 && (JpsiKE_e1_Ele5_match==1 && JpsiKE_e2_Ele5_match==1) && JpsiKE_e1_bestL1pt>8.5  && JpsiKE_e2_bestL1pt>8.5 & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.001 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.001'
doubleEle5BothMatchedL1_10p5_Match= 'DoubleEle5_fired==1 && (JpsiKE_e1_Ele5_match==1 && JpsiKE_e2_Ele5_match==1) && JpsiKE_e1_bestL1pt>10.5 && JpsiKE_e2_bestL1pt>10.5 & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.001 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.001'
doubleEle5p5BothMatchedL1_8p5_Match= 'DoubleEle5p5_fired==1 && (JpsiKE_e1_Ele5p5_match==1 && JpsiKE_e2_Ele5p5_match==1) && JpsiKE_e1_bestL1pt>8.5 && JpsiKE_e2_bestL1pt>8.5 & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.001 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.001'
doubleEle6BothMatchedL1_5p5_Match = 'DoubleEle6_fired==1 && (JpsiKE_e1_Ele6_match==1 && JpsiKE_e2_Ele6_match==1) && JpsiKE_e1_bestL1pt>5.5  && JpsiKE_e2_bestL1pt>5.5 & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.001 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.001'
doubleEle6BothMatchedL1_9p0_Match = 'DoubleEle6_fired==1 && (JpsiKE_e1_Ele6_match==1 && JpsiKE_e2_Ele6_match==1) && JpsiKE_e1_bestL1pt>9.0  && JpsiKE_e2_bestL1pt>9.0 & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.001 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.001'
doubleEle6p5BothMatchedL1_9p5_Match = 'DoubleEle6p5_fired==1 && (  JpsiKE_e1_Ele6p5_match==1 && JpsiKE_e2_Ele6p5_match==1 )  && JpsiKE_e1_bestL1pt>9.5 && JpsiKE_e2_bestL1pt > 9.5 & JpsiKE_e1_bestL1pt>0 & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.001 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.001'
doubleEle6p5BothMatchedL1_10p5_Match = 'DoubleEle6p5_fired==1 && (  JpsiKE_e1_Ele6p5_match==1 && JpsiKE_e2_Ele6p5_match==1 )  && JpsiKE_e1_bestL1pt>10.5 && JpsiKE_e2_bestL1pt > 10.5 & JpsiKE_e1_bestL1pt>0 & JpsiKE_e2_bestL1pt>0 & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.001 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.001'
doubleEle6p5BothMatchedL1_11p0_Match = 'DoubleEle6p5_fired==1 && (  JpsiKE_e1_Ele6p5_match==1 && JpsiKE_e2_Ele6p5_match==1 )  && JpsiKE_e1_bestL1pt>11.0 && JpsiKE_e2_bestL1pt > 11.0 & JpsiKE_e1_bestL1pt>0 & JpsiKE_e2_bestL1pt>0 & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.001 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.001'

# flag to be Tested
flags = {
    'doubleEle10Fired' : doubleEle10Fired,
    'doubleEle10ProbeMatched' : doubleEle10ProbeMatched,
    'doubleEle10BothMatched': doubleEle10BothMatched,

    'doubleEle9p5Fired': doubleEle9p5Fired,
    'doubleEle9p5ProbeMatched' : doubleEle9p5ProbeMatched,
    'doubleEle9p5BothMatched': doubleEle9p5BothMatched,

    'doubleEle9Fired'  : doubleEle9Fired,
    'doubleEle9ProbeMatched' : doubleEle9ProbeMatched,
    'doubleEle9BothMatched': doubleEle9BothMatched,

    'doubleEle8p5Fired': doubleEle8p5Fired,
    'doubleEle8p5ProbeMatched' : doubleEle8p5ProbeMatched,
    'doubleEle8p5BothMatched': doubleEle8p5BothMatched,

    'doubleEle8Fired'  : doubleEle8Fired,
    'doubleEle8ProbeMatched' : doubleEle8ProbeMatched,
    'doubleEle8BothMatched': doubleEle8BothMatched,

    'doubleEle7p5Fired': doubleEle7p5Fired,
    'doubleEle7p5ProbeMatched' : doubleEle7p5ProbeMatched,
    'doubleEle7p5BothMatched': doubleEle7p5BothMatched,

    'doubleEle7Fired'  : doubleEle7Fired,
    'doubleEle7ProbeMatched' : doubleEle7ProbeMatched,
    'doubleEle7BothMatched': doubleEle7BothMatched,

    'doubleEle6p5Fired': doubleEle6p5Fired,
    'doubleEle6p5ProbeMatched' : doubleEle6p5ProbeMatched,
    'doubleEle6p5BothMatched': doubleEle6p5BothMatched,
    'doubleEle6p5FiredL1_11p0_Match': doubleEle6p5FiredL1_11p0_Match,
    'doubleEle6p5ProbeMatchedL1_11p0_Match' : doubleEle6p5ProbeMatchedL1_11p0_Match,
    'doubleEle6p5FiredL1_10p5_Match': doubleEle6p5FiredL1_10p5_Match,
    'doubleEle6p5ProbeMatchedL1_10p5_Match' : doubleEle6p5ProbeMatchedL1_10p5_Match,
    'doubleEle6p5FiredL1_9p5_Match': doubleEle6p5FiredL1_9p5_Match,
    'doubleEle6p5ProbeMatchedL1_9p5_Match' : doubleEle6p5ProbeMatchedL1_9p5_Match,

    'doubleEle6Fired'  : doubleEle6Fired,
    'doubleEle6ProbeMatched' : doubleEle6ProbeMatched,
    'doubleEle6BothMatched': doubleEle6BothMatched,

    'doubleEle5p5Fired': doubleEle5p5Fired,
    'doubleEle5p5ProbeMatched' : doubleEle5p5ProbeMatched,
    'doubleEle5p5BothMatched': doubleEle5p5BothMatched,

    'doubleEle5Fired'  : doubleEle5Fired,
    'doubleEle5ProbeMatched' : doubleEle5ProbeMatched,
    'doubleEle5BothMatched': doubleEle5BothMatched,

    'doubleEle4p5Fired': doubleEle4p5Fired,
    'doubleEle4p5ProbeMatched' : doubleEle4p5ProbeMatched,
    'doubleEle4p5BothMatched': doubleEle4p5BothMatched,

    'doubleEle4Fired'  : doubleEle4Fired,
    'doubleEle4ProbeMatched' : doubleEle4ProbeMatched,
    'doubleEle4BothMatched': doubleEle4BothMatched,

    'doubleEle4BothMatchedL1_4p5_Match'   : doubleEle4BothMatchedL1_4p5_Match,
    'doubleEle4BothMatchedL1_5p0_Match'   : doubleEle4BothMatchedL1_5p0_Match,
    'doubleEle4BothMatchedL1_5p5_Match'   : doubleEle4BothMatchedL1_5p5_Match,
    'doubleEle4BothMatchedL1_6p0_Match'   : doubleEle4BothMatchedL1_6p0_Match,
    'doubleEle4p5BothMatchedL1_6p5_Match' : doubleEle4p5BothMatchedL1_6p5_Match,
    'doubleEle5BothMatchedL1_7p0_Match'   : doubleEle5BothMatchedL1_7p0_Match,
    'doubleEle5BothMatchedL1_7p5_Match'   : doubleEle5BothMatchedL1_7p5_Match,
    'doubleEle5BothMatchedL1_8p0_Match'   : doubleEle5BothMatchedL1_8p0_Match,
    'doubleEle5BothMatchedL1_8p5_Match'   : doubleEle5BothMatchedL1_8p5_Match,
    'doubleEle5BothMatchedL1_10p5_Match'  : doubleEle5BothMatchedL1_10p5_Match,
    'doubleEle5p5BothMatchedL1_8p5_Match' : doubleEle5p5BothMatchedL1_8p5_Match,
    'doubleEle6BothMatchedL1_5p5_Match'   : doubleEle6BothMatchedL1_5p5_Match,
    'doubleEle6BothMatchedL1_9p0_Match'   : doubleEle6BothMatchedL1_9p0_Match,
    'doubleEle6p5BothMatchedL1_9p5_Match' : doubleEle6p5BothMatchedL1_9p5_Match,
    'doubleEle6p5BothMatchedL1_10p5_Match': doubleEle6p5BothMatchedL1_10p5_Match,
    'doubleEle6p5BothMatchedL1_11p0_Match': doubleEle6p5BothMatchedL1_11p0_Match,

    }

# FINAL EFFICIENCY DEFINITION

#baseOutDir = 'results/doubleEleFired_ElePlusJet_2022CDEFG_final'
#baseOutDir = 'results/doubleEleFired_ElePlusJet_2022CDEFG_final_rebinned'
#baseOutDir = 'results/doubleEleFired_SingleEle_SingleEGL1_2022FG_final'
#baseOutDir = 'results/doubleEleFired_SingleEle_SingleEGL1_2022FG_final_rebinned'
baseOutDir = 'results/doubleEleFired_SingleEle_DiEleEGL1_2022FG_final'
#baseOutDir = 'results/doubleEleFired_MC_BuTOjpsiKEE_realisticPU_final'

##########################################################################
################# OLD EFFICIENCY DEFINITIONS #############################
##########################################################################

#baseOutDir = 'results/doubleEleFired_MC_BuTOjpsiKEE'
#baseOutDir = 'results/doubleEleFired_MC_BuTOjpsiKEE_passMVA'
#baseOutDir = 'results/doubleEleFired_MC_BuTOjpsiKEE_passMVA_binned'
#baseOutDir = 'results/doubleEleFired_MC_BuTOjpsiKEE_L1match'
#baseOutDir = 'results/doubleEleFired_MC_BuTOjpsiKEE_passMVA_binnedMC'

#baseOutDir = 'results/doubleEleFired_ElePlusJet_2022CDEF'
#baseOutDir = 'results/doubleEleFired_ElePlusJet_2022CDEF_L1match'
#baseOutDir = 'results/doubleEleFired_ElePlusJet_2022CDEF_L1match_json'
#baseOutDir = 'results/doubleEleFired_ElePlusJet_2022CDEF_passMVA'
#baseOutDir = 'results/doubleEleFired_ElePlusJet_2022CDEF_passMVA_binned'
#baseOutDir = 'results/doubleEleFired_ElePlusJet_2022CDEF_passMVA_binnedMC'

#baseOutDir = 'results/doubleEleFired_SingleEle_2022F'
#baseOutDir = 'results/doubleEleFired_SingleEle_2022F_L1match'
#baseOutDir = 'results/doubleEleFired_SingleEle_2022F_L1match_json'
#baseOutDir = 'results/doubleEleFired_SingleEle_2022F_passMVA_binned'
#baseOutDir = 'results/doubleEleFired_SingleEle_2022F_passMVA_binnedMC'

#baseOutDir = 'results/doubleEleFired_SingleEleDiEleL1_2022F_L1match'
#baseOutDir = 'results/doubleEleFired_SingleEleDiEleL1_2022F_L1match_json'
#baseOutDir = 'results/doubleEleFired_SingleEleDiEleL1_2022F_passMVA'
#baseOutDir = 'results/doubleEleFired_SingleEleDiEleL1_2022F_passMVA_binned'
#baseOutDir = 'results/doubleEleFired_SingleEleDiEleL1_2022F_passMVA_binnedMC'

#############################################################
# Samples definition  - preparing the samples

### samples are defined in etc/inputs/tnpSampleDef.py
### not: you can setup another sampleDef File in inputs
import etc.inputs.tnpSampleDef as tnpSamples
tnpTreeDir = 'nano_'

samplesDef = {
    #'data'   : tnpSamples.Parking_doubleEle_run3['data_Run2022C-Prompt'].clone(),
    #'data'   : tnpSamples.Parking_doubleEle_run3['data_Run2022CD-Prompt'].clone(),
    #'data'   : tnpSamples.Parking_doubleEle_run3['data_Run2022EF-Prompt'].clone(),

    #'data'   : tnpSamples.Parking_doubleEle_run3['BuToKJpsi'].clone(),
    #'data'   : tnpSamples.Parking_doubleEle_run3['BuToKJpsi_realisticPU'].clone(),

    # 'data' : tnpSamples.Parking_doubleEle_run3['data_Run2022CDEF-Prompt'].clone(),
    # 'data' : tnpSamples.Parking_doubleEle_run3['data_SingleEleSingleEGL1_Run2022F-Prompt'].clone(),
    # 'data' : tnpSamples.Parking_doubleEle_run3['data_SingleEle_Run2022F-Prompt'].clone(),

    # 'data' : tnpSamples.Parking_doubleEle_run3['data_Run2022CDEFG-Prompt'].clone(),
    # 'data' : tnpSamples.Parking_doubleEle_run3['data_SingleEleSingleEGL1_Run2022FG-Prompt'].clone(),
    'data' : tnpSamples.Parking_doubleEle_run3['data_SingleEle_Run2022FG-Prompt'].clone(),

    'mcNom'  : tnpSamples.Parking_doubleEle_run3['BuToKJpsi'].clone(),
    'mcAlt'  : tnpSamples.Parking_doubleEle_run3['BuToKJpsi'].clone(),
    'tagSel' : tnpSamples.Parking_doubleEle_run3['BuToKJpsi'].clone(),
}

## if you need to use 2 times the same sample, then rename the second one
# if not samplesDef['mcAlt'] is None:
#     samplesDef['mcAlt'].rename('BuToKJpsi_mcAlt')
# if not samplesDef['tagSel'] is None:
#     samplesDef['tagSel'].rename('BuToKJpsi_tagSel')

## set MC weight
weightName = 'weight'    # 1 for data; pu_weight for MC   
# if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
# if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
# if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_weight(weightName)

#############################################################
# Bining definition  [can be nD bining]
biningDef = [
    #{ 'var' : 'JpsiKE_e2_pt', 'type': 'float', 'bins': [5.0, 999.0] }, #no binning

    { 'var' : 'JpsiKE_e2_pt', 'type': 'float', 'bins': [5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 13.0, 19.0, 9999999.0] }, #standard_2022_final
    #{ 'var' : 'JpsiKE_e2_pt', 'type': 'float', 'bins': [5.0, 6.0, 7.0, 8.0, 9.0, 11.0, 13.0, 9999999.0] }, #rebinned_2022_final_Ele+Jet
    #{ 'var' : 'JpsiKE_e2_pt', 'type': 'float', 'bins': [5.0, 6.0, 9.0, 13.0, 9999999.0] }, #rebinned_2022_final_SingleEle8SingleEGL1

    # OLD BINNING DEF
    #{ 'var' : 'JpsiKE_e2_pt', 'type': 'float', 'bins': [5.0, 6.0, 6.5, 7.5, 9.5, 10.5, 12.5, 14.5, 18.5, 9999999.0] }, #binned_2022_full
    #{ 'var' : 'JpsiKE_e2_pt', 'type': 'float', 'bins': [5.0, 6, 6.5, 7.5, 9.5, 10.5, 11.5, 12.5, 13.5, 16, 25, 35, 9999999.0] }, #binnedMC
]

#############################################################

# Cuts definition for all samples
cutBase = 'JpsiKE_Jpsi_mass_nofit>2.10001 && JpsiKE_Jpsi_mass_nofit<3.61 && abs(JpsiKE_e1_eta)<1.22 & abs(JpsiKE_e2_eta)<1.22 & JpsiKE_e1_pt>5.0 & JpsiKE_e2_pt>5.0 & JpsiKE_elesDr<0.6 & JpsiKE_e1_passMVA==1'

# MC cutbase
#cutBase = 'JpsiKE_Jpsi_mass_nofit>2.10001 && JpsiKE_Jpsi_mass_nofit<3.61 && abs(JpsiKE_e1_eta)<1.22 & abs(JpsiKE_e2_eta)<1.22 & JpsiKE_e1_pt>5.0 & JpsiKE_e2_pt>5.0 & JpsiKE_elesDr<0.6 && JpsiKE_e1_genMatchPt>0 && JpsiKE_e2_genMatchPt>0  & JpsiKE_e1_genMatchPt!=JpsiKE_e2_genMatchPt & JpsiKE_e1_passMVA==1'

# the two electrons are matched at L1 and don't match the same L1 ele
#cutBase += '& JpsiKE_e1_bestL1pt>0 & JpsiKE_e2_bestL1pt>0 & abs(JpsiKE_e1_bestL1eta-JpsiKE_e2_bestL1eta)>0.001 & abs(JpsiKE_e1_bestL1phi-JpsiKE_e2_bestL1phi)>0.001'

# can add addtionnal cuts for some bins (first check bin number using tnpEGM --checkBins)
#additionalCuts = { 
#    0 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45'
#}

# or remove any additional cut (default)
additionalCuts = None

### Add filtering on input json file
# if jsonfilter == True, filter data using json in jsonfileDict
jsonfilter = True

jsonfileDict = {
    'doubleEle4BothMatchedL1_4p5_Match'   : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_4p5_HLT_4p0_Incl_Final.json',
    'doubleEle4BothMatchedL1_5p0_Match'   : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_5p0_HLT_4p0_Incl_Final.json',
    'doubleEle4BothMatchedL1_5p5_Match'   : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_5p5_HLT_4p0_Incl_Final.json',
    'doubleEle4BothMatchedL1_6p0_Match'   : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_6p0_HLT_4p0_Incl_Final.json',
    'doubleEle4p5BothMatchedL1_6p5_Match' : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_6p5_HLT_4p5_Incl_Final.json',
    'doubleEle5BothMatchedL1_7p0_Match'   : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_7p0_HLT_5p0_Incl_Final.json',
    'doubleEle5BothMatchedL1_7p5_Match'   : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_7p5_HLT_5p0_Incl_Final.json',
    'doubleEle5BothMatchedL1_8p0_Match'   : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_8p0_HLT_5p0_Incl_Final.json',
    'doubleEle5BothMatchedL1_8p5_Match'   : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_8p5_HLT_5p0_Incl_Final.json',
    'doubleEle5BothMatchedL1_10p5_Match'  : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_10p5_HLT_5p0_Incl_Final.json',
    'doubleEle5p5BothMatchedL1_8p5_Match' : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_8p5_HLT_5p5_Incl_Final.json',
    'doubleEle6BothMatchedL1_5p5_Match'   : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_5p5_HLT_6p0_Incl_Final.json',
    'doubleEle6BothMatchedL1_9p0_Match'   : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_9p0_HLT_6p0_Incl_Final.json',
    #'doubleEle6p5BothMatchedL1_9p5_Match' : '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_9p5_HLT_6p5_Incl_Final.json',
    'doubleEle6p5BothMatchedL1_9p5_Match' : '',
    'doubleEle6p5BothMatchedL1_10p5_Match': '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_10p5_HLT_6p5_Incl_Final.json',
    'doubleEle6p5BothMatchedL1_11p0_Match': '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_11p0_HLT_6p5_Incl_Final.json',

    # to be added to the dictionary of flags later
    # jsonfileDef = '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_4p5_HLT_4p0_Incl_Final.json'
    # jsonfileDef = '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_5p0_HLT_4p0_Incl_Final.json'
    # jsonfileDef = '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_7p5_HLT_5p0_Incl_Final.json'
    # jsonfileDef = '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_8p5_HLT_5p5_Incl_Final.json'
    # jsonfileDef = '/afs/cern.ch/work/c/cquarant/RKanalysis/data/json/L1_9p0_HLT_6p0_Incl_Final.json'
}

#############################################################
# Fitting params to tune fit by hand if necessary
tnpParAltSigFitJPsi = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.1,0.01,3.0]",      
    "meanF[-0.0,-0.5,0.5]","sigmaF[0.1,0.01,1.0]",
    "alphaP[0.5, 0.2, 0.8]",
    "alphaF[0.5, 0.2, 0.8]",    
    ]

tnpParNomFitJPsi = [

    ### DoubleCB signal single pt bin MC
    # nominal fit
    # "meanP[3.096, 3.06, 3.12]","sigmaP[0.05, 0.045, 0.055]" , "alphaLP[0.5, 0.4, 0.7]" , "alphaRP[0.9, 0.8, 1.5]" , "nLP[14, 0, 16]","nRP[3, 2, 4]",
    # "meanF[3.096, 3.06, 3.12]","sigmaF[0.05, 0.045, 0.055]" , "alphaLF[0.5, 0.4, 0.6]" , "alphaRF[0.9, 0.8, 1.5]" , "nLF[14, 0, 16]","nRF[3, 2, 4]",
    # "expalphaP[0, 0, 0]",
    # "expalphaF[0, 0, 0]",   
    # to be edited for special bins
    # "meanP[3.110, 3.0, 3.2]","sigmaP[0.05, 0.04, 0.10]" , "alphaLP[0.5, 0.4, 0.7]" , "alphaRP[0.9, 0.8, 1.5]" , "nLP[14, 0, 16]","nRP[5, 3, 8]",
    # "meanF[3.096, 3.0, 3.2]","sigmaF[0.05, 0.04, 0.06]" , "alphaLF[0.563, 0.4, 0.7]" , "alphaRF[0.9, 0.8, 1.5]" , "nLF[8, 4, 10]","nRF[5, 3, 8]",

    # DoubleCB signal + Bkg Exp on DATA
    "meanP[3.096, 3.0, 3.2]","sigmaP[0.055, 0.045, 0.06]" , "alphaLP[0.5, 0.2, 0.7]" , "alphaRP[0.9, 0.8, 1.5]" , "nLP[14, 10, 16]","nRP[5, 4, 8]",
    "meanF[3.096, 3.0, 3.15]","sigmaF[0.055, 0.045, 0.06]" , "alphaLF[0.6, 0.5, 0.7]" , "alphaRF[1.0, 0.8, 1.2]" , "nLF[14, 10, 16]","nRF[5, 4, 8]",
    "expalphaP[-0.7, -1.0, 0]",
    "expalphaF[-0.75, -1.0, -0.]",   

    # to be edited for selected bins bins
    # "meanP[3.096, 3.0, 3.2]","sigmaP[0.055, 0.045, 0.065]" , "alphaLP[0.5, 0.2, 0.7]" , "alphaRP[0.9, 0.8, 1.5]" , "nLP[14, 10, 16]","nRP[5, 4, 8]",
    # "meanF[3.096, 3.0, 3.15]","sigmaF[0.055, 0.045, 0.065]" , "alphaLF[0.6, 0.5, 0.7]" , "alphaRF[1.0, 0.8, 1.2]" , "nLF[14, 10, 16]","nRF[5, 4, 8]",
    # "expalphaP[-0.7, -1.0, 0]",
    # "expalphaF[-0.75, -1.0, -0.]",   

    # DoubleCB signal SingleEle_SingleEGL1
    # "meanP[3.096, 3.0, 3.2]","sigmaP[0.05, 0.04, 0.06]" , "alphaLP[0.5, 0.4, 0.7]" , "alphaRP[0.9, 0.8, 1.5]" , "nLP[14, 0, 16]","nRP[5, 3, 8]",
    # "meanF[3.096, 3.0, 3.2]","sigmaF[0.05, 0.04, 0.06]" , "alphaLF[0.5, 0.4, 0.6]" , "alphaRF[0.9, 0.8, 1.5]" , "nLF[14, 0, 16]","nRF[5, 3, 8]",
    # "expalphaP[-1.0, -2.0, 0]",
    # "expalphaF[-1.0, -2.0, 0]",   

    # Gaussian Signal
    # "meanP[3.109, 3.09, 3.13]","sigmaP[0.07, 0.05, 0.12]",
    # "meanF[3.1, 3.09, 3.15]","sigmaF[0.03, 0.05, 0.13]",
    # "expalphaP[-0.75, -1., 0]",
    # "expalphaF[-0.75, -1.0, 0]",   
]
     
tnpParAltBkgFitJPsi = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.1,0.01,3.0]",      
    "meanF[-0.0,-0.5,0.5]","sigmaF[0.1,0.01,1.0]",
    "cP[0.,-100.,100.]",
    "cF[0.,-100.,500.]",
    ]

