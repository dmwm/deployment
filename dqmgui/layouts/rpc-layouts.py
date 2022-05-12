def rpclayout(i, p, *rows): i["RPC/Layouts/" + p] = DQMItem(layout=rows)

########### define varialbles for frequently used strings #############
rpclink = "   >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Description</a>";
summary = "summary map for rpc, this is NOT an efficiency measurement"
rpcevents = "Events processed by the RPC DQM"
fed = "FED Fatal Errors";
top = "RPC TOP Summary Histogram <br><font color=green><b>GREEN</b> - Good Chamber </font><br> <font color=blue><b>BLUE</b> - Chamber OFF</font><br> <font color=yellow><b>YELLOW</b> - Noisy Strip </font><br> <font color=orange><b>ORANGE</b> - Noisy Chamber </font><br> <font color=pink><b>PINK</b> - Partly Dead Chamber </font><br> <font color=red><b>RED</b> - Fully Dead Chamber </font><br> <font color=aqua><b>LIGHT BLUE</b> - Bad Occupancy Shape </font> <br>";
occupancy = "Occupancy ";
clsize = "Cluster Size of RPC system";
nrofcl = "Number of clusters, i.e. reconstructed hits.";
nrofdigi = "Number of single hits.";
bx = "RPC BX distribution "
emtf = "RPC L1T EMTF information. "

################### Links to TOP Summary Histograms #################################

#FED Fatal
rpclayout(dqmitems, "00-Summary_Map",
          [{ 'path': "RPC/EventInfo/reportSummaryMap", 'description': summary + rpclink }])

rpclayout(dqmitems, "01-Fatal_FED_Errors",
          [{ 'path': "RPC/FEDIntegrity_EvF/FEDFatal", 'description': fed + rpclink }])
##-------------------

#RPC Events
rpclayout(dqmitems, "02-RPC_Events",
          [{ 'path': "RPC/AllHits/RPCEvents", 'description': rpcevents + rpclink }])
##-------------------

#Occupancy

rpclayout(dqmitems, "03-Barrel_Occupancy",
          [{ 'path': "RPC/AllHits/SummaryHistograms/Occupancy_for_Barrel", 'description': occupancy + rpclink }]
          )

rpclayout(dqmitems, "04-Endcap_Occupancy",
          [{'path': "RPC/AllHits/SummaryHistograms/Occupancy_for_Endcap", 'description': occupancy + rpclink }]
          )

rpclayout(dqmitems, "05-Barrel_1DOccupancy",
          [{ 'path': "RPC/AllHits/SummaryHistograms/1DOccupancy_Wheel_2", 'description': occupancy + rpclink },
           { 'path': "RPC/AllHits/SummaryHistograms/1DOccupancy_Wheel_1", 'description': occupancy + rpclink  }],

          [{ 'path': "RPC/AllHits/SummaryHistograms/1DOccupancy_Wheel_0", 'description': occupancy + rpclink  },
           { 'path': "RPC/AllHits/SummaryHistograms/1DOccupancy_Wheel_-1", 'description': occupancy + rpclink  },
           { 'path': "RPC/AllHits/SummaryHistograms/1DOccupancy_Wheel_-2", 'description': occupancy + rpclink  }]
          )

rpclayout(dqmitems, "06-EndCap_1DOccupancy",
          [{ 'path': "RPC/AllHits/SummaryHistograms/1DOccupancy_Ring_2", 'description': occupancy + rpclink },
           { 'path': "RPC/AllHits/SummaryHistograms/1DOccupancy_Ring_3", 'description': occupancy + rpclink }]
          )

##------------------------

##Number Digi
rpclayout(dqmitems, "07-Barrel_Multiplicity",
          [{ 'path': "RPC/AllHits/SummaryHistograms/Multiplicity_Barrel", 'description': nrofdigi + rpclink }])

rpclayout(dqmitems, "08-Endcap_Multiplicity",
          [ { 'path': "RPC/AllHits/SummaryHistograms/Multiplicity_Endcap-", 'description': nrofdigi + rpclink },
            { 'path': "RPC/AllHits/SummaryHistograms/Multiplicity_Endcap+", 'description': nrofdigi + rpclink  }]
          )
##-----------------------

##Number Cluster

rpclayout(dqmitems, "09-Barrel_Number_Of_Clusters",
          [{ 'path': "RPC/AllHits/SummaryHistograms/NumberOfClusters_Barrel", 'description': nrofcl + rpclink }]
          )

rpclayout(dqmitems, "10-Endcap_Number_Of_Clusters",
          [ { 'path': "RPC/AllHits/SummaryHistograms/NumberOfClusters_Endcap-", 'description': nrofcl + rpclink },
            { 'path': "RPC/AllHits/SummaryHistograms/NumberOfClusters_Endcap+", 'description': nrofcl + rpclink  }]
          )

##-----------------------

##BX
rpclayout(dqmitems, "11-Barrel_Bunch_Crossing",
          [{ 'path': "RPC/AllHits/SummaryHistograms/BxDistribution_Wheel_2", 'description': bx + rpclink },
           { 'path': "RPC/AllHits/SummaryHistograms/BxDistribution_Wheel_1", 'description': bx + rpclink  }],

          [{ 'path': "RPC/AllHits/SummaryHistograms/BxDistribution_Wheel_0", 'description': bx + rpclink  },
           { 'path': "RPC/AllHits/SummaryHistograms/BxDistribution_Wheel_-1", 'description': bx + rpclink  },
           { 'path': "RPC/AllHits/SummaryHistograms/BxDistribution_Wheel_-2", 'description': bx + rpclink  }]
          )

rpclayout(dqmitems, "12-Positive_EndCap_Bunch_Crossing",
          [{ 'path': "RPC/AllHits/SummaryHistograms/BxDistribution_Disk_4", 'description': bx + rpclink },
           { 'path': "RPC/AllHits/SummaryHistograms/BxDistribution_Disk_3", 'description': bx + rpclink }],

          [{ 'path': "RPC/AllHits/SummaryHistograms/BxDistribution_Disk_2", 'description': bx + rpclink},
           { 'path': "RPC/AllHits/SummaryHistograms/BxDistribution_Disk_1", 'description': bx + rpclink}]
          )


rpclayout(dqmitems, "13-Negative_EndCap_Bunch_Crossing",
          [{ 'path': "RPC/AllHits/SummaryHistograms/BxDistribution_Disk_-4", 'description': bx + rpclink },
           { 'path': "RPC/AllHits/SummaryHistograms/BxDistribution_Disk_-3", 'description': bx + rpclink }],

          [{ 'path': "RPC/AllHits/SummaryHistograms/BxDistribution_Disk_-2", 'description': bx + rpclink},
           { 'path': "RPC/AllHits/SummaryHistograms/BxDistribution_Disk_-1", 'description': bx + rpclink}]
          )
##------------------------

##EMTF
rpclayout(dqmitems, "14-RPC_Hit_BX",
          [{ 'path': "L1T/L1TStage2EMTF/rpcHitBX", 'description': emtf + rpclink }])

rpclayout(dqmitems, "15-RPC_Chamber_Occupancy",
          [{ 'path': "L1T/L1TStage2EMTF/rpcHitOccupancy", 'description': emtf + rpclink }])

##------------------------
