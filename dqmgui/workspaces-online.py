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
server.workspace('DQMContent', 3, 'Summaries', 'Everything', '^', '^')

# Tracker/Muons workspaces:
server.workspace('DQMContent', 20, 'Tracker/Muons', 'Pixel', '^Pixel/', '',
                 'Pixel/Layouts/000 - Pixel FED Occupancy vs Lumi Sections',
                 'Pixel/Layouts/00a - Pixel_Error_Summary',
                 'Pixel/Layouts/00b - Pixel_Error_Summary',
                 'Pixel/Layouts/00c - Pixel_Error_Summary',
                 'Pixel/Layouts/09 - Pixel Clusters vs LS',
                 'Pixel/Layouts/20a - Cluster occupancy Barrel Layer 1',
                 'Pixel/Layouts/20b - Cluster occupancy Barrel Layer 2',
                 'Pixel/Layouts/20c - Cluster occupancy Barrel Layer 3',
                 'Pixel/Layouts/20d - Cluster occupancy Endcap -z Disk 1',
                 'Pixel/Layouts/20e - Cluster occupancy Endcap -z Disk 2',
                 'Pixel/Layouts/20f - Cluster occupancy Endcap +z Disk 1',
                 'Pixel/Layouts/20g - Cluster occupancy Endcap +z Disk 2',
                 'Pixel/Layouts/30a - Pixel event rates',
                )
server.workspace('DQMContent', 21, 'Tracker/Muons', 'SiStrip', '^(SiStrip|Tracking)/', '',
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
server.workspace('DQMContent', 22, 'Tracker/Muons', 'DT', '^DT/', '',
                 'DT/Layouts/00-Summary/00-DataIntegritySummary',
                 'DT/Layouts/00-Summary/00-ROChannelSummary',
                 'DT/Layouts/00-Summary/01-OccupancySummary',
                 'DT/Layouts/00-Summary/02-SegmentSummary',
                 'DT/Layouts/00-Summary/03-TM_TriggerCorrFractionSummary',
                 'DT/Layouts/00-Summary/04-TM_Trigger2ndFractionSummary',
                 'DT/Layouts/00-Summary/05-NoiseChannelsSummary',
                 'DT/Layouts/00-Summary/06-SynchNoiseSummary',
                )
server.workspace('DQMContent', 23, 'Tracker/Muons', 'RPC', '^RPC/', '',
                 'RPC/Layouts/01-Fatal_FED_Errors',
                 'RPC/Layouts/02-RPC_Events',
                 'RPC/Layouts/08-Barrel_Occupancy',
                 'RPC/Layouts/09-Endcap_Occupancy',
                )
server.workspace('DQMContent', 24, 'Tracker/Muons', 'CSC', '^CSC/', '',
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

# Calorimeter workspaces:
server.workspace('DQMContent', 30, 'Calorimeter', 'EcalPreshower', '^EcalPreshower/', '',
                 'EcalPreshower/Layouts/01-IntegritySummary-EcalPreshower',
                 'EcalPreshower/Layouts/02-GoodRechitOccupancySummary-EcalPreshower',
                 'EcalPreshower/Layouts/03-GoodRechitEnergySummary-EcalPreshower',
                 'EcalPreshower/Layouts/04-ESTimingTaskSummary-EcalPreshower',
                 'EcalPreshower/Layouts/05-ESGain-EcalPreshower',
                )
server.workspace('DQMContent', 31, 'Calorimeter', 'Ecal', '(^Ecal(|Barrel|Endcap|Calibration)/|^L1T2016/L1TStage2CaloLayer1/ECalDetail/ecalOccRecdEtWgt|^L1T2016/L1TStage2CaloLayer1/ECalDetail/ecalOccSent|^L1T2016/L1TStage2CaloLayer1/ECalDetail/ecalOccSentAndRecd|^HLT/ObjectMonitor/MainShifter/di-Electron_Mass)', 'Ecal/Layouts',
                 'Ecal/Layouts/00 Summary',
                 'Ecal/Layouts/01 Occupancy Summary',
                 'Ecal/Layouts/02 Calibration Summary',
                )
# Ecal workspace modified above to include three L1 Trigger plots and one HLT plot as requested by Ecal team
server.workspace('DQMContent', 32, 'Calorimeter', 'HCAL', '^(Hcal|Hcal2)/', '',
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
server.workspace('DQMContent',33,'Calorimeter','HCALcalib', '^HcalCalib/', '',
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
server.workspace('DQMContent', 34, 'Calorimeter', 'Castor', '^Castor/', '',
                 'Castor/Layouts/01 - Map of frontend and readout errors',
                 'Castor/Layouts/02 - Channel-wise timing',
                 'Castor/Layouts/02b - Channel-wise timing (rms)',
                 'Castor/Layouts/Digi/05 - DigiSize',
                )

# Trigger/Lumi workspaces:
server.workspace('DQMContent', 40, 'Trigger/Lumi', 'L1T', '^(L1T|L1T2016)/', '',
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
                 'L1T/Layouts/Stage2-QuickCollection/10 - uGT Algorithm Trigger Bits (after BX mask) vs. BX Number in Event',
                )

server.workspace('DQMContent', 41, 'Trigger/Lumi', 'L1TEMU', '^(L1TEMU|L1T2016EMU)/', '',
                 # Please add plots to Stage2-QuickCollection layout in layouts/l1temulator-layouts.py
                 # with a useful name and description, then reference them here
                 # 'L1TEMU/Layouts/Stage2-QuickCollection/',
                )
server.workspace('DQMContent', 42, 'Trigger/Lumi', 'HLT', '^HLT/', '',
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

# CTPPS workspaces:
server.workspace('DQMContent', 51, 'CTPPS', 'TrackingStrip', '^CTPPS/', 'CTPPS/TrackingStrip/Layouts')
