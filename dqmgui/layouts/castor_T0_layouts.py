def castorlayout(i, p, *rows): i["Castor/Layouts/" + p] = DQMItem(layout=rows)

castorlayout(dqmitems, "01 - Map of frontend and readout errors",
           [{ 'path': "Castor/CastorDigiMonitor/QIE_capID+er+dv",
             'description':"Frontend and readout errors"}]
           )

castorlayout(dqmitems, "02 - Channel-wise timing",
           [{ 'path': "Castor/CastorDigiMonitor/QfC=f(Tile TS) (cumulative)",
             'description':"Channel-wise timing"}]
           )

castorlayout(dqmitems, "03 - Map of rechit occupancies",
           [{ 'path': "Castor/CastorRecHitMonitor/CastorRecHitOccMap",
             'description':"Map of rechit occupancies"}]
           )
