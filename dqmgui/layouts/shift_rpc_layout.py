def shiftrpclayout(i, p, *rows): i["00 Shift/RPC/" + p] = DQMItem(layout=rows)

########### define varialbles for frequently used strings #############
summary = "summary map for rpc, this is NOT an efficiency measurement"
rpclink = "   >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Description</a>"
fed = "FED Fatal Errors";
rpcevents = "Events processed by the RPC DQM"
occupancy = "Occupancy per sector"
noise = "Average number of noisy strip per roll, counted if a occupancy of single strip is greater than 3.5 times the average of a chamber"

################### Links to Histograms #################################
shiftrpclayout(dqmitems, "00-Summary_Map",
              [{ 'path': "RPC/EventInfo/reportSummaryMap", 'description': summary + rpclink }])

#Noisy summary
shiftrpclayout(dqmitems, "01-Noisy_summary_Map",
              [{ 'path': "RPC/EventInfo/noisySummaryMap", 'description': noise + rpclink }])

#FED Fatal
shiftrpclayout(dqmitems, "02-Fatal_FED_Errors",
              [{ 'path': "RPC/FEDIntegrity_EvF/FEDFatal", 'description': fed + rpclink }])

#RPC Events
shiftrpclayout(dqmitems, "04-RPC_Events",
              [{ 'path': "RPC/AllHits/RPCEvents", 'description': rpcevents + rpclink }])

shiftrpclayout(dqmitems, "04-RPC_Occupancy",
              [{ 'path': "RPC/AllHits/SummaryHistograms/Occupancy_for_Barrel", 'description': occupancy + rpclink  }],
              [{ 'path': "RPC/AllHits/SummaryHistograms/Occupancy_for_Endcap", 'description': occupancy + rpclink }])
