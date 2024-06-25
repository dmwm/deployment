def pfClusterlayout(
    i, p, *rows): i["ParticleFlow/Layouts/" + p] = DQMItem(layout=rows)


pfClusterlayout(dqmitems, "000 - Compare PFCluster Depths",
   [{'path':  "ParticleFlow/pfCaloGPUCompDir/pfCluster_Depth_HostvsDevice",
      'description': "PFCluster depth GPU vs CPU",
      'draw': {'withref': "no", 'drawopts': "COLZ"}}]
   )

pfClusterlayout(dqmitems, "001 - Compare PFCluster Duplicates",
   [{'path':  "ParticleFlow/pfCaloGPUCompDir/pfCluster_Duplicates_HostvsDevice",
      'description': "PFCluster duplicates GPU vs CPU",
      'draw': {'withref': "no"}}]
   )

pfClusterlayout(dqmitems, "002 - Compare PFCluster Energy",
   [{'path':  "ParticleFlow/pfCaloGPUCompDir/pfCluster_Energy_HostvsDevice",
      'description': "PFCluster Energy [Gev] GPU vs CPU",
      'draw': {'withref': "no", 'drawopts': "COLZ"}}]
   )

pfClusterlayout(dqmitems, "003 - Compare PFCluster eta",
   [{'path':  "ParticleFlow/pfCaloGPUCompDir/pfCluster_Eta_HostvsDevice",
      'description': "PFCluster eta GPU vs CPU",
      'draw': {'withref': "no", 'drawopts': "COLZ"}}]

pfClusterlayout(dqmitems, "004 - Compare PFCluster phi",
   [{'path':  "ParticleFlow/pfCaloGPUCompDir/pfCluster_Phi_HostvsDevice",
      'description': "PFCluster Phi GPU vs CPU",
      'draw': {'withref': "no", 'drawopts': "COLZ"}}]
   )

pfClusterlayout(dqmitems, "005 - Compare Number of PFCluster",
   [{'path':  "ParticleFlow/pfCaloGPUCompDir/pfCluster_Multiplicity_HostvsDevice",
      'description': "Number of PFCluster GPU vs CPU",
      'draw': {'withref': "no", 'drawopts': "COLZ"}}]
   )

pfClusterlayout(dqmitems, "006 - Compare PFCluster Rechit multiplicity",
   [{'path':  "ParticleFlow/pfCaloGPUCompDir/pfCluster_RecHitMultiplicity_HostvsDevice",
      'description': "RecHit multiplicity in PFClusters GPU vs CPU",
      'draw': {'withref': "no", 'drawopts': "COLZ"}}]
   )
