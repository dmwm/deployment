# Generated automatically by dqmgui/gem_custom/fillLayouts.py 
#   in https://github.com/quark2/deployment/tree/addingGem
#   Recipe: 
#     cd deployment/dqmgui
#     python3 gem_custom/fillLayouts.py
def GEMLayout(i, p, *rows): i["00 Shift/GEM/" + p] = DQMItem(layout=rows)

GEMLayout(dqmitems, 'Common/00 Summary',
    [{'path': 'GEM/EventInfo/reportSummaryMap', 'description': 'For more information (... under construction)'}],
    )


GEMLayout(dqmitems, 'Common/01 GE11-M-L1 recHit xy occupancy',
    [{'path': 'GEM/RecHits/occ_xy_GE11-M-L1', 'description': 'recHit xy occupancy in GE11-M-L1'}],
    )


GEMLayout(dqmitems, 'Common/02 GE11-M-L2 recHit xy occupancy',
    [{'path': 'GEM/RecHits/occ_xy_GE11-M-L2', 'description': 'recHit xy occupancy in GE11-M-L2'}],
    )


GEMLayout(dqmitems, 'Common/03 GE11-P-L1 recHit xy occupancy',
    [{'path': 'GEM/RecHits/occ_xy_GE11-P-L1', 'description': 'recHit xy occupancy in GE11-P-L1'}],
    )


GEMLayout(dqmitems, 'Common/04 GE11-P-L2 recHit xy occupancy',
    [{'path': 'GEM/RecHits/occ_xy_GE11-P-L2', 'description': 'recHit xy occupancy in GE11-P-L2'}],
    )


GEMLayout(dqmitems, 'Common/05 GE21-M-L1 recHit xy occupancy',
    [{'path': 'GEM/RecHits/occ_xy_GE21-M-L1', 'description': 'recHit xy occupancy in GE21-M-L1'}],
    )


GEMLayout(dqmitems, 'Common/06 GE21-P-L2 recHit xy occupancy',
    [{'path': 'GEM/RecHits/occ_xy_GE21-P-L2', 'description': 'recHit xy occupancy in GE21-P-L2'}],
    )


GEMLayout(dqmitems, 'Common/07 GE11-M-L1 GEM-CSC segment efficiency',
    [{'path': 'GEM/Efficiency/GEMCSCSegment/eff_chamber_GE11-M-L1', 'description': 'GEM-CSC segment efficiency in GE11-M-L1'}],
    )


GEMLayout(dqmitems, 'Common/08 GE11-M-L2 GEM-CSC segment efficiency',
    [{'path': 'GEM/Efficiency/GEMCSCSegment/eff_chamber_GE11-M-L2', 'description': 'GEM-CSC segment efficiency in GE11-M-L2'}],
    )


GEMLayout(dqmitems, 'Common/09 GE11-P-L1 GEM-CSC segment efficiency',
    [{'path': 'GEM/Efficiency/GEMCSCSegment/eff_chamber_GE11-P-L1', 'description': 'GEM-CSC segment efficiency in GE11-P-L1'}],
    )


GEMLayout(dqmitems, 'Common/10 GE11-P-L2 GEM-CSC segment efficiency',
    [{'path': 'GEM/Efficiency/GEMCSCSegment/eff_chamber_GE11-P-L2', 'description': 'GEM-CSC segment efficiency in GE11-P-L2'}],
    )


