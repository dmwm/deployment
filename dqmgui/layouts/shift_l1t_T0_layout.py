def l1toccupancy(i, p, *rows): i["00 Shift/L1T/Occupancy/" + p] = DQMItem(layout=rows)

l1toccupancy(dqmitems,"00 - BMTF WEDGE BX",
    [{'path': "L1T/L1TStage2BMTF/bmtf_wedge_bx", 'description': "BMTF WEDGE BX. x-axis: BMTF WEDGE; y-axis: BMTF BX.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>.", 'draw': { 'withref': "no" }}])
l1toccupancy(dqmitems,"01 - BMTF HW PT",
    [{'path': "L1T/L1TStage2BMTF/bmtf_hwPt", 'description': "BMTF HW PT. x-axis: BMTF HW PT.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>.", 'draw': { 'withref': "yes" }}])
l1toccupancy(dqmitems,"02 - CaloLayer1 ECAL OCCUPANCY",
  [{'path': "L1T/L1TStage2CaloLayer1/ecalOccupancy", 'description': "CaloLayer1 ECAL OCCUPANCY. x-axis: CaloLayer1 ECAL OCCUPANCY.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>.", 'draw': { 'withref': "no" }}])
l1toccupancy(dqmitems,"03 - CaloLayer1 HCAL OCCUPANCY",
  [{'path': "L1T/L1TStage2CaloLayer1/hcalOccupancy", 'description': "CaloLayer1 HCAL OCCUPANCY. x-axis: CaloLayer1 HCAL OCCUPANCY.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>.", 'draw': { 'withref': "no" }}])
l1toccupancy(dqmitems,"04 - CaloLayer2 CENTRAL JET E_{T} ETA PHI",
    [{'path': "L1T/L1TStage2CaloLayer2/Central-Jets/CenJetsEtEtaPhi", 'description': "CaloLayer2 CENTRAL JET E_{T} ETA PHI. x-axis: CaloLayer2 CENTRAL JET E_{T} ETA; y-axis: CaloLayer2 CENTRAL JET E_{T} PHI.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>.", 'draw': { 'withref': "no" }}])
l1toccupancy(dqmitems,"05 - CaloLayer2 FORWARD JET E_{T} ETA PHI",
    [{'path': "L1T/L1TStage2CaloLayer2/Forward-Jets/ForJetsEtEtaPhi", 'description': "CaloLayer2 FORWARD JET E_{T} ETA PHI. x-axis: CaloLayer2 FORWARD JET E_{T} ETA; y-axis: CaloLayer2 FORWARD JET E_{T} PHI.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>.", 'draw': { 'withref': "no" }}])
l1toccupancy(dqmitems,"06 - CaloLayer2 ISO EG E_{T} ETA PHI",
    [{'path': "L1T/L1TStage2CaloLayer2/Isolated-EG/IsoEGsEtEtaPhi", 'description': "CaloLayer2 ISO EG E_{T} ETA PHI. x-axis: CaloLayer2 ISO EG E_{T} ETA; y-axis: CaloLayer2 ISO EG E_{T} PHI.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>.", 'draw': { 'withref': "no" }}])
l1toccupancy(dqmitems,"07 - CaloLayer2 NonISO EG E_{T} ETA PHI",
    [{'path': "L1T/L1TStage2CaloLayer2/NonIsolated-EG/NonIsoEGsEtEtaPhi", 'description': "CaloLayer2 NonISO EG E_{T} ETA PHI. x-axis: CaloLayer2 NonISO EG E_{T} ETA; y-axis: CaloLayer2 NonISO EG E_{T} PHI.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>.", 'draw': { 'withref': "no" }}])
l1toccupancy(dqmitems,"08 - CaloLayer2 ISO TAU E_{T} ETA PHI",
    [{'path': "L1T/L1TStage2CaloLayer2/Isolated-Tau/IsoTausEtEtaPhi", 'description': "CaloLayer2 ISO TAU E_{T} ETA PHI. x-axis: CaloLayer2 ISO TAU E_{T} ETA; y-axis: CaloLayer2 ISO TAU E_{T} PHI.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>.", 'draw': { 'withref': "no" }}])
l1toccupancy(dqmitems,"09 - CaloLayer2 NonISO TAU E_{T} ETA PHI",
    [{'path': "L1T/L1TStage2CaloLayer2/NonIsolated-Tau/TausEtEtaPhi", 'description': "CaloLayer2 NonISO TAU E_{T} ETA PHI. x-axis: CaloLayer2 NonISO TAU E_{T} ETA; y-axis: CaloLayer2 NonISO TAU E_{T} PHI.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>.", 'draw': { 'withref': "no" }}])
l1toccupancy(dqmitems,"10 - uGMT MUON BX",
    [{'path': "L1T/L1TStage2uGMT/ugmtMuonBX", 'description': "uGMT Muon BX. x-axis: uGMT Muon BX.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>.", 'draw': { 'withref': "yes" }}])
l1toccupancy(dqmitems,"11 - uGMT MUON ETA",
    [{'path': "L1T/L1TStage2uGMT/ugmtMuonEta", 'description': "uGMT MUON ETA. x-axis: uGMT MUON ETA.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>.", 'draw': { 'withref': "yes" }}])
l1toccupancy(dqmitems,"12 - uGMT MUON P_{T}",
    [{'path': "L1T/L1TStage2uGMT/ugmtMuonPt", 'description': "uGMT MUON P_{T}. x-axis: uGMT MUON P_{T}.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>.", 'draw': { 'withref': "yes" }}])
l1toccupancy(dqmitems,"13 - uGMT MUON PHI ETA",
    [{'path': "L1T/L1TStage2uGMT/ugmtMuonPhivsEta", 'description': "uGMT MUON PHI ETA. x-axis: uGMT MUON PHI; y-axis: uGMT MUON ETA.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>.", 'draw': { 'withref': "no" }}])
l1toccupancy(dqmitems,"14 - uGMT BMTF Input BX",
    [{'path': "L1T/L1TStage2uGMT/BMTFInput/ugmtBMTFBX", 'description': "uGMT BMTF Input BX. x-axis: uGMT BMTF Input BX.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>.", 'draw': { 'withref': "yes" }}])
l1toccupancy(dqmitems,"15 - uGMT BMTF Input HW Global PHI",
    [{'path': "L1T/L1TStage2uGMT/BMTFInput/ugmtBMTFglbhwPhi", 'description': "uGMT BMTF Input HW Global PHI. x-axis: uGMT BMTF Input HW Global PHI.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>.", 'draw': { 'withref': "yes" }}])
l1toccupancy(dqmitems,"16 - uGMT BMTF Input HW ETA",
    [{'path': "L1T/L1TStage2uGMT/BMTFInput/ugmtBMTFhwEta", 'description': "uGMT BMTF Input HW ETA. x-axis: uGMT BMTF Input HW ETA.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>.", 'draw': { 'withref': "yes" }}])
l1toccupancy(dqmitems,"17 - uGMT BMTF Input SIGN",
    [{'path': "L1T/L1TStage2uGMT/BMTFInput/ugmtBMTFhwSign", 'description': "uGMT BMTF Input SIGN. x-axis: uGMT BMTF Input SIGN.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>.", 'draw': { 'withref': "yes" }}])
l1toccupancy(dqmitems,"18 - uGMT OMTF Input BX",
    [{'path': "L1T/L1TStage2uGMT/OMTFInput/ugmtOMTFBX", 'description': "uGMT OMTF Input BX. x-axis: uGMT OMTF Input BX.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>.", 'draw': { 'withref': "yes" }}])
l1toccupancy(dqmitems,"19 - uGMT OMTF Input HW Global PHI Negative",
    [{'path': "L1T/L1TStage2uGMT/OMTFInput/ugmtOMTFglbhwPhiNeg", 'description': "uGMT OMTF Input HW Global PHI Negative. x-axis: uGMT OMTF Input HW Global PHI Negative.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>.", 'draw': { 'withref': "yes" }}])
l1toccupancy(dqmitems,"20 - uGMT OMTF Input HW Global PHI Positive",
    [{'path': "L1T/L1TStage2uGMT/OMTFInput/ugmtOMTFglbhwPhiPos", 'description': "uGMT OMTF Input HW Global PHI Positive. x-axis: uGMT OMTF Input HW Global PHI Positive.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>.", 'draw': { 'withref': "yes" }}])
l1toccupancy(dqmitems,"21 - uGMT OMTF Input HW ETA",
    [{'path': "L1T/L1TStage2uGMT/OMTFInput/ugmtOMTFhwEta", 'description': "uGMT OMTF Input HW ETA. x-axis: uGMT OMTF Input HW ETA.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>.", 'draw': { 'withref': "yes" }}])
l1toccupancy(dqmitems,"22 - uGMT OMTF Input P_{T}",
    [{'path': "L1T/L1TStage2uGMT/OMTFInput/ugmtOMTFhwPt", 'description': "uGMT OMTF Input P_{T}. x-axis: uGMT OMTF Input P_{T}.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>.", 'draw': { 'withref': "yes" }}])
l1toccupancy(dqmitems,"23 - uGMT OMTF Input SIGN",
    [{'path': "L1T/L1TStage2uGMT/OMTFInput/ugmtOMTFhwSign", 'description': "uGMT OMTF Input SIGN. x-axis: uGMT OMTF Input SIGN.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>.", 'draw': { 'withref': "yes" }}])
l1toccupancy(dqmitems,"24 - uGMT EMTF Input BX",
    [{'path': "L1T/L1TStage2uGMT/EMTFInput/ugmtEMTFBX", 'description': "uGMT EMTF Input BX. x-axis: uGMT EMTF Input BX.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>.", 'draw': { 'withref': "yes" }}])
l1toccupancy(dqmitems,"25 - uGMT EMTF Input HW Global PHI Negative",
    [{'path': "L1T/L1TStage2uGMT/EMTFInput/ugmtEMTFglbhwPhiNeg", 'description': "uGMT EMTF Input HW Global PHI Negative. x-axis: uGMT EMTF Input HW Global PHI Negative.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>.", 'draw': { 'withref': "yes" }}])
l1toccupancy(dqmitems,"26 - uGMT EMTF Input HW Global PHI Positive",
    [{'path': "L1T/L1TStage2uGMT/EMTFInput/ugmtEMTFglbhwPhiPos", 'description': "uGMT EMTF Input HW Global PHI Positive. x-axis: uGMT EMTF Input HW Global PHI Positive.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>.", 'draw': { 'withref': "yes" }}])
l1toccupancy(dqmitems,"27 - uGT Algorithm Trigger Bits (after prescale) vs. Global BX Number",
    [{'path': "L1T/L1TStage2uGT/algoBits_after_prescale_bx_global", 'description': "uGT Algorithm Trigger Bits (after prescale) vs. Global BX Number. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>.", 'draw': { 'withref': "no" }}])
l1toccupancy(dqmitems,"28 - uGT Algorithm Trigger Bits (after prescale) vs. BX Number in Event",
    [{'path': "L1T/L1TStage2uGT/algoBits_after_prescale_bx_inEvt", 'description': "uGT Algorithm Trigger Bits (after prescale) vs. BX Number in Event. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>.", 'draw': { 'withref': "no" }}])
l1toccupancy(dqmitems,"29 - uGMT Muon Phi for EMTF Inputs",
    [{'path': "L1T/L1TStage2uGMT/ugmtMuonPhiEmtf", 'description': "uGMT Muon Phi for EMTF Inputs.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>.", 'draw': { 'withref': "yes" }}])
l1toccupancy(dqmitems,"30 - EMTF Chamber Occupancy",
    [{'path': "L1T/L1TStage2EMTF/cscLCTOccupancy", 'description': "EMTF CSC chamber Occupancy. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>.", 'draw': { 'withref': "no" }}])
l1toccupancy(dqmitems,"31 - EMTF Track Bunch Crossing",
    [{'path': "L1T/L1TStage2EMTF/emtfTrackBX", 'description': "EMTF Track Bunch Crossing. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>.", 'draw': { 'withref': "no" }}])



def l1tefficiency(i, p, *rows): i["00 Shift/L1T/Efficiency/" + p] = DQMItem(layout=rows)

l1tefficiency(dqmitems, "00 - Reco Muon L1T Efficiency",
  [{'path': "L1T/L1TMuon/EffvsPt_SINGLE_25", 'description': "", 'draw': { 'withref': "yes" }},
   {'path': "L1T/L1TMuon/EffvsPt_DOUBLE_16", 'description': "", 'draw': { 'withref': "yes" }},
   {'path': "L1T/L1TMuon/EffvsPt_OPEN_16", 'description': "", 'draw': { 'withref': "yes" }}],
  [{'path': "L1T/L1TMuon/EffvsEta_SINGLE_25", 'description': "", 'draw': { 'withref': "yes" }},
   {'path': "L1T/L1TMuon/EffvsEta_DOUBLE_16", 'description': "", 'draw': { 'withref': "yes" }},
   {'path': "L1T/L1TMuon/EffvsEta_OPEN_16", 'description': "", 'draw': { 'withref': "yes" }}],
  [{'path': "L1T/L1TMuon/EffvsPhi_SINGLE_25", 'description': "", 'draw': { 'withref': "yes" }},
   {'path': "L1T/L1TMuon/EffvsPhi_DOUBLE_16", 'description': "", 'draw': { 'withref': "yes" }},
   {'path': "L1T/L1TMuon/EffvsPhi_OPEN_16", 'description': "", 'draw': { 'withref': "yes" }}])

l1tefficiency(dqmitems, "01 - Reco Photon L1T Efficiency",
  [{'path': "L1T/L1TEGamma/efficiencyPhotonET_EB_EE_threshold_36", 'description': "", 'draw': { 'withref': "yes" }},
   {'path': "L1T/L1TEGamma/efficiencyPhotonET_EB_EE_threshold_68", 'description': "", 'draw': { 'withref': "yes" }}],
  [{'path': "L1T/L1TEGamma/efficiencyPhotonET_EB_EE_threshold_128", 'description': "", 'draw': { 'withref': "yes" }},
   {'path': "L1T/L1TEGamma/efficiencyPhotonET_EB_EE_threshold_176", 'description': "", 'draw': { 'withref': "yes" }}])

l1tefficiency(dqmitems, "02 - Reco Electron L1T Efficiency",
  [{'path': "L1T/L1TEGamma/efficiencyElectronET_EB_EE_threshold_36", 'description': "", 'draw': { 'withref': "yes" }},
   {'path': "L1T/L1TEGamma/efficiencyElectronET_EB_EE_threshold_68", 'description': "", 'draw': { 'withref': "yes" }}],
  [{'path': "L1T/L1TEGamma/efficiencyElectronET_EB_EE_threshold_128", 'description': "", 'draw': { 'withref': "yes" }},
   {'path': "L1T/L1TEGamma/efficiencyElectronET_EB_EE_threshold_176", 'description': "", 'draw': { 'withref': "yes" }}])

l1tefficiency(dqmitems, "03 - Reco IsoTau L1T Efficiency",
  [{'path': "L1T/L1TTau/efficiencyIsoTauET_EB_EE_threshold_28", 'description': "", 'draw': { 'withref': "yes" }},
   {'path': "L1T/L1TTau/efficiencyIsoTauET_EB_EE_threshold_32", 'description': "", 'draw': { 'withref': "yes" }}],
  [{'path': "L1T/L1TTau/efficiencyIsoTauET_EB_EE_threshold_128", 'description': "", 'draw': { 'withref': "yes" }},
   {'path': "L1T/L1TTau/efficiencyIsoTauET_EB_EE_threshold_176", 'description': "", 'draw': { 'withref': "yes" }}])

l1tefficiency(dqmitems, "04 - Reco NonIsoTau L1T Efficiency",
  [{'path': "L1T/L1TTau/efficiencyNonIsoTauET_EB_EE_threshold_28", 'description': "", 'draw': { 'withref': "yes" }},
   {'path': "L1T/L1TTau/efficiencyNonIsoTauET_EB_EE_threshold_32", 'description': "", 'draw': { 'withref': "yes" }}],
  [{'path': "L1T/L1TTau/efficiencyNonIsoTauET_EB_EE_threshold_128", 'description': "", 'draw': { 'withref': "yes" }},
   {'path': "L1T/L1TTau/efficiencyNonIsoTauET_EB_EE_threshold_176", 'description': "", 'draw': { 'withref': "yes" }}])

l1tefficiency(dqmitems, "05 - Reco Jet L1T Efficiency",
  [{'path': "L1T/L1TStage2CaloLayer2/efficiencyJetEt_HB_HE_threshold_36", 'description': "", 'draw': { 'withref': "yes" }},
   {'path': "L1T/L1TStage2CaloLayer2/efficiencyJetEt_HB_HE_threshold_68", 'description': "", 'draw': { 'withref': "yes" }}],
  [{'path': "L1T/L1TStage2CaloLayer2/efficiencyJetEt_HB_HE_threshold_128", 'description': "", 'draw': { 'withref': "yes" }},
   {'path': "L1T/L1TStage2CaloLayer2/efficiencyJetEt_HB_HE_threshold_176", 'description': "", 'draw': { 'withref': "yes" }}])

l1tefficiency(dqmitems, "06 - Reco MET L1T Efficiency",
  [{'path': "L1T/L1TStage2CaloLayer2/efficiencyMET_threshold_40", 'description': "", 'draw': { 'withref': "yes" }},
   {'path': "L1T/L1TStage2CaloLayer2/efficiencyMET_threshold_60", 'description': "", 'draw': { 'withref': "yes" }}],
  [{'path': "L1T/L1TStage2CaloLayer2/efficiencyMET_threshold_80", 'description': "", 'draw': { 'withref': "yes" }},
   {'path': "L1T/L1TStage2CaloLayer2/efficiencyMET_threshold_100", 'description': "", 'draw': { 'withref': "yes" }},
   {'path': "L1T/L1TStage2CaloLayer2/efficiencyMET_threshold_120", 'description': "", 'draw': { 'withref': "yes" }}])


def l1tresolution(i, p, *rows): i["00 Shift/L1T/Resolution/" + p] = DQMItem(layout=rows)

l1tresolution(dqmitems, "00 - Photon",
  [{'path': "L1T/L1TEGamma/resolutionPhotonET_EB", 'description': "", 'draw': { 'withref': "yes" }},
   {'path': "L1T/L1TEGamma/resolutionPhotonET_EE", 'description': "", 'draw': { 'withref': "yes" }}],
  [{'path': "L1T/L1TEGamma/resolutionPhotonEta", 'description': "", 'draw': { 'withref': "yes" }},
   {'path': "L1T/L1TEGamma/resolutionPhotonPhi_EB", 'description': "", 'draw': { 'withref': "yes" }},
   {'path': "L1T/L1TEGamma/resolutionPhotonPhi_EE", 'description': "", 'draw': { 'withref': "yes" }}])

l1tresolution(dqmitems, "01 - Electron",
  [{'path': "L1T/L1TEGamma/resolutionElectronET_EB", 'description': "", 'draw': { 'withref': "yes" }},
   {'path': "L1T/L1TEGamma/resolutionElectronET_EE", 'description': "", 'draw': { 'withref': "yes" }}],
  [{'path': "L1T/L1TEGamma/resolutionElectronEta", 'description': "", 'draw': { 'withref': "yes" }},
   {'path': "L1T/L1TEGamma/resolutionElectronPhi_EB", 'description': "", 'draw': { 'withref': "yes" }},
   {'path': "L1T/L1TEGamma/resolutionElectronPhi_EE", 'description': "", 'draw': { 'withref': "yes" }}])

l1tresolution(dqmitems, "02 - Tau",
  [{'path': "L1T/L1TTau/resolutionTauET_EB", 'description': "", 'draw': { 'withref': "yes" }},
   {'path': "L1T/L1TTau/resolutionTauET_EE", 'description': "", 'draw': { 'withref': "yes" }}],
  [{'path': "L1T/L1TTau/resolutionTauEta", 'description': "", 'draw': { 'withref': "yes" }},
   {'path': "L1T/L1TTau/resolutionTauPhi_EB", 'description': "", 'draw': { 'withref': "yes" }},
   {'path': "L1T/L1TTau/resolutionTauPhi_EE", 'description': "", 'draw': { 'withref': "yes" }}])

l1tresolution(dqmitems, "03 - Jet",
  [{'path': "L1T/L1TStage2CaloLayer2/resolutionJetET_HB", 'description': "", 'draw': { 'withref': "yes" }},
   {'path': "L1T/L1TStage2CaloLayer2/resolutionJetET_HE", 'description': "", 'draw': { 'withref': "yes" }},
   {'path': "L1T/L1TStage2CaloLayer2/resolutionJetET_HF", 'description': "", 'draw': { 'withref': "yes" }}],
  [{'path': "L1T/L1TStage2CaloLayer2/resolutionJetPhi_HB", 'description': "", 'draw': { 'withref': "yes" }},
   {'path': "L1T/L1TStage2CaloLayer2/resolutionJetPhi_HE", 'description': "", 'draw': { 'withref': "yes" }},
   {'path': "L1T/L1TStage2CaloLayer2/resolutionJetPhi_HF", 'description': "", 'draw': { 'withref': "yes" }}],
  [{'path': "L1T/L1TStage2CaloLayer2/resolutionJetEta", 'description': "", 'draw': { 'withref': "yes" }}])

l1tresolution(dqmitems, "04 - MET",
  [{'path': "L1T/L1TStage2CaloLayer2/resolutionETT", 'description': "", 'draw': { 'withref': "yes" }},
   {'path': "L1T/L1TStage2CaloLayer2/resolutionHTT", 'description': "", 'draw': { 'withref': "yes" }}],
  [{'path': "L1T/L1TStage2CaloLayer2/resolutionMET", 'description': "", 'draw': { 'withref': "yes" }},
   {'path': "L1T/L1TStage2CaloLayer2/resolutionMETPhi", 'description': "", 'draw': { 'withref': "yes" }}],
  [{'path': "L1T/L1TStage2CaloLayer2/resolutionMHT", 'description': "", 'draw': { 'withref': "yes" }},
   {'path': "L1T/L1TStage2CaloLayer2/resolutionMHTPhi", 'description': "", 'draw': { 'withref': "yes" }}])



# BVB 20160314: Removed content of old L1T shift workspace from before the trigger upgrade.
# Left an example below as template for upcoming new content based on L1T2016

##l1toccupancy(dqmitems,"00 Name of the plot for your shifter",
##    [{
##        'path': "L1T2016/path/to/plot",
##        'description': "Short explanation of the plot for the describe button. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."
##    }])
