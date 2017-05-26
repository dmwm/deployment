def GEMLayout(i, p, *rows): i["GEM/Layouts/" + p] = DQMItem(layout=rows)

GEMLayout(dqmitems, "00 Globla view", [{'path' : "GEM/testEta", 'test 1'}])
GEMLayout(dqmitems, "00 Globla view", [{'path' : "GEM/testPhi", 'test 2'}])
