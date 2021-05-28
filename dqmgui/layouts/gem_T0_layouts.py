def gemlayout(i, p, *rows): i["GEM/Layouts/" + p] = DQMItem(layout=rows)

_GEM_OFF_LINK = '<a href="https://twiki.cern.ch/twiki/bin/view/CMS/GEMPPDOfflineDQM">Link to TWiki</a>'

gemlayout(dqmitems, "01 - Efficiency vs Chamber",
    [{ "path": "GEM/Efficiency/type1/Efficiency/eff_chamber_GE-11_L2",
       "description": _GEM_OFF_LINK },
     { "path": "GEM/Efficiency/type2/Efficiency/eff_chamber_GE-11_L2",
       "description": _GEM_OFF_LINK }],
    [{ "path": "GEM/Efficiency/type1/Efficiency/eff_chamber_GE-11_L1",
       "description": _GEM_OFF_LINK },
     { "path": "GEM/Efficiency/type2/Efficiency/eff_chamber_GE-11_L1",
       "description": _GEM_OFF_LINK }],
    [{ "path": "GEM/Efficiency/type1/Efficiency/eff_chamber_GE+11_L1",
       "description": _GEM_OFF_LINK },
     { "path": "GEM/Efficiency/type2/Efficiency/eff_chamber_GE+11_L1",
       "description": _GEM_OFF_LINK }],
    [{ "path": "GEM/Efficiency/type1/Efficiency/eff_chamber_GE+11_L2",
       "description": _GEM_OFF_LINK },
     { "path": "GEM/Efficiency/type2/Efficiency/eff_chamber_GE+11_L2",
       "description": _GEM_OFF_LINK }],
)

gemlayout(dqmitems, "02 - Efficiency vs Muon PT",
    [{ "path": "GEM/Efficiency/type1/Efficiency/eff_muon_pt_GE-11",
       "description": _GEM_OFF_LINK },
     { "path": "GEM/Efficiency/type1/Efficiency/eff_muon_pt_GE+11",
       "description": _GEM_OFF_LINK }],
    [{ "path": "GEM/Efficiency/type2/Efficiency/eff_muon_pt_GE-11",
       "description": _GEM_OFF_LINK },
     { "path": "GEM/Efficiency/type2/Efficiency/eff_muon_pt_GE+11",
       "description": _GEM_OFF_LINK }]
)

gemlayout(dqmitems, "03 - Efficiency vs Muon Eta",
    [{ "path": "GEM/Efficiency/type1/Efficiency/eff_muon_eta_GE-11",
       "description": _GEM_OFF_LINK },
     { "path": "GEM/Efficiency/type1/Efficiency/eff_muon_eta_GE+11",
       "description": _GEM_OFF_LINK }],
    [{ "path": "GEM/Efficiency/type2/Efficiency/eff_muon_eta_GE-11",
       "description": _GEM_OFF_LINK },
     { "path": "GEM/Efficiency/type2/Efficiency/eff_muon_eta_GE+11",
       "description": _GEM_OFF_LINK }]
)

gemlayout(dqmitems, "04 - Resolution Summary",
    [{ "path": "GEM/Efficiency/type1/Resolution/residual_rphi_mean",
       "description": _GEM_OFF_LINK },
     { "path": "GEM/Efficiency/type1/Resolution/residual_rphi_stddev",
       "description": _GEM_OFF_LINK },
     { "path": "GEM/Efficiency/type1/Resolution/residual_rphi_skewness",
       "description": _GEM_OFF_LINK }],
    [{ "path": "GEM/Efficiency/type2/Resolution/residual_rphi_mean",
       "description": _GEM_OFF_LINK },
     { "path": "GEM/Efficiency/type2/Resolution/residual_rphi_stddev",
       "description": _GEM_OFF_LINK },
     { "path": "GEM/Efficiency/type2/Resolution/residual_rphi_skewness",
       "description": _GEM_OFF_LINK }],
)
