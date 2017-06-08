def GEMLayout(i, p, *rows): i["GEM/Layouts/" + p] = DQMItem(layout=rows)

GEMLayout(dqmitems, "0 eta", [{'path' : "GEM/eta", 'description': 'eta recHit'}])
GEMLayout(dqmitems, "1 phi", [{'path' : "GEM/phi", 'description': 'phi recHit'}])

layers = ["_la_1", "_la_2"]
Geminis = ["671093248", "671095040", "671095296", "671095552", "671095808"]
index = 2

for gemini in Geminis:
	for layer in layers:
	
		recHit = "GEM/recHit/recHit_Gemini_" + gemini + layer
		recHit_index = "'GEM/Layouts/%d recHit per VFAT %s%s," % (index, gemini, layer)
		index = index + 1
		VFAT = "GEM/recHit/VFAT_vs_ClusterSize_Gemini_" + gemini + layer
		VFAT_index = "'GEM/Layouts/%d VFAT vs ClusterSize %s%s," % (index, gemini, layer)
		index = index + 1
		Fired = "GEM/recHit/StripFired_Gemini_" + gemini + layer
		Fired_index = "'GEM/Layouts/%d FiredStrips %s%s," % (index, gemini, layer)
		index = index + 1
		Digi = "GEM/digi/Digi_Strips_Gemini_" + gemini + layer
		Digi_index = "'GEM/Layouts/%d DigiStrips %s%s," % (index, gemini, layer)
		index = index + 1
# 		print recHit_index
# 		print VFAT_index
# 		print Fired_index
# 		print Digi_index
		GEMLayout(dqmitems, gemini + layer, 
			[{'path': recHit, 'description': "Number of recHit per VFAT"},
     		{'path': VFAT, 'description': "VFAT cs ClusterSize"}],
		    [{'path': Fired, 'description': "Number of Fired Strips"},
		    {'path': Digi, 'description': "Number of Digi Strips"}])	
# 		GEMLayout(dqmitems, recHit_index, [{'path' : recHit, 'description': 'Number of recHit per VFAT'}])
# 		GEMLayout(dqmitems, VFAT_index, [{'path' : VFAT, 'description': 'VFAT cs ClusterSize'}])
# 		GEMLayout(dqmitems, Fired_index, [{'path' : Fired, 'description': 'Number of Fired Strips'}])
# 		GEMLayout(dqmitems, Digi_index, [{'path' : Digi, 'description': 'Number of Digi Strips'}])

    				
# GEMLayout(dqmitems, "02 recHit per VFAT", [{'path' : "GEM/recHit/recHit_Gemini_671088640_la_1", 'description': 'Number of recHit per VFAT'}])
# GEMLayout(dqmitems, "03 VFAT vs ClusterSize", [{'path' : "GEM/recHit/VFAT_vs_ClusterSize_Gemini_671088640_la_1", 'description': 'VFAT cs ClusterSize'}])
# GEMLayout(dqmitems, "04 FiredStrips", [{'path' : "GEM/recHit/StripFired_Gemini_671088640_la_1", 'description': 'Number of Fired Strips'}])
# GEMLayout(dqmitems, "05 DigiStrips", [{'path' : "GEM/digi/Digi_Strips_Gemini_671088640_la_1", 'description': 'Number of Digi Strips'}])




