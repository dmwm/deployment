def rpclayout(i, p, *rows): i["RPC/Layouts/" + p] = DQMItem(layout=rows)

rpclink = "   >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Description</a>";

top = "RPC TOP Summary Histogram <br><font color=green><b>GREEN</b> - Good Chamber </font><br> <font color=blue><b>BLUE</b> - Chamber OFF</font><br> <font co
lor=yellow><b>YELLOW</b> - Noisy Strip </font><br> <font color=orange><b>ORANGE</b> - Noisy Chamber </font><br> <font color=pink><b>PINK</b> - Partly Dead Ch
amber </font><br> <font color=red><b>RED</b> - Fully Dead Chamber </font><br> <font color=aqua><b>LIGHT BLUE</b> - Bad Occupancy Shape </font> <br>";

bx = "RPC BX distribution ";
eff = "RPC Efficiency ";
nrofcl = "Number of Clusters ";

rpclayout(dqmitems, "Barrel_TOP_Summary",
          [{ 'path': "RPC/RecHits/SummaryHistograms/RPCChamberQuality_Roll_vs_Sector_Wheel2", 'description': top + rpclink },
           { 'path': "RPC/RecHits/SummaryHistograms/RPCChamberQuality_Roll_vs_Sector_Wheel1", 'description': top + rpclink  }],

          [{ 'path': "RPC/RecHits/SummaryHistograms/RPCChamberQuality_Roll_vs_Sector_Wheel0", 'description': top + rpclink  },
           { 'path': "RPC/RecHits/SummaryHistograms/RPCChamberQuality_Roll_vs_Sector_Wheel-1", 'description': top + rpclink  },
           { 'path': "RPC/RecHits/SummaryHistograms/RPCChamberQuality_Roll_vs_Sector_Wheel-2", 'description': top + rpclink  }]
          )

rpclayout(dqmitems, "Barrel_BX",
          [{ 'path': "RPC/RecHits/SummaryHistograms/BxDistribution_Wheel_2", 'description': bx + rpclink },
           { 'path': "RPC/RecHits/SummaryHistograms/BxDistribution_Wheel_1", 'description': bx + rpclink  }],

          [{ 'path': "RPC/RecHits/SummaryHistograms/BxDistribution_Wheel_0", 'description': bx + rpclink  },
           { 'path': "RPC/RecHits/SummaryHistograms/BxDistribution_Wheel_-1", 'description': bx + rpclink  },
           { 'path': "RPC/RecHits/SummaryHistograms/BxDistribution_Wheel_-2", 'description': bx + rpclink  }]
          )

rpclayout(dqmitems, "EndCal_TOP_Summary",
          [{ 'path': "RPC/RecHits/SummaryHistograms/RPCChamberQuality_Distribution_Wheel2", 'description': top + rpclink },
           { 'path': "RPC/RecHits/SummaryHistograms/RPCChamberQuality_Distribution_Wheel1", 'description': top + rpclink  }],

          [{ 'path': "RPC/RecHits/SummaryHistograms/RPCChamberQuality_Distribution_Wheel0", 'description': top + rpclink  },
           { 'path': "RPC/RecHits/SummaryHistograms/RPCChamberQuality_Distribution_Wheel-1", 'description': top + rpclink  },
           { 'path': "RPC/RecHits/SummaryHistograms/RPCChamberQuality_Distribution_Wheel-2", 'description': top + rpclink  }]
          )

rpclayout(dqmitems, "Barrel_TOP_summary_Distribution",
          [{ 'path': "RPC/RecHits/SummaryHistograms/RPCChamberQuality_Distribution_Wheel2", 'description': top + rpclink },
           { 'path': "RPC/RecHits/SummaryHistograms/RPCChamberQuality_Distribution_Wheel1", 'description': top + rpclink  }],

          [{ 'path': "RPC/RecHits/SummaryHistograms/RPCChamberQuality_Distribution_Wheel0", 'description': top + rpclink  },
           { 'path': "RPC/RecHits/SummaryHistograms/RPCChamberQuality_Distribution_Wheel-1", 'description': top + rpclink  },
           { 'path': "RPC/RecHits/SummaryHistograms/RPCChamberQuality_Distribution_Wheel-2", 'description': top + rpclink  }]
          )

shiftrpclayout(dqmitems, "BarrelEfficiency",
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
           { 'path': "RPC/RecHits/SummaryHistograms/BxDistribution_Disk_1", 'description': bx + rpclink  }],

          [{ 'path': "RPC/RecHits/SummaryHistograms/BxDistribution_Disk_-3", 'description': bx + rpclink  },
           { 'path': "RPC/RecHits/SummaryHistograms/BxDistribution_Disk_-2", 'description': bx + rpclink  },
           { 'path': "RPC/RecHits/SummaryHistograms/BxDistribution_Disk_-1", 'description': bx + rpclink  }]
          )

rpclayout(dqmitems, "NumberOfClusters",
          [{ 'path': "RPC/RecHits/SummaryHistograms/NumberOfClusters_for_Barrel", 'description': nrofcl + rpclink }],
          [ { 'path': "RPC/RecHits/SummaryHistograms/NumberOfClusters_for_EndcapNegative", 'description': nrofcl + rpclink },
           { 'path': "RPC/RecHits/SummaryHistograms/NumberOfClusters_for_EndcapPositive", 'description': nrofcl + rpclink  }]
          )

