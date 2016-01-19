def shiftcastorlayout(i, p, *rows): i["00 Shift/Castor/" + p] = DQMItem(layout=rows)

shiftcastorlayout(dqmitems, "01 - Map of frontend and readout errors",
           [{ 'path': "Castor/CastorDigiMonitor/QIE_capID+er+dv",
             'description':"Frontend and readout errors"}]
           )

shiftcastorlayout(dqmitems, "02 - Channel-wise timing",
           [{ 'path': "Castor/CastorDigiMonitor/QfC=f(Tile TS) (cumulative)",
             'description':"Channel-wise timing"}]
           )

shiftcastorlayout(dqmitems, "03 - Map of rechit occupancies",
           [{ 'path': "Castor/CastorRecHitMonitor/CastorRecHitOccMap",
             'description':"Map of rechit occupancies"}]
           )
