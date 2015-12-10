def castorlayout(i, p, *rows): i["Castor/Layouts/" + p] = DQMItem(layout=rows)

castorlayout(dqmitems, "00 Castor quick collection plot",
           [{ 'path': "Castor/CastorDigiMonitor/QIE_capID+er+dv",
             'description':"Frontend and readout errors"}]
           )

castorlayout(dqmitems, "01 Castor quick collection plot",
           [{ 'path': "Castor/CastorDigiMonitor/QfC=f(Tile TS) (cumulative)",
             'description':"Channel-wise timing"}]
           )

castorlayout(dqmitems, "02 Castor quick collection plot",
           [{ 'path': "Castor/CastorRecHitMonitor/CastorRecHitOccMap",
             'description':"Map of rechit occupancies"}]
           )
