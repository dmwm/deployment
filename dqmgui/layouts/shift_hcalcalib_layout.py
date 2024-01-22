if __name__=="__main__":
	class DQMItem:
		def __init__(self,layout):
			print(layout)
	dqmitems={}

def shifthcalcaliblayout(i, p, *rows): i['00 Shift/HcalCalib/' + p] = DQMItem(layout=rows)


shifthcalcaliblayout(dqmitems, '00 Run Summary', [{'path':'HcalCalib/PedestalTask/SummaryvsLS/SummaryvsLS', 'description':"""Calibration Summary. Anything that is not either WHITE or GREEN or Gray is BAD.<br> Color Scheme:<br><font color='green'>GOOD</font> for GOOD<br><font color='yellow'>PROBLEMATIC</font> for Problematic<br><font color='red'>BAD</font> for BAD<br><font color='black'>RESERVED</font> Not used at the moment <br><font color='gray'>NCDAQ with Gray Font</font> FED is excluded from cDAQ<br>WHITE color stands for INAPPLICABLE flag<br>FED(Y) vs LS(X). All the Monitoring Tasks are summarized. For details...  <a href='https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Pedestal_Task_Description'>Details...</a>"""}, {'path':'HcalCalib/RawTask/SummaryvsLS/SummaryvsLS', 'description':"""RAW Summary Summary. Anything that is not either WHITE or GREEN or Gray is BAD.<br> Color Scheme:<br><font color='green'>GOOD</font> for GOOD<br><font color='yellow'>PROBLEMATIC</font> for Problematic<br><font color='red'>BAD</font> for BAD<br><font color='black'>RESERVED</font> Not used at the moment <br><font color='gray'>NCDAQ with Gray Font</font> FED is excluded from cDAQ<br>WHITE color stands for INAPPLICABLE flag<br>FED(Y) vs LS(X). All the Monitoring Tasks are summarized. For details...  <a href='https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription#Raw_Task_Description'>Details...</a>"""}])

