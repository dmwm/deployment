# Generated automatically by dqmgui/gem_custom/fillLayouts.py 
#   in https://github.com/quark2/deployment/tree/addingGem
#   Recipe: 
#     cd deployment/dqmgui
#     python3 gem_custom/fillLayouts.py
def GEMLayout(i, p, *rows): i["GEM/Layouts/" + p] = DQMItem(layout=rows)

GEMLayout(dqmitems, 'Common/00 Summary', 
    [{'path': 'GEM/EventInfo/reportSummaryMap', 'description': 'For more information (... under construction)'}], 
    )
GEMLayout(dqmitems, 'Common/01 AMC status positive endcap', 
    [{'path': 'GEM/DAQStatus/amc_statusflagPos', 'description': 'For more information (... under construction)'}], 
    )
GEMLayout(dqmitems, 'Common/02 AMC status negative endcap', 
    [{'path': 'GEM/DAQStatus/amc_statusflagNeg', 'description': 'For more information (... under construction)'}], 
    )
GEMLayout(dqmitems, 'Common/03 GE-11L1 GEB input status', 
    [{'path': 'GEM/DAQStatus/geb_input_status_re-1_st1_la1', 'description': 'GEB input status in GE-1/1 Layer 1'}], 
    )
GEMLayout(dqmitems, 'Common/04 GE-11L2 GEB input status', 
    [{'path': 'GEM/DAQStatus/geb_input_status_re-1_st1_la2', 'description': 'GEB input status in GE-1/1 Layer 2'}], 
    )
GEMLayout(dqmitems, 'Common/05 GE+11L1 GEB input status', 
    [{'path': 'GEM/DAQStatus/geb_input_status_re1_st1_la1', 'description': 'GEB input status in GE+1/1 Layer 1'}], 
    )
GEMLayout(dqmitems, 'Common/06 GE+11L2 GEB input status', 
    [{'path': 'GEM/DAQStatus/geb_input_status_re1_st1_la2', 'description': 'GEB input status in GE+1/1 Layer 2'}], 
    )
GEMLayout(dqmitems, 'Common/07 GE-11L1 VFAT input status', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la1', 'description': 'VFAT input status in GE-1/1 Layer 1'}], 
    )
GEMLayout(dqmitems, 'Common/08 GE-11L2 VFAT input status', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la2', 'description': 'VFAT input status in GE-1/1 Layer 2'}], 
    )
GEMLayout(dqmitems, 'Common/09 GE+11L1 VFAT input status', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la1', 'description': 'VFAT input status in GE+1/1 Layer 1'}], 
    )
GEMLayout(dqmitems, 'Common/10 GE+11L2 VFAT input status', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la2', 'description': 'VFAT input status in GE+1/1 Layer 2'}], 
    )
GEMLayout(dqmitems, 'Common/11 GE-11L1 VFAT input status (chamber vs. VFAT)', 
    [{'path': 'GEM/DAQStatus/vfat_statusSummary_re-1_st1_la1', 'description': 'VFAT input status (chamber vs. VFAT) in GE-1/1 Layer 1'}], 
    )
GEMLayout(dqmitems, 'Common/12 GE-11L2 VFAT input status (chamber vs. VFAT)', 
    [{'path': 'GEM/DAQStatus/vfat_statusSummary_re-1_st1_la2', 'description': 'VFAT input status (chamber vs. VFAT) in GE-1/1 Layer 2'}], 
    )
GEMLayout(dqmitems, 'Common/13 GE+11L1 VFAT input status (chamber vs. VFAT)', 
    [{'path': 'GEM/DAQStatus/vfat_statusSummary_re1_st1_la1', 'description': 'VFAT input status (chamber vs. VFAT) in GE+1/1 Layer 1'}], 
    )
GEMLayout(dqmitems, 'Common/14 GE+11L2 VFAT input status (chamber vs. VFAT)', 
    [{'path': 'GEM/DAQStatus/vfat_statusSummary_re1_st1_la2', 'description': 'VFAT input status (chamber vs. VFAT) in GE+1/1 Layer 2'}], 
    )
GEMLayout(dqmitems, 'Common/15 GE-11L1 recHit wheel occupancy', 
    [{'path': 'GEM/recHit/rechit_wheel_re-1_st1_la1', 'description': 'recHit wheel occupancy in GE-1/1 Layer 1'}], 
    )
GEMLayout(dqmitems, 'Common/16 GE-11L2 recHit wheel occupancy', 
    [{'path': 'GEM/recHit/rechit_wheel_re-1_st1_la2', 'description': 'recHit wheel occupancy in GE-1/1 Layer 2'}], 
    )
GEMLayout(dqmitems, 'Common/17 GE+11L1 recHit wheel occupancy', 
    [{'path': 'GEM/recHit/rechit_wheel_re1_st1_la1', 'description': 'recHit wheel occupancy in GE+1/1 Layer 1'}], 
    )
GEMLayout(dqmitems, 'Common/18 GE+11L2 recHit wheel occupancy', 
    [{'path': 'GEM/recHit/rechit_wheel_re1_st1_la2', 'description': 'recHit wheel occupancy in GE+1/1 Layer 2'}], 
    )
GEMLayout(dqmitems, 'Common/19 GE-11L1 bunch crossing', 
    [{'path': 'GEM/digi/bx_re-1_st1_la1', 'description': 'Bunch crossing in GE-1/1 Layer 1'}], 
    )
GEMLayout(dqmitems, 'Common/20 GE-11L2 bunch crossing', 
    [{'path': 'GEM/digi/bx_re-1_st1_la2', 'description': 'Bunch crossing in GE-1/1 Layer 2'}], 
    )
GEMLayout(dqmitems, 'Common/21 GE+11L1 bunch crossing', 
    [{'path': 'GEM/digi/bx_re1_st1_la1', 'description': 'Bunch crossing in GE+1/1 Layer 1'}], 
    )
GEMLayout(dqmitems, 'Common/22 GE+11L2 bunch crossing', 
    [{'path': 'GEM/digi/bx_re1_st1_la2', 'description': 'Bunch crossing in GE+1/1 Layer 2'}], 
    )
GEMLayout(dqmitems, 'Common/23 GE-11L1 digi occupancy', 
    [{'path': 'GEM/digi/digi_det_re-1_st1_la1', 'description': 'Digi occupancy in GE-1/1 Layer 1'}], 
    )
GEMLayout(dqmitems, 'Common/24 GE-11L2 digi occupancy', 
    [{'path': 'GEM/digi/digi_det_re-1_st1_la2', 'description': 'Digi occupancy in GE-1/1 Layer 2'}], 
    )
GEMLayout(dqmitems, 'Common/25 GE+11L1 digi occupancy', 
    [{'path': 'GEM/digi/digi_det_re1_st1_la1', 'description': 'Digi occupancy in GE+1/1 Layer 1'}], 
    )
GEMLayout(dqmitems, 'Common/26 GE+11L2 digi occupancy', 
    [{'path': 'GEM/digi/digi_det_re1_st1_la2', 'description': 'Digi occupancy in GE+1/1 Layer 2'}], 
    )
GEMLayout(dqmitems, 'Common/27 GE-11L1 digi occupancy vs iEta', 
    [{'path': 'GEM/digi/strip_ieta_occ_re-1_st1_la1', 'description': 'Digi occupancy vs iEta in GE-1/1 Layer 1'}], 
    )
GEMLayout(dqmitems, 'Common/28 GE-11L2 digi occupancy vs iEta', 
    [{'path': 'GEM/digi/strip_ieta_occ_re-1_st1_la2', 'description': 'Digi occupancy vs iEta in GE-1/1 Layer 2'}], 
    )
GEMLayout(dqmitems, 'Common/29 GE+11L1 digi occupancy vs iEta', 
    [{'path': 'GEM/digi/strip_ieta_occ_re1_st1_la1', 'description': 'Digi occupancy vs iEta in GE+1/1 Layer 1'}], 
    )
GEMLayout(dqmitems, 'Common/30 GE+11L2 digi occupancy vs iEta', 
    [{'path': 'GEM/digi/strip_ieta_occ_re1_st1_la2', 'description': 'Digi occupancy vs iEta in GE+1/1 Layer 2'}], 
    )
GEMLayout(dqmitems, 'Common/31 GE-11L1 digi occupancy vs phi', 
    [{'path': 'GEM/digi/strip_phi_occ_re-1_st1_la1', 'description': 'Digi occupancy vs phi in GE-1/1 Layer 1'}], 
    )
GEMLayout(dqmitems, 'Common/32 GE-11L2 digi occupancy vs phi', 
    [{'path': 'GEM/digi/strip_phi_occ_re-1_st1_la2', 'description': 'Digi occupancy vs phi in GE-1/1 Layer 2'}], 
    )
GEMLayout(dqmitems, 'Common/33 GE+11L1 digi occupancy vs phi', 
    [{'path': 'GEM/digi/strip_phi_occ_re1_st1_la1', 'description': 'Digi occupancy vs phi in GE+1/1 Layer 1'}], 
    )
GEMLayout(dqmitems, 'Common/34 GE+11L2 digi occupancy vs phi', 
    [{'path': 'GEM/digi/strip_phi_occ_re1_st1_la2', 'description': 'Digi occupancy vs phi in GE+1/1 Layer 2'}], 
    )
GEMLayout(dqmitems, 'Common/35 GE-11L1 total number of strips per event', 
    [{'path': 'GEM/digi/total_strips_per_event_re-1_st1_la1', 'description': 'Total number of strips per event in GE-1/1 Layer 1'}], 
    )
GEMLayout(dqmitems, 'Common/36 GE-11L2 total number of strips per event', 
    [{'path': 'GEM/digi/total_strips_per_event_re-1_st1_la2', 'description': 'Total number of strips per event in GE-1/1 Layer 2'}], 
    )
GEMLayout(dqmitems, 'Common/37 GE+11L1 total number of strips per event', 
    [{'path': 'GEM/digi/total_strips_per_event_re1_st1_la1', 'description': 'Total number of strips per event in GE+1/1 Layer 1'}], 
    )
GEMLayout(dqmitems, 'Common/38 GE+11L2 total number of strips per event', 
    [{'path': 'GEM/digi/total_strips_per_event_re1_st1_la2', 'description': 'Total number of strips per event in GE+1/1 Layer 2'}], 
    )
GEMLayout(dqmitems, 'Common/39 GE-11L1 recHit occupancy', 
    [{'path': 'GEM/recHit/rechit_det_re-1_st1_la1', 'description': 'recHit occupancy in GE-1/1 Layer 1'}], 
    )
GEMLayout(dqmitems, 'Common/40 GE-11L2 recHit occupancy', 
    [{'path': 'GEM/recHit/rechit_det_re-1_st1_la2', 'description': 'recHit occupancy in GE-1/1 Layer 2'}], 
    )
GEMLayout(dqmitems, 'Common/41 GE+11L1 recHit occupancy', 
    [{'path': 'GEM/recHit/rechit_det_re1_st1_la1', 'description': 'recHit occupancy in GE+1/1 Layer 1'}], 
    )
GEMLayout(dqmitems, 'Common/42 GE+11L2 recHit occupancy', 
    [{'path': 'GEM/recHit/rechit_det_re1_st1_la2', 'description': 'recHit occupancy in GE+1/1 Layer 2'}], 
    )
GEMLayout(dqmitems, 'Common/43 GE-11L1 recHit occupancy vs iEta', 
    [{'path': 'GEM/recHit/rechit_ieta_occ_re-1_st1_la1', 'description': 'recHit occupancy vs iEta in GE-1/1 Layer 1'}], 
    )
GEMLayout(dqmitems, 'Common/44 GE-11L2 recHit occupancy vs iEta', 
    [{'path': 'GEM/recHit/rechit_ieta_occ_re-1_st1_la2', 'description': 'recHit occupancy vs iEta in GE-1/1 Layer 2'}], 
    )
GEMLayout(dqmitems, 'Common/45 GE+11L1 recHit occupancy vs iEta', 
    [{'path': 'GEM/recHit/rechit_ieta_occ_re1_st1_la1', 'description': 'recHit occupancy vs iEta in GE+1/1 Layer 1'}], 
    )
GEMLayout(dqmitems, 'Common/46 GE+11L2 recHit occupancy vs iEta', 
    [{'path': 'GEM/recHit/rechit_ieta_occ_re1_st1_la2', 'description': 'recHit occupancy vs iEta in GE+1/1 Layer 2'}], 
    )
GEMLayout(dqmitems, 'Common/47 GE-11L1 recHit occupancy vs phi', 
    [{'path': 'GEM/recHit/rechit_phi_occ_re-1_st1_la1', 'description': 'recHit occupancy vs phi in GE-1/1 Layer 1'}], 
    )
GEMLayout(dqmitems, 'Common/48 GE-11L2 recHit occupancy vs phi', 
    [{'path': 'GEM/recHit/rechit_phi_occ_re-1_st1_la2', 'description': 'recHit occupancy vs phi in GE-1/1 Layer 2'}], 
    )
GEMLayout(dqmitems, 'Common/49 GE+11L1 recHit occupancy vs phi', 
    [{'path': 'GEM/recHit/rechit_phi_occ_re1_st1_la1', 'description': 'recHit occupancy vs phi in GE+1/1 Layer 1'}], 
    )
GEMLayout(dqmitems, 'Common/50 GE+11L2 recHit occupancy vs phi', 
    [{'path': 'GEM/recHit/rechit_phi_occ_re1_st1_la2', 'description': 'recHit occupancy vs phi in GE+1/1 Layer 2'}], 
    )
GEMLayout(dqmitems, 'Common/51 GE-11L1 total number of recHits per event', 
    [{'path': 'GEM/recHit/total_rechit_per_event_re-1_st1_la1', 'description': 'Total number of recHits per event in GE-1/1 Layer 1'}], 
    )
GEMLayout(dqmitems, 'Common/52 GE-11L2 total number of recHits per event', 
    [{'path': 'GEM/recHit/total_rechit_per_event_re-1_st1_la2', 'description': 'Total number of recHits per event in GE-1/1 Layer 2'}], 
    )
GEMLayout(dqmitems, 'Common/53 GE+11L1 total number of recHits per event', 
    [{'path': 'GEM/recHit/total_rechit_per_event_re1_st1_la1', 'description': 'Total number of recHits per event in GE+1/1 Layer 1'}], 
    )
GEMLayout(dqmitems, 'Common/54 GE+11L2 total number of recHits per event', 
    [{'path': 'GEM/recHit/total_rechit_per_event_re1_st1_la2', 'description': 'Total number of recHits per event in GE+1/1 Layer 2'}], 
    )
GEMLayout(dqmitems, 'Common/55 GE-11L1 iEta 1 cluster size', 
    [{'path': 'GEM/recHit/cls_re-1_st1_la1_ieta01', 'description': 'Cluster size distribution in GE-1/1 Layer 1 iEta 1'}], 
    )
GEMLayout(dqmitems, 'Common/56 GE-11L1 iEta 2 cluster size', 
    [{'path': 'GEM/recHit/cls_re-1_st1_la1_ieta02', 'description': 'Cluster size distribution in GE-1/1 Layer 1 iEta 2'}], 
    )
GEMLayout(dqmitems, 'Common/57 GE-11L1 iEta 3 cluster size', 
    [{'path': 'GEM/recHit/cls_re-1_st1_la1_ieta03', 'description': 'Cluster size distribution in GE-1/1 Layer 1 iEta 3'}], 
    )
GEMLayout(dqmitems, 'Common/58 GE-11L1 iEta 4 cluster size', 
    [{'path': 'GEM/recHit/cls_re-1_st1_la1_ieta04', 'description': 'Cluster size distribution in GE-1/1 Layer 1 iEta 4'}], 
    )
GEMLayout(dqmitems, 'Common/59 GE-11L1 iEta 5 cluster size', 
    [{'path': 'GEM/recHit/cls_re-1_st1_la1_ieta05', 'description': 'Cluster size distribution in GE-1/1 Layer 1 iEta 5'}], 
    )
GEMLayout(dqmitems, 'Common/60 GE-11L1 iEta 6 cluster size', 
    [{'path': 'GEM/recHit/cls_re-1_st1_la1_ieta06', 'description': 'Cluster size distribution in GE-1/1 Layer 1 iEta 6'}], 
    )
GEMLayout(dqmitems, 'Common/61 GE-11L1 iEta 7 cluster size', 
    [{'path': 'GEM/recHit/cls_re-1_st1_la1_ieta07', 'description': 'Cluster size distribution in GE-1/1 Layer 1 iEta 7'}], 
    )
GEMLayout(dqmitems, 'Common/62 GE-11L1 iEta 8 cluster size', 
    [{'path': 'GEM/recHit/cls_re-1_st1_la1_ieta08', 'description': 'Cluster size distribution in GE-1/1 Layer 1 iEta 8'}], 
    )
GEMLayout(dqmitems, 'Common/63 GE-11L2 iEta 1 cluster size', 
    [{'path': 'GEM/recHit/cls_re-1_st1_la2_ieta01', 'description': 'Cluster size distribution in GE-1/1 Layer 2 iEta 1'}], 
    )
GEMLayout(dqmitems, 'Common/64 GE-11L2 iEta 2 cluster size', 
    [{'path': 'GEM/recHit/cls_re-1_st1_la2_ieta02', 'description': 'Cluster size distribution in GE-1/1 Layer 2 iEta 2'}], 
    )
GEMLayout(dqmitems, 'Common/65 GE-11L2 iEta 3 cluster size', 
    [{'path': 'GEM/recHit/cls_re-1_st1_la2_ieta03', 'description': 'Cluster size distribution in GE-1/1 Layer 2 iEta 3'}], 
    )
GEMLayout(dqmitems, 'Common/66 GE-11L2 iEta 4 cluster size', 
    [{'path': 'GEM/recHit/cls_re-1_st1_la2_ieta04', 'description': 'Cluster size distribution in GE-1/1 Layer 2 iEta 4'}], 
    )
GEMLayout(dqmitems, 'Common/67 GE-11L2 iEta 5 cluster size', 
    [{'path': 'GEM/recHit/cls_re-1_st1_la2_ieta05', 'description': 'Cluster size distribution in GE-1/1 Layer 2 iEta 5'}], 
    )
GEMLayout(dqmitems, 'Common/68 GE-11L2 iEta 6 cluster size', 
    [{'path': 'GEM/recHit/cls_re-1_st1_la2_ieta06', 'description': 'Cluster size distribution in GE-1/1 Layer 2 iEta 6'}], 
    )
GEMLayout(dqmitems, 'Common/69 GE-11L2 iEta 7 cluster size', 
    [{'path': 'GEM/recHit/cls_re-1_st1_la2_ieta07', 'description': 'Cluster size distribution in GE-1/1 Layer 2 iEta 7'}], 
    )
GEMLayout(dqmitems, 'Common/70 GE-11L2 iEta 8 cluster size', 
    [{'path': 'GEM/recHit/cls_re-1_st1_la2_ieta08', 'description': 'Cluster size distribution in GE-1/1 Layer 2 iEta 8'}], 
    )
GEMLayout(dqmitems, 'Common/71 GE+11L1 iEta 1 cluster size', 
    [{'path': 'GEM/recHit/cls_re1_st1_la1_ieta01', 'description': 'Cluster size distribution in GE+1/1 Layer 1 iEta 1'}], 
    )
GEMLayout(dqmitems, 'Common/72 GE+11L1 iEta 2 cluster size', 
    [{'path': 'GEM/recHit/cls_re1_st1_la1_ieta02', 'description': 'Cluster size distribution in GE+1/1 Layer 1 iEta 2'}], 
    )
GEMLayout(dqmitems, 'Common/73 GE+11L1 iEta 3 cluster size', 
    [{'path': 'GEM/recHit/cls_re1_st1_la1_ieta03', 'description': 'Cluster size distribution in GE+1/1 Layer 1 iEta 3'}], 
    )
GEMLayout(dqmitems, 'Common/74 GE+11L1 iEta 4 cluster size', 
    [{'path': 'GEM/recHit/cls_re1_st1_la1_ieta04', 'description': 'Cluster size distribution in GE+1/1 Layer 1 iEta 4'}], 
    )
GEMLayout(dqmitems, 'Common/75 GE+11L1 iEta 5 cluster size', 
    [{'path': 'GEM/recHit/cls_re1_st1_la1_ieta05', 'description': 'Cluster size distribution in GE+1/1 Layer 1 iEta 5'}], 
    )
GEMLayout(dqmitems, 'Common/76 GE+11L1 iEta 6 cluster size', 
    [{'path': 'GEM/recHit/cls_re1_st1_la1_ieta06', 'description': 'Cluster size distribution in GE+1/1 Layer 1 iEta 6'}], 
    )
GEMLayout(dqmitems, 'Common/77 GE+11L1 iEta 7 cluster size', 
    [{'path': 'GEM/recHit/cls_re1_st1_la1_ieta07', 'description': 'Cluster size distribution in GE+1/1 Layer 1 iEta 7'}], 
    )
GEMLayout(dqmitems, 'Common/78 GE+11L1 iEta 8 cluster size', 
    [{'path': 'GEM/recHit/cls_re1_st1_la1_ieta08', 'description': 'Cluster size distribution in GE+1/1 Layer 1 iEta 8'}], 
    )
GEMLayout(dqmitems, 'Common/79 GE+11L2 iEta 1 cluster size', 
    [{'path': 'GEM/recHit/cls_re1_st1_la2_ieta01', 'description': 'Cluster size distribution in GE+1/1 Layer 2 iEta 1'}], 
    )
GEMLayout(dqmitems, 'Common/80 GE+11L2 iEta 2 cluster size', 
    [{'path': 'GEM/recHit/cls_re1_st1_la2_ieta02', 'description': 'Cluster size distribution in GE+1/1 Layer 2 iEta 2'}], 
    )
GEMLayout(dqmitems, 'Common/81 GE+11L2 iEta 3 cluster size', 
    [{'path': 'GEM/recHit/cls_re1_st1_la2_ieta03', 'description': 'Cluster size distribution in GE+1/1 Layer 2 iEta 3'}], 
    )
GEMLayout(dqmitems, 'Common/82 GE+11L2 iEta 4 cluster size', 
    [{'path': 'GEM/recHit/cls_re1_st1_la2_ieta04', 'description': 'Cluster size distribution in GE+1/1 Layer 2 iEta 4'}], 
    )
GEMLayout(dqmitems, 'Common/83 GE+11L2 iEta 5 cluster size', 
    [{'path': 'GEM/recHit/cls_re1_st1_la2_ieta05', 'description': 'Cluster size distribution in GE+1/1 Layer 2 iEta 5'}], 
    )
GEMLayout(dqmitems, 'Common/84 GE+11L2 iEta 6 cluster size', 
    [{'path': 'GEM/recHit/cls_re1_st1_la2_ieta06', 'description': 'Cluster size distribution in GE+1/1 Layer 2 iEta 6'}], 
    )
GEMLayout(dqmitems, 'Common/85 GE+11L2 iEta 7 cluster size', 
    [{'path': 'GEM/recHit/cls_re1_st1_la2_ieta07', 'description': 'Cluster size distribution in GE+1/1 Layer 2 iEta 7'}], 
    )
GEMLayout(dqmitems, 'Common/86 GE+11L2 iEta 8 cluster size', 
    [{'path': 'GEM/recHit/cls_re1_st1_la2_ieta08', 'description': 'Cluster size distribution in GE+1/1 Layer 2 iEta 8'}], 
    )
GEMLayout(dqmitems, 'GE-11 L1/00 GE-11L1 Chamber 01', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la1_ch01', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la1_ch01', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la1_ch01', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la1_ch01', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L1/01 GE-11L1 Chamber 02', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la1_ch02', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la1_ch02', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la1_ch02', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la1_ch02', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L1/02 GE-11L1 Chamber 03', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la1_ch03', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la1_ch03', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la1_ch03', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la1_ch03', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L1/03 GE-11L1 Chamber 04', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la1_ch04', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la1_ch04', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la1_ch04', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la1_ch04', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L1/04 GE-11L1 Chamber 05', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la1_ch05', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la1_ch05', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la1_ch05', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la1_ch05', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L1/05 GE-11L1 Chamber 06', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la1_ch06', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la1_ch06', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la1_ch06', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la1_ch06', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L1/06 GE-11L1 Chamber 07', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la1_ch07', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la1_ch07', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la1_ch07', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la1_ch07', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L1/07 GE-11L1 Chamber 08', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la1_ch08', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la1_ch08', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la1_ch08', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la1_ch08', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L1/08 GE-11L1 Chamber 09', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la1_ch09', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la1_ch09', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la1_ch09', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la1_ch09', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L1/09 GE-11L1 Chamber 10', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la1_ch10', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la1_ch10', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la1_ch10', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la1_ch10', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L1/10 GE-11L1 Chamber 11', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la1_ch11', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la1_ch11', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la1_ch11', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la1_ch11', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L1/11 GE-11L1 Chamber 12', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la1_ch12', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la1_ch12', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la1_ch12', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la1_ch12', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L1/12 GE-11L1 Chamber 13', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la1_ch13', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la1_ch13', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la1_ch13', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la1_ch13', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L1/13 GE-11L1 Chamber 14', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la1_ch14', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la1_ch14', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la1_ch14', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la1_ch14', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L1/14 GE-11L1 Chamber 15', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la1_ch15', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la1_ch15', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la1_ch15', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la1_ch15', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L1/15 GE-11L1 Chamber 16', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la1_ch16', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la1_ch16', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la1_ch16', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la1_ch16', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L1/16 GE-11L1 Chamber 17', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la1_ch17', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la1_ch17', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la1_ch17', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la1_ch17', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L1/17 GE-11L1 Chamber 18', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la1_ch18', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la1_ch18', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la1_ch18', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la1_ch18', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L1/18 GE-11L1 Chamber 19', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la1_ch19', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la1_ch19', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la1_ch19', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la1_ch19', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L1/19 GE-11L1 Chamber 20', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la1_ch20', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la1_ch20', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la1_ch20', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la1_ch20', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L1/20 GE-11L1 Chamber 21', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la1_ch21', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la1_ch21', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la1_ch21', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la1_ch21', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L1/21 GE-11L1 Chamber 22', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la1_ch22', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la1_ch22', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la1_ch22', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la1_ch22', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L1/22 GE-11L1 Chamber 23', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la1_ch23', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la1_ch23', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la1_ch23', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la1_ch23', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L1/23 GE-11L1 Chamber 24', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la1_ch24', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la1_ch24', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la1_ch24', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la1_ch24', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L1/24 GE-11L1 Chamber 25', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la1_ch25', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la1_ch25', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la1_ch25', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la1_ch25', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L1/25 GE-11L1 Chamber 26', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la1_ch26', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la1_ch26', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la1_ch26', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la1_ch26', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L1/26 GE-11L1 Chamber 27', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la1_ch27', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la1_ch27', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la1_ch27', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la1_ch27', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L1/27 GE-11L1 Chamber 28', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la1_ch28', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la1_ch28', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la1_ch28', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la1_ch28', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L1/28 GE-11L1 Chamber 29', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la1_ch29', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la1_ch29', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la1_ch29', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la1_ch29', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L1/29 GE-11L1 Chamber 30', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la1_ch30', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la1_ch30', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la1_ch30', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la1_ch30', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L1/30 GE-11L1 Chamber 31', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la1_ch31', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la1_ch31', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la1_ch31', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la1_ch31', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L1/31 GE-11L1 Chamber 32', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la1_ch32', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la1_ch32', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la1_ch32', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la1_ch32', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L1/32 GE-11L1 Chamber 33', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la1_ch33', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la1_ch33', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la1_ch33', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la1_ch33', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L1/33 GE-11L1 Chamber 34', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la1_ch34', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la1_ch34', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la1_ch34', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la1_ch34', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L1/34 GE-11L1 Chamber 35', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la1_ch35', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la1_ch35', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la1_ch35', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la1_ch35', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L1/35 GE-11L1 Chamber 36', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la1_ch36', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la1_ch36', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la1_ch36', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la1_ch36', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L2/00 GE-11L2 Chamber 01', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la2_ch01', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la2_ch01', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la2_ch01', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la2_ch01', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L2/01 GE-11L2 Chamber 02', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la2_ch02', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la2_ch02', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la2_ch02', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la2_ch02', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L2/02 GE-11L2 Chamber 03', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la2_ch03', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la2_ch03', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la2_ch03', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la2_ch03', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L2/03 GE-11L2 Chamber 04', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la2_ch04', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la2_ch04', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la2_ch04', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la2_ch04', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L2/04 GE-11L2 Chamber 05', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la2_ch05', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la2_ch05', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la2_ch05', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la2_ch05', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L2/05 GE-11L2 Chamber 06', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la2_ch06', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la2_ch06', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la2_ch06', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la2_ch06', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L2/06 GE-11L2 Chamber 07', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la2_ch07', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la2_ch07', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la2_ch07', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la2_ch07', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L2/07 GE-11L2 Chamber 08', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la2_ch08', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la2_ch08', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la2_ch08', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la2_ch08', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L2/08 GE-11L2 Chamber 09', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la2_ch09', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la2_ch09', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la2_ch09', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la2_ch09', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L2/09 GE-11L2 Chamber 10', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la2_ch10', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la2_ch10', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la2_ch10', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la2_ch10', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L2/10 GE-11L2 Chamber 11', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la2_ch11', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la2_ch11', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la2_ch11', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la2_ch11', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L2/11 GE-11L2 Chamber 12', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la2_ch12', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la2_ch12', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la2_ch12', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la2_ch12', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L2/12 GE-11L2 Chamber 13', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la2_ch13', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la2_ch13', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la2_ch13', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la2_ch13', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L2/13 GE-11L2 Chamber 14', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la2_ch14', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la2_ch14', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la2_ch14', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la2_ch14', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L2/14 GE-11L2 Chamber 15', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la2_ch15', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la2_ch15', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la2_ch15', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la2_ch15', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L2/15 GE-11L2 Chamber 16', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la2_ch16', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la2_ch16', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la2_ch16', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la2_ch16', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L2/16 GE-11L2 Chamber 17', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la2_ch17', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la2_ch17', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la2_ch17', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la2_ch17', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L2/17 GE-11L2 Chamber 18', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la2_ch18', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la2_ch18', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la2_ch18', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la2_ch18', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L2/18 GE-11L2 Chamber 19', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la2_ch19', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la2_ch19', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la2_ch19', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la2_ch19', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L2/19 GE-11L2 Chamber 20', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la2_ch20', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la2_ch20', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la2_ch20', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la2_ch20', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L2/20 GE-11L2 Chamber 21', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la2_ch21', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la2_ch21', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la2_ch21', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la2_ch21', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L2/21 GE-11L2 Chamber 22', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la2_ch22', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la2_ch22', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la2_ch22', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la2_ch22', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L2/22 GE-11L2 Chamber 23', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la2_ch23', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la2_ch23', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la2_ch23', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la2_ch23', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L2/23 GE-11L2 Chamber 24', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la2_ch24', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la2_ch24', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la2_ch24', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la2_ch24', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L2/24 GE-11L2 Chamber 25', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la2_ch25', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la2_ch25', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la2_ch25', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la2_ch25', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L2/25 GE-11L2 Chamber 26', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la2_ch26', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la2_ch26', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la2_ch26', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la2_ch26', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L2/26 GE-11L2 Chamber 27', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la2_ch27', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la2_ch27', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la2_ch27', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la2_ch27', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L2/27 GE-11L2 Chamber 28', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la2_ch28', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la2_ch28', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la2_ch28', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la2_ch28', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L2/28 GE-11L2 Chamber 29', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la2_ch29', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la2_ch29', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la2_ch29', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la2_ch29', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L2/29 GE-11L2 Chamber 30', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la2_ch30', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la2_ch30', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la2_ch30', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la2_ch30', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L2/30 GE-11L2 Chamber 31', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la2_ch31', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la2_ch31', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la2_ch31', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la2_ch31', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L2/31 GE-11L2 Chamber 32', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la2_ch32', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la2_ch32', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la2_ch32', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la2_ch32', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L2/32 GE-11L2 Chamber 33', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la2_ch33', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la2_ch33', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la2_ch33', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la2_ch33', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L2/33 GE-11L2 Chamber 34', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la2_ch34', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la2_ch34', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la2_ch34', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la2_ch34', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L2/34 GE-11L2 Chamber 35', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la2_ch35', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la2_ch35', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la2_ch35', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la2_ch35', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE-11 L2/35 GE-11L2 Chamber 36', 
    [{'path': 'GEM/DAQStatus/vfat_status_re-1_st1_la2_ch36', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re-1_st1_la2_ch36', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re-1_st1_la2_ch36', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re-1_st1_la2_ch36', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L1/00 GE+11L1 Chamber 01', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la1_ch01', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la1_ch01', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la1_ch01', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la1_ch01', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L1/01 GE+11L1 Chamber 02', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la1_ch02', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la1_ch02', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la1_ch02', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la1_ch02', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L1/02 GE+11L1 Chamber 03', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la1_ch03', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la1_ch03', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la1_ch03', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la1_ch03', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L1/03 GE+11L1 Chamber 04', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la1_ch04', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la1_ch04', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la1_ch04', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la1_ch04', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L1/04 GE+11L1 Chamber 05', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la1_ch05', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la1_ch05', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la1_ch05', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la1_ch05', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L1/05 GE+11L1 Chamber 06', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la1_ch06', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la1_ch06', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la1_ch06', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la1_ch06', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L1/06 GE+11L1 Chamber 07', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la1_ch07', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la1_ch07', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la1_ch07', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la1_ch07', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L1/07 GE+11L1 Chamber 08', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la1_ch08', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la1_ch08', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la1_ch08', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la1_ch08', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L1/08 GE+11L1 Chamber 09', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la1_ch09', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la1_ch09', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la1_ch09', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la1_ch09', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L1/09 GE+11L1 Chamber 10', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la1_ch10', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la1_ch10', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la1_ch10', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la1_ch10', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L1/10 GE+11L1 Chamber 11', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la1_ch11', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la1_ch11', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la1_ch11', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la1_ch11', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L1/11 GE+11L1 Chamber 12', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la1_ch12', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la1_ch12', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la1_ch12', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la1_ch12', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L1/12 GE+11L1 Chamber 13', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la1_ch13', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la1_ch13', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la1_ch13', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la1_ch13', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L1/13 GE+11L1 Chamber 14', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la1_ch14', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la1_ch14', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la1_ch14', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la1_ch14', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L1/14 GE+11L1 Chamber 15', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la1_ch15', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la1_ch15', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la1_ch15', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la1_ch15', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L1/15 GE+11L1 Chamber 16', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la1_ch16', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la1_ch16', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la1_ch16', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la1_ch16', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L1/16 GE+11L1 Chamber 17', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la1_ch17', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la1_ch17', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la1_ch17', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la1_ch17', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L1/17 GE+11L1 Chamber 18', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la1_ch18', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la1_ch18', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la1_ch18', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la1_ch18', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L1/18 GE+11L1 Chamber 19', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la1_ch19', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la1_ch19', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la1_ch19', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la1_ch19', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L1/19 GE+11L1 Chamber 20', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la1_ch20', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la1_ch20', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la1_ch20', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la1_ch20', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L1/20 GE+11L1 Chamber 21', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la1_ch21', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la1_ch21', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la1_ch21', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la1_ch21', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L1/21 GE+11L1 Chamber 22', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la1_ch22', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la1_ch22', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la1_ch22', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la1_ch22', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L1/22 GE+11L1 Chamber 23', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la1_ch23', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la1_ch23', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la1_ch23', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la1_ch23', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L1/23 GE+11L1 Chamber 24', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la1_ch24', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la1_ch24', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la1_ch24', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la1_ch24', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L1/24 GE+11L1 Chamber 25', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la1_ch25', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la1_ch25', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la1_ch25', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la1_ch25', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L1/25 GE+11L1 Chamber 26', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la1_ch26', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la1_ch26', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la1_ch26', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la1_ch26', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L1/26 GE+11L1 Chamber 27', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la1_ch27', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la1_ch27', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la1_ch27', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la1_ch27', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L1/27 GE+11L1 Chamber 28', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la1_ch28', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la1_ch28', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la1_ch28', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la1_ch28', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L1/28 GE+11L1 Chamber 29', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la1_ch29', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la1_ch29', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la1_ch29', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la1_ch29', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L1/29 GE+11L1 Chamber 30', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la1_ch30', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la1_ch30', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la1_ch30', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la1_ch30', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L1/30 GE+11L1 Chamber 31', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la1_ch31', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la1_ch31', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la1_ch31', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la1_ch31', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L1/31 GE+11L1 Chamber 32', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la1_ch32', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la1_ch32', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la1_ch32', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la1_ch32', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L1/32 GE+11L1 Chamber 33', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la1_ch33', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la1_ch33', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la1_ch33', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la1_ch33', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L1/33 GE+11L1 Chamber 34', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la1_ch34', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la1_ch34', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la1_ch34', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la1_ch34', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L1/34 GE+11L1 Chamber 35', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la1_ch35', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la1_ch35', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la1_ch35', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la1_ch35', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L1/35 GE+11L1 Chamber 36', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la1_ch36', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la1_ch36', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la1_ch36', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la1_ch36', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L2/00 GE+11L2 Chamber 01', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la2_ch01', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la2_ch01', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la2_ch01', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la2_ch01', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L2/01 GE+11L2 Chamber 02', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la2_ch02', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la2_ch02', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la2_ch02', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la2_ch02', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L2/02 GE+11L2 Chamber 03', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la2_ch03', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la2_ch03', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la2_ch03', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la2_ch03', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L2/03 GE+11L2 Chamber 04', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la2_ch04', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la2_ch04', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la2_ch04', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la2_ch04', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L2/04 GE+11L2 Chamber 05', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la2_ch05', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la2_ch05', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la2_ch05', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la2_ch05', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L2/05 GE+11L2 Chamber 06', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la2_ch06', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la2_ch06', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la2_ch06', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la2_ch06', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L2/06 GE+11L2 Chamber 07', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la2_ch07', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la2_ch07', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la2_ch07', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la2_ch07', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L2/07 GE+11L2 Chamber 08', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la2_ch08', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la2_ch08', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la2_ch08', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la2_ch08', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L2/08 GE+11L2 Chamber 09', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la2_ch09', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la2_ch09', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la2_ch09', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la2_ch09', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L2/09 GE+11L2 Chamber 10', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la2_ch10', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la2_ch10', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la2_ch10', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la2_ch10', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L2/10 GE+11L2 Chamber 11', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la2_ch11', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la2_ch11', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la2_ch11', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la2_ch11', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L2/11 GE+11L2 Chamber 12', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la2_ch12', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la2_ch12', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la2_ch12', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la2_ch12', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L2/12 GE+11L2 Chamber 13', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la2_ch13', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la2_ch13', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la2_ch13', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la2_ch13', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L2/13 GE+11L2 Chamber 14', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la2_ch14', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la2_ch14', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la2_ch14', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la2_ch14', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L2/14 GE+11L2 Chamber 15', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la2_ch15', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la2_ch15', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la2_ch15', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la2_ch15', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L2/15 GE+11L2 Chamber 16', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la2_ch16', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la2_ch16', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la2_ch16', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la2_ch16', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L2/16 GE+11L2 Chamber 17', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la2_ch17', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la2_ch17', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la2_ch17', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la2_ch17', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L2/17 GE+11L2 Chamber 18', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la2_ch18', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la2_ch18', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la2_ch18', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la2_ch18', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L2/18 GE+11L2 Chamber 19', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la2_ch19', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la2_ch19', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la2_ch19', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la2_ch19', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L2/19 GE+11L2 Chamber 20', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la2_ch20', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la2_ch20', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la2_ch20', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la2_ch20', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L2/20 GE+11L2 Chamber 21', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la2_ch21', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la2_ch21', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la2_ch21', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la2_ch21', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L2/21 GE+11L2 Chamber 22', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la2_ch22', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la2_ch22', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la2_ch22', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la2_ch22', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L2/22 GE+11L2 Chamber 23', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la2_ch23', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la2_ch23', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la2_ch23', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la2_ch23', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L2/23 GE+11L2 Chamber 24', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la2_ch24', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la2_ch24', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la2_ch24', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la2_ch24', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L2/24 GE+11L2 Chamber 25', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la2_ch25', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la2_ch25', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la2_ch25', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la2_ch25', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L2/25 GE+11L2 Chamber 26', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la2_ch26', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la2_ch26', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la2_ch26', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la2_ch26', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L2/26 GE+11L2 Chamber 27', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la2_ch27', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la2_ch27', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la2_ch27', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la2_ch27', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L2/27 GE+11L2 Chamber 28', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la2_ch28', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la2_ch28', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la2_ch28', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la2_ch28', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L2/28 GE+11L2 Chamber 29', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la2_ch29', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la2_ch29', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la2_ch29', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la2_ch29', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L2/29 GE+11L2 Chamber 30', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la2_ch30', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la2_ch30', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la2_ch30', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la2_ch30', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L2/30 GE+11L2 Chamber 31', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la2_ch31', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la2_ch31', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la2_ch31', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la2_ch31', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L2/31 GE+11L2 Chamber 32', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la2_ch32', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la2_ch32', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la2_ch32', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la2_ch32', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L2/32 GE+11L2 Chamber 33', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la2_ch33', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la2_ch33', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la2_ch33', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la2_ch33', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L2/33 GE+11L2 Chamber 34', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la2_ch34', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la2_ch34', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la2_ch34', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la2_ch34', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L2/34 GE+11L2 Chamber 35', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la2_ch35', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la2_ch35', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la2_ch35', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la2_ch35', 'description': 'VFAT vs ClusterSize'}], 
    )
GEMLayout(dqmitems, 'GE+11 L2/35 GE+11L2 Chamber 36', 
    [{'path': 'GEM/DAQStatus/vfat_status_re1_st1_la2_ch36', 'description': 'VFAT status'}, {'path': 'GEM/digi/bx_ch_re1_st1_la2_ch36', 'description': 'Bunch crossing'}], 
    [{'path': 'GEM/digi/strip_occ_re1_st1_la2_ch36', 'description': 'Digi occupancy'}, {'path': 'GEM/recHit/cls_re1_st1_la2_ch36', 'description': 'VFAT vs ClusterSize'}], 
    )
