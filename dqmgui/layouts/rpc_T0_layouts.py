def rpclayout(i, p, *rows): i["RPC/Layouts/" + p] = DQMItem(layout=rows)

########### define varialbles for frequently used strings #############
rpclink = '   >>> <a href="https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC">Description</a>'
summary = "summary map for rpc, this is NOT an efficiency measurement. Each bin is normalized to 1 considering disconnected chamber"
noise = "Noisy strip map for rpc, counted if a occupancy of single strip is greater than 3.5 times the average of a chamber"
rpcevents = "Events processed by the RPC DQM"
fed = "FED Fatal Errors"
top = "RPC TOP Summary Histogram <br><font color=green><b>GREEN</b> - Good Chamber </font><br> <font color=blue><b>BLUE</b> - Chamber OFF</font><br> <font color=yellow><b>YELLOW</b> - Noisy Strip </font><br> <font color=orange><b>ORANGE</b> - Noisy Chamber </font><br> <font color=pink><b>PINK</b> - Partly Dead Chamber </font><br> <font color=red><b>RED</b> - Fully Dead Chamber </font><br> <font color=aqua><b>LIGHT BLUE</b> - Bad Occupancy Shape </font> <br>"
occupancy = "Occupancy "
clsize = "Cluster Size of RPC system"
nrofcl = "Number of Clusters "
nrofdigi = "Number of Digi"
eff = "Efficiency"
bx  = "RPC BX distribution "
emtf = "RPC L1T EMTF information. "

################### Links to TOP Summary Histograms #################################
rpclayout(dqmitems, "00-Summary_Map",
          [{ 'path': "RPC/EventInfo/reportSummaryMap", 'description': summary + rpclink }])

#Noisy summary
rpclayout(dqmitems, "01-Noisy_summary_Map",
          [{ 'path': "RPC/EventInfo/noisySummaryMap", 'description': noise + rpclink }])

#FED Fatal
rpclayout(dqmitems, "02-Fatal_FED_Errors",
          [{ 'path': "RPC/FEDIntegrity/FEDFatal", 'description': fed + rpclink }])

#RPC Events
rpclayout(dqmitems, "03-RPC_Events",
          [{ 'path': "RPC/AllHits/RPCEvents", 'description': rpcevents + rpclink }])

#RPC HV status
rpclayout(dqmitems, "04-RPC_HV_Status",
          [{ 'path': "RPC/DCSInfo/rpcHV", 'description': rpcevents + rpclink }])

##-------------------
#Occupancy

rpclayout(dqmitems, "05-Barrel_Occupancy",
          [{ 'path': "RPC/AllHits/SummaryHistograms/Occupancy_for_Barrel", 'description': occupancy + rpclink }]
          )

rpclayout(dqmitems, "06-Endcap_Occupancy",
          [{ 'path': "RPC/AllHits/SummaryHistograms/Occupancy_for_Endcap", 'description': occupancy + rpclink }]
          )

rpclayout(dqmitems, "07-Barrel_Occupancy_Muon",
          [{ 'path': "RPC/Muon/SummaryHistograms/Occupancy_for_Barrel", 'description': occupancy + rpclink }]
          )

rpclayout(dqmitems, "08-Endcap_Occupancy_Muon",
          [{'path': "RPC/Muon/SummaryHistograms/Occupancy_for_Endcap", 'description': occupancy + rpclink }]
          )

rpclayout(dqmitems, "09-Barrel_Occupancy_per_Roll",
          [{ 'path': "RPC/AllHits/SummaryHistograms/Occupancy_Roll_vs_Sector_Wheel_2", 'description': occupancy + rpclink },
           { 'path': "RPC/AllHits/SummaryHistograms/Occupancy_Roll_vs_Sector_Wheel_1", 'description': occupancy + rpclink  }],

          [{ 'path': "RPC/AllHits/SummaryHistograms/Occupancy_Roll_vs_Sector_Wheel_0", 'description': occupancy + rpclink  },
           { 'path': "RPC/AllHits/SummaryHistograms/Occupancy_Roll_vs_Sector_Wheel_-1", 'description': occupancy + rpclink  },
           { 'path': "RPC/AllHits/SummaryHistograms/Occupancy_Roll_vs_Sector_Wheel_-2", 'description': occupancy + rpclink  }]
          )

rpclayout(dqmitems, "10-EndCap_Neg_Occupancy_per_Roll",
          [{ 'path': "RPC/AllHits/SummaryHistograms/Occupancy_Ring_vs_Segment_Disk_-1", 'description': occupancy + rpclink },
           { 'path': "RPC/AllHits/SummaryHistograms/Occupancy_Ring_vs_Segment_Disk_-2", 'description': occupancy + rpclink }],

          [{ 'path': "RPC/AllHits/SummaryHistograms/Occupancy_Ring_vs_Segment_Disk_-3", 'description': occupancy + rpclink },
           { 'path': "RPC/AllHits/SummaryHistograms/Occupancy_Ring_vs_Segment_Disk_-4", 'description': occupancy + rpclink }]
          )

rpclayout(dqmitems, "11-EndCap_Pos_Occupancy_per_Roll",
          [{ 'path': "RPC/AllHits/SummaryHistograms/Occupancy_Ring_vs_Segment_Disk_1", 'description': occupancy + rpclink },
           { 'path': "RPC/AllHits/SummaryHistograms/Occupancy_Ring_vs_Segment_Disk_2", 'description': occupancy + rpclink }],

          [{ 'path': "RPC/AllHits/SummaryHistograms/Occupancy_Ring_vs_Segment_Disk_3", 'description': occupancy + rpclink },
           { 'path': "RPC/AllHits/SummaryHistograms/Occupancy_Ring_vs_Segment_Disk_4", 'description': occupancy + rpclink }]
          )

##------------------------
##Mean cluster size

rpclayout(dqmitems, "12-Barrel_MeanClusterSize",
          [{ 'path': "RPC/AllHits/SummaryHistograms/ClusterSizeMean_Roll_vs_Sector_Wheel2", 'description': occupancy + rpclink },
           { 'path': "RPC/AllHits/SummaryHistograms/ClusterSizeMean_Roll_vs_Sector_Wheel1", 'description': occupancy + rpclink  }],

          [{ 'path': "RPC/AllHits/SummaryHistograms/ClusterSizeMean_Roll_vs_Sector_Wheel0", 'description': occupancy + rpclink  },
           { 'path': "RPC/AllHits/SummaryHistograms/ClusterSizeMean_Roll_vs_Sector_Wheel-1", 'description': occupancy + rpclink  },
           { 'path': "RPC/AllHits/SummaryHistograms/ClusterSizeMean_Roll_vs_Sector_Wheel-2", 'description': occupancy + rpclink  }]
          )

rpclayout(dqmitems, "13-EndCap_Neg_MeanClusterSize",
          [{ 'path': "RPC/AllHits/SummaryHistograms/ClusterSizeMean_Ring_vs_Segment_Disk-1", 'description': occupancy + rpclink },
           { 'path': "RPC/AllHits/SummaryHistograms/ClusterSizeMean_Ring_vs_Segment_Disk-2", 'description': occupancy + rpclink }],

          [{ 'path': "RPC/AllHits/SummaryHistograms/ClusterSizeMean_Ring_vs_Segment_Disk-3", 'description': occupancy + rpclink },
           { 'path': "RPC/AllHits/SummaryHistograms/ClusterSizeMean_Ring_vs_Segment_Disk-4", 'description': occupancy + rpclink }]
          )

rpclayout(dqmitems, "14-EndCap_Pos_MeanClusterSize",
          [{ 'path': "RPC/AllHits/SummaryHistograms/ClusterSizeMean_Ring_vs_Segment_Disk1", 'description': occupancy + rpclink },
           { 'path': "RPC/AllHits/SummaryHistograms/ClusterSizeMean_Ring_vs_Segment_Disk2", 'description': occupancy + rpclink }],

          [{ 'path': "RPC/AllHits/SummaryHistograms/ClusterSizeMean_Ring_vs_Segment_Disk3", 'description': occupancy + rpclink },
           { 'path': "RPC/AllHits/SummaryHistograms/ClusterSizeMean_Ring_vs_Segment_Disk4", 'description': occupancy + rpclink }]
          )

##------------------------
##Number Digi

rpclayout(dqmitems, "15-Barrel_Multiplicity",
          [{ 'path': "RPC/AllHits/SummaryHistograms/Multiplicity_Barrel", 'description': nrofdigi + rpclink }])

rpclayout(dqmitems, "16-Endcap_Multiplicity",
          [ { 'path': "RPC/AllHits/SummaryHistograms/Multiplicity_Endcap-", 'description': nrofdigi + rpclink },
            { 'path': "RPC/AllHits/SummaryHistograms/Multiplicity_Endcap+", 'description': nrofdigi + rpclink  }]
          )

##-----------------------
##BX

rpclayout(dqmitems, "17-Barrel_Bunch_Crossing",
          [{ 'path': "RPC/Muon/SummaryHistograms/BxDistribution_Wheel_2", 'description': bx + rpclink },
           { 'path': "RPC/Muon/SummaryHistograms/BxDistribution_Wheel_1", 'description': bx + rpclink  }],

          [{ 'path': "RPC/Muon/SummaryHistograms/BxDistribution_Wheel_0", 'description': bx + rpclink  },
           { 'path': "RPC/Muon/SummaryHistograms/BxDistribution_Wheel_-1", 'description': bx + rpclink  },
           { 'path': "RPC/Muon/SummaryHistograms/BxDistribution_Wheel_-2", 'description': bx + rpclink  }]
          )

rpclayout(dqmitems, "18-EndCap_Negative_Bunch_Crossing",
          [{ 'path': "RPC/Muon/SummaryHistograms/BxDistribution_Disk_-1", 'description': bx + rpclink },
           { 'path': "RPC/Muon/SummaryHistograms/BxDistribution_Disk_-2", 'description': bx + rpclink }],

          [{ 'path': "RPC/Muon/SummaryHistograms/BxDistribution_Disk_-3", 'description': bx + rpclink},
           { 'path': "RPC/Muon/SummaryHistograms/BxDistribution_Disk_-4", 'description': bx  + rpclink}]
          )

rpclayout(dqmitems, "19-EndCap_Positive_Bunch_Crossing",
          [{ 'path': "RPC/Muon/SummaryHistograms/BxDistribution_Disk_1", 'description': bx + rpclink },
           { 'path': "RPC/Muon/SummaryHistograms/BxDistribution_Disk_2", 'description': bx + rpclink }],

          [{ 'path': "RPC/Muon/SummaryHistograms/BxDistribution_Disk_3", 'description': bx + rpclink},
           { 'path': "RPC/Muon/SummaryHistograms/BxDistribution_Disk_4", 'description': bx  + rpclink}]
          )

##-------------------------
##EMTF

rpclayout(dqmitems, "20-RPC_Hit_BX",
          [{ 'path': "L1T/L1TStage2EMTF/rpcHitBX", 'description': emtf + rpclink }])

rpclayout(dqmitems, "21-RPC_Chamber_Occupancy",
          [{ 'path': "L1T/L1TStage2EMTF/rpcHitOccupancy", 'description': emtf + rpclink }])

