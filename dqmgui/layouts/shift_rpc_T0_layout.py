def shiftrpclayout(i, p, *rows): i["00 Shift/RPC/" + p] = DQMItem(layout=rows)

summary = "summary map for rpc, this is NOT an efficiency measurement"
fed = "FED Fatal Errors. Entries MUST be ZERO at all times. If not, report the problem and ask to stop the run."
rpcevents = "Number of processed events."
eff = "RPC Efficiency distribution. Make sure average values is greater than 80."
rpclink = "   >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Description</a>"
occupancy = "Occupancy per sector"
hv = "High Voltage status per lumi section. If ALL bins are red mark the run as BAD."
noise = "Average number of noisy strip per roll, counted if a occupancy of single strip is greater than 3.5 times the average of a chamber"

shiftrpclayout(dqmitems, "00-Summary_Map",
              [{ 'path': "RPC/EventInfo/reportSummaryMap", 'description': summary + rpclink }])

shiftrpclayout(dqmitems, "01-Noisy_summary_Map",
              [{ 'path': "RPC/EventInfo/noisySummaryMap", 'description': noise + rpclink }])

shiftrpclayout(dqmitems, "02-FED_Fatal_Errors",
              [{ 'path': "RPC/FEDIntegrity/FEDFatal", 'description': fed + rpclink }])

shiftrpclayout(dqmitems, "03-RPC_HV_Status",
              [{ 'path': "RPC/DCSInfo/rpcHVStatus", 'description': hv + rpclink }])

shiftrpclayout(dqmitems, "04-RPC_Events",
              [{ 'path': "RPC/AllHits/RPCEvents", 'description': rpcevents + rpclink }])

shiftrpclayout(dqmitems, "04-RPC_Occupancy",
              [{ 'path': "RPC/AllHits/SummaryHistograms/Occupancy_for_Barrel", 'description': occupancy + rpclink  }],
              [{ 'path': "RPC/AllHits/SummaryHistograms/Occupancy_for_Endcap", 'description': occupancy + rpclink  }])

