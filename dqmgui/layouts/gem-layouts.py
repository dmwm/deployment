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


GeminisId = [ i + 1 for i in range(36) ]
listLayers = ["p1_1", "p1_2", "m1_1", "m1_2"]
listLayersWithTitle = [ [ s, "GE%s%s%s"%("+" if s[ 0 ] == "p" else "-", s[ 1 ], s[ 3 ]) ] for s in listLayers ]
strTitleFmt = "%02i GEMINI%02i_%s"
bIsLayerWise = True
bIsGlobalPos = True


if bIsGlobalPos: 
  for layer in listLayersWithTitle: 
    GEMLayout(dqmitems, "%02i Global position %s"%(nIdx, layer[ 1 ]), 
        [{"path": "GEM/recHit/recHit_globalPos_Gemini_GE" + layer[ 0 ], 
          "description": "Global position"}])
    nIdx += 1

listGEMChambers = []

if bIsLayerWise: 
  for layer in listLayersWithTitle:
    for gemini in GeminisId:
      listGEMChambers.append([gemini, layer])
else: 
  for gemini in GeminisId:
    for layer in listLayersWithTitle:
      listGEMChambers.append([gemini, layer])

for itCh in listGEMChambers: 
  gemini = itCh[ 0 ]
  layer  = itCh[ 1 ]
  
  strID = "Gemini_%i_GE%s"%(gemini, layer[ 0 ])
  
  strPathVFATStatus = "GEM/StatusDigi/vfatStatus_QualityFlag_" + strID
  strPathBxCross    = "GEM/StatusDigi/vfatStatus_BC_" + strID
  strPathEvtCounter = "GEM/StatusDigi/vfatStatus_EC_" + strID
  strPathDigiStrip  = "GEM/digi/Digi_Strips_" + strID
  strPathRHCLSize   = "GEM/recHit/VFAT_vs_ClusterSize_" + strID
  strPathRHHitX     = "GEM/recHit/recHit_x_" + strID
  
  GEMLayout(dqmitems, strTitleFmt%(nIdx, gemini, layer[ 1 ]), 
    [{'path': strPathVFATStatus, 'description': "VFAT quality"},
     {'path': strPathBxCross,    'description': "Bunch crossing"}, 
     {'path': strPathEvtCounter, 'description': "Event counter"}],
    [{'path': strPathDigiStrip,  'description': "Number of Digi Strips"}, 
     {'path': strPathRHCLSize,   'description': "VFAT vs ClusterSize"}])
  
  nIdx += 1


