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
                 'L1T/Layouts/Stage2-QuickCollection/02 - Calo Layer1 Input Link Errors and event mismatches',
                 'L1T/Layouts/Stage2-QuickCollection/03 - uGMT MUON BX and Link vs BX',
                 'L1T/Layouts/Stage2-QuickCollection/04 - uGMT MUON P_{T}',
                 'L1T/Layouts/Stage2-QuickCollection/05 - uGMT MUON ETA',
                 'L1T/Layouts/Stage2-QuickCollection/06 - uGMT MUON PHI',
                 'L1T/Layouts/Stage2-QuickCollection/07 - uGMT MUON PHI ETA',
                 'L1T/Layouts/Stage2-QuickCollection/08 - uGT Algoritm Trigger Bits (before prescale) vs Global BX Number',
                 'L1T/Layouts/Stage2-QuickCollection/09 - uGT Algorithm Trigger Bits (after prescale) vs. Global BX Number',
                 'L1T/Layouts/Stage2-QuickCollection/10 - uGT Algorithm Trigger Bits (after prescale) vs. BX Number in Event',
                 'L1T/Layouts/Stage2-QuickCollection/11 - uGT Algorithm Trigger Bits (after prescale)',
                 'L1T/Layouts/Stage2-QuickCollection/12 - Calo Layer2 Bx Occupancy distributions',
                 'L1T/Layouts/Stage2-QuickCollection/13 - Calo Layer2 Central Jet Et Eta vs Phi distribution',
                 'L1T/Layouts/Stage2-QuickCollection/14 - Calo Layer2 Central Jets Pt distribution',
                 'L1T/Layouts/Stage2-QuickCollection/15 - Calo Layer2 Forward Jet Et Eta vs Phi distribution',
                 'L1T/Layouts/Stage2-QuickCollection/16 - Calo Layer2 Forward Jet Pt distribution',
                 'L1T/Layouts/Stage2-QuickCollection/17 - Calo Layer2 Isolated EG Et Eta vs Phi distribution',
                 'L1T/Layouts/Stage2-QuickCollection/18 - Calo Layer2 Isolated EG Pt distribution',
                 'L1T/Layouts/Stage2-QuickCollection/19 - Calo Layer2 Non-Isolated EG Et Eta vs Phi distribution',
                 'L1T/Layouts/Stage2-QuickCollection/20 - Calo Layer2 Non-Isolated EG Pt distribution',
                 'L1T/Layouts/Stage2-QuickCollection/21 - Calo Layer2 Isolated Tau Et Eta vs Phi distribution',
                 'L1T/Layouts/Stage2-QuickCollection/22 - Calo Layer2 Isolated Tau Pt distribution',
                 'L1T/Layouts/Stage2-QuickCollection/23 - Calo Layer2 Non-Isolated Tau Et Eta vs Phi distribution',
                 'L1T/Layouts/Stage2-QuickCollection/24 - Calo Layer2 Non-Isolated Tau Pt distribution',
                 'L1T/Layouts/Stage2-QuickCollection/25 - Calo Layer2 EtSum Bx Occupancy distribution',
                 'L1T/Layouts/Stage2-QuickCollection/26 - Calo Layer2 ETT Et distribution',
                 'L1T/Layouts/Stage2-QuickCollection/27 - Calo Layer2 ETTEM Et distribution',
                 'L1T/Layouts/Stage2-QuickCollection/28 - Calo Layer2 HTT Et distribution',
                 'L1T/Layouts/Stage2-QuickCollection/29 - Calo Layer2 MET Et distribution',
                 'L1T/Layouts/Stage2-QuickCollection/30 - Calo Layer2 MET Phi distribution',
                 'L1T/Layouts/Stage2-QuickCollection/31 - Calo Layer2 METHF Et distribution',
                 'L1T/Layouts/Stage2-QuickCollection/32 - Calo Layer2 METHF Phi distribution',
                 'L1T/Layouts/Stage2-QuickCollection/33 - Calo Layer2 MHT Et distribution',
                 'L1T/Layouts/Stage2-QuickCollection/34 - Calo Layer2 MHT Phi distribution',
                 'L1T/Layouts/Stage2-QuickCollection/35 - Calo Layer2 MHTHF Et distribution',
                 'L1T/Layouts/Stage2-QuickCollection/36 - Calo Layer2 MHTHF Phi distribution',
                 'L1T/Layouts/Stage2-QuickCollection/37 - uGMT BMTF BX and Wedge vs BX',
                 'L1T/Layouts/Stage2-QuickCollection/38 - BMTF Muon HW p_{T}',
                 'L1T/Layouts/Stage2-QuickCollection/39 - uGMT BMTF HW Eta',
                 'L1T/Layouts/Stage2-QuickCollection/40 - uGMT BMTF HW Phi',
                 'L1T/Layouts/Stage2-QuickCollection/41 - uGMT BMTF HW vs Sign',
                 'L1T/Layouts/Stage2-QuickCollection/42 - uGMT OMTF BX and Sector vs. BX',
                 'L1T/Layouts/Stage2-QuickCollection/43 - uGMT OMTF HW p_{T}',
                 'L1T/Layouts/Stage2-QuickCollection/44 - uGMT OMTF HW Eta',
                 'L1T/Layouts/Stage2-QuickCollection/45 - uGMT OMTF HW Phi (top: positive, bottom: negative)',
                 'L1T/Layouts/Stage2-QuickCollection/46 - uGMT OMTF HW Sign',
                 'L1T/Layouts/Stage2-QuickCollection/47 - uGMT EMTF BX and Track vs BX',
                 'L1T/Layouts/Stage2-QuickCollection/48 - uGMT EMTF Phi',
                 'L1T/Layouts/Stage2-QuickCollection/49 - EMTF LCT Occupancy',
                 'L1T/Layouts/Stage2-QuickCollection/50 - Calo TPG Link Errors and event mismatches (top: ECAL, bottom: HCAL)',
                 'L1T/Layouts/Stage2-QuickCollection/51 - uGT CaloLayer2 Inputs Board 2-6 misMatch Ratios',
                 'L1T/Layouts/Stage2-QuickCollection/52 - uGT Muon Inputs Board 2-6 misMatch Ratios',
                 'L1T/Layouts/Stage2-QuickCollection/53 - uGMT Muon Copy 1-5 misMatch Ratios',
                 'L1T/Layouts/Stage2-QuickCollection/54 - Input vs Output misMatch Ratios (clockwise from top left: uGT vs. uGMT, uGT vs. caloL2, uGMT vs. EMTF, uGMT vs. OMTF, uGMT vs. BMTF)',
                 'L1T/Layouts/Stage2-QuickCollection/56 - BMTF Zero Suppression misMatch Ratio (left: all events, right: fat events)',
                )

server.workspace('DQMContent', 11, 'Trigger', 'L1TEMU', '^(L1TEMU|L1T2016EMU)/', '',
                 # Please add plots to Stage2-QuickCollection layout in layouts/l1temulator-layouts.py
                 # with a useful name and description, then reference them here
                 'L1TEMU/Layouts/Stage2-QuickCollection/00 - CaloTower Data-Emulator Status',
                 "L1TEMU/Layouts/Stage2-QuickCollection/01 - uGMT Data-Emulator misMatch ratio",
                 "L1TEMU/Layouts/Stage2-QuickCollection/02 - BMTF Data-Emulator misMatch ratio",
                 "L1TEMU/Layouts/Stage2-QuickCollection/03 - OMTF Data-Emulator misMatch ratio",
                 "L1TEMU/Layouts/Stage2-QuickCollection/04 - EMTF Data-Emulator misMatch ratio",
                 "L1TEMU/Layouts/Stage2-QuickCollection/05 - Calo Layer2 High Level Data-Emulator Agreement Summary",
                 "L1TEMU/Layouts/Stage2-QuickCollection/06 - Calo Layer2 Jet Data-Emulator Agreement Summary",
                 "L1TEMU/Layouts/Stage2-QuickCollection/07 - Calo Layer2 EG Data-Emulator Agreement Summary",
                 "L1TEMU/Layouts/Stage2-QuickCollection/08 - Calo Layer2 Tau Data-Emulator Agreement Summary",
                 "L1TEMU/Layouts/Stage2-QuickCollection/09 - Calo Layer2 Energy Sum Data-Emulator Agreement Summary",
                 "L1TEMU/Layouts/Stage2-QuickCollection/10 - Calo Layer2 Problem Summary",
                 "L1TEMU/Layouts/Stage2-QuickCollection/11 - uGT Data-Emulator misMatch ratio",
                 "L1TEMU/Layouts/Stage2-QuickCollection/12 - uGMT Intermediate Muon Data-Emulator misMatch ratio",
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
                 'HLT/Tracking/tracks/GeneralProperties/TrackPt_ImpactPoint_GenTk',
                 'HLT/Tracking/pixelTracks/GeneralProperties/TrackPt_ImpactPoint_GenTk',
                 'HLT/Tracking/tracks/GeneralProperties/NumberOfTracksVsLS_GenTk',
                 'HLT/Tracking/pixelTracks/GeneralProperties/NumberOfTracksVsLS_GenTk',
                 'HLT/Tracking/tracks/GeneralProperties/NumberOfRecHitsPerTrackVsLS_GenTk',
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
                  'PixelPhase1/Layouts/35c - Cluster charge (on-track) per Disk',
                  #'PixelPhase1/Layouts/35 - Cluster on track and vertices per lumi',
                  'PixelPhase1/Layouts/36 - Cluster position (on-track) per PXLayer',
                  'PixelPhase1/Layouts/37 - Cluster position (on-track) per Disk',
                  'PixelPhase1/Layouts/40 - PixelPhase1 Residuals',
                  'PixelPhase1/Layouts/41a - ClusterSize Vs Eta (on-track) inner',
                  'PixelPhase1/Layouts/41b - ClusterSize Vs Eta (on-track) outer',
                  'PixelPhase1/Layouts/42a - Cluster size (on-track) per Ladders',
                  'PixelPhase1/Layouts/42b - Cluster size (on-track) per Disk',
                  'PixelPhase1/Layouts/43a - Dead Channels per ROC per Barrel Layer',
                  'PixelPhase1/Layouts/43b - Dead Channels per ROC per Forward Ring',
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
                 'SiStrip/Layouts/33 - Cluster & Digi occupancy per FED',
                 'SiStrip/Layouts/34 - FED Errors Vs Id Vs Lumi',
                )


server.workspace('DQMContent', 22, 'Tracker', 'SiPixelHeterogeneous', '^SiPixelHeterogeneous/', '',
                 'SiPixelHeterogeneous/Layouts/000 - Compare number of RecHits',
                 'SiPixelHeterogeneous/Layouts/00a - Compare number of tracks',
                 'SiPixelHeterogeneous/Layouts/00b - Compare number of vertices',
                 'SiPixelHeterogeneous/Layouts/00c - Compare number of FE errors per FEDid',
                 'SiPixelHeterogeneous/Layouts/01a - Compare rechit charge in Barrel',
                 'SiPixelHeterogeneous/Layouts/01b - Compare rechit charge in Endcap',
                 'SiPixelHeterogeneous/Layouts/02a - Compare rechit x-position in Barrel',
                 'SiPixelHeterogeneous/Layouts/02b - Compare rechit x-position in Endcap',
                 'SiPixelHeterogeneous/Layouts/03a - Compare rechit y-position in Barrel',
                 'SiPixelHeterogeneous/Layouts/03b - Compare rechit y-position in Endcap',
                 'SiPixelHeterogeneous/Layouts/04a - Compare rechit size x in Barrel',
                 'SiPixelHeterogeneous/Layouts/04b - Compare rechit size x in Endcap',
                 'SiPixelHeterogeneous/Layouts/05a - Compare rechit size y in Barrel',
                 'SiPixelHeterogeneous/Layouts/05b - Compare rechit size y in Endcap',
                 'SiPixelHeterogeneous/Layouts/06 - Difference in rechit charge',
                 'SiPixelHeterogeneous/Layouts/07 - Difference in rechit position',
                 'SiPixelHeterogeneous/Layouts/08 - Difference in rechit size',
                 'SiPixelHeterogeneous/Layouts/09a - Compare track properties',
                 'SiPixelHeterogeneous/Layouts/09b - Compare track properties',
                 'SiPixelHeterogeneous/Layouts/10 - Track matching phase space',
                 'SiPixelHeterogeneous/Layouts/11 - Differences in track properties',
                 'SiPixelHeterogeneous/Layouts/12a - Compare vertices',
                 'SiPixelHeterogeneous/Layouts/12b - Compare vertices',
                 'SiPixelHeterogeneous/Layouts/12c - Differences in vertex properties',
                )

# Calorimeter workspaces:
server.workspace('DQMContent', 30, 'Calorimeters', 'Ecal', '(^Ecal(|Barrel|Endcap|Calibration)/|^L1T/L1TStage2CaloLayer1/ecalOccRecdEtWgt|^L1T/L1TStage2CaloLayer1/ECalDetail/ecalOccSent|^L1T/L1TStage2CaloLayer1/ECalDetail/ecalOccSentAndRecd|^HLT/ObjectMonitor/MainShifter/di-Electron_Mass|^L1T/L1TObjects/L1TEGamma/timing/Ratio_L1TEGamma_BX_0|^L1T/L1TObjects/L1TEGamma/timing/Ratio_L1TEGamma_BX_minus1|^L1T/L1TObjects/L1TEGamma/timing/First_bunch/ptmin_20p0_gev/egamma_noniso_bx_ieta_firstbunch_ptmin20p0|^L1T/L1TObjects/L1TEGamma/timing/Last_bunch/ptmin_20p0_gev/egamma_noniso_bx_ieta_lastbunch_ptmin20p0)', 'Ecal/Layouts',
                 'Ecal/Layouts/00 Summary',
                 'Ecal/Layouts/01 Occupancy Summary',
                 'Ecal/Layouts/02 Calibration Summary',
                )
                # Ecal workspace modified above to include one additional L1 Trigger plot as requested by Trigger team                

server.workspace('DQMContent', 31, 'Calorimeters', 'EcalPreshower', '^EcalPreshower/', '',
                 'EcalPreshower/Layouts/01-IntegritySummary-EcalPreshower',
                 'EcalPreshower/Layouts/02-GoodRechitOccupancySummary-EcalPreshower',
                 'EcalPreshower/Layouts/03-GoodRechitEnergySummary-EcalPreshower',
                 'EcalPreshower/Layouts/04-ESTimingTaskSummary-EcalPreshower',
                 'EcalPreshower/Layouts/05-ESGain-EcalPreshower',
                 'EcalPreshower/Layouts/06-ES-Fiber-Error-Code',
                )

server.workspace('DQMContent', 32, 'Calorimeters', 'HCAL', '^(Hcal|Hcal2|HcalReco)/', '',
                 'Hcal/Layouts/00 Run Summary',
                 'Hcal/Layouts/01 RAW Bad Quality',
                 'Hcal/Layouts/02 RAW Bad Quality depth',
                 'Hcal/Layouts/03 RAW Bcn(Evn) Mismatches',
                 'Hcal/Layouts/04 DIGI Occupancy',
                 'Hcal/Layouts/05 DIGI Occupancy vs LS',
                 'Hcal/Layouts/06 DIGI Occupancy Cut',
                 'Hcal/Layouts/08 DIGI Occupancy Cut vs LS',
                 'Hcal/Layouts/11 DIGI Amplitude vs LS',
                 'Hcal/Layouts/14 DIGI Timing',
                 'Hcal/Layouts/18 RECO Energy',
                 'Hcal/Layouts/23 RECO Occupancy',
                 'Hcal/Layouts/24 RECO Occupancy Cut',
                 'Hcal/Layouts/28 RECO Timing',
                 'Hcal/Layouts/33 RECO HBHEabc Timing',
                 'Hcal/Layouts/34 RECO Timing vs Energy',
                 'Hcal/Layouts/35 TP Et Correlation',
                 'Hcal/Layouts/36 TP Et Correlation Ratio',
                 'Hcal/Layouts/38 TP Et Distributions',
                 'Hcal/Layouts/40 TP Et(FG) Mismatches',
                 'Hcal/Layouts/42 TP Occupancy',
                 'Hcal/Layouts/51 TP uHTR-L1T mismatch',
                 'Hcal/Layouts/53 (CapId-BX)%4'
                )

server.workspace('DQMContent',33,'Calorimeters','HCALcalib', '^HcalCalib/', '',
                 'HcalCalib/Layouts/00 Run Summary',
                 'HcalCalib/Layouts/01 Pedestal Mean vs CondDB',
                 'HcalCalib/Layouts/02 Pedestal Mean vs CondDB',
                 'HcalCalib/Layouts/03 Pedestal RMS vs CondDB',
                 'HcalCalib/Layouts/04 Pedestal RMS vs CondDB',
                 'HcalCalib/Layouts/05 Pedestal Missing vs LS',
                 'HcalCalib/Layouts/06 Pedestal Occupancy vs LS',
                 'HcalCalib/Layouts/07 Pedestal #Bad Mean Chs vs LS',
                 'HcalCalib/Layouts/08 Pedestal #Bad RMS Chs vs LS',
                 'HcalCalib/Layouts/09 Pedestal Pedestal Occupancy EA vs LS ',
                 'HcalCalib/Layouts/10 RAW BadQuality vs BX (LS)',
                 'HcalCalib/Layouts/11 RAW Bcn(Evn) Mismatches',
                 'HcalCalib/Layouts/12 LED pulse shape',
                 'HcalCalib/Layouts/13 LED pin diode amplitude',
                 'HcalCalib/Layouts/14 LED SignalMean',
                 'HcalCalib/Layouts/15 LED TDCTime'
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

server.workspace('DQMContent', 41, 'Muons', 'RPC', '^(RPC/|L1T/L1TStage2EMTF/rpc)', '',
                 'RPC/Layouts/00-Summary_Map',
                 'RPC/Layouts/01-Noisy_summary_Map',
                 'RPC/Layouts/02-Fatal_FED_Errors',
                 'RPC/Layouts/03-RPC_Events',
                 'RPC/Layouts/04-Barrel_Occupancy',
                 'RPC/Layouts/05-Endcap_Occupancy',
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
# Generated automatically by dqmgui/gem_custom/fillLayouts.py 
#   in https://github.com/quark2/deployment/tree/addingGem
#   Recipe: 
#     cd deployment/dqmgui
#     python3 gem_custom/fillLayouts.py
server.workspace('DQMContent', 43, 'Muons', 'GEM', '^GEM/', '',
                 'GEM/Layouts/Common/00 Summary', 
                 'GEM/Layouts/Common/01 GE11-M-L1 Lumi-based chamber status', 
                 'GEM/Layouts/Common/02 GE11-M-L2 Lumi-based chamber status', 
                 'GEM/Layouts/Common/03 GE11-P-L1 Lumi-based chamber status', 
                 'GEM/Layouts/Common/04 GE11-P-L2 Lumi-based chamber status', 
                 'GEM/Layouts/Common/05 GE21-M-L1-M1 Lumi-based chamber status',
                 'GEM/Layouts/Common/06 GE21-M-L1-M2 Lumi-based chamber status',
                 'GEM/Layouts/Common/07 GE21-M-L1-M3 Lumi-based chamber status',
                 'GEM/Layouts/Common/08 GE21-M-L1-M4 Lumi-based chamber status',
                 'GEM/Layouts/Common/09 GE21-P-L2-M1 Lumi-based chamber status',
                 'GEM/Layouts/Common/10 GE21-P-L2-M2 Lumi-based chamber status',
                 'GEM/Layouts/Common/11 GE21-P-L2-M3 Lumi-based chamber status',
                 'GEM/Layouts/Common/12 GE21-P-L2-M4 Lumi-based chamber status',
                 'GEM/Layouts/Common/13 AMC13 status', 
                 'GEM/Layouts/Common/14 AMC status GE11-M',
                 'GEM/Layouts/Common/15 AMC status GE11-P', 
                 'GEM/Layouts/Common/16 AMC status GE21-M',
                 'GEM/Layouts/Common/17 AMC status GE21-P',  
                 'GEM/Layouts/Common/18 GE11-M-L1 OptoHybrid status', 
                 'GEM/Layouts/Common/19 GE11-M-L2 OptoHybrid status', 
                 'GEM/Layouts/Common/20 GE11-P-L1 OptoHybrid status', 
                 'GEM/Layouts/Common/21 GE11-P-L2 OptoHybrid status', 
                 'GEM/Layouts/Common/22 GE21-M-L1-M1 OptoHybrid status',
                 'GEM/Layouts/Common/23 GE21-M-L1-M2 OptoHybrid status',
                 'GEM/Layouts/Common/24 GE21-M-L1-M3 OptoHybrid status',
                 'GEM/Layouts/Common/25 GE21-M-L1-M4 OptoHybrid status',
                 'GEM/Layouts/Common/26 GE21-P-L2-M1 OptoHybrid status',
                 'GEM/Layouts/Common/27 GE21-P-L2-M2 OptoHybrid status',
                 'GEM/Layouts/Common/28 GE21-P-L2-M3 OptoHybrid status',
                 'GEM/Layouts/Common/29 GE21-P-L2-M4 OptoHybrid status',
                 'GEM/Layouts/Common/30 GE11-M-L1 VFAT status (chamber vs. VFAT)', 
                 'GEM/Layouts/Common/31 GE11-M-L2 VFAT status (chamber vs. VFAT)', 
                 'GEM/Layouts/Common/32 GE11-P-L1 VFAT status (chamber vs. VFAT)', 
                 'GEM/Layouts/Common/33 GE11-P-L2 VFAT status (chamber vs. VFAT)', 
                 'GEM/Layouts/Common/34 GE21-M-L1-M1 VFAT status (chamber vs. VFAT)',
                 'GEM/Layouts/Common/35 GE21-M-L1-M2 VFAT status (chamber vs. VFAT)',
                 'GEM/Layouts/Common/36 GE21-M-L1-M3 VFAT status (chamber vs. VFAT)',
                 'GEM/Layouts/Common/37 GE21-M-L1-M4 VFAT status (chamber vs. VFAT)', 
                 'GEM/Layouts/Common/38 GE21-P-L2-M1 VFAT status (chamber vs. VFAT)',
                 'GEM/Layouts/Common/39 GE21-P-L2-M2 VFAT status (chamber vs. VFAT)',
                 'GEM/Layouts/Common/40 GE21-P-L2-M3 VFAT status (chamber vs. VFAT)',
                 'GEM/Layouts/Common/41 GE21-P-L2-M4 VFAT status (chamber vs. VFAT)',
                 'GEM/Layouts/Common/42 GE11-M-L1 recHit xy occupancy', 
                 'GEM/Layouts/Common/43 GE11-M-L2 recHit xy occupancy',
                 'GEM/Layouts/Common/44 GE11-P-L1 recHit xy occupancy', 
                 'GEM/Layouts/Common/45 GE11-P-L2 recHit xy occupancy', 
                 'GEM/Layouts/Common/46 GE21-M-L1 recHit xy occupancy',
                 'GEM/Layouts/Common/47 GE21-P-L2 recHit xy occupancy',
                 'GEM/Layouts/Common/48 GE11-M-L1 RecHit Average Cluster Size', 
                 'GEM/Layouts/Common/49 GE11-M-L2 RecHit Average Cluster Size',
                 'GEM/Layouts/Common/50 GE11-P-L1 RecHit Average Cluster Size', 
                 'GEM/Layouts/Common/51 GE11-P-L2 RecHit Average Cluster Size', 
                 'GEM/Layouts/Common/52 GE21-M-L1 RecHit Average Cluster Size',
                 'GEM/Layouts/Common/53 GE21-P-L2 RecHit Average Cluster Size',
                 'GEM/Layouts/Common/54 GE11-M-L1 GEM-CSC segment efficiency', 
                 'GEM/Layouts/Common/55 GE11-M-L2 GEM-CSC segment efficiency', 
                 'GEM/Layouts/Common/56 GE11-P-L1 GEM-CSC segment efficiency', 
                 'GEM/Layouts/Common/57 GE11-P-L2 GEM-CSC segment efficiency',
                )
# ParticleFlow workspaces
server.workspace('DQMContent', 44, 'ParticleFlow', 'ParticleFlow', '^ParticleFlow/', '')

# CTPPS workspaces:
server.workspace('DQMContent', 50, 'CTPPS', 'TrackingStrip', '^CTPPS/(TrackingStrip|common)/', 'CTPPS/TrackingStrip/Layouts')
server.workspace('DQMContent', 51, 'CTPPS', 'TrackingPixel', '^CTPPS/(TrackingPixel|common)/', 'CTPPS/TrackingPixel/Layouts')
server.workspace('DQMContent', 52, 'CTPPS', 'TimingDiamond', '^CTPPS/(TimingDiamond|common)/', 'CTPPS/TimingDiamond/Layouts')
server.workspace('DQMContent', 53, 'CTPPS', 'TimingFastSilicon', '^CTPPS/(TimingFastSilicon|common)/', 'CTPPS/TimingFastSilicon/Layouts')
