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
                 'SiStrip/Layouts/01 - FED-Detected Errors Summary',
                 'SiStrip/Layouts/02 - FED-Detected Errors',
                 'SiStrip/Layouts/03 - # of Cluster Trend',
                 'SiStrip/Layouts/04 - OnTrackCluster (StoN)',
                 'SiStrip/Layouts/05 - OffTrackCluster (Total Number)',
                 'SiStrip/Layouts/06 - FED Errors vs FED ID',
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
server.workspace('DQMContent', 40, 'Muons', 'CSC', '^CSC/', '',
                 'CSC/Layouts/00 Data Integrity/Physics Efficiency 01',
                 'CSC/Layouts/00 Data Integrity/Physics Efficiency 02',
                 'CSC/Layouts/00 Data Integrity/Physics Efficiency 04 - CSCs Reporting Data and Unpacked',
                 'CSC/Layouts/00 Data Integrity/Physics Efficiency 08 - CSCs Occupancy Overal',
                 'CSC/Layouts/00 Data Integrity/Physics Efficiency 07 - CSCs Occupancy 2D',
                 'CSC/Layouts/00 Data Integrity/Physics Efficiency 09 - RecHits Minus',
                 'CSC/Layouts/00 Data Integrity/Physics Efficiency 10 - RecHits Plus',
                )

server.workspace('DQMContent', 41, 'Muons', 'DT', '^DT/', '')

server.workspace('DQMContent', 42, 'Muons', 'RPC', '^RPC/', '')

# CTPPS workspaces:
server.workspace('DQMContent', 50, 'CTPPS', 'TrackingStrip', '^CTPPS/', 'CTPPS/TrackingStrip/Layouts')

# POG workspaces:
server.workspace('DQMContent', 60, 'POG', 'Muons', '^Muons/', '')

server.workspace('DQMContent', 61, 'POG', 'JetMet', '^JetMET/', '')

server.workspace('DQMContent', 62, 'POG', 'EGamma', '^Egamma/', '')

server.workspace('DQMContent', 63, 'POG', 'Btag', '^Btag/', '',
                 'Btag/Layouts/00 - Jet Property',
                 'Btag/Layouts/01 - Tracks in Jet',
                 'Btag/Layouts/02 - Vertex Property',
                 'Btag/Layouts/03 - Flight Distance Summary',
                 'Btag/Layouts/04 - Discriminator Summary',
                 'Btag/Layouts/05 - 2D-Impact Parameter',
                 'Btag/Layouts/06 - 3D-Impact Parameter',
                )

server.workspace('DQMContent', 64, 'POG', 'Tracking', '^(Tracking|AlcaBeamMonitor|OfflinePV)/', '',
                 'Tracking/Layouts/01 - Tracking ReportSummary',
                 'Tracking/Layouts/02 - Tracks (pp collisions)',
                 'Tracking/Layouts/03 - Tracks (Cosmic Tracking)',
                 'Tracking/Layouts/04 - Tracks (HI run)',
                 'Tracking/Layouts/06 - Number of Seeds (pp collisions)',
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
