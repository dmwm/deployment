# workspace method arguments:
#   type: Type of workspace. Use DQMContent for custom workspaces.
#   rank: Integer defining the order in which to show the workspaces
#   category: Column name of the column in which you want the workspace
#   name: Name of the workspace
#   match: Regular expression defining which elements to display (this acts as
#          filter on the complete tree)
#   layout: Folder to browse to when the layout button is clicked. If left
#           empty this is <name>/Layouts
#   *content: Layouts for the Quick Collection = what will be displayed when
#             the workspace is first opened

# This file can be edited by many people, please respect the formatting!
# (I.e.: Don't make a mess.)

# DQM workspaces:
server.workspace('DQMQuality', 0, 'Summaries', 'Summary')

server.workspace('DQMSummary', 1, 'Summaries', 'Reports')

server.workspace('DQMShift',   2, 'Summaries', 'Shift')

server.workspace('DQMContent', 3, 'Summaries', 'Info', '^Info/', '',
                 'Info/Layouts/1 - HV and Beam Status per LumiSection',
                 'Info/Layouts/2 - Run key set for DQM',
                 'Info/Layouts/3 - HLT menu used',
                 'Info/Layouts/4 - Version of CMSSW used',
                 'Info/Layouts/5 - Global Tag used',
                )

server.workspace('DQMContent', 4, 'Summaries', 'Everything', '^', '^')

# Trigger workspaces:
server.workspace('DQMContent', 10, 'Trigger', 'L1T', '^(L1T|L1T2016)/', '',
                 # Please add plots to Stage2-QuickCollection layout in layouts/l1t-layouts.py
                 # with a useful name and description, then reference them here
                 'L1T/Layouts/Stage2-QuickCollection/00 - Calo Layer1 ECAL Input Occupancy',
                 'L1T/Layouts/Stage2-QuickCollection/01 - Calo Layer1 HCAL Input Occupancy',
                 'L1T/Layouts/Stage2-QuickCollection/02 - Calo Layer1 Input Link Errors',
                 'L1T/Layouts/Stage2-QuickCollection/03 - uGMT MUON BX',
                 'L1T/Layouts/Stage2-QuickCollection/04 - uGMT MUON ETA',
                 'L1T/Layouts/Stage2-QuickCollection/05 - uGMT MUON P_{T}',
                 'L1T/Layouts/Stage2-QuickCollection/06 - uGMT MUON PHI ETA',
                 'L1T/Layouts/Stage2-QuickCollection/07 - uGT Algorithm Trigger Bits (after prescale) vs. Global BX Number',
                 'L1T/Layouts/Stage2-QuickCollection/08 - uGT Algorithm Trigger Bits (after prescale) vs. BX Number in Event',
                 'L1T/Layouts/Stage2-QuickCollection/09 - uGT Algorithm Trigger Bits (after prescale)',
		 'L1T/Layouts/Stage2-QuickCollection/10 - Calo Layer2 Central Jet Bx Occupancy distribution',
		 'L1T/Layouts/Stage2-QuickCollection/11 - Calo Layer2 Central Jet Et Eta vs Phi distribution',
		 'L1T/Layouts/Stage2-QuickCollection/12 - Calo Layer2 Central Jets Pt distribution',
		 'L1T/Layouts/Stage2-QuickCollection/13 - Calo Layer2 Forward Jet Bx Occupancy distribution',
		 'L1T/Layouts/Stage2-QuickCollection/14 - Calo Layer2 Forward Jet Et Eta vs Phi distribution',
		 'L1T/Layouts/Stage2-QuickCollection/15 - Calo Layer2 Forward Jet Pt distribution',
		 'L1T/Layouts/Stage2-QuickCollection/16 - Calo Layer2 Isolated EG Bx Occupancy distribution',
		 'L1T/Layouts/Stage2-QuickCollection/17 - Calo Layer2 Isolated EG Et Eta vs Phi distribution',
		 'L1T/Layouts/Stage2-QuickCollection/18 - Calo Layer2 Isolated EG Pt distribution',
		 'L1T/Layouts/Stage2-QuickCollection/19 - Calo Layer2 Non-Isolated EG Bx Occupancy distribution',
		 'L1T/Layouts/Stage2-QuickCollection/20 - Calo Layer2 Non-Isolated EG Et Eta vs Phi distribution',
		 'L1T/Layouts/Stage2-QuickCollection/21 - Calo Layer2 Non-Isolated EG Pt distribution',
		 'L1T/Layouts/Stage2-QuickCollection/22 - Calo Layer2 Isolated Tau Bx Occupancy distribution',
		 'L1T/Layouts/Stage2-QuickCollection/23 - Calo Layer2 Isolated Tau Et Eta vs Phi distribution',
		 'L1T/Layouts/Stage2-QuickCollection/24 - Calo Layer2 Isolated Tau Pt distribution',
		 'L1T/Layouts/Stage2-QuickCollection/25 - Calo Layer2 Non-Isolated Tau Bx Occupancy distribution',
		 'L1T/Layouts/Stage2-QuickCollection/26 - Calo Layer2 Non-Isolated Tau Et Eta vs Phi distribution',
		 'L1T/Layouts/Stage2-QuickCollection/27 - Calo Layer2 Non-Isolated Tau Pt distribution',
		 'L1T/Layouts/Stage2-QuickCollection/28 - Calo Layer2 ETTEM Et distribution',
                 'L1T/Layouts/Stage2-QuickCollection/29 - Calo Layer2 ETT Et distribution',
                 'L1T/Layouts/Stage2-QuickCollection/30 - Calo Layer2 EtSum Bx Occupancy distribution',
                 'L1T/Layouts/Stage2-QuickCollection/31 - Calo Layer2 HTT Et distribution',
                 'L1T/Layouts/Stage2-QuickCollection/32 - Calo Layer2 METHF Phi distribution',
                 'L1T/Layouts/Stage2-QuickCollection/33 - Calo Layer2 METHF Et distribution',
                 'L1T/Layouts/Stage2-QuickCollection/34 - Calo Layer2 MET Phi distribution',
                 'L1T/Layouts/Stage2-QuickCollection/35 - Calo Layer2 MET Et distribution',
                 'L1T/Layouts/Stage2-QuickCollection/36 - Calo Layer2 MHTHF Phi distribution',
		 'L1T/Layouts/Stage2-QuickCollection/37 - Calo Layer2 MHTHF Et distribution',
	         'L1T/Layouts/Stage2-QuickCollection/38 - Calo Layer2 MHT Phi distribution',
	         'L1T/Layouts/Stage2-QuickCollection/39 - Calo Layer2 MHT Et distribution',
	         'L1T/Layouts/Stage2-QuickCollection/40 - ECAL TPG Input Link Errors',
	         'L1T/Layouts/Stage2-QuickCollection/41 - ECAL TPG Event Mismatches',
	         'L1T/Layouts/Stage2-QuickCollection/42 - HCAL TPG Input Link Errors',
	         'L1T/Layouts/Stage2-QuickCollection/43 - HCAL TPG Event Mismatches',
	         'L1T/Layouts/Stage2-QuickCollection/44 - Calo Layer1 Event Mismatches',
	         'L1T/Layouts/Stage2-QuickCollection/45 - BMTF Muon HW p_{T}',
	         'L1T/Layouts/Stage2-QuickCollection/46 - BMTF Muon Wedge vs BX',
	         'L1T/Layouts/Stage2-QuickCollection/47 - EMTF LCT Occupancy',
	         'L1T/Layouts/Stage2-QuickCollection/48 - EMTF Track vs BX',
	         'L1T/Layouts/Stage2-QuickCollection/49 - uGMT BMTF BX',
	         'L1T/Layouts/Stage2-QuickCollection/50 - uGMT BMTF HW Phi',
	         'L1T/Layouts/Stage2-QuickCollection/51 - uGMT BMTF HW Eta',
	         'L1T/Layouts/Stage2-QuickCollection/52 - uGMT BMTF HW vs Sign',
	         'L1T/Layouts/Stage2-QuickCollection/53 - uGMT OMTF BX',
	         'L1T/Layouts/Stage2-QuickCollection/54 - uGMT OMTF Positive HW Phi',
	         'L1T/Layouts/Stage2-QuickCollection/55 - uGMT OMTF Negative HW Phi',
	         'L1T/Layouts/Stage2-QuickCollection/56 - uGMT OMTF HW Eta',
	         'L1T/Layouts/Stage2-QuickCollection/57 - uGMT OMTF HW p_{T}',
	         'L1T/Layouts/Stage2-QuickCollection/58 - uGMT OMTF HW Sign',
	         'L1T/Layouts/Stage2-QuickCollection/59 - uGMT EMTF BX',
	         'L1T/Layouts/Stage2-QuickCollection/60 - uGMT EMTF Phi',
	         'L1T/Layouts/Stage2-QuickCollection/61 - uGMT Input vs BMTF Output misMatch Ratio',
	         'L1T/Layouts/Stage2-QuickCollection/62 - uGMT Muon Copy 1 misMatch Ratio',
	         'L1T/Layouts/Stage2-QuickCollection/63 - uGMT Muon Copy 2 misMatch Ratio',
	         'L1T/Layouts/Stage2-QuickCollection/64 - uGMT Muon Copy 3 misMatch Ratio',
	         'L1T/Layouts/Stage2-QuickCollection/65 - uGMT Muon Copy 4 misMatch Ratio',
	         'L1T/Layouts/Stage2-QuickCollection/66 - uGMT Muon Copy 5 misMatch Ratio',
	         'L1T/Layouts/Stage2-QuickCollection/67 - uGMT Zero Suppression misMatch Ratio (All Events)',
	         'L1T/Layouts/Stage2-QuickCollection/68 - uGMT Zero Suppression misMatch Ratio (Fat Events)',
	         'L1T/Layouts/Stage2-QuickCollection/69 - uGT Input vs uGMT Output misMatch Ratio',
                )

server.workspace('DQMContent', 11, 'Trigger', 'L1TEMU', '^(L1TEMU|L1T2016EMU)/', '',
                 # Please add plots to Stage2-QuickCollection layout in layouts/l1temulator-layouts.py
                 # with a useful name and description, then reference them here
                 'L1TEMU/Layouts/Stage2-QuickCollection/00 - CaloTower Data-Emulator Status',
                 "L1TEMU/Layouts/Stage2-QuickCollection/01 - uGMT Data-Emulator misMatch ratio",
                 "L1TEMU/Layouts/Stage2-QuickCollection/02 - BMTF Data-Emulator misMatch ratio",
                 "L1TEMU/Layouts/Stage2-QuickCollection/03 - OMTF Data-Emulator misMatch ratio",
                 "L1TEMU/Layouts/Stage2-QuickCollection/04 - EMTF Data-Emulator misMatch ratio",
		 "L1TEMU/Layouts/Stage2-QuickCollection/05 - Calo Layer2 EG Data-Emulator Agreement Summary",
		 "L1TEMU/Layouts/Stage2-QuickCollection/06 - Calo Layer2 Energy Sum Data-Emulator Agreement Summary",
		 "L1TEMU/Layouts/Stage2-QuickCollection/07 - Calo Layer2 High Level Data-Emulator Agreement Summary",
		 "L1TEMU/Layouts/Stage2-QuickCollection/08 - Calo Layer2 Jet Data-Emulator Agreement Summary",
		 "L1TEMU/Layouts/Stage2-QuickCollection/09 - Calo Layer2 Problem Summary",
		 "L1TEMU/Layouts/Stage2-QuickCollection/10 - Calo Layer2 Tau Data-Emulator Agreement Summary",
                 "L1TEMU/Layouts/Stage2-QuickCollection/11 - uGT Data-Emulator misMatch ratio",
                 "L1TEMU/Layouts/Stage2-QuickCollection/12 - uGMT Intermediate Muon BMTF Data-Emulator misMatch ratio",
                 "L1TEMU/Layouts/Stage2-QuickCollection/13 - uGMT Intermediate Muon OMTF Neg Data-Emulator misMatch ratio",
                 "L1TEMU/Layouts/Stage2-QuickCollection/14 - uGMT Intermediate Muon OMTF Pos Data-Emulator misMatch ratio",
                 "L1TEMU/Layouts/Stage2-QuickCollection/15 - uGMT Intermediate Muon EMTF Neg Data-Emulator misMatch ratio",
                 "L1TEMU/Layouts/Stage2-QuickCollection/16 - uGMT Intermediate Muon EMTF Pos Data-Emulator misMatch ratio",
                )

server.workspace('DQMContent', 12, 'Trigger', 'HLT', '^HLT/', '',
                 'HLT/ObjectMonitor/MainShifter/Photon_pT',
                 'HLT/ObjectMonitor/MainShifter/Muon_pT',
                 'HLT/ObjectMonitor/MainShifter/Electron_pT',
                 'HLT/ObjectMonitor/MainShifter/Jet_pT',
                 'HLT/ObjectMonitor/MainShifter/JetAK8_Pt',
                 'HLT/ObjectMonitor/MainShifter/JetAK8_mass',
                 'HLT/ObjectMonitor/MainShifter/Tau_pT',
                 'HLT/ObjectMonitor/MainShifter/Dimuon_LowMass',
                 'HLT/ObjectMonitor/MainShifter/diMuon_Mass',
                 'HLT/ObjectMonitor/MainShifter/di-Electron_Mass',
                 'HLT/ObjectMonitor/MainShifter/alphaT',
                 'HLT/ObjectMonitor/MainShifter/CaloMET_pT',
                 'HLT/ObjectMonitor/MainShifter/CaloHT_pT',
                 'HLT/ObjectMonitor/MainShifter/PFHT_pT',
                 'HLT/ObjectMonitor/MainShifter/PFMET_pT',
                 'HLT/ObjectMonitor/MainShifter/L2Muon_pT',
                 'HLT/ObjectMonitor/MainShifter/L2NoBPTXMuon_pT',
                 'HLT/ObjectMonitor/MainShifter/Rsq',
                 'HLT/ObjectMonitor/MainShifter/mr',
                 'HLT/ObjectMonitor/MainShifter/Muon_dxy',
                 'HLT/ObjectMonitor/MainShifter/bJetCSVCalo',
                 'HLT/ObjectMonitor/MainShifter/bJetCSVPF',
                 'HLT/Tracking/iter2Merged/GeneralProperties/TrackPt_ImpactPoint_GenTk',
                 'HLT/Tracking/pixelTracks/GeneralProperties/TrackPt_ImpactPoint_GenTk',
                 'HLT/Tracking/iter2Merged/GeneralProperties/NumberOfTracksVsLS_GenTk',
                 'HLT/Tracking/pixelTracks/GeneralProperties/NumberOfTracksVsLS_GenTk',
                 'HLT/Tracking/iter2Merged/GeneralProperties/NumberOfRecHitsPerTrackVsLS_GenTk',
                 'HLT/Tracking/pixelTracks/GeneralProperties/NumberOfRecHitsPerTrackVsLS_GenTk',
                 'HLT/SiStrip/MechanicalView/TIB/TotalNumberOfClusterProfile__TIB',
                 'HLT/Layouts/highestRate Summary',
                )

# Tracker workspaces:
server.workspace('DQMContent', 19, 'Tracker', 'PixelPhase1', '^PixelPhase1/', '',
                  'PixelPhase1/Layouts/000 - PixelPhase1 ReportSummary: Layer or Disk vs subdet',
                  #'PixelPhase1/Layouts/01a - PixelPhase1_Event_Rate',
                  'PixelPhase1/Layouts/00a - PixelPhase1 FED Occupancy vs Lumi Sections',
                  'PixelPhase1/Layouts/00b - PixelPhase1_Error_Summary', 
                  'PixelPhase1/Layouts/01c - PixelPhase1 Cluster Size vs Cluster Eta',
                  'PixelPhase1/Layouts/02 - PixelPhase1_Digi_ADC_Barrel',
                  'PixelPhase1/Layouts/03 - PixelPhase1_Digi_ADC_Endcap',
                  'PixelPhase1/Layouts/04 - PixelPhase1_Cluster_Number',
                  'PixelPhase1/Layouts/05 - PixelPhase1_Cluster_Charge',
                  'PixelPhase1/Layouts/06 - PixelPhase1_Cluster_Size',
                  'PixelPhase1/Layouts/19 - PixelPhase1 Digis: Ladder vs Module barrel summary',
                  'PixelPhase1/Layouts/20 - PixelPhase1 Clusters: Ladder vs Module barrel summary',
                  'PixelPhase1/Layouts/24 - PixelPhase1 Cluster Position: Z vs Phi barrel summary',
                  'PixelPhase1/Layouts/27 - PixelPhase1 Digis: BladePanel vs Disk endcap summary',
                  'PixelPhase1/Layouts/28 - PixelPhase1 Clusters: BladePanel vs Disk endcap summary',
                  'PixelPhase1/Layouts/30 - PixelPhase1 Cluster Position: X vs Y endcap summary',
                  'PixelPhase1/Layouts/31 - PixelPhase1 Dead ROC Trends in barrel',
                  'PixelPhase1/Layouts/32 - PixelPhase1 Dead ROC Trends in endcap',
                  'PixelPhase1/Layouts/33 - ntracks',
                  'PixelPhase1/Layouts/34 - Charge and size (on-track)',
                  'PixelPhase1/Layouts/35a - Cluster charge (on-track) per Inner Ladders',
                  'PixelPhase1/Layouts/35b - Cluster charge (on-track) per Outer Ladders',  
                  #'PixelPhase1/Layouts/35 - Cluster on track and vertices per lumi',
                  'PixelPhase1/Layouts/36 - Cluster position (on-track) per PXLayer',
                  'PixelPhase1/Layouts/37 - Cluster position (on-track) per Disk',
                  'PixelPhase1/Layouts/40 - PixelPhase1 Residuals',
                  'PixelPhase1/Layouts/41a - ClusterSize Vs Eta (on-track) inner',
                  'PixelPhase1/Layouts/41b - ClusterSize Vs Eta (on-track) outer',
                )


server.workspace('DQMContent', 21, 'Tracker', 'SiStrip', '^(SiStrip|Tracking)/', '',
                 'SiStrip/Layouts/00 - SiStrip ReportSummary',
                 'SiStrip/Layouts/01 - FED-Detected Errors Summary',
                 'SiStrip/Layouts/02 - FED-Detected Errors Trend',
                 'SiStrip/Layouts/03 - # of Digi Trend',
                 'SiStrip/Layouts/04 - # of Cluster Trend',
                 'SiStrip/Layouts/05 - OnTrackCluster (StoN)',
                 'SiStrip/Layouts/06 - OffTrackCluster (Total Number)',
                 'SiStrip/Layouts/07 - Tracking ReportSummary',
                 'SiStrip/Layouts/08 - Tracks (pp collisions)',
                 'SiStrip/Layouts/09 - Tracks (Cosmic Tracking)',
                 'SiStrip/Layouts/10 - Tracks (HI run)',
                 'SiStrip/Layouts/11a - FED Errors vs FED ID',
                )

# Calorimeter workspaces:
server.workspace('DQMContent', 30, 'Calorimeters', 'Ecal', '(^Ecal(|Barrel|Endcap|Calibration)/|^L1T/L1TStage2CaloLayer1/ECalDetail/ecalOccRecdEtWgt|^L1T/L1TStage2CaloLayer1/ECalDetail/ecalOccSent|^L1T/L1TStage2CaloLayer1/ECalDetail/ecalOccSentAndRecd|^HLT/ObjectMonitor/MainShifter/di-Electron_Mass)', 'Ecal/Layouts',
                 'Ecal/Layouts/00 Summary',
                 'Ecal/Layouts/01 Occupancy Summary',
                 'Ecal/Layouts/02 Calibration Summary',
                )
                # Ecal workspace modified above to include three L1 Trigger
                # plots and one HLT plot as requested by Ecal team

server.workspace('DQMContent', 31, 'Calorimeters', 'EcalPreshower', '^EcalPreshower/', '',
                 'EcalPreshower/Layouts/01-IntegritySummary-EcalPreshower',
                 'EcalPreshower/Layouts/02-GoodRechitOccupancySummary-EcalPreshower',
                 'EcalPreshower/Layouts/03-GoodRechitEnergySummary-EcalPreshower',
                 'EcalPreshower/Layouts/04-ESTimingTaskSummary-EcalPreshower',
                 'EcalPreshower/Layouts/05-ESGain-EcalPreshower',
                )

server.workspace('DQMContent', 32, 'Calorimeters', 'HCAL', '^(Hcal|Hcal2)/', '',
                 'Hcal/Layouts/00 Current Summary',
                 'Hcal/Layouts/01 RAW Bad Quality',
                 'Hcal/Layouts/02 RAW Bad Quality depth',
                 'Hcal/Layouts/03 RAW Mismatches',
                 'Hcal/Layouts/04 DIGI Missing 1LS',
                 'Hcal/Layouts/05 DIGI Occupancy',
                 'Hcal/Layouts/06 DIGI Occupancy Total',
                 'Hcal/Layouts/07 DIGI Occupancy Cut',
                 'Hcal/Layouts/08 DIGI Timing',
                 'Hcal/Layouts/09 DIGI Total Charge',
                 'Hcal/Layouts/10 DIGI Occupancy vs LS',
                 'Hcal/Layouts/11 DIGI Amplitude vs LS',
                 'Hcal/Layouts/12 RECO Energy',
                 'Hcal/Layouts/13 RECO Occupancy',
                 'Hcal/Layouts/14 RECO Occupancy Cut',
                 'Hcal/Layouts/15 RECO Timing',
                 'Hcal/Layouts/16 RECO HBHEabc Timing',
                 'Hcal/Layouts/17 RECO Timing vs Energy',
                 'Hcal/Layouts/18 TP Et Correlation',
                 'Hcal/Layouts/19 TP Et Correlation Ratio',
                 'Hcal/Layouts/20 TP Et Distribution',
                 'Hcal/Layouts/21 TP Et Mismatches',
                 'Hcal/Layouts/22 TP Et Missing',
                 'Hcal/Layouts/23 TP Et Occupancy'
                )

server.workspace('DQMContent',33,'Calorimeters','HCALcalib', '^HcalCalib/', '',
                 'HcalCalib/Layouts/00 Current Summary',
                 'HcalCalib/Layouts/01 Pedestal Mean',
                 'HcalCalib/Layouts/02 Pedestal Mean by FED',
                 'HcalCalib/Layouts/03 Pedestal RMS',
                 'HcalCalib/Layouts/04 Pedestal RMS by FED',
                 'HcalCalib/Layouts/05 Pedestal Mean DB Ref',
                 'HcalCalib/Layouts/06 Pedestal Mean DB Ref by FED',
                 'HcalCalib/Layouts/07 Pedestal RMS DB Ref',
                 'HcalCalib/Layouts/08 Pedestal RMS DB Ref by FED',
                 'HcalCalib/Layouts/09 Pedestal Mean Bad',
                 'HcalCalib/Layouts/10 Pedestal Mean Bad by FED',
                 'HcalCalib/Layouts/11 Pedestal RMS Bad',
                 'HcalCalib/Layouts/12 Pedestal RMS Bad by FED',
                 'HcalCalib/Layouts/13 Pedestal Missing',
                 'HcalCalib/Layouts/14 Pedestal Missing by FED',
                 'HcalCalib/Layouts/15 Pedestal Occupancy vs LS',
                 'HcalCalib/Layouts/16 Missing vs LS',
                 'HcalCalib/Layouts/17 Number of Bad Mean vs LS',
                 'HcalCalib/Layouts/18 Number of Bad RMS vs LS'
                )

server.workspace('DQMContent', 34, 'Calorimeters', 'Castor', '^Castor/', '',
                 'Castor/Layouts/01 - Map of frontend and readout errors',
                 'Castor/Layouts/02 - Channel-wise timing',
                 'Castor/Layouts/02b - Channel-wise timing (rms)',
                 'Castor/Layouts/Digi/05 - DigiSize',
                )

# Muons workspaces:
server.workspace('DQMContent', 40, 'Muons', 'DT', '^DT/', '',
                 'DT/Layouts/00-Summary/00-DataIntegritySummary',
                 'DT/Layouts/00-Summary/00-ROChannelSummary',
                 'DT/Layouts/00-Summary/01-OccupancySummary',
                 'DT/Layouts/00-Summary/02-SegmentSummary',
                 'DT/Layouts/00-Summary/03-TM_TriggerCorrFractionSummaryIn',
                 'DT/Layouts/00-Summary/04-TM_Trigger2ndFractionSummaryIn',
                 'DT/Layouts/00-Summary/05-NoiseChannelsSummary',
                 'DT/Layouts/00-Summary/06-SynchNoiseSummary',
                )

server.workspace('DQMContent', 41, 'Muons', 'RPC', '^RPC/', '',
                 'RPC/Layouts/01-Fatal_FED_Errors',
                 'RPC/Layouts/02-RPC_Events',
                 'RPC/Layouts/08-Barrel_Occupancy',
                 'RPC/Layouts/09-Endcap_Occupancy',
                )

server.workspace('DQMContent', 42, 'Muons', 'CSC', '^CSC/', '',
                 'CSC/Layouts/00 Top Physics Efficiency',
                 'CSC/Layouts/01 Station Physics Efficiency',
                 'CSC/Layouts/02 EMU Summary/EMU Test01 - DDUs in Readout',
                 'CSC/Layouts/02 EMU Summary/EMU Test03 - DDU Reported Errors',
                 'CSC/Layouts/02 EMU Summary/EMU Test04 - DDU Format Errors',
                 'CSC/Layouts/02 EMU Summary/EMU Test05 - DDU Inputs Status',
                 'CSC/Layouts/02 EMU Summary/EMU Test06 - DDU Inputs in ERROR-WARNING State',
                 'CSC/Layouts/02 EMU Summary/EMU Test08 - CSCs Reporting Data and Unpacked',
                 'CSC/Layouts/02 EMU Summary/EMU Test10 - CSCs with Errors and Warnings (Fractions)',
                 'CSC/Layouts/02 EMU Summary/EMU Test11 - CSCs without Data Blocks',
                 'CSC/Layouts/06 Physics Efficiency - RecHits Minus',
                 'CSC/Layouts/07 Physics Efficiency - RecHits Plus',
                )


# GEM workspaces:
server.workspace('DQMContent', 43, 'Muons', 'GEM', '^GEM/', '',
                 'GEM/Layouts/00 StatusDigi Critical Errors',
                 'GEM/Layouts/01 StatusDigi Warnings',
                 'GEM/Layouts/02 GEMINI01la1',
                 'GEM/Layouts/03 GEMINI01la2',
                 'GEM/Layouts/04 GEMINI27la1',
                 'GEM/Layouts/05 GEMINI27la2',
                 'GEM/Layouts/06 GEMINI28la1',
                 'GEM/Layouts/07 GEMINI28la2',
                 'GEM/Layouts/08 GEMINI29la1',
                 'GEM/Layouts/09 GEMINI29la2',
                 'GEM/Layouts/10 GEMINI30la1',
                 'GEM/Layouts/11 GEMINI30la2',
)

# CTPPS workspaces:
server.workspace('DQMContent', 50, 'CTPPS', 'TrackingStrip', '^CTPPS/', 'CTPPS/TrackingStrip/Layouts')
server.workspace('DQMContent', 51, 'CTPPS', 'TrackingPixel', '^CTPPS/TrackingPixel/', 'CTPPS/TrackingPixel/Layouts')
server.workspace('DQMContent', 52, 'CTPPS', 'TimingDiamond', '^CTPPS/TimingDiamond', 'CTPPS/TimingDiamond/Layouts')
