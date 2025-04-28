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
                 "MCLayouts/Phase2Tk/000 - IT Cluster Barrel X",
                 "MCLayouts/Phase2Tk/001 - IT Cluster Barrel Y",
                 "MCLayouts/Phase2Tk/002 - IT Cluster Endcap MINUS EPix X",
                 "MCLayouts/Phase2Tk/003 - IT Cluster Endcap MINUS EPix Y",
                 "MCLayouts/Phase2Tk/004 - IT Cluster Endcap MINUS FPix X",
                 "MCLayouts/Phase2Tk/005 - IT Cluster Endcap MINUS FPix Y",
                 "MCLayouts/Phase2Tk/006 - IT Cluster Endcap PLUS EPix X",
                 "MCLayouts/Phase2Tk/007 - IT Cluster Endcap PLUS EPix Y",
                 "MCLayouts/Phase2Tk/008 - IT Cluster Endcap PLUS FPix X",
                 "MCLayouts/Phase2Tk/009 - IT Cluster Endcap PLUS FPix Y",
                 "MCLayouts/Phase2Tk/100 - IT RecHit Barrel Delta Y v Delta X",
                 "MCLayouts/Phase2Tk/101 - IT RecHit Endcap MINUS EPix Delta Y v Delta X",
                 "MCLayouts/Phase2Tk/102 - IT RecHit Endcap MINUS FPix Delta Y v Delta X",
                 "MCLayouts/Phase2Tk/103 - IT RecHit Endcap PLUS EPix Delta Y v Delta X",
                 "MCLayouts/Phase2Tk/104 - IT RecHit Endcap PLUS FPix Delta Y v Delta X",
                 "MCLayouts/Phase2Tk/200 - IT TrackingRecHit Barrel X",
                 "MCLayouts/Phase2Tk/201 - IT TrackingRecHit Barrel Y",
                 "MCLayouts/Phase2Tk/202 - IT TrackingRecHit Endcap MINUS EPix X",
                 "MCLayouts/Phase2Tk/203 - IT TrackingRecHit Endcap MINUS EPix Y",
                 "MCLayouts/Phase2Tk/204 - IT TrackingRecHit Endcap MINUS FPix X",
                 "MCLayouts/Phase2Tk/205 - IT TrackingRecHit Endcap MINUS FPix Y",
                 "MCLayouts/Phase2Tk/206 - IT TrackingRecHit Endcap PLUS EPix X",
                 "MCLayouts/Phase2Tk/207 - IT TrackingRecHit Endcap PLUS EPix Y",
                 "MCLayouts/Phase2Tk/208 - IT TrackingRecHit Endcap PLUS FPix X",
                 "MCLayouts/Phase2Tk/209 - IT TrackingRecHit Endcap PLUS FPix Y",
                 "MCLayouts/Phase2Tk/300 - OT Cluster Barrel Pixel X",
                 "MCLayouts/Phase2Tk/301 - OT Cluster Barrel Pixel Y",
                 "MCLayouts/Phase2Tk/302 - OT Cluster Barrel Strip X",
                 "MCLayouts/Phase2Tk/303 - OT Cluster Barrel Strip Y",
                 "MCLayouts/Phase2Tk/304 - OT Cluster Endcap MINUS TEDD1 Pixel and Strip XY",
                 "MCLayouts/Phase2Tk/305 - OT Cluster Endcap MINUS TEDD2 Pixel and Strip XY",
                 "MCLayouts/Phase2Tk/306 - OT Cluster Endcap PLUS TEDD1 Pixel and Strip XY",
                 "MCLayouts/Phase2Tk/307 - OT Cluster Endcap PLUS TEDD2 Pixel and Strip XY",
                 "MCLayouts/Phase2Tk/400 - OT L1Track Eta Efficiency and Resolution",
                 "MCLayouts/Phase2Tk/401 - OT L1Track Phi Efficiency and Resolution",
                 "MCLayouts/Phase2Tk/402 - OT L1Track Lxy Efficiency and Resolution",
                 "MCLayouts/Phase2Tk/403 - OT L1Track d0 Efficiency and Resolution",
                 "MCLayouts/Phase2Tk/404 - OT Extended L1Track Displaced Eta Efficiency and Resolution",
                 "MCLayouts/Phase2Tk/405 - OT Extended L1Track Displaced Phi Efficiency and Resolution",
                 "MCLayouts/Phase2Tk/406 - OT Extended L1Track Displaced Lxy Efficiency and Resolution",
                 "MCLayouts/Phase2Tk/407 - OT Extended L1Track Displaced d0 Efficiency and Resolution",
                 "MCLayouts/Phase2Tk/408 - OT Extended L1Track Prompt Eta Efficiency and Resolution",
                 "MCLayouts/Phase2Tk/409 - OT Extended L1Track Prompt Phi Efficiency and Resolution",
                 "MCLayouts/Phase2Tk/410 - OT Extended L1Track Prompt Lxy Efficiency and Resolution",
                 "MCLayouts/Phase2Tk/411 - OT Extended L1Track Prompt d0 Efficiency and Resolution",
                 "MCLayouts/Phase2Tk/500 - OT RecHit Barrel Pixel X",
                 "MCLayouts/Phase2Tk/501 - OT RecHit Barrel Pixel Y",
                 "MCLayouts/Phase2Tk/502 - OT RecHit Barrel Strip X",
                 "MCLayouts/Phase2Tk/503 - OT RecHit Barrel Strip Y",
                 "MCLayouts/Phase2Tk/504 - OT RecHit Endcap MINUS TEDD1 Pixel and Strip XY",
                 "MCLayouts/Phase2Tk/505 - OT RecHit Endcap MINUS TEDD2 Pixel and Strip XY",
                 "MCLayouts/Phase2Tk/506 - OT RecHit Endcap PLUS TEDD1 Pixel and Strip XY",
                 "MCLayouts/Phase2Tk/507 - OT RecHit Endcap PLUS TEDD2 Pixel and Strip XY")

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
