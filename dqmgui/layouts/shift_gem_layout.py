# Generated automatically by dqmgui/gem_custom/fillLayouts.py 
#   in https://github.com/quark2/deployment/tree/addingGem
#   Recipe: 
#     cd deployment/dqmgui
#     python3 gem_custom/fillLayouts.py
def GEMLayout(i, p, *rows): i["00 Shift/GEM/" + p] = DQMItem(layout=rows)

GEMLayout(dqmitems, '00 Summary', 
    [{'path': 'GEM/EventInfo/reportSummaryMap', 'description': 'For more information (... under construction)'}], 
    )


GEMLayout(dqmitems, '01 AMC13 status', 
    [{'path': 'GEM/DAQStatus/amc13_status', 'description': 'For more information (... under construction)'}], 
    )


GEMLayout(dqmitems, '02 AMC status GE11-M', 
    [{'path': 'GEM/DAQStatus/amc_status_GE11-M', 'description': 'For more information (... under construction)'}], 
    )


GEMLayout(dqmitems, '03 AMC status GE11-P', 
    [{'path': 'GEM/DAQStatus/amc_status_GE11-P', 'description': 'For more information (... under construction)'}], 
    )


GEMLayout(dqmitems, '04 GE11-M-L1 OptoHybrid status', 
    [{'path': 'GEM/DAQStatus/oh_status_GE11-M-L1', 'description': 'OptoHybrid status in GE11-M-L1'}], 
    )


GEMLayout(dqmitems, '05 GE11-M-L2 OptoHybrid status', 
    [{'path': 'GEM/DAQStatus/oh_status_GE11-M-L2', 'description': 'OptoHybrid status in GE11-M-L2'}], 
    )


GEMLayout(dqmitems, '06 GE11-P-L1 OptoHybrid status', 
    [{'path': 'GEM/DAQStatus/oh_status_GE11-P-L1', 'description': 'OptoHybrid status in GE11-P-L1'}], 
    )


GEMLayout(dqmitems, '07 GE11-P-L2 OptoHybrid status', 
    [{'path': 'GEM/DAQStatus/oh_status_GE11-P-L2', 'description': 'OptoHybrid status in GE11-P-L2'}], 
    )


GEMLayout(dqmitems, '08 GE11-M-L1 VFAT status', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-L1', 'description': 'VFAT status in GE11-M-L1'}], 
    )


GEMLayout(dqmitems, '09 GE11-M-L2 VFAT status', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-M-L2', 'description': 'VFAT status in GE11-M-L2'}], 
    )


GEMLayout(dqmitems, '10 GE11-P-L1 VFAT status', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-L1', 'description': 'VFAT status in GE11-P-L1'}], 
    )


GEMLayout(dqmitems, '11 GE11-P-L2 VFAT status', 
    [{'path': 'GEM/DAQStatus/vfat_status_GE11-P-L2', 'description': 'VFAT status in GE11-P-L2'}], 
    )

