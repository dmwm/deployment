server.workspace('DQMQuality', 0, 'Summaries', 'Summary')
server.workspace('DQMSummary', 1, 'Summaries', 'Reports')
server.workspace('DQMShift',   2, 'Summaries', 'Shift')
server.workspace('DQMContent', 3, 'Summaries', 'Everything', '^', '^')

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
                 'Pixel/Layouts/30a - Pixel event rates')

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
                 'SiStrip/Layouts/09 - Tracks (Cosmic Tracking)')

server.workspace('DQMContent', 20, 'Tracker/Muons', 'SiStripLAS', '^SiStripLAS/', '',
                 'SiStripLAS/Layouts/00 - SiStripLAS ReportSummary',
                 'SiStripLAS/Layouts/01 - SiStripLAS TIB&TOB',
                 'SiStripLAS/Layouts/02 - SiStripLAS TEC+',
                 'SiStripLAS/Layouts/03 - SiStripLAS TEC-')

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
                 'CSC/Layouts/07 Physics Efficiency - RecHits Plus')

server.workspace('DQMContent', 20, 'Tracker/Muons', 'DT', '^DT/', '',
                 'DT/Layouts/00-Summary/00-DataIntegritySummary',
                 'DT/Layouts/00-Summary/00-ROChannelSummary',
                 'DT/Layouts/00-Summary/01-OccupancySummary',
                 'DT/Layouts/00-Summary/02-SegmentSummary',
                 'DT/Layouts/00-Summary/03-DDU_TriggerCorrFractionSummary',
                 'DT/Layouts/00-Summary/04-DDU_Trigger2ndFractionSummary',
                 'DT/Layouts/00-Summary/05-DCC_TriggerCorrFractionSummary',
                 'DT/Layouts/00-Summary/06-DCC_Trigger2ndFractionSummary',
                 'DT/Layouts/00-Summary/07-NoiseChannelsSummary',
                 'DT/Layouts/00-Summary/08-SynchNoiseSummary')

server.workspace('DQMContent', 20, 'Tracker/Muons', 'RPC', '^RPC/', '',
                 'RPC/Layouts/01-Fatal_FED_Errors',
                 'RPC/Layouts/02-RPC_Events',
                 'RPC/Layouts/08-Barrel_Occupancy',
                 'RPC/Layouts/09-Endcap_Occupancy')

server.workspace('DQMContent', 30, 'Calorimeter', 'EcalPreshower', '^EcalPreshower/', '',
                'EcalPreshower/Layouts/01-IntegritySummary-EcalPreshower',
                'EcalPreshower/Layouts/02-OccupancySummary-EcalPreshower',
                'EcalPreshower/Layouts/03-GoodRechitEnergySummary-EcalPreshower',
                'EcalPreshower/Layouts/04-RechitEnergySummary-EcalPreshower',
                'EcalPreshower/Layouts/05-ESTimingTaskSummary-EcalPreshower')

server.workspace('DQMContent', 30, 'Calorimeter', 'Ecal', '^Ecal(|Barrel|Endcap|Calibration)/', 'Ecal/Layouts',
                 'Ecal/Layouts/00 Summary',
                 'Ecal/Layouts/01 Occupancy Summary',
                 'Ecal/Layouts/02 Calibration Summary')

server.workspace('DQMContent', 30, 'Calorimeter', 'HCAL', '^Hcal/', '',
                 "Hcal/Layouts/01 HCAL Summaries",
                 'Hcal/Layouts/02 HCAL Digi Problems',
                 'Hcal/Layouts/03 HCAL Dead Cell Check',
                 'Hcal/Layouts/04 HCAL Hot Cell Check',
                 'Hcal/Layouts/05 HCAL Raw Data',
                 'Hcal/Layouts/06 HCAL Trigger Primitives',
                 'Hcal/Layouts/07 HCAL Pedestal Problems',
                 'Hcal/Layouts/08 HCAL Lumi Problems',
                 'Hcal/Layouts/09 HCAL Calibration Type',
                 'Hcal/Layouts/10 HCAL Error Thresholds',
                 'Hcal/Layouts/11 ZDC Report Summary'
                 )

server.workspace('DQMContent',30,'Calorimeter','HCALcalib', '^HcalCalib/', '',
                 'HcalCalib/Layouts/01 HcalCalib Summary',
                 'HcalCalib/Layouts/02 HcalCalib Problem Pedestals',
                 'HcalCalib/Layouts/03 HcalCalib Problem Laser',
                 'HcalCalib/Layouts/04 HcalCalib Pedestal Check',
                 'HcalCalib/Layouts/08 HcalCalib RecHit Energies')

server.workspace('DQMContent', 30, 'Calorimeter', 'Castor', '^Castor/', '',
                 'Castor/Layouts/01 - Report Summary Map',
		 'Castor/Layouts/02 - Digi Channel Summary Map',
                 'Castor/Layouts/03 - Digi Occupancy Map',
                 'Castor/Layouts/04 - Digi Saturation Summary Map',
                 'Castor/Layouts/05 - FEDFatal errors',
                 'Castor/Layouts/06 - Spigot Status',
                 'Castor/Layouts/07 - Event Products',
                 'Castor/Layouts/08 - RecHit Occupancy Map',
                 'Castor/Layouts/09a - RecHit Energy by modules',
                 'Castor/Layouts/09b - RecHit Energy by sectors',
		 'Castor/Layouts/10 - Average pulse in bunch crossings',
                 'Castor/Layouts/11_01 - Pulse Shape for sector 1',
                 'Castor/Layouts/11_02 - Pulse Shape for sector 2',
                 'Castor/Layouts/11_03 - Pulse Shape for sector 3',
                 'Castor/Layouts/11_04 - Pulse Shape for sector 4',
                 'Castor/Layouts/11_05 - Pulse Shape for sector 5',
                 'Castor/Layouts/11_06 - Pulse Shape for sector 6',
                 'Castor/Layouts/11_07 - Pulse Shape for sector 7',
                 'Castor/Layouts/11_08 - Pulse Shape for sector 8',
                 'Castor/Layouts/11_09 - Pulse Shape for sector 9',
                 'Castor/Layouts/11_10 - Pulse Shape for sector 10',
                 'Castor/Layouts/11_11 - Pulse Shape for sector 11',
                 'Castor/Layouts/11_12 - Pulse Shape for sector 12',
                 'Castor/Layouts/11_13 - Pulse Shape for sector 13',
                 'Castor/Layouts/11_14 - Pulse Shape for sector 14',
                 'Castor/Layouts/11_15 - Pulse Shape for sector 15',
                 'Castor/Layouts/11_16 - Pulse Shape for sector 16')

server.workspace('DQMContent', 40, 'Trigger/Lumi', 'HLX', '^HLX/', '',
                 'HLX/Layouts/HF-Comparison',
                 'HLX/Layouts/HLX-Averages',
                 'HLX/Layouts/HLX-Luminosity',
                 'HLX/Layouts/HLX-Occupancy-Check-Sums',
                 'HLX/Layouts/HLX-EtSumAndLumi-History-Plots')

server.workspace('DQMContent', 40, 'Trigger/Lumi', 'L1T', '^(L1T|L1TEMU)/', '',
                 'L1T/L1TGT/algo_bits',
                 'L1T/L1TGT/tt_bits',
                 'L1T/L1TGT/gtfe_bx',
                 'L1TEMU/L1TdeRCT/rctInputTPGEcalOcc',
                 'L1TEMU/L1TdeRCT/rctInputTPGHcalOcc',
                 'L1T/L1TGMT/Regional_trigger',
                 'L1T/L1TGMT/GMT_etaphi',
                 'L1T/L1TGCT/IsoEmRankEtaPhi',
                 'L1T/L1TGCT/NonIsoEmRankEtaPhi',
                 'L1T/L1TGCT/AllJetsEtEtaPhi',
                 'L1T/L1TGCT/TauJetsEtEtaPhi',
                 'L1T/Layouts/03-RCT-Summary/RctEmNonIsoEmEtEtaPhi',
                 'L1T/Layouts/03-RCT-Summary/RctEmIsoEmEtEtaPhi',
                 'L1T/Layouts/03-RCT-Summary/RctRegionsEtEtaPhi',
                 'L1T/Layouts/05-DTTF-Summary/03 - DTTF Tracks Occupancy',
                 'L1T/L1TCSCTF/CSCTF_Chamber_Occupancies',
                 'L1T/L1TCSCTF/CSCTF_occupancies',
                 'L1T/L1TRPCTF/RPCTF_muons_eta_phi_bx0')

server.workspace('DQMContent', 40, 'Trigger/Lumi', 'L1TEMU', '^L1TEMU/', '',
                 'L1TEMU/common/sysrates',
                 'L1TEMU/common/errorflag',
                 'L1TEMU/common/sysncandData',
                 'L1TEMU/common/sysncandEmul',
                 'L1TEMU/GT/GLTErrorFlag',
                 'L1TEMU/GCT/GCTErrorFlag',
                 'L1TEMU/GMT/GMTErrorFlag',
                 'L1TEMU/RCT/RCTErrorFlag',
                 'L1TEMU/CSCTF/CTFErrorFlag',
                 'L1TEMU/CSCTPG/CTPErrorFlag',
                 'L1TEMU/DTTF/DTFErrorFlag',
                 'L1TEMU/DTTPG/DTPErrorFlag',
                 'L1TEMU/RPC/RPCErrorFlag',
                 'L1TEMU/ECAL/ETPErrorFlag',
                 'L1TEMU/HCAL/HTPErrorFlag')

server.workspace('DQMContent', 40, 'Trigger/Lumi', 'HLT', '^HLT/', '',
                 'HLT/TriggerRates/L1 Algo/L1_SingleMuOpen (bit 55)',
                 'HLT/TriggerRates/L1 Algo/L1_SingleEG5 (bit 47)',
                 'HLT/TriggerRates/Streams/A',
                 'HLT/TriggerRates/Streams/Calibration',
                 'HLT/TriggerRates/Streams/DQM',
                 'HLT/TriggerRates/Streams/DQMCalibration',
                 'HLT/TriggerRates/HLT/HLT_Random_v2 accept',
                 'HLT/TriggerRates/HLT/HLT_L1SingleMuOpen_v6 accept',
                 'HLT/TriggerRates/HLT/HLT_L1SingleEG5_v1 accept',
                 'HLT/TriggerRates/HLT/HLT_Physics_v4 accept',
                 'HLT/TriggerRates/physics',
                 'HLT/TriggerRates/calibration',
                 'HLT/TriggerRates/random',
                 'HLT/TriggerRates/processed'
                )

server.workspace('DQMContent', 51,'FeedBack for Collisions', 'Tracking FeedBack', '^(Collisions|SiStrip|Tracking|Pixel)/', 'Collisions/TrackingFeedBack',
                 'Collisions/TrackingFeedBack/00 - Number Of Tracks',
                 'Collisions/TrackingFeedBack/01 - Track Pt',
                 'Collisions/TrackingFeedBack/02 - Track Phi',
                 'Collisions/TrackingFeedBack/03 - Track Eta',
                 'Collisions/TrackingFeedBack/04 - X-Position Of Closest Approach',
                 'Collisions/TrackingFeedBack/05 - Y-Position Of Closest Approach',
                 'Collisions/TrackingFeedBack/06 - Z-Position Of Closest Approach',
                 'Collisions/TrackingFeedBack/07 - Cluster y width vs. cluster eta'
)
server.workspace('DQMContent', 52,'FeedBack for Collisions', 'Ecal FeedBack', '^(Collisions|Ecal[^/]*)/', 'Collisions/EcalFeedBack',
                 "Collisions/EcalFeedBack/00 Single Event Timing",
                 "Collisions/EcalFeedBack/01 Forward-Backward EB",
                 "Collisions/EcalFeedBack/02 Forward-Backward EE",
                 "Collisions/EcalFeedBack/03 Timing Map EB",
                 "Collisions/EcalFeedBack/04 Timing Map EE -",
                 "Collisions/EcalFeedBack/05 Timing Map EE +",
                 "Collisions/EcalFeedBack/06 Timing ES",
                 "Collisions/EcalFeedBack/07 Occupancy EB",
                 "Collisions/EcalFeedBack/08 Occupancy EE -",
                 "Collisions/EcalFeedBack/09 Occupancy EE +",
                 "Collisions/EcalFeedBack/10 Occupancy ES",
                 "Collisions/EcalFeedBack/11 RecHit Energy EB",
                 "Collisions/EcalFeedBack/12 RecHit Energy EE",
                 "Collisions/EcalFeedBack/13 RecHit Energy ES"
                 )

server.workspace('DQMContent', 53,'FeedBack for Collisions', 'Hcal FeedBack', '^(Collisions|Hcal)/', 'Collisions/HcalFeedBack',

                 "Collisions/HcalFeedBack/01 - HF+,HF- distributions for MinBias",
                 "Collisions/HcalFeedBack/02 - HF+,HF- distributions for Hcal HLT",
                 "Collisions/HcalFeedBack/03 - HE+,HE- distributions for MinBias",

                 "Collisions/HcalFeedBack/04 - Digi Shapes for Total Digi Signals > N counts",
                 "Collisions/HcalFeedBack/05 - Lumi Bunch Crossing Checks",
                 "Collisions/HcalFeedBack/06 - Events Per Lumi Section",
                 "Collisions/HcalFeedBack/07 - Lumi Distributions",
                 "Collisions/HcalFeedBack/08 - RecHit Average Occupancy",
                 "Collisions/HcalFeedBack/09 - RecHit Average Energy",
                 "Collisions/HcalFeedBack/10 - RecHit Average Time",
                 "Collisions/HcalFeedBack/11 - Coarse Pedestal Monitor",
                 "Collisions/HcalFeedBack/12 - HFPlus VS HFMinus Energy",
                 "Collisions/HcalFeedBack/1729 - Temporary HF Timing Study Plots",
                 )

server.workspace('DQMContent', 50,'FeedBack for Collisions', 'BeamMonitor FeedBack', '^(Collisions|BeamMonitor|BeamPixel)/', 'Collisions/BeamMonitorFeedBack',
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
                 'Collisions/BeamMonitorFeedBack/10 - Pixel-Vertices: Z0 vs. Lumisection'
                 )

server.workspace('DQMContent', 54,'FeedBack for Collisions', 'L1T FeedBack','^(Collisions|L1T|EcalBarrel|EcalEndcap)/', 'Collisions/L1TFeedBack',
                "Collisions/L1TFeedBack/00 ECAL TP Spectra",
                "Collisions/L1TFeedBack/01 ECAL TP Occupancy",
                "Collisions/L1TFeedBack/02 ECAL TP Emulator Comparison",
                "Collisions/L1TFeedBack/03 Rate BSCL.BSCR",
                "Collisions/L1TFeedBack/04 Rate BSC splash right",
                "Collisions/L1TFeedBack/05 Rate BSC splash left",
                "Collisions/L1TFeedBack/06 Rate BSCOR and BPTX",
		"Collisions/L1TFeedBack/07 Rate Ratio 33 over 32",
		"Collisions/L1TFeedBack/08 Rate Ratio 41 over 40",
                "Collisions/L1TFeedBack/09 Integ BSCL*BSCR Triggers vs LS",
                "Collisions/L1TFeedBack/10 Integ BSCL or BSCR Triggers vs LS",
                "Collisions/L1TFeedBack/11 Integ HF Triggers vs LS",
                "Collisions/L1TFeedBack/12 Integ BSCOR and BPTX"
                )

server.workspace('DQMContent', 55,'FeedBack for Collisions', 'HLT FeedBack','^(Collisions|HLT)/', 'Collisions/HLTFeedBack',
                "Collisions/HLTFeedBack/00 HLT_Egamma_Pass_Any",
                "Collisions/HLTFeedBack/01 HLT_JetMet_Pass_Any",
                "Collisions/HLTFeedBack/02 HLT_Muon_Pass_Any",
                "Collisions/HLTFeedBack/03 HLT_Rest_Pass_Any",
                "Collisions/HLTFeedBack/04 HLT_Special_Pass_Any",
                "Collisions/HLTFeedBack/05 All_count_LS",
                "Collisions/HLTFeedBack/06 Group_0_paths_count_LS",
                "Collisions/HLTFeedBack/07 Group_1_paths_count_LS",
                "Collisions/HLTFeedBack/08 Group_2_paths_count_LS",
                "Collisions/HLTFeedBack/09 Group_3_paths_count_LS",
                "Collisions/HLTFeedBack/10 Group_4_paths_count_LS",
                "Collisions/HLTFeedBack/11 Group_-1_paths_count_LS"
                )

server.workspace('DQMContent', 56, 'FeedBack for Collisions', 'CSC FeedBack', '^(Collisions|CSC)/', '',
                'CSC/Layouts/04 Timing/00 ALCT Timing',
                'CSC/Layouts/04 Timing/01 CLCT Timing'
                )
