def GEMLayout(i, p, *rows): i["00 Shift/GEM/" + p] = DQMItem(layout=rows)

_GEM_OFF_TWIKI = '<a href="https://twiki.cern.ch/twiki/bin/view/CMS/GEMPPDOfflineDQM">Link to TWiki</a>'

###############################################################################
# Summary Map
###############################################################################
GEMLayout(dqmitems, '00 Summary Map',
          [{'path': 'GEM/EventInfo/reportSummaryMap',
            'description': _GEM_OFF_TWIKI}])

###############################################################################
# RecHit Occupancy
###############################################################################
GEMLayout(dqmitems, '01 GE11-M-L1 RecHit Occupancy',
          [{'path': 'GEM/RecHits/occ_xy_GE11-M-L1',
            'description': _GEM_OFF_TWIKI}])

GEMLayout(dqmitems, '02 GE11-M-L2 RecHit Occupancy',
          [{'path': 'GEM/RecHits/occ_xy_GE11-M-L2',
            'description': _GEM_OFF_TWIKI}])

GEMLayout(dqmitems, '03 GE11-P-L1 RecHit Occupancy',
          [{'path': 'GEM/RecHits/occ_xy_GE11-P-L1',
            'description': _GEM_OFF_TWIKI}])

GEMLayout(dqmitems, '04 GE11-P-L2 RecHit Occupancy',
          [{'path': 'GEM/RecHits/occ_xy_GE11-P-L2',
            'description': _GEM_OFF_TWIKI}])

###############################################################################
# RecHit Average Cluster Size
###############################################################################
GEMLayout(dqmitems, '05 GE11-M-L1 RecHit Average Cluster Size',
          [{'path': 'GEM/RecHits/rechit_average_GE11-M-L1',
            'description': _GEM_OFF_TWIKI}])

GEMLayout(dqmitems, '06 GE11-M-L2 RecHit Average Cluster Size',
          [{'path': 'GEM/RecHits/rechit_average_GE11-M-L2',
            'description': _GEM_OFF_TWIKI}])

GEMLayout(dqmitems, '07 GE11-P-L1 RecHit Average Cluster Size',
          [{'path': 'GEM/RecHits/rechit_average_GE11-P-L1',
            'description': _GEM_OFF_TWIKI}])

GEMLayout(dqmitems, '08 GE11-P-L2 RecHit Average Cluster Size',
          [{'path': 'GEM/RecHits/rechit_average_GE11-P-L2',
            'description': _GEM_OFF_TWIKI}])

###############################################################################
# Efficiency
###############################################################################
GEMLayout(dqmitems, '09 GE11-M-L1 Chamber Efficiency',
          [{'path': 'GEM/Efficiency/muonSTA/eff_chamber_GE11-M-L1',
            'description': _GEM_OFF_TWIKI}])

GEMLayout(dqmitems, '10 GE11-M-L2 Chamber Efficiency',
          [{'path': 'GEM/Efficiency/muonSTA/eff_chamber_GE11-M-L2',
            'description': _GEM_OFF_TWIKI}])

GEMLayout(dqmitems, '11 GE11-P-L1 Chamber Efficiency',
          [{'path': 'GEM/Efficiency/muonSTA/eff_chamber_GE11-P-L1',
            'description': _GEM_OFF_TWIKI}])

GEMLayout(dqmitems, '12 GE11-P-L2 Chamber Efficiency',
          [{'path': 'GEM/Efficiency/muonSTA/eff_chamber_GE11-P-L2',
            'description': _GEM_OFF_TWIKI}])

###############################################################################
# Misc
###############################################################################
GEMLayout(dqmitems, '13 GE21-P-L2 DIGI Occupancy',
          [{'path': 'GEM/Digis/occ_GE21-P-L2',
            'description': _GEM_OFF_TWIKI}])
