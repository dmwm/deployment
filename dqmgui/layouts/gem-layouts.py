def GEMLayout(i, p, *rows): i["GEM/Layouts/" + p] = DQMItem(layout=rows)
#def GEMLayout(i, p, *rows): return 1 # this line and the following one line is for printing out indices
#dqmitems = ""

#GEMLayout(dqmitems, "0 eta", [{'path' : "GEM/eta", 'description': 'eta recHit'}])
#GEMLayout(dqmitems, "1 phi", [{'path' : "GEM/phi", 'description': 'phi recHit'}])

# StatusDigi
GEMLayout(dqmitems, "00 StatusDigi Critical Errors", 
    [{'path' : "GEM/StatusDigi/GEB_Errors", 
    'description': 'Critical errors on GEM'}])

GEMLayout(dqmitems, "01 StatusDigi Warnings", 
    [{'path' : "GEM/StatusDigi/GEB_Warnings", 
    'description': 'Warnings on GEM'}])

GEMLayout(dqmitems, "01 StatusDigi VFAT Error all", 
    [{'path' : "GEM/StatusDigi/vfatErrors_all_CRC", 
    'description': 'CRC (all) in StatusDigi'}, 
    {'path' : "GEM/StatusDigi/vfatErrors_all_flag", 
    'description': 'Flag (all) in StatusDigi'}], 
    [{'path' : "GEM/StatusDigi/vfatErrors_all_b1010", 
    'description': 'Control bit 1010 (all) in StatusDigi'}, 
    {'path' : "GEM/StatusDigi/vfatErrors_all_b1100", 
    'description': 'Control bit 1100 (all) in StatusDigi'}, 
    {'path' : "GEM/StatusDigi/vfatErrors_all_b1110", 
    'description': 'Control bit 1110 (all) in StatusDigi'}])

layers = ["1", "2"]
#Geminis = ["671093248", "671095040", "671095296", "671095552", "671095808"]
Geminis = ["671088640", "671095296", "671095552", "671095808", "671096064"]
GeminisId = ["1", "27", "28", "29", "30"]
index = 2

for i, gemini in enumerate(Geminis):
  for layer in layers:
    """
    recHit = "GEM/recHit/recHit_Gemini_" + GeminisId[ i ] + "_la_" + layer
    VFAT = "GEM/recHit/VFAT_vs_ClusterSize_Gemini_" + GeminisId[ i ] + "_la_" + layer
    Fired = "GEM/recHit/StripFired_Gemini_" + GeminisId[ i ] + "_la_" + layer
    Digi = "GEM/digi/Digi_Strips_Gemini_" + gemini + "_la_" + layer
    
    GEMLayout(dqmitems, "%02i GEMINI%02ila%s"%(index, int(GeminisId[ i ]), layer), 
      [{'path': recHit, 'description': "Number of recHit per VFAT (!!!)"},
        {'path': VFAT, 'description': "VFAT cs ClusterSize"}],
      [{'path': Fired, 'description': "Number of Fired Strips"},
        {'path': Digi, 'description': "Number of Digi Strips"}])  
    """
    strPathDigiVFAT   = "GEM/digi/Digi_Strips_Gemini_%s_l_%s_VFAT"%(GeminisId[ i ], layer)
    strPathDigiStrip  = "GEM/digi/Digi_Strips_Gemini_%s_l_%s"%(GeminisId[ i ], layer)
    strPathRHCLSize   = "GEM/recHit/VFAT_vs_ClusterSize_Gemini_%s_la_%s"%(GeminisId[ i ], layer)
    strPathRHHitX     = "GEM/recHit/recHit_x_Gemini_%s_la_%s"%(GeminisId[ i ], layer)
    
    GEMLayout(dqmitems, "%02i GEMINI%02ila%s"%(index, int(GeminisId[ i ]), layer), 
      [{'path': strPathDigiVFAT, 'description': "Number of VFAT"},
        {'path': strPathDigiStrip, 'description': "Number of Digi Strips"}],
      [{'path': strPathRHCLSize, 'description': "VFAT vs ClusterSize"},
        {'path': strPathRHHitX, 'description': "Number on hit x"}])  
    
    index += 1


