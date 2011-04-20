

###---- GENERIC - FourVector selection goes here: ####
######################################################

###---- GENERIC - FourVector Muon
def trigvalFVMuon(i, p, *rows): i["00 Shift/HLT/FourVector/Muon/" + p] = DQMItem(layout=rows)


trigvalFVMuon(dqmitems,"Muon Eff HLT to L1",
[{'path': "HLT/FourVector/paths/HLT_Mu9/custom-eff/HLT_Mu9_wrt__l1Et_Eff_OnToL1", 'description':"Efficiency of HLT to L1 for path HLT_Mu9"}])

trigvalFVMuon(dqmitems,"Muon Eff HLT to RECO",
[{'path': "HLT/FourVector/paths/HLT_Mu9/custom-eff/HLT_Mu9_wrt__offEt_Eff_OnToOff", 'description':"Efficiency of HLT to RECO for path HLT_Mu9"}])

trigvalFVMuon(dqmitems,"HLT_Mu9: Et of L1 Muon Objects",
[{'path': "HLT/FourVector/paths/HLT_Mu9/HLT_Mu9_wrt__l1EtL1", 'description':"Et of L1 Muon object for path HLT_Mu9"}])

trigvalFVMuon(dqmitems,"HLT_Mu9: Et of HLT Muon Objects",
[{'path': "HLT/FourVector/paths/HLT_Mu9/HLT_Mu9_wrt__onEtOn", 'description':"Et of HLT Muon object for path HLT_Mu9"}])

trigvalFVMuon(dqmitems,"HLT_Mu9: Et of RECO Muon Objects",
[{'path': "HLT/FourVector/paths/HLT_Mu9/HLT_Mu9_wrt__offEtOff", 'description':"Et of RECO Muon object for path HLT_Mu9"}])



###---- GENERIC - FourVector Electron
def trigvalFVEle(i, p, *rows): i["00 Shift/HLT/FourVector/Electron/" + p] = DQMItem(layout=rows)


trigvalFVEle(dqmitems,"Electron Eff HLT to L1",
[{'path': "HLT/FourVector/paths/HLT_Ele10_LW_L1R/custom-eff/HLT_Ele10_LW_L1R_wrt__l1Et_Eff_OnToL1", 'description':"Efficiency of HLT to L1 for path HLT_Ele10_LW_L1R"}])

trigvalFVEle(dqmitems,"Electron Eff HLT to RECO",
[{'path': "HLT/FourVector/paths/HLT_Ele10_LW_L1R/custom-eff/HLT_Ele10_LW_L1R_wrt__offEt_Eff_OnToOff", 'description':"Efficiency of HLT to RECO for path HLT_Ele10_LW_L1R"}])

trigvalFVEle(dqmitems,"HLT_Ele10_LW_L1R: Et of L1 Electron Objects",
     [{'path': "HLT/FourVector/paths/HLT_Ele10_LW_L1R/HLT_Ele10_LW_L1R_wrt__l1EtL1", 'description':"Et of L1 Electron object for path HLT_Ele10_LW_L1R"}])

trigvalFVEle(dqmitems,"HLT_Ele10_LW_L1R: Et of HLT Electron Objects",
[{'path': "HLT/FourVector/paths/HLT_Ele10_LW_L1R/HLT_Ele10_LW_L1R_wrt__onEtOn", 'description':"Et of HLT Electron object for path HLT_Ele10_LW_L1R"}])

trigvalFVEle(dqmitems,"HLT_Ele10_LW_L1R: Et of RECO Electron Objects",
[{'path': "HLT/FourVector/paths/HLT_Ele10_LW_L1R/HLT_Ele10_LW_L1R_wrt__offEtOff", 'description':"Et of RECO Electron object for path HLT_Ele10_LW_L1R"}])



###---- GENERIC - FourVector Jet
def trigvalFVJet(i, p, *rows): i["00 Shift/HLT/FourVector/Jet/" + p] = DQMItem(layout=rows)


trigvalFVJet(dqmitems,"Jet Eff HLT to L1",
[{'path': "HLT/FourVector/paths/HLT_Jet30U/custom-eff/HLT_Jet30U_wrt__l1Et_Eff_OnToL1", 'description':"Efficiency of HLT to L1 for path HLT_Jet30U"}])

trigvalFVJet(dqmitems,"Jet Eff HLT to RECO",
[{'path': "HLT/FourVector/paths/HLT_Jet30U/custom-eff/HLT_Jet30U_wrt__offEt_Eff_OnToOff", 'description':"Efficiency of HLT to RECO for path HLT_Jet30U"}])

trigvalFVJet(dqmitems,"HLT_Jet30U: Et of L1 Jet Objects",
[{'path': "HLT/FourVector/paths/HLT_Jet30U/HLT_Jet30U_wrt__l1EtL1", 'description':"Et of L1 Jet object for path HLT_Jet30U"}])

trigvalFVJet(dqmitems,"HLT_Jet30U: Et of HLT Jet Objects",
[{'path': "HLT/FourVector/paths/HLT_Jet30U/HLT_Jet30U_wrt__onEtOn", 'description':"Et of HLT Jet object for path HLT_Jet30U"}])

trigvalFVJet(dqmitems,"HLT_Jet30U: Et of RECO Jet Objects",
[{'path': "HLT/FourVector/paths/HLT_Jet30U/HLT_Jet30U_wrt__offEtOff", 'description':"Et of RECO Jet object for path HLT_Jet30U"}])

###---- GENERIC - FourVector Photon
def trigvalFVPho(i, p, *rows): i["00 Shift/HLT/FourVector/Photon/" + p] = DQMItem(layout=rows)


trigvalFVPho(dqmitems,"Photon Eff HLT to L1",
[{'path': "HLT/FourVector/paths/HLT_Photon15_L1R/custom-eff/HLT_Photon15_L1R_wrt__l1Et_Eff_OnToL1", 'description':"Efficiency of HLT to L1 for path HLT_Photon15_L1R"}])

trigvalFVPho(dqmitems,"Photon Eff HLT to RECO",
[{'path': "HLT/FourVector/paths/HLT_Photon15_L1R/custom-eff/HLT_Photon15_L1R_wrt__offEt_Eff_OnToOff", 'description':"Efficiency of HLT to RECO for path HLT_Photon15_L1R"}])

trigvalFVPho(dqmitems,"HLT_Photon15_L1R: Et of L1 Photon Objects",
[{'path': "HLT/FourVector/paths/HLT_Photon15_L1R/HLT_Photon15_L1R_wrt__l1EtL1", 'description':"Et of L1 Photon object for path HLT_Photon15_L1R"}])

trigvalFVPho(dqmitems,"HLT_Photon15_L1R: Et of HLT Photon Objects",
[{'path': "HLT/FourVector/paths/HLT_Photon15_L1R/HLT_Photon15_L1R_wrt__onEtOn", 'description':"Et of HLT Photon object for path HLT_Photon15_L1R"}])

trigvalFVPho(dqmitems,"HLT_Photon15_L1R: Et of RECO Photon objects",
[{'path': "HLT/FourVector/paths/HLT_Photon15_L1R/HLT_Photon15_L1R_wrt__offEtOff", 'description':"Et of RECO Photon object for path HLT_Photon15_L1R"}])

def hltCollLayout(i, p, *rows): i["00 Shift/HLT/Collisions/" + p] = DQMItem(layout=rows)

hltCollLayout(dqmitems,"Eff of HLT_Photon30_Cleaned_L1R L1 seed to RECO",
[{'path': "HLT/FourVector/paths/HLT_Photon30_Cleaned_L1R/custom-eff/HLT_Photon30_Cleaned_L1R_wrt__offEt_Eff_L1ToOff", 'description':"Efficiency of L1 seed to RECO for path HLT_Photon30_Cleaned_L1R. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineHLT\">here</a>."}])

hltCollLayout(dqmitems,"Eff of HLT_Photon30_Cleaned_L1R L1 seed wrt RECO in eta-phi RECO space",
[{'path': "HLT/FourVector/paths/HLT_Photon30_Cleaned_L1R/custom-eff/HLT_Photon30_Cleaned_L1R_wrt__offEtaoffPhi_Eff_L1ToOff", 'description':"Efficiency of L1 to RECO above 2 times HLT threshold for path HLT_Photon30_Cleaned_L1R (eta-phi).   For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineHLT\">here</a>."}])

hltCollLayout(dqmitems,"Eff of HLT_Photon30_Cleaned_L1R to RECO",
[{'path': "HLT/FourVector/paths/HLT_Photon30_Cleaned_L1R/custom-eff/HLT_Photon30_Cleaned_L1R_wrt__offEt_Eff_OnToOff", 'description':"Efficiency of HLT to RECO for path HLT_Photon30_Cleaned_L1R. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineHLT\">here</a>."}])


hltCollLayout(dqmitems,"Eff of HLT_Jet140U_v3 L1 seed to RECO",
[{'path': "HLT/FourVector/paths/HLT_Jet140U_v3/custom-eff/HLT_Jet140U_v3_wrt__offEt_Eff_L1ToOff", 'description':"Efficiency of L1 seed to RECO for path HLT_Jet140U_v3. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineHLT\">here</a>."}])

hltCollLayout(dqmitems,"Eff of HLT_Jet140U_v3 L1 seed wrt RECO in eta-phi RECO space",
[{'path': "HLT/FourVector/paths/HLT_Jet140U_v3/custom-eff/HLT_Jet140U_v3_wrt__offEtaoffPhi_Eff_L1ToOff", 'description':"Efficiency of L1 to RECO above 2 times HLT threshold for path HLT_Jet140U_v3 (eta-phi).   For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineHLT\">here</a>."}])

hltCollLayout(dqmitems,"Eff of HLT_Jet140U_v3 to RECO",
[{'path': "HLT/FourVector/paths/HLT_Jet140U_v3/custom-eff/HLT_Jet140U_v3_wrt__offEt_Eff_OnToOff", 'description':"Efficiency of HLT to RECO for path HLT_Jet140U_v3. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineHLT\">here</a>."}])


hltCollLayout(dqmitems,"Eff of HLT_Mu11 L1 seed to RECO",
[{'path': "HLT/FourVector/paths/HLT_Mu11/custom-eff/HLT_Mu11_wrt__offEt_Eff_L1ToOff", 'description':"Efficiency of L1 seed to RECO for path HLT_Mu11. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineHLT\">here</a>."}])

hltCollLayout(dqmitems,"Eff of HLT_Mu11 L1 seed wrt RECO in eta-phi RECO space",
[{'path': "HLT/FourVector/paths/HLT_Mu11/custom-eff/HLT_Mu11_wrt__offEtaoffPhi_Eff_L1ToOff", 'description':"Efficiency of L1 to RECO above 2 times HLT threshold for path HLT_Mu11 (eta-phi).   For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineHLT\">here</a>."}])

hltCollLayout(dqmitems,"Eff of HLT_Mu11 to RECO",
[{'path': "HLT/FourVector/paths/HLT_Mu11/custom-eff/HLT_Mu11_wrt__offEt_Eff_OnToOff", 'description':"Efficiency of HLT to RECO for path HLT_Mu11. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineHLT\">here</a>."}])


hltCollLayout(dqmitems,"Eff of HLT_Ele22_SW_TighterEleId_L1R_v2 L1 seed to RECO",
[{'path': "HLT/FourVector/paths/HLT_Ele22_SW_TighterEleId_L1R_v2/custom-eff/HLT_Ele22_SW_TighterEleId_L1R_v2_wrt__offEt_Eff_L1ToOff", 'description':"Efficiency of L1 seed to RECO for path HLT_Ele22_SW_TighterEleId_L1R_v2. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineHLT\">here</a>."}])

hltCollLayout(dqmitems,"Eff of HLT_Ele22_SW_TighterEleId_L1R_v2 L1 seed wrt RECO in eta-phi RECO space",
[{'path': "HLT/FourVector/paths/HLT_Ele22_SW_TighterEleId_L1R_v2/custom-eff/HLT_Ele22_SW_TighterEleId_L1R_v2_wrt__offEtaoffPhi_Eff_L1ToOff", 'description':"Efficiency of L1 to RECO above 2 times HLT threshold for path HLT_Ele22_SW_TighterEleId_L1R_v2 (eta-phi).   For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineHLT\">here</a>."}])

hltCollLayout(dqmitems,"Eff of HLT_Ele22_SW_TighterEleId_L1R_v2 to its RECO",
[{'path': "HLT/FourVector/paths/HLT_Ele22_SW_TighterEleId_L1R_v2/custom-eff/HLT_Ele22_SW_TighterEleId_L1R_v2_wrt__offEt_Eff_OnToOff", 'description':"Efficiency of HLT to RECO for path HLT_Ele22_SW_TighterEleId_L1R_v2. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineHLT\">here</a>."}])

def hltlayout(i, p, *rows): i["00 Shift/HLT/Cosmics/" + p] = DQMItem(layout=rows)

hltlayout(dqmitems,"N of HLT_L1MuOpen_NoBPTX muons" ,
  	[{'path': "HLT/FourVector/paths/HLT_L1MuOpen_NoBPTX/HLT_L1MuOpen_NoBPTX_wrt__NOn", 'description': "Multiplicity of HLT muons passing HLT_L1Mu path.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineHLT\">here</a>."}])

hltlayout(dqmitems,"RECO muons Et",
  	[{'path': "HLT/FourVector/paths/HLT_L1MuOpen_NoBPTX/HLT_L1MuOpen_NoBPTX_wrt__offEtOnOff", 'description': "Et of the RECO muons matched (eta-phi) with the triggering HLT_L1MuOpen_NoBPTX muons.   For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineHLT\">here</a>."}])

hltlayout(dqmitems,"RECO muons eta-phi",
  	[{'path': "HLT/FourVector/paths/HLT_L1MuOpen_NoBPTX/HLT_L1MuOpen_NoBPTX_wrt__offEtaoffPhiOff", 'description': "X=eta and Y=phi for RECO muons that are matched (eta-phi) with HLT muons triggering this path.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineHLT\">here</a>."}])

hltlayout(dqmitems,"HLT_L1MuOpen_NoBPTX & L1 muons eta-phi",
  	[{'path': "HLT/FourVector/paths/HLT_L1MuOpen_NoBPTX/HLT_L1MuOpen_NoBPTX_wrt__l1Etal1PhiL1On", 'description': "X=eta and Y=phi for L1 muons that are matched (eta-phi) with HLT muons triggering this path.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineHLT\">here</a>."}])

hltlayout(dqmitems,"Eff HLT_L1MuOpen_NoBPTX to its L1 vs Pt",
  	[{'path': "HLT/FourVector/paths/HLT_L1MuOpen_NoBPTX/custom-eff/HLT_L1MuOpen_NoBPTX_wrt__l1Et_Eff_OnToL1", 'description': "Fraction of L1 muons that triggered this HLT paht as function of Et.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineHLT\">here</a>."}])

hltlayout(dqmitems,"Eff HLT_L1MuOpen_NoBPTX to its L1 vs eta-phi",
  	[{'path': "HLT/FourVector/paths/HLT_L1MuOpen_NoBPTX/custom-eff/HLT_L1MuOpen_NoBPTX_wrt__l1Etal1Phi_Eff_OnToL1", 'description': "Fraction of L1 muons that triggered this HLT paht as function of eta-phi.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineHLT\">here</a>."}])

hltlayout(dqmitems,"Eff HLT_L2Mu9 to its L1 vs Pt",
  	[{'path': "HLT/FourVector/paths/HLT_L2Mu9/custom-eff/HLT_L2Mu9_wrt__l1Et_Eff_OnToL1", 'description': "Fraction of L1 muons that triggered this HLT paht as function of Et.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineHLT\">here</a>."}])

hltlayout(dqmitems,"Eff HLT_L2Mu9 to its L1 vs eta-phi",
  	[{'path': "HLT/FourVector/paths/HLT_L2Mu9/custom-eff/HLT_L2Mu9_wrt__l1Etal1Phi_Eff_OnToL1", 'description': "Fraction of L1 muons that triggered this HLT paht as function of eta-phi.  For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineHLT\">here</a>."}])

hltlayout(dqmitems,"Jet Eff HLT to L1",
[{'path': "HLT/FourVector/paths/HLT_Jet30U/custom-eff/HLT_Jet30U_wrt__l1Et_Eff_OnToL1", 'description':"Efficiency of HLT to L1 for path HLT_Jet30U"}])

hltlayout(dqmitems,"Jet Eff HLT to RECO",
[{'path': "HLT/FourVector/paths/HLT_Jet30U/custom-eff/HLT_Jet30U_wrt__l1Etal1Phi_Eff_OnToL1", 'description':"Efficiency of HLT to L1 for path HLT_Jet30U"}])





##########################################
#
#    TPG Layouts
#
##########################################



def tpgOfflineLayout(i, p, *rows): i["HLT/Layouts/TPG-Summary-HLTOffline/" + p] = DQMItem(layout=rows)


################  Muons ###########################

tpgOfflineLayout(dqmitems,"00 - HLT Muon Pt",
[{'path': "HLT/Muon/Distributions/HLT_Mu3/allMuons/recEffPt_L3Filtered", 'description':"HLT_Mu3 Pt"}])

tpgOfflineLayout(dqmitems,"01 - HLT Muon Eta vs Phi",
[{'path': "HLT/Muon/Distributions/HLT_Mu3/allMuons/recPhiVsRecEta_L3Filtered", 'description':"HLT_Mu3 EtaVsPhi"}])

tpgOfflineLayout(dqmitems,"02 - HLT Muon Passthru Pt",
[{'path': "HLT/Muon/Distributions/HLT_L1MuOpen/allMuons/recEffPt_L1Filtered", 'description':"HLT_L1MuOpen PT"}])

tpgOfflineLayout(dqmitems,"03 - HLT Muon Passthru Eta Phi ",
[{'path': "HLT/Muon/Distributions/HLT_L1MuOpen/allMuons/recPhiVsRecEta_L1Filtered", 'description':"HLT_L1MuOpen EtaVsPhi"}])


################ JETMET  ###########################


tpgOfflineLayout(dqmitems,"04 - HLT JetMet ",
[{'path': "HLT/JetMET/EffWrtMBTrigger/HLT_Jet30U/ME_Eff_Eta", 'description':""}])

tpgOfflineLayout(dqmitems,"05 - ",
[{'path': "HLT/JetMET/EffWrtMBTrigger/HLT_Jet30U/ME_Eff_Phi", 'description':""}])

tpgOfflineLayout(dqmitems,"06 - ",
[{'path': "HLT/JetMET/EffWrtMBTrigger/HLT_Jet30U/ME_Eff_Pt", 'description':""}])

tpgOfflineLayout(dqmitems,"07 - ",
[{'path': "HLT/JetMET/EffWrtMBTrigger/HLT_L1Jet6U/ME_Eff_Eta", 'description':""}])

tpgOfflineLayout(dqmitems,"08 - ",
[{'path': "HLT/JetMET/EffWrtMBTrigger/HLT_L1Jet6U/ME_Eff_Phi", 'description':""}])

tpgOfflineLayout(dqmitems,"09 - ",
[{'path': "HLT/JetMET/EffWrtMBTrigger/HLT_L1Jet6U/ME_Eff_Pt", 'description':""}])


################ ELECTRONS ###########################

tpgOfflineLayout(dqmitems,"10 - HLT Ele",
[{'path': "HLT/EgOffline/hltL1NonIsoHLTNonIsoSinglePhotonEt10HcalIsolFilter_trigEffTo_hltPreL1SingleEG5_pho_trigCuts_vs_et_eb", 'description':""}])

tpgOfflineLayout(dqmitems,"11 - HLT Ele",
[{'path': "HLT/EgOffline/hltL1NonIsoHLTNonIsoSinglePhotonEt10HcalIsolFilter_trigEffTo_hltPreL1SingleEG5_pho_trigCuts_vs_et_ee", 'description':""}])

tpgOfflineLayout(dqmitems,"12 - HLT Ele",
[{'path': "HLT/EgOffline/hltL1NonIsoHLTNonIsoSinglePhotonEt10HcalIsolFilter_trigEffTo_hltPreL1SingleEG5_pho_trigCuts_vs_eta_eb", 'description':""}])

tpgOfflineLayout(dqmitems,"13 - HLT Ele",
[{'path': "HLT/EgOffline/hltL1NonIsoHLTNonIsoSinglePhotonEt10HcalIsolFilter_trigEffTo_hltPreL1SingleEG5_pho_trigCuts_vs_eta_ee", 'description':""}])

tpgOfflineLayout(dqmitems,"14 - HLT Ele",
[{'path': "HLT/EgOffline/hltL1NonIsoHLTNonIsoSinglePhotonEt10HcalIsolFilter_trigEffTo_hltPreL1SingleEG5_pho_trigCuts_vs_phi_eb", 'description':""}])


tpgOfflineLayout(dqmitems,"15 - HLT Ele",
[{'path': "HLT/EgOffline/hltL1NonIsoHLTNonIsoSinglePhotonEt10HcalIsolFilter_trigEffTo_hltPreL1SingleEG5_pho_trigCuts_vs_phi_ee", 'description':""}])


tpgOfflineLayout(dqmitems,"16 - HLT Ele",
[{'path': "HLT/EgOffline/hltL1NonIsoHLTNonIsoSingleElectronLWEt10PixelMatchFilter_trigEffTo_hltL1NonIsoHLTNonIsoSinglePhotonEt10HcalIsolFilter_gsfEle_trigCuts_vs_et_eb", 'description':""}])

tpgOfflineLayout(dqmitems,"17 - HLT Ele",
[{'path': "HLT/EgOffline/hltL1NonIsoHLTNonIsoSingleElectronLWEt10PixelMatchFilter_trigEffTo_hltL1NonIsoHLTNonIsoSinglePhotonEt10HcalIsolFilter_gsfEle_trigCuts_vs_et_ee", 'description':""}])

tpgOfflineLayout(dqmitems,"18 - HLT Ele",
[{'path': "HLT/EgOffline/hltL1NonIsoHLTNonIsoSingleElectronLWEt10PixelMatchFilter_trigEffTo_hltL1NonIsoHLTNonIsoSinglePhotonEt10HcalIsolFilter_gsfEle_trigCuts_vs_eta_eb", 'description':""}])

tpgOfflineLayout(dqmitems,"19 - HLT Ele",
[{'path': "HLT/EgOffline/hltL1NonIsoHLTNonIsoSingleElectronLWEt10PixelMatchFilter_trigEffTo_hltL1NonIsoHLTNonIsoSinglePhotonEt10HcalIsolFilter_gsfEle_trigCuts_vs_eta_ee", 'description':""}])

tpgOfflineLayout(dqmitems,"20 - HLT Ele",
[{'path': "HLT/EgOffline/hltL1NonIsoHLTNonIsoSingleElectronLWEt10PixelMatchFilter_trigEffTo_hltL1NonIsoHLTNonIsoSinglePhotonEt10HcalIsolFilter_gsfEle_trigCuts_vs_phi_eb", 'description':""}])

tpgOfflineLayout(dqmitems,"21 - HLT Ele",
[{'path': "HLT/EgOffline/hltL1NonIsoHLTNonIsoSingleElectronLWEt10PixelMatchFilter_trigEffTo_hltL1NonIsoHLTNonIsoSinglePhotonEt10HcalIsolFilter_gsfEle_trigCuts_vs_phi_ee", 'description':""}])
