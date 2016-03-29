if __name__=="__main__":
	class DQMItem:
		def __init__(self,layout):
			print layout
	dqmitems={}

def hcallayout(i, p, *rows): i['Hcal/Layouts/' + p] = DQMItem(layout=rows)


hcallayout(dqmitems, 'FG_TS2/TP_VMEvsuTCA/TTSubdet/HBHE', [{'path':'Hcal2/TPComparisonTask/FG_TS2/TTSubdet/HBHE', 'description':"""FG Correlation for TS2. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Trigger_Primitives_Comparison_Ta">Details...</a>"""}])

hcallayout(dqmitems, 'FG_TS2/TP_VMEvsuTCA/TTSubdet/HF', [{'path':'Hcal2/TPComparisonTask/FG_TS2/TTSubdet/HF', 'description':"""FG Correlation for TS2. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Trigger_Primitives_Comparison_Ta">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA', [{'path':'Hcal2/TPComparisonTask/EtMsm/EtMsm', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Missing_VME/DIGI_VMEvsuTCA/depth/depth1', [{'path':'Hcal2/DigiComparisonTask/Missing_VME/depth/depth1', 'description':"""Digis missing from VME collection and present in uTCA  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing_VME/DIGI_VMEvsuTCA/depth/depth2', [{'path':'Hcal2/DigiComparisonTask/Missing_VME/depth/depth2', 'description':"""Digis missing from VME collection and present in uTCA  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing_VME/DIGI_VMEvsuTCA/depth/depth3', [{'path':'Hcal2/DigiComparisonTask/Missing_VME/depth/depth3', 'description':"""Digis missing from VME collection and present in uTCA  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing_VME/DIGI_VMEvsuTCA/depth/depth4', [{'path':'Hcal2/DigiComparisonTask/Missing_VME/depth/depth4', 'description':"""Digis missing from VME collection and present in uTCA  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Energy/RECO/Electronics/VME', [{'path':'Hcal2/RecHitTask/Energy/Electronics/VME', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Energy/RECO/Electronics/uTCA', [{'path':'Hcal2/RecHitTask/Energy/Electronics/uTCA', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'OccupancyCutvsLS/RECO/Subdet/HB', [{'path':'Hcal2/RecHitTask/OccupancyCutvsLS/Subdet/HB', 'description':"""Occupancy after a cut vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCutvsLS/RECO/Subdet/HE', [{'path':'Hcal2/RecHitTask/OccupancyCutvsLS/Subdet/HE', 'description':"""Occupancy after a cut vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCutvsLS/RECO/Subdet/HF', [{'path':'Hcal2/RecHitTask/OccupancyCutvsLS/Subdet/HF', 'description':"""Occupancy after a cut vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCutvsLS/RECO/Subdet/HO', [{'path':'Hcal2/RecHitTask/OccupancyCutvsLS/Subdet/HO', 'description':"""Occupancy after a cut vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'ADC_TS2/DIGI_VMEvsuTCA/Subdet/HB', [{'path':'Hcal2/DigiComparisonTask/ADC_TS2/Subdet/HB', 'description':"""ADC Correlation for TS2. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADC_TS2/DIGI_VMEvsuTCA/Subdet/HE', [{'path':'Hcal2/DigiComparisonTask/ADC_TS2/Subdet/HE', 'description':"""ADC Correlation for TS2. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADC_TS2/DIGI_VMEvsuTCA/Subdet/HF', [{'path':'Hcal2/DigiComparisonTask/ADC_TS2/Subdet/HF', 'description':"""ADC Correlation for TS2. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADC_TS2/DIGI_VMEvsuTCA/Subdet/HO', [{'path':'Hcal2/DigiComparisonTask/ADC_TS2/Subdet/HO', 'description':"""ADC Correlation for TS2. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADC_TS0/DIGI_VMEvsuTCA/Subdet/HB', [{'path':'Hcal2/DigiComparisonTask/ADC_TS0/Subdet/HB', 'description':"""ADC Correlation for TS0. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADC_TS0/DIGI_VMEvsuTCA/Subdet/HE', [{'path':'Hcal2/DigiComparisonTask/ADC_TS0/Subdet/HE', 'description':"""ADC Correlation for TS0. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADC_TS0/DIGI_VMEvsuTCA/Subdet/HF', [{'path':'Hcal2/DigiComparisonTask/ADC_TS0/Subdet/HF', 'description':"""ADC Correlation for TS0. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADC_TS0/DIGI_VMEvsuTCA/Subdet/HO', [{'path':'Hcal2/DigiComparisonTask/ADC_TS0/Subdet/HO', 'description':"""ADC Correlation for TS0. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Et_TS3/TP_VMEvsuTCA/TTSubdet/HBHE', [{'path':'Hcal2/TPComparisonTask/Et_TS3/TTSubdet/HBHE', 'description':"""Et Correlation for TS3. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Trigger_Primitives_Comparison_Ta">Details...</a>"""}])

hcallayout(dqmitems, 'Et_TS3/TP_VMEvsuTCA/TTSubdet/HF', [{'path':'Hcal2/TPComparisonTask/Et_TS3/TTSubdet/HF', 'description':"""Et Correlation for TS3. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Trigger_Primitives_Comparison_Ta">Details...</a>"""}])

hcallayout(dqmitems, 'ADC_TS9/DIGI_VMEvsuTCA/Subdet/HB', [{'path':'Hcal2/DigiComparisonTask/ADC_TS9/Subdet/HB', 'description':"""ADC Correlation for TS9. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADC_TS9/DIGI_VMEvsuTCA/Subdet/HE', [{'path':'Hcal2/DigiComparisonTask/ADC_TS9/Subdet/HE', 'description':"""ADC Correlation for TS9. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADC_TS9/DIGI_VMEvsuTCA/Subdet/HF', [{'path':'Hcal2/DigiComparisonTask/ADC_TS9/Subdet/HF', 'description':"""ADC Correlation for TS9. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADC_TS9/DIGI_VMEvsuTCA/Subdet/HO', [{'path':'Hcal2/DigiComparisonTask/ADC_TS9/Subdet/HO', 'description':"""ADC Correlation for TS9. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'TimingCut/RECO/Electronics/VME', [{'path':'Hcal2/RecHitTask/TimingCut/Electronics/VME', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCut/RECO/Electronics/uTCA', [{'path':'Hcal2/RecHitTask/TimingCut/Electronics/uTCA', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/RECO/Electronics/VME', [{'path':'Hcal2/RecHitTask/Occupancy/Electronics/VME', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/RECO/Electronics/uTCA', [{'path':'Hcal2/RecHitTask/Occupancy/Electronics/uTCA', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'FG_TS3/TP_VMEvsuTCA/TTSubdet/HBHE', [{'path':'Hcal2/TPComparisonTask/FG_TS3/TTSubdet/HBHE', 'description':"""FG Correlation for TS3. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Trigger_Primitives_Comparison_Ta">Details...</a>"""}])

hcallayout(dqmitems, 'FG_TS3/TP_VMEvsuTCA/TTSubdet/HF', [{'path':'Hcal2/TPComparisonTask/FG_TS3/TTSubdet/HF', 'description':"""FG Correlation for TS3. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Trigger_Primitives_Comparison_Ta">Details...</a>"""}])

hcallayout(dqmitems, 'TimingCut/RECO/SubdetPM/HBM', [{'path':'Hcal2/RecHitTask/TimingCut/SubdetPM/HBM', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCut/RECO/SubdetPM/HBP', [{'path':'Hcal2/RecHitTask/TimingCut/SubdetPM/HBP', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCut/RECO/SubdetPM/HEM', [{'path':'Hcal2/RecHitTask/TimingCut/SubdetPM/HEM', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCut/RECO/SubdetPM/HEP', [{'path':'Hcal2/RecHitTask/TimingCut/SubdetPM/HEP', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCut/RECO/SubdetPM/HFM', [{'path':'Hcal2/RecHitTask/TimingCut/SubdetPM/HFM', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCut/RECO/SubdetPM/HFP', [{'path':'Hcal2/RecHitTask/TimingCut/SubdetPM/HFP', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCut/RECO/SubdetPM/HOM', [{'path':'Hcal2/RecHitTask/TimingCut/SubdetPM/HOM', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCut/RECO/SubdetPM/HOP', [{'path':'Hcal2/RecHitTask/TimingCut/SubdetPM/HOP', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Energy/RECO/depth/depth1', [{'path':'Hcal2/RecHitTask/Energy/depth/depth1', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Energy/RECO/depth/depth2', [{'path':'Hcal2/RecHitTask/Energy/depth/depth2', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Energy/RECO/depth/depth3', [{'path':'Hcal2/RecHitTask/Energy/depth/depth3', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Energy/RECO/depth/depth4', [{'path':'Hcal2/RecHitTask/Energy/depth/depth4', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'TimingCutvsLS/RECO/FED/FED1100', [{'path':'Hcal2/RecHitTask/TimingCutvsLS/FED/FED1100', 'description':"""Timing either @RECO or @DIGI level. A cut is applied either on signal amplitude (DIGI) or on energy (RECO)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCutvsLS/RECO/FED/FED1102', [{'path':'Hcal2/RecHitTask/TimingCutvsLS/FED/FED1102', 'description':"""Timing either @RECO or @DIGI level. A cut is applied either on signal amplitude (DIGI) or on energy (RECO)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCutvsLS/RECO/FED/FED1104', [{'path':'Hcal2/RecHitTask/TimingCutvsLS/FED/FED1104', 'description':"""Timing either @RECO or @DIGI level. A cut is applied either on signal amplitude (DIGI) or on energy (RECO)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCutvsLS/RECO/FED/FED1106', [{'path':'Hcal2/RecHitTask/TimingCutvsLS/FED/FED1106', 'description':"""Timing either @RECO or @DIGI level. A cut is applied either on signal amplitude (DIGI) or on energy (RECO)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCutvsLS/RECO/FED/FED1108', [{'path':'Hcal2/RecHitTask/TimingCutvsLS/FED/FED1108', 'description':"""Timing either @RECO or @DIGI level. A cut is applied either on signal amplitude (DIGI) or on energy (RECO)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCutvsLS/RECO/FED/FED1110', [{'path':'Hcal2/RecHitTask/TimingCutvsLS/FED/FED1110', 'description':"""Timing either @RECO or @DIGI level. A cut is applied either on signal amplitude (DIGI) or on energy (RECO)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCutvsLS/RECO/FED/FED1112', [{'path':'Hcal2/RecHitTask/TimingCutvsLS/FED/FED1112', 'description':"""Timing either @RECO or @DIGI level. A cut is applied either on signal amplitude (DIGI) or on energy (RECO)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCutvsLS/RECO/FED/FED1114', [{'path':'Hcal2/RecHitTask/TimingCutvsLS/FED/FED1114', 'description':"""Timing either @RECO or @DIGI level. A cut is applied either on signal amplitude (DIGI) or on energy (RECO)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCutvsLS/RECO/FED/FED1116', [{'path':'Hcal2/RecHitTask/TimingCutvsLS/FED/FED1116', 'description':"""Timing either @RECO or @DIGI level. A cut is applied either on signal amplitude (DIGI) or on energy (RECO)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCutvsLS/RECO/FED/FED1118', [{'path':'Hcal2/RecHitTask/TimingCutvsLS/FED/FED1118', 'description':"""Timing either @RECO or @DIGI level. A cut is applied either on signal amplitude (DIGI) or on energy (RECO)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCutvsLS/RECO/FED/FED1120', [{'path':'Hcal2/RecHitTask/TimingCutvsLS/FED/FED1120', 'description':"""Timing either @RECO or @DIGI level. A cut is applied either on signal amplitude (DIGI) or on energy (RECO)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCutvsLS/RECO/FED/FED1122', [{'path':'Hcal2/RecHitTask/TimingCutvsLS/FED/FED1122', 'description':"""Timing either @RECO or @DIGI level. A cut is applied either on signal amplitude (DIGI) or on energy (RECO)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCutvsLS/RECO/FED/FED1132', [{'path':'Hcal2/RecHitTask/TimingCutvsLS/FED/FED1132', 'description':"""Timing either @RECO or @DIGI level. A cut is applied either on signal amplitude (DIGI) or on energy (RECO)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCutvsLS/RECO/FED/FED724', [{'path':'Hcal2/RecHitTask/TimingCutvsLS/FED/FED724', 'description':"""Timing either @RECO or @DIGI level. A cut is applied either on signal amplitude (DIGI) or on energy (RECO)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCutvsLS/RECO/FED/FED725', [{'path':'Hcal2/RecHitTask/TimingCutvsLS/FED/FED725', 'description':"""Timing either @RECO or @DIGI level. A cut is applied either on signal amplitude (DIGI) or on energy (RECO)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCutvsLS/RECO/FED/FED726', [{'path':'Hcal2/RecHitTask/TimingCutvsLS/FED/FED726', 'description':"""Timing either @RECO or @DIGI level. A cut is applied either on signal amplitude (DIGI) or on energy (RECO)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCutvsLS/RECO/FED/FED727', [{'path':'Hcal2/RecHitTask/TimingCutvsLS/FED/FED727', 'description':"""Timing either @RECO or @DIGI level. A cut is applied either on signal amplitude (DIGI) or on energy (RECO)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCutvsLS/RECO/FED/FED728', [{'path':'Hcal2/RecHitTask/TimingCutvsLS/FED/FED728', 'description':"""Timing either @RECO or @DIGI level. A cut is applied either on signal amplitude (DIGI) or on energy (RECO)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCutvsLS/RECO/FED/FED729', [{'path':'Hcal2/RecHitTask/TimingCutvsLS/FED/FED729', 'description':"""Timing either @RECO or @DIGI level. A cut is applied either on signal amplitude (DIGI) or on energy (RECO)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCutvsLS/RECO/FED/FED730', [{'path':'Hcal2/RecHitTask/TimingCutvsLS/FED/FED730', 'description':"""Timing either @RECO or @DIGI level. A cut is applied either on signal amplitude (DIGI) or on energy (RECO)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCutvsLS/RECO/FED/FED731', [{'path':'Hcal2/RecHitTask/TimingCutvsLS/FED/FED731', 'description':"""Timing either @RECO or @DIGI level. A cut is applied either on signal amplitude (DIGI) or on energy (RECO)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyvsLS/RECO/Subdet/HB', [{'path':'Hcal2/RecHitTask/OccupancyvsLS/Subdet/HB', 'description':"""Occupancy vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Pedestal_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'OccupancyvsLS/RECO/Subdet/HE', [{'path':'Hcal2/RecHitTask/OccupancyvsLS/Subdet/HE', 'description':"""Occupancy vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Pedestal_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'OccupancyvsLS/RECO/Subdet/HF', [{'path':'Hcal2/RecHitTask/OccupancyvsLS/Subdet/HF', 'description':"""Occupancy vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Pedestal_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'OccupancyvsLS/RECO/Subdet/HO', [{'path':'Hcal2/RecHitTask/OccupancyvsLS/Subdet/HO', 'description':"""Occupancy vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Pedestal_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Energy/RECO/Subdet/HB', [{'path':'Hcal2/RecHitTask/Energy/Subdet/HB', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Energy/RECO/Subdet/HE', [{'path':'Hcal2/RecHitTask/Energy/Subdet/HE', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Energy/RECO/Subdet/HF', [{'path':'Hcal2/RecHitTask/Energy/Subdet/HF', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Energy/RECO/Subdet/HO', [{'path':'Hcal2/RecHitTask/Energy/Subdet/HO', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'TimingvsEnergy/RECO/SubdetPM/HBM', [{'path':'Hcal2/RecHitTask/TimingvsEnergy/SubdetPM/HBM', 'description':"""Timing vs Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'TimingvsEnergy/RECO/SubdetPM/HBP', [{'path':'Hcal2/RecHitTask/TimingvsEnergy/SubdetPM/HBP', 'description':"""Timing vs Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'TimingvsEnergy/RECO/SubdetPM/HEM', [{'path':'Hcal2/RecHitTask/TimingvsEnergy/SubdetPM/HEM', 'description':"""Timing vs Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'TimingvsEnergy/RECO/SubdetPM/HEP', [{'path':'Hcal2/RecHitTask/TimingvsEnergy/SubdetPM/HEP', 'description':"""Timing vs Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'TimingvsEnergy/RECO/SubdetPM/HFM', [{'path':'Hcal2/RecHitTask/TimingvsEnergy/SubdetPM/HFM', 'description':"""Timing vs Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'TimingvsEnergy/RECO/SubdetPM/HFP', [{'path':'Hcal2/RecHitTask/TimingvsEnergy/SubdetPM/HFP', 'description':"""Timing vs Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'TimingvsEnergy/RECO/SubdetPM/HOM', [{'path':'Hcal2/RecHitTask/TimingvsEnergy/SubdetPM/HOM', 'description':"""Timing vs Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'TimingvsEnergy/RECO/SubdetPM/HOP', [{'path':'Hcal2/RecHitTask/TimingvsEnergy/SubdetPM/HOP', 'description':"""Timing vs Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED1100', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED1100', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED1102', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED1102', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED1104', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED1104', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED1106', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED1106', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED1108', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED1108', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED1110', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED1110', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED1112', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED1112', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED1114', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED1114', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED1116', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED1116', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED1118', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED1118', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED1120', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED1120', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED1122', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED1122', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED1132', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED1132', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED700', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED700', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED701', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED701', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED702', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED702', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED703', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED703', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED704', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED704', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED705', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED705', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED706', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED706', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED707', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED707', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED708', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED708', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED709', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED709', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED710', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED710', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED711', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED711', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED712', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED712', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED713', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED713', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED714', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED714', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED715', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED715', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED716', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED716', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED717', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED717', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED724', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED724', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED725', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED725', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED726', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED726', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED727', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED727', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED728', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED728', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED729', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED729', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED730', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED730', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA/FED/FED731', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED731', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED1100', [{'path':'Hcal2/RecHitTask/Energy/FED/FED1100', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED1102', [{'path':'Hcal2/RecHitTask/Energy/FED/FED1102', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED1104', [{'path':'Hcal2/RecHitTask/Energy/FED/FED1104', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED1106', [{'path':'Hcal2/RecHitTask/Energy/FED/FED1106', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED1108', [{'path':'Hcal2/RecHitTask/Energy/FED/FED1108', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED1110', [{'path':'Hcal2/RecHitTask/Energy/FED/FED1110', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED1112', [{'path':'Hcal2/RecHitTask/Energy/FED/FED1112', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED1114', [{'path':'Hcal2/RecHitTask/Energy/FED/FED1114', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED1116', [{'path':'Hcal2/RecHitTask/Energy/FED/FED1116', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED1118', [{'path':'Hcal2/RecHitTask/Energy/FED/FED1118', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED1120', [{'path':'Hcal2/RecHitTask/Energy/FED/FED1120', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED1122', [{'path':'Hcal2/RecHitTask/Energy/FED/FED1122', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED1132', [{'path':'Hcal2/RecHitTask/Energy/FED/FED1132', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED724', [{'path':'Hcal2/RecHitTask/Energy/FED/FED724', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED725', [{'path':'Hcal2/RecHitTask/Energy/FED/FED725', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED726', [{'path':'Hcal2/RecHitTask/Energy/FED/FED726', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED727', [{'path':'Hcal2/RecHitTask/Energy/FED/FED727', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED728', [{'path':'Hcal2/RecHitTask/Energy/FED/FED728', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED729', [{'path':'Hcal2/RecHitTask/Energy/FED/FED729', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED730', [{'path':'Hcal2/RecHitTask/Energy/FED/FED730', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED731', [{'path':'Hcal2/RecHitTask/Energy/FED/FED731', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'TimingCut/RECO/depth/depth1', [{'path':'Hcal2/RecHitTask/TimingCut/depth/depth1', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCut/RECO/depth/depth2', [{'path':'Hcal2/RecHitTask/TimingCut/depth/depth2', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCut/RECO/depth/depth3', [{'path':'Hcal2/RecHitTask/TimingCut/depth/depth3', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCut/RECO/depth/depth4', [{'path':'Hcal2/RecHitTask/TimingCut/depth/depth4', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/depth/depth1', [{'path':'Hcal2/DigiComparisonTask/Mismatched/depth/depth1', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/depth/depth2', [{'path':'Hcal2/DigiComparisonTask/Mismatched/depth/depth2', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/depth/depth3', [{'path':'Hcal2/DigiComparisonTask/Mismatched/depth/depth3', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/depth/depth4', [{'path':'Hcal2/DigiComparisonTask/Mismatched/depth/depth4', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADCMsnVME/DIGI_VMEvsuTCA/Subdet/HB', [{'path':'Hcal2/DigiComparisonTask/ADCMsnVME/Subdet/HB', 'description':"""ADC Distribution for Missing VME Digis  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADCMsnVME/DIGI_VMEvsuTCA/Subdet/HE', [{'path':'Hcal2/DigiComparisonTask/ADCMsnVME/Subdet/HE', 'description':"""ADC Distribution for Missing VME Digis  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADCMsnVME/DIGI_VMEvsuTCA/Subdet/HF', [{'path':'Hcal2/DigiComparisonTask/ADCMsnVME/Subdet/HF', 'description':"""ADC Distribution for Missing VME Digis  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADCMsnVME/DIGI_VMEvsuTCA/Subdet/HO', [{'path':'Hcal2/DigiComparisonTask/ADCMsnVME/Subdet/HO', 'description':"""ADC Distribution for Missing VME Digis  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing_uTCA/DIGI_VMEvsuTCA/depth/depth1', [{'path':'Hcal2/DigiComparisonTask/Missing_uTCA/depth/depth1', 'description':"""Digis missing from uTCA collection and present in VME  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing_uTCA/DIGI_VMEvsuTCA/depth/depth2', [{'path':'Hcal2/DigiComparisonTask/Missing_uTCA/depth/depth2', 'description':"""Digis missing from uTCA collection and present in VME  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing_uTCA/DIGI_VMEvsuTCA/depth/depth3', [{'path':'Hcal2/DigiComparisonTask/Missing_uTCA/depth/depth3', 'description':"""Digis missing from uTCA collection and present in VME  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing_uTCA/DIGI_VMEvsuTCA/depth/depth4', [{'path':'Hcal2/DigiComparisonTask/Missing_uTCA/depth/depth4', 'description':"""Digis missing from uTCA collection and present in VME  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'FG_TS0/TP_VMEvsuTCA/TTSubdet/HBHE', [{'path':'Hcal2/TPComparisonTask/FG_TS0/TTSubdet/HBHE', 'description':"""FG Correlation for TS0. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Trigger_Primitives_Comparison_Ta">Details...</a>"""}])

hcallayout(dqmitems, 'FG_TS0/TP_VMEvsuTCA/TTSubdet/HF', [{'path':'Hcal2/TPComparisonTask/FG_TS0/TTSubdet/HF', 'description':"""FG Correlation for TS0. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Trigger_Primitives_Comparison_Ta">Details...</a>"""}])

hcallayout(dqmitems, 'ADC_TS8/DIGI_VMEvsuTCA/Subdet/HB', [{'path':'Hcal2/DigiComparisonTask/ADC_TS8/Subdet/HB', 'description':"""ADC Correlation for TS8. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADC_TS8/DIGI_VMEvsuTCA/Subdet/HE', [{'path':'Hcal2/DigiComparisonTask/ADC_TS8/Subdet/HE', 'description':"""ADC Correlation for TS8. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADC_TS8/DIGI_VMEvsuTCA/Subdet/HF', [{'path':'Hcal2/DigiComparisonTask/ADC_TS8/Subdet/HF', 'description':"""ADC Correlation for TS8. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADC_TS8/DIGI_VMEvsuTCA/Subdet/HO', [{'path':'Hcal2/DigiComparisonTask/ADC_TS8/Subdet/HO', 'description':"""ADC Correlation for TS8. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADCMsnuTCA/DIGI_VMEvsuTCA/Subdet/HB', [{'path':'Hcal2/DigiComparisonTask/ADCMsnuTCA/Subdet/HB', 'description':"""ADC Distribution for Missing uTCA Digis  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADCMsnuTCA/DIGI_VMEvsuTCA/Subdet/HE', [{'path':'Hcal2/DigiComparisonTask/ADCMsnuTCA/Subdet/HE', 'description':"""ADC Distribution for Missing uTCA Digis  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADCMsnuTCA/DIGI_VMEvsuTCA/Subdet/HF', [{'path':'Hcal2/DigiComparisonTask/ADCMsnuTCA/Subdet/HF', 'description':"""ADC Distribution for Missing uTCA Digis  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADCMsnuTCA/DIGI_VMEvsuTCA/Subdet/HO', [{'path':'Hcal2/DigiComparisonTask/ADCMsnuTCA/Subdet/HO', 'description':"""ADC Distribution for Missing uTCA Digis  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Et_TS0/TP_VMEvsuTCA/TTSubdet/HBHE', [{'path':'Hcal2/TPComparisonTask/Et_TS0/TTSubdet/HBHE', 'description':"""Et Correlation for TS0. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Trigger_Primitives_Comparison_Ta">Details...</a>"""}])

hcallayout(dqmitems, 'Et_TS0/TP_VMEvsuTCA/TTSubdet/HF', [{'path':'Hcal2/TPComparisonTask/Et_TS0/TTSubdet/HF', 'description':"""Et Correlation for TS0. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Trigger_Primitives_Comparison_Ta">Details...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/RECO/depth/depth1', [{'path':'Hcal2/RecHitTask/OccupancyCut/depth/depth1', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/RECO/depth/depth2', [{'path':'Hcal2/RecHitTask/OccupancyCut/depth/depth2', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/RECO/depth/depth3', [{'path':'Hcal2/RecHitTask/OccupancyCut/depth/depth3', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/RECO/depth/depth4', [{'path':'Hcal2/RecHitTask/OccupancyCut/depth/depth4', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED1100', [{'path':'Hcal2/RecHitTask/TimingCut/FED/FED1100', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED1102', [{'path':'Hcal2/RecHitTask/TimingCut/FED/FED1102', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED1104', [{'path':'Hcal2/RecHitTask/TimingCut/FED/FED1104', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED1106', [{'path':'Hcal2/RecHitTask/TimingCut/FED/FED1106', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED1108', [{'path':'Hcal2/RecHitTask/TimingCut/FED/FED1108', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED1110', [{'path':'Hcal2/RecHitTask/TimingCut/FED/FED1110', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED1112', [{'path':'Hcal2/RecHitTask/TimingCut/FED/FED1112', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED1114', [{'path':'Hcal2/RecHitTask/TimingCut/FED/FED1114', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED1116', [{'path':'Hcal2/RecHitTask/TimingCut/FED/FED1116', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED1118', [{'path':'Hcal2/RecHitTask/TimingCut/FED/FED1118', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED1120', [{'path':'Hcal2/RecHitTask/TimingCut/FED/FED1120', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED1122', [{'path':'Hcal2/RecHitTask/TimingCut/FED/FED1122', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED1132', [{'path':'Hcal2/RecHitTask/TimingCut/FED/FED1132', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED724', [{'path':'Hcal2/RecHitTask/TimingCut/FED/FED724', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED725', [{'path':'Hcal2/RecHitTask/TimingCut/FED/FED725', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED726', [{'path':'Hcal2/RecHitTask/TimingCut/FED/FED726', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED727', [{'path':'Hcal2/RecHitTask/TimingCut/FED/FED727', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED728', [{'path':'Hcal2/RecHitTask/TimingCut/FED/FED728', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED729', [{'path':'Hcal2/RecHitTask/TimingCut/FED/FED729', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED730', [{'path':'Hcal2/RecHitTask/TimingCut/FED/FED730', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED731', [{'path':'Hcal2/RecHitTask/TimingCut/FED/FED731', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Et/TP_VMEvsuTCA/TTSubdet/HBHE', [{'path':'Hcal2/TPComparisonTask/Et/TTSubdet/HBHE', 'description':"""Et Correlation over all TS. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Trigger_Primitives_Comparison_Ta">Details...</a>"""}])

hcallayout(dqmitems, 'Et/TP_VMEvsuTCA/TTSubdet/HF', [{'path':'Hcal2/TPComparisonTask/Et/TTSubdet/HF', 'description':"""Et Correlation over all TS. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Trigger_Primitives_Comparison_Ta">Details...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED1100', [{'path':'Hcal2/RecHitTask/OccupancyCut/FED/FED1100', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED1102', [{'path':'Hcal2/RecHitTask/OccupancyCut/FED/FED1102', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED1104', [{'path':'Hcal2/RecHitTask/OccupancyCut/FED/FED1104', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED1106', [{'path':'Hcal2/RecHitTask/OccupancyCut/FED/FED1106', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED1108', [{'path':'Hcal2/RecHitTask/OccupancyCut/FED/FED1108', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED1110', [{'path':'Hcal2/RecHitTask/OccupancyCut/FED/FED1110', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED1112', [{'path':'Hcal2/RecHitTask/OccupancyCut/FED/FED1112', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED1114', [{'path':'Hcal2/RecHitTask/OccupancyCut/FED/FED1114', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED1116', [{'path':'Hcal2/RecHitTask/OccupancyCut/FED/FED1116', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED1118', [{'path':'Hcal2/RecHitTask/OccupancyCut/FED/FED1118', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED1120', [{'path':'Hcal2/RecHitTask/OccupancyCut/FED/FED1120', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED1122', [{'path':'Hcal2/RecHitTask/OccupancyCut/FED/FED1122', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED1132', [{'path':'Hcal2/RecHitTask/OccupancyCut/FED/FED1132', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED724', [{'path':'Hcal2/RecHitTask/OccupancyCut/FED/FED724', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED725', [{'path':'Hcal2/RecHitTask/OccupancyCut/FED/FED725', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED726', [{'path':'Hcal2/RecHitTask/OccupancyCut/FED/FED726', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED727', [{'path':'Hcal2/RecHitTask/OccupancyCut/FED/FED727', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED728', [{'path':'Hcal2/RecHitTask/OccupancyCut/FED/FED728', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED729', [{'path':'Hcal2/RecHitTask/OccupancyCut/FED/FED729', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED730', [{'path':'Hcal2/RecHitTask/OccupancyCut/FED/FED730', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED731', [{'path':'Hcal2/RecHitTask/OccupancyCut/FED/FED731', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'ADC/DIGI_VMEvsuTCA/Subdet/HB', [{'path':'Hcal2/DigiComparisonTask/ADC/Subdet/HB', 'description':"""ADC Distributions per 1 TS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'ADC/DIGI_VMEvsuTCA/Subdet/HE', [{'path':'Hcal2/DigiComparisonTask/ADC/Subdet/HE', 'description':"""ADC Distributions per 1 TS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'ADC/DIGI_VMEvsuTCA/Subdet/HF', [{'path':'Hcal2/DigiComparisonTask/ADC/Subdet/HF', 'description':"""ADC Distributions per 1 TS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'ADC/DIGI_VMEvsuTCA/Subdet/HO', [{'path':'Hcal2/DigiComparisonTask/ADC/Subdet/HO', 'description':"""ADC Distributions per 1 TS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED1100', [{'path':'Hcal2/RecHitTask/Missing1LS/FED/FED1100', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED1102', [{'path':'Hcal2/RecHitTask/Missing1LS/FED/FED1102', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED1104', [{'path':'Hcal2/RecHitTask/Missing1LS/FED/FED1104', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED1106', [{'path':'Hcal2/RecHitTask/Missing1LS/FED/FED1106', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED1108', [{'path':'Hcal2/RecHitTask/Missing1LS/FED/FED1108', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED1110', [{'path':'Hcal2/RecHitTask/Missing1LS/FED/FED1110', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED1112', [{'path':'Hcal2/RecHitTask/Missing1LS/FED/FED1112', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED1114', [{'path':'Hcal2/RecHitTask/Missing1LS/FED/FED1114', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED1116', [{'path':'Hcal2/RecHitTask/Missing1LS/FED/FED1116', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED1118', [{'path':'Hcal2/RecHitTask/Missing1LS/FED/FED1118', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED1120', [{'path':'Hcal2/RecHitTask/Missing1LS/FED/FED1120', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED1122', [{'path':'Hcal2/RecHitTask/Missing1LS/FED/FED1122', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED1132', [{'path':'Hcal2/RecHitTask/Missing1LS/FED/FED1132', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED724', [{'path':'Hcal2/RecHitTask/Missing1LS/FED/FED724', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED725', [{'path':'Hcal2/RecHitTask/Missing1LS/FED/FED725', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED726', [{'path':'Hcal2/RecHitTask/Missing1LS/FED/FED726', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED727', [{'path':'Hcal2/RecHitTask/Missing1LS/FED/FED727', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED728', [{'path':'Hcal2/RecHitTask/Missing1LS/FED/FED728', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED729', [{'path':'Hcal2/RecHitTask/Missing1LS/FED/FED729', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED730', [{'path':'Hcal2/RecHitTask/Missing1LS/FED/FED730', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED731', [{'path':'Hcal2/RecHitTask/Missing1LS/FED/FED731', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA', [{'path':'Hcal2/TPComparisonTask/Missing/Missing_VME', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA', [{'path':'Hcal2/TPComparisonTask/Missing/Missing_uTCA', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/RECO/Electronics/VME', [{'path':'Hcal2/RecHitTask/OccupancyCut/Electronics/VME', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/RECO/Electronics/uTCA', [{'path':'Hcal2/RecHitTask/OccupancyCut/Electronics/uTCA', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'ADC_TS1/DIGI_VMEvsuTCA/Subdet/HB', [{'path':'Hcal2/DigiComparisonTask/ADC_TS1/Subdet/HB', 'description':"""ADC Correlation for TS1. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADC_TS1/DIGI_VMEvsuTCA/Subdet/HE', [{'path':'Hcal2/DigiComparisonTask/ADC_TS1/Subdet/HE', 'description':"""ADC Correlation for TS1. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADC_TS1/DIGI_VMEvsuTCA/Subdet/HF', [{'path':'Hcal2/DigiComparisonTask/ADC_TS1/Subdet/HF', 'description':"""ADC Correlation for TS1. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADC_TS1/DIGI_VMEvsuTCA/Subdet/HO', [{'path':'Hcal2/DigiComparisonTask/ADC_TS1/Subdet/HO', 'description':"""ADC Correlation for TS1. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'TimingCut/RECO/HBHEPartition/HBHEa', [{'path':'Hcal2/RecHitTask/TimingCut/HBHEPartition/HBHEa', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCut/RECO/HBHEPartition/HBHEb', [{'path':'Hcal2/RecHitTask/TimingCut/HBHEPartition/HBHEb', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingCut/RECO/HBHEPartition/HBHEc', [{'path':'Hcal2/RecHitTask/TimingCut/HBHEPartition/HBHEc', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'FG_TS1/TP_VMEvsuTCA/TTSubdet/HBHE', [{'path':'Hcal2/TPComparisonTask/FG_TS1/TTSubdet/HBHE', 'description':"""FG Correlation for TS1. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Trigger_Primitives_Comparison_Ta">Details...</a>"""}])

hcallayout(dqmitems, 'FG_TS1/TP_VMEvsuTCA/TTSubdet/HF', [{'path':'Hcal2/TPComparisonTask/FG_TS1/TTSubdet/HF', 'description':"""FG Correlation for TS1. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Trigger_Primitives_Comparison_Ta">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED1100', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED1100', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED1102', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED1102', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED1104', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED1104', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED1106', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED1106', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED1108', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED1108', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED1110', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED1110', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED1112', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED1112', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED1114', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED1114', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED1116', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED1116', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED1118', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED1118', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED1120', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED1120', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED1122', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED1122', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED1132', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED1132', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED700', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED700', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED701', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED701', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED702', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED702', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED703', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED703', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED704', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED704', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED705', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED705', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED706', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED706', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED707', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED707', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED708', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED708', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED709', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED709', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED710', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED710', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED711', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED711', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED712', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED712', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED713', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED713', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED714', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED714', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED715', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED715', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED716', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED716', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED717', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED717', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED724', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED724', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED725', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED725', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED726', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED726', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED727', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED727', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED728', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED728', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED729', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED729', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED730', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED730', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Mismatched/DIGI_VMEvsuTCA/FED/FED731', [{'path':'Hcal2/DigiComparisonTask/Mismatched/FED/FED731', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Occupancy/RECO/depth/depth1', [{'path':'Hcal2/RecHitTask/Occupancy/depth/depth1', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/RECO/depth/depth2', [{'path':'Hcal2/RecHitTask/Occupancy/depth/depth2', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/RECO/depth/depth3', [{'path':'Hcal2/RecHitTask/Occupancy/depth/depth3', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/RECO/depth/depth4', [{'path':'Hcal2/RecHitTask/Occupancy/depth/depth4', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Et_TS1/TP_VMEvsuTCA/TTSubdet/HBHE', [{'path':'Hcal2/TPComparisonTask/Et_TS1/TTSubdet/HBHE', 'description':"""Et Correlation for TS1. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Trigger_Primitives_Comparison_Ta">Details...</a>"""}])

hcallayout(dqmitems, 'Et_TS1/TP_VMEvsuTCA/TTSubdet/HF', [{'path':'Hcal2/TPComparisonTask/Et_TS1/TTSubdet/HF', 'description':"""Et Correlation for TS1. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Trigger_Primitives_Comparison_Ta">Details...</a>"""}])

hcallayout(dqmitems, 'ADC_TS6/DIGI_VMEvsuTCA/Subdet/HB', [{'path':'Hcal2/DigiComparisonTask/ADC_TS6/Subdet/HB', 'description':"""ADC Correlation for TS6. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADC_TS6/DIGI_VMEvsuTCA/Subdet/HE', [{'path':'Hcal2/DigiComparisonTask/ADC_TS6/Subdet/HE', 'description':"""ADC Correlation for TS6. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADC_TS6/DIGI_VMEvsuTCA/Subdet/HF', [{'path':'Hcal2/DigiComparisonTask/ADC_TS6/Subdet/HF', 'description':"""ADC Correlation for TS6. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADC_TS6/DIGI_VMEvsuTCA/Subdet/HO', [{'path':'Hcal2/DigiComparisonTask/ADC_TS6/Subdet/HO', 'description':"""ADC Correlation for TS6. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED1100', [{'path':'Hcal2/RecHitTask/Occupancy/FED/FED1100', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED1102', [{'path':'Hcal2/RecHitTask/Occupancy/FED/FED1102', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED1104', [{'path':'Hcal2/RecHitTask/Occupancy/FED/FED1104', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED1106', [{'path':'Hcal2/RecHitTask/Occupancy/FED/FED1106', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED1108', [{'path':'Hcal2/RecHitTask/Occupancy/FED/FED1108', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED1110', [{'path':'Hcal2/RecHitTask/Occupancy/FED/FED1110', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED1112', [{'path':'Hcal2/RecHitTask/Occupancy/FED/FED1112', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED1114', [{'path':'Hcal2/RecHitTask/Occupancy/FED/FED1114', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED1116', [{'path':'Hcal2/RecHitTask/Occupancy/FED/FED1116', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED1118', [{'path':'Hcal2/RecHitTask/Occupancy/FED/FED1118', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED1120', [{'path':'Hcal2/RecHitTask/Occupancy/FED/FED1120', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED1122', [{'path':'Hcal2/RecHitTask/Occupancy/FED/FED1122', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED1132', [{'path':'Hcal2/RecHitTask/Occupancy/FED/FED1132', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED724', [{'path':'Hcal2/RecHitTask/Occupancy/FED/FED724', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED725', [{'path':'Hcal2/RecHitTask/Occupancy/FED/FED725', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED726', [{'path':'Hcal2/RecHitTask/Occupancy/FED/FED726', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED727', [{'path':'Hcal2/RecHitTask/Occupancy/FED/FED727', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED728', [{'path':'Hcal2/RecHitTask/Occupancy/FED/FED728', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED729', [{'path':'Hcal2/RecHitTask/Occupancy/FED/FED729', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED730', [{'path':'Hcal2/RecHitTask/Occupancy/FED/FED730', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED731', [{'path':'Hcal2/RecHitTask/Occupancy/FED/FED731', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED1100', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED1100', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED1102', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED1102', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED1104', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED1104', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED1106', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED1106', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED1108', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED1108', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED1110', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED1110', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED1112', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED1112', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED1114', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED1114', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED1116', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED1116', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED1118', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED1118', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED1120', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED1120', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED1122', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED1122', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED1132', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED1132', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED700', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED700', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED701', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED701', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED702', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED702', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED703', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED703', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED704', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED704', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED705', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED705', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED706', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED706', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED707', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED707', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED708', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED708', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED709', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED709', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED710', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED710', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED711', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED711', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED712', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED712', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED713', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED713', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED714', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED714', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED715', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED715', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED716', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED716', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED717', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED717', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED724', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED724', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED725', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED725', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED726', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED726', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED727', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED727', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED728', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED728', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED729', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED729', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED730', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED730', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/DIGI_VMEvsuTCA/FED/FED731', [{'path':'Hcal2/DigiComparisonTask/Missing/FED/FED731', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED1100', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED1100', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED1102', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED1102', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED1104', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED1104', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED1106', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED1106', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED1108', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED1108', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED1110', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED1110', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED1112', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED1112', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED1114', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED1114', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED1116', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED1116', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED1118', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED1118', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED1120', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED1120', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED1122', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED1122', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED1132', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED1132', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED700', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED700', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED701', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED701', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED702', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED702', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED703', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED703', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED704', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED704', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED705', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED705', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED706', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED706', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED707', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED707', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED708', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED708', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED709', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED709', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED710', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED710', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED711', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED711', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED712', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED712', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED713', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED713', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED714', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED714', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED715', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED715', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED716', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED716', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED717', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED717', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED724', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED724', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED725', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED725', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED726', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED726', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED727', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED727', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED728', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED728', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED729', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED729', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED730', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED730', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Missing/TP_VMEvsuTCA/FED/FED731', [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED731', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED1100', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED1100', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED1102', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED1102', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED1104', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED1104', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED1106', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED1106', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED1108', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED1108', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED1110', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED1110', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED1112', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED1112', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED1114', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED1114', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED1116', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED1116', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED1118', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED1118', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED1120', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED1120', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED1122', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED1122', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED1132', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED1132', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED700', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED700', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED701', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED701', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED702', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED702', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED703', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED703', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED704', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED704', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED705', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED705', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED706', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED706', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED707', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED707', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED708', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED708', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED709', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED709', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED710', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED710', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED711', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED711', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED712', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED712', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED713', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED713', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED714', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED714', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED715', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED715', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED716', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED716', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED717', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED717', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED724', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED724', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED725', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED725', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED726', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED726', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED727', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED727', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED728', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED728', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED729', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED729', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED730', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED730', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP_VMEvsuTCA/FED/FED731', [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED731', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'ADC_TS7/DIGI_VMEvsuTCA/Subdet/HB', [{'path':'Hcal2/DigiComparisonTask/ADC_TS7/Subdet/HB', 'description':"""ADC Correlation for TS7. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADC_TS7/DIGI_VMEvsuTCA/Subdet/HE', [{'path':'Hcal2/DigiComparisonTask/ADC_TS7/Subdet/HE', 'description':"""ADC Correlation for TS7. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADC_TS7/DIGI_VMEvsuTCA/Subdet/HF', [{'path':'Hcal2/DigiComparisonTask/ADC_TS7/Subdet/HF', 'description':"""ADC Correlation for TS7. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADC_TS7/DIGI_VMEvsuTCA/Subdet/HO', [{'path':'Hcal2/DigiComparisonTask/ADC_TS7/Subdet/HO', 'description':"""ADC Correlation for TS7. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADC_TS3/DIGI_VMEvsuTCA/Subdet/HB', [{'path':'Hcal2/DigiComparisonTask/ADC_TS3/Subdet/HB', 'description':"""ADC Correlation for TS3. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADC_TS3/DIGI_VMEvsuTCA/Subdet/HE', [{'path':'Hcal2/DigiComparisonTask/ADC_TS3/Subdet/HE', 'description':"""ADC Correlation for TS3. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADC_TS3/DIGI_VMEvsuTCA/Subdet/HF', [{'path':'Hcal2/DigiComparisonTask/ADC_TS3/Subdet/HF', 'description':"""ADC Correlation for TS3. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADC_TS3/DIGI_VMEvsuTCA/Subdet/HO', [{'path':'Hcal2/DigiComparisonTask/ADC_TS3/Subdet/HO', 'description':"""ADC Correlation for TS3. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP_VMEvsuTCA', [{'path':'Hcal2/TPComparisonTask/FGMsm/FGMsm', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Et_TS2/TP_VMEvsuTCA/TTSubdet/HBHE', [{'path':'Hcal2/TPComparisonTask/Et_TS2/TTSubdet/HBHE', 'description':"""Et Correlation for TS2. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Trigger_Primitives_Comparison_Ta">Details...</a>"""}])

hcallayout(dqmitems, 'Et_TS2/TP_VMEvsuTCA/TTSubdet/HF', [{'path':'Hcal2/TPComparisonTask/Et_TS2/TTSubdet/HF', 'description':"""Et Correlation for TS2. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Trigger_Primitives_Comparison_Ta">Details...</a>"""}])

hcallayout(dqmitems, 'ADC_TS4/DIGI_VMEvsuTCA/Subdet/HB', [{'path':'Hcal2/DigiComparisonTask/ADC_TS4/Subdet/HB', 'description':"""ADC Correlation for TS4. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADC_TS4/DIGI_VMEvsuTCA/Subdet/HE', [{'path':'Hcal2/DigiComparisonTask/ADC_TS4/Subdet/HE', 'description':"""ADC Correlation for TS4. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADC_TS4/DIGI_VMEvsuTCA/Subdet/HF', [{'path':'Hcal2/DigiComparisonTask/ADC_TS4/Subdet/HF', 'description':"""ADC Correlation for TS4. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADC_TS4/DIGI_VMEvsuTCA/Subdet/HO', [{'path':'Hcal2/DigiComparisonTask/ADC_TS4/Subdet/HO', 'description':"""ADC Correlation for TS4. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADC_TS5/DIGI_VMEvsuTCA/Subdet/HB', [{'path':'Hcal2/DigiComparisonTask/ADC_TS5/Subdet/HB', 'description':"""ADC Correlation for TS5. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADC_TS5/DIGI_VMEvsuTCA/Subdet/HE', [{'path':'Hcal2/DigiComparisonTask/ADC_TS5/Subdet/HE', 'description':"""ADC Correlation for TS5. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADC_TS5/DIGI_VMEvsuTCA/Subdet/HF', [{'path':'Hcal2/DigiComparisonTask/ADC_TS5/Subdet/HF', 'description':"""ADC Correlation for TS5. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'ADC_TS5/DIGI_VMEvsuTCA/Subdet/HO', [{'path':'Hcal2/DigiComparisonTask/ADC_TS5/Subdet/HO', 'description':"""ADC Correlation for TS5. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, 'Summary/RECO', [{'path':'Hcal2/RecHitTask/Summary/Summary', 'description':"""Summary. Anything that is not either WHITE or GREEN is BAD.<br>Color Scheme:<br><font color='green'>GOOD</font> for GOOD<br><font color='yellow'>PROBLEMATIC</font> for Problematic<br><font color='red'>BAD</font> for BAD<br><font color='black'>BAD</font> for BAD<br>WHITE color stands for INAPPLICABLE flag<br>Flags(Y) vs FED(X). For details...   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Summary_Generation_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED1100', [{'path':'Hcal/DigiTask/Missing1LS/FED/FED1100', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED1102', [{'path':'Hcal/DigiTask/Missing1LS/FED/FED1102', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED1104', [{'path':'Hcal/DigiTask/Missing1LS/FED/FED1104', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED1106', [{'path':'Hcal/DigiTask/Missing1LS/FED/FED1106', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED1108', [{'path':'Hcal/DigiTask/Missing1LS/FED/FED1108', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED1110', [{'path':'Hcal/DigiTask/Missing1LS/FED/FED1110', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED1112', [{'path':'Hcal/DigiTask/Missing1LS/FED/FED1112', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED1114', [{'path':'Hcal/DigiTask/Missing1LS/FED/FED1114', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED1116', [{'path':'Hcal/DigiTask/Missing1LS/FED/FED1116', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED1118', [{'path':'Hcal/DigiTask/Missing1LS/FED/FED1118', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED1120', [{'path':'Hcal/DigiTask/Missing1LS/FED/FED1120', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED1122', [{'path':'Hcal/DigiTask/Missing1LS/FED/FED1122', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED1132', [{'path':'Hcal/DigiTask/Missing1LS/FED/FED1132', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED724', [{'path':'Hcal/DigiTask/Missing1LS/FED/FED724', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED725', [{'path':'Hcal/DigiTask/Missing1LS/FED/FED725', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED726', [{'path':'Hcal/DigiTask/Missing1LS/FED/FED726', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED727', [{'path':'Hcal/DigiTask/Missing1LS/FED/FED727', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED728', [{'path':'Hcal/DigiTask/Missing1LS/FED/FED728', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED729', [{'path':'Hcal/DigiTask/Missing1LS/FED/FED729', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED730', [{'path':'Hcal/DigiTask/Missing1LS/FED/FED730', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED731', [{'path':'Hcal/DigiTask/Missing1LS/FED/FED731', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'EtCorr/TP/TTSubdet/HBHE', [{'path':'Hcal/TPTask/EtCorr/TTSubdet/HBHE', 'description':"""Et Correlation Distributions. Emulator(Y) vs Data(X). Channels not present in respective Collections are plotted as Et=-2.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtCorr/TP/TTSubdet/HF', [{'path':'Hcal/TPTask/EtCorr/TTSubdet/HF', 'description':"""Et Correlation Distributions. Emulator(Y) vs Data(X). Channels not present in respective Collections are plotted as Et=-2.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Timing/DIGI/SubdetPM/HBM', [{'path':'Hcal/DigiTask/Timing/SubdetPM/HBM', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Timing/DIGI/SubdetPM/HBP', [{'path':'Hcal/DigiTask/Timing/SubdetPM/HBP', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Timing/DIGI/SubdetPM/HEM', [{'path':'Hcal/DigiTask/Timing/SubdetPM/HEM', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Timing/DIGI/SubdetPM/HEP', [{'path':'Hcal/DigiTask/Timing/SubdetPM/HEP', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Timing/DIGI/SubdetPM/HFM', [{'path':'Hcal/DigiTask/Timing/SubdetPM/HFM', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Timing/DIGI/SubdetPM/HFP', [{'path':'Hcal/DigiTask/Timing/SubdetPM/HFP', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Timing/DIGI/SubdetPM/HOM', [{'path':'Hcal/DigiTask/Timing/SubdetPM/HOM', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Timing/DIGI/SubdetPM/HOP', [{'path':'Hcal/DigiTask/Timing/SubdetPM/HOP', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyEmul/TP/Electronics/VME', [{'path':'Hcal/TPTask/OccupancyEmul/Electronics/VME', 'description':"""Occupancy Distributions for Emulator  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'OccupancyEmul/TP/Electronics/uTCA', [{'path':'Hcal/TPTask/OccupancyEmul/Electronics/uTCA', 'description':"""Occupancy Distributions for Emulator  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'BcnMsm/RAW/Electronics/VME', [{'path':'Hcal/RawTask/BcnMsm/Electronics/VME', 'description':"""BX Number Mismatches.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'BcnMsm/RAW/Electronics/uTCA', [{'path':'Hcal/RawTask/BcnMsm/Electronics/uTCA', 'description':"""BX Number Mismatches.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/depth/depth1', [{'path':'Hcal/DigiTask/OccupancyCut/depth/depth1', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/depth/depth2', [{'path':'Hcal/DigiTask/OccupancyCut/depth/depth2', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/depth/depth3', [{'path':'Hcal/DigiTask/OccupancyCut/depth/depth3', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/depth/depth4', [{'path':'Hcal/DigiTask/OccupancyCut/depth/depth4', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/DIGI/Electronics/VME', [{'path':'Hcal/DigiTask/Occupancy/Electronics/VME', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/DIGI/Electronics/uTCA', [{'path':'Hcal/DigiTask/Occupancy/Electronics/uTCA', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'EtEmul/TP/TTSubdet/HBHE', [{'path':'Hcal/TPTask/EtEmul/TTSubdet/HBHE', 'description':"""Et Emulator Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtEmul/TP/TTSubdet/HF', [{'path':'Hcal/TPTask/EtEmul/TTSubdet/HF', 'description':"""Et Emulator Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Occupancy/DIGI/depth/depth1', [{'path':'Hcal/DigiTask/Occupancy/depth/depth1', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/DIGI/depth/depth2', [{'path':'Hcal/DigiTask/Occupancy/depth/depth2', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/DIGI/depth/depth3', [{'path':'Hcal/DigiTask/Occupancy/depth/depth3', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/DIGI/depth/depth4', [{'path':'Hcal/DigiTask/Occupancy/depth/depth4', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED1100', [{'path':'Hcal/DigiTask/OccupancyNRCut/FED/FED1100', 'description':"""Occupancy Total after a cut without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED1102', [{'path':'Hcal/DigiTask/OccupancyNRCut/FED/FED1102', 'description':"""Occupancy Total after a cut without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED1104', [{'path':'Hcal/DigiTask/OccupancyNRCut/FED/FED1104', 'description':"""Occupancy Total after a cut without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED1106', [{'path':'Hcal/DigiTask/OccupancyNRCut/FED/FED1106', 'description':"""Occupancy Total after a cut without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED1108', [{'path':'Hcal/DigiTask/OccupancyNRCut/FED/FED1108', 'description':"""Occupancy Total after a cut without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED1110', [{'path':'Hcal/DigiTask/OccupancyNRCut/FED/FED1110', 'description':"""Occupancy Total after a cut without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED1112', [{'path':'Hcal/DigiTask/OccupancyNRCut/FED/FED1112', 'description':"""Occupancy Total after a cut without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED1114', [{'path':'Hcal/DigiTask/OccupancyNRCut/FED/FED1114', 'description':"""Occupancy Total after a cut without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED1116', [{'path':'Hcal/DigiTask/OccupancyNRCut/FED/FED1116', 'description':"""Occupancy Total after a cut without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED1118', [{'path':'Hcal/DigiTask/OccupancyNRCut/FED/FED1118', 'description':"""Occupancy Total after a cut without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED1120', [{'path':'Hcal/DigiTask/OccupancyNRCut/FED/FED1120', 'description':"""Occupancy Total after a cut without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED1122', [{'path':'Hcal/DigiTask/OccupancyNRCut/FED/FED1122', 'description':"""Occupancy Total after a cut without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED1132', [{'path':'Hcal/DigiTask/OccupancyNRCut/FED/FED1132', 'description':"""Occupancy Total after a cut without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED724', [{'path':'Hcal/DigiTask/OccupancyNRCut/FED/FED724', 'description':"""Occupancy Total after a cut without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED725', [{'path':'Hcal/DigiTask/OccupancyNRCut/FED/FED725', 'description':"""Occupancy Total after a cut without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED726', [{'path':'Hcal/DigiTask/OccupancyNRCut/FED/FED726', 'description':"""Occupancy Total after a cut without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED727', [{'path':'Hcal/DigiTask/OccupancyNRCut/FED/FED727', 'description':"""Occupancy Total after a cut without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED728', [{'path':'Hcal/DigiTask/OccupancyNRCut/FED/FED728', 'description':"""Occupancy Total after a cut without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED729', [{'path':'Hcal/DigiTask/OccupancyNRCut/FED/FED729', 'description':"""Occupancy Total after a cut without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED730', [{'path':'Hcal/DigiTask/OccupancyNRCut/FED/FED730', 'description':"""Occupancy Total after a cut without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED731', [{'path':'Hcal/DigiTask/OccupancyNRCut/FED/FED731', 'description':"""Occupancy Total after a cut without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1100S1', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1100S1', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1100S10', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1100S10', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1100S11', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1100S11', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1100S12', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1100S12', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1100S2', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1100S2', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1100S3', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1100S3', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1100S4', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1100S4', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1100S5', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1100S5', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1100S6', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1100S6', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1100S7', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1100S7', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1100S8', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1100S8', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1100S9', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1100S9', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1102S1', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1102S1', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1102S10', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1102S10', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1102S11', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1102S11', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1102S12', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1102S12', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1102S2', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1102S2', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1102S3', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1102S3', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1102S4', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1102S4', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1102S5', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1102S5', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1102S6', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1102S6', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1102S7', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1102S7', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1102S8', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1102S8', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1102S9', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1102S9', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1104S1', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1104S1', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1104S10', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1104S10', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1104S11', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1104S11', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1104S12', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1104S12', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1104S2', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1104S2', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1104S3', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1104S3', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1104S4', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1104S4', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1104S5', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1104S5', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1104S6', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1104S6', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1104S7', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1104S7', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1104S8', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1104S8', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1104S9', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1104S9', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1106S1', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1106S1', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1106S10', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1106S10', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1106S11', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1106S11', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1106S12', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1106S12', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1106S2', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1106S2', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1106S3', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1106S3', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1106S4', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1106S4', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1106S5', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1106S5', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1106S6', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1106S6', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1106S7', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1106S7', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1106S8', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1106S8', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1106S9', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1106S9', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1108S1', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1108S1', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1108S10', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1108S10', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1108S11', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1108S11', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1108S12', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1108S12', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1108S2', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1108S2', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1108S3', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1108S3', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1108S4', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1108S4', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1108S5', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1108S5', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1108S6', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1108S6', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1108S7', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1108S7', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1108S8', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1108S8', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1108S9', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1108S9', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1110S1', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1110S1', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1110S10', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1110S10', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1110S11', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1110S11', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1110S12', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1110S12', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1110S2', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1110S2', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1110S3', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1110S3', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1110S4', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1110S4', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1110S5', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1110S5', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1110S6', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1110S6', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1110S7', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1110S7', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1110S8', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1110S8', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1110S9', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1110S9', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1112S1', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1112S1', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1112S10', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1112S10', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1112S11', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1112S11', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1112S12', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1112S12', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1112S2', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1112S2', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1112S3', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1112S3', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1112S4', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1112S4', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1112S5', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1112S5', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1112S6', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1112S6', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1112S7', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1112S7', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1112S8', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1112S8', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1112S9', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1112S9', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1114S1', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1114S1', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1114S10', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1114S10', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1114S11', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1114S11', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1114S12', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1114S12', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1114S2', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1114S2', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1114S3', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1114S3', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1114S4', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1114S4', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1114S5', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1114S5', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1114S6', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1114S6', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1114S7', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1114S7', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1114S8', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1114S8', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1114S9', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1114S9', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1116S1', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1116S1', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1116S10', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1116S10', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1116S11', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1116S11', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1116S12', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1116S12', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1116S2', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1116S2', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1116S3', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1116S3', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1116S4', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1116S4', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1116S5', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1116S5', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1116S6', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1116S6', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1116S7', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1116S7', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1116S8', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1116S8', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1116S9', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1116S9', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1118S1', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1118S1', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1118S10', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1118S10', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1118S11', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1118S11', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1118S12', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1118S12', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1118S2', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1118S2', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1118S3', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1118S3', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1118S4', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1118S4', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1118S5', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1118S5', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1118S6', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1118S6', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1118S7', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1118S7', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1118S8', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1118S8', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1118S9', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1118S9', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1120S1', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1120S1', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1120S10', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1120S10', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1120S11', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1120S11', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1120S12', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1120S12', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1120S2', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1120S2', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1120S3', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1120S3', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1120S4', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1120S4', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1120S5', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1120S5', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1120S6', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1120S6', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1120S7', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1120S7', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1120S8', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1120S8', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1120S9', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1120S9', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1122S1', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1122S1', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1122S10', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1122S10', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1122S11', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1122S11', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1122S12', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1122S12', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1122S2', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1122S2', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1122S3', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1122S3', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1122S4', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1122S4', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1122S5', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1122S5', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1122S6', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1122S6', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1122S7', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1122S7', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1122S8', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1122S8', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1122S9', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1122S9', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1132S12', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED1132S12', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED724S0', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED724S0', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED724S1', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED724S1', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED724S10', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED724S10', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED724S11', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED724S11', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED724S2', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED724S2', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED724S3', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED724S3', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED724S4', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED724S4', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED724S5', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED724S5', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED724S6', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED724S6', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED724S7', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED724S7', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED724S8', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED724S8', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED724S9', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED724S9', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED725S0', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED725S0', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED725S1', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED725S1', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED725S10', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED725S10', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED725S11', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED725S11', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED725S2', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED725S2', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED725S3', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED725S3', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED725S4', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED725S4', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED725S5', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED725S5', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED725S6', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED725S6', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED725S7', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED725S7', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED725S8', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED725S8', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED725S9', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED725S9', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED726S0', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED726S0', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED726S1', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED726S1', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED726S10', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED726S10', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED726S11', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED726S11', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED726S12', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED726S12', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED726S13', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED726S13', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED726S2', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED726S2', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED726S3', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED726S3', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED726S4', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED726S4', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED726S5', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED726S5', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED726S6', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED726S6', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED726S7', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED726S7', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED726S8', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED726S8', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED726S9', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED726S9', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED727S0', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED727S0', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED727S1', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED727S1', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED727S10', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED727S10', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED727S11', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED727S11', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED727S12', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED727S12', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED727S13', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED727S13', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED727S2', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED727S2', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED727S3', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED727S3', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED727S4', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED727S4', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED727S5', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED727S5', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED727S6', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED727S6', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED727S7', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED727S7', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED727S8', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED727S8', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED727S9', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED727S9', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED728S0', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED728S0', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED728S1', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED728S1', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED728S10', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED728S10', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED728S11', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED728S11', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED728S12', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED728S12', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED728S13', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED728S13', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED728S2', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED728S2', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED728S3', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED728S3', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED728S4', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED728S4', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED728S5', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED728S5', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED728S6', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED728S6', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED728S7', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED728S7', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED728S8', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED728S8', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED728S9', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED728S9', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED729S0', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED729S0', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED729S1', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED729S1', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED729S10', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED729S10', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED729S11', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED729S11', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED729S12', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED729S12', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED729S13', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED729S13', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED729S2', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED729S2', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED729S3', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED729S3', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED729S4', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED729S4', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED729S5', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED729S5', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED729S6', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED729S6', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED729S7', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED729S7', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED729S8', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED729S8', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED729S9', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED729S9', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED730S0', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED730S0', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED730S1', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED730S1', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED730S10', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED730S10', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED730S11', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED730S11', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED730S12', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED730S12', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED730S13', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED730S13', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED730S2', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED730S2', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED730S3', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED730S3', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED730S4', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED730S4', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED730S5', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED730S5', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED730S6', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED730S6', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED730S7', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED730S7', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED730S8', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED730S8', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED730S9', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED730S9', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED731S0', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED731S0', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED731S1', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED731S1', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED731S10', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED731S10', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED731S11', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED731S11', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED731S2', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED731S2', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED731S3', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED731S3', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED731S4', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED731S4', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED731S5', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED731S5', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED731S6', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED731S6', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED731S7', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED731S7', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED731S8', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED731S8', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED731S9', [{'path':'Hcal/DigiTask/Shape/FEDSlot/FED731S9', 'description':"""Signal Shape.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'BadQualityvsLS/RAW', [{'path':'Hcal/RawTask/BadQualityvsLS/BadQualityvsLS', 'description':"""BadQuality Channels vs LS  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'BadQualityvsBX/RAW', [{'path':'Hcal/RawTask/BadQualityvsBX/BadQualityvsBX', 'description':"""BadQuality Channels vs BX.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'MsnData/TP/Electronics/VME', [{'path':'Hcal/TPTask/MsnData/Electronics/VME', 'description':"""Distribution of channels missing from Data w.r.t. Emulator  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'MsnData/TP/Electronics/uTCA', [{'path':'Hcal/TPTask/MsnData/Electronics/uTCA', 'description':"""Distribution of channels missing from Data w.r.t. Emulator  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'OccupancyData/TP', [{'path':'Hcal/TPTask/OccupancyData/OccupancyData', 'description':"""Occupancy Distributions for Data  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtEmul/TP', [{'path':'Hcal/TPTask/EtEmul/EtEmul', 'description':"""Et Emulator Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'BadQuality/RAW/depth/depth1', [{'path':'Hcal/RawTask/BadQuality/depth/depth1', 'description':"""Bad Quality Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'BadQuality/RAW/depth/depth2', [{'path':'Hcal/RawTask/BadQuality/depth/depth2', 'description':"""Bad Quality Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'BadQuality/RAW/depth/depth3', [{'path':'Hcal/RawTask/BadQuality/depth/depth3', 'description':"""Bad Quality Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'BadQuality/RAW/depth/depth4', [{'path':'Hcal/RawTask/BadQuality/depth/depth4', 'description':"""Bad Quality Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtData/TP/Electronics/VME', [{'path':'Hcal/TPTask/EtData/Electronics/VME', 'description':"""Et Data Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtData/TP/Electronics/uTCA', [{'path':'Hcal/TPTask/EtData/Electronics/uTCA', 'description':"""Et Data Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'SumQ/DIGI/depth/depth1', [{'path':'Hcal/DigiTask/SumQ/depth/depth1', 'description':"""Total Charge per channel per event.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'SumQ/DIGI/depth/depth2', [{'path':'Hcal/DigiTask/SumQ/depth/depth2', 'description':"""Total Charge per channel per event.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'SumQ/DIGI/depth/depth3', [{'path':'Hcal/DigiTask/SumQ/depth/depth3', 'description':"""Total Charge per channel per event.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'SumQ/DIGI/depth/depth4', [{'path':'Hcal/DigiTask/SumQ/depth/depth4', 'description':"""Total Charge per channel per event.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Summary/DIGI', [{'path':'Hcal/DigiTask/Summary/Summary', 'description':"""Summary. Anything that is not either WHITE or GREEN is BAD.<br>Color Scheme:<br><font color='green'>GOOD</font> for GOOD<br><font color='yellow'>PROBLEMATIC</font> for Problematic<br><font color='red'>BAD</font> for BAD<br><font color='black'>BAD</font> for BAD<br>WHITE color stands for INAPPLICABLE flag<br>Flags(Y) vs FED(X). For details...   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Summary_Generation_Description">Details...</a>"""}])

hcallayout(dqmitems, 'SumQ/DIGI/SubdetPM/HBM', [{'path':'Hcal/DigiTask/SumQ/SubdetPM/HBM', 'description':"""Total Charge per channel per event.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'SumQ/DIGI/SubdetPM/HBP', [{'path':'Hcal/DigiTask/SumQ/SubdetPM/HBP', 'description':"""Total Charge per channel per event.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'SumQ/DIGI/SubdetPM/HEM', [{'path':'Hcal/DigiTask/SumQ/SubdetPM/HEM', 'description':"""Total Charge per channel per event.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'SumQ/DIGI/SubdetPM/HEP', [{'path':'Hcal/DigiTask/SumQ/SubdetPM/HEP', 'description':"""Total Charge per channel per event.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'SumQ/DIGI/SubdetPM/HFM', [{'path':'Hcal/DigiTask/SumQ/SubdetPM/HFM', 'description':"""Total Charge per channel per event.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'SumQ/DIGI/SubdetPM/HFP', [{'path':'Hcal/DigiTask/SumQ/SubdetPM/HFP', 'description':"""Total Charge per channel per event.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'SumQ/DIGI/SubdetPM/HOM', [{'path':'Hcal/DigiTask/SumQ/SubdetPM/HOM', 'description':"""Total Charge per channel per event.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'SumQ/DIGI/SubdetPM/HOP', [{'path':'Hcal/DigiTask/SumQ/SubdetPM/HOP', 'description':"""Total Charge per channel per event.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED1100', [{'path':'Hcal/DigiTask/Occupancy/FED/FED1100', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED1102', [{'path':'Hcal/DigiTask/Occupancy/FED/FED1102', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED1104', [{'path':'Hcal/DigiTask/Occupancy/FED/FED1104', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED1106', [{'path':'Hcal/DigiTask/Occupancy/FED/FED1106', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED1108', [{'path':'Hcal/DigiTask/Occupancy/FED/FED1108', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED1110', [{'path':'Hcal/DigiTask/Occupancy/FED/FED1110', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED1112', [{'path':'Hcal/DigiTask/Occupancy/FED/FED1112', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED1114', [{'path':'Hcal/DigiTask/Occupancy/FED/FED1114', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED1116', [{'path':'Hcal/DigiTask/Occupancy/FED/FED1116', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED1118', [{'path':'Hcal/DigiTask/Occupancy/FED/FED1118', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED1120', [{'path':'Hcal/DigiTask/Occupancy/FED/FED1120', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED1122', [{'path':'Hcal/DigiTask/Occupancy/FED/FED1122', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED1132', [{'path':'Hcal/DigiTask/Occupancy/FED/FED1132', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED724', [{'path':'Hcal/DigiTask/Occupancy/FED/FED724', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED725', [{'path':'Hcal/DigiTask/Occupancy/FED/FED725', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED726', [{'path':'Hcal/DigiTask/Occupancy/FED/FED726', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED727', [{'path':'Hcal/DigiTask/Occupancy/FED/FED727', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED728', [{'path':'Hcal/DigiTask/Occupancy/FED/FED728', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED729', [{'path':'Hcal/DigiTask/Occupancy/FED/FED729', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED730', [{'path':'Hcal/DigiTask/Occupancy/FED/FED730', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED731', [{'path':'Hcal/DigiTask/Occupancy/FED/FED731', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'EtData/TP', [{'path':'Hcal/TPTask/EtData/EtData', 'description':"""Et Data Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'OccupancyCutData/TP/Electronics/VME', [{'path':'Hcal/TPTask/OccupancyCutData/Electronics/VME', 'description':"""Occupancy Distributions for Data with a cut on Et  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'OccupancyCutData/TP/Electronics/uTCA', [{'path':'Hcal/TPTask/OccupancyCutData/Electronics/uTCA', 'description':"""Occupancy Distributions for Data with a cut on Et  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtEmul/TP/Electronics/VME', [{'path':'Hcal/TPTask/EtEmul/Electronics/VME', 'description':"""Et Emulator Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtEmul/TP/Electronics/uTCA', [{'path':'Hcal/TPTask/EtEmul/Electronics/uTCA', 'description':"""Et Emulator Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'OccupancyData/TP/Electronics/VME', [{'path':'Hcal/TPTask/OccupancyData/Electronics/VME', 'description':"""Occupancy Distributions for Data  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'OccupancyData/TP/Electronics/uTCA', [{'path':'Hcal/TPTask/OccupancyData/Electronics/uTCA', 'description':"""Occupancy Distributions for Data  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FED/FED1100', [{'path':'Hcal/DigiTask/TimingvsLS/FED/FED1100', 'description':"""Timing either @RECO or @DIGI level.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FED/FED1102', [{'path':'Hcal/DigiTask/TimingvsLS/FED/FED1102', 'description':"""Timing either @RECO or @DIGI level.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FED/FED1104', [{'path':'Hcal/DigiTask/TimingvsLS/FED/FED1104', 'description':"""Timing either @RECO or @DIGI level.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FED/FED1106', [{'path':'Hcal/DigiTask/TimingvsLS/FED/FED1106', 'description':"""Timing either @RECO or @DIGI level.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FED/FED1108', [{'path':'Hcal/DigiTask/TimingvsLS/FED/FED1108', 'description':"""Timing either @RECO or @DIGI level.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FED/FED1110', [{'path':'Hcal/DigiTask/TimingvsLS/FED/FED1110', 'description':"""Timing either @RECO or @DIGI level.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FED/FED1112', [{'path':'Hcal/DigiTask/TimingvsLS/FED/FED1112', 'description':"""Timing either @RECO or @DIGI level.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FED/FED1114', [{'path':'Hcal/DigiTask/TimingvsLS/FED/FED1114', 'description':"""Timing either @RECO or @DIGI level.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FED/FED1116', [{'path':'Hcal/DigiTask/TimingvsLS/FED/FED1116', 'description':"""Timing either @RECO or @DIGI level.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FED/FED1118', [{'path':'Hcal/DigiTask/TimingvsLS/FED/FED1118', 'description':"""Timing either @RECO or @DIGI level.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FED/FED1120', [{'path':'Hcal/DigiTask/TimingvsLS/FED/FED1120', 'description':"""Timing either @RECO or @DIGI level.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FED/FED1122', [{'path':'Hcal/DigiTask/TimingvsLS/FED/FED1122', 'description':"""Timing either @RECO or @DIGI level.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FED/FED1132', [{'path':'Hcal/DigiTask/TimingvsLS/FED/FED1132', 'description':"""Timing either @RECO or @DIGI level.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FED/FED724', [{'path':'Hcal/DigiTask/TimingvsLS/FED/FED724', 'description':"""Timing either @RECO or @DIGI level.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FED/FED725', [{'path':'Hcal/DigiTask/TimingvsLS/FED/FED725', 'description':"""Timing either @RECO or @DIGI level.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FED/FED726', [{'path':'Hcal/DigiTask/TimingvsLS/FED/FED726', 'description':"""Timing either @RECO or @DIGI level.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FED/FED727', [{'path':'Hcal/DigiTask/TimingvsLS/FED/FED727', 'description':"""Timing either @RECO or @DIGI level.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FED/FED728', [{'path':'Hcal/DigiTask/TimingvsLS/FED/FED728', 'description':"""Timing either @RECO or @DIGI level.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FED/FED729', [{'path':'Hcal/DigiTask/TimingvsLS/FED/FED729', 'description':"""Timing either @RECO or @DIGI level.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FED/FED730', [{'path':'Hcal/DigiTask/TimingvsLS/FED/FED730', 'description':"""Timing either @RECO or @DIGI level.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FED/FED731', [{'path':'Hcal/DigiTask/TimingvsLS/FED/FED731', 'description':"""Timing either @RECO or @DIGI level.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'EtData/TP/TTSubdet/HBHE', [{'path':'Hcal/TPTask/EtData/TTSubdet/HBHE', 'description':"""Et Data Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtData/TP/TTSubdet/HF', [{'path':'Hcal/TPTask/EtData/TTSubdet/HF', 'description':"""Et Data Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED1100', [{'path':'Hcal/RawTask/BadQuality/FED/FED1100', 'description':"""Bad Quality Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED1102', [{'path':'Hcal/RawTask/BadQuality/FED/FED1102', 'description':"""Bad Quality Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED1104', [{'path':'Hcal/RawTask/BadQuality/FED/FED1104', 'description':"""Bad Quality Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED1106', [{'path':'Hcal/RawTask/BadQuality/FED/FED1106', 'description':"""Bad Quality Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED1108', [{'path':'Hcal/RawTask/BadQuality/FED/FED1108', 'description':"""Bad Quality Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED1110', [{'path':'Hcal/RawTask/BadQuality/FED/FED1110', 'description':"""Bad Quality Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED1112', [{'path':'Hcal/RawTask/BadQuality/FED/FED1112', 'description':"""Bad Quality Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED1114', [{'path':'Hcal/RawTask/BadQuality/FED/FED1114', 'description':"""Bad Quality Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED1116', [{'path':'Hcal/RawTask/BadQuality/FED/FED1116', 'description':"""Bad Quality Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED1118', [{'path':'Hcal/RawTask/BadQuality/FED/FED1118', 'description':"""Bad Quality Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED1120', [{'path':'Hcal/RawTask/BadQuality/FED/FED1120', 'description':"""Bad Quality Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED1122', [{'path':'Hcal/RawTask/BadQuality/FED/FED1122', 'description':"""Bad Quality Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED1132', [{'path':'Hcal/RawTask/BadQuality/FED/FED1132', 'description':"""Bad Quality Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED724', [{'path':'Hcal/RawTask/BadQuality/FED/FED724', 'description':"""Bad Quality Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED725', [{'path':'Hcal/RawTask/BadQuality/FED/FED725', 'description':"""Bad Quality Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED726', [{'path':'Hcal/RawTask/BadQuality/FED/FED726', 'description':"""Bad Quality Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED727', [{'path':'Hcal/RawTask/BadQuality/FED/FED727', 'description':"""Bad Quality Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED728', [{'path':'Hcal/RawTask/BadQuality/FED/FED728', 'description':"""Bad Quality Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED729', [{'path':'Hcal/RawTask/BadQuality/FED/FED729', 'description':"""Bad Quality Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED730', [{'path':'Hcal/RawTask/BadQuality/FED/FED730', 'description':"""Bad Quality Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED731', [{'path':'Hcal/RawTask/BadQuality/FED/FED731', 'description':"""Bad Quality Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'MsnData/TP', [{'path':'Hcal/TPTask/MsnData/MsnData', 'description':"""Distribution of channels missing from Data w.r.t. Emulator  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED1100', [{'path':'Hcal/DigiTask/OccupancyCut/FED/FED1100', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED1102', [{'path':'Hcal/DigiTask/OccupancyCut/FED/FED1102', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED1104', [{'path':'Hcal/DigiTask/OccupancyCut/FED/FED1104', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED1106', [{'path':'Hcal/DigiTask/OccupancyCut/FED/FED1106', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED1108', [{'path':'Hcal/DigiTask/OccupancyCut/FED/FED1108', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED1110', [{'path':'Hcal/DigiTask/OccupancyCut/FED/FED1110', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED1112', [{'path':'Hcal/DigiTask/OccupancyCut/FED/FED1112', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED1114', [{'path':'Hcal/DigiTask/OccupancyCut/FED/FED1114', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED1116', [{'path':'Hcal/DigiTask/OccupancyCut/FED/FED1116', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED1118', [{'path':'Hcal/DigiTask/OccupancyCut/FED/FED1118', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED1120', [{'path':'Hcal/DigiTask/OccupancyCut/FED/FED1120', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED1122', [{'path':'Hcal/DigiTask/OccupancyCut/FED/FED1122', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED1132', [{'path':'Hcal/DigiTask/OccupancyCut/FED/FED1132', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED724', [{'path':'Hcal/DigiTask/OccupancyCut/FED/FED724', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED725', [{'path':'Hcal/DigiTask/OccupancyCut/FED/FED725', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED726', [{'path':'Hcal/DigiTask/OccupancyCut/FED/FED726', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED727', [{'path':'Hcal/DigiTask/OccupancyCut/FED/FED727', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED728', [{'path':'Hcal/DigiTask/OccupancyCut/FED/FED728', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED729', [{'path':'Hcal/DigiTask/OccupancyCut/FED/FED729', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED730', [{'path':'Hcal/DigiTask/OccupancyCut/FED/FED730', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED731', [{'path':'Hcal/DigiTask/OccupancyCut/FED/FED731', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED1100', [{'path':'Hcal/DigiTask/DigiSize/FED/FED1100', 'description':"""Digi Size Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED1102', [{'path':'Hcal/DigiTask/DigiSize/FED/FED1102', 'description':"""Digi Size Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED1104', [{'path':'Hcal/DigiTask/DigiSize/FED/FED1104', 'description':"""Digi Size Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED1106', [{'path':'Hcal/DigiTask/DigiSize/FED/FED1106', 'description':"""Digi Size Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED1108', [{'path':'Hcal/DigiTask/DigiSize/FED/FED1108', 'description':"""Digi Size Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED1110', [{'path':'Hcal/DigiTask/DigiSize/FED/FED1110', 'description':"""Digi Size Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED1112', [{'path':'Hcal/DigiTask/DigiSize/FED/FED1112', 'description':"""Digi Size Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED1114', [{'path':'Hcal/DigiTask/DigiSize/FED/FED1114', 'description':"""Digi Size Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED1116', [{'path':'Hcal/DigiTask/DigiSize/FED/FED1116', 'description':"""Digi Size Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED1118', [{'path':'Hcal/DigiTask/DigiSize/FED/FED1118', 'description':"""Digi Size Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED1120', [{'path':'Hcal/DigiTask/DigiSize/FED/FED1120', 'description':"""Digi Size Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED1122', [{'path':'Hcal/DigiTask/DigiSize/FED/FED1122', 'description':"""Digi Size Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED1132', [{'path':'Hcal/DigiTask/DigiSize/FED/FED1132', 'description':"""Digi Size Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED724', [{'path':'Hcal/DigiTask/DigiSize/FED/FED724', 'description':"""Digi Size Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED725', [{'path':'Hcal/DigiTask/DigiSize/FED/FED725', 'description':"""Digi Size Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED726', [{'path':'Hcal/DigiTask/DigiSize/FED/FED726', 'description':"""Digi Size Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED727', [{'path':'Hcal/DigiTask/DigiSize/FED/FED727', 'description':"""Digi Size Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED728', [{'path':'Hcal/DigiTask/DigiSize/FED/FED728', 'description':"""Digi Size Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED729', [{'path':'Hcal/DigiTask/DigiSize/FED/FED729', 'description':"""Digi Size Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED730', [{'path':'Hcal/DigiTask/DigiSize/FED/FED730', 'description':"""Digi Size Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED731', [{'path':'Hcal/DigiTask/DigiSize/FED/FED731', 'description':"""Digi Size Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'OccupancyEmul/TP', [{'path':'Hcal/TPTask/OccupancyEmul/OccupancyEmul', 'description':"""Occupancy Distributions for Emulator  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'OccupancyCutEmul/TP', [{'path':'Hcal/TPTask/OccupancyCutEmul/OccupancyCutEmul', 'description':"""Occupancy Distributions for Emulator with a cut on Et  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Summary/RAW', [{'path':'Hcal/RawTask/Summary/Summary', 'description':"""Summary. Anything that is not either WHITE or GREEN is BAD.<br>Color Scheme:<br><font color='green'>GOOD</font> for GOOD<br><font color='yellow'>PROBLEMATIC</font> for Problematic<br><font color='red'>BAD</font> for BAD<br><font color='black'>BAD</font> for BAD<br>WHITE color stands for INAPPLICABLE flag<br>Flags(Y) vs FED(X). For details...   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Summary_Generation_Description">Details...</a>"""}])

hcallayout(dqmitems, 'OccupancyvsLS/DIGI/Subdet/HB', [{'path':'Hcal/DigiTask/OccupancyvsLS/Subdet/HB', 'description':"""Occupancy vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Pedestal_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'OccupancyvsLS/DIGI/Subdet/HE', [{'path':'Hcal/DigiTask/OccupancyvsLS/Subdet/HE', 'description':"""Occupancy vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Pedestal_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'OccupancyvsLS/DIGI/Subdet/HF', [{'path':'Hcal/DigiTask/OccupancyvsLS/Subdet/HF', 'description':"""Occupancy vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Pedestal_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'OccupancyvsLS/DIGI/Subdet/HO', [{'path':'Hcal/DigiTask/OccupancyvsLS/Subdet/HO', 'description':"""Occupancy vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Pedestal_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGCorr/TP/TTSubdet/HBHE', [{'path':'Hcal/TPTask/FGCorr/TTSubdet/HBHE', 'description':"""Correction of Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGCorr/TP/TTSubdet/HF', [{'path':'Hcal/TPTask/FGCorr/TTSubdet/HF', 'description':"""Correction of Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Summary/TP', [{'path':'Hcal/TPTask/Summary/Summary', 'description':"""Summary. Anything that is not either WHITE or GREEN is BAD.<br>Color Scheme:<br><font color='green'>GOOD</font> for GOOD<br><font color='yellow'>PROBLEMATIC</font> for Problematic<br><font color='red'>BAD</font> for BAD<br><font color='black'>BAD</font> for BAD<br>WHITE color stands for INAPPLICABLE flag<br>Flags(Y) vs FED(X). For details...   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Summary_Generation_Description">Details...</a>"""}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED1100', [{'path':'Hcal/DigiTask/CapId/FED/FED1100', 'description':"""Cap ID Nonrotated Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED1102', [{'path':'Hcal/DigiTask/CapId/FED/FED1102', 'description':"""Cap ID Nonrotated Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED1104', [{'path':'Hcal/DigiTask/CapId/FED/FED1104', 'description':"""Cap ID Nonrotated Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED1106', [{'path':'Hcal/DigiTask/CapId/FED/FED1106', 'description':"""Cap ID Nonrotated Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED1108', [{'path':'Hcal/DigiTask/CapId/FED/FED1108', 'description':"""Cap ID Nonrotated Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED1110', [{'path':'Hcal/DigiTask/CapId/FED/FED1110', 'description':"""Cap ID Nonrotated Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED1112', [{'path':'Hcal/DigiTask/CapId/FED/FED1112', 'description':"""Cap ID Nonrotated Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED1114', [{'path':'Hcal/DigiTask/CapId/FED/FED1114', 'description':"""Cap ID Nonrotated Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED1116', [{'path':'Hcal/DigiTask/CapId/FED/FED1116', 'description':"""Cap ID Nonrotated Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED1118', [{'path':'Hcal/DigiTask/CapId/FED/FED1118', 'description':"""Cap ID Nonrotated Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED1120', [{'path':'Hcal/DigiTask/CapId/FED/FED1120', 'description':"""Cap ID Nonrotated Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED1122', [{'path':'Hcal/DigiTask/CapId/FED/FED1122', 'description':"""Cap ID Nonrotated Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED1132', [{'path':'Hcal/DigiTask/CapId/FED/FED1132', 'description':"""Cap ID Nonrotated Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED724', [{'path':'Hcal/DigiTask/CapId/FED/FED724', 'description':"""Cap ID Nonrotated Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED725', [{'path':'Hcal/DigiTask/CapId/FED/FED725', 'description':"""Cap ID Nonrotated Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED726', [{'path':'Hcal/DigiTask/CapId/FED/FED726', 'description':"""Cap ID Nonrotated Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED727', [{'path':'Hcal/DigiTask/CapId/FED/FED727', 'description':"""Cap ID Nonrotated Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED728', [{'path':'Hcal/DigiTask/CapId/FED/FED728', 'description':"""Cap ID Nonrotated Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED729', [{'path':'Hcal/DigiTask/CapId/FED/FED729', 'description':"""Cap ID Nonrotated Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED730', [{'path':'Hcal/DigiTask/CapId/FED/FED730', 'description':"""Cap ID Nonrotated Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED731', [{'path':'Hcal/DigiTask/CapId/FED/FED731', 'description':"""Cap ID Nonrotated Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'OrnMsm/RAW/Electronics/VME', [{'path':'Hcal/RawTask/OrnMsm/Electronics/VME', 'description':"""Orbit Number Mismatches.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'OrnMsm/RAW/Electronics/uTCA', [{'path':'Hcal/RawTask/OrnMsm/Electronics/uTCA', 'description':"""Orbit Number Mismatches.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/Electronics/VME', [{'path':'Hcal/DigiTask/OccupancyCut/Electronics/VME', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/Electronics/uTCA', [{'path':'Hcal/DigiTask/OccupancyCut/Electronics/uTCA', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCutEmul/TP/Electronics/VME', [{'path':'Hcal/TPTask/OccupancyCutEmul/Electronics/VME', 'description':"""Occupancy Distributions for Emulator with a cut on Et  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'OccupancyCutEmul/TP/Electronics/uTCA', [{'path':'Hcal/TPTask/OccupancyCutEmul/Electronics/uTCA', 'description':"""Occupancy Distributions for Emulator with a cut on Et  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'MsnEmul/TP', [{'path':'Hcal/TPTask/MsnEmul/MsnEmul', 'description':"""Distribution of channels missing from Emulator w.r.t. Data  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP/Electronics/VME', [{'path':'Hcal/TPTask/FGMsm/Electronics/VME', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'FGMsm/TP/Electronics/uTCA', [{'path':'Hcal/TPTask/FGMsm/Electronics/uTCA', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtCorrRatio/TP', [{'path':'Hcal/TPTask/EtCorrRatio/EtCorrRatio', 'description':"""Et Correlation Ratio. It is always min(etd, ete)/max(etd, ete).   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtCorrRatio/TP/Electronics/VME', [{'path':'Hcal/TPTask/EtCorrRatio/Electronics/VME', 'description':"""Et Correlation Ratio. It is always min(etd, ete)/max(etd, ete).   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtCorrRatio/TP/Electronics/uTCA', [{'path':'Hcal/TPTask/EtCorrRatio/Electronics/uTCA', 'description':"""Et Correlation Ratio. It is always min(etd, ete)/max(etd, ete).   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED1100', [{'path':'Hcal/DigiTask/OccupancyNR/FED/FED1100', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED1102', [{'path':'Hcal/DigiTask/OccupancyNR/FED/FED1102', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED1104', [{'path':'Hcal/DigiTask/OccupancyNR/FED/FED1104', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED1106', [{'path':'Hcal/DigiTask/OccupancyNR/FED/FED1106', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED1108', [{'path':'Hcal/DigiTask/OccupancyNR/FED/FED1108', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED1110', [{'path':'Hcal/DigiTask/OccupancyNR/FED/FED1110', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED1112', [{'path':'Hcal/DigiTask/OccupancyNR/FED/FED1112', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED1114', [{'path':'Hcal/DigiTask/OccupancyNR/FED/FED1114', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED1116', [{'path':'Hcal/DigiTask/OccupancyNR/FED/FED1116', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED1118', [{'path':'Hcal/DigiTask/OccupancyNR/FED/FED1118', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED1120', [{'path':'Hcal/DigiTask/OccupancyNR/FED/FED1120', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED1122', [{'path':'Hcal/DigiTask/OccupancyNR/FED/FED1122', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED1132', [{'path':'Hcal/DigiTask/OccupancyNR/FED/FED1132', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED724', [{'path':'Hcal/DigiTask/OccupancyNR/FED/FED724', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED725', [{'path':'Hcal/DigiTask/OccupancyNR/FED/FED725', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED726', [{'path':'Hcal/DigiTask/OccupancyNR/FED/FED726', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED727', [{'path':'Hcal/DigiTask/OccupancyNR/FED/FED727', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED728', [{'path':'Hcal/DigiTask/OccupancyNR/FED/FED728', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED729', [{'path':'Hcal/DigiTask/OccupancyNR/FED/FED729', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED730', [{'path':'Hcal/DigiTask/OccupancyNR/FED/FED730', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED731', [{'path':'Hcal/DigiTask/OccupancyNR/FED/FED731', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCutData/TP', [{'path':'Hcal/TPTask/OccupancyCutData/OccupancyCutData', 'description':"""Occupancy Distributions for Data with a cut on Et  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Timing/DIGI/Electronics/VME', [{'path':'Hcal/DigiTask/Timing/Electronics/VME', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Timing/DIGI/Electronics/uTCA', [{'path':'Hcal/DigiTask/Timing/Electronics/uTCA', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'ADC/DIGI/SubdetPM/HBM', [{'path':'Hcal/DigiTask/ADC/SubdetPM/HBM', 'description':"""ADC Distributions per 1 TS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'ADC/DIGI/SubdetPM/HBP', [{'path':'Hcal/DigiTask/ADC/SubdetPM/HBP', 'description':"""ADC Distributions per 1 TS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'ADC/DIGI/SubdetPM/HEM', [{'path':'Hcal/DigiTask/ADC/SubdetPM/HEM', 'description':"""ADC Distributions per 1 TS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'ADC/DIGI/SubdetPM/HEP', [{'path':'Hcal/DigiTask/ADC/SubdetPM/HEP', 'description':"""ADC Distributions per 1 TS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'ADC/DIGI/SubdetPM/HFM', [{'path':'Hcal/DigiTask/ADC/SubdetPM/HFM', 'description':"""ADC Distributions per 1 TS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'ADC/DIGI/SubdetPM/HFP', [{'path':'Hcal/DigiTask/ADC/SubdetPM/HFP', 'description':"""ADC Distributions per 1 TS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'ADC/DIGI/SubdetPM/HOM', [{'path':'Hcal/DigiTask/ADC/SubdetPM/HOM', 'description':"""ADC Distributions per 1 TS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'ADC/DIGI/SubdetPM/HOP', [{'path':'Hcal/DigiTask/ADC/SubdetPM/HOP', 'description':"""ADC Distributions per 1 TS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Occupancy/RAW/Electronics/VME', [{'path':'Hcal/RawTask/Occupancy/Electronics/VME', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Occupancy/RAW/Electronics/uTCA', [{'path':'Hcal/RawTask/Occupancy/Electronics/uTCA', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'fC/DIGI/SubdetPM/HBM', [{'path':'Hcal/DigiTask/fC/SubdetPM/HBM', 'description':"""fC per TS distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'fC/DIGI/SubdetPM/HBP', [{'path':'Hcal/DigiTask/fC/SubdetPM/HBP', 'description':"""fC per TS distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'fC/DIGI/SubdetPM/HEM', [{'path':'Hcal/DigiTask/fC/SubdetPM/HEM', 'description':"""fC per TS distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'fC/DIGI/SubdetPM/HEP', [{'path':'Hcal/DigiTask/fC/SubdetPM/HEP', 'description':"""fC per TS distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'fC/DIGI/SubdetPM/HFM', [{'path':'Hcal/DigiTask/fC/SubdetPM/HFM', 'description':"""fC per TS distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'fC/DIGI/SubdetPM/HFP', [{'path':'Hcal/DigiTask/fC/SubdetPM/HFP', 'description':"""fC per TS distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'fC/DIGI/SubdetPM/HOM', [{'path':'Hcal/DigiTask/fC/SubdetPM/HOM', 'description':"""fC per TS distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'fC/DIGI/SubdetPM/HOP', [{'path':'Hcal/DigiTask/fC/SubdetPM/HOP', 'description':"""fC per TS distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'MsnEmul/TP/Electronics/VME', [{'path':'Hcal/TPTask/MsnEmul/Electronics/VME', 'description':"""Distribution of channels missing from Emulator w.r.t. Data  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'MsnEmul/TP/Electronics/uTCA', [{'path':'Hcal/TPTask/MsnEmul/Electronics/uTCA', 'description':"""Distribution of channels missing from Emulator w.r.t. Data  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EvnMsm/RAW/Electronics/VME', [{'path':'Hcal/RawTask/EvnMsm/Electronics/VME', 'description':"""Event Number Mismatches.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EvnMsm/RAW/Electronics/uTCA', [{'path':'Hcal/RawTask/EvnMsm/Electronics/uTCA', 'description':"""Event Number Mismatches.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP', [{'path':'Hcal/TPTask/EtMsm/EtMsm', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FED/FED1100', [{'path':'Hcal/DigiTask/SumQvsLS/FED/FED1100', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FED/FED1102', [{'path':'Hcal/DigiTask/SumQvsLS/FED/FED1102', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FED/FED1104', [{'path':'Hcal/DigiTask/SumQvsLS/FED/FED1104', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FED/FED1106', [{'path':'Hcal/DigiTask/SumQvsLS/FED/FED1106', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FED/FED1108', [{'path':'Hcal/DigiTask/SumQvsLS/FED/FED1108', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FED/FED1110', [{'path':'Hcal/DigiTask/SumQvsLS/FED/FED1110', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FED/FED1112', [{'path':'Hcal/DigiTask/SumQvsLS/FED/FED1112', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FED/FED1114', [{'path':'Hcal/DigiTask/SumQvsLS/FED/FED1114', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FED/FED1116', [{'path':'Hcal/DigiTask/SumQvsLS/FED/FED1116', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FED/FED1118', [{'path':'Hcal/DigiTask/SumQvsLS/FED/FED1118', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FED/FED1120', [{'path':'Hcal/DigiTask/SumQvsLS/FED/FED1120', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FED/FED1122', [{'path':'Hcal/DigiTask/SumQvsLS/FED/FED1122', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FED/FED1132', [{'path':'Hcal/DigiTask/SumQvsLS/FED/FED1132', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FED/FED724', [{'path':'Hcal/DigiTask/SumQvsLS/FED/FED724', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FED/FED725', [{'path':'Hcal/DigiTask/SumQvsLS/FED/FED725', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FED/FED726', [{'path':'Hcal/DigiTask/SumQvsLS/FED/FED726', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FED/FED727', [{'path':'Hcal/DigiTask/SumQvsLS/FED/FED727', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FED/FED728', [{'path':'Hcal/DigiTask/SumQvsLS/FED/FED728', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FED/FED729', [{'path':'Hcal/DigiTask/SumQvsLS/FED/FED729', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FED/FED730', [{'path':'Hcal/DigiTask/SumQvsLS/FED/FED730', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FED/FED731', [{'path':'Hcal/DigiTask/SumQvsLS/FED/FED731', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FED/FED1118', [{'path':'Hcal/DigiTask/Q2Q12vsLS/FED/FED1118', 'description':"""Charge in TS2 over the sum of charges in TS1 and TS2 vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FED/FED1120', [{'path':'Hcal/DigiTask/Q2Q12vsLS/FED/FED1120', 'description':"""Charge in TS2 over the sum of charges in TS1 and TS2 vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FED/FED1122', [{'path':'Hcal/DigiTask/Q2Q12vsLS/FED/FED1122', 'description':"""Charge in TS2 over the sum of charges in TS1 and TS2 vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP/Electronics/VME', [{'path':'Hcal/TPTask/EtMsm/Electronics/VME', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'EtMsm/TP/Electronics/uTCA', [{'path':'Hcal/TPTask/EtMsm/Electronics/uTCA', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, 'OccupancyCutvsLS/DIGI/Subdet/HB', [{'path':'Hcal/DigiTask/OccupancyCutvsLS/Subdet/HB', 'description':"""Occupancy after a cut vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCutvsLS/DIGI/Subdet/HE', [{'path':'Hcal/DigiTask/OccupancyCutvsLS/Subdet/HE', 'description':"""Occupancy after a cut vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCutvsLS/DIGI/Subdet/HF', [{'path':'Hcal/DigiTask/OccupancyCutvsLS/Subdet/HF', 'description':"""Occupancy after a cut vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'OccupancyCutvsLS/DIGI/Subdet/HO', [{'path':'Hcal/DigiTask/OccupancyCutvsLS/Subdet/HO', 'description':"""Occupancy after a cut vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED1100', [{'path':'Hcal/DigiTask/Timing/FED/FED1100', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED1102', [{'path':'Hcal/DigiTask/Timing/FED/FED1102', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED1104', [{'path':'Hcal/DigiTask/Timing/FED/FED1104', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED1106', [{'path':'Hcal/DigiTask/Timing/FED/FED1106', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED1108', [{'path':'Hcal/DigiTask/Timing/FED/FED1108', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED1110', [{'path':'Hcal/DigiTask/Timing/FED/FED1110', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED1112', [{'path':'Hcal/DigiTask/Timing/FED/FED1112', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED1114', [{'path':'Hcal/DigiTask/Timing/FED/FED1114', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED1116', [{'path':'Hcal/DigiTask/Timing/FED/FED1116', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED1118', [{'path':'Hcal/DigiTask/Timing/FED/FED1118', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED1120', [{'path':'Hcal/DigiTask/Timing/FED/FED1120', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED1122', [{'path':'Hcal/DigiTask/Timing/FED/FED1122', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED1132', [{'path':'Hcal/DigiTask/Timing/FED/FED1132', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED724', [{'path':'Hcal/DigiTask/Timing/FED/FED724', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED725', [{'path':'Hcal/DigiTask/Timing/FED/FED725', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED726', [{'path':'Hcal/DigiTask/Timing/FED/FED726', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED727', [{'path':'Hcal/DigiTask/Timing/FED/FED727', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED728', [{'path':'Hcal/DigiTask/Timing/FED/FED728', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED729', [{'path':'Hcal/DigiTask/Timing/FED/FED729', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED730', [{'path':'Hcal/DigiTask/Timing/FED/FED730', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED731', [{'path':'Hcal/DigiTask/Timing/FED/FED731', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, '00 Current Summary', [{'path':'Hcal2/RecHitTask/Summary/Summary', 'description':"""Summary. Anything that is not either WHITE or GREEN is BAD.<br>Color Scheme:<br><font color='green'>GOOD</font> for GOOD<br><font color='yellow'>PROBLEMATIC</font> for Problematic<br><font color='red'>BAD</font> for BAD<br><font color='black'>BAD</font> for BAD<br>WHITE color stands for INAPPLICABLE flag<br>Flags(Y) vs FED(X). For details...   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Summary_Generation_Description">Details...</a>"""}, {'path':'Hcal/DigiTask/Summary/Summary', 'description':"""Summary. Anything that is not either WHITE or GREEN is BAD.<br>Color Scheme:<br><font color='green'>GOOD</font> for GOOD<br><font color='yellow'>PROBLEMATIC</font> for Problematic<br><font color='red'>BAD</font> for BAD<br><font color='black'>BAD</font> for BAD<br>WHITE color stands for INAPPLICABLE flag<br>Flags(Y) vs FED(X). For details...   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Summary_Generation_Description">Details...</a>"""}], [{'path':'Hcal/RawTask/Summary/Summary', 'description':"""Summary. Anything that is not either WHITE or GREEN is BAD.<br>Color Scheme:<br><font color='green'>GOOD</font> for GOOD<br><font color='yellow'>PROBLEMATIC</font> for Problematic<br><font color='red'>BAD</font> for BAD<br><font color='black'>BAD</font> for BAD<br>WHITE color stands for INAPPLICABLE flag<br>Flags(Y) vs FED(X). For details...   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Summary_Generation_Description">Details...</a>"""}, {'path':'Hcal/TPTask/Summary/Summary', 'description':"""Summary. Anything that is not either WHITE or GREEN is BAD.<br>Color Scheme:<br><font color='green'>GOOD</font> for GOOD<br><font color='yellow'>PROBLEMATIC</font> for Problematic<br><font color='red'>BAD</font> for BAD<br><font color='black'>BAD</font> for BAD<br>WHITE color stands for INAPPLICABLE flag<br>Flags(Y) vs FED(X). For details...   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Summary_Generation_Description">Details...</a>"""}])

hcallayout(dqmitems, '01 RAW Bad Quality', [{'path':'Hcal/RawTask/BadQualityvsBX/BadQualityvsBX', 'description':"""BadQuality Channels vs BX.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}, {'path':'Hcal/RawTask/BadQualityvsLS/BadQualityvsLS', 'description':"""BadQuality Channels vs LS  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, '02 RAW Bad Quality depth', [{'path':'Hcal/RawTask/BadQuality/depth/depth1', 'description':"""Bad Quality Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}, {'path':'Hcal/RawTask/BadQuality/depth/depth2', 'description':"""Bad Quality Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}], [{'path':'Hcal/RawTask/BadQuality/depth/depth3', 'description':"""Bad Quality Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}, {'path':'Hcal/RawTask/BadQuality/depth/depth4', 'description':"""Bad Quality Channels.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, '03 RAW Mismatches', [{'path':'Hcal/RawTask/BcnMsm/Electronics/VME', 'description':"""BX Number Mismatches.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}, {'path':'Hcal/RawTask/BcnMsm/Electronics/uTCA', 'description':"""BX Number Mismatches.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}], [{'path':'Hcal/RawTask/EvnMsm/Electronics/VME', 'description':"""Event Number Mismatches.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}, {'path':'Hcal/RawTask/EvnMsm/Electronics/uTCA', 'description':"""Event Number Mismatches.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, '04 DIGI Missing 1LS', [{'path':'Hcal/DigiTask/Missing1LS/FED/FED1100', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/Missing1LS/FED/FED1102', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/Missing1LS/FED/FED1104', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/Missing1LS/FED/FED1106', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/Missing1LS/FED/FED1108', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}], [{'path':'Hcal/DigiTask/Missing1LS/FED/FED1110', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/Missing1LS/FED/FED1112', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/Missing1LS/FED/FED1114', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/Missing1LS/FED/FED1116', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/Missing1LS/FED/FED1118', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}], [{'path':'Hcal/DigiTask/Missing1LS/FED/FED1120', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/Missing1LS/FED/FED1122', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/Missing1LS/FED/FED1132', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/Missing1LS/FED/FED724', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/Missing1LS/FED/FED725', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}], [{'path':'Hcal/DigiTask/Missing1LS/FED/FED726', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/Missing1LS/FED/FED727', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/Missing1LS/FED/FED728', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/Missing1LS/FED/FED729', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/Missing1LS/FED/FED730', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}], [{'path':'Hcal/DigiTask/Missing1LS/FED/FED731', 'description':"""Channels missing per 1LS. Reset every 10LSs.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, '05 DIGI Occupancy', [{'path':'Hcal/DigiTask/Occupancy/depth/depth1', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/Occupancy/depth/depth2', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}], [{'path':'Hcal/DigiTask/Occupancy/depth/depth3', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/Occupancy/depth/depth4', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, '06 DIGI Occupancy Total', [{'path':'Hcal/DigiTask/OccupancyNR/FED/FED1100', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/OccupancyNR/FED/FED1102', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/OccupancyNR/FED/FED1104', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/OccupancyNR/FED/FED1106', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/OccupancyNR/FED/FED1108', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}], [{'path':'Hcal/DigiTask/OccupancyNR/FED/FED1110', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/OccupancyNR/FED/FED1112', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/OccupancyNR/FED/FED1114', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/OccupancyNR/FED/FED1116', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/OccupancyNR/FED/FED1118', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}], [{'path':'Hcal/DigiTask/OccupancyNR/FED/FED1120', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/OccupancyNR/FED/FED1122', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/OccupancyNR/FED/FED1132', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/OccupancyNR/FED/FED724', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/OccupancyNR/FED/FED725', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}], [{'path':'Hcal/DigiTask/OccupancyNR/FED/FED726', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/OccupancyNR/FED/FED727', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/OccupancyNR/FED/FED728', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/OccupancyNR/FED/FED729', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/OccupancyNR/FED/FED730', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}], [{'path':'Hcal/DigiTask/OccupancyNR/FED/FED731', 'description':"""Occupnacy Total without Reset.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, '07 DIGI Occupancy Cut', [{'path':'Hcal/DigiTask/OccupancyCut/depth/depth1', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/OccupancyCut/depth/depth2', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}], [{'path':'Hcal/DigiTask/OccupancyCut/depth/depth3', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/OccupancyCut/depth/depth4', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, '08 DIGI Timing', [{'path':'Hcal/DigiTask/Timing/FED/FED1100', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/Timing/FED/FED1102', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/Timing/FED/FED1104', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/Timing/FED/FED1106', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/Timing/FED/FED1108', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}], [{'path':'Hcal/DigiTask/Timing/FED/FED1110', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/Timing/FED/FED1112', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/Timing/FED/FED1114', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/Timing/FED/FED1116', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/Timing/FED/FED1118', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}], [{'path':'Hcal/DigiTask/Timing/FED/FED1120', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/Timing/FED/FED1122', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/Timing/FED/FED1132', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/Timing/FED/FED724', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/Timing/FED/FED725', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}], [{'path':'Hcal/DigiTask/Timing/FED/FED726', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/Timing/FED/FED727', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/Timing/FED/FED728', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/Timing/FED/FED729', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/DigiTask/Timing/FED/FED730', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}], [{'path':'Hcal/DigiTask/Timing/FED/FED731', 'description':"""Timing either @RECO or @DIGI level. Timing is always computed after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, '09 DIGI Total Charge', [{'path':'Hcal/DigiTask/SumQ/SubdetPM/HBM', 'description':"""Total Charge per channel per event.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}, {'path':'Hcal/DigiTask/SumQ/SubdetPM/HBP', 'description':"""Total Charge per channel per event.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}, {'path':'Hcal/DigiTask/SumQ/SubdetPM/HEM', 'description':"""Total Charge per channel per event.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}], [{'path':'Hcal/DigiTask/SumQ/SubdetPM/HEP', 'description':"""Total Charge per channel per event.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}, {'path':'Hcal/DigiTask/SumQ/SubdetPM/HFM', 'description':"""Total Charge per channel per event.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}, {'path':'Hcal/DigiTask/SumQ/SubdetPM/HFP', 'description':"""Total Charge per channel per event.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}], [{'path':'Hcal/DigiTask/SumQ/SubdetPM/HOM', 'description':"""Total Charge per channel per event.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}, {'path':'Hcal/DigiTask/SumQ/SubdetPM/HOP', 'description':"""Total Charge per channel per event.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, '10 DIGI Occupancy vs LS', [{'path':'Hcal/DigiTask/OccupancyvsLS/Subdet/HB', 'description':"""Occupancy vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Pedestal_Task_Description">Details...</a>"""}, {'path':'Hcal/DigiTask/OccupancyvsLS/Subdet/HE', 'description':"""Occupancy vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Pedestal_Task_Description">Details...</a>"""}], [{'path':'Hcal/DigiTask/OccupancyvsLS/Subdet/HF', 'description':"""Occupancy vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Pedestal_Task_Description">Details...</a>"""}, {'path':'Hcal/DigiTask/OccupancyvsLS/Subdet/HO', 'description':"""Occupancy vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Pedestal_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, '11 DIGI Amplitude vs LS', [{'path':'Hcal/DigiTask/SumQvsLS/FED/FED1100', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}, {'path':'Hcal/DigiTask/SumQvsLS/FED/FED1102', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}, {'path':'Hcal/DigiTask/SumQvsLS/FED/FED1104', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}, {'path':'Hcal/DigiTask/SumQvsLS/FED/FED1106', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}, {'path':'Hcal/DigiTask/SumQvsLS/FED/FED1108', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}], [{'path':'Hcal/DigiTask/SumQvsLS/FED/FED1110', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}, {'path':'Hcal/DigiTask/SumQvsLS/FED/FED1112', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}, {'path':'Hcal/DigiTask/SumQvsLS/FED/FED1114', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}, {'path':'Hcal/DigiTask/SumQvsLS/FED/FED1116', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}, {'path':'Hcal/DigiTask/SumQvsLS/FED/FED1118', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}], [{'path':'Hcal/DigiTask/SumQvsLS/FED/FED1120', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}, {'path':'Hcal/DigiTask/SumQvsLS/FED/FED1122', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}, {'path':'Hcal/DigiTask/SumQvsLS/FED/FED1132', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}, {'path':'Hcal/DigiTask/SumQvsLS/FED/FED724', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}, {'path':'Hcal/DigiTask/SumQvsLS/FED/FED725', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}], [{'path':'Hcal/DigiTask/SumQvsLS/FED/FED726', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}, {'path':'Hcal/DigiTask/SumQvsLS/FED/FED727', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}, {'path':'Hcal/DigiTask/SumQvsLS/FED/FED728', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}, {'path':'Hcal/DigiTask/SumQvsLS/FED/FED729', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}, {'path':'Hcal/DigiTask/SumQvsLS/FED/FED730', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}], [{'path':'Hcal/DigiTask/SumQvsLS/FED/FED731', 'description':"""Total charge per channel per event vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, '12 RECO Energy', [{'path':'Hcal2/RecHitTask/Energy/Subdet/HB', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}, {'path':'Hcal2/RecHitTask/Energy/Subdet/HE', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}, {'path':'Hcal2/RecHitTask/Energy/Subdet/HF', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}], [{'path':'Hcal2/RecHitTask/Energy/Subdet/HO', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}, {'path':'Hcal2/RecHitTask/Energy/depth/depth1', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}, {'path':'Hcal2/RecHitTask/Energy/depth/depth2', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}], [{'path':'Hcal2/RecHitTask/Energy/depth/depth3', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}, {'path':'Hcal2/RecHitTask/Energy/depth/depth4', 'description':"""Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, '13 RECO Occupancy', [{'path':'Hcal2/RecHitTask/Occupancy/depth/depth1', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal2/RecHitTask/Occupancy/depth/depth2', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}], [{'path':'Hcal2/RecHitTask/Occupancy/depth/depth3', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal2/RecHitTask/Occupancy/depth/depth4', 'description':"""Occupancy.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, '14 RECO Occupancy Cut', [{'path':'Hcal2/RecHitTask/OccupancyCut/depth/depth1', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal2/RecHitTask/OccupancyCut/depth/depth2', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}], [{'path':'Hcal2/RecHitTask/OccupancyCut/depth/depth3', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal2/RecHitTask/OccupancyCut/depth/depth4', 'description':"""Occupancy after a cut.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, '15 RECO Timing', [{'path':'Hcal2/RecHitTask/TimingCut/depth/depth1', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal2/RecHitTask/TimingCut/depth/depth2', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}], [{'path':'Hcal2/RecHitTask/TimingCut/depth/depth3', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal2/RecHitTask/TimingCut/depth/depth4', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, '16 RECO HBHEabc Timing', [{'path':'Hcal2/RecHitTask/TimingCut/HBHEPartition/HBHEa', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal2/RecHitTask/TimingCut/HBHEPartition/HBHEb', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}], [{'path':'Hcal2/RecHitTask/TimingCut/HBHEPartition/HBHEc', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

hcallayout(dqmitems, '17 RECO Timing vs Energy', [{'path':'Hcal2/RecHitTask/TimingvsEnergy/SubdetPM/HBM', 'description':"""Timing vs Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}, {'path':'Hcal2/RecHitTask/TimingvsEnergy/SubdetPM/HBP', 'description':"""Timing vs Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}, {'path':'Hcal2/RecHitTask/TimingvsEnergy/SubdetPM/HEM', 'description':"""Timing vs Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}], [{'path':'Hcal2/RecHitTask/TimingvsEnergy/SubdetPM/HEP', 'description':"""Timing vs Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}, {'path':'Hcal2/RecHitTask/TimingvsEnergy/SubdetPM/HFM', 'description':"""Timing vs Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}, {'path':'Hcal2/RecHitTask/TimingvsEnergy/SubdetPM/HFP', 'description':"""Timing vs Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}], [{'path':'Hcal2/RecHitTask/TimingvsEnergy/SubdetPM/HOM', 'description':"""Timing vs Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}, {'path':'Hcal2/RecHitTask/TimingvsEnergy/SubdetPM/HOP', 'description':"""Timing vs Energy Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, '18 TP Et Correlation', [{'path':'Hcal/TPTask/EtCorr/TTSubdet/HBHE', 'description':"""Et Correlation Distributions. Emulator(Y) vs Data(X). Channels not present in respective Collections are plotted as Et=-2.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal/TPTask/EtCorr/TTSubdet/HF', 'description':"""Et Correlation Distributions. Emulator(Y) vs Data(X). Channels not present in respective Collections are plotted as Et=-2.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, '19 TP Et Correlation Ratio', [{'path':'Hcal/TPTask/EtCorrRatio/EtCorrRatio', 'description':"""Et Correlation Ratio. It is always min(etd, ete)/max(etd, ete).   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal/TPTask/EtCorrRatio/Electronics/VME', 'description':"""Et Correlation Ratio. It is always min(etd, ete)/max(etd, ete).   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}], [{'path':'Hcal/TPTask/EtCorrRatio/Electronics/uTCA', 'description':"""Et Correlation Ratio. It is always min(etd, ete)/max(etd, ete).   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, '20 TP Et Distribution', [{'path':'Hcal/TPTask/EtData/Electronics/VME', 'description':"""Et Data Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal/TPTask/EtData/Electronics/uTCA', 'description':"""Et Data Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal/TPTask/EtData/EtData', 'description':"""Et Data Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal/TPTask/EtData/TTSubdet/HBHE', 'description':"""Et Data Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}], [{'path':'Hcal/TPTask/EtData/TTSubdet/HF', 'description':"""Et Data Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal/TPTask/EtEmul/TTSubdet/HBHE', 'description':"""Et Emulator Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal/TPTask/EtEmul/TTSubdet/HF', 'description':"""Et Emulator Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal/TPTask/EtEmul/EtEmul', 'description':"""Et Emulator Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}], [{'path':'Hcal/TPTask/EtEmul/Electronics/VME', 'description':"""Et Emulator Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal/TPTask/EtEmul/Electronics/uTCA', 'description':"""Et Emulator Distributions.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, '21 TP Et Mismatches', [{'path':'Hcal/TPTask/EtMsm/EtMsm', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal/TPTask/EtMsm/Electronics/VME', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}], [{'path':'Hcal/TPTask/EtMsm/Electronics/uTCA', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, '22 TP Et Missing', [{'path':'Hcal/TPTask/MsnData/Electronics/VME', 'description':"""Distribution of channels missing from Data w.r.t. Emulator  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal/TPTask/MsnData/Electronics/uTCA', 'description':"""Distribution of channels missing from Data w.r.t. Emulator  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal/TPTask/MsnData/MsnData', 'description':"""Distribution of channels missing from Data w.r.t. Emulator  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}], [{'path':'Hcal/TPTask/MsnEmul/MsnEmul', 'description':"""Distribution of channels missing from Emulator w.r.t. Data  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal/TPTask/MsnEmul/Electronics/VME', 'description':"""Distribution of channels missing from Emulator w.r.t. Data  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal/TPTask/MsnEmul/Electronics/uTCA', 'description':"""Distribution of channels missing from Emulator w.r.t. Data  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, '23 TP Et Occupancy', [{'path':'Hcal/TPTask/OccupancyData/OccupancyData', 'description':"""Occupancy Distributions for Data  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal/TPTask/OccupancyData/Electronics/VME', 'description':"""Occupancy Distributions for Data  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal/TPTask/OccupancyData/Electronics/uTCA', 'description':"""Occupancy Distributions for Data  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}], [{'path':'Hcal/TPTask/OccupancyEmul/Electronics/VME', 'description':"""Occupancy Distributions for Emulator  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal/TPTask/OccupancyEmul/Electronics/uTCA', 'description':"""Occupancy Distributions for Emulator  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal/TPTask/OccupancyEmul/OccupancyEmul', 'description':"""Occupancy Distributions for Emulator  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, '24 DIGI VME vs uTCA ADC', [{'path':'Hcal2/DigiComparisonTask/ADC/Subdet/HB', 'description':"""ADC Distributions per 1 TS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}, {'path':'Hcal2/DigiComparisonTask/ADC/Subdet/HE', 'description':"""ADC Distributions per 1 TS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}], [{'path':'Hcal2/DigiComparisonTask/ADC/Subdet/HF', 'description':"""ADC Distributions per 1 TS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}, {'path':'Hcal2/DigiComparisonTask/ADC/Subdet/HO', 'description':"""ADC Distributions per 1 TS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, '25 DIGI VME vs uTCA ADC(uTCA) Missing VME', [{'path':'Hcal2/DigiComparisonTask/ADCMsnVME/Subdet/HB', 'description':"""ADC Distribution for Missing VME Digis  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/DigiComparisonTask/ADCMsnVME/Subdet/HE', 'description':"""ADC Distribution for Missing VME Digis  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}], [{'path':'Hcal2/DigiComparisonTask/ADCMsnVME/Subdet/HF', 'description':"""ADC Distribution for Missing VME Digis  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/DigiComparisonTask/ADCMsnVME/Subdet/HO', 'description':"""ADC Distribution for Missing VME Digis  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, '26 DIGI VME vs uTCA ADC(VME) Missing uTCA', [{'path':'Hcal2/DigiComparisonTask/ADCMsnuTCA/Subdet/HB', 'description':"""ADC Distribution for Missing uTCA Digis  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/DigiComparisonTask/ADCMsnuTCA/Subdet/HE', 'description':"""ADC Distribution for Missing uTCA Digis  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}], [{'path':'Hcal2/DigiComparisonTask/ADCMsnuTCA/Subdet/HF', 'description':"""ADC Distribution for Missing uTCA Digis  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/DigiComparisonTask/ADCMsnuTCA/Subdet/HO', 'description':"""ADC Distribution for Missing uTCA Digis  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, '27 DIGI VME vs uTCA Mismatched', [{'path':'Hcal2/DigiComparisonTask/Mismatched/depth/depth1', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/DigiComparisonTask/Mismatched/depth/depth2', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}], [{'path':'Hcal2/DigiComparisonTask/Mismatched/depth/depth3', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/DigiComparisonTask/Mismatched/depth/depth4', 'description':"""Digis for which ADCs are mismatched  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, '28 DIGI VME vs uTCA Missing', [{'path':'Hcal2/DigiComparisonTask/Missing_VME/depth/depth1', 'description':"""Digis missing from VME collection and present in uTCA  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/DigiComparisonTask/Missing_VME/depth/depth2', 'description':"""Digis missing from VME collection and present in uTCA  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/DigiComparisonTask/Missing_VME/depth/depth3', 'description':"""Digis missing from VME collection and present in uTCA  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}], [{'path':'Hcal2/DigiComparisonTask/Missing_VME/depth/depth4', 'description':"""Digis missing from VME collection and present in uTCA  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/DigiComparisonTask/Missing_uTCA/depth/depth1', 'description':"""Digis missing from uTCA collection and present in VME  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/DigiComparisonTask/Missing_uTCA/depth/depth2', 'description':"""Digis missing from uTCA collection and present in VME  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}], [{'path':'Hcal2/DigiComparisonTask/Missing_uTCA/depth/depth3', 'description':"""Digis missing from uTCA collection and present in VME  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/DigiComparisonTask/Missing_uTCA/depth/depth4', 'description':"""Digis missing from uTCA collection and present in VME  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])

hcallayout(dqmitems, '29 TP VME vs uTCA Et', [{'path':'Hcal2/TPComparisonTask/Et/TTSubdet/HBHE', 'description':"""Et Correlation over all TS. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Trigger_Primitives_Comparison_Ta">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/Et/TTSubdet/HF', 'description':"""Et Correlation over all TS. VME(Y) vs uTCA(X)  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Trigger_Primitives_Comparison_Ta">Details...</a>"""}])

hcallayout(dqmitems, '30 TP VME vs uTCA Et Mismatched', [{'path':'Hcal2/TPComparisonTask/EtMsm/EtMsm', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED1100', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED1102', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED1104', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED1106', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED1108', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED1110', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}], [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED1112', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED1114', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED1116', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED1118', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED1120', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED1122', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED1132', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}], [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED700', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED701', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED702', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED703', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED704', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED705', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED706', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}], [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED707', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED708', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED709', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED710', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED711', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED712', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED713', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}], [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED714', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED715', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED716', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED717', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED724', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED725', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED726', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}], [{'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED727', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED728', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED729', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED730', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/EtMsm/FED/FED731', 'description':"""Distribution of channels with mismatched Et   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, '31 TP VME vs uTCA FG Mismatched', [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED1100', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED1102', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED1104', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED1106', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED1108', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED1110', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED1112', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}], [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED1114', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED1116', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED1118', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED1120', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED1122', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED1132', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED700', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}], [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED701', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED702', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED703', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED704', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED705', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED706', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED707', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}], [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED708', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED709', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED710', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED711', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED712', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED713', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED714', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}], [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED715', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED716', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED717', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED724', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED725', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED726', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED727', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}], [{'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED728', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED729', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED730', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/FGMsm/FED/FED731', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/FGMsm/FGMsm', 'description':"""Distribution of channels with mismatched Fine Grain Bit  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])

hcallayout(dqmitems, '32 TP VME vs uTCA Missing', [{'path':'Hcal2/TPComparisonTask/Missing/Missing_VME', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/Missing/Missing_uTCA', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/Missing/FED/FED1100', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/Missing/FED/FED1102', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/Missing/FED/FED1104', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/Missing/FED/FED1106', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/Missing/FED/FED1108', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}], [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED1110', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/Missing/FED/FED1112', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/Missing/FED/FED1114', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/Missing/FED/FED1116', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/Missing/FED/FED1118', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/Missing/FED/FED1120', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/Missing/FED/FED1122', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}], [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED1132', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/Missing/FED/FED700', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/Missing/FED/FED701', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/Missing/FED/FED702', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/Missing/FED/FED703', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/Missing/FED/FED704', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/Missing/FED/FED705', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}], [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED706', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/Missing/FED/FED707', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/Missing/FED/FED708', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/Missing/FED/FED709', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/Missing/FED/FED710', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/Missing/FED/FED711', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/Missing/FED/FED712', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}], [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED713', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/Missing/FED/FED714', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/Missing/FED/FED715', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/Missing/FED/FED716', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/Missing/FED/FED717', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/Missing/FED/FED724', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/Missing/FED/FED725', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}], [{'path':'Hcal2/TPComparisonTask/Missing/FED/FED726', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/Missing/FED/FED727', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/Missing/FED/FED728', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/Missing/FED/FED729', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/Missing/FED/FED730', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}, {'path':'Hcal2/TPComparisonTask/Missing/FED/FED731', 'description':"""Missing Digis. Present in 1 collection and missing from the other.  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Comparison_Task_VME_vs_uTCA">Details...</a>"""}])
