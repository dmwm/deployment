def GEMLayout(i, p, *rows): i["GEM/Layouts/" + p] = DQMItem(layout=rows)

GEMLayout(dqmitems, "00 Global view", [{'path' : "GEM/testEta", 'description': 'test 1'}])
GEMLayout(dqmitems, "01 recHit", [{'path' : "GEM/testPhi", 'description': 'test 2'}])
