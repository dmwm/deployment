def castorlayout(i, p, *rows): i["Castor/Layouts/" + p] = DQMItem(layout=rows)

castorlayout(dqmitems, "01 - Report Summary Map",
           [{ 'path': "Castor/EventInfo/reportSummaryMap",
             'description':"Report Summary Map"}]
           )

castorlayout(dqmitems, "02 - Digi Channel Summary Map",
           [{ 'path': "Castor/CastorPSMonitor/CASTOR Digi ChannelSummaryMap",
             'description':"Digi Channel Summary Map"}]
           )

castorlayout(dqmitems, "03 - Digi Occupancy Map",
           [{ 'path': "Castor/CastorPSMonitor/CASTOR Digi Occupancy Map",
             'description':"Digi Occcupancy Map"}]
           )

castorlayout(dqmitems, "04 - Digi Saturation Summary Map",
           [{ 'path': "Castor/CastorPSMonitor/CASTOR Digi SaturationSummaryMap",
             'description':"Digi Saturation Summary Map"}]
           )

castorlayout(dqmitems, "05 - FEDFatal errors",
           [{ 'path': "Castor/CastorDataIntegrityMonitor/CASTOR FEDFatal errors",
             'description':"FED Fatal errors"}]
           )

castorlayout(dqmitems, "06 - Spigot Status",
           [{ 'path': "Castor/CastorDataIntegrityMonitor/CASTOR spigot status",
             'description':"Data Integrity Summary - Spigot Status"}]
           )

castorlayout(dqmitems, "07 - Event Products",
           [{ 'path': "Castor/CastorEventProducts/CastorEventProduct",
             'description':"check whether CASTOR objects are present in the events"}]
           )

castorlayout(dqmitems, "08 - RecHit Occupancy Map",
           [{ 'path': "Castor/CastorRecHitMonitor/CastorRecHits Occupancy Map",
             'description':""}]
           )
           
castorlayout(dqmitems, "09a - RecHit Energy by modules",
           [{ 'path': "Castor/CastorRecHitMonitor/CastorRecHit Energy in modules- above threshold",
             'description':""}]
           )

castorlayout(dqmitems, "09b - RecHit Energy by sectors",
           [{ 'path': "Castor/CastorRecHitMonitor/CastorRecHit Energy in sectors- above threshold",
             'description':""}]
           )

castorlayout(dqmitems, "10 - Average pulse in bunch crossings",
           [{ 'path': "Castor/CastorPSMonitor/CASTOR average pulse in bunch crossings",
             'description':"average pulse in bunch crossings"}]
           )

castorlayout(dqmitems, "11_01 - Pulse Shape for sector 1",
           [{ 'path': "Castor/CastorPSMonitor/Castor Pulse Shape for sector=1 (in all 14 modules)",
             'description':"pulse shape in this particular sector"}]
           )

castorlayout(dqmitems, "11_02 - Pulse Shape for sector 2",
           [{ 'path': "Castor/CastorPSMonitor/Castor Pulse Shape for sector=2 (in all 14 modules)",
             'description':"pulse shape in this particular sector"}]
           )

castorlayout(dqmitems, "11_03 - Pulse Shape for sector 3",
           [{ 'path': "Castor/CastorPSMonitor/Castor Pulse Shape for sector=3 (in all 14 modules)",
             'description':"pulse shape in this particular sector"}]
           )

castorlayout(dqmitems, "11_04 - Pulse Shape for sector 4",
           [{ 'path': "Castor/CastorPSMonitor/Castor Pulse Shape for sector=4 (in all 14 modules)",
             'description':"pulse shape in this particular sector"}]
           )

castorlayout(dqmitems, "11_05 - Pulse Shape for sector 5",
           [{ 'path': "Castor/CastorPSMonitor/Castor Pulse Shape for sector=5 (in all 14 modules)",
             'description':"pulse shape in this particular sector"}]
           )

castorlayout(dqmitems, "11_06 - Pulse Shape for sector 6",
           [{ 'path': "Castor/CastorPSMonitor/Castor Pulse Shape for sector=6 (in all 14 modules)",
             'description':"pulse shape in this particular sector"}]
           )

castorlayout(dqmitems, "11_07 - Pulse Shape for sector 7",
           [{ 'path': "Castor/CastorPSMonitor/Castor Pulse Shape for sector=7 (in all 14 modules)",
             'description':"pulse shape in this particular sector"}]
           )

castorlayout(dqmitems, "11_08 - Pulse Shape for sector 8",
           [{ 'path': "Castor/CastorPSMonitor/Castor Pulse Shape for sector=8 (in all 14 modules)",
             'description':"pulse shape in this particular sector"}]
           )

castorlayout(dqmitems, "11_09 - Pulse Shape for sector 9",
           [{ 'path': "Castor/CastorPSMonitor/Castor Pulse Shape for sector=9 (in all 14 modules)",
             'description':"pulse shape in this particular sector"}]
           )

castorlayout(dqmitems, "11_10 - Pulse Shape for sector 10",
           [{ 'path': "Castor/CastorPSMonitor/Castor Pulse Shape for sector=10 (in all 14 modules)",
             'description':"pulse shape in this particular sector"}]
           )

castorlayout(dqmitems, "11_11 - Pulse Shape for sector 11",
           [{ 'path': "Castor/CastorPSMonitor/Castor Pulse Shape for sector=11 (in all 14 modules)",
             'description':"pulse shape in this particular sector"}]
           )

castorlayout(dqmitems, "11_12 - Pulse Shape for sector 12",
           [{ 'path': "Castor/CastorPSMonitor/Castor Pulse Shape for sector=12 (in all 14 modules)",
             'description':"pulse shape in this particular sector"}]
           )

castorlayout(dqmitems, "11_13 - Pulse Shape for sector 13",
           [{ 'path': "Castor/CastorPSMonitor/Castor Pulse Shape for sector=13 (in all 14 modules)",
             'description':"pulse shape in this particular sector"}]
           )

castorlayout(dqmitems, "11_14 - Pulse Shape for sector 14",
           [{ 'path': "Castor/CastorPSMonitor/Castor Pulse Shape for sector=14 (in all 14 modules)",
             'description':"pulse shape in this particular sector"}]
           )

castorlayout(dqmitems, "11_15 - Pulse Shape for sector 15",
           [{ 'path': "Castor/CastorPSMonitor/Castor Pulse Shape for sector=15 (in all 14 modules)",
             'description':"pulse shape in this particular sector"}]
           )

castorlayout(dqmitems, "11_16 - Pulse Shape for sector 16",
           [{ 'path': "Castor/CastorPSMonitor/Castor Pulse Shape for sector=16 (in all 14 modules)",
             'description':"pulse shape in this particular sector"}]
           )
