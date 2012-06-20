def shiftegammalayout(i, p, *rows): i["00 Shift/Egamma/" + p] = DQMItem(layout=rows)

shiftegammalayout(dqmitems, "1-Good Photon Candidates: Et Spectra",
  [{'path': "Egamma/PhotonAnalyzer/GoodCandidatePhotons/Et above 20 GeV/h_02_phoEtBarrel",
	'description': "Transverse energy of good candidate photons in ECAL barrel - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineEgamma>Shift Instructions</a>" }],
  [{'path': "Egamma/PhotonAnalyzer/GoodCandidatePhotons/Et above 20 GeV/h_02_phoEtEndcaps",
	'description': "Transverse energy of good candidate photons in ECAL endcaps - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineEgamma>Shift Instructions</a>" }])

shiftegammalayout(dqmitems, "2-Good Photon Candidates: R9",
  [{'path': "Egamma/PhotonAnalyzer/GoodCandidatePhotons/Et above 20 GeV/h_08_r9Barrel",
	'description': "R9 parameter for good candidate photons in ECAL barrel - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineEgamma>Shift Instructions</a>" }],
  [{'path': "Egamma/PhotonAnalyzer/GoodCandidatePhotons/Et above 20 GeV/h_08_r9Endcaps",
	'description': "R9 paramater for good candidate photons in ECAL endcaps - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineEgamma>Shift Instructions</a>"}])

shiftegammalayout(dqmitems, "3-Good Photon Candidates: SigmaIetaIeta",
  [{'path': "Egamma/PhotonAnalyzer/GoodCandidatePhotons/Et above 20 GeV/h_13_phoSigmaIetaIetaBarrel",
	'description': "SigmaIetaIeta parameter for good candidate photons in ECAL barrel - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineEgamma>Shift Instructions</a>" }],
  [{'path': "Egamma/PhotonAnalyzer/GoodCandidatePhotons/Et above 20 GeV/h_13_phoSigmaIetaIetaEndcaps",
	'description': "SigmaIetaIeta paramater for good candidate photons in ECAL endcaps - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineEgamma>Shift Instructions</a>"}])

shiftegammalayout(dqmitems, "4-PiZeros",
  [{'path': "Egamma/PiZeroAnalyzer/Pi0InvmassEB",
	'description': "Reconstructed mass of the PiZero particle - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineEgamma>Shift Instructions</a>" }])

shiftegammalayout(dqmitems, "5-Good Photon Candidates: ECAL Isolation Sum",
  [{'path': "Egamma/PhotonAnalyzer/GoodCandidatePhotons/Et above 20 GeV/h_56_ecalSum",
	'description': "Ecal sum in iso cone - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineEgamma>Shift Instructions</a>" }])

shiftegammalayout(dqmitems, "6-Good Photon Candidates: HCAL Isolation Sum",
  [{'path': "Egamma/PhotonAnalyzer/GoodCandidatePhotons/Et above 20 GeV/h_61_hcalSum",
	'description': "Hcal sum in iso cone - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineEgamma>Shift Instructions</a>" }])

shiftegammalayout(dqmitems, "7-Good Photon Candidates: Eta distribution",
  [{'path': "Egamma/PhotonAnalyzer/GoodCandidatePhotons/Et above 20 GeV/h_04_phoEta",
	'description': "Eta Distribution - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineEgamma>Shift Instructions</a>" }])

shiftegammalayout(dqmitems, "8-Good Photon Candidates: H Over E",
  [{'path': "Egamma/PhotonAnalyzer/GoodCandidatePhotons/Et above 20 GeV/h_66_hOverEBarrel",
	'description': "H over E for good candidate photons in ECAL barrel - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineEgamma>Shift Instructions</a>" }],
  [{'path': "Egamma/PhotonAnalyzer/GoodCandidatePhotons/Et above 20 GeV/h_66_hOverEEndcaps",
	'description': "H over E for good candidate photons in ECAL endcaps - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineEgamma>Shift Instructions</a>"}])

shiftegammalayout(dqmitems, "9-Good Photon Candidates: invMass",
  [{'path': "Egamma/PhotonAnalyzer/InvMass/h_01_invMassAllIsolatedPhotons",
	'description': "Invariant mass of all photons - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineEgamma>Shift Instructions</a>"}])
