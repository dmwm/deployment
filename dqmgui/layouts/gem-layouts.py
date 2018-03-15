def GEMLayout(i, p, *rows): i["GEM/Layouts/" + p] = DQMItem(layout=rows)
#def GEMLayout(i, p, *rows): return 1 # this line and the following one line is for printing out indices
#dqmitems = ""

#GEMLayout(dqmitems, "0 eta", [{'path' : "GEM/eta", 'description': 'eta recHit'}])
#GEMLayout(dqmitems, "1 phi", [{'path' : "GEM/phi", 'description': 'phi recHit'}])

# StatusDigi
GEMLayout(dqmitems, "00 StatusDigi GDcount", 
    [{'path' : "GEM/StatusDigi/GDcount", 
    'description': 'GDCount in StatusDigi'}])

GEMLayout(dqmitems, "01 StatusDigi VFAT Error all", 
    [{'path' : "GEM/StatusDigi/vfatErrors_all_CRC", 
    'description': 'CRC (all) in StatusDigi'}, 
    {'path' : "GEM/StatusDigi/vfatErrors_all_flag", 
    'description': 'Flag (all) in StatusDigi'}, 
    {'path' : "GEM/StatusDigi/vfatErrors_all_b1110", 
    'description': 'Control bit 1110 (all) in StatusDigi'}], 
    [{'path' : "GEM/StatusDigi/vfatErrors_all_b1010", 
    'description': 'Control bit 1010 (all) in StatusDigi'}, 
    {'path' : "GEM/StatusDigi/vfatErrors_all_b1100", 
    'description': 'Control bit 1100 (all) in StatusDigi'}])

layers = ["_la_1", "_la_2"]
#Geminis = ["671093248", "671095040", "671095296", "671095552", "671095808"]
Geminis = ["671088640", "671095296", "671095552", "671095808", "671096064"]
GeminisId = ["1", "27", "28", "29", "30"]
index = 2

for i, gemini in enumerate(Geminis):
	for layer in layers:
		recHit = "GEM/recHit/recHit_Gemini_" + GeminisId[ i ] + layer
		#recHit_index = "GEM/Layouts/%d recHit per VFAT %s%s" % (index, gemini, layer)
		#index = index + 1
		VFAT = "GEM/recHit/VFAT_vs_ClusterSize_Gemini_" + GeminisId[ i ] + layer
		#VFAT_index = "GEM/Layouts/%d VFAT vs ClusterSize %s%s" % (index, gemini, layer)
		#index = index + 1
		Fired = "GEM/recHit/StripFired_Gemini_" + GeminisId[ i ] + layer
		#Fired_index = "GEM/Layouts/%d FiredStrips %s%s" % (index, gemini, layer)
		#index = index + 1
		Digi = "GEM/digi/Digi_Strips_Gemini_" + gemini + layer
		#Digi_index = "GEM/Layouts/%d DigiStrips %s%s" % (index, gemini, layer)
		#index = index + 1
		#print "'%s', "%recHit_index
		#print "'%s', "%VFAT_index
		#print "'%s', "%Fired_index
		#print "'%s', "%Digi_index
		gemid = GeminisId[ i ] if len(GeminisId[ i ]) > 2 else "0" + GeminisId[ i ]
		#GEMLayout(dqmitems, gemini + layer, 
		GEMLayout(dqmitems, "%2d GEMINI%sla%s"%(index, gemid, layer.replace("_la_", "")), 
			[{'path': recHit, 'description': "Number of recHit per VFAT (!!!)"},
     		{'path': VFAT, 'description': "VFAT cs ClusterSize"}],
			[{'path': Fired, 'description': "Number of Fired Strips"},
		    {'path': Digi, 'description': "Number of Digi Strips"}])	
		index += 1
# 		GEMLayout(dqmitems, recHit_index, [{'path' : recHit, 'description': 'Number of recHit per VFAT'}])
# 		GEMLayout(dqmitems, VFAT_index, [{'path' : VFAT, 'description': 'VFAT cs ClusterSize'}])
# 		GEMLayout(dqmitems, Fired_index, [{'path' : Fired, 'description': 'Number of Fired Strips'}])
# 		GEMLayout(dqmitems, Digi_index, [{'path' : Digi, 'description': 'Number of Digi Strips'}])

    				
# GEMLayout(dqmitems, "02 recHit per VFAT", [{'path' : "GEM/recHit/recHit_Gemini_671088640_la_1", 'description': 'Number of recHit per VFAT'}])
# GEMLayout(dqmitems, "03 VFAT vs ClusterSize", [{'path' : "GEM/recHit/VFAT_vs_ClusterSize_Gemini_671088640_la_1", 'description': 'VFAT cs ClusterSize'}])
# GEMLayout(dqmitems, "04 FiredStrips", [{'path' : "GEM/recHit/StripFired_Gemini_671088640_la_1", 'description': 'Number of Fired Strips'}])
# GEMLayout(dqmitems, "05 DigiStrips", [{'path' : "GEM/digi/Digi_Strips_Gemini_671088640_la_1", 'description': 'Number of Digi Strips'}])




