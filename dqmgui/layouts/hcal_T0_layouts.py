# Dummy check of python syntax within file when run stand-alone
if __name__=="__main__":
    class DQMItem:
        def __init__(self,layout):
            print layout

    dqmitems={}



def hcallayout(i, p, *rows): i["Hcal/Layouts/" + p] = DQMItem(layout=rows)

hcallayout(dqmitems, "01 HCAL Summaries",
           [{ 'path':"Hcal/EventInfo/reportSummaryMap",
             'description':"This shows the fraction of bad cells in each subdetector.  All subdetectors should appear green"}]
           )

hcallayout(dqmitems, "02 HCAL Events Processed",
          [{ 'path': "Hcal/HcalInfo/EventsInHcalMonitorModule",
             'description': "This histogram counts the total events seen by this process." }]
           )

hcallayout(dqmitems, "03 HCAL Sufficient Events",
          [{ 'path': "Hcal/HcalInfo/SummaryClientPlots/EnoughEvents",
             'description': "This histogram indicates whether the individual tasks have produced enough events to make a proper evaluation of reportSummary values.  All individual tasks should have 'true' values (1).  HcalMonitorModule may be either 1 or 0. " }]
           )

hcallayout(dqmitems, "04 HCAL Raw Data",
           [{ 'path': "Hcal/RawDataMonitor_Hcal/ ProblemRawData",
              'description': "A Raw Data Format error indicates that the data received from this channel was somehow corrupted or compromised.  This plot is the sum of bad digis over all depths. iPhi (1 to 72) by iEta (-41 to 41) More at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }]
           )

hcallayout(dqmitems, "05 HCAL Digi Problems",
          [{ 'path': "Hcal/DigiMonitor_Hcal/ ProblemDigis",
             'description': "A digi cell is considered bad if the capid rotation for that digi was incorrect, if the digi's data valid/error flags are incorrect, or if there is an IDLE-BCN mismatch.  Currently, only digis with IDLE-BCN mismatches are displayed.  This plot is the sum of bad digis over all depths. iPhi (1 to 72) by iEta (-41 to 41) More at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }],
           [{ 'path': "Hcal/DigiMonitor_Hcal/bad_digis/1D_digi_plots/BadDigisVsLB",
              'description': "Total number of bad digis found in HCAL vs luminosity section"}],
           )

hcallayout(dqmitems, "06 HCAL Dead Cell Check",
          [{ 'path': "Hcal/DeadCellMonitor_Hcal/ ProblemDeadCells",
             'description': "Potential dead cell candidates in all depths. Seriously dead if dead for >5% of a full run. iPhi (1 to 72) by iEta (-41 to 41) More at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }],
           [{ 'path': "Hcal/DeadCellMonitor_Hcal/TotalDeadCells_HCAL_vs_LS",
             'description': "Total number of dead cells found in HCAL vs luminosity section"}],
           )

hcallayout(dqmitems, "07 HCAL Hot Cell Check",
          [{ 'path': "Hcal/HotCellMonitor_Hcal/ ProblemHotCells",
             'description': "A cell is considered potentially hot if it is above some threshold energy, or if it is persistently below some (lower) threshold enery for a number of consecutive events. Seriously hot if hot for >5% of a full run. All depths. iPhi (1 to 72) by iEta (-41 to 41) More at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }],
           [{ 'path': "Hcal/HotCellMonitor_Hcal/TotalHotCells_HCAL_vs_LS",
              'description': "Total number of hot cells found in HCAL vs luminosity section"}],
           )

hcallayout(dqmitems, "08 HCAL HF Luminosity Check",
           [{ 'path':"Hcal/BeamMonitor_Hcal/ Problem BeamMonitor",
              'description':  "This makes specific hot and dead cell checks to the HF channels used in the luminosity measurement.  If too many channels are found to be outside a given energy range in a luminosity section, those channels are counted as bad for that section."}],
           )
