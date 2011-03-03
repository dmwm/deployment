def hltlayout(i, p, *rows): i["00 Shift/HLT/" + p] = DQMItem(layout=rows)


hltlayout(dqmitems,"01 HLT_BTau_Pass_Any", [{'path': "HLT/TrigResults/PathsSummary/HLT LS/HLT_A_LS", 'description': "Shows total rate of Stream A (top Y bin) and the PD's in stream A. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])


def hltlayout(i, p, *rows): i["00 Shift/HLT/Cosmics/" + p] = DQMItem(layout=rows)


hltlayout(dqmitems,"01 HLT_Egamma_Pass_Any",
    [{'path': "HLT/FourVector/PathsSummary/HLT_Egamma_Pass_Any", 'description': "Shows total number of HLT Egamma trigger accepts and the total number of any HLT accepts. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"02 HLT_JetMet_Pass_Any",
    [{'path': "HLT/FourVector/PathsSummary/HLT_JetMet_Pass_Any", 'description': "Shows total number of HLT JetMET trigger accepts and the total number of any HLT accepts. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"03 HLT_Muon_Pass_Any",
    [{'path': "HLT/FourVector/PathsSummary/HLT_Muon_Pass_Any", 'description': "Shows total number of HLT Muon trigger accepts and the total number of any HLT accepts. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"04 HLT_Rest_Pass_Any",
    [{'path': "HLT/FourVector/PathsSummary/HLT_Rest_Pass_Any", 'description': "Shows total number of HLT Rest trigger accepts and the total number of any HLT accepts. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"05 HLT_Special_Pass_Any",
    [{'path': "HLT/FourVector/PathsSummary/HLT_Special_Pass_Any", 'description': "Shows total number of HLT Special trigger accepts and the total number of any HLT accepts. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])



def hltlayout(i, p, *rows): i["00 Shift/HLT/Collisions/" + p] = DQMItem(layout=rows)


hltlayout(dqmitems,"01 HLT_BTau_Pass_Any", [{'path': "HLT/TrigResults/PathsSummary/HLT Counts/HLT_BTau_Pass_Any", 'description': "Shows total number of BTau PD accepts and the total number of any HLT accepts in this PD. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"02 HLT_Commissioning_Pass_Any", [{'path': "HLT/TrigResults/PathsSummary/HLT Counts/HLT_Commissioning_Pass_Any", 'description': "Shows total number of Commissioning PD accepts and the total number of any HLT accepts in this PD. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"03 HLT_Cosmics_Pass_Any", [{'path': "HLT/TrigResults/PathsSummary/HLT Counts/HLT_Cosmics_Pass_Any", 'description': "Shows total number of Cosmics PD accepts and the total number of any HLT accepts in this PD. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"04 HLT_EGMonitor_Pass_Any", [{'path': "HLT/TrigResults/PathsSummary/HLT Counts/HLT_EGMonitor_Pass_Any", 'description': "Shows total number of EGMonitor PD accepts and the total number of any HLT accepts in this PD. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"05 HLT_Electron_Pass_Any", [{'path': "HLT/TrigResults/PathsSummary/HLT Counts/HLT_Electron_Pass_Any", 'description': "Shows total number of Electron PD accepts and the total number of any HLT accepts in this PD. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"06 HLT_HcalHPDNoise_Pass_Any", [{'path': "HLT/TrigResults/PathsSummary/HLT Counts/HLT_HcalHPDNoise_Pass_Any", 'description': "Shows total number of HcalHPDNoise PD accepts and the total number of any HLT accepts in this PD. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"07 HLT_HcalNZS_Pass_Any", [{'path': "HLT/TrigResults/PathsSummary/HLT Counts/HLT_HcalNZS_Pass_Any", 'description': "Shows total number of HcalNZS PD accepts and the total number of any HLT accepts in this PD. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"08 HLT_Jet_Pass_Any", [{'path': "HLT/TrigResults/PathsSummary/HLT Counts/HLT_Jet_Pass_Any", 'description': "Shows total number of Jet PD accepts and the total number of any HLT accepts in this PD. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"09 HLT_JetMETTauMonitor_Pass_Any", [{'path': "HLT/TrigResults/PathsSummary/HLT Counts/HLT_JetMETTauMonitor_Pass_Any", 'description': "Shows total number of JetMETTauMonitor PD accepts and the total number of any HLT accepts in this PD. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"10 HLT_METFwd_Pass_Any", [{'path': "HLT/TrigResults/PathsSummary/HLT Counts/HLT_METFwd_Pass_Any", 'description': "Shows total number of METFwd PD accepts and the total number of any HLT accepts in this PD. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"11 HLT_MinimumBias_Pass_Any", [{'path': "HLT/TrigResults/PathsSummary/HLT Counts/HLT_MinimumBias_Pass_Any", 'description': "Shows total number of MinimumBias PD accepts and the total number of any HLT accepts in this PD. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"12 HLT_Mu_Pass_Any", [{'path': "HLT/TrigResults/PathsSummary/HLT Counts/HLT_Mu_Pass_Any", 'description': "Shows total number of Mu PD accepts and the total number of any HLT accepts in this PD. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"13 HLT_MuMonitor_Pass_Any", [{'path': "HLT/TrigResults/PathsSummary/HLT Counts/HLT_MuMonitor_Pass_Any", 'description': "Shows total number of MuMonitor PD accepts and the total number of any HLT accepts in this PD. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"14 HLT_MuOnia_Pass_Any", [{'path': "HLT/TrigResults/PathsSummary/HLT Counts/HLT_MuOnia_Pass_Any", 'description': "Shows total number of MuOnia PD accepts and the total number of any HLT accepts in this PD. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"15 HLT_MultiJet_Pass_Any", [{'path': "HLT/TrigResults/PathsSummary/HLT Counts/HLT_MultiJet_Pass_Any", 'description': "Shows total number of MultiJet PD accepts and the total number of any HLT accepts in this PD. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

hltlayout(dqmitems,"16 HLT_Photon_Pass_Any", [{'path': "HLT/TrigResults/PathsSummary/HLT Counts/HLT_Photon_Pass_Any", 'description': "Shows total number of Photon PD accepts and the total number of any HLT accepts in this PD. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/TriggerShiftHLTGuide\">here</a>."}])

