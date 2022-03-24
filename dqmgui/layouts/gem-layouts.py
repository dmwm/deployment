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


GEMLayout(dqmitems, 'Common/05 AMC13 status', 
    [{'path': 'GEM/DAQStatus/amc13_status', 'description': 'For more information (... under construction)'}], 
    )


GEMLayout(dqmitems, 'Common/06 AMC status GE11-M', 
    [{'path': 'GEM/DAQStatus/amc_status_GE11-M', 'description': 'For more information (... under construction)'}], 
    )


GEMLayout(dqmitems, 'Common/07 AMC status GE11-P', 
    [{'path': 'GEM/DAQStatus/amc_status_GE11-P', 'description': 'For more information (... under construction)'}], 
    )


GEMLayout(dqmitems, 'Common/08 GE11-M-L1 OptoHybrid status', 
    [{'path': 'GEM/DAQStatus/oh_status_GE11-M-L1', 'description': 'OptoHybrid status in GE11-M-L1'}], 
    )


GEMLayout(dqmitems, 'Common/09 GE11-M-L2 OptoHybrid status', 
    [{'path': 'GEM/DAQStatus/oh_status_GE11-M-L2', 'description': 'OptoHybrid status in GE11-M-L2'}], 
    )


GEMLayout(dqmitems, 'Common/10 GE11-P-L1 OptoHybrid status', 
    [{'path': 'GEM/DAQStatus/oh_status_GE11-P-L1', 'description': 'OptoHybrid status in GE11-P-L1'}], 
    )


GEMLayout(dqmitems, 'Common/11 GE11-P-L2 OptoHybrid status', 
    [{'path': 'GEM/DAQStatus/oh_status_GE11-P-L2', 'description': 'OptoHybrid status in GE11-P-L2'}], 
    )


GEMLayout(dqmitems, 'Common/12 GE11-M-L1 VFAT status', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-L1', 'description': 'VFAT status in GE11-M-L1'}], 
    )


GEMLayout(dqmitems, 'Common/13 GE11-M-L2 VFAT status', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-L2', 'description': 'VFAT status in GE11-M-L2'}], 
    )


GEMLayout(dqmitems, 'Common/14 GE11-P-L1 VFAT status', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-L1', 'description': 'VFAT status in GE11-P-L1'}], 
    )


GEMLayout(dqmitems, 'Common/15 GE11-P-L2 VFAT status', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-L2', 'description': 'VFAT status in GE11-P-L2'}], 
    )


GEMLayout(dqmitems, 'Common/16 GE11-M-L1 VFAT status (chamber vs. VFAT)', 
    [{'path': 'GEM/EventInfo/vfat_statusSummary_GE11-M-L1', 'description': 'VFAT status (chamber vs. VFAT) in GE11-M-L1'}], 
    )


GEMLayout(dqmitems, 'Common/17 GE11-M-L2 VFAT status (chamber vs. VFAT)', 
    [{'path': 'GEM/EventInfo/vfat_statusSummary_GE11-M-L2', 'description': 'VFAT status (chamber vs. VFAT) in GE11-M-L2'}], 
    )


GEMLayout(dqmitems, 'Common/18 GE11-P-L1 VFAT status (chamber vs. VFAT)', 
    [{'path': 'GEM/EventInfo/vfat_statusSummary_GE11-P-L1', 'description': 'VFAT status (chamber vs. VFAT) in GE11-P-L1'}], 
    )


GEMLayout(dqmitems, 'Common/19 GE11-P-L2 VFAT status (chamber vs. VFAT)', 
    [{'path': 'GEM/EventInfo/vfat_statusSummary_GE11-P-L2', 'description': 'VFAT status (chamber vs. VFAT) in GE11-P-L2'}], 
    )


GEMLayout(dqmitems, 'Common/20 GE11-M-L1 recHit wheel occupancy', 
    [{'path': 'GEM/RecHits/rphi_occ_GE11-M-L1', 'description': 'recHit wheel occupancy in GE11-M-L1'}], 
    )


GEMLayout(dqmitems, 'Common/21 GE11-M-L2 recHit wheel occupancy', 
    [{'path': 'GEM/RecHits/rphi_occ_GE11-M-L2', 'description': 'recHit wheel occupancy in GE11-M-L2'}], 
    )


GEMLayout(dqmitems, 'Common/22 GE11-P-L1 recHit wheel occupancy', 
    [{'path': 'GEM/RecHits/rphi_occ_GE11-P-L1', 'description': 'recHit wheel occupancy in GE11-P-L1'}], 
    )


GEMLayout(dqmitems, 'Common/23 GE11-P-L2 recHit wheel occupancy', 
    [{'path': 'GEM/RecHits/rphi_occ_GE11-P-L2', 'description': 'recHit wheel occupancy in GE11-P-L2'}], 
    )


GEMLayout(dqmitems, 'Common/24 GE11-M-L1 digi occupancy', 
    [{'path': 'GEM/Digis/det_GE11-M-L1', 'description': 'Digi occupancy in GE11-M-L1'}], 
    )


GEMLayout(dqmitems, 'Common/25 GE11-M-L2 digi occupancy', 
    [{'path': 'GEM/Digis/det_GE11-M-L2', 'description': 'Digi occupancy in GE11-M-L2'}], 
    )


GEMLayout(dqmitems, 'Common/26 GE11-P-L1 digi occupancy', 
    [{'path': 'GEM/Digis/det_GE11-P-L1', 'description': 'Digi occupancy in GE11-P-L1'}], 
    )


GEMLayout(dqmitems, 'Common/27 GE11-P-L2 digi occupancy', 
    [{'path': 'GEM/Digis/det_GE11-P-L2', 'description': 'Digi occupancy in GE11-P-L2'}], 
    )


GEMLayout(dqmitems, 'Common/28 GE11-M-L1 recHit occupancy', 
    [{'path': 'GEM/RecHits/det_GE11-M-L1', 'description': 'RecHits occupancy in GE11-M-L1'}], 
    )


GEMLayout(dqmitems, 'Common/29 GE11-M-L2 recHit occupancy', 
    [{'path': 'GEM/RecHits/det_GE11-M-L2', 'description': 'RecHits occupancy in GE11-M-L2'}], 
    )


GEMLayout(dqmitems, 'Common/30 GE11-P-L1 recHit occupancy', 
    [{'path': 'GEM/RecHits/det_GE11-P-L1', 'description': 'RecHits occupancy in GE11-P-L1'}], 
    )


GEMLayout(dqmitems, 'Common/31 GE11-P-L2 recHit occupancy', 
    [{'path': 'GEM/RecHits/det_GE11-P-L2', 'description': 'RecHits occupancy in GE11-P-L2'}], 
    )


GEMLayout(dqmitems, 'Common/32 GE11-M-L1 RecHit Average Cluster Size', 
    [{'path': 'GEM/RecHits/rechit_average_GE11-M-L1', 'description': 'RecHit Average Cluster Size (iEta vs Chamber) in GE11-M-L1'}], 
    )


GEMLayout(dqmitems, 'Common/33 GE11-M-L2 RecHit Average Cluster Size', 
    [{'path': 'GEM/RecHits/rechit_average_GE11-M-L2', 'description': 'RecHit Average Cluster Size (iEta vs Chamber) in GE11-M-L2'}], 
    )


GEMLayout(dqmitems, 'Common/34 GE11-P-L1 RecHit Average Cluster Size', 
    [{'path': 'GEM/RecHits/rechit_average_GE11-P-L1', 'description': 'RecHit Average Cluster Size (iEta vs Chamber) in GE11-P-L1'}], 
    )


GEMLayout(dqmitems, 'Common/35 GE11-P-L2 RecHit Average Cluster Size', 
    [{'path': 'GEM/RecHits/rechit_average_GE11-P-L2', 'description': 'RecHit Average Cluster Size (iEta vs Chamber) in GE11-P-L2'}], 
    )


GEMLayout(dqmitems, 'Common/36 GE11-M-L1 Large Cluster Occupancy', 
    [{'path': 'GEM/RecHits/largeCls_occ_GE11-M-L1', 'description': 'Large Cluster (>5) Occupancy (iEta vs Chamber) in GE11-M-L1'}], 
    )


GEMLayout(dqmitems, 'Common/37 GE11-M-L2 Large Cluster Occupancy', 
    [{'path': 'GEM/RecHits/largeCls_occ_GE11-M-L2', 'description': 'Large Cluster (>5) Occupancy (iEta vs Chamber) in GE11-M-L2'}], 
    )


GEMLayout(dqmitems, 'Common/38 GE11-P-L1 Large Cluster Occupancy', 
    [{'path': 'GEM/RecHits/largeCls_occ_GE11-P-L1', 'description': 'Large Cluster (>5) Occupancy (iEta vs Chamber) in GE11-P-L1'}], 
    )


GEMLayout(dqmitems, 'Common/39 GE11-P-L2 Large Cluster Occupancy', 
    [{'path': 'GEM/RecHits/largeCls_occ_GE11-P-L2', 'description': 'Large Cluster (>5) Occupancy (iEta vs Chamber) in GE11-P-L2'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/00 GE11-M-L1 digi occupancy vs phi', 
    [{'path': 'GEM/Digis/occ_phi_GE11-M-L1', 'description': 'Digi occupancy vs phi in GE11-M-L1'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/01 GE11-M-L2 digi occupancy vs phi', 
    [{'path': 'GEM/Digis/occ_phi_GE11-M-L2', 'description': 'Digi occupancy vs phi in GE11-M-L2'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/02 GE11-P-L1 digi occupancy vs phi', 
    [{'path': 'GEM/Digis/occ_phi_GE11-P-L1', 'description': 'Digi occupancy vs phi in GE11-P-L1'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/03 GE11-P-L2 digi occupancy vs phi', 
    [{'path': 'GEM/Digis/occ_phi_GE11-P-L2', 'description': 'Digi occupancy vs phi in GE11-P-L2'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/04 GE11-M-L1 digi occupancy vs iEta', 
    [{'path': 'GEM/Digis/occ_ieta_GE11-M-L1', 'description': 'Digi occupancy vs iEta in GE11-M-L1'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/05 GE11-M-L2 digi occupancy vs iEta', 
    [{'path': 'GEM/Digis/occ_ieta_GE11-M-L2', 'description': 'Digi occupancy vs iEta in GE11-M-L2'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/06 GE11-P-L1 digi occupancy vs iEta', 
    [{'path': 'GEM/Digis/occ_ieta_GE11-P-L1', 'description': 'Digi occupancy vs iEta in GE11-P-L1'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/07 GE11-P-L2 digi occupancy vs iEta', 
    [{'path': 'GEM/Digis/occ_ieta_GE11-P-L2', 'description': 'Digi occupancy vs iEta in GE11-P-L2'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/08 GE11-M-L1 total number of digis per event', 
    [{'path': 'GEM/Digis/digis_per_layer_GE11-M-L1', 'description': 'Total number of digis per event in GE11-M-L1'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/09 GE11-M-L2 total number of digis per event', 
    [{'path': 'GEM/Digis/digis_per_layer_GE11-M-L2', 'description': 'Total number of digis per event in GE11-M-L2'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/10 GE11-P-L1 total number of digis per event', 
    [{'path': 'GEM/Digis/digis_per_layer_GE11-P-L1', 'description': 'Total number of digis per event in GE11-P-L1'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/11 GE11-P-L2 total number of digis per event', 
    [{'path': 'GEM/Digis/digis_per_layer_GE11-P-L2', 'description': 'Total number of digis per event in GE11-P-L2'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/12 GE11-M-E01 total number of digis per event', 
    [{'path': 'GEM/Digis/digis_per_ieta_GE11-M-E01', 'description': 'Total number of digis per event in GE11-M-E01'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/13 GE11-M-E02 total number of digis per event', 
    [{'path': 'GEM/Digis/digis_per_ieta_GE11-M-E02', 'description': 'Total number of digis per event in GE11-M-E02'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/14 GE11-M-E03 total number of digis per event', 
    [{'path': 'GEM/Digis/digis_per_ieta_GE11-M-E03', 'description': 'Total number of digis per event in GE11-M-E03'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/15 GE11-M-E04 total number of digis per event', 
    [{'path': 'GEM/Digis/digis_per_ieta_GE11-M-E04', 'description': 'Total number of digis per event in GE11-M-E04'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/16 GE11-M-E05 total number of digis per event', 
    [{'path': 'GEM/Digis/digis_per_ieta_GE11-M-E05', 'description': 'Total number of digis per event in GE11-M-E05'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/17 GE11-M-E06 total number of digis per event', 
    [{'path': 'GEM/Digis/digis_per_ieta_GE11-M-E06', 'description': 'Total number of digis per event in GE11-M-E06'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/18 GE11-M-E07 total number of digis per event', 
    [{'path': 'GEM/Digis/digis_per_ieta_GE11-M-E07', 'description': 'Total number of digis per event in GE11-M-E07'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/19 GE11-M-E08 total number of digis per event', 
    [{'path': 'GEM/Digis/digis_per_ieta_GE11-M-E08', 'description': 'Total number of digis per event in GE11-M-E08'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/20 GE11-P-E01 total number of digis per event', 
    [{'path': 'GEM/Digis/digis_per_ieta_GE11-P-E01', 'description': 'Total number of digis per event in GE11-P-E01'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/21 GE11-P-E02 total number of digis per event', 
    [{'path': 'GEM/Digis/digis_per_ieta_GE11-P-E02', 'description': 'Total number of digis per event in GE11-P-E02'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/22 GE11-P-E03 total number of digis per event', 
    [{'path': 'GEM/Digis/digis_per_ieta_GE11-P-E03', 'description': 'Total number of digis per event in GE11-P-E03'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/23 GE11-P-E04 total number of digis per event', 
    [{'path': 'GEM/Digis/digis_per_ieta_GE11-P-E04', 'description': 'Total number of digis per event in GE11-P-E04'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/24 GE11-P-E05 total number of digis per event', 
    [{'path': 'GEM/Digis/digis_per_ieta_GE11-P-E05', 'description': 'Total number of digis per event in GE11-P-E05'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/25 GE11-P-E06 total number of digis per event', 
    [{'path': 'GEM/Digis/digis_per_ieta_GE11-P-E06', 'description': 'Total number of digis per event in GE11-P-E06'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/26 GE11-P-E07 total number of digis per event', 
    [{'path': 'GEM/Digis/digis_per_ieta_GE11-P-E07', 'description': 'Total number of digis per event in GE11-P-E07'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/27 GE11-P-E08 total number of digis per event', 
    [{'path': 'GEM/Digis/digis_per_ieta_GE11-P-E08', 'description': 'Total number of digis per event in GE11-P-E08'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/28 GE11-M-E01 bunch crossing', 
    [{'path': 'GEM/Digis/bx_GE11-M-E01', 'description': 'Bunch crossing in GE11-M-E01'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/29 GE11-M-E02 bunch crossing', 
    [{'path': 'GEM/Digis/bx_GE11-M-E02', 'description': 'Bunch crossing in GE11-M-E02'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/30 GE11-M-E03 bunch crossing', 
    [{'path': 'GEM/Digis/bx_GE11-M-E03', 'description': 'Bunch crossing in GE11-M-E03'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/31 GE11-M-E04 bunch crossing', 
    [{'path': 'GEM/Digis/bx_GE11-M-E04', 'description': 'Bunch crossing in GE11-M-E04'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/32 GE11-M-E05 bunch crossing', 
    [{'path': 'GEM/Digis/bx_GE11-M-E05', 'description': 'Bunch crossing in GE11-M-E05'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/33 GE11-M-E06 bunch crossing', 
    [{'path': 'GEM/Digis/bx_GE11-M-E06', 'description': 'Bunch crossing in GE11-M-E06'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/34 GE11-M-E07 bunch crossing', 
    [{'path': 'GEM/Digis/bx_GE11-M-E07', 'description': 'Bunch crossing in GE11-M-E07'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/35 GE11-M-E08 bunch crossing', 
    [{'path': 'GEM/Digis/bx_GE11-M-E08', 'description': 'Bunch crossing in GE11-M-E08'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/36 GE11-P-E01 bunch crossing', 
    [{'path': 'GEM/Digis/bx_GE11-P-E01', 'description': 'Bunch crossing in GE11-P-E01'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/37 GE11-P-E02 bunch crossing', 
    [{'path': 'GEM/Digis/bx_GE11-P-E02', 'description': 'Bunch crossing in GE11-P-E02'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/38 GE11-P-E03 bunch crossing', 
    [{'path': 'GEM/Digis/bx_GE11-P-E03', 'description': 'Bunch crossing in GE11-P-E03'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/39 GE11-P-E04 bunch crossing', 
    [{'path': 'GEM/Digis/bx_GE11-P-E04', 'description': 'Bunch crossing in GE11-P-E04'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/40 GE11-P-E05 bunch crossing', 
    [{'path': 'GEM/Digis/bx_GE11-P-E05', 'description': 'Bunch crossing in GE11-P-E05'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/41 GE11-P-E06 bunch crossing', 
    [{'path': 'GEM/Digis/bx_GE11-P-E06', 'description': 'Bunch crossing in GE11-P-E06'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/42 GE11-P-E07 bunch crossing', 
    [{'path': 'GEM/Digis/bx_GE11-P-E07', 'description': 'Bunch crossing in GE11-P-E07'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/43 GE11-P-E08 bunch crossing', 
    [{'path': 'GEM/Digis/bx_GE11-P-E08', 'description': 'Bunch crossing in GE11-P-E08'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/44 GE11-M-01L1-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-01L1-S', 'description': 'Digi occupancy in GE11-M-01L1-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/45 GE11-M-02L1-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-02L1-L', 'description': 'Digi occupancy in GE11-M-02L1-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/46 GE11-M-03L1-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-03L1-S', 'description': 'Digi occupancy in GE11-M-03L1-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/47 GE11-M-04L1-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-04L1-L', 'description': 'Digi occupancy in GE11-M-04L1-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/48 GE11-M-05L1-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-05L1-S', 'description': 'Digi occupancy in GE11-M-05L1-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/49 GE11-M-06L1-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-06L1-L', 'description': 'Digi occupancy in GE11-M-06L1-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/50 GE11-M-07L1-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-07L1-S', 'description': 'Digi occupancy in GE11-M-07L1-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/51 GE11-M-08L1-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-08L1-L', 'description': 'Digi occupancy in GE11-M-08L1-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/52 GE11-M-09L1-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-09L1-S', 'description': 'Digi occupancy in GE11-M-09L1-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/53 GE11-M-10L1-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-10L1-L', 'description': 'Digi occupancy in GE11-M-10L1-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/54 GE11-M-11L1-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-11L1-S', 'description': 'Digi occupancy in GE11-M-11L1-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/55 GE11-M-12L1-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-12L1-L', 'description': 'Digi occupancy in GE11-M-12L1-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/56 GE11-M-13L1-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-13L1-S', 'description': 'Digi occupancy in GE11-M-13L1-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/57 GE11-M-14L1-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-14L1-L', 'description': 'Digi occupancy in GE11-M-14L1-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/58 GE11-M-15L1-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-15L1-S', 'description': 'Digi occupancy in GE11-M-15L1-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/59 GE11-M-16L1-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-16L1-L', 'description': 'Digi occupancy in GE11-M-16L1-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/60 GE11-M-17L1-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-17L1-S', 'description': 'Digi occupancy in GE11-M-17L1-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/61 GE11-M-18L1-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-18L1-L', 'description': 'Digi occupancy in GE11-M-18L1-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/62 GE11-M-19L1-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-19L1-S', 'description': 'Digi occupancy in GE11-M-19L1-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/63 GE11-M-20L1-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-20L1-L', 'description': 'Digi occupancy in GE11-M-20L1-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/64 GE11-M-21L1-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-21L1-S', 'description': 'Digi occupancy in GE11-M-21L1-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/65 GE11-M-22L1-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-22L1-L', 'description': 'Digi occupancy in GE11-M-22L1-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/66 GE11-M-23L1-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-23L1-S', 'description': 'Digi occupancy in GE11-M-23L1-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/67 GE11-M-24L1-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-24L1-L', 'description': 'Digi occupancy in GE11-M-24L1-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/68 GE11-M-25L1-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-25L1-S', 'description': 'Digi occupancy in GE11-M-25L1-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/69 GE11-M-26L1-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-26L1-L', 'description': 'Digi occupancy in GE11-M-26L1-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/70 GE11-M-27L1-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-27L1-S', 'description': 'Digi occupancy in GE11-M-27L1-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/71 GE11-M-28L1-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-28L1-L', 'description': 'Digi occupancy in GE11-M-28L1-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/72 GE11-M-29L1-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-29L1-S', 'description': 'Digi occupancy in GE11-M-29L1-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/73 GE11-M-30L1-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-30L1-L', 'description': 'Digi occupancy in GE11-M-30L1-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/74 GE11-M-31L1-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-31L1-S', 'description': 'Digi occupancy in GE11-M-31L1-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/75 GE11-M-32L1-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-32L1-L', 'description': 'Digi occupancy in GE11-M-32L1-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/76 GE11-M-33L1-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-33L1-S', 'description': 'Digi occupancy in GE11-M-33L1-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/77 GE11-M-34L1-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-34L1-L', 'description': 'Digi occupancy in GE11-M-34L1-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/78 GE11-M-35L1-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-35L1-S', 'description': 'Digi occupancy in GE11-M-35L1-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/79 GE11-M-36L1-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-36L1-L', 'description': 'Digi occupancy in GE11-M-36L1-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/80 GE11-M-01L2-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-01L2-S', 'description': 'Digi occupancy in GE11-M-01L2-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/81 GE11-M-02L2-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-02L2-L', 'description': 'Digi occupancy in GE11-M-02L2-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/82 GE11-M-03L2-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-03L2-S', 'description': 'Digi occupancy in GE11-M-03L2-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/83 GE11-M-04L2-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-04L2-L', 'description': 'Digi occupancy in GE11-M-04L2-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/84 GE11-M-05L2-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-05L2-S', 'description': 'Digi occupancy in GE11-M-05L2-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/85 GE11-M-06L2-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-06L2-L', 'description': 'Digi occupancy in GE11-M-06L2-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/86 GE11-M-07L2-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-07L2-S', 'description': 'Digi occupancy in GE11-M-07L2-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/87 GE11-M-08L2-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-08L2-L', 'description': 'Digi occupancy in GE11-M-08L2-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/88 GE11-M-09L2-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-09L2-S', 'description': 'Digi occupancy in GE11-M-09L2-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/89 GE11-M-10L2-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-10L2-L', 'description': 'Digi occupancy in GE11-M-10L2-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/90 GE11-M-11L2-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-11L2-S', 'description': 'Digi occupancy in GE11-M-11L2-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/91 GE11-M-12L2-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-12L2-L', 'description': 'Digi occupancy in GE11-M-12L2-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/92 GE11-M-13L2-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-13L2-S', 'description': 'Digi occupancy in GE11-M-13L2-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/93 GE11-M-14L2-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-14L2-L', 'description': 'Digi occupancy in GE11-M-14L2-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/94 GE11-M-15L2-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-15L2-S', 'description': 'Digi occupancy in GE11-M-15L2-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/95 GE11-M-16L2-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-16L2-L', 'description': 'Digi occupancy in GE11-M-16L2-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/96 GE11-M-17L2-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-17L2-S', 'description': 'Digi occupancy in GE11-M-17L2-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/97 GE11-M-18L2-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-18L2-L', 'description': 'Digi occupancy in GE11-M-18L2-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/98 GE11-M-19L2-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-19L2-S', 'description': 'Digi occupancy in GE11-M-19L2-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/99 GE11-M-20L2-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-20L2-L', 'description': 'Digi occupancy in GE11-M-20L2-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/100 GE11-M-21L2-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-21L2-S', 'description': 'Digi occupancy in GE11-M-21L2-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/101 GE11-M-22L2-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-22L2-L', 'description': 'Digi occupancy in GE11-M-22L2-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/102 GE11-M-23L2-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-23L2-S', 'description': 'Digi occupancy in GE11-M-23L2-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/103 GE11-M-24L2-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-24L2-L', 'description': 'Digi occupancy in GE11-M-24L2-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/104 GE11-M-25L2-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-25L2-S', 'description': 'Digi occupancy in GE11-M-25L2-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/105 GE11-M-26L2-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-26L2-L', 'description': 'Digi occupancy in GE11-M-26L2-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/106 GE11-M-27L2-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-27L2-S', 'description': 'Digi occupancy in GE11-M-27L2-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/107 GE11-M-28L2-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-28L2-L', 'description': 'Digi occupancy in GE11-M-28L2-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/108 GE11-M-29L2-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-29L2-S', 'description': 'Digi occupancy in GE11-M-29L2-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/109 GE11-M-30L2-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-30L2-L', 'description': 'Digi occupancy in GE11-M-30L2-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/110 GE11-M-31L2-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-31L2-S', 'description': 'Digi occupancy in GE11-M-31L2-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/111 GE11-M-32L2-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-32L2-L', 'description': 'Digi occupancy in GE11-M-32L2-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/112 GE11-M-33L2-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-33L2-S', 'description': 'Digi occupancy in GE11-M-33L2-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/113 GE11-M-34L2-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-34L2-L', 'description': 'Digi occupancy in GE11-M-34L2-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/114 GE11-M-35L2-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-35L2-S', 'description': 'Digi occupancy in GE11-M-35L2-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/115 GE11-M-36L2-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-M-36L2-L', 'description': 'Digi occupancy in GE11-M-36L2-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/116 GE11-P-01L1-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-01L1-S', 'description': 'Digi occupancy in GE11-P-01L1-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/117 GE11-P-02L1-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-02L1-L', 'description': 'Digi occupancy in GE11-P-02L1-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/118 GE11-P-03L1-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-03L1-S', 'description': 'Digi occupancy in GE11-P-03L1-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/119 GE11-P-04L1-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-04L1-L', 'description': 'Digi occupancy in GE11-P-04L1-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/120 GE11-P-05L1-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-05L1-S', 'description': 'Digi occupancy in GE11-P-05L1-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/121 GE11-P-06L1-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-06L1-L', 'description': 'Digi occupancy in GE11-P-06L1-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/122 GE11-P-07L1-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-07L1-S', 'description': 'Digi occupancy in GE11-P-07L1-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/123 GE11-P-08L1-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-08L1-L', 'description': 'Digi occupancy in GE11-P-08L1-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/124 GE11-P-09L1-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-09L1-S', 'description': 'Digi occupancy in GE11-P-09L1-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/125 GE11-P-10L1-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-10L1-L', 'description': 'Digi occupancy in GE11-P-10L1-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/126 GE11-P-11L1-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-11L1-S', 'description': 'Digi occupancy in GE11-P-11L1-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/127 GE11-P-12L1-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-12L1-L', 'description': 'Digi occupancy in GE11-P-12L1-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/128 GE11-P-13L1-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-13L1-S', 'description': 'Digi occupancy in GE11-P-13L1-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/129 GE11-P-14L1-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-14L1-L', 'description': 'Digi occupancy in GE11-P-14L1-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/130 GE11-P-15L1-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-15L1-S', 'description': 'Digi occupancy in GE11-P-15L1-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/131 GE11-P-16L1-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-16L1-L', 'description': 'Digi occupancy in GE11-P-16L1-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/132 GE11-P-17L1-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-17L1-S', 'description': 'Digi occupancy in GE11-P-17L1-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/133 GE11-P-18L1-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-18L1-L', 'description': 'Digi occupancy in GE11-P-18L1-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/134 GE11-P-19L1-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-19L1-S', 'description': 'Digi occupancy in GE11-P-19L1-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/135 GE11-P-20L1-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-20L1-L', 'description': 'Digi occupancy in GE11-P-20L1-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/136 GE11-P-21L1-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-21L1-S', 'description': 'Digi occupancy in GE11-P-21L1-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/137 GE11-P-22L1-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-22L1-L', 'description': 'Digi occupancy in GE11-P-22L1-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/138 GE11-P-23L1-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-23L1-S', 'description': 'Digi occupancy in GE11-P-23L1-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/139 GE11-P-24L1-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-24L1-L', 'description': 'Digi occupancy in GE11-P-24L1-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/140 GE11-P-25L1-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-25L1-S', 'description': 'Digi occupancy in GE11-P-25L1-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/141 GE11-P-26L1-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-26L1-L', 'description': 'Digi occupancy in GE11-P-26L1-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/142 GE11-P-27L1-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-27L1-S', 'description': 'Digi occupancy in GE11-P-27L1-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/143 GE11-P-28L1-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-28L1-L', 'description': 'Digi occupancy in GE11-P-28L1-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/144 GE11-P-29L1-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-29L1-S', 'description': 'Digi occupancy in GE11-P-29L1-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/145 GE11-P-30L1-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-30L1-L', 'description': 'Digi occupancy in GE11-P-30L1-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/146 GE11-P-31L1-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-31L1-S', 'description': 'Digi occupancy in GE11-P-31L1-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/147 GE11-P-32L1-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-32L1-L', 'description': 'Digi occupancy in GE11-P-32L1-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/148 GE11-P-33L1-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-33L1-S', 'description': 'Digi occupancy in GE11-P-33L1-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/149 GE11-P-34L1-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-34L1-L', 'description': 'Digi occupancy in GE11-P-34L1-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/150 GE11-P-35L1-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-35L1-S', 'description': 'Digi occupancy in GE11-P-35L1-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/151 GE11-P-36L1-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-36L1-L', 'description': 'Digi occupancy in GE11-P-36L1-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/152 GE11-P-01L2-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-01L2-S', 'description': 'Digi occupancy in GE11-P-01L2-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/153 GE11-P-02L2-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-02L2-L', 'description': 'Digi occupancy in GE11-P-02L2-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/154 GE11-P-03L2-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-03L2-S', 'description': 'Digi occupancy in GE11-P-03L2-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/155 GE11-P-04L2-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-04L2-L', 'description': 'Digi occupancy in GE11-P-04L2-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/156 GE11-P-05L2-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-05L2-S', 'description': 'Digi occupancy in GE11-P-05L2-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/157 GE11-P-06L2-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-06L2-L', 'description': 'Digi occupancy in GE11-P-06L2-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/158 GE11-P-07L2-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-07L2-S', 'description': 'Digi occupancy in GE11-P-07L2-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/159 GE11-P-08L2-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-08L2-L', 'description': 'Digi occupancy in GE11-P-08L2-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/160 GE11-P-09L2-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-09L2-S', 'description': 'Digi occupancy in GE11-P-09L2-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/161 GE11-P-10L2-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-10L2-L', 'description': 'Digi occupancy in GE11-P-10L2-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/162 GE11-P-11L2-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-11L2-S', 'description': 'Digi occupancy in GE11-P-11L2-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/163 GE11-P-12L2-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-12L2-L', 'description': 'Digi occupancy in GE11-P-12L2-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/164 GE11-P-13L2-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-13L2-S', 'description': 'Digi occupancy in GE11-P-13L2-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/165 GE11-P-14L2-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-14L2-L', 'description': 'Digi occupancy in GE11-P-14L2-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/166 GE11-P-15L2-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-15L2-S', 'description': 'Digi occupancy in GE11-P-15L2-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/167 GE11-P-16L2-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-16L2-L', 'description': 'Digi occupancy in GE11-P-16L2-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/168 GE11-P-17L2-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-17L2-S', 'description': 'Digi occupancy in GE11-P-17L2-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/169 GE11-P-18L2-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-18L2-L', 'description': 'Digi occupancy in GE11-P-18L2-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/170 GE11-P-19L2-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-19L2-S', 'description': 'Digi occupancy in GE11-P-19L2-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/171 GE11-P-20L2-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-20L2-L', 'description': 'Digi occupancy in GE11-P-20L2-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/172 GE11-P-21L2-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-21L2-S', 'description': 'Digi occupancy in GE11-P-21L2-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/173 GE11-P-22L2-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-22L2-L', 'description': 'Digi occupancy in GE11-P-22L2-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/174 GE11-P-23L2-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-23L2-S', 'description': 'Digi occupancy in GE11-P-23L2-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/175 GE11-P-24L2-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-24L2-L', 'description': 'Digi occupancy in GE11-P-24L2-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/176 GE11-P-25L2-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-25L2-S', 'description': 'Digi occupancy in GE11-P-25L2-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/177 GE11-P-26L2-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-26L2-L', 'description': 'Digi occupancy in GE11-P-26L2-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/178 GE11-P-27L2-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-27L2-S', 'description': 'Digi occupancy in GE11-P-27L2-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/179 GE11-P-28L2-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-28L2-L', 'description': 'Digi occupancy in GE11-P-28L2-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/180 GE11-P-29L2-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-29L2-S', 'description': 'Digi occupancy in GE11-P-29L2-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/181 GE11-P-30L2-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-30L2-L', 'description': 'Digi occupancy in GE11-P-30L2-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/182 GE11-P-31L2-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-31L2-S', 'description': 'Digi occupancy in GE11-P-31L2-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/183 GE11-P-32L2-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-32L2-L', 'description': 'Digi occupancy in GE11-P-32L2-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/184 GE11-P-33L2-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-33L2-S', 'description': 'Digi occupancy in GE11-P-33L2-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/185 GE11-P-34L2-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-34L2-L', 'description': 'Digi occupancy in GE11-P-34L2-L'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/186 GE11-P-35L2-S digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-35L2-S', 'description': 'Digi occupancy in GE11-P-35L2-S'}], 
    )


GEMLayout(dqmitems, 'Common_Digis/187 GE11-P-36L2-L digi occupancy', 
    [{'path': 'GEM/Digis/occ_GE11-P-36L2-L', 'description': 'Digi occupancy in GE11-P-36L2-L'}], 
    )


GEMLayout(dqmitems, 'Common_RecHits/00 GE11-M-L1 recHit occupancy vs iEta', 
    [{'path': 'GEM/RecHits/occ_ieta_GE11-M-L1', 'description': 'recHit occupancy vs iEta in GE11-M-L1'}], 
    )


GEMLayout(dqmitems, 'Common_RecHits/01 GE11-M-L2 recHit occupancy vs iEta', 
    [{'path': 'GEM/RecHits/occ_ieta_GE11-M-L2', 'description': 'recHit occupancy vs iEta in GE11-M-L2'}], 
    )


GEMLayout(dqmitems, 'Common_RecHits/02 GE11-P-L1 recHit occupancy vs iEta', 
    [{'path': 'GEM/RecHits/occ_ieta_GE11-P-L1', 'description': 'recHit occupancy vs iEta in GE11-P-L1'}], 
    )


GEMLayout(dqmitems, 'Common_RecHits/03 GE11-P-L2 recHit occupancy vs iEta', 
    [{'path': 'GEM/RecHits/occ_ieta_GE11-P-L2', 'description': 'recHit occupancy vs iEta in GE11-P-L2'}], 
    )


GEMLayout(dqmitems, 'Common_RecHits/04 GE11-M-L1 recHit occupancy vs phi', 
    [{'path': 'GEM/RecHits/occ_phi_GE11-M-L1', 'description': 'recHit occupancy vs phi in GE11-M-L1'}], 
    )


GEMLayout(dqmitems, 'Common_RecHits/05 GE11-M-L2 recHit occupancy vs phi', 
    [{'path': 'GEM/RecHits/occ_phi_GE11-M-L2', 'description': 'recHit occupancy vs phi in GE11-M-L2'}], 
    )


GEMLayout(dqmitems, 'Common_RecHits/06 GE11-P-L1 recHit occupancy vs phi', 
    [{'path': 'GEM/RecHits/occ_phi_GE11-P-L1', 'description': 'recHit occupancy vs phi in GE11-P-L1'}], 
    )


GEMLayout(dqmitems, 'Common_RecHits/07 GE11-P-L2 recHit occupancy vs phi', 
    [{'path': 'GEM/RecHits/occ_phi_GE11-P-L2', 'description': 'recHit occupancy vs phi in GE11-P-L2'}], 
    )


GEMLayout(dqmitems, 'Common_RecHits/08 GE11-E01 Cluster size', 
    [{'path': 'GEM/RecHits/cls_GE11-E01', 'description': 'Total number of recHits per event in GE11-E01'}], 
    )


GEMLayout(dqmitems, 'Common_RecHits/09 GE11-E02 Cluster size', 
    [{'path': 'GEM/RecHits/cls_GE11-E02', 'description': 'Total number of recHits per event in GE11-E02'}], 
    )


GEMLayout(dqmitems, 'Common_RecHits/10 GE11-E03 Cluster size', 
    [{'path': 'GEM/RecHits/cls_GE11-E03', 'description': 'Total number of recHits per event in GE11-E03'}], 
    )


GEMLayout(dqmitems, 'Common_RecHits/11 GE11-E04 Cluster size', 
    [{'path': 'GEM/RecHits/cls_GE11-E04', 'description': 'Total number of recHits per event in GE11-E04'}], 
    )


GEMLayout(dqmitems, 'Common_RecHits/12 GE11-E05 Cluster size', 
    [{'path': 'GEM/RecHits/cls_GE11-E05', 'description': 'Total number of recHits per event in GE11-E05'}], 
    )


GEMLayout(dqmitems, 'Common_RecHits/13 GE11-E06 Cluster size', 
    [{'path': 'GEM/RecHits/cls_GE11-E06', 'description': 'Total number of recHits per event in GE11-E06'}], 
    )


GEMLayout(dqmitems, 'Common_RecHits/14 GE11-E07 Cluster size', 
    [{'path': 'GEM/RecHits/cls_GE11-E07', 'description': 'Total number of recHits per event in GE11-E07'}], 
    )


GEMLayout(dqmitems, 'Common_RecHits/15 GE11-E08 Cluster size', 
    [{'path': 'GEM/RecHits/cls_GE11-E08', 'description': 'Total number of recHits per event in GE11-E08'}], 
    )


GEMLayout(dqmitems, 'Common_RecHits/16 GE11-M-L1 total number of recHits per event', 
    [{'path': 'GEM/RecHits/rechits_per_layer_GE11-M-L1', 'description': 'Total number of recHits per event in GE11-M-L1'}], 
    )


GEMLayout(dqmitems, 'Common_RecHits/17 GE11-M-L2 total number of recHits per event', 
    [{'path': 'GEM/RecHits/rechits_per_layer_GE11-M-L2', 'description': 'Total number of recHits per event in GE11-M-L2'}], 
    )


GEMLayout(dqmitems, 'Common_RecHits/18 GE11-P-L1 total number of recHits per event', 
    [{'path': 'GEM/RecHits/rechits_per_layer_GE11-P-L1', 'description': 'Total number of recHits per event in GE11-P-L1'}], 
    )


GEMLayout(dqmitems, 'Common_RecHits/19 GE11-P-L2 total number of recHits per event', 
    [{'path': 'GEM/RecHits/rechits_per_layer_GE11-P-L2', 'description': 'Total number of recHits per event in GE11-P-L2'}], 
    )


GEMLayout(dqmitems, 'Common_RecHits/20 GE11-M-E01 total number of recHits per event', 
    [{'path': 'GEM/RecHits/rechits_per_ieta_GE11-M-E01', 'description': 'Total number of recHits per event in GE11-M-E01'}], 
    )


GEMLayout(dqmitems, 'Common_RecHits/21 GE11-M-E02 total number of recHits per event', 
    [{'path': 'GEM/RecHits/rechits_per_ieta_GE11-M-E02', 'description': 'Total number of recHits per event in GE11-M-E02'}], 
    )


GEMLayout(dqmitems, 'Common_RecHits/22 GE11-M-E03 total number of recHits per event', 
    [{'path': 'GEM/RecHits/rechits_per_ieta_GE11-M-E03', 'description': 'Total number of recHits per event in GE11-M-E03'}], 
    )


GEMLayout(dqmitems, 'Common_RecHits/23 GE11-M-E04 total number of recHits per event', 
    [{'path': 'GEM/RecHits/rechits_per_ieta_GE11-M-E04', 'description': 'Total number of recHits per event in GE11-M-E04'}], 
    )


GEMLayout(dqmitems, 'Common_RecHits/24 GE11-M-E05 total number of recHits per event', 
    [{'path': 'GEM/RecHits/rechits_per_ieta_GE11-M-E05', 'description': 'Total number of recHits per event in GE11-M-E05'}], 
    )


GEMLayout(dqmitems, 'Common_RecHits/25 GE11-M-E06 total number of recHits per event', 
    [{'path': 'GEM/RecHits/rechits_per_ieta_GE11-M-E06', 'description': 'Total number of recHits per event in GE11-M-E06'}], 
    )


GEMLayout(dqmitems, 'Common_RecHits/26 GE11-M-E07 total number of recHits per event', 
    [{'path': 'GEM/RecHits/rechits_per_ieta_GE11-M-E07', 'description': 'Total number of recHits per event in GE11-M-E07'}], 
    )


GEMLayout(dqmitems, 'Common_RecHits/27 GE11-M-E08 total number of recHits per event', 
    [{'path': 'GEM/RecHits/rechits_per_ieta_GE11-M-E08', 'description': 'Total number of recHits per event in GE11-M-E08'}], 
    )


GEMLayout(dqmitems, 'Common_RecHits/28 GE11-P-E01 total number of recHits per event', 
    [{'path': 'GEM/RecHits/rechits_per_ieta_GE11-P-E01', 'description': 'Total number of recHits per event in GE11-P-E01'}], 
    )


GEMLayout(dqmitems, 'Common_RecHits/29 GE11-P-E02 total number of recHits per event', 
    [{'path': 'GEM/RecHits/rechits_per_ieta_GE11-P-E02', 'description': 'Total number of recHits per event in GE11-P-E02'}], 
    )


GEMLayout(dqmitems, 'Common_RecHits/30 GE11-P-E03 total number of recHits per event', 
    [{'path': 'GEM/RecHits/rechits_per_ieta_GE11-P-E03', 'description': 'Total number of recHits per event in GE11-P-E03'}], 
    )


GEMLayout(dqmitems, 'Common_RecHits/31 GE11-P-E04 total number of recHits per event', 
    [{'path': 'GEM/RecHits/rechits_per_ieta_GE11-P-E04', 'description': 'Total number of recHits per event in GE11-P-E04'}], 
    )


GEMLayout(dqmitems, 'Common_RecHits/32 GE11-P-E05 total number of recHits per event', 
    [{'path': 'GEM/RecHits/rechits_per_ieta_GE11-P-E05', 'description': 'Total number of recHits per event in GE11-P-E05'}], 
    )


GEMLayout(dqmitems, 'Common_RecHits/33 GE11-P-E06 total number of recHits per event', 
    [{'path': 'GEM/RecHits/rechits_per_ieta_GE11-P-E06', 'description': 'Total number of recHits per event in GE11-P-E06'}], 
    )


GEMLayout(dqmitems, 'Common_RecHits/34 GE11-P-E07 total number of recHits per event', 
    [{'path': 'GEM/RecHits/rechits_per_ieta_GE11-P-E07', 'description': 'Total number of recHits per event in GE11-P-E07'}], 
    )


GEMLayout(dqmitems, 'Common_RecHits/35 GE11-P-E08 total number of recHits per event', 
    [{'path': 'GEM/RecHits/rechits_per_ieta_GE11-P-E08', 'description': 'Total number of recHits per event in GE11-P-E08'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/00 GE11-M-01L1-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-01L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-01L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-01L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/01 GE11-M-02L1-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-02L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-02L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-02L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/02 GE11-M-03L1-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-03L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-03L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-03L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/03 GE11-M-04L1-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-04L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-04L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-04L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/04 GE11-M-05L1-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-05L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-05L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-05L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/05 GE11-M-06L1-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-06L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-06L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-06L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/06 GE11-M-07L1-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-07L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-07L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-07L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/07 GE11-M-08L1-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-08L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-08L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-08L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/08 GE11-M-09L1-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-09L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-09L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-09L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/09 GE11-M-10L1-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-10L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-10L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-10L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/10 GE11-M-11L1-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-11L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-11L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-11L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/11 GE11-M-12L1-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-12L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-12L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-12L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/12 GE11-M-13L1-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-13L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-13L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-13L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/13 GE11-M-14L1-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-14L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-14L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-14L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/14 GE11-M-15L1-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-15L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-15L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-15L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/15 GE11-M-16L1-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-16L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-16L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-16L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/16 GE11-M-17L1-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-17L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-17L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-17L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/17 GE11-M-18L1-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-18L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-18L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-18L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/18 GE11-M-19L1-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-19L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-19L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-19L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/19 GE11-M-20L1-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-20L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-20L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-20L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/20 GE11-M-21L1-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-21L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-21L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-21L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/21 GE11-M-22L1-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-22L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-22L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-22L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/22 GE11-M-23L1-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-23L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-23L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-23L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/23 GE11-M-24L1-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-24L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-24L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-24L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/24 GE11-M-25L1-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-25L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-25L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-25L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/25 GE11-M-26L1-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-26L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-26L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-26L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/26 GE11-M-27L1-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-27L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-27L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-27L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/27 GE11-M-28L1-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-28L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-28L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-28L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/28 GE11-M-29L1-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-29L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-29L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-29L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/29 GE11-M-30L1-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-30L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-30L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-30L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/30 GE11-M-31L1-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-31L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-31L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-31L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/31 GE11-M-32L1-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-32L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-32L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-32L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/32 GE11-M-33L1-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-33L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-33L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-33L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/33 GE11-M-34L1-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-34L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-34L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-34L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/34 GE11-M-35L1-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-35L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-35L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-35L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L1/35 GE11-M-36L1-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-36L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-36L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-36L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/00 GE11-M-01L2-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-01L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-01L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-01L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/01 GE11-M-02L2-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-02L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-02L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-02L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/02 GE11-M-03L2-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-03L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-03L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-03L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/03 GE11-M-04L2-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-04L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-04L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-04L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/04 GE11-M-05L2-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-05L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-05L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-05L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/05 GE11-M-06L2-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-06L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-06L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-06L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/06 GE11-M-07L2-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-07L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-07L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-07L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/07 GE11-M-08L2-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-08L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-08L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-08L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/08 GE11-M-09L2-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-09L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-09L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-09L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/09 GE11-M-10L2-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-10L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-10L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-10L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/10 GE11-M-11L2-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-11L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-11L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-11L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/11 GE11-M-12L2-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-12L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-12L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-12L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/12 GE11-M-13L2-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-13L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-13L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-13L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/13 GE11-M-14L2-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-14L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-14L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-14L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/14 GE11-M-15L2-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-15L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-15L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-15L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/15 GE11-M-16L2-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-16L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-16L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-16L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/16 GE11-M-17L2-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-17L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-17L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-17L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/17 GE11-M-18L2-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-18L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-18L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-18L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/18 GE11-M-19L2-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-19L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-19L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-19L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/19 GE11-M-20L2-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-20L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-20L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-20L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/20 GE11-M-21L2-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-21L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-21L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-21L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/21 GE11-M-22L2-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-22L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-22L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-22L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/22 GE11-M-23L2-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-23L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-23L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-23L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/23 GE11-M-24L2-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-24L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-24L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-24L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/24 GE11-M-25L2-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-25L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-25L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-25L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/25 GE11-M-26L2-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-26L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-26L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-26L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/26 GE11-M-27L2-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-27L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-27L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-27L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/27 GE11-M-28L2-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-28L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-28L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-28L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/28 GE11-M-29L2-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-29L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-29L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-29L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/29 GE11-M-30L2-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-30L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-30L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-30L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/30 GE11-M-31L2-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-31L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-31L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-31L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/31 GE11-M-32L2-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-32L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-32L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-32L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/32 GE11-M-33L2-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-33L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-33L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-33L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/33 GE11-M-34L2-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-34L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-34L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-34L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/34 GE11-M-35L2-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-35L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-35L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-35L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE-11 L2/35 GE11-M-36L2-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-36L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-M-36L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-M-36L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/00 GE11-P-01L1-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-01L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-01L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-01L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/01 GE11-P-02L1-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-02L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-02L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-02L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/02 GE11-P-03L1-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-03L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-03L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-03L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/03 GE11-P-04L1-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-04L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-04L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-04L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/04 GE11-P-05L1-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-05L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-05L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-05L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/05 GE11-P-06L1-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-06L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-06L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-06L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/06 GE11-P-07L1-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-07L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-07L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-07L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/07 GE11-P-08L1-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-08L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-08L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-08L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/08 GE11-P-09L1-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-09L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-09L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-09L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/09 GE11-P-10L1-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-10L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-10L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-10L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/10 GE11-P-11L1-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-11L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-11L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-11L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/11 GE11-P-12L1-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-12L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-12L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-12L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/12 GE11-P-13L1-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-13L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-13L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-13L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/13 GE11-P-14L1-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-14L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-14L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-14L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/14 GE11-P-15L1-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-15L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-15L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-15L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/15 GE11-P-16L1-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-16L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-16L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-16L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/16 GE11-P-17L1-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-17L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-17L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-17L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/17 GE11-P-18L1-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-18L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-18L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-18L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/18 GE11-P-19L1-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-19L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-19L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-19L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/19 GE11-P-20L1-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-20L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-20L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-20L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/20 GE11-P-21L1-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-21L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-21L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-21L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/21 GE11-P-22L1-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-22L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-22L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-22L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/22 GE11-P-23L1-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-23L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-23L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-23L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/23 GE11-P-24L1-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-24L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-24L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-24L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/24 GE11-P-25L1-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-25L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-25L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-25L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/25 GE11-P-26L1-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-26L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-26L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-26L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/26 GE11-P-27L1-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-27L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-27L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-27L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/27 GE11-P-28L1-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-28L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-28L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-28L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/28 GE11-P-29L1-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-29L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-29L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-29L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/29 GE11-P-30L1-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-30L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-30L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-30L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/30 GE11-P-31L1-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-31L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-31L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-31L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/31 GE11-P-32L1-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-32L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-32L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-32L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/32 GE11-P-33L1-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-33L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-33L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-33L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/33 GE11-P-34L1-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-34L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-34L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-34L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/34 GE11-P-35L1-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-35L1-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-35L1-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-35L1-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L1/35 GE11-P-36L1-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-36L1-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-36L1-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-36L1-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/00 GE11-P-01L2-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-01L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-01L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-01L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/01 GE11-P-02L2-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-02L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-02L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-02L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/02 GE11-P-03L2-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-03L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-03L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-03L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/03 GE11-P-04L2-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-04L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-04L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-04L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/04 GE11-P-05L2-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-05L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-05L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-05L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/05 GE11-P-06L2-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-06L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-06L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-06L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/06 GE11-P-07L2-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-07L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-07L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-07L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/07 GE11-P-08L2-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-08L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-08L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-08L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/08 GE11-P-09L2-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-09L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-09L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-09L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/09 GE11-P-10L2-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-10L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-10L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-10L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/10 GE11-P-11L2-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-11L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-11L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-11L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/11 GE11-P-12L2-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-12L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-12L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-12L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/12 GE11-P-13L2-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-13L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-13L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-13L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/13 GE11-P-14L2-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-14L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-14L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-14L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/14 GE11-P-15L2-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-15L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-15L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-15L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/15 GE11-P-16L2-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-16L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-16L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-16L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/16 GE11-P-17L2-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-17L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-17L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-17L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/17 GE11-P-18L2-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-18L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-18L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-18L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/18 GE11-P-19L2-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-19L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-19L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-19L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/19 GE11-P-20L2-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-20L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-20L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-20L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/20 GE11-P-21L2-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-21L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-21L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-21L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/21 GE11-P-22L2-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-22L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-22L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-22L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/22 GE11-P-23L2-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-23L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-23L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-23L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/23 GE11-P-24L2-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-24L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-24L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-24L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/24 GE11-P-25L2-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-25L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-25L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-25L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/25 GE11-P-26L2-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-26L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-26L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-26L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/26 GE11-P-27L2-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-27L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-27L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-27L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/27 GE11-P-28L2-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-28L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-28L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-28L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/28 GE11-P-29L2-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-29L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-29L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-29L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/29 GE11-P-30L2-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-30L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-30L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-30L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/30 GE11-P-31L2-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-31L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-31L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-31L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/31 GE11-P-32L2-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-32L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-32L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-32L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/32 GE11-P-33L2-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-33L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-33L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-33L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/33 GE11-P-34L2-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-34L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-34L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-34L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/34 GE11-P-35L2-S', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-35L2-S', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-35L2-S', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-35L2-S', 'description': 'VFAT vs ClusterSize'}], 
    )


GEMLayout(dqmitems, 'GE+11 L2/35 GE11-P-36L2-L', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-36L2-L', 'description': 'VFAT status'}], 
    [{'path': 'GEM/Digis/occ_GE11-P-36L2-L', 'description': 'Digi occupancy'}, {'path': 'GEM/RecHits/cls_GE11-P-36L2-L', 'description': 'VFAT vs ClusterSize'}], 
    )

