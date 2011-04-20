def rpclayout(i, p, *rows): i["RPC/Layouts/" + p] = DQMItem(layout=rows)

########### define varialbles for frequently used strings #############
rpclink = "   >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Description</a>";

rpcevents = "Events processed by the RPC DQM"
fed = "FED Fatal Errors";
top = "RPC TOP Summary Histogram <br><font color=green><b>GREEN</b> - Good Chamber </font><br> <font color=blue><b>BLUE</b> - Chamber OFF</font><br> <font color=yellow><b>YELLOW</b> - Noisy Strip </font><br> <font color=orange><b>ORANGE</b> - Noisy Chamber </font><br> <font color=pink><b>PINK</b> - Partly Dead Chamber </font><br> <font color=red><b>RED</b> - Fully Dead Chamber </font><br> <font color=aqua><b>LIGHT BLUE</b> - Bad Occupancy Shape </font> <br>";
occupancy = "Occupancy ";
clsize = "Cluster Size";
nrofcl = "Number of Clusters ";
nrofdigi = "Number of Digi";
eff = "Efficiency";
bx  = "RPC BX distribution "





################### Links to TOP Summary Histograms #################################


#RPC Events
rpclayout(dqmitems, "RPC_Events",
          [{ 'path': "RPC/RecHits/SummaryHistograms/RPCEvents", 'description': rpcevents + rpclink }])
##-------------------

#FED Fatal
rpclayout(dqmitems, "Fatal_FED_Errors",
          [{ 'path': "RPC/FEDIntegrity/FEDFatal", 'description': fed + rpclink }])
##-----------------

#Roll Quality
rpclayout(dqmitems, "Barrel_TOP_Summary",
          [{ 'path': "RPC/RecHits/SummaryHistograms/RPCChamberQuality_Roll_vs_Sector_Wheel2", 'description': top + rpclink },
           { 'path': "RPC/RecHits/SummaryHistograms/RPCChamberQuality_Roll_vs_Sector_Wheel1", 'description': top + rpclink }],

          [{ 'path': "RPC/RecHits/SummaryHistograms/RPCChamberQuality_Roll_vs_Sector_Wheel0", 'description': top + rpclink },
           { 'path': "RPC/RecHits/SummaryHistograms/RPCChamberQuality_Roll_vs_Sector_Wheel-1", 'description': top + rpclink},
           { 'path': "RPC/RecHits/SummaryHistograms/RPCChamberQuality_Roll_vs_Sector_Wheel-2", 'description': top + rpclink}]
          )


rpclayout(dqmitems, "EndCap_TOP_Summary",
          [{ 'path': "RPC/RecHits/SummaryHistograms/RPCChamberQuality_Ring_vs_Segment_Disk3", 'description': top + rpclink },
           { 'path': "RPC/RecHits/SummaryHistograms/RPCChamberQuality_Ring_vs_Segment_Disk2", 'description': top + rpclink },
           { 'path': "RPC/RecHits/SummaryHistograms/RPCChamberQuality_Ring_vs_Segment_Disk1", 'description': top + rpclink }],

          [{ 'path': "RPC/RecHits/SummaryHistograms/RPCChamberQuality_Ring_vs_Segment_Disk-3", 'description': top + rpclink},
           { 'path': "RPC/RecHits/SummaryHistograms/RPCChamberQuality_Ring_vs_Segment_Disk-2", 'description': top + rpclink},
           { 'path': "RPC/RecHits/SummaryHistograms/RPCChamberQuality_Ring_vs_Segment_Disk-1", 'description': top + rpclink}]
          )

rpclayout(dqmitems, "Barrel_TOP_summary_Distribution",
          [{ 'path': "RPC/RecHits/SummaryHistograms/RPCChamberQuality_Distribution_Wheel2", 'description': top + rpclink },
           { 'path': "RPC/RecHits/SummaryHistograms/RPCChamberQuality_Distribution_Wheel1", 'description': top + rpclink  }],

          [{ 'path': "RPC/RecHits/SummaryHistograms/RPCChamberQuality_Distribution_Wheel0", 'description': top + rpclink  },
           { 'path': "RPC/RecHits/SummaryHistograms/RPCChamberQuality_Distribution_Wheel-1", 'description': top + rpclink  },
           { 'path': "RPC/RecHits/SummaryHistograms/RPCChamberQuality_Distribution_Wheel-2", 'description': top + rpclink  }]
          )

rpclayout(dqmitems, "EndCap_TOP_Summary_Distribution",
          [{ 'path': "RPC/RecHits/SummaryHistograms/RPCChamberQuality_Distribution_Disk3", 'description': top + rpclink },
           { 'path': "RPC/RecHits/SummaryHistograms/RPCChamberQuality_Distribution_Disk2", 'description': top + rpclink },
           { 'path': "RPC/RecHits/SummaryHistograms/RPCChamberQuality_Distribution_Disk1", 'description': top + rpclink }],

          [{ 'path': "RPC/RecHits/SummaryHistograms/RPCChamberQuality_Distribution_Disk-3", 'description': top + rpclink},
           { 'path': "RPC/RecHits/SummaryHistograms/RPCChamberQuality_Distribution_Disk-2", 'description': top + rpclink},
           { 'path': "RPC/RecHits/SummaryHistograms/RPCChamberQuality_Distribution_Disk-1", 'description': top + rpclink}]
          )
##------------------------

#Occupancy

rpclayout(dqmitems, "Barrel_Occupancy",
          [{ 'path': "RPC/RecHits/SummaryHistograms/Occupancy_for_Barrel", 'description': occupancy + rpclink }]
          )

rpclayout(dqmitems, "Endcap_Occupancy",
          [{'path': "RPC/RecHits/SummaryHistograms/Occupancy_for_EndcapNegative", 'description': occupancy + rpclink },
           {'path': "RPC/RecHits/SummaryHistograms/Occupancy_for_EndcapPositive", 'description': occupancy + rpclink }]
          )


rpclayout(dqmitems, "Barrel_1DOccupancy",
          [{ 'path': "RPC/RecHits/SummaryHistograms/1DOccupancy_Wheel_2", 'description': occupancy + rpclink },
           { 'path': "RPC/RecHits/SummaryHistograms/1DOccupancy_Wheel_1", 'description': occupancy + rpclink  }],

          [{ 'path': "RPC/RecHits/SummaryHistograms/1DOccupancy_Wheel_0", 'description': occupancy + rpclink  },
           { 'path': "RPC/RecHits/SummaryHistograms/1DOccupancy_Wheel_-1", 'description': occupancy + rpclink  },
           { 'path': "RPC/RecHits/SummaryHistograms/1DOccupancy_Wheel_-2", 'description': occupancy + rpclink  }]
          )

rpclayout(dqmitems, "EndCap_1DOccupancy",
          [{ 'path': "RPC/RecHits/SummaryHistograms/1DOccupancy_Disk_3", 'description': occupancy + rpclink },
           { 'path': "RPC/RecHits/SummaryHistograms/1DOccupancy_Disk_2", 'description': occupancy + rpclink },
           { 'path': "RPC/RecHits/SummaryHistograms/1DOccupancy_Disk_1", 'description': occupancy + rpclink }],

          [{ 'path': "RPC/RecHits/SummaryHistograms/1DOccupancy_Disk_-3", 'description':occupancy  + rpclink},
           { 'path': "RPC/RecHits/SummaryHistograms/1DOccupancy_Disk_-2", 'description':occupancy  + rpclink},
           { 'path': "RPC/RecHits/SummaryHistograms/1DOccupancy_Disk_-1", 'description':occupancy  + rpclink}]
          )

##------------------------


##BX
rpclayout(dqmitems, "Barrel_BX",
          [{ 'path': "RPC/RecHits/SummaryHistograms/BxDistribution_Wheel_2", 'description': bx + rpclink },
           { 'path': "RPC/RecHits/SummaryHistograms/BxDistribution_Wheel_1", 'description': bx + rpclink  }],

          [{ 'path': "RPC/RecHits/SummaryHistograms/BxDistribution_Wheel_0", 'description': bx + rpclink  },
           { 'path': "RPC/RecHits/SummaryHistograms/BxDistribution_Wheel_-1", 'description': bx + rpclink  },
           { 'path': "RPC/RecHits/SummaryHistograms/BxDistribution_Wheel_-2", 'description': bx + rpclink  }]
          )


rpclayout(dqmitems, "EndCap_BX",
          [{ 'path': "RPC/RecHits/SummaryHistograms/BxDistribution_Disk_3", 'description': bx + rpclink },
           { 'path': "RPC/RecHits/SummaryHistograms/BxDistribution_Disk_2", 'description': bx + rpclink },
           { 'path': "RPC/RecHits/SummaryHistograms/BxDistribution_Disk_1", 'description': bx + rpclink }],

          [{ 'path': "RPC/RecHits/SummaryHistograms/BxDistribution_Disk_-3", 'description': bx + rpclink},
           { 'path': "RPC/RecHits/SummaryHistograms/BxDistribution_Disk_-2", 'description': bx + rpclink},
           { 'path': "RPC/RecHits/SummaryHistograms/BxDistribution_Disk_-1", 'description': bx  + rpclink}]
          )
##------------------------

##Number Cluster
rpclayout(dqmitems, "Cluster_Size",
          [{ 'path': "RPC/RecHits/SummaryHistograms/ClusterSize_for_BarrelandEndcap", 'description': clsize + rpclink }]
          )


rpclayout(dqmitems, "Barrel_Number_Of_Clusters",
          [{ 'path': "RPC/RecHits/SummaryHistograms/NumberOfClusters_for_Barrel", 'description': nrofcl + rpclink }]
          )


rpclayout(dqmitems, "Endcap_Number_Of_Clusters",
          [ { 'path': "RPC/RecHits/SummaryHistograms/NumberOfClusters_for_EndcapNegative", 'description': nrofcl + rpclink },
            { 'path': "RPC/RecHits/SummaryHistograms/NumberOfClusters_for_EndcapPositive", 'description': nrofcl + rpclink  }]
          )
##-----------------------



##Number Digi
rpclayout(dqmitems, "Barrel_Number_Of_Digi",
          [{ 'path': "RPC/RecHits/SummaryHistograms/NumberOfDigi_for_Barrel", 'description': nrofdigi + rpclink }])


rpclayout(dqmitems, "Endcap_Number_Of_Digi",
          [ { 'path': "RPC/RecHits/SummaryHistograms/NumberOfDigi_for_EndcapNegative", 'description': nrofdigi + rpclink },
            { 'path': "RPC/RecHits/SummaryHistograms/NumberOfDigi_for_EndcapPositive", 'description': nrofdigi + rpclink  }]
          )
        ##-----------------------



        ##Efficiency
rpclayout(dqmitems, "BarrelEfficiency",
          [{ 'path': "RPC/RPCEfficiency/Efficiency_Roll_vs_Sector_Wheel_-2", 'description': eff + rpclink },
           { 'path': "RPC/RPCEfficiency/Efficiency_Roll_vs_Sector_Wheel_-1", 'description': eff + rpclink  }],

          [{ 'path': "RPC/RPCEfficiency/Efficiency_Roll_vs_Sector_Wheel_0", 'description': eff + rpclink  },
           { 'path': "RPC/RPCEfficiency/Efficiency_Roll_vs_Sector_Wheel_+1", 'description': eff + rpclink  },
           { 'path': "RPC/RPCEfficiency/Efficiency_Roll_vs_Sector_Wheel_+2", 'description': eff + rpclink  }]
          )

rpclayout(dqmitems, "EndCapEfficiency",
          [{ 'path': "RPC/RPCEfficiency/Efficiency_Roll_vs_Segment_Disk_-3", 'description': eff + rpclink },
           { 'path': "RPC/RPCEfficiency/Efficiency_Roll_vs_Segment_Disk_-2", 'description': eff + rpclink },
           { 'path': "RPC/RPCEfficiency/Efficiency_Roll_vs_Segment_Disk_-1", 'description': eff + rpclink }],

          [{ 'path': "RPC/RPCEfficiency/Efficiency_Roll_vs_Segment_Disk_1", 'description': eff + rpclink },
           { 'path': "RPC/RPCEfficiency/Efficiency_Roll_vs_Segment_Disk_2", 'description': eff + rpclink },
           { 'path': "RPC/RPCEfficiency/Efficiency_Roll_vs_Segment_Disk_3", 'description': eff + rpclink }],
          )
        ##-------------------------
