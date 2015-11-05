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
server.workspace('DQMCertification', 3, 'Summaries', 'Certification')
server.workspace('DQMContent', 4, 'Summaries', 'Everything', '^', '^')

# Tracker/Muons workspaces:
server.workspace('DQMContent', 10, 'Tracker/Muons', 'Pixel', '^Pixel/', '')
server.workspace('DQMContent', 11, 'Tracker/Muons', 'SiStrip', '^SiStrip/', '')
server.workspace('DQMContent', 12, 'Tracker/Muons', 'CSC', '^CSC/', '')
server.workspace('DQMContent', 13, 'Tracker/Muons', 'DT', '^DT/', '')
server.workspace('DQMContent', 14, 'Tracker/Muons', 'RPC', '^RPC/', '')
server.workspace('DQMContent', 15, 'Tracker/Muons', 'SiStripLAS', '^SiStripLAS/', '')

# Calorimeter workspaces:
server.workspace('DQMContent', 21, 'Calorimeter', 'Ecal', '^Ecal(|Barrel|Endcap|Calibration)/', '')
server.workspace('DQMContent', 22, 'Calorimeter', 'EcalPreshower', '^EcalPreshower', '')
server.workspace('DQMContent', 23, 'Calorimeter', 'HCAL', '^Hcal/', '')
server.workspace('DQMContent', 24, 'Calorimeter', 'CASTOR', '^Castor/', '')
server.workspace('DQMContent', 25, 'Calorimeter', 'HCALcalib', '^HcalCalib/', '')

# Trigger/Lumi workspaces:
server.workspace('DQMContent', 31, 'Trigger/Lumi', 'L1T', '^L1T/', '')
server.workspace('DQMContent', 32, 'Trigger/Lumi', 'L1TEMU', '^L1TEMU/', '')
server.workspace('DQMContent', 33, 'Trigger/Lumi', 'HLT', '^HLT/', '')

# POG workspaces:
server.workspace('DQMContent', 41, 'POG', 'Muons', '^Muons/', '')
server.workspace('DQMContent', 42, 'POG', 'JetMet', '^JetMET/', '')
server.workspace('DQMContent', 43, 'POG', 'EGamma', '^Egamma/', '')
