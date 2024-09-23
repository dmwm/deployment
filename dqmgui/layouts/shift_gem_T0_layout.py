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

GEMLayout(dqmitems, '13 GE11-M-L1 Eta Efficiency',
          [{'path': 'GEM/Efficiency/muonGLB/eff_ieta_GE11-M-L1',
            'description': _GEM_OFF_TWIKI}])

GEMLayout(dqmitems, '14 GE11-M-L2 Eta Efficiency',
          [{'path': 'GEM/Efficiency/muonGLB/eff_ieta_GE11-M-L2',
            'description': _GEM_OFF_TWIKI}])

GEMLayout(dqmitems, '15 GE11-P-L1 Eta Efficiency',
          [{'path': 'GEM/Efficiency/muonGLB/eff_ieta_GE11-P-L1',
            'description': _GEM_OFF_TWIKI}])

GEMLayout(dqmitems, '16 GE11-P-L2 Eta Efficiency',
          [{'path': 'GEM/Efficiency/muonGLB/eff_ieta_GE11-P-L2',
            'description': _GEM_OFF_TWIKI}])

###############################################################################
# Residual distribution
###############################################################################

GEMLayout(dqmitems, '17 GE11-M-E1 Residual phi',
          [{'path': 'GEM/Efficiency/muonGLB/residual_phi_GE11-M-E1',
            'description': _GEM_OFF_TWIKI}])

GEMLayout(dqmitems, '18 GE11-M-E2 Residual phi',
          [{'path': 'GEM/Efficiency/muonGLB/residual_phi_GE11-M-E2',
            'description': _GEM_OFF_TWIKI}])

GEMLayout(dqmitems, '19 GE11-M-E3 Residual phi',
          [{'path': 'GEM/Efficiency/muonGLB/residual_phi_GE11-M-E3',
            'description': _GEM_OFF_TWIKI}])

GEMLayout(dqmitems, '20 GE11-M-E4 Residual phi',
          [{'path': 'GEM/Efficiency/muonGLB/residual_phi_GE11-M-E4',
            'description': _GEM_OFF_TWIKI}])

GEMLayout(dqmitems, '21 GE11-M-E5 Residual phi',
          [{'path': 'GEM/Efficiency/muonGLB/residual_phi_GE11-M-E5',
            'description': _GEM_OFF_TWIKI}])

GEMLayout(dqmitems, '22 GE11-M-E6 Residual phi',
          [{'path': 'GEM/Efficiency/muonGLB/residual_phi_GE11-M-E6',
            'description': _GEM_OFF_TWIKI}])

GEMLayout(dqmitems, '23 GE11-M-E7 Residual phi',
          [{'path': 'GEM/Efficiency/muonGLB/residual_phi_GE11-M-E7',
            'description': _GEM_OFF_TWIKI}])

GEMLayout(dqmitems, '24 GE11-M-E8 Residual phi',
          [{'path': 'GEM/Efficiency/muonGLB/residual_phi_GE11-M-E8',
            'description': _GEM_OFF_TWIKI}])

GEMLayout(dqmitems, '25 GE11-P-E1 Residual phi',
          [{'path': 'GEM/Efficiency/muonGLB/residual_phi_GE11-P-E1',
            'description': _GEM_OFF_TWIKI}])

GEMLayout(dqmitems, '26 GE11-P-E2 Residual phi',
          [{'path': 'GEM/Efficiency/muonGLB/residual_phi_GE11-P-E2',
            'description': _GEM_OFF_TWIKI}])

GEMLayout(dqmitems, '27 GE11-P-E3 Residual phi',
          [{'path': 'GEM/Efficiency/muonGLB/residual_phi_GE11-P-E3',
            'description': _GEM_OFF_TWIKI}])

GEMLayout(dqmitems, '28 GE11-P-E4 Residual phi',
          [{'path': 'GEM/Efficiency/muonGLB/residual_phi_GE11-P-E4',
            'description': _GEM_OFF_TWIKI}])

GEMLayout(dqmitems, '29 GE11-P-E5 Residual phi',
          [{'path': 'GEM/Efficiency/muonGLB/residual_phi_GE11-P-E5',
            'description': _GEM_OFF_TWIKI}])

GEMLayout(dqmitems, '30 GE11-P-E6 Residual phi',
          [{'path': 'GEM/Efficiency/muonGLB/residual_phi_GE11-P-E6',
            'description': _GEM_OFF_TWIKI}])

GEMLayout(dqmitems, '31 GE11-P-E7 Residual phi',
          [{'path': 'GEM/Efficiency/muonGLB/residual_phi_GE11-P-E7',
            'description': _GEM_OFF_TWIKI}])

GEMLayout(dqmitems, '32 GE11-P-E8 Residual phi',
          [{'path': 'GEM/Efficiency/muonGLB/residual_phi_GE11-P-E8',
            'description': _GEM_OFF_TWIKI}])

###############################################################################
# Misc
###############################################################################
GEMLayout(dqmitems, '33 GE21-P-L2 DIGI Occupancy',
          [{'path': 'GEM/Digis/occ_GE21-P-L2',
            'description': _GEM_OFF_TWIKI}])

