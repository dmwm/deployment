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

# DQM/general workspaces:
server.workspace('DQMQuality', 0, 'Summaries', 'Summary')

server.workspace('DQMSummary', 1, 'Summaries', 'Reports')

server.workspace('DQMShift', 2, 'Summaries', 'Shift')

server.workspace('DQMContent', 3, 'Summaries', 'Info', '^Info/', '',
                 'Info/Layouts/1 - High Voltage (HV) per LumiSection',
                 'Info/Layouts/2 - Processed LumiSections',
                 'Info/Layouts/3 - Run is completely processed',
                 'Info/Layouts/4 - Version of CMSSW used',
                 'Info/Layouts/5 - Global Tag used for filling',
                 'Info/Layouts/6 - Global Tag used for harvesting',
                )

server.workspace('DQMCertification', 4, 'Summaries', 'Certification')

server.workspace('DQMContent', 5, 'Summaries', 'Everything', '^', '^')

# Trigger workspaces:
server.workspace('DQMContent', 11, 'Trigger', 'L1T', '^L1T/', '')

server.workspace('DQMContent', 12, 'Trigger', 'L1TEMU', '^L1TEMU/', '')

server.workspace('DQMContent', 13, 'Trigger', 'HLT', '^HLT/', '')

# Tracker workspaces:

server.workspace('DQMContent', 19, 'Tracker', 'PixelPhase1', '^PixelPhase1/', '',
                  'PixelPhase1/Layouts/000 - PixelPhase1 ReportSummary: Layer or Disk vs subdet',
                  'PixelPhase1/Layouts/00a - PixelPhase1 FED Occupancy vs Lumi Block',
                 # 'PixelPhase1/Layouts/00b - PixelPhase1_Error_Summary',
                 # 'PixelPhase1/Layouts/01a - PixelPhase1_Event_Rate',
                  'PixelPhase1/Layouts/01b - Dead ROCs (Collisions only)',
                  'PixelPhase1/Layouts/01c - PixelPhase1 Cluster Size vs Cluster Eta',
                  'PixelPhase1/Layouts/02 - PixelPhase1_Digi_Number',
                  'PixelPhase1/Layouts/04 - PixelPhase1_Cluster_Number',
                  #'PixelPhase1/Layouts/05 - PixelPhase1_Cluster_Charge',
                  #'PixelPhase1/Layouts/06 - PixelPhase1_Cluster_Size',
                  #'PixelPhase1/Layouts/19 - PixelPhase1 Cluster Position: Z vs Phi barrel summary',
                  #'PixelPhase1/Layouts/20 - PixelPhase1 Cluster Position: X vs Y endcap summary',
                  'PixelPhase1/Layouts/21 - PixelPhase1 Digis: Ladder vs Module barrel summary',
                 # 'PixelPhase1/Layouts/22 - PixelPhase1 Clusters: Ladder vs Module barrel summary',
                  'PixelPhase1/Layouts/25 - PixelPhase1 Cluster Occupancy: Ladder vs Module barrel summary',
                  'PixelPhase1/Layouts/28 - PixelPhase1 Digis: BladePanel vs Disk endcap summary',
                 # 'PixelPhase1/Layouts/29 - PixelPhase1 Clusters: BladePanel vs Disk endcap summary',
                  'PixelPhase1/Layouts/30 - PixelPhase1 Cluster Occupancy: BladePanel vs Disk endcap summary',
                  'PixelPhase1/Layouts/41 - ntracks',
                  'PixelPhase1/Layouts/32 - Charge and size',
                  'PixelPhase1/Layouts/33a - Cluster on track charge per Inner Ladders',
                  'PixelPhase1/Layouts/33b - Cluster on track charge per Outer Ladders',
                  'PixelPhase1/Layouts/33c - Cluster charge (on-track) per Disk',
                  #'PixelPhase1/Layouts/33 - Cluster on track and vertices per lumi',
                  'PixelPhase1/Layouts/34 -  Ontrack PXLayer',
                  'PixelPhase1/Layouts/35 - Ontrack Disk',
                  'PixelPhase1/Layouts/38 - PixelPhase1 Residuals',
                  #'PixelPhase1/Layouts/39a - ClusterSize Vs Eta (OnTrack) inner',
                 # 'PixelPhase1/Layouts/39b - ClusterSize Vs Eta (OnTrack) outer',
                 # 'PixelPhase1/Layouts/40a - Cluster size (on-track) per Ladders',
                 # 'PixelPhase1/Layouts/40b - Cluster size (on-track) per Disk',
                  'PixelPhase1/Layouts/31a - Dead Channels per ROC per Barrel Layer',
                  'PixelPhase1/Layouts/31b - Dead Channels per ROC per Forward Ring',
                )

server.workspace('DQMContent', 20, 'Tracker', 'Pixel', '^Pixel/', '',
                 'Pixel/Layouts/00b - Pixel_Error_Summary',
                 'Pixel/Layouts/01 - Pixel_FEDOccupancy_Summary',
                 'Pixel/Layouts/02 - Pixel_Cluster_Summary',
                 'Pixel/Layouts/03 - Pixel_Track_Summary',
                 'Pixel/Layouts/05 - Barrel OnTrack cluster positions',
                 'Pixel/Layouts/06 - Endcap OnTrack cluster positions',
                 'Pixel/Layouts/07 - Pixel_Digi_Summary',
                 'Pixel/Layouts/08 - ROC occupancies',
                 'Pixel/Layouts/09 - Pixel Clusters vs LS',
                )

server.workspace('DQMContent', 21, 'Tracker', 'SiStrip', '^SiStrip/', '',
                 'SiStrip/Layouts/00 - SiStrip ReportSummary',
                 'SiStrip/Layouts/01a - FED Errors vs FED ID',
                #'SiStrip/Layouts/01 - FED-Detected Errors Summary',
                #'SiStrip/Layouts/02 - FED-Detected Errors',
                 'SiStrip/Layouts/03 - # of Cluster Trend',
                 'SiStrip/Layouts/07 - OnTrackClusters(Total Number)',
                 'SiStrip/Layouts/04a - OnTrackCluster (StoN)',
                 'SiStrip/Layouts/04b - Cluster Charge per CM (On-Track)',
                 'SiStrip/Layouts/05 - OffTrackCluster (Total Number)',
                # 'SiStrip/Layouts/29 - Cluster & Digi occupancy per FED',
                )

server.workspace('DQMContent', 22, 'Tracker', 'Alignment', '', '',
                 'OfflinePV/AlignmentValidation/00 - Vertex and vertex tracks quality',
                 'OfflinePV/AlignmentValidation/01 - Impact parameters and errors',
                 'OfflinePV/AlignmentValidation/02 - Impact parameters projections (pT>1 GeV)',
                 'OfflinePV/AlignmentValidation/03 - Impact parameters projections (pT>10 GeV)',
                 'OfflinePV/AlignmentValidation/04 - 2D impact parameters projections',
                 'OfflinePV/AlignmentValidation/05 - Impact parameters error projections (pT>1 GeV)',
                 'OfflinePV/AlignmentValidation/06 - Impact parameters error projections (pT>10 GeV)',
                 'OfflinePV/AlignmentValidation/07 - 2D impact parameters error projections',
                 'PixelPhase1/Layouts/38 - PixelPhase1 Residuals',
                 'PixelPhase1/Layouts/38aa - Residuals x per Layer',
                 'PixelPhase1/Layouts/38ab - Residuals y per Layer',
                 'PixelPhase1/Layouts/38ba - Profile Residuals x PXBarrel',
                 'PixelPhase1/Layouts/38bb - Profile Residuals y PXBarrel',
                 'PixelPhase1/Layouts/38ca - Mean Residuals x inner Modules per Layer',
                 'PixelPhase1/Layouts/38cb - Mean Residuals x outer Modules per Layer',
                 'PixelPhase1/Layouts/38cc - Mean Residuals y inner Modules per Layer',
                 'PixelPhase1/Layouts/38cd - Mean Residuals y outer Modules per Layer',
                 'PixelPhase1/Layouts/38da - Residuals x per Disk',
                 'PixelPhase1/Layouts/38db - Residuals y per Disk',
                 'PixelPhase1/Layouts/38e - Profile Residuals PXFoward',
                 'PixelPhase1/Layouts/38fa - Mean Residuals InnerOuter Modules PXForward',
                 'PixelPhase1/Layouts/38fb - Mean Residuals pos.neg. Side PXForward',
                 'PixelPhase1/Layouts/42a - Barycenter coordinates',
                 'PixelPhase1/Layouts/42b - Barycenter coordinates',
                 'SiStrip/Layouts/21 - TIB Residuals',
                 'SiStrip/Layouts/22 - TOB Residuals',
                 'SiStrip/Layouts/23 - TID+ Residuals',
                 'SiStrip/Layouts/24 - TID- Residuals',
                 'SiStrip/Layouts/25 - TEC+ Residual',
                 'SiStrip/Layouts/26 - TEC- Residual',
                )

# Calorimeter workspaces:
server.workspace('DQMContent', 30, 'Calorimeters', 'Ecal', '^Ecal(|Barrel|Endcap)/', 'Ecal/Layouts',
                 'Ecal/Layouts/00 Summary',
                 'Ecal/Layouts/01 Occupancy Summary',
                )

server.workspace('DQMContent', 31, 'Calorimeters', 'EcalPreshower', '^EcalPreshower/', '',
                 'EcalPreshower/Layouts/01-IntegritySummary-EcalPreshower',
                 'EcalPreshower/Layouts/02-GoodRechitOccupancySummary-EcalPreshower',
                 'EcalPreshower/Layouts/03-GoodRechitEnergySummary-EcalPreshower',
                 'EcalPreshower/Layouts/04-ESTimingTaskSummary-EcalPreshower',
                 'EcalPreshower/Layouts/05-ESGain-EcalPreshower',
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
                 'Hcal/Layouts/15 DIGI Timing',
                 'Hcal/Layouts/18 RECO Energy',
                 'Hcal/Layouts/23 RECO Occupancy',
                 'Hcal/Layouts/24 RECO Occupancy Cut',
                 'Hcal/Layouts/28 RECO Timing',
                 'Hcal/Layouts/33 RECO HBHEabc Timing',
                 'Hcal/Layouts/34 RECO Timing vs Energy',
                 'Hcal/Layouts/35 TP Et Correlation',
                 'Hcal/Layouts/36 TP Et Correlation Ratio',
                 'Hcal/Layouts/38 TP Et Distribution',
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


# server.workspace('DQMContent', 34, 'Calorimeters', 'Castor', '^Castor/', '',
#                  'Castor/Layouts/01 - Map of frontend and readout errors',
#                  'Castor/Layouts/02 - Channel-wise timing',
#                  'Castor/Layouts/02b - Channel-wise timing (rms)',
#                  'Castor/Layouts/Digi/05 - DigiSize',
#                 )

# Muons workspaces:
server.workspace('DQMContent', 40, 'Muons', 'CSC', '^CSC/', '',
                 'CSC/Layouts/00 Data Integrity/Physics Efficiency 01',
                 'CSC/Layouts/00 Data Integrity/Physics Efficiency 02',
                 'CSC/Layouts/00 Data Integrity/Physics Efficiency 04 - CSCs Reporting Data and Unpacked',
                 'CSC/Layouts/00 Data Integrity/Physics Efficiency 08 - CSCs Occupancy Overal',
                 'CSC/Layouts/00 Data Integrity/Physics Efficiency 07 - CSCs Occupancy 2D',
                 'CSC/Layouts/00 Data Integrity/Physics Efficiency 09 - RecHits Minus',
                 'CSC/Layouts/00 Data Integrity/Physics Efficiency 10 - RecHits Plus',
                 'CSC/Layouts/00 Data Integrity/Physics Efficiency 11 - Segments',
                 'CSC/Layouts/00 Data Integrity/Physics Efficiency 12 - Timing',
                 'CSC/Layouts/00 Data Integrity/Physics Efficiency 13 - Tag-and-Probe Segments Efficiency'
                )

server.workspace('DQMContent', 41, 'Muons', 'DT', '^DT/', '')

server.workspace('DQMContent', 42, 'Muons', 'RPC', '^(RPC/|L1T/L1TStage2EMTF/rpc)', '')

server.workspace('DQMContent', 43, 'Muons', 'GEM', '^GEM/', '',
                 'GEM/Layouts/00 Summary Map',
                 'GEM/Layouts/01 GE11-M-L1 RecHit Occupancy',
                 'GEM/Layouts/02 GE11-M-L2 RecHit Occupancy',
                 'GEM/Layouts/03 GE11-P-L1 RecHit Occupancy',
                 'GEM/Layouts/04 GE11-P-L2 RecHit Occupancy',
                 'GEM/Layouts/05 GE11-M-L1 RecHit Average Cluster Size',
                 'GEM/Layouts/06 GE11-M-L2 RecHit Average Cluster Size',
                 'GEM/Layouts/07 GE11-P-L1 RecHit Average Cluster Size',
                 'GEM/Layouts/08 GE11-P-L2 RecHit Average Cluster Size',
                 'GEM/Layouts/09 GE11-M-L1 Chamber Efficiency',
                 'GEM/Layouts/10 GE11-M-L2 Chamber Efficiency',
                 'GEM/Layouts/11 GE11-P-L1 Chamber Efficiency',
                 'GEM/Layouts/12 GE11-P-L2 Chamber Efficiency',
                 'GEM/Layouts/13 GE11-M-L1 Eta Efficiency',
                 'GEM/Layouts/14 GE11-M-L2 Eta Efficiency',
                 'GEM/Layouts/15 GE11-P-L1 Eta Efficiency',
                 'GEM/Layouts/16 GE11-P-L2 Eta Efficiency',
                 'GEM/Layouts/17 GE11-M-E1 residual phi',
                 'GEM/Layouts/18 GE11-M-E2 residual phi',
                 'GEM/Layouts/19 GE11-M-E3 residual phi',
                 'GEM/Layouts/20 GE11-M-E4 residual phi',
                 'GEM/Layouts/21 GE11-M-E5 residual phi',
                 'GEM/Layouts/22 GE11-M-E6 residual phi',
                 'GEM/Layouts/23 GE11-M-E7 residual phi',
                 'GEM/Layouts/24 GE11-M-E8 residual phi',
                 'GEM/Layouts/25 GE11-P-E1 residual phi',
                 'GEM/Layouts/26 GE11-P-E2 residual phi',
                 'GEM/Layouts/27 GE11-P-E3 residual phi',
                 'GEM/Layouts/28 GE11-P-E4 residual phi',
                 'GEM/Layouts/29 GE11-P-E5 residual phi',
                 'GEM/Layouts/30 GE11-P-E6 residual phi',
                 'GEM/Layouts/31 GE11-P-E7 residual phi',
                 'GEM/Layouts/32 GE11-P-E8 residual phi',
                 'GEM/Layouts/33 GE21-P-L2 DIGI Occupancy',
                 )

# CTPPS workspaces:
server.workspace('DQMContent', 50, 'CTPPS', 'TrackingStrip', '^CTPPS/(TrackingStrip|common)/', 'CTPPS/TrackingStrip/Layouts')
server.workspace('DQMContent', 51, 'CTPPS', 'TrackingPixel', '^CTPPS/(TrackingPixel|common)/', 'CTPPS/TrackingPixel/Layouts')
server.workspace('DQMContent', 52, 'CTPPS', 'TimingDiamond', '^CTPPS/(TimingDiamond|common)/', 'CTPPS/TimingDiamond/Layouts')
server.workspace('DQMContent', 53, 'CTPPS', 'TimingFastSilicon', '^CTPPS/(TimingFastSilicon|common)/', 'CTPPS/TimingFastSilicon/Layouts')


# POG workspaces:
server.workspace('DQMContent', 60, 'POG', 'Muons', '^Muons/', '')

server.workspace('DQMContent', 61, 'POG', 'JetMet', '^JetMET/', '')

server.workspace('DQMContent', 62, 'POG', 'EGamma', '^Egamma/', '')

server.workspace('DQMContent', 63, 'POG', 'Btag', '^Btag/', '',
                 'Btag/Layouts/00 - Jet Properties',
                 'Btag/Layouts/01 - Tracks in Jet',
                 'Btag/Layouts/02 - Secondary Vertex Properties',
                 'Btag/Layouts/03 - Flight Distance Summary',
                 'Btag/Layouts/04 - Discriminator Summary',
                 'Btag/Layouts/05 - 2D-Impact Parameter',
                 'Btag/Layouts/06 - 3D-Impact Parameter',
                 'Btag/Layouts/07 - ROC Curves',
                )

server.workspace('DQMContent', 64, 'POG', 'Tracking', '^(Tracking|AlcaBeamMonitor|OfflinePV)/', '',
                 'Tracking/Layouts/01a - Summary',
                 'Tracking/Layouts/01b - Track Eta-Phi',
                 'Tracking/Layouts/02a - Tracks (pp collisions)',
                 'Tracking/Layouts/02b - Total Hits Strip and Pixel (pp collisions)',
                 'Tracking/Layouts/03 - Tracks (Cosmic Tracking)',
                 'Tracking/Layouts/04 - Tracking vs LS',
                 # 'Tracking/Layouts/05 - Number of Seeds (pp collisions)',
                 # 'Tracking/Layouts/06 - Tracks resolution',
                 'Tracking/Layouts/05 - Track pT and eta vs Quality',
                 'Tracking/Layouts/06a - Tracks Quality',
                 'Tracking/Layouts/06b - Tracks from Vertex',
                 'Tracking/Layouts/06c - Distance wrt Beam Spot'
                 # 'Tracking/Layouts/07 - Vertex reconstruction',
                 # 'Tracking/Layouts/08 - Tracking Efficiency',
                )

server.workspace('DQMContent', 65, 'POG', 'Tau', '^RecoTauV/', '',
                 'RecoTauV/Layouts/SingleMu/00aa - Fake rate from muons vs pt',
                 'RecoTauV/Layouts/SingleMu/00ab - Fake rate from muons vs pt',
                 'RecoTauV/Layouts/SingleMu/01a - Muon rejection fake rate vs pt',
                 'RecoTauV/Layouts/Jet/00aa - Fake rate from jets vs pt',
                 'RecoTauV/Layouts/Jet/00ab - Fake rate from jets vs pt',
                 'RecoTauV/Layouts/DoubleElectron_OR_TauPlusX/00aa - Fake rate from electrons vs pt',
                 'RecoTauV/Layouts/DoubleElectron_OR_TauPlusX/00ab - Fake rate from electrons vs pt',
                 'RecoTauV/Layouts/DoubleElectron_OR_TauPlusX/01a - Electron rejection fake rate vs pt',
                 'RecoTauV/Layouts/SingleMu/00ba - Fake rate from muons vs pileup',
                 'RecoTauV/Layouts/SingleMu/00bb - Fake rate from muons vs pileup',
                 'RecoTauV/Layouts/Jet/00ba - Fake rate from jets vs pileup',
                 'RecoTauV/Layouts/Jet/00bb - Fake rate from jets vs pileup',
                 'RecoTauV/Layouts/Jet/01e - Distributions of size and sumPt for isolation PF Cands, QCD Jets faking taus',
                 'RecoTauV/Layouts/Jet/01f - Distributions of Raw Quantities of Tau Cands, QCD Jets faking taus',
                 'RecoTauV/Layouts/Jet/01g - Distributions of Tau Cands Multiplicity, QCD Jets faking taus',
                 'RecoTauV/Layouts/Jet/01h - Distributions of Tau Cands pTRatio, QCD Jets faking taus',
                 'RecoTauV/Layouts/DoubleElectron_OR_TauPlusX/00ba - Fake rate from electrons vs pileup',
                 'RecoTauV/Layouts/DoubleElectron_OR_TauPlusX/00bb - Fake rate from electrons vs pileup',
                )
