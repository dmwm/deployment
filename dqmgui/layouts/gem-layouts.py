def GEMLayout(i, p, *rows): i["GEM/Layouts/" + p] = DQMItem(layout=rows)

GEMLayout(dqmitems, "00 eta", [{'path' : "GEM/eta", 'description': 'eta recHit'}])
GEMLayout(dqmitems, "01 phi", [{'path' : "GEM/phi", 'description': 'phi recHit'}])
GEMLayout(dqmitems, "02 recHit per VFAT", [{'path' : "GEM/recHit/recHit_Gemini_671088640_la_1", 'description': 'Number of recHit per VFAT'}])
GEMLayout(dqmitems, "03 VFAT vs ClusterSize", [{'path' : "GEM/recHit/VFAT_vs_ClusterSize_Gemini_671088640_la_1", 'description': 'VFAT cs ClusterSize'}])
GEMLayout(dqmitems, "04 FiredStrips", [{'path' : "GEM/recHit/StripFired_Gemini_671088640_la_1", 'description': 'Number of Fired Strips'}])
GEMLayout(dqmitems, "05 DigiStrips", [{'path' : "GEM/digi/Digi_Strips_Gemini_671088640_la_1", 'description': 'Number of Digi Strips'}])




