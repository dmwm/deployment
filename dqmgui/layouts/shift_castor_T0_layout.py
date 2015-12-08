def shiftcastorlayout(i, p, *rows): i["00 Shift/Castor/" + p] = DQMItem(layout=rows)

shiftcastorlayout(dqmitems, "00 Castor shifter plot",
           [{ 'path': "Castor/CastorDigiMonitor/QIE_capID+er+dv",
             'description':"Frontend and readout errors"}]
           )

shiftcastorlayout(dqmitems, "01 Castor shifter plot",
           [{ 'path': "Castor/CastorDigiMonitor/QfC=f(Tile TS) (cumulative)",
             'description':"Channel-wise timing"}]
           )

shiftcastorlayout(dqmitems, "02 Castor shifter plot",
           [{ 'path': "Castor/CastorRecHitMonitor/CastorRecHitOccMap",
             'description':"Map of rechit occupancies"}]
           )
