def errorlayout(i, p, *rows): i["00 Shift/Errors/" + p] = DQMItem(layout=rows)

errorlayout(dqmitems, "00 - HBHEHF Warning Plots",
 [{ 'path': "Hcal/DeadCellMonitor_Hcal/TotalDeadCells_HBHEHF_vs_LS",
    'description': "This plot represents the number of HCAL dead Cells in HB,HE,HF as a function of the LumiSection. The shift leader must be immediately informed if this number is greater than 50.", 'draw': { 'withref': "no" }}])
errorlayout(dqmitems, "01 - HO Warning Plots",
 [{ 'path': "Hcal/DeadCellMonitor_Hcal/TotalDeadCells_HO_vs_LS",
    'description': "This plot represents the number of HO dead Cells as a function of the LumiSection.",'draw':{'withref':"no"}}])
errorlayout(dqmitems, "02 - SiStrip FED errors",
 [{ 'path': "SiStrip/ReadoutView/FedMonitoringSummary/FEDLevel/nFEDErrors",
    'description': "# of FEDs in error per event - Call Tracker DOC 165503 if the mean value is above 10 - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftSiStrip>DQMShiftOnlineSiStrip</a>",'draw':{'withref':"no"}}])
errorlayout(dqmitems, "03 - HBHEHF Dead Cells in last N LS",
 [{ 'path': "Hcal/DeadCellMonitor_Hcal/ProblemsInLastNLB_HBHEHF_alarm",
    'description': "This plot shows the total number of HCAL dead Cells in HB,HE,HF in last N LS. The plot is filled if there are more than 50 DeadCells present for more than 4 consequtive LumiSections. The shift leader must be immediately informed if this number is greater than 50.", 'draw': { 'withref': "no" }}])
