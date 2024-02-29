# Generated automatically by dqmgui/gem_custom/fillLayouts.py 
#   in https://github.com/quark2/deployment/tree/addingGem
#   Recipe: 
#     cd deployment/dqmgui
#     python3 gem_custom/fillLayouts.py
def GEMLayout(i, p, *rows): i["GEM/Layouts/" + p] = DQMItem(layout=rows)

GEMLayout(dqmitems, 'Common/00 Summary', 
    [{'path': 'GEM/EventInfo/reportSummaryMap', 'description': 'For more information (... under construction)'}], 
    )


GEMLayout(dqmitems, 'Common/01 GE11-M-L1 Lumi-based chamber status', 
    [{'path': 'GEM/EventInfo/chamberStatus_inLumi_GE11-M-L1', 'description': 'Lumi-based chamber status in GE11-M-L1'}], 
    )


GEMLayout(dqmitems, 'Common/02 GE11-M-L2 Lumi-based chamber status', 
    [{'path': 'GEM/EventInfo/chamberStatus_inLumi_GE11-M-L2', 'description': 'Lumi-based chamber status in GE11-M-L2'}], 
    )


GEMLayout(dqmitems, 'Common/03 GE11-P-L1 Lumi-based chamber status', 
    [{'path': 'GEM/EventInfo/chamberStatus_inLumi_GE11-P-L1', 'description': 'Lumi-based chamber status in GE11-P-L1'}], 
    )


GEMLayout(dqmitems, 'Common/04 GE11-P-L2 Lumi-based chamber status', 
    [{'path': 'GEM/EventInfo/chamberStatus_inLumi_GE11-P-L2', 'description': 'Lumi-based chamber status in GE11-P-L2'}], 
    )


GEMLayout(dqmitems, 'Common/05 GE21-P-L2-M1 Lumi-based chamber status', 
    [{'path': 'GEM/EventInfo/chamberStatus_inLumi_GE21-P-L2-M1', 'description': 'Lumi-based chamber status in GE21-P-L2-M1'}], 
    )



GEMLayout(dqmitems, 'Common/06 GE21-P-L2-M2 Lumi-based chamber status', 
    [{'path': 'GEM/EventInfo/chamberStatus_inLumi_GE21-P-L2-M2', 'description': 'Lumi-based chamber status in GE21-P-L2-M2'}], 
    )



GEMLayout(dqmitems, 'Common/07 GE21-P-L2-M3 Lumi-based chamber status', 
    [{'path': 'GEM/EventInfo/chamberStatus_inLumi_GE21-P-L2-M3', 'description': 'Lumi-based chamber status in GE21-P-L2-M3'}], 
    )



GEMLayout(dqmitems, 'Common/08 GE21-P-L2-M4 Lumi-based chamber status', 
    [{'path': 'GEM/EventInfo/chamberStatus_inLumi_GE21-P-L2-M4', 'description': 'Lumi-based chamber status in GE21-P-L2-M4'}], 
    )


GEMLayout(dqmitems, 'Common/09 GE21-M-L2-M1 Lumi-based chamber status', 
    [{'path': 'GEM/EventInfo/chamberStatus_inLumi_GE21-M-L2-M1', 'description': 'Lumi-based chamber status in GE21-M-L2-M1'}], 
    )


GEMLayout(dqmitems, 'Common/10 GE21-M-L2-M2 Lumi-based chamber status', 
    [{'path': 'GEM/EventInfo/chamberStatus_inLumi_GE21-M-L2-M2', 'description': 'Lumi-based chamber status in GE21-M-L2-M2'}], 
    )



GEMLayout(dqmitems, 'Common/11 GE21-M-L2-M3 Lumi-based chamber status', 
    [{'path': 'GEM/EventInfo/chamberStatus_inLumi_GE21-M-L2-M3', 'description': 'Lumi-based chamber status in GE21-M-L2-M3'}], 
    )



GEMLayout(dqmitems, 'Common/12 GE21-M-L2-M4 Lumi-based chamber status', 
    [{'path': 'GEM/EventInfo/chamberStatus_inLumi_GE21-M-L2-M4', 'description': 'Lumi-based chamber status in GE21-M-L2-M4'}], 
    )




GEMLayout(dqmitems, 'Common/13 AMC13 status', 
    [{'path': 'GEM/DAQStatus/amc13_status', 'description': 'For more information (... under construction)'}], 
    )


GEMLayout(dqmitems, 'Common/14 AMC status GE11-M', 
    [{'path': 'GEM/DAQStatus/amc_status_GE11-M', 'description': 'For more information (... under construction)'}], 
    )


GEMLayout(dqmitems, 'Common/15 AMC status GE11-P', 
    [{'path': 'GEM/DAQStatus/amc_status_GE11-P', 'description': 'For more information (... under construction)'}], 
    )


GEMLayout(dqmitems, 'Common/16 AMC status GE21-P', 
    [{'path': 'GEM/DAQStatus/amc_status_GE21-P', 'description': 'For more information (... under construction)'}], 
    )


GEMLayout(dqmitems, 'Common/17 GE11-M-L1 OptoHybrid status', 
    [{'path': 'GEM/DAQStatus/oh_status_GE11-M-L1', 'description': 'OptoHybrid status in GE11-M-L1'}], 
    )


GEMLayout(dqmitems, 'Common/18 GE11-M-L2 OptoHybrid status', 
    [{'path': 'GEM/DAQStatus/oh_status_GE11-M-L2', 'description': 'OptoHybrid status in GE11-M-L2'}], 
    )


GEMLayout(dqmitems, 'Common/19 GE11-P-L1 OptoHybrid status', 
    [{'path': 'GEM/DAQStatus/oh_status_GE11-P-L1', 'description': 'OptoHybrid status in GE11-P-L1'}], 
    )


GEMLayout(dqmitems, 'Common/20 GE11-P-L2 OptoHybrid status', 
    [{'path': 'GEM/DAQStatus/oh_status_GE11-P-L2', 'description': 'OptoHybrid status in GE11-P-L2'}], 
    )


GEMLayout(dqmitems, 'Common/21 GE21-P-L2-M1 OptoHybrid status', 
    [{'path': 'GEM/DAQStatus/oh_status_GE21-P-L2-M1', 'description': 'OptoHybrid status in GE21-P-L2-M1'}], 
    )


GEMLayout(dqmitems, 'Common/22 GE21-P-L2-M2 OptoHybrid status', 
    [{'path': 'GEM/DAQStatus/oh_status_GE21-P-L2-M2', 'description': 'OptoHybrid status in GE21-P-L2-M2'}], 
    )


GEMLayout(dqmitems, 'Common/23 GE21-P-L2-M3 OptoHybrid status', 
    [{'path': 'GEM/DAQStatus/oh_status_GE21-P-L2-M3', 'description': 'OptoHybrid status in GE21-P-L2-M3'}], 
    )


GEMLayout(dqmitems, 'Common/24 GE21-P-L2-M4 OptoHybrid status', 
    [{'path': 'GEM/DAQStatus/oh_status_GE21-P-L2-M4', 'description': 'OptoHybrid status in GE21-P-L2-M4'}], 
    )


GEMLayout(dqmitems, 'Common/25 GE21-M-L2-M1 OptoHybrid status', 
    [{'path': 'GEM/DAQStatus/oh_status_GE21-M-L2-M1', 'description': 'OptoHybrid status in GE21-M-L2-M1'}], 
    )


GEMLayout(dqmitems, 'Common/26 GE21-M-L2-M2 OptoHybrid status', 
    [{'path': 'GEM/DAQStatus/oh_status_GE21-M-L2-M2', 'description': 'OptoHybrid status in GE21-M-L2-M2'}], 
    )


GEMLayout(dqmitems, 'Common/27 GE21-M-L2-M3 OptoHybrid status', 
    [{'path': 'GEM/DAQStatus/oh_status_GE21-M-L2-M3', 'description': 'OptoHybrid status in GE21-M-L2-M3'}], 
    )


GEMLayout(dqmitems, 'Common/28 GE21-M-L2-M4 OptoHybrid status', 
    [{'path': 'GEM/DAQStatus/oh_status_GE21-M-L2-M4', 'description': 'OptoHybrid status in GE21-M-L2-M4'}], 
    )



GEMLayout(dqmitems, 'Common/29 GE11-M-L1 VFAT status (chamber vs. VFAT)', 
    [{'path': 'GEM/EventInfo/vfat_statusSummary_GE11-M-L1', 'description': 'VFAT status (chamber vs. VFAT) in GE11-M-L1'}], 
    )


GEMLayout(dqmitems, 'Common/30 GE11-M-L2 VFAT status (chamber vs. VFAT)', 
    [{'path': 'GEM/EventInfo/vfat_statusSummary_GE11-M-L2', 'description': 'VFAT status (chamber vs. VFAT) in GE11-M-L2'}], 
    )


GEMLayout(dqmitems, 'Common/31 GE11-P-L1 VFAT status (chamber vs. VFAT)', 
    [{'path': 'GEM/EventInfo/vfat_statusSummary_GE11-P-L1', 'description': 'VFAT status (chamber vs. VFAT) in GE11-P-L1'}], 
    )


GEMLayout(dqmitems, 'Common/32 GE11-P-L2 VFAT status (chamber vs. VFAT)', 
    [{'path': 'GEM/EventInfo/vfat_statusSummary_GE11-P-L2', 'description': 'VFAT status (chamber vs. VFAT) in GE11-P-L2'}], 
    )



GEMLayout(dqmitems, 'Common/33 GE21-P-L2-M1 VFAT status (chamber vs. VFAT)', 
    [{'path': 'GEM/EventInfo/vfat_statusSummary_GE21-P-L2-M1', 'description': 'VFAT status (chamber vs. VFAT) in GE21-P-L2-M1'}], 
    )



GEMLayout(dqmitems, 'Common/34 GE21-P-L2-M2 VFAT status (chamber vs. VFAT)', 
    [{'path': 'GEM/EventInfo/vfat_statusSummary_GE21-P-L2-M2', 'description': 'VFAT status (chamber vs. VFAT) in GE21-P-L2-M2'}], 
    )



GEMLayout(dqmitems, 'Common/35 GE21-P-L2-M3 VFAT status (chamber vs. VFAT)', 
    [{'path': 'GEM/EventInfo/vfat_statusSummary_GE21-P-L2-M3', 'description': 'VFAT status (chamber vs. VFAT) in GE21-P-L2-M3'}], 
    )



GEMLayout(dqmitems, 'Common/36 GE21-P-L2-M4 VFAT status (chamber vs. VFAT)', 
    [{'path': 'GEM/EventInfo/vfat_statusSummary_GE21-P-L2-M4', 'description': 'VFAT status (chamber vs. VFAT) in GE21-P-L2-M4'}], 
    )


GEMLayout(dqmitems, 'Common/37 GE21-M-L2-M1 VFAT status (chamber vs. VFAT)', 
    [{'path': 'GEM/EventInfo/vfat_statusSummary_GE21-M-L2-M1', 'description': 'VFAT status (chamber vs. VFAT) in GE21-P-L2-M1'}], 
    )


GEMLayout(dqmitems, 'Common/38 GE21-M-L2-M2 VFAT status (chamber vs. VFAT)', 
    [{'path': 'GEM/EventInfo/vfat_statusSummary_GE21-M-L2-M2', 'description': 'VFAT status (chamber vs. VFAT) in GE21-P-L2-M2'}], 
    )



GEMLayout(dqmitems, 'Common/39 GE21-M-L2-M3 VFAT status (chamber vs. VFAT)', 
    [{'path': 'GEM/EventInfo/vfat_statusSummary_GE21-M-L2-M3', 'description': 'VFAT status (chamber vs. VFAT) in GE21-P-L2-M3'}], 
    )



GEMLayout(dqmitems, 'Common/40 GE21-M-L2-M4 VFAT status (chamber vs. VFAT)', 
    [{'path': 'GEM/EventInfo/vfat_statusSummary_GE21-M-L2-M4', 'description': 'VFAT status (chamber vs. VFAT) in GE21-P-L2-M4'}], 
    )



GEMLayout(dqmitems, 'Common/41 GE11-M-L1 recHit xy occupancy', 
    [{'path': 'GEM/RecHits/occ_xy_GE11-M-L1', 'description': 'recHit xy occupancy in GE11-M-L1'}], 
    )


GEMLayout(dqmitems, 'Common/42 GE11-M-L2 recHit xy occupancy', 
    [{'path': 'GEM/RecHits/occ_xy_GE11-M-L2', 'description': 'recHit xy occupancy in GE11-M-L2'}], 
    )


GEMLayout(dqmitems, 'Common/43 GE11-P-L1 recHit xy occupancy', 
    [{'path': 'GEM/RecHits/occ_xy_GE11-P-L1', 'description': 'recHit xy occupancy in GE11-P-L1'}], 
    )


GEMLayout(dqmitems, 'Common/44 GE11-P-L2 recHit xy occupancy', 
    [{'path': 'GEM/RecHits/occ_xy_GE11-P-L2', 'description': 'recHit xy occupancy in GE11-P-L2'}], 
    )


GEMLayout(dqmitems, 'Common/45 GE21-P-L2 recHit xy occupancy', 
    [{'path': 'GEM/RecHits/occ_xy_GE21-P-L2', 'description': 'recHit xy occupancy in GE21-P-L2'}], 
    )


GEMLayout(dqmitems, 'Common/46 GE11-M-L1 RecHit Average Cluster Size', 
    [{'path': 'GEM/RecHits/rechit_average_GE11-M-L1', 'description': 'RecHit Average Cluster Size (iEta vs Chamber) in GE11-M-L1'}], 
    )


GEMLayout(dqmitems, 'Common/47 GE11-M-L2 RecHit Average Cluster Size', 
    [{'path': 'GEM/RecHits/rechit_average_GE11-M-L2', 'description': 'RecHit Average Cluster Size (iEta vs Chamber) in GE11-M-L2'}], 
    )


GEMLayout(dqmitems, 'Common/48 GE11-P-L1 RecHit Average Cluster Size', 
    [{'path': 'GEM/RecHits/rechit_average_GE11-P-L1', 'description': 'RecHit Average Cluster Size (iEta vs Chamber) in GE11-P-L1'}], 
    )


GEMLayout(dqmitems, 'Common/49 GE11-P-L2 RecHit Average Cluster Size', 
    [{'path': 'GEM/RecHits/rechit_average_GE11-P-L2', 'description': 'RecHit Average Cluster Size (iEta vs Chamber) in GE11-P-L2'}], 
    )


GEMLayout(dqmitems, 'Common/50 GE21-P-L2 RecHit Average Cluster Size', 
    [{'path': 'GEM/RecHits/rechit_average_GE21-P-L2', 'description': 'RecHit Average Cluster Size (iEta vs Chamber) in GE21-P-L2'}], 
    )


GEMLayout(dqmitems, 'Common/51 GE11-M-L1 GEM-CSC segment efficiency', 
    [{'path': 'GEM/Efficiency/GEMCSCSegment/eff_chamber_GE11-M-L1', 'description': 'GEM-CSC segment efficiency in GE11-M-L1'}], 
    )


GEMLayout(dqmitems, 'Common/52 GE11-M-L2 GEM-CSC segment efficiency', 
    [{'path': 'GEM/Efficiency/GEMCSCSegment/eff_chamber_GE11-M-L2', 'description': 'GEM-CSC segment efficiency in GE11-M-L2'}], 
    )


GEMLayout(dqmitems, 'Common/53 GE11-P-L1 GEM-CSC segment efficiency', 
    [{'path': 'GEM/Efficiency/GEMCSCSegment/eff_chamber_GE11-P-L1', 'description': 'GEM-CSC segment efficiency in GE11-P-L1'}], 
    )


GEMLayout(dqmitems, 'Common/54 GE11-P-L2 GEM-CSC segment efficiency', 
    [{'path': 'GEM/Efficiency/GEMCSCSegment/eff_chamber_GE11-P-L2', 'description': 'GEM-CSC segment efficiency in GE11-P-L2'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/00 GE11-M-01L1-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L1/vfat_status_GE11-M-01L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L1/occ_GE11-M-01L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L1/cls_GE11-M-01L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/01 GE11-M-02L1-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L1/vfat_status_GE11-M-02L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L1/occ_GE11-M-02L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L1/cls_GE11-M-02L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/02 GE11-M-03L1-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L1/vfat_status_GE11-M-03L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L1/occ_GE11-M-03L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L1/cls_GE11-M-03L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/03 GE11-M-04L1-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L1/vfat_status_GE11-M-04L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L1/occ_GE11-M-04L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L1/cls_GE11-M-04L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/04 GE11-M-05L1-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L1/vfat_status_GE11-M-05L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L1/occ_GE11-M-05L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L1/cls_GE11-M-05L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/05 GE11-M-06L1-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L1/vfat_status_GE11-M-06L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L1/occ_GE11-M-06L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L1/cls_GE11-M-06L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/06 GE11-M-07L1-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L1/vfat_status_GE11-M-07L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L1/occ_GE11-M-07L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L1/cls_GE11-M-07L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/07 GE11-M-08L1-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L1/vfat_status_GE11-M-08L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L1/occ_GE11-M-08L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L1/cls_GE11-M-08L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/08 GE11-M-09L1-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L1/vfat_status_GE11-M-09L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L1/occ_GE11-M-09L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L1/cls_GE11-M-09L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/09 GE11-M-10L1-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L1/vfat_status_GE11-M-10L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L1/occ_GE11-M-10L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L1/cls_GE11-M-10L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/10 GE11-M-11L1-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L1/vfat_status_GE11-M-11L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L1/occ_GE11-M-11L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L1/cls_GE11-M-11L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/11 GE11-M-12L1-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L1/vfat_status_GE11-M-12L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L1/occ_GE11-M-12L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L1/cls_GE11-M-12L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/12 GE11-M-13L1-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L1/vfat_status_GE11-M-13L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L1/occ_GE11-M-13L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L1/cls_GE11-M-13L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/13 GE11-M-14L1-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L1/vfat_status_GE11-M-14L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L1/occ_GE11-M-14L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L1/cls_GE11-M-14L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/14 GE11-M-15L1-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L1/vfat_status_GE11-M-15L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L1/occ_GE11-M-15L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L1/cls_GE11-M-15L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/15 GE11-M-16L1-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L1/vfat_status_GE11-M-16L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L1/occ_GE11-M-16L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L1/cls_GE11-M-16L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/16 GE11-M-17L1-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L1/vfat_status_GE11-M-17L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L1/occ_GE11-M-17L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L1/cls_GE11-M-17L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/17 GE11-M-18L1-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L1/vfat_status_GE11-M-18L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L1/occ_GE11-M-18L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L1/cls_GE11-M-18L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/18 GE11-M-19L1-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L1/vfat_status_GE11-M-19L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L1/occ_GE11-M-19L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L1/cls_GE11-M-19L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/19 GE11-M-20L1-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L1/vfat_status_GE11-M-20L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L1/occ_GE11-M-20L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L1/cls_GE11-M-20L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/20 GE11-M-21L1-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L1/vfat_status_GE11-M-21L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L1/occ_GE11-M-21L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L1/cls_GE11-M-21L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/21 GE11-M-22L1-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L1/vfat_status_GE11-M-22L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L1/occ_GE11-M-22L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L1/cls_GE11-M-22L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/22 GE11-M-23L1-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L1/vfat_status_GE11-M-23L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L1/occ_GE11-M-23L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L1/cls_GE11-M-23L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/23 GE11-M-24L1-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L1/vfat_status_GE11-M-24L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L1/occ_GE11-M-24L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L1/cls_GE11-M-24L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/24 GE11-M-25L1-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L1/vfat_status_GE11-M-25L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L1/occ_GE11-M-25L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L1/cls_GE11-M-25L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/25 GE11-M-26L1-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L1/vfat_status_GE11-M-26L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L1/occ_GE11-M-26L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L1/cls_GE11-M-26L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/26 GE11-M-27L1-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L1/vfat_status_GE11-M-27L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L1/occ_GE11-M-27L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L1/cls_GE11-M-27L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/27 GE11-M-28L1-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L1/vfat_status_GE11-M-28L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L1/occ_GE11-M-28L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L1/cls_GE11-M-28L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/28 GE11-M-29L1-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L1/vfat_status_GE11-M-29L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L1/occ_GE11-M-29L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L1/cls_GE11-M-29L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/29 GE11-M-30L1-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L1/vfat_status_GE11-M-30L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L1/occ_GE11-M-30L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L1/cls_GE11-M-30L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/30 GE11-M-31L1-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L1/vfat_status_GE11-M-31L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L1/occ_GE11-M-31L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L1/cls_GE11-M-31L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/31 GE11-M-32L1-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L1/vfat_status_GE11-M-32L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L1/occ_GE11-M-32L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L1/cls_GE11-M-32L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/32 GE11-M-33L1-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L1/vfat_status_GE11-M-33L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L1/occ_GE11-M-33L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L1/cls_GE11-M-33L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/33 GE11-M-34L1-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L1/vfat_status_GE11-M-34L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L1/occ_GE11-M-34L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L1/cls_GE11-M-34L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/34 GE11-M-35L1-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L1/vfat_status_GE11-M-35L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L1/occ_GE11-M-35L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L1/cls_GE11-M-35L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/35 GE11-M-36L1-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L1/vfat_status_GE11-M-36L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L1/occ_GE11-M-36L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L1/cls_GE11-M-36L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/00 GE11-M-01L2-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L2/vfat_status_GE11-M-01L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L2/occ_GE11-M-01L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L2/cls_GE11-M-01L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/01 GE11-M-02L2-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L2/vfat_status_GE11-M-02L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L2/occ_GE11-M-02L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L2/cls_GE11-M-02L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/02 GE11-M-03L2-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L2/vfat_status_GE11-M-03L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L2/occ_GE11-M-03L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L2/cls_GE11-M-03L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/03 GE11-M-04L2-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L2/vfat_status_GE11-M-04L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L2/occ_GE11-M-04L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L2/cls_GE11-M-04L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/04 GE11-M-05L2-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L2/vfat_status_GE11-M-05L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L2/occ_GE11-M-05L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L2/cls_GE11-M-05L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/05 GE11-M-06L2-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L2/vfat_status_GE11-M-06L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L2/occ_GE11-M-06L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L2/cls_GE11-M-06L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/06 GE11-M-07L2-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L2/vfat_status_GE11-M-07L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L2/occ_GE11-M-07L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L2/cls_GE11-M-07L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/07 GE11-M-08L2-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L2/vfat_status_GE11-M-08L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L2/occ_GE11-M-08L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L2/cls_GE11-M-08L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/08 GE11-M-09L2-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L2/vfat_status_GE11-M-09L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L2/occ_GE11-M-09L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L2/cls_GE11-M-09L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/09 GE11-M-10L2-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L2/vfat_status_GE11-M-10L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L2/occ_GE11-M-10L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L2/cls_GE11-M-10L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/10 GE11-M-11L2-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L2/vfat_status_GE11-M-11L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L2/occ_GE11-M-11L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L2/cls_GE11-M-11L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/11 GE11-M-12L2-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L2/vfat_status_GE11-M-12L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L2/occ_GE11-M-12L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L2/cls_GE11-M-12L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/12 GE11-M-13L2-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L2/vfat_status_GE11-M-13L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L2/occ_GE11-M-13L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L2/cls_GE11-M-13L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/13 GE11-M-14L2-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L2/vfat_status_GE11-M-14L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L2/occ_GE11-M-14L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L2/cls_GE11-M-14L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/14 GE11-M-15L2-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L2/vfat_status_GE11-M-15L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L2/occ_GE11-M-15L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L2/cls_GE11-M-15L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/15 GE11-M-16L2-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L2/vfat_status_GE11-M-16L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L2/occ_GE11-M-16L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L2/cls_GE11-M-16L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/16 GE11-M-17L2-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L2/vfat_status_GE11-M-17L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L2/occ_GE11-M-17L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L2/cls_GE11-M-17L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/17 GE11-M-18L2-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L2/vfat_status_GE11-M-18L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L2/occ_GE11-M-18L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L2/cls_GE11-M-18L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/18 GE11-M-19L2-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L2/vfat_status_GE11-M-19L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L2/occ_GE11-M-19L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L2/cls_GE11-M-19L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/19 GE11-M-20L2-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L2/vfat_status_GE11-M-20L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L2/occ_GE11-M-20L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L2/cls_GE11-M-20L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/20 GE11-M-21L2-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L2/vfat_status_GE11-M-21L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L2/occ_GE11-M-21L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L2/cls_GE11-M-21L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/21 GE11-M-22L2-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L2/vfat_status_GE11-M-22L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L2/occ_GE11-M-22L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L2/cls_GE11-M-22L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/22 GE11-M-23L2-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L2/vfat_status_GE11-M-23L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L2/occ_GE11-M-23L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L2/cls_GE11-M-23L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/23 GE11-M-24L2-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L2/vfat_status_GE11-M-24L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L2/occ_GE11-M-24L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L2/cls_GE11-M-24L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/24 GE11-M-25L2-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L2/vfat_status_GE11-M-25L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L2/occ_GE11-M-25L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L2/cls_GE11-M-25L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/25 GE11-M-26L2-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L2/vfat_status_GE11-M-26L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L2/occ_GE11-M-26L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L2/cls_GE11-M-26L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/26 GE11-M-27L2-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L2/vfat_status_GE11-M-27L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L2/occ_GE11-M-27L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L2/cls_GE11-M-27L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/27 GE11-M-28L2-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L2/vfat_status_GE11-M-28L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L2/occ_GE11-M-28L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L2/cls_GE11-M-28L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/28 GE11-M-29L2-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L2/vfat_status_GE11-M-29L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L2/occ_GE11-M-29L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L2/cls_GE11-M-29L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/29 GE11-M-30L2-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L2/vfat_status_GE11-M-30L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L2/occ_GE11-M-30L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L2/cls_GE11-M-30L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/30 GE11-M-31L2-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L2/vfat_status_GE11-M-31L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L2/occ_GE11-M-31L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L2/cls_GE11-M-31L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/31 GE11-M-32L2-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L2/vfat_status_GE11-M-32L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L2/occ_GE11-M-32L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L2/cls_GE11-M-32L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/32 GE11-M-33L2-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L2/vfat_status_GE11-M-33L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L2/occ_GE11-M-33L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L2/cls_GE11-M-33L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/33 GE11-M-34L2-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L2/vfat_status_GE11-M-34L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L2/occ_GE11-M-34L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L2/cls_GE11-M-34L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/34 GE11-M-35L2-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L2/vfat_status_GE11-M-35L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L2/occ_GE11-M-35L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L2/cls_GE11-M-35L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/35 GE11-M-36L2-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-M-L2/vfat_status_GE11-M-36L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-M-L2/occ_GE11-M-36L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-M-L2/cls_GE11-M-36L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/00 GE11-P-01L1-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L1/vfat_status_GE11-P-01L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L1/occ_GE11-P-01L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L1/cls_GE11-P-01L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/01 GE11-P-02L1-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L1/vfat_status_GE11-P-02L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L1/occ_GE11-P-02L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L1/cls_GE11-P-02L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/02 GE11-P-03L1-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L1/vfat_status_GE11-P-03L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L1/occ_GE11-P-03L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L1/cls_GE11-P-03L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/03 GE11-P-04L1-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L1/vfat_status_GE11-P-04L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L1/occ_GE11-P-04L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L1/cls_GE11-P-04L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/04 GE11-P-05L1-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L1/vfat_status_GE11-P-05L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L1/occ_GE11-P-05L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L1/cls_GE11-P-05L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/05 GE11-P-06L1-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L1/vfat_status_GE11-P-06L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L1/occ_GE11-P-06L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L1/cls_GE11-P-06L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/06 GE11-P-07L1-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L1/vfat_status_GE11-P-07L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L1/occ_GE11-P-07L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L1/cls_GE11-P-07L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/07 GE11-P-08L1-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L1/vfat_status_GE11-P-08L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L1/occ_GE11-P-08L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L1/cls_GE11-P-08L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/08 GE11-P-09L1-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L1/vfat_status_GE11-P-09L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L1/occ_GE11-P-09L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L1/cls_GE11-P-09L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/09 GE11-P-10L1-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L1/vfat_status_GE11-P-10L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L1/occ_GE11-P-10L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L1/cls_GE11-P-10L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/10 GE11-P-11L1-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L1/vfat_status_GE11-P-11L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L1/occ_GE11-P-11L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L1/cls_GE11-P-11L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/11 GE11-P-12L1-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L1/vfat_status_GE11-P-12L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L1/occ_GE11-P-12L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L1/cls_GE11-P-12L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/12 GE11-P-13L1-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L1/vfat_status_GE11-P-13L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L1/occ_GE11-P-13L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L1/cls_GE11-P-13L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/13 GE11-P-14L1-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L1/vfat_status_GE11-P-14L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L1/occ_GE11-P-14L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L1/cls_GE11-P-14L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/14 GE11-P-15L1-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L1/vfat_status_GE11-P-15L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L1/occ_GE11-P-15L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L1/cls_GE11-P-15L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/15 GE11-P-16L1-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L1/vfat_status_GE11-P-16L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L1/occ_GE11-P-16L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L1/cls_GE11-P-16L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/16 GE11-P-17L1-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L1/vfat_status_GE11-P-17L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L1/occ_GE11-P-17L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L1/cls_GE11-P-17L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/17 GE11-P-18L1-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L1/vfat_status_GE11-P-18L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L1/occ_GE11-P-18L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L1/cls_GE11-P-18L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/18 GE11-P-19L1-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L1/vfat_status_GE11-P-19L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L1/occ_GE11-P-19L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L1/cls_GE11-P-19L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/19 GE11-P-20L1-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L1/vfat_status_GE11-P-20L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L1/occ_GE11-P-20L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L1/cls_GE11-P-20L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/20 GE11-P-21L1-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L1/vfat_status_GE11-P-21L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L1/occ_GE11-P-21L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L1/cls_GE11-P-21L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/21 GE11-P-22L1-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L1/vfat_status_GE11-P-22L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L1/occ_GE11-P-22L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L1/cls_GE11-P-22L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/22 GE11-P-23L1-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L1/vfat_status_GE11-P-23L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L1/occ_GE11-P-23L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L1/cls_GE11-P-23L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/23 GE11-P-24L1-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L1/vfat_status_GE11-P-24L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L1/occ_GE11-P-24L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L1/cls_GE11-P-24L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/24 GE11-P-25L1-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L1/vfat_status_GE11-P-25L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L1/occ_GE11-P-25L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L1/cls_GE11-P-25L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/25 GE11-P-26L1-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L1/vfat_status_GE11-P-26L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L1/occ_GE11-P-26L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L1/cls_GE11-P-26L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/26 GE11-P-27L1-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L1/vfat_status_GE11-P-27L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L1/occ_GE11-P-27L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L1/cls_GE11-P-27L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/27 GE11-P-28L1-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L1/vfat_status_GE11-P-28L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L1/occ_GE11-P-28L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L1/cls_GE11-P-28L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/28 GE11-P-29L1-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L1/vfat_status_GE11-P-29L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L1/occ_GE11-P-29L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L1/cls_GE11-P-29L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/29 GE11-P-30L1-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L1/vfat_status_GE11-P-30L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L1/occ_GE11-P-30L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L1/cls_GE11-P-30L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/30 GE11-P-31L1-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L1/vfat_status_GE11-P-31L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L1/occ_GE11-P-31L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L1/cls_GE11-P-31L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/31 GE11-P-32L1-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L1/vfat_status_GE11-P-32L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L1/occ_GE11-P-32L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L1/cls_GE11-P-32L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/32 GE11-P-33L1-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L1/vfat_status_GE11-P-33L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L1/occ_GE11-P-33L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L1/cls_GE11-P-33L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/33 GE11-P-34L1-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L1/vfat_status_GE11-P-34L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L1/occ_GE11-P-34L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L1/cls_GE11-P-34L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/34 GE11-P-35L1-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L1/vfat_status_GE11-P-35L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L1/occ_GE11-P-35L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L1/cls_GE11-P-35L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/35 GE11-P-36L1-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L1/vfat_status_GE11-P-36L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L1/occ_GE11-P-36L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L1/cls_GE11-P-36L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/00 GE11-P-01L2-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L2/vfat_status_GE11-P-01L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L2/occ_GE11-P-01L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L2/cls_GE11-P-01L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/01 GE11-P-02L2-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L2/vfat_status_GE11-P-02L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L2/occ_GE11-P-02L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L2/cls_GE11-P-02L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/02 GE11-P-03L2-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L2/vfat_status_GE11-P-03L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L2/occ_GE11-P-03L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L2/cls_GE11-P-03L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/03 GE11-P-04L2-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L2/vfat_status_GE11-P-04L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L2/occ_GE11-P-04L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L2/cls_GE11-P-04L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/04 GE11-P-05L2-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L2/vfat_status_GE11-P-05L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L2/occ_GE11-P-05L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L2/cls_GE11-P-05L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/05 GE11-P-06L2-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L2/vfat_status_GE11-P-06L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L2/occ_GE11-P-06L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L2/cls_GE11-P-06L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/06 GE11-P-07L2-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L2/vfat_status_GE11-P-07L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L2/occ_GE11-P-07L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L2/cls_GE11-P-07L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/07 GE11-P-08L2-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L2/vfat_status_GE11-P-08L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L2/occ_GE11-P-08L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L2/cls_GE11-P-08L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/08 GE11-P-09L2-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L2/vfat_status_GE11-P-09L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L2/occ_GE11-P-09L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L2/cls_GE11-P-09L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/09 GE11-P-10L2-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L2/vfat_status_GE11-P-10L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L2/occ_GE11-P-10L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L2/cls_GE11-P-10L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/10 GE11-P-11L2-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L2/vfat_status_GE11-P-11L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L2/occ_GE11-P-11L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L2/cls_GE11-P-11L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/11 GE11-P-12L2-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L2/vfat_status_GE11-P-12L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L2/occ_GE11-P-12L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L2/cls_GE11-P-12L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/12 GE11-P-13L2-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L2/vfat_status_GE11-P-13L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L2/occ_GE11-P-13L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L2/cls_GE11-P-13L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/13 GE11-P-14L2-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L2/vfat_status_GE11-P-14L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L2/occ_GE11-P-14L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L2/cls_GE11-P-14L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/14 GE11-P-15L2-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L2/vfat_status_GE11-P-15L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L2/occ_GE11-P-15L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L2/cls_GE11-P-15L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/15 GE11-P-16L2-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L2/vfat_status_GE11-P-16L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L2/occ_GE11-P-16L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L2/cls_GE11-P-16L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/16 GE11-P-17L2-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L2/vfat_status_GE11-P-17L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L2/occ_GE11-P-17L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L2/cls_GE11-P-17L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/17 GE11-P-18L2-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L2/vfat_status_GE11-P-18L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L2/occ_GE11-P-18L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L2/cls_GE11-P-18L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/18 GE11-P-19L2-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L2/vfat_status_GE11-P-19L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L2/occ_GE11-P-19L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L2/cls_GE11-P-19L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/19 GE11-P-20L2-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L2/vfat_status_GE11-P-20L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L2/occ_GE11-P-20L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L2/cls_GE11-P-20L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/20 GE11-P-21L2-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L2/vfat_status_GE11-P-21L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L2/occ_GE11-P-21L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L2/cls_GE11-P-21L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/21 GE11-P-22L2-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L2/vfat_status_GE11-P-22L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L2/occ_GE11-P-22L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L2/cls_GE11-P-22L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/22 GE11-P-23L2-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L2/vfat_status_GE11-P-23L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L2/occ_GE11-P-23L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L2/cls_GE11-P-23L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/23 GE11-P-24L2-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L2/vfat_status_GE11-P-24L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L2/occ_GE11-P-24L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L2/cls_GE11-P-24L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/24 GE11-P-25L2-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L2/vfat_status_GE11-P-25L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L2/occ_GE11-P-25L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L2/cls_GE11-P-25L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/25 GE11-P-26L2-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L2/vfat_status_GE11-P-26L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L2/occ_GE11-P-26L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L2/cls_GE11-P-26L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/26 GE11-P-27L2-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L2/vfat_status_GE11-P-27L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L2/occ_GE11-P-27L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L2/cls_GE11-P-27L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/27 GE11-P-28L2-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L2/vfat_status_GE11-P-28L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L2/occ_GE11-P-28L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L2/cls_GE11-P-28L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/28 GE11-P-29L2-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L2/vfat_status_GE11-P-29L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L2/occ_GE11-P-29L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L2/cls_GE11-P-29L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/29 GE11-P-30L2-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L2/vfat_status_GE11-P-30L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L2/occ_GE11-P-30L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L2/cls_GE11-P-30L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/30 GE11-P-31L2-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L2/vfat_status_GE11-P-31L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L2/occ_GE11-P-31L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L2/cls_GE11-P-31L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/31 GE11-P-32L2-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L2/vfat_status_GE11-P-32L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L2/occ_GE11-P-32L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L2/cls_GE11-P-32L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/32 GE11-P-33L2-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L2/vfat_status_GE11-P-33L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L2/occ_GE11-P-33L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L2/cls_GE11-P-33L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/33 GE11-P-34L2-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L2/vfat_status_GE11-P-34L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L2/occ_GE11-P-34L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L2/cls_GE11-P-34L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/34 GE11-P-35L2-S', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE11-P-L2/vfat_status_GE11-P-35L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE11-P-L2/occ_GE11-P-35L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE11-P-L2/cls_GE11-P-35L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+21 L2/00 GE21-P-16L2-M1-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE21-P-L2/vfat_status_GE21-P-16L2-M1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE21-P-L2/occ_GE21-P-16L2-M1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE21-P-L2/cls_GE21-P-16L2-M1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+21 L2/01 GE21-P-16L2-M2-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE21-P-L2/vfat_status_GE21-P-16L2-M2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE21-P-L2/occ_GE21-P-16L2-M2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE21-P-L2/cls_GE21-P-16L2-M2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+21 L2/02 GE21-P-16L2-M3-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE21-P-L2/vfat_status_GE21-P-16L2-M3-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE21-P-L2/occ_GE21-P-16L2-M3-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE21-P-L2/cls_GE21-P-16L2-M3-L', 'description': 'VFAT vs ClusterSize'}], 
    )

GEMLayout(dqmitems, 'GE+21 L2/03 GE21-P-16L2-M4-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE21-P-L2/vfat_status_GE21-P-16L2-M4-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE21-P-L2/occ_GE21-P-16L2-M4-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE21-P-L2/cls_GE21-P-16L2-M$-L', 'description': 'VFAT vs ClusterSize'}], 
    )

GEMLayout(dqmitems, 'GE+21 L2/00 GE21-M-16L2-M1-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE21-M-L2/vfat_status_GE21-M-16L2-M1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE21-M-L2/occ_GE21-M-16L2-M1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE21-M-L2/cls_GE21-M-16L2-M1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+21 L2/01 GE21-M-16L2-M2-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE21-M-L2/vfat_status_GE21-M-16L2-M2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE21-M-L2/occ_GE21-M-16L2-M2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE21-M-L2/cls_GE21-M-16L2-M2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+21 L2/02 GE21-M-16L2-M3-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE21-M-L2/vfat_status_GE21-M-16L2-M3-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE21-M-L2/occ_GE21-M-16L2-M3-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE21-M-L2/cls_GE21-M-16L2-M3-L', 'description': 'VFAT vs ClusterSize'}], 
    )

GEMLayout(dqmitems, 'GE+21 L2/03 GE21-M-16L2-M4-L', 
    [{'path': 'GEM/DAQStatus/VFATStatus_GE21-M-L2/vfat_status_GE21-M-16L2-M4-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occupancy_GE21-M-L2/occ_GE21-M-16L2-M4-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/clusterSize_GE21-M-L2/cls_GE21-M-16L2-M$-L', 'description': 'VFAT vs ClusterSize'}], 
    )


