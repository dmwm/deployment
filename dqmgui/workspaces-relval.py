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
                 "MCLayouts/Phase2Tk/00 - IT Cluster Barrel X",
                 "MCLayouts/Phase2Tk/01 - IT Cluster Barrel Y",
                 "MCLayouts/Phase2Tk/02 - IT Cluster Endcap MINUS EPix X",
                 "MCLayouts/Phase2Tk/03 - IT Cluster Endcap MINUS EPix Y",
                 "MCLayouts/Phase2Tk/04 - IT Cluster Endcap MINUS FPix X",
                 "MCLayouts/Phase2Tk/05 - IT Cluster Endcap MINUS FPix Y",
                 "MCLayouts/Phase2Tk/06 - IT Cluster Endcap PLUS EPix X",
                 "MCLayouts/Phase2Tk/07 - IT Cluster Endcap PLUS EPix Y",
                 "MCLayouts/Phase2Tk/08 - IT Cluster Endcap PLUS FPix X",
                 "MCLayouts/Phase2Tk/09 - IT Cluster Endcap PLUS FPix Y",
                 "MCLayouts/Phase2Tk/10 - IT RecHit Barrel Delta Y v Delta X",
                 "MCLayouts/Phase2Tk/11 - IT RecHit Endcap MINUS EPix Delta Y v Delta X",
                 "MCLayouts/Phase2Tk/12 - IT RecHit Endcap MINUS FPix Delta Y v Delta X",
                 "MCLayouts/Phase2Tk/13 - IT RecHit Endcap PLUS EPix Delta Y v Delta X",
                 "MCLayouts/Phase2Tk/14 - IT RecHit Endcap PLUS FPix Delta Y v Delta X",
                 "MCLayouts/Phase2Tk/20 - IT TrackingRecHit Barrel X",
                 "MCLayouts/Phase2Tk/21 - IT TrackingRecHit Barrel Y",
                 "MCLayouts/Phase2Tk/22 - IT TrackingRecHit Endcap MINUS EPix X",
                 "MCLayouts/Phase2Tk/23 - IT TrackingRecHit Endcap MINUS EPix Y",
                 "MCLayouts/Phase2Tk/24 - IT TrackingRecHit Endcap MINUS FPix X",
                 "MCLayouts/Phase2Tk/25 - IT TrackingRecHit Endcap MINUS FPix Y",
                 "MCLayouts/Phase2Tk/26 - IT TrackingRecHit Endcap PLUS EPix X",
                 "MCLayouts/Phase2Tk/27 - IT TrackingRecHit Endcap PLUS EPix Y",
                 "MCLayouts/Phase2Tk/28 - IT TrackingRecHit Endcap PLUS FPix X",
                 "MCLayouts/Phase2Tk/29 - IT TrackingRecHit Endcap PLUS FPix Y",
                 "MCLayouts/Phase2Tk/30 - OT Cluster Barrel Pixel X",
                 "MCLayouts/Phase2Tk/31 - OT Cluster Barrel Pixel Y",
                 "MCLayouts/Phase2Tk/32 - OT Cluster Barrel Strip X",
                 "MCLayouts/Phase2Tk/33 - OT Cluster Barrel Strip Y",
                 "MCLayouts/Phase2Tk/34 - OT Cluster Endcap MINUS TEDD1 Pixel/StripXY",
                 "MCLayouts/Phase2Tk/35 - OT Cluster Endcap MINUS TEDD2 Pixel/StripXY",
                 "MCLayouts/Phase2Tk/36 - OT Cluster Endcap PLUS TEDD1 Pixel/StripXY",
                 "MCLayouts/Phase2Tk/37 - OT Cluster Endcap PLUS TEDD2 Pixel/StripXY",
                 "MCLayouts/Phase2Tk/40 - OT L1Track Eta Efficiency/Resolution",
                 "MCLayouts/Phase2Tk/41 - OT L1Track Phi Efficiency/Resolution",
                 "MCLayouts/Phase2Tk/42 - OT L1Track VtxZ Efficiency/Resolution",
                 "MCLayouts/Phase2Tk/43 - OT L1Track d0 Efficiency/Resolution",
                 "MCLayouts/Phase2Tk/44 - OT Extended L1Track Displaced Eta Efficiency/Resolution",
                 "MCLayouts/Phase2Tk/45 - OT Extended L1Track Displaced Phi Efficiency/Resolution",
                 "MCLayouts/Phase2Tk/46 - OT Extended L1Track Displaced VtxZ Efficiency/Resolution",
                 "MCLayouts/Phase2Tk/47 - OT Extended L1Track Displaced d0 Efficiency/Resolution",
                 "MCLayouts/Phase2Tk/48 - OT Extended L1Track Prompt Eta Efficiency/Resolution",
                 "MCLayouts/Phase2Tk/49 - OT Extended L1Track Prompt Phi Efficiency/Resolution",
                 "MCLayouts/Phase2Tk/410 - OT Extended L1Track Prompt VtxZ Efficiency/Resolution",
                 "MCLayouts/Phase2Tk/411 - OT Extended L1Track Prompt d0 Efficiency/Resolution",
                 "MCLayouts/Phase2Tk/50 - OT RecHit Barrel Pixel X",
                 "MCLayouts/Phase2Tk/51 - OT RecHit Barrel Pixel Y",
                 "MCLayouts/Phase2Tk/52 - OT RecHit Barrel Strip X",
                 "MCLayouts/Phase2Tk/53 - OT RecHit Barrel Strip Y",
                 "MCLayouts/Phase2Tk/54 - OT RecHit Endcap MINUS TEDD1 Pixel/StripXY",
                 "MCLayouts/Phase2Tk/55 - OT RecHit Endcap MINUS TEDD2 Pixel/StripXY",
                 "MCLayouts/Phase2Tk/56 - OT RecHit Endcap PLUS TEDD1 Pixel/StripXY",
                 "MCLayouts/Phase2Tk/57 - OT RecHit Endcap PLUS TEDD2 Pixel/StripXY")

server.workspace('DQMContent', 31, 'Monte Carlo', 'MC Ecal' , '^Ecal.*/', 'MCLayouts/Ecal')
server.workspace('DQMContent', 32, 'Monte Carlo', 'MC Hcal' , '(^Hcal(|NoiseRatesD|RecHitsD|DigisV|HitsV)|^CaloTowersD)/', 'MCLayouts/Hcal')
server.workspace('DQMContent', 33, 'Monte Carlo', 'MC DT' , '^DT/', '')
server.workspace('DQMContent', 34, 'Monte Carlo', 'MC CSC' , '^CSC/', '')
server.workspace('DQMContent', 35, 'Monte Carlo', 'MC RPC' , '^RPC/', '')
server.workspace('DQMContent', 36, 'Monte Carlo', 'MC Tracking' , '^Tracking/', '')
server.workspace('DQMContent', 37, 'Monte Carlo', 'MC L1T', '^L1T/', '')
server.workspace('DQMContent', 38, 'Monte Carlo', 'MC L1TEMU', '^L1TEMU/', '')
server.workspace('DQMContent', 39, 'Monte Carlo', 'MC HLT', '^HLT/', '')
server.workspace('DQMContent', 40, 'Monte Carlo', 'MC Electron' , '^Electron/', '')
server.workspace('DQMContent', 41, 'Monte Carlo', 'MC Photon' , '^Photon/', '')
server.workspace('DQMContent', 42, 'Monte Carlo', 'MC Muon' , '^Muon/', '')
server.workspace('DQMContent', 43, 'Monte Carlo', 'MC Jet' , '^Jet/', '')
server.workspace('DQMContent', 44, 'Monte Carlo', 'MC MET' , '^MET/', '')
server.workspace('DQMContent', 45, 'Monte Carlo', 'MC BTag' , '^BTag/', '')
server.workspace('DQMContent', 46, 'Monte Carlo', 'MC Tau' , '^.*Tau.*/', 'RecoTauV/Layouts')
server.workspace('DQMContent', 47, 'Monte Carlo', 'MC PFlow' , '^ParticleFlow/', 'MCLayouts/PFlow',
                 'MCLayouts/PFlow/01 - Jet Pt Resolution - Barrel',
                 'MCLayouts/PFlow/02 - Jet Pt Resolution - Endcap',
                 'MCLayouts/PFlow/03 - Jet Pt Resolution distribution - Barrel',
                 'MCLayouts/PFlow/04 - Jet Pt Resolution distribution - Endcap',
                )
