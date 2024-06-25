if __name__=="__main__":
	class DQMItem:
		def __init__(self,layout):
			print(layout)
	dqmitems={}

def shifthcallayout(i, p, *rows): i['00 Shift/Hcal/' + p] = DQMItem(layout=rows)


shifthcallayout(dqmitems, '00 Current Summary', [{'path':'Hcal/TPTask/Summary/Summary', 'description':"""Summary. Anything that is not either WHITE or GREEN is BAD.<br>Color Scheme:<br><font color='green'>GOOD</font> for GOOD<br><font color='yellow'>PROBLEMATIC</font> for Problematic<br><font color='red'>BAD</font> for BAD<br><font color='black'>BAD</font> for BAD<br>WHITE color stands for INAPPLICABLE flag<br>Flags(Y) vs FED(X). For details...   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Summary_Generation_Description">Details...</a>"""}, {'path':'Hcal/RawTask/Summary/Summary', 'description':"""Summary. Anything that is not either WHITE or GREEN is BAD.<br>Color Scheme:<br><font color='green'>GOOD</font> for GOOD<br><font color='yellow'>PROBLEMATIC</font> for Problematic<br><font color='red'>BAD</font> for BAD<br><font color='black'>BAD</font> for BAD<br>WHITE color stands for INAPPLICABLE flag<br>Flags(Y) vs FED(X). For details...   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Summary_Generation_Description">Details...</a>"""}], [{'path':'Hcal/RecHitTask/Summary/Summary', 'description':"""Summary. Anything that is not either WHITE or GREEN is BAD.<br>Color Scheme:<br><font color='green'>GOOD</font> for GOOD<br><font color='yellow'>PROBLEMATIC</font> for Problematic<br><font color='red'>BAD</font> for BAD<br><font color='black'>BAD</font> for BAD<br>WHITE color stands for INAPPLICABLE flag<br>Flags(Y) vs FED(X). For details...   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Summary_Generation_Description">Details...</a>"""}, {'path':'Hcal/DigiTask/Summary/Summary', 'description':"""Summary. Anything that is not either WHITE or GREEN is BAD.<br>Color Scheme:<br><font color='green'>GOOD</font> for GOOD<br><font color='yellow'>PROBLEMATIC</font> for Problematic<br><font color='red'>BAD</font> for BAD<br><font color='black'>BAD</font> for BAD<br>WHITE color stands for INAPPLICABLE flag<br>Flags(Y) vs FED(X). For details...   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Summary_Generation_Description">Details...</a>"""}])

shifthcallayout(dqmitems, '01 RAW Bad Quality', [{'path':'Hcal/RawTask/BadQualityvsBX/BadQualityvsBX', 'description':"""BadQuality Channels vs BX.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}, {'path':'Hcal/RawTask/BadQualityvsLS/BadQualityvsLS', 'description':"""BadQuality Channels vs LS  <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description">Details...</a>"""}])

shifthcallayout(dqmitems, '10 DIGI Occupancy vs LS', [{'path':'Hcal/DigiTask/OccupancyvsLS/Subdet/HB', 'description':"""Occupancy vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Pedestal_Task_Description">Details...</a>"""}, {'path':'Hcal/DigiTask/OccupancyvsLS/Subdet/HE', 'description':"""Occupancy vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Pedestal_Task_Description">Details...</a>"""}], [{'path':'Hcal/DigiTask/OccupancyvsLS/Subdet/HF', 'description':"""Occupancy vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Pedestal_Task_Description">Details...</a>"""}, {'path':'Hcal/DigiTask/OccupancyvsLS/Subdet/HO', 'description':"""Occupancy vs LS.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Pedestal_Task_Description">Details...</a>"""}])

shifthcallayout(dqmitems, '16 RECO HBHEabc Timing', [{'path':'Hcal/RecHitTask/TimingCut/HBHEPartition/HBHEa', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}, {'path':'Hcal/RecHitTask/TimingCut/HBHEPartition/HBHEb', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}], [{'path':'Hcal/RecHitTask/TimingCut/HBHEPartition/HBHEc', 'description':"""Timing either @RECO or @DIGI level. A cut is applied in advance.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Digi_Task_Description">Details...</a> or <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#RecHit_Task_Description">Here...</a>"""}])

shifthcallayout(dqmitems, '18 TP Et Correlation', [{'path':'Hcal/TPTask/EtCorr/TTSubdet/HBHE', 'description':"""Et Correlation Distributions. Emulator(Y) vs Data(X). Channels not present in respective Collections are plotted as Et=-2.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}, {'path':'Hcal/TPTask/EtCorr/TTSubdet/HF', 'description':"""Et Correlation Distributions. Emulator(Y) vs Data(X). Channels not present in respective Collections are plotted as Et=-2.   <a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#TP_Task_Description">Details...</a>"""}])
