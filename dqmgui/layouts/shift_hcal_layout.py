# Dummy check of python syntax within file when run stand-alone
if __name__=="__main__":
    class DQMItem:
        def __init__(self,layout):
            print layout

    dqmitems={}

def shifthcallayout(i, p, *rows): i["00 Shift/Hcal/" + p] = DQMItem(layout=rows)

# Report Summary Map
shifthcallayout(dqmitems, "01 Hcal Report Summary",
                [{'path':"Hcal/EventInfo/reportSummaryMapShift",
                  'description':  "Shows average fraction of good cells per event in each Hcal subdetector (HB/HE/HO/HF/HO0/HO12/HFLumi).  Values should be greater than 0.98 for HB, HE, and HF.  There are known dead cells in HO, so the HO/HO0/HO12 values will usually be lower than those of the other subdetectors.  The HO0 value should still be > 0.95.  The summary map is fed by the results from the other plots on this page, so when a value is less than expected, you can use the other tests to determine the type of failure."}]
                )

shifthcallayout(dqmitems, "02 HCAL Raw Data",
                [{ 'path': "Hcal/RawDataMonitor_Hcal/problem_rawdata/HB HE HF Depth 1  Problem Raw Data Rate",
                   'description': "A Raw Data error indicates that the data received from this channel was somehow corrupted or compromised.  This plot is the sum of bad channels over all 4 depths in HCAL. The histogram is binned in coordinates of iPhi (1 to 72) by iEta (-41 to 41). More at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" },
                 { 'path': "Hcal/RawDataMonitor_Hcal/problem_rawdata/HB HE HF Depth 2  Problem Raw Data Rate",
                   'description': "A Raw Data error indicates that the data received from this channel was somehow corrupted or compromised.  This plot is the sum of bad channels over all 4 depths in HCAL. The histogram is binned in coordinates of iPhi (1 to 72) by iEta (-41 to 41). More at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }],
                [{ 'path': "Hcal/RawDataMonitor_Hcal/problem_rawdata/HE Depth 3  Problem Raw Data Rate",
                   'description': "A Raw Data error indicates that the data received from this channel was somehow corrupted or compromised.  This plot is the sum of bad channels over all 4 depths in HCAL. The histogram is binned in coordinates of iPhi (1 to 72) by iEta (-41 to 41). More at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" },
                 { 'path': "Hcal/RawDataMonitor_Hcal/problem_rawdata/HO Depth 4  Problem Raw Data Rate",
                   'description': "A Raw Data error indicates that the data received from this channel was somehow corrupted or compromised.  This plot is the sum of bad channels over all 4 depths in HCAL. The histogram is binned in coordinates of iPhi (1 to 72) by iEta (-41 to 41). More at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }]
                )

shifthcallayout(dqmitems, "03 HCAL Digi Problems",
                [{ 'path': "Hcal/DigiMonitor_Hcal/problem_digis/HB HE HF Depth 1  Problem Digi Rate",
                   'description': "This plot shows the results of checks on the HCAL digis  ('digis' are digitized signals produced from the raw data.)  A digi is considered bad if the capid rotation for that digi was incorrect, if the digi's data valid/error flags are incorrect, or if there is an IDLE-BCN mismatch.  This plot is the sum of bad digis over all depths. Known bad cells appear in black, while new problems appear in yellow, orange, or red.  (Entries in green can still be considered okay, but should be tracked in case they move into the yellow or orange range.)  The histogram is binned in coordinates of iPhi (1 to 72) by iEta (-41 to 41). More at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" },
                 { 'path': "Hcal/DigiMonitor_Hcal/problem_digis/HB HE HF Depth 2  Problem Digi Rate",
                   'description': "This plot shows the results of checks on the HCAL digis  ('digis' are digitized signals produced from the raw data.)  A digi is considered bad if the capid rotation for that digi was incorrect, if the digi's data valid/error flags are incorrect, or if there is an IDLE-BCN mismatch.  This plot is the sum of bad digis over all depths. Known bad cells appear in black, while new problems appear in yellow, orange, or red.  (Entries in green can still be considered okay, but should be tracked in case they move into the yellow or orange range.)  The histogram is binned in coordinates of iPhi (1 to 72) by iEta (-41 to 41). More at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }],
                [{ 'path': "Hcal/DigiMonitor_Hcal/problem_digis/HE Depth 3  Problem Digi Rate",
                   'description': "This plot shows the results of checks on the HCAL digis  ('digis' are digitized signals produced from the raw data.)  A digi is considered bad if the capid rotation for that digi was incorrect, if the digi's data valid/error flags are incorrect, or if there is an IDLE-BCN mismatch.  This plot is the sum of bad digis over all depths. Known bad cells appear in black, while new problems appear in yellow, orange, or red.  (Entries in green can still be considered okay, but should be tracked in case they move into the yellow or orange range.)  The histogram is binned in coordinates of iPhi (1 to 72) by iEta (-41 to 41). More at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" },
                 { 'path': "Hcal/DigiMonitor_Hcal/problem_digis/HO Depth 4  Problem Digi Rate",
                   'description': "This plot shows the results of checks on the HCAL digis  ('digis' are digitized signals produced from the raw data.)  A digi is considered bad if the capid rotation for that digi was incorrect, if the digi's data valid/error flags are incorrect, or if there is an IDLE-BCN mismatch.  This plot is the sum of bad digis over all depths. Known bad cells appear in black, while new problems appear in yellow, orange, or red.  (Entries in green can still be considered okay, but should be tracked in case they move into the yellow or orange range.)  The histogram is binned in coordinates of iPhi (1 to 72) by iEta (-41 to 41). More at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }],
                [{ 'path': "Hcal/DigiMonitor_Hcal/bad_digis/1D_digi_plots/HBHEHF Bad Quality Digis vs LB",
                   'description': "Total number of bad digis found in HBHEHF vs luminosity section.  This keeps a running tally of the number of bad digis versus luminosity section.  Sudden jumps in the number of bad digis may indicate that a new problem has appeared during a run."},
                 { 'path': "Hcal/DigiMonitor_Hcal/bad_digis/1D_digi_plots/HO Bad Quality Digis vs LB",
                   'description': "Total number of bad digis found in HO vs luminosity section.  This keeps a running tally of the number of bad digis versus luminosity section.  Sudden jumps in the number of bad digis may indicate that a new problem has appeared during a run."}],
                )

shifthcallayout(dqmitems, "04 HCAL Dead Cell Check",
                [{ 'path': "Hcal/DeadCellMonitor_Hcal/problem_deadcells/HB HE HF Depth 1  Problem Dead Cell Rate",
                   'description': "Potential dead cell candidates in HB HE HF depth 1. Known problems appear in black, while new dead cells appear in yellow, orange, or red. (Occasional 'green' entries are okay, but should be watched in case they increase into the yellow or orange range.)  Binned in coordinates of iPhi (1 to 72) by iEta (-41 to 41).  More at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" },
                 { 'path': "Hcal/DeadCellMonitor_Hcal/problem_deadcells/HB HE HF Depth 2  Problem Dead Cell Rate",
                   'description': "Potential dead cell candidates in HB HE HF depth 2. Known problems appear in black, while new dead cells appear in yellow, orange, or red. (Occasional 'green' entries are okay, but should be watched in case they increase into the yellow or orange range.)  Binned in coordinates of iPhi (1 to 72) by iEta (-41 to 41).  More at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }],
                [{ 'path': "Hcal/DeadCellMonitor_Hcal/problem_deadcells/HE Depth 3  Problem Dead Cell Rate",
                   'description': "Potential dead cell candidates in HE depth 3. Known problems appear in black, while new dead cells appear in yellow, orange, or red. (Occasional 'green' entries are okay, but should be watched in case they increase into the yellow or orange range.)  Binned in coordinates of iPhi (1 to 72) by iEta (-41 to 41).  More at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" },
                 { 'path': "Hcal/DeadCellMonitor_Hcal/problem_deadcells/HO Depth 4  Problem Dead Cell Rate",
                   'description': "Potential dead cell candidates in HO depth 4. Known problems appear in black, while new dead cells appear in yellow, orange, or red. (Occasional 'green' entries are okay, but should be watched in case they increase into the yellow or orange range.)  Binned in coordinates of iPhi (1 to 72) by iEta (-41 to 41).  More at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }],
                [{ 'path': "Hcal/DeadCellMonitor_Hcal/TotalDeadCells_HBHEHF_vs_LS",
                   'description': "Total number of dead cells found in HBHEHF vs luminosity section.  Sudden jumps in the number of dead cells may indicate a channel dying in the middle of a run"},
                 { 'path': "Hcal/DeadCellMonitor_Hcal/TotalDeadCells_HO_vs_LS",
                   'description': "Total number of dead cells found in HO vs luminosity section.  Sudden jumps in the number of dead cells may indicate a channel dying in the middle of a run"}],
                )

shifthcallayout(dqmitems, "05 HCAL Hot Cell Check",
                [{ 'path': "Hcal/HotCellMonitor_Hcal/problem_hotcells/HB HE HF Depth 1  Problem Hot Cell Rate",
                   'description': "A cell is considered potentially hot if it is above some threshold energy in some fraction of events, or if it is persistently above some (lower) threshold enery for a number of consecutive events. Seriously hot if hot for >5% of a full run. Known problems appear in black, while new problems will appear in red, orange, or yellow.  Occasional green entries are okay.  Histogram is binned in coordinates of iPhi (1 to 72) by iEta (-41 to 41). More at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" },
                 { 'path': "Hcal/HotCellMonitor_Hcal/problem_hotcells/HB HE HF Depth 2  Problem Hot Cell Rate",
                   'description': "A cell is considered potentially hot if it is above some threshold energy in some fraction of events, or if it is persistently above some (lower) threshold enery for a number of consecutive events. Seriously hot if hot for >5% of a full run. Known problems appear in black, while new problems will appear in red, orange, or yellow.  Occasional green entries are okay.  Histogram is binned in coordinates of iPhi (1 to 72) by iEta (-41 to 41). More at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }],
                [{ 'path': "Hcal/HotCellMonitor_Hcal/problem_hotcells/HE Depth 3  Problem Hot Cell Rate",
                   'description': "A cell is considered potentially hot if it is above some threshold energy in some fraction of events, or if it is persistently above some (lower) threshold enery for a number of consecutive events. Seriously hot if hot for >5% of a full run. Known problems appear in black, while new problems will appear in red, orange, or yellow.  Occasional green entries are okay.  Histogram is binned in coordinates of iPhi (1 to 72) by iEta (-41 to 41). More at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" },
                 { 'path': "Hcal/HotCellMonitor_Hcal/problem_hotcells/HO Depth 4  Problem Hot Cell Rate",
                   'description': "A cell is considered potentially hot if it is above some threshold energy in some fraction of events, or if it is persistently above some (lower) threshold enery for a number of consecutive events. Seriously hot if hot for >5% of a full run. Known problems appear in black, while new problems will appear in red, orange, or yellow.  Occasional green entries are okay.  Histogram is binned in coordinates of iPhi (1 to 72) by iEta (-41 to 41). More at <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }],
                [{ 'path': "Hcal/HotCellMonitor_Hcal/TotalHotCells_HBHEHF_vs_LS",
                   'description': "Total number of hot cells found in HBHEHF vs luminosity section.  Sudden jumps in the number of hot cells may indicate a problem that has occurred in the middle of a run."},
                 { 'path': "Hcal/HotCellMonitor_Hcal/TotalHotCells_HO_vs_LS",
                   'description': "Total number of hot cells found in HO vs luminosity section.  Sudden jumps in the number of hot cells may indicate a problem that has occurred in the middle of a run."}],
                )

shifthcallayout(dqmitems, "06 HCAL Trigger Primitives",
                [{ 'path': "Hcal/TrigPrimMonitor_Hcal/ ProblemTriggerPrimitives",
                   'description': "See details at: <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }]
                )

shifthcallayout(dqmitems, "07 HCAL Pedestal Problems",
                [{ 'path':"Hcal/CoarsePedestalMonitor_Hcal/ ProblemCoarsePedestals",
                   'description': "See details at: <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }]
                )

shifthcallayout(dqmitems, "08 HCAL Lumi Problems",
                [{'path': "Hcal/BeamMonitor_Hcal/ Problem BeamMonitor",
                  'description':"This shows problems only in the sections of HF used for luminosity monitoring.  Channels that are hot or dead are considered as problems, where the definitions of 'hot' and 'dead' are slightly different than in the normal HCAL monitors.  More details at  <a href=https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMHistograms>HcalDQMHistograms</a>" }]
                )

shifthcallayout(dqmitems, "09 HCAL RecHit Energies",
                [{'path': "Hcal/RecHitMonitor_Hcal/Distributions_AllRecHits/rechit_1D_plots/HB_energy_1D",
                  'description':"Average energy/hit for each of the 2592 channels in HB"},

                 {'path': "Hcal/RecHitMonitor_Hcal/Distributions_AllRecHits/rechit_1D_plots/HE_energy_1D",
                  'description':"Average energy/hit for each of the 2592 channels in HE"}],
                [{'path': "Hcal/RecHitMonitor_Hcal/Distributions_AllRecHits/rechit_1D_plots/HF_energy_1D",
                  'description':"Average energy/hit for each of the 1728 channels in HF"},
                 {'path': "Hcal/RecHitMonitor_Hcal/Distributions_AllRecHits/rechit_1D_plots/HO_energy_1D",
                  'description':"Average energy/hit for each of the 2160 channels in HO.  (You may see fewer entries than 2160 because of ~30 known dead cells in HO.)"}]
                )


shifthcallayout(dqmitems, "11 HCAL HBHE Timing Shifts on Digi Level",
	[
		{
			"path" : "Hcal/HcalTimingTask/HBHE/HBHE_TS5TS4_iphi1to2_iphi51to72",
			"description" : "Ratio of TS5 to TS4 for HBHEc"
		},
		{
			"path" : "Hcal/HcalTimingTask/HBHE/HBHE_TS5TS4_iphi3to26",
			"description" : "Ratio of TS5 to TS4 for HBHEa"
		},
		{
			"path" : "Hcal/HcalTimingTask/HBHE/HBHE_TS5TS4_iphi27to50",
			"description" : "Ratio of TS5 to TS4 for HBHEb"
		}
	],
	[
		{
			"path" : "Hcal/HcalTimingTask/HBHE/HBHE_TimingDiffs",
			"description" : "Relative difference among the partitions TS5 to TS4 ratio. Shouldn't be greater 13% for the Physics Data Taking"
		},
		{
			"path" : "Hcal/HcalTimingTask/HBHE/HBHE_TS5TS4VSiphi",
			"description" : "Ratio of TS5 to TS4 vs iphi"
		}
	]
)

shifthcallayout(dqmitems, "12 HCAL HBHE Timing Shifts on RecHit Level",
	[
		{
			"path" : "Hcal/HcalRecHitTask/HB/HB_RecHitTimeVSiphi",
			"description" : "HB RecHit Timing vs iphi - Shows potential TCDS related Shifts among partitions"
		},
		{
			"path" : "Hcal/HcalRecHitTask/HE/HE_RecHitTimeVSiphi",
			"description" : "HE RecHit Timing vs iphi - Shows potential TCDS related Shifts among partitions"
		}
	],
	[
		{
			"path" : "Hcal/HcalRecHitTask/HBHE/HBHE_RecHitTime_iphi1to2_iphi51to72",
			"description" : "HBHE RecHit Timing for HBHEc"
		},
		{
			"path" : "Hcal/HcalRecHitTask/HBHE/HBHE_RecHitTime_iphi3to26",
			"description" : "HBHE RecHit Timing for HBHEb"
		},
		{
			"path" : "Hcal/HcalRecHitTask/HBHE/HBHE_RecHitTime_iphi27to50",
			"description" : "HBHE RecHit Timing for HBHEa"
		}
	]
)

shifthcallayout(dqmitems, "13 HCAL Occupancies vs LS",
	[
		{
			"path" : "Hcal/HcalDigiTask/HB/HB_OccupancyVSls_NoZSCut",
			"description" : "HB Digi Occupancy vs LS. HB has ZS. Even with ZS, in case of beam presence, there shouldn't be any real drops observed"
		},
		{
			"path" : "Hcal/HcalDigiTask/HE/HE_OccupancyVSls_NoZSCut",
			"description" : "HE Digi Occupancy vs LS. HE has ZS. Even with ZS, in case of beam presence, there shouldn't be any real drops observed"
		}
	],
	[
		{
			"path" : "Hcal/HcalDigiTask/HF/HF_OccupancyVSls_NoZSCut",
			"description" : "HF Digi Occupancy vs LS. No ZS for HF - 1728 channels should be read out all the time for each event "
		},
		{
			"path" : "Hcal/HcalDigiTask/HO/HO_OccupancyVSls_NoZSCut",
			"description" : "HO Digi Occupancy vs LS. HO has ZS. Even with ZS, in case of beam presence, there shouldn't be any real drops observed"
		}
	]
)

shifthcallayout(dqmitems, "14 HCAL HF Timing",
	[
		{
			"path" : "Hcal/HcalTimingTask/HF/HFM_QTS2QTS12vsLS",
			"description" : "HFM Ratio of Q in TS2 over the sum of Qs in TS1 & TS2. For low PU this ratio should be very close to 1, > 0.96; However for high PU running ratio on average should be 0.5"
		},
		{
			"path" : "Hcal/HcalTimingTask/HF/HFP_QTS2QTS12vsLS",
			"description" : "HFM Ratio of Q in TS2 over the sum of Qs in TS1 & TS2. For low PU this ratio should be very close to 1, > 0.96; However for high PU running ratio on average should be 0.5"
		}
	],
	[
		{
			"path" : "Hcal/HcalTimingTask/HF/HFMiphi3ieta41D2_QTS2QTS12",
			"description" : "HFM iphi3 ieta-41 D2 Ratio of Q in TS2 over the sum of Qs in TS1 & TS2. Currently this is one of the 50/50 Channels"
		},
		{
			"path" : "Hcal/HcalTimingTask/HF/HFMiphi3ieta41D2_Timing",
			"description" : "HFM iphi3 ieta-41 D2 Nominal fC weighted Time Average. Currently this is one of the 50/50 Channels"
		}
	],
	[
		{
			"path" : "Hcal/HcalTimingTask/HF/HFPiphi3ieta41D2_QTS2QTS12",
			"description" : "HFP iphi3 ieta41 D2 Ratio of Q in TS2 over the sum of Qs in TS1 & TS2. Currently this is one of the 50/50 Channels"
		},
		{
			"path" : "Hcal/HcalTimingTask/HF/HFPiphi3ieta41D2_Timing",
			"description" : "HFP iphi3 ieta41 D2 Nominal fC weighted Time Average. Currently this is one of the 50/50 Channels"
		}
	]
)

shifthcallayout(dqmitems, "15 HCAL HBHE RecHit Timing",
	[
		{
			"path" : "Hcal/HcalRecHitTask/HB/HB_RecHitTime",
			"description" : "HB RecHit Timing, E>5GeV, "
		},
		{
			"path" : "Hcal/HcalRecHitTask/HB/HB_RecHitTimeVSenergy",
			"description" : "HB RecHit Timing vs Energy for E>5GeV, "
		}
	],
	[
		{
			"path" : "Hcal/HcalRecHitTask/HE/HE_RecHitTime",
			"description" : "HE RecHit Timing, E>5GeV, "
		},
		{
			"path" : "Hcal/HcalRecHitTask/HE/HE_RecHitTimeVSenergy",
			"description" : "HE RecHit Timing vs Energy for E>5GeV, "
		}
	]
)

shifthcallayout(dqmitems, "16 HCAL D1&D2 Digi and RecHit Occupancies with Cuts",
	[
		{
			"path" : "Hcal/HcalDigiTask/HBHEHF_OccupancyMapD1_ZSCut",
			"description" : "HBHEHF D1 Digi Occupancy after applying 3TS cut of 20 nom fC"
		},
		{
			"path" : "Hcal/HcalDigiTask/HBHEHF_OccupancyMapD2_ZSCut",
			"description" : "HBHEHF D2 Digi Occupancy after applying 3TS cut of 20 nomfC"
		}
	],
	[
		{
			"path" : "Hcal/HcalRecHitTask/HBHEHFD1_RecHitOccupancy",
			"description" : "HBHEHF D1 RecHit Occupancy after applying 5GeV Cut"
		},
		{
			"path" : "Hcal/HcalRecHitTask/HBHEHFD2_RecHitOccupancy",
			"description" : "HBHEHF D2 RecHit Occupancy after applying 5GeV Cut"
		}
	]
)

shifthcallayout(dqmitems, "17 HCAL HFP&HFM RecHit iphi-dependent Occupancies Tracking",
	[
		{
			"path" : "Hcal/HcalRecHitTask/HF/HF_iphiOccupancyRatios",
			"description" : "HFP&HFM uHTR Occupancy Ratios with neighboring uHTR in terms of iphi"
		}
	],
	[
		{
			"path" : "Hcal/HcalRecHitTask/HF/HFM_OccupancyVSiphi",
			"description" : "HFM Occupancy vs iphi"
		},
		{
			"path" : "Hcal/HcalRecHitTask/HF/HFP_OccupancyVSiphi",
			"description" : "HFP Occupancy vs iphi"
		}
	]
)

shifthcallayout(dqmitems, "18 HCAL RAW Evn&Bcn Mismatches",
	[
		{
			"path" : "Hcal/HcalRawTask/uTCA/uTCA_CratesVSslots_dBcN",
			"description" : "uTCA Crates BCN Mismatches"
		},
		{
			"path" : "Hcal/HcalRawTask/uTCA/uTCA_CratesVSslots_dEvN",
			"description" : "uTCA Crates EVN Mismatches"
		}
	]
)

shifthcallayout(dqmitems, "19 HCAL HF Data&Emul TP Et Mismatches",
	[
		{
			"path" : "Hcal/HcalTPTask/HF/HF_SOI_Et_Correlation",
			"description" : "HF Et Correlation for Data vs Emulator"
		},
		{
			"path" : "Hcal/HcalTPTask/HBHEHF_Mismatch_SOIEt",
			"description" : "HBHEHF Map of SOI Et Mismatches"
		}
	]
)







