def shiftrpclayout(i, p, *rows): i["00 Shift/RPC/" + p] = DQMItem(layout=rows)

########### define varialbles for frequently used strings #############
summary = "summary map for rpc, this is NOT an efficiency measurement"
rpclink = "   >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Description</a>"
fed = "FED Fatal Errors";
rpcevents = "Events processed by the RPC DQM"
occupancy = "Occupancy per sector"

################### Links to Histograms #################################
shiftrpclayout(dqmitems, "00-Summary_Map",
               [{ 'path': "RPC/EventInfo/reportSummaryMap", 'description': summary + rpclink }])

#FED Fatal
shiftrpclayout(dqmitems, "01-Fatal_FED_Errors",
               [{ 'path': "RPC/FEDIntegrity_EvF/FEDFatal", 'description': fed + rpclink }])

#RPC Events
shiftrpclayout(dqmitems, "02-RPC_Events",
               [{ 'path': "RPC/AllHits/RPCEvents", 'description': rpcevents + rpclink }])

shiftrpclayout(dqmitems, "03-RPC_Occupancy",
               [{ 'path': "RPC/AllHits/SummaryHistograms/Occupancy_for_Barrel", 'description': occupancy + rpclink  }],
               [{ 'path': "RPC/AllHits/SummaryHistograms/Occupancy_for_Endcap", 'description': occupancy + rpclink }])
