def GEMLayout(i, p, *rows): i["GEM/Layouts/" + p] = DQMItem(layout=rows)
#def GEMLayout(i, p, *rows): return 1 # this line and the following one line is for printing out indices


nIdx = 0

GEMLayout(dqmitems, "%02i Summary"%nIdx, 
    [{"path" : "GEM/EventInfo/reportSummaryMap", 
    "description": 'For more information (... under construction)'}])
nIdx += 1

GEMLayout(dqmitems, "%02i AMC status"%nIdx, 
    [{"path" : "GEM/StatusDigi/amc_statusflag", 
    "description": 'For more information (... under construction)'}])
nIdx += 1

# StatusDigi
GEMLayout(dqmitems, "%02i GEB input status"%nIdx, 
    [
      {"path": "GEM/StatusDigi/geb_input_status_st_m1_la_1", "description": "GEB input status in GE-1/1"}, 
      {"path": "GEM/StatusDigi/geb_input_status_st_m1_la_2", "description": "GEB input status in GE-1/2"}, 
    ], 
    [
      {"path": "GEM/StatusDigi/geb_input_status_st_p1_la_1", "description": "GEB input status in GE+1/1"}, 
      {"path": "GEM/StatusDigi/geb_input_status_st_p1_la_2", "description": "GEB input status in GE+1/2"}, 
    ])
nIdx += 1

listLayers = ["p1_1", "p1_2", "m1_1", "m1_2"]

for layer in listLayers: 
  strTitle = "%s%s%s"%("+" if layer[ 0 ] == "p" else "-", layer[ 1 ], layer[ 3 ])
  GEMLayout(dqmitems, "%02i Global position GE%s"%(nIdx, strTitle), 
      [{"path": "GEM/recHit/recHit_globalPos_Gemini_GE" + layer, 
        "description": "Global position"}])
  nIdx += 1


#Geminis = ["671093248", "671095040", "671095296", "671095552", "671095808"]
#Geminis = ["671088640", "671095296", "671095552", "671095808", "671096064"]
#GeminisId = ["1", "11", "13", "15", "17", "19", "27", "28", "29", "30"]
#GeminisId = ["11", "13", "15", "17", "19"]
#nIdx = 3
layers = ["p1_1", "p1_2", "m1_1", "m1_2"]
GeminisId = [ i + 1 for i in range(30) ]

for i, gemini in enumerate(GeminisId):
  for layer in layers:
    strID = "Gemini_%i_GE%s"%(gemini, layer)
    strLayerLabel = "GE%s%s%s"%("+" if layer[ 0 ] == "p" else "-", layer[ 1 ], layer[ 3 ])
    
    strPathVFATStatus = "GEM/StatusDigi/vfatStatus_QualityFlag_" + strID
    strPathBxCross    = "GEM/StatusDigi/vfatStatus_BC_" + strID
    strPathEvtCounter = "GEM/StatusDigi/vfatStatus_EC_" + strID
    strPathDigiStrip  = "GEM/digi/Digi_Strips_" + strID
    strPathRHCLSize   = "GEM/recHit/VFAT_vs_ClusterSize_" + strID
    strPathRHHitX     = "GEM/recHit/recHit_x_" + strID
    
    GEMLayout(dqmitems, "%02i GEMINI%02i_%s"%(nIdx, int(GeminisId[ i ]), strLayerLabel), 
      [{'path': strPathVFATStatus, 'description': "VFAT quality"},
       {'path': strPathBxCross,    'description': "Bunch crossing"}, 
       {'path': strPathEvtCounter, 'description': "Event counter"}],
      [{'path': strPathDigiStrip,  'description': "Number of Digi Strips"}, 
       {'path': strPathRHCLSize,   'description': "VFAT vs ClusterSize"}])
    
    nIdx += 1


