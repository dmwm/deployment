

###---- GENERIC - FourVector selection goes here: ####
######################################################

###---- GENERIC - FourVector Muon
def trigHltMuonOfflineSummary(i, p, *rows):
   i["HLT/Muon/MuonHLTSummary/" + p] = DQMItem(layout=rows)


######################################################

trigHltMuonOfflineSummary(dqmitems,"01 - HLT_Mu3",
   [{'path': "HLT/Muon/Distributions/HLT_Mu3/allMuons/recEffPt_L3Filtered", 'description':"Efficiency for RECO muons to match HLT"}],
   [{'path': "HLT/Muon/Distributions/HLT_Mu3/allMuons/recEffPhiVsEta_L3Filtered", 'description':"Efficiency for RECO muons to match HLT"}])

######################################################

trigHltMuonOfflineSummary(dqmitems,"02 - HLT_Mu5",
   [{'path': "HLT/Muon/Distributions/HLT_Mu5/allMuons/recEffPt_L3Filtered", 'description':"Efficiency for RECO muons to match HLT"}],
   [{'path': "HLT/Muon/Distributions/HLT_Mu5/allMuons/recEffPhiVsEta_L3Filtered", 'description':"Efficiency for RECO muons to match HLT"}])

######################################################

trigHltMuonOfflineSummary(dqmitems,"03 - HLT_Mu9",
   [{'path': "HLT/Muon/Distributions/HLT_Mu9/allMuons/recEffPt_L3Filtered", 'description':"Efficiency for RECO muons to match HLT"}],
   [{'path': "HLT/Muon/Distributions/HLT_Mu9/allMuons/recEffPhiVsEta_L3Filtered", 'description':"Efficiency for RECO muons to match HLT"}])

######################################################

trigHltMuonOfflineSummary(dqmitems,"04 - HLT_Mu11",
   [{'path': "HLT/Muon/Distributions/HLT_Mu11/allMuons/recEffPt_L3Filtered", 'description':"Efficiency for RECO muons to match HLT"}],
   [{'path': "HLT/Muon/Distributions/HLT_Mu11/allMuons/recEffPhiVsEta_L3Filtered", 'description':"Efficiency for RECO muons to match HLT"}])

######################################################

trigHltMuonOfflineSummary(dqmitems,"05 - HLT_L2Mu9",
   [{'path': "HLT/Muon/Distributions/HLT_L2Mu9/allMuons/recEffPt_L2Filtered", 'description':"Efficiency for RECO muons to match HLT"}],
   [{'path': "HLT/Muon/Distributions/HLT_L2Mu9/allMuons/recEffPhiVsEta_L2Filtered", 'description':"Efficiency for RECO muons to match HLT"}])

######################################################

trigHltMuonOfflineSummary(dqmitems,"06 - HLT_L2Mu11",
   [{'path': "HLT/Muon/Distributions/HLT_L2Mu11/allMuons/recEffPt_L2Filtered", 'description':"Efficiency for RECO muons to match HLT"}],
   [{'path': "HLT/Muon/Distributions/HLT_L2Mu11/allMuons/recEffPhiVsEta_L2Filtered", 'description':"Efficiency for RECO muons to match HLT"}])

