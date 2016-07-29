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
                 'Pixel/Layouts/20a - Cluster occupancy Barrel Layer 1',
                 'Pixel/Layouts/20b - Cluster occupancy Barrel Layer 2',
                 'Pixel/Layouts/20c - Cluster occupancy Barrel Layer 3',
                 'Pixel/Layouts/20d - Cluster occupancy Endcap -z Disk 1',
                 'Pixel/Layouts/20e - Cluster occupancy Endcap -z Disk 2',
                 'Pixel/Layouts/20f - Cluster occupancy Endcap +z Disk 1',
                 'Pixel/Layouts/20g - Cluster occupancy Endcap +z Disk 2',
                 'Pixel/Layouts/30a - Pixel event rates',
                )
server.workspace('DQMContent', 20, 'Tracker/Muons', 'SiStrip', '^(SiStrip|Tracking)/', '',
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
                )
server.workspace('DQMContent', 20, 'Tracker/Muons', 'SiStripLAS', '^SiStripLAS/', '',
                 'SiStripLAS/Layouts/00 - SiStripLAS ReportSummary',
                 'SiStripLAS/Layouts/01 - SiStripLAS TIB&TOB',
                 'SiStripLAS/Layouts/02 - SiStripLAS TEC+',
                 'SiStripLAS/Layouts/03 - SiStripLAS TEC-',
                )
server.workspace('DQMContent', 20, 'Tracker/Muons', 'CSC', '^CSC/', '',
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
server.workspace('DQMContent', 20, 'Tracker/Muons', 'DT', '^DT/', '',
                 'DT/Layouts/00-Summary/00-DataIntegritySummary',
                 'DT/Layouts/00-Summary/00-ROChannelSummary',
                 'DT/Layouts/00-Summary/01-OccupancySummary',
                 'DT/Layouts/00-Summary/02-SegmentSummary',
                 'DT/Layouts/00-Summary/03-TM_TriggerCorrFractionSummary',
                 'DT/Layouts/00-Summary/04-TM_Trigger2ndFractionSummary',
                 'DT/Layouts/00-Summary/05-NoiseChannelsSummary',
                 'DT/Layouts/00-Summary/06-SynchNoiseSummary',
                )
server.workspace('DQMContent', 20, 'Tracker/Muons', 'RPC', '^RPC/', '',
                 'RPC/Layouts/01-Fatal_FED_Errors',
                 'RPC/Layouts/02-RPC_Events',
                 'RPC/Layouts/08-Barrel_Occupancy',
                 'RPC/Layouts/09-Endcap_Occupancy',
                )

# Calorimeter workspaces:
server.workspace('DQMContent', 30, 'Calorimeter', 'EcalPreshower', '^EcalPreshower/', '',
                 'EcalPreshower/Layouts/01-IntegritySummary-EcalPreshower',
                 'EcalPreshower/Layouts/02-GoodRechitOccupancySummary-EcalPreshower',
                 'EcalPreshower/Layouts/03-GoodRechitEnergySummary-EcalPreshower',
                 'EcalPreshower/Layouts/04-ESTimingTaskSummary-EcalPreshower',
                 'EcalPreshower/Layouts/05-ESGain-EcalPreshower',
                )
server.workspace('DQMContent', 30, 'Calorimeter', 'Ecal', '(^Ecal(|Barrel|Endcap|Calibration)/|^L1T2016/L1TStage2CaloLayer1/ECalDetail/ecalOccRecdEtWgt|^L1T2016/L1TStage2CaloLayer1/ECalDetail/ecalOccSent|^L1T2016/L1TStage2CaloLayer1/ECalDetail/ecalOccSentAndRecd|^HLT/ObjectMonitor/MainShifter/di-Electron_Mass)', 'Ecal/Layouts',
                 'Ecal/Layouts/00 Summary',
                 'Ecal/Layouts/01 Occupancy Summary',
                 'Ecal/Layouts/02 Calibration Summary',
                )
# Ecal workspace modified above to include three L1 Trigger plots and one HLT plot as requested by Ecal team
server.workspace('DQMContent', 30, 'Calorimeter', 'HCAL', '^(Hcal|Hcal2)/', '',
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
server.workspace('DQMContent',30,'Calorimeter','HCALcalib', '^HcalCalib/', '',
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
server.workspace('DQMContent', 30, 'Calorimeter', 'Castor', '^Castor/', '',
                 'Castor/Layouts/01 - Map of frontend and readout errors',
                 'Castor/Layouts/02 - Channel-wise timing',
                 'Castor/Layouts/03 - Map of rechit occupancies',
                )

# Trigger/Lumi workspaces:
server.workspace('DQMContent', 40, 'Trigger/Lumi', 'L1T', '^(L1T|L1T2016)/', '',
                # Please add plots to Stage2-QuickCollection layout in layouts/l1t-layouts.py
                # with a useful name and description, then reference them here
                 'L1T/Layouts/Stage2-QuickCollection/00 - Calo Layer1 ECAL Input Occupancy',
                 'L1T/Layouts/Stage2-QuickCollection/01 - Calo Layer1 HCAL Input Occupancy',
                 'L1T/Layouts/Stage2-QuickCollection/02 - Calo Layer1 Input Link Errors',
                )
server.workspace('DQMContent', 40, 'Trigger/Lumi', 'L1TEMU', '^(L1TEMU|L1T2016EMU)/', '',
                # Please add plots to Stage2-QuickCollection layout in layouts/l1temulator-layouts.py
                # with a useful name and description, then reference them here
                 #'L1TEMU/Layouts/Stage2-QuickCollection/',
                )
server.workspace('DQMContent', 40, 'Trigger/Lumi', 'HLT', '^HLT/', '',
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

# FeedBack for Collisions workspaces:
server.workspace('DQMContent', 61, 'FeedBack for Collisions', 'Tracking FeedBack', '^(Collisions|SiStrip|Tracking|Pixel)/', 'Collisions/TrackingFeedBack',
                 'Collisions/TrackingFeedBack/00 - Number Of Tracks',
                 'Collisions/TrackingFeedBack/01 - Track Pt',
                 'Collisions/TrackingFeedBack/02 - Track Phi',
                 'Collisions/TrackingFeedBack/03 - Track Eta',
                 'Collisions/TrackingFeedBack/04 - Cluster y width vs. cluster eta',
                )
server.workspace('DQMContent', 62, 'FeedBack for Collisions', 'Ecal FeedBack', '^(Collisions|Ecal[^/]*)/', 'Collisions/EcalFeedBack',
                 'Collisions/EcalFeedBack/00 Single Event Timing',
                 'Collisions/EcalFeedBack/01 Forward-Backward EB',
                 'Collisions/EcalFeedBack/02 Forward-Backward EE',
                 'Collisions/EcalFeedBack/03 Timing Map EB',
                 'Collisions/EcalFeedBack/04 Timing Map EE -',
                 'Collisions/EcalFeedBack/05 Timing Map EE +',
                 'Collisions/EcalFeedBack/06 Timing ES',
                 'Collisions/EcalFeedBack/07 Occupancy EB',
                 'Collisions/EcalFeedBack/08 Occupancy EE -',
                 'Collisions/EcalFeedBack/09 Occupancy EE +',
                 'Collisions/EcalFeedBack/10 Occupancy ES',
                 'Collisions/EcalFeedBack/11 RecHit Energy EB',
                 'Collisions/EcalFeedBack/12 RecHit Energy EE',
                 'Collisions/EcalFeedBack/13 RecHit Energy ES',
                )
server.workspace('DQMContent', 63,'FeedBack for Collisions', 'Hcal FeedBack', '^(Collisions|Hcal)/', 'Collisions/HcalFeedBack',
                 'Collisions/HcalFeedBack/01 - HF+,HF- distributions for MinBias',
                 'Collisions/HcalFeedBack/02 - HF+,HF- distributions for Hcal HLT',
                 'Collisions/HcalFeedBack/03 - HE+,HE- distributions for MinBias',
                 'Collisions/HcalFeedBack/04 - Digi Shapes for Total Digi Signals > N counts',
                 'Collisions/HcalFeedBack/05 - Lumi Bunch Crossing Checks',
                 'Collisions/HcalFeedBack/06 - Events Per Lumi Section',
                 'Collisions/HcalFeedBack/07 - Lumi Distributions',
                 'Collisions/HcalFeedBack/08 - RecHit Average Occupancy',
                 'Collisions/HcalFeedBack/09 - RecHit Average Energy',
                 'Collisions/HcalFeedBack/10 - RecHit Average Time',
                 'Collisions/HcalFeedBack/11 - Coarse Pedestal Monitor',
                 'Collisions/HcalFeedBack/12 - HFPlus VS HFMinus Energy',
                 'Collisions/HcalFeedBack/1729 - Temporary HF Timing Study Plots',
                 )
server.workspace('DQMContent', 60,'FeedBack for Collisions', 'BeamMonitor FeedBack', '^(Collisions|BeamMonitor|BeamPixel)/', 'Collisions/BeamMonitorFeedBack',
                 'Collisions/BeamMonitorFeedBack/00 - d0-phi0 of selected tracks',
                 'Collisions/BeamMonitorFeedBack/01 - z0 of selected tracks',
                 'Collisions/BeamMonitorFeedBack/02 - x position of beam spot',
                 'Collisions/BeamMonitorFeedBack/03 - y position of beam spot',
                 'Collisions/BeamMonitorFeedBack/04 - z position of beam spot',
                 'Collisions/BeamMonitorFeedBack/05 - sigma z of beam spot',
                 'Collisions/BeamMonitorFeedBack/06 - fit results beam spot',
                 'Collisions/BeamMonitorFeedBack/07 - Pixel-Vertices: Results of Beam Spot Fit',
                 'Collisions/BeamMonitorFeedBack/08 - Pixel-Vertices: X0 vs. Lumisection',
                 'Collisions/BeamMonitorFeedBack/09 - Pixel-Vertices: Y0 vs. Lumisection',
                 'Collisions/BeamMonitorFeedBack/10 - Pixel-Vertices: Z0 vs. Lumisection',
                 )
server.workspace('DQMContent', 64,'FeedBack for Collisions', 'L1T FeedBack','^(Collisions|L1T|EcalBarrel|EcalEndcap)/', 'Collisions/L1TFeedBack',
                 'Collisions/L1TFeedBack/00 ECAL TP Spectra',
                 'Collisions/L1TFeedBack/01 ECAL TP Occupancy',
                 'Collisions/L1TFeedBack/02 ECAL TP Emulator Comparison',
                 'Collisions/L1TFeedBack/03 Rate BSCL.BSCR',
                 'Collisions/L1TFeedBack/04 Rate BSC splash right',
                 'Collisions/L1TFeedBack/05 Rate BSC splash left',
                 'Collisions/L1TFeedBack/06 Rate BSCOR and BPTX',
                 'Collisions/L1TFeedBack/07 Rate Ratio 33 over 32',
                 'Collisions/L1TFeedBack/08 Rate Ratio 41 over 40',
                 'Collisions/L1TFeedBack/09 Integ BSCL*BSCR Triggers vs LS',
                 'Collisions/L1TFeedBack/10 Integ BSCL or BSCR Triggers vs LS',
                 'Collisions/L1TFeedBack/11 Integ HF Triggers vs LS',
                 'Collisions/L1TFeedBack/12 Integ BSCOR and BPTX',
                )
server.workspace('DQMContent', 65,'FeedBack for Collisions', 'HLT FeedBack','^(Collisions|HLT)/', 'Collisions/HLTFeedBack',
                 'Collisions/HLTFeedBack/00 HLT_Egamma_Pass_Any',
                 'Collisions/HLTFeedBack/01 HLT_JetMet_Pass_Any',
                 'Collisions/HLTFeedBack/02 HLT_Muon_Pass_Any',
                 'Collisions/HLTFeedBack/03 HLT_Rest_Pass_Any',
                 'Collisions/HLTFeedBack/04 HLT_Special_Pass_Any',
                 'Collisions/HLTFeedBack/05 All_count_LS',
                 'Collisions/HLTFeedBack/06 Group_0_paths_count_LS',
                 'Collisions/HLTFeedBack/07 Group_1_paths_count_LS',
                 'Collisions/HLTFeedBack/08 Group_2_paths_count_LS',
                 'Collisions/HLTFeedBack/09 Group_3_paths_count_LS',
                 'Collisions/HLTFeedBack/10 Group_4_paths_count_LS',
                 'Collisions/HLTFeedBack/11 Group_-1_paths_count_LS',
                )
server.workspace('DQMContent', 66, 'FeedBack for Collisions', 'CSC FeedBack', '^(Collisions|CSC)/', '',
                 'CSC/Layouts/04 Timing/00 ALCT Timing',
                 'CSC/Layouts/04 Timing/01 CLCT Timing',
                )
