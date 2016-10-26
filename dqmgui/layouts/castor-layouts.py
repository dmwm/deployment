def castorlayout(i, p, *rows):
    i["Castor/Layouts/" + p] = DQMItem(layout=rows)

# BVB 20160316: Removed Castor from the shift layouts (there are no instructions
#               and as far as we know Castor will not be in before the HI run at
#               the end of the year). We leave the expert workspace for what it
#               is.

castorlayout(dqmitems, "01 - Map of frontend and readout errors",
           [{ 'path': "Castor/CastorDigiMonitor/CASTOR QIE_capID+er+dv",
             'description':"Frontend and readout errors"}]
           )

castorlayout(dqmitems, "02 - Channel-wise timing",
           [{ 'path': "Castor/CastorDigiMonitor/QfC=f(x=Tile y=TS) (cumulative)",
             'description':"Channel-wise timing"}]
           )
castorlayout(dqmitems, "02b - Channel-wise timing (rms)",
           [{ 'path': "Castor/CastorDigiMonitor/QrmsfC=f(Tile TS)",
             'description':"Channel-wise timing (rms)"}]
           )

castorlayout(dqmitems, "RECO/01 - CASTOR Jet Energy",
           [{ 'path': "Castor/CastorRecHitMonitor/CASTORJetEnergy",
             'description':"CASTORJetEnergy",
		'draw': { 'ytype':'log' } }]
           )
castorlayout(dqmitems, "RECO/02 - CASTOR Jet Eta",
           [{ 'path': "Castor/CastorRecHitMonitor/CASTORJetEta",
             'description':"CASTOR Jet Eta"}]
           )
castorlayout(dqmitems, "RECO/03 - CASTOR Jet Phi",
           [{ 'path': "Castor/CastorRecHitMonitor/CASTORJetPhi",
             'description':"CASTORJetPhi"}]
           )
castorlayout(dqmitems, "RECO/04 - CASTOR Jets Multiplicity",
           [{ 'path': "Castor/CastorRecHitMonitor/CASTORJetsMultiplicity",
             'description':"CASTORJetsMultiplicity"}]
           )

castorlayout(dqmitems, "RECO/05 - CASTOR Towers Multiplicity",
           [{ 'path': "Castor/CastorRecHitMonitor/CASTORTowerMultiplicity",
             'description':"CASTOR Tower Multiplicity"}]
           )

castorlayout(dqmitems, "RECO/06 - CASTOR Tower Depth",
           [{ 'path': "Castor/CastorRecHitMonitor/CASTORTowerDepth",
             'description':"CASTORTowerDepth"}]
           )

castorlayout(dqmitems, "RECO/07 - Tower Total Energy (EM + HAD)",
           [{ 'path': "Castor/CastorRecHitMonitor/CASTORTowerTotalEnergy",
             'description':"CASTORTowerTotalEnergy",
		'draw': { 'ytype':'log' } }]
           )

castorlayout(dqmitems, "RECO/08 - Tower EM vs HAD",
           [{ 'path': "Castor/CastorRecHitMonitor/CASTORTowerEMvsEhad",
             'description':"CASTOR Tower EM vs Ehad",
 'draw': { 'xtype': 'log', 'ytype':'log', 'drawopts': "COLZ" } }]
           )

castorlayout(dqmitems, "RECO/09 - Cells Energy profile(GeV)",
           [{ 'path': "Castor/CastorRecHitMonitor/CastorTileRecHit",
             'description':"CastorTileRecHit",
		'draw': { 'ytype':'log' } }]
           )

castorlayout(dqmitems, "RECO/10 - Map: cells average Energy per event",
           [{ 'path': "Castor/CastorRecHitMonitor/CastorRecHitOccMap",
             'description':"Map of rechit occupancies"}]
           )

castorlayout(dqmitems, "RECO/11 - Energy(EM + HAD) by Sectors",
           [{ 'path': "Castor/CastorRecHitMonitor/CastorRecHit by Sectors",
             'description':"CastorRecHit by Sectors",
		'draw': { 'ytype':'log' } }]
           )

castorlayout(dqmitems, "RECO/12 - Castor Total Energy",
           [{ 'path': "Castor/CastorRecHitMonitor/Reco all tiles",
             'description':"Reco all tiles",
		'draw': { 'ytype':'log' } }]
           )

castorlayout(dqmitems, "RECO/13 - Rec Hits Time",
           [{ 'path': "Castor/CastorRecHitMonitor/CastorRecHitTime",
             'description':"CastorRecHitTime",
		'draw': { 'ytype':'log' } }]
           )


# Digi folder
castorlayout(dqmitems, "Digi/01 - CASTORreportSummaryMap",
           [{ 'path': "Castor/CastorDigiMonitor/CASTORreportSummaryMap",
             'description':"CASTORreportSummaryMap"}]
           )

castorlayout(dqmitems, "Digi/02 - CASTOR DeadChannelsMap",
           [{ 'path': "Castor/CastorDigiMonitor/CASTOR DeadChannelsMap",
             'description':"CASTOR DeadChannelsMap"}]
           )

castorlayout(dqmitems, "Digi/03 - CASTOR TSmax Significance Map",
           [{ 'path': "Castor/CastorDigiMonitor/CASTOR TSmax Significance Map",
             'description':"CASTOR TSmax Significance Map"}]
           )
castorlayout(dqmitems, "Digi/04 - CASTOR TSmax Significance All chan",
           [{ 'path': "Castor/CastorDigiMonitor/CASTOR TSmax Significance All chan",
             'description':"CASTOR TSmax Significance All chan",
		'draw': { 'ytype':'log' } }]
           )
castorlayout(dqmitems, "Digi/05 - DigiSize",
           [{ 'path': "Castor/CastorDigiMonitor/DigiSize",
             'description':"CASTOR DigiSize",
		'draw': { 'ytype':'log' } }]
           )

castorlayout(dqmitems, "Digi/06 - ModuleZ(fC)_allTS",
           [{ 'path': "Castor/CastorDigiMonitor/ModuleZ(fC)_allTS",
             'description':"ModuleZ(fC)_allTS"}]
           )
castorlayout(dqmitems, "Digi/07 - Sector #phi(fC)_all TS",
           [{ 'path': "Castor/CastorDigiMonitor/Sector #phi(fC)_allTS",
             'description':"Sector #phi(fC)_all TS"}]
           )
castorlayout(dqmitems, "Digi/08 - QfC=f(x=Cell y=TS) (cumulative)",
           [{ 'path': "Castor/CastorDigiMonitor/QfC=f(x=Tile y=TS) (cumulative)",
             'description':"QfC=f(x=Tile y=TS) (cumulative)" }]
           )
castorlayout(dqmitems, "Digi/09 - QmeanfC=f(Cell, TS)",
           [{ 'path': "Castor/CastorDigiMonitor/QmeanfC=f(Tile TS)",
             'description':"QmeanfC=f(Tile TS)"}]
           )

castorlayout(dqmitems, "Digi/10 - QrmsfC=f(Cell, TS)",
           [{ 'path': "Castor/CastorDigiMonitor/QrmsfC=f(Tile TS)",
             'description':"QrmsfC=f(Tile TS)"}]
           )
castorlayout(dqmitems, "Digi/11 - QmeanfC_map(allTS)",
           [{ 'path': "Castor/CastorDigiMonitor/QmeanfC_map(allTS)",
             'description':"QmeanfC_map(allTS)"}]
           )

castorlayout(dqmitems, "Digi/12 - QIErms_TS=0",
           [{ 'path': "Castor/CastorDigiMonitor/QIErms_TS=0",
             'description':"QIErms_TS=0",
		'draw': { 'ytype':'log' } }]
           )

castorlayout(dqmitems, "Digi/13 - QIErms_TS=1",
           [{ 'path': "Castor/CastorDigiMonitor/QIErms_TS=1",
             'description':"QIErms_TS=1",
		'draw': { 'ytype':'log' } }]
           )

