def l1tlayout(i, p, *rows): i["00 Shift/L1T/" + p] = DQMItem(layout=rows)

l1tlayout(dqmitems,"00 - BMTF WEDGE BX",
    [{'path': "L1T2016/L1TStage2BMTF/bmtf_wedge_bx", 'description': "BMTF WEDGE BX. x-axis: BMTF WEDGE; y-axis: BMTF BX.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"01 - BMTF HW ETA HW GLOBAL PHI",
    [{'path': "L1T2016/L1TStage2BMTF/bmtf_hwEta_hwGlobalPhi", 'description': "BMTF HW ETA HW GLOBAL PHI. x-axis: BMTF HW ETA; y-axis: BMTF GLOBAL PHI.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"02 - CaloLayer2 CENTRAL JET E_{T} ETA PHI",
    [{'path': "L1T2016/L1TStage2CaloLayer2/Central-Jets/CenJetsEtEtaPhi", 'description': "CaloLayer2 CENTRAL JET E_{T} ETA PHI. x-axis: CaloLayer2 CENTRAL JET E_{T} ETA; y-axis: CaloLayer2 CENTRAL JET E_{T} PHI.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"03 - CaloLayer2 FORWARD JET E_{T} ETA PHI",
    [{'path': "L1T2016/L1TStage2CaloLayer2/Forward-Jets/ForJetsEtEtaPhi", 'description': "CaloLayer2 FORWARD JET E_{T} ETA PHI. x-axis: CaloLayer2 FORWARD JET E_{T} ETA; y-axis: CaloLayer2 FORWARD JET E_{T} PHI.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"04 - CaloLayer2 ISO EG E_{T} ETA PHI",
    [{'path': "L1T2016/L1TStage2CaloLayer2/Isolated-EG/IsoEGsEtEtaPhi", 'description': "CaloLayer2 ISO EG E_{T} ETA PHI. x-axis: CaloLayer2 ISO EG E_{T} ETA; y-axis: CaloLayer2 ISO EG E_{T} PHI.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"05 - CaloLayer2 NonISO EG E_{T} ETA PHI",
    [{'path': "L1T2016/L1TStage2CaloLayer2/NonIsolated-EG/NonIsoEGsEtEtaPhi", 'description': "CaloLayer2 NonISO EG E_{T} ETA PHI. x-axis: CaloLayer2 NonISO EG E_{T} ETA; y-axis: CaloLayer2 NonISO EG E_{T} PHI.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"06 - CaloLayer2 ISO TAU E_{T} ETA PHI",
    [{'path': "L1T2016/L1TStage2CaloLayer2/Isolated-Tau/IsoTausEtEtaPhi", 'description': "CaloLayer2 ISO TAU E_{T} ETA PHI. x-axis: CaloLayer2 ISO TAU E_{T} ETA; y-axis: CaloLayer2 ISO TAU E_{T} PHI.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"07 - CaloLayer2 NonISO TAU E_{T} ETA PHI",
    [{'path': "L1T2016/L1TStage2CaloLayer2/NonIsolated-Tau/TausEtEtaPhi", 'description': "CaloLayer2 NonISO TAU E_{T} ETA PHI. x-axis: CaloLayer2 NonISO TAU E_{T} ETA; y-axis: CaloLayer2 NonISO TAU E_{T} PHI.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"08 - CaloLayer2 CENTRAL JET BX OCCUPANCY",
    [{'path': "L1T2016/L1TStage2CaloLayer2/Central-Jets/CenJetsBxOcc", 'description': "CaloLayer2 CENTRAL JET BX OCCUPANCY. x-axis: CaloLayer2 CENTRAL JET BX; y-axis: CaloLayer2 CENTRAL JET OCCUPANCY.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"09 - CaloLayer2 FORWARD JET BX OCCUPANCY",
    [{'path': "L1T2016/L1TStage2CaloLayer2/Forward-Jets/ForJetsBxOcc", 'description': "CaloLayer2 FORWARD JET BX OCCUPANCY. x-axis: CaloLayer2 FORWARD JET BX; y-axis: CaloLayer2 FORWARD JET OCCUPANCY.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"10 - CaloLayer2 ISO EG BX OCCUPANCY",
    [{'path': "L1T2016/L1TStage2CaloLayer2/Isolated-EG/IsoEGsBxOcc", 'description': "CaloLayer2 ISO EG BX OCCUPANCY. x-axis: CaloLayer2 ISO EG BX; y-axis: CaloLayer2 ISO EG OCCUPANCY.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"11 - CaloLayer2 NonISO EG BX OCCUPANCY",
    [{'path': "L1T2016/L1TStage2CaloLayer2/NonIsolated-EG/NonIsoEGsBxOcc", 'description': "CaloLayer2 NonISO EG BX OCCUPANCY. x-axis: CaloLayer2 NonISO EG BX; y-axis: CaloLayer2 NonISO EG OCCUPANCY.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"12 - CaloLayer2 ISO TAU BX OCCUPANCY",
    [{'path': "L1T2016/L1TStage2CaloLayer2/Isolated-Tau/IsoTausBxOcc", 'description': "CaloLayer2 ISO TAU BX OCCUPANCY. x-axis: CaloLayer2 ISO TAU BX; y-axis: CaloLayer2 ISO TAU OCCUPANCY.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"13 - CaloLayer2 NonISO TAU BX OCCUPANCY",
    [{'path': "L1T2016/L1TStage2CaloLayer2/NonIsolated-Tau/TausBxOcc", 'description': "CaloLayer2 NonISO TAU BX OCCUPANCY. x-axis: CaloLayer2 NonISO TAU BX; y-axis: CaloLayer2 NonISO TAU OCCUPANCY.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"14 - CaloLayer2 EtSum BX OCCUPANCY",
    [{'path': "L1T2016/L1TStage2CaloLayer2/Energy-Sums/EtSumBxOcc", 'description': "CaloLayer2 EtSum BX OCCUPANCY. x-axis: CaloLayer2 EtSum BX; y-axis: CaloLayer2 EtSum OCCUPANCY.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"15 - uGMT MUON BX",
    [{'path': "L1T2016/L1TStage2uGMT/ugmtMuonBX", 'description': "uGMT Muon BX. x-axis: uGMT Muon BX.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"16 - uGMT MUON ETA",
    [{'path': "L1T2016/L1TStage2uGMT/ugmtMuonEta", 'description': "uGMT MUON ETA. x-axis: uGMT MUON ETA.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"17 - uGMT MUON P_{T}",
    [{'path': "L1T2016/L1TStage2uGMT/ugmtMuonPt", 'description': "uGMT MUON P_{T}. x-axis: uGMT MUON P_{T}.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"18 - uGMT MUON PHI ETA",
    [{'path': "L1T2016/L1TStage2uGMT/ugmtMuonPhivsEta", 'description': "uGMT MUON PHI ETA. x-axis: uGMT MUON PHI; y-axis: uGMT MUON ETA.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"19 - uGMT MUON HW QUALITY",
    [{'path': "L1T2016/L1TStage2uGMT/ugmtMuonhwQual", 'description': "uGMT Muon HW Quality. x-axis: uGMT Muon HW Quality.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"20 - uGMT BMTF Input BX",
    [{'path': "L1T2016/L1TStage2uGMT/BMTFInput/ugmtBMTFBX", 'description': "uGMT BMTF Input BX. x-axis: uGMT BMTF Input BX.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"21 - uGMT BMTF Input HW Global PHI",
    [{'path': "L1T2016/L1TStage2uGMT/BMTFInput/ugmtBMTFglbhwPhi", 'description': "uGMT BMTF Input HW Global PHI. x-axis: uGMT BMTF Input HW Global PHI.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"22 - uGMT BMTF Input HW ETA",
    [{'path': "L1T2016/L1TStage2uGMT/BMTFInput/ugmtBMTFhwEta", 'description': "uGMT BMTF Input HW ETA. x-axis: uGMT BMTF Input HW ETA.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"23 - uGMT BMTF Input P_{T}",
    [{'path': "L1T2016/L1TStage2uGMT/BMTFInput/ugmtBMTFhwPt", 'description': "uGMT BMTF Input P_{T}. x-axis: uGMT BMTF Input P_{T}.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"24 - uGMT BMTF Input SIGN",
    [{'path': "L1T2016/L1TStage2uGMT/BMTFInput/ugmtBMTFhwSign", 'description': "uGMT BMTF Input SIGN. x-axis: uGMT BMTF Input SIGN.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"25 - uGMT OMTF Input BX",
    [{'path': "L1T2016/L1TStage2uGMT/OMTFInput/ugmtOMTFBX", 'description': "uGMT OMTF Input BX. x-axis: uGMT OMTF Input BX.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"26 - uGMT OMTF Input HW Global PHI Negative",
    [{'path': "L1T2016/L1TStage2uGMT/OMTFInput/ugmtOMTFglbhwPhiNeg", 'description': "uGMT OMTF Input HW Global PHI Negative. x-axis: uGMT OMTF Input HW Global PHI Negative.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"27 - uGMT OMTF Input HW Global PHI Positive",
    [{'path': "L1T2016/L1TStage2uGMT/OMTFInput/ugmtOMTFglbhwPhiNeg", 'description': "uGMT OMTF Input HW Global PHI Positive. x-axis: uGMT OMTF Input HW Global PHI Positive.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"28 - uGMT OMTF Input HW ETA",
    [{'path': "L1T2016/L1TStage2uGMT/OMTFInput/ugmtOMTFhwEta", 'description': "uGMT OMTF Input HW ETA. x-axis: uGMT OMTF Input HW ETA.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"29 - uGMT OMTF Input P_{T}",
    [{'path': "L1T2016/L1TStage2uGMT/OMTFInput/ugmtOMTFhwPt", 'description': "uGMT OMTF Input P_{T}. x-axis: uGMT OMTF Input P_{T}.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"30 - uGMT OMTF Input SIGN",
    [{'path': "L1T2016/L1TStage2uGMT/OMTFInput/ugmtOMTFhwSign", 'description': "uGMT OMTF Input SIGN. x-axis: uGMT OMTF Input SIGN.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"31 - uGMT EMTF Input BX",
    [{'path': "L1T2016/L1TStage2uGMT/EMTFInput/ugmtEMTFBX", 'description': "uGMT EMTF Input BX. x-axis: uGMT EMTF Input BX.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"32 - uGMT EMTF Input HW Global PHI Negative",
    [{'path': "L1T2016/L1TStage2uGMT/EMTFInput/ugmtEMTFglbhwPhiNeg", 'description': "uGMT EMTF Input HW Global PHI Negative. x-axis: uGMT EMTF Input HW Global PHI Negative.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"33 - uGMT EMTF Input HW Global PHI Positive",
    [{'path': "L1T2016/L1TStage2uGMT/EMTFInput/ugmtEMTFglbhwPhiPos", 'description': "uGMT EMTF Input HW Global PHI Positive. x-axis: uGMT EMTF Input HW Global PHI Positive.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"34 - uGMT EMTF Input HW ETA",
    [{'path': "L1T2016/L1TStage2uGMT/EMTFInput/ugmtEMTFhwEta", 'description': "uGMT EMTF Input HW ETA. x-axis: uGMT EMTF Input HW ETA.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"35 - uGMT EMTF Input P_{T}",
    [{'path': "L1T2016/L1TStage2uGMT/EMTFInput/ugmtEMTFhwPt", 'description': "uGMT EMTF Input P_{T}. x-axis: uGMT EMTF Input P_{T}.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"36 - uGMT EMTF Input SIGN",
    [{'path': "L1T2016/L1TStage2uGMT/EMTFInput/ugmtEMTFhwSign", 'description': "uGMT EMTF Input SIGN. x-axis: uGMT EMTF Input SIGN.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"37 - CaloLayer1 ECAL DISCREOANCY",
  [{'path': "L1T2016/L1TStage2CaloLayer1/ecalDiscrepancy", 'description': "CaloLayer1 ECAL DISCREOANCY. x-axis: CaloLayer1 ECAL DISCREOANCY.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"38 - CaloLayer1 ECAL LINK ERROR",
  [{'path': "L1T2016/L1TStage2CaloLayer1/ecalLinkError", 'description': "CaloLayer1 ECAL LINK Error. x-axis: CaloLayer1 ECAL LINK Error.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"39 - CaloLayer1 ECAL OCCUPANCY",
  [{'path': "L1T2016/L1TStage2CaloLayer1/ecalOccupancy", 'description': "CaloLayer1 ECAL OCCUPANCY. x-axis: CaloLayer1 ECAL OCCUPANCY.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"40 - CaloLayer1 HCAL DISCREOANCY",
  [{'path': "L1T2016/L1TStage2CaloLayer1/hcalDiscrepancy", 'description': "CaloLayer1 HCAL DISCREOANCY. x-axis: CaloLayer1 HCAL DISCREOANCY.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"41 - CaloLayer1 HCAL LINK ERROR",
  [{'path': "L1T2016/L1TStage2CaloLayer1/hcalLinkError", 'description': "CaloLayer1 HCAL LINK Error. x-axis: CaloLayer1 HCAL LINK Error.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"42 - CaloLayer1 HCAL OCCUPANCY",
  [{'path': "L1T2016/L1TStage2CaloLayer1/hcalOccupancy", 'description': "CaloLayer1 HCAL OCCUPANCY. x-axis: CaloLayer1 HCAL OCCUPANCY.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"43 - CaloLayer1 MAXIMUM EVENTs LINK ERROR by LUMISECTION",
  [{'path': "L1T2016/L1TStage2CaloLayer1/maxEvtLinkErrorsByLumi", 'description': "CaloLayer1 MAXIMUM EVENTs LINK ERROR by LUMISECTION. x-axis: CaloLayer1 MAXIMUM EVENTs LINK ERROR by LUMISECTION.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"44 - CaloLayer1 MAXIMUM EVENTs MISMATCHES by LUMISECTION",
  [{'path': "L1T2016/L1TStage2CaloLayer1/maxEvtMismatchByLumi", 'description': "CaloLayer1 MAXIMUM EVENTs MISMATCHES by LUMISECTION. x-axis: CaloLayer1 MAXIMUM EVENTs MISMATCHES by LUMISECTION.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])

l1tlayout(dqmitems,"45 - BMTF HW PT",
    [{'path': "L1T2016/L1TStage2BMTF/bmtf_hwPt", 'description': "BMTF HW PT. x-axis: BMTF HW PT.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftL1T\">here</a>."}])







