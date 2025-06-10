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

# Data workspaces:
server.workspace('DQMContent', 10, 'Data', 'Tk' , '^(Tk/|Pixel|SiStrip|Tracking|OfflinePV)', 'DataLayouts/Tk',
                 'DataLayouts/Tk/01 - TEC-',
                 'DataLayouts/Tk/02 - TEC+',
                 'DataLayouts/Tk/03 - TIB',
                 'DataLayouts/Tk/04 - TID-',
                 'DataLayouts/Tk/05 - TID+',
                 'DataLayouts/Tk/06 - TOB',
                 'DataLayouts/Tk/07 - Pixel Digis ADC Barrel',
                 'DataLayouts/Tk/08 - Pixel Digis ADC Endcap',
                 'DataLayouts/Tk/09 - Pixel Occupancy',
                 'DataLayouts/Tk/10 - PXBarrel OnTk Clusters Charge',
                 'DataLayouts/Tk/11 - PXEndcap OnTk Clusters Charge',
                 'DataLayouts/Tk/12 - PXBarrel OnTk Clusters Size',
                 'DataLayouts/Tk/13 - PXEndcap OnTk Clusters Size',
                )
server.workspace('DQMContent', 11, 'Data', 'Ecal' , '^Ecal.*/', 'DataLayouts/Ecal',
                 'DataLayouts/Ecal/04 Ecal Spectrum',
                 'DataLayouts/Ecal/00 Number of Ecal RecHits',
                 'DataLayouts/Ecal/08 Ecal Timing',
                )

server.workspace('DQMContent', 12, 'Data', 'Hcal' , '(^Hcal(|NoiseRatesD|RecHitsD)|^CaloTowersD)/', 'DataLayouts/Hcal')
server.workspace('DQMContent', 13, 'Data', 'DT' , '^DT/', '')
server.workspace('DQMContent', 14, 'Data', 'CSC' , '^CSC/', '')
server.workspace('DQMContent', 15, 'Data', 'RPC' , '^RPC/', '')
server.workspace('DQMContent', 16, 'Data', 'Tracking' , '^Tracking/', '')
server.workspace('DQMContent', 17, 'Data', 'L1T', '^L1T/', '')
server.workspace('DQMContent', 18, 'Data', 'L1TEMU', '^L1TEMU/', '')
server.workspace('DQMContent', 19, 'Data', 'HLT', '^HLT/', '')
server.workspace('DQMContent', 20, 'Data', 'Electron' , '^Electron/', '')
server.workspace('DQMContent', 21, 'Data', 'Photon' , '^Photon/', '')
server.workspace('DQMContent', 22, 'Data', 'Muon' , '^Muon/', '')
server.workspace('DQMContent', 23, 'Data', 'Jet' , '^Jet/', '')
server.workspace('DQMContent', 24, 'Data', 'MET' , '^MET/', '')
server.workspace('DQMContent', 25, 'Data', 'BTag' , '^BTag/', '')
server.workspace('DQMContent', 26, 'Data', 'Tau' , '^.*Tau.*/', 'RecoTauV/Layouts')
server.workspace('DQMContent', 27, 'Data', 'PFlow' , '^ParticleFlow/', '')
server.workspace('DQMContent', 28, 'Data', 'TkAlignment', '', 'DataLayouts/TkAli',
                 'DataLayouts/TkAli/00 - Vertex and vertex tracks quality',
                 'DataLayouts/TkAli/01 - Impact parameters and errors',
                 'DataLayouts/TkAli/02 - Impact parameters projections (pT>1 GeV)',
                 'DataLayouts/TkAli/03 - Impact parameters projections (pT>10 GeV)',
                 'DataLayouts/TkAli/04 - 2D impact parameters projections',
                 'DataLayouts/TkAli/38 - PixelPhase1 Residuals',
                 'DataLayouts/TkAli/38aa - Residuals x per Layer',
                 'DataLayouts/TkAli/38ab - Residuals y per Layer',
                 'DataLayouts/TkAli/38ba - Profile Residuals x PXBarrel',
                 'DataLayouts/TkAli/38bb - Profile Residuals y PXBarrel',
                 'DataLayouts/TkAli/38ca - Mean Residuals x inner Modules per Layer',
                 'DataLayouts/TkAli/38cb - Mean Residuals x outer Modules per Layer',
                 'DataLayouts/TkAli/38cc - Mean Residuals y inner Modules per Layer',
                 'DataLayouts/TkAli/38cd - Mean Residuals y outer Modules per Layer',
                 'DataLayouts/TkAli/38da - Residuals x per Disk',
                 'DataLayouts/TkAli/38db - Residuals y per Disk',
                 'DataLayouts/TkAli/38e - Profile Residuals PXFoward',
                 'DataLayouts/TkAli/38fa - Mean Residuals InnerOuter Modules PXForward',
                 'DataLayouts/TkAli/38fb - Mean Residuals pos.neg. Side PXForward',
                 'DataLayouts/TkAli/42a - Barycenter coordinates',
                 'DataLayouts/TkAli/42b - Barycenter coordinates',
                 'DataLayouts/TkAli/21 - TIB Residuals',
                 'DataLayouts/TkAli/22 - TOB Residuals',
                 'DataLayouts/TkAli/23 - TID+ Residuals',
                 'DataLayouts/TkAli/24 - TID- Residuals',
                 'DataLayouts/TkAli/25 - TEC+ Residual',
                 'DataLayouts/TkAli/26 - TEC- Residual',
                )

# Monte Carlo workspaces:
server.workspace('DQMContent', 30, 'Monte Carlo', 'MC Tk' , '^(Tk/|TrackerDigisV|TrackerHitsV|TrackerRecHitsV|Pixel|SiStrip|Tracking)', 'MCLayouts/Tk',
                 'MCLayouts/Tk/01 - TrackerDigisV',
                 'MCLayouts/Tk/02 - TrackerHitsV',
                 'MCLayouts/Tk/03 - TrackerRecHitsV',
                 'MCLayouts/Tk/04 - TrackingMCTruth',
                 'MCLayouts/Tk/05 - TrackingRecHits',
                )
server.workspace('DQMContent', 31, 'Monte Carlo', 'MC Tk Phase-2' , '^TrackerPhase2(OT|IT)(Cluster|L1Track|RecHit|Stub|TrackingRecHit)V', 'MCLayouts/Phase2Tk',
                 "MCLayouts/Phase2Tk/000 - IT Clusters Barrel Delta_X_Pixel",
                 "MCLayouts/Phase2Tk/001 - IT Clusters Barrel Delta_Y_Pixel",
                 "MCLayouts/Phase2Tk/002 - IT Clusters MINUS Endcap FPix Delta_X_Pixel",
                 "MCLayouts/Phase2Tk/003 - IT Clusters MINUS Endcap EPix Delta_X_Pixel",
                 "MCLayouts/Phase2Tk/004 - IT Clusters MINUS Endcap FPix Delta_Y_Pixel",
                 "MCLayouts/Phase2Tk/005 - IT Clusters MINUS Endcap EPix Delta_Y_Pixel",
                 "MCLayouts/Phase2Tk/006 - IT Clusters PLUS Endcap FPix Delta_X_Pixel",
                 "MCLayouts/Phase2Tk/007 - IT Clusters PLUS Endcap EPix Delta_X_Pixel",
                 "MCLayouts/Phase2Tk/008 - IT Clusters PLUS Endcap FPix Delta_Y_Pixel",
                 "MCLayouts/Phase2Tk/009 - IT Clusters PLUS Endcap EPix Delta_Y_Pixel",
                 "MCLayouts/Phase2Tk/100 - IT RecHit Barrel Delta_Y_vs_DeltaX",
                 "MCLayouts/Phase2Tk/101 - IT RecHit MINUS Endcap FPix Delta_Y_vs_DeltaX",
                 "MCLayouts/Phase2Tk/102 - IT RecHit MINUS Endcap EPix Delta_Y_vs_DeltaX",
                 "MCLayouts/Phase2Tk/103 - IT RecHit PLUS Endcap FPix Delta_Y_vs_DeltaX",
                 "MCLayouts/Phase2Tk/104 - IT RecHit PLUS Endcap EPix Delta_Y_vs_DeltaX",
                 "MCLayouts/Phase2Tk/200 - IT TrackingRecHit Barrel Delta_X",
                 "MCLayouts/Phase2Tk/201 - IT TrackingRecHit Barrel Delta_Y",
                 "MCLayouts/Phase2Tk/202 - IT TrackingRecHit MINUS Endcap FPix Delta_X",
                 "MCLayouts/Phase2Tk/203 - IT TrackingRecHit MINUS Endcap EPix Delta_X",
                 "MCLayouts/Phase2Tk/204 - IT TrackingRecHit MINUS Endcap FPix Delta_Y",
                 "MCLayouts/Phase2Tk/205 - IT TrackingRecHit MINUS Endcap EPix Delta_Y",
                 "MCLayouts/Phase2Tk/206 - IT TrackingRecHit PLUS Endcap FPix Delta_X",
                 "MCLayouts/Phase2Tk/207 - IT TrackingRecHit PLUS Endcap EPix Delta_X",
                 "MCLayouts/Phase2Tk/208 - IT TrackingRecHit PLUS Endcap FPix Delta_Y",
                 "MCLayouts/Phase2Tk/209 - IT TrackingRecHit PLUS Endcap EPix Delta_Y",
                 "MCLayouts/Phase2Tk/300 - OT Clusters Barrel Delta_X_Strip",
                 "MCLayouts/Phase2Tk/301 - OT Clusters Barrel Delta_Y_Strip",
                 "MCLayouts/Phase2Tk/302 - OT Clusters Barrel Delta_X_Pixel",
                 "MCLayouts/Phase2Tk/303 - OT Clusters Barrel Delta_Y_Pixel",
                 "MCLayouts/Phase2Tk/400 - OT RecHit Barrel Delta_X_Strip",
                 "MCLayouts/Phase2Tk/401 - OT RecHit Barrel Delta_Y_Strip",
                 "MCLayouts/Phase2Tk/402 - OT RecHit Barrel Delta_X_Pixel",
                 "MCLayouts/Phase2Tk/403 - OT RecHit Barrel Delta_Y_Pixel",
                 "MCLayouts/Phase2Tk/500 - OT TrackingRecHit Barrel Delta_X_Strip",
                 "MCLayouts/Phase2Tk/501 - OT TrackingRecHit Barrel Delta_Y_Strip",
                 "MCLayouts/Phase2Tk/502 - OT TrackingRecHit Barrel Delta_X_Pixel",
                 "MCLayouts/Phase2Tk/503 - OT TrackingRecHit Barrel Delta_Y_Pixel",
                 "MCLayouts/Phase2Tk/600 - OT L1Track Eta Efficiency and Resolution",
                 "MCLayouts/Phase2Tk/601 - OT L1Track Phi Resolution",
                 "MCLayouts/Phase2Tk/602 - OT L1Track Lxy Efficiency",
                 "MCLayouts/Phase2Tk/603 - OT L1Track d0 Efficiency and Resolution",
                 "MCLayouts/Phase2Tk/604 - OT L1Track z0 Efficiency and Resolution",
                 "MCLayouts/Phase2Tk/605 - OT Extended L1Track Displaced Eta Efficiency and Resolution",
                 "MCLayouts/Phase2Tk/606 - OT Extended L1Track Displaced Phi Resolution",
                 "MCLayouts/Phase2Tk/607 - OT Extended L1Track Displaced Lxy Efficiency",
                 "MCLayouts/Phase2Tk/608 - OT Extended L1Track Displaced d0 Efficiency and Resolution",
                 "MCLayouts/Phase2Tk/609 - OT Extended L1Track Prompt Eta Efficiency and Resolution",
                 "MCLayouts/Phase2Tk/610 - OT Extended L1Track Prompt Phi Resolution",
                 "MCLayouts/Phase2Tk/611 - OT Extended L1Track Prompt Lxy Efficiency",
                 "MCLayouts/Phase2Tk/612 - OT Extended L1Track Prompt d0 Efficiency and Resolution",)

server.workspace('DQMContent', 32, 'Monte Carlo', 'MC Ecal' , '^Ecal.*/', 'MCLayouts/Ecal')
server.workspace('DQMContent', 33, 'Monte Carlo', 'MC Hcal' , '(^Hcal(|NoiseRatesD|RecHitsD|DigisV|HitsV)|^CaloTowersD)/', 'MCLayouts/Hcal')
server.workspace('DQMContent', 34, 'Monte Carlo', 'MC DT' , '^DT/', '')
server.workspace('DQMContent', 35, 'Monte Carlo', 'MC CSC' , '^CSC/', '')
server.workspace('DQMContent', 36, 'Monte Carlo', 'MC RPC' , '^RPC/', '')
server.workspace('DQMContent', 37, 'Monte Carlo', 'MC Tracking' , '^Tracking/', '')
server.workspace('DQMContent', 38, 'Monte Carlo', 'MC L1T', '^L1T/', '')
server.workspace('DQMContent', 39, 'Monte Carlo', 'MC L1TEMU', '^L1TEMU/', '')
server.workspace('DQMContent', 40, 'Monte Carlo', 'MC HLT', '^HLT/', '')
server.workspace('DQMContent', 41, 'Monte Carlo', 'MC Electron' , '^Electron/', '')
server.workspace('DQMContent', 42, 'Monte Carlo', 'MC Photon' , '^Photon/', '')
server.workspace('DQMContent', 43, 'Monte Carlo', 'MC Muon' , '^Muon/', '')
server.workspace('DQMContent', 44, 'Monte Carlo', 'MC Jet' , '^Jet/', '')
server.workspace('DQMContent', 45, 'Monte Carlo', 'MC MET' , '^MET/', '')
server.workspace('DQMContent', 46, 'Monte Carlo', 'MC BTag' , '^BTag/', '')
server.workspace('DQMContent', 47, 'Monte Carlo', 'MC Tau' , '^.*Tau.*/', 'RecoTauV/Layouts')
server.workspace('DQMContent', 48, 'Monte Carlo', 'MC PFlow' , '^ParticleFlow/', 'MCLayouts/PFlow',
                 'MCLayouts/PFlow/01 - Jet Pt Resolution - Barrel',
                 'MCLayouts/PFlow/02 - Jet Pt Resolution - Endcap',
                 'MCLayouts/PFlow/03 - Jet Pt Resolution distribution - Barrel',
                 'MCLayouts/PFlow/04 - Jet Pt Resolution distribution - Endcap',
                )
