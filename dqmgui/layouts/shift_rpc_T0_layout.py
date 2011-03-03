def shiftrpclayout(i, p, *rows): i["00 Shift/RPC/" + p] = DQMItem(layout=rows)
eff = "RPC Efficiency, Roll vs Sector ";
rpclink = "   >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Description</a>";

shiftrpclayout(dqmitems, "00-BarrelOccupancy",
  [{ 'path': "RPC/RecHits/SummaryHistograms/Occupancy_for_Barrel", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Description</a>" }],
  [{ 'path': "RPC/RecHits/SummaryHistograms/Occupancy_for_EndcapNegative", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Description</a>" },
 { 'path': "RPC/RecHits/SummaryHistograms/Occupancy_for_EndcapPositive", 'description': "<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Description</a>" }])

shiftrpclayout(dqmitems, "01-BarrelEfficiency",
          [{ 'path': "RPC/RPCEfficiency/Efficiency_Roll_vs_Sector_Wheel_-2", 'description': eff + rpclink },
           { 'path': "RPC/RPCEfficiency/Efficiency_Roll_vs_Sector_Wheel_-1", 'description': eff + rpclink  }],

          [{ 'path': "RPC/RPCEfficiency/Efficiency_Roll_vs_Sector_Wheel_0", 'description': eff + rpclink  },
           { 'path': "RPC/RPCEfficiency/Efficiency_Roll_vs_Sector_Wheel_+1", 'description': eff + rpclink  },
           { 'path': "RPC/RPCEfficiency/Efficiency_Roll_vs_Sector_Wheel_+2", 'description': eff + rpclink  }]
          )
shiftrpclayout(dqmitems, "01-EndCapEfficiency",
          [{ 'path': "RPC/RPCEfficiency/Efficiency_Roll_vs_Segment_Disk_-3", 'description': eff + rpclink },
           { 'path': "RPC/RPCEfficiency/Efficiency_Roll_vs_Segment_Disk_-2", 'description': eff + rpclink },
           { 'path': "RPC/RPCEfficiency/Efficiency_Roll_vs_Segment_Disk_-1", 'description': eff + rpclink }],

          [{ 'path': "RPC/RPCEfficiency/Efficiency_Roll_vs_Segment_Disk_1", 'description': eff + rpclink },
           { 'path': "RPC/RPCEfficiency/Efficiency_Roll_vs_Segment_Disk_2", 'description': eff + rpclink },
           { 'path': "RPC/RPCEfficiency/Efficiency_Roll_vs_Segment_Disk_3", 'description': eff + rpclink }],


          )
