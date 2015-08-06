server.workspace('DQMQuality', 0, 'Summaries', 'Summary')
server.workspace('DQMSummary', 1, 'Summaries', 'Reports')
server.workspace('DQMShift',   2, 'Summaries', 'Shift')
server.workspace('DQMCertification', 3, 'Summaries', 'Certification')
server.workspace('DQMContent', 4, 'Summaries', 'Everything', '^', '^')

server.workspace('DQMContent', 10, 'Tracker/Muons', 'Pixel', '^Pixel/', '',
                 'Pixel/Layouts/00b - Pixel_Error_Summary',
                 'Pixel/Layouts/01 - Pixel_FEDOccupancy_Summary',
                 'Pixel/Layouts/02 - Pixel_Cluster_Summary',
                 'Pixel/Layouts/03 - Pixel_Track_Summary',
                 'Pixel/Layouts/05 - Barrel OnTrack cluster positions',
                 'Pixel/Layouts/06 - Endcap OnTrack cluster positions',
                 'Pixel/Layouts/07 - Pixel_Digi_Summary',)

server.workspace('DQMContent', 11, 'Tracker/Muons', 'SiStrip', '^SiStrip/', '',
                 'SiStrip/Layouts/00 - SiStrip ReportSummary',
                 'SiStrip/Layouts/01 - FED-Detected Errors Summary',
                 'SiStrip/Layouts/02 - FED-Detected Errors',
                 'SiStrip/Layouts/03 - # of Cluster Trend',
                 'SiStrip/Layouts/04 - OnTrackCluster (StoN)',
                                  'SiStrip/Layouts/05 - OffTrackCluster (Total Number)'
                 )

server.workspace('DQMContent', 12, 'Tracker/Muons', 'CSC', '^CSC/', '',
	         'CSC/Layouts/00 Data Integrity/Physics Efficiency 01',
		 'CSC/Layouts/00 Data Integrity/Physics Efficiency 02',
	         'CSC/Layouts/00 Data Integrity/Physics Efficiency 04 - CSCs Reporting Data and Unpacked',
		 'CSC/Layouts/00 Data Integrity/Physics Efficiency 08 - CSCs Occupancy Overal',
	         'CSC/Layouts/00 Data Integrity/Physics Efficiency 07 - CSCs Occupancy 2D',
	         'CSC/Layouts/00 Data Integrity/Physics Efficiency 09 - RecHits Minus',
		 'CSC/Layouts/00 Data Integrity/Physics Efficiency 10 - RecHits Plus'
	         )

server.workspace('DQMContent', 13, 'Tracker/Muons', 'DT', '^DT/', '')
server.workspace('DQMContent', 14, 'Tracker/Muons', 'RPC', '^RPC/', '')

server.workspace('DQMContent', 21, 'Calorimeter', 'Ecal', '^Ecal(|Barrel|Endcap)/', 'Ecal/Layouts',
                 'Ecal/Layouts/00 Summary',
                 'Ecal/Layouts/01 Occupancy Summary')

server.workspace('DQMContent', 22, 'Calorimeter', 'EcalPreshower', '^EcalPreshower/', '',
                'EcalPreshower/Layouts/01-IntegritySummary-EcalPreshower',
                'EcalPreshower/Layouts/02-OccupancySummary-EcalPreshower',
                'EcalPreshower/Layouts/03-GoodRechitEnergySummary-EcalPreshower',
                'EcalPreshower/Layouts/04-RechitEnergySummary-EcalPreshower',
                'EcalPreshower/Layouts/05-ESTimingTaskSummary-EcalPreshower')

server.workspace('DQMContent', 23, 'Calorimeter', 'HCAL', '^Hcal/', '',
                 'Hcal/Layouts/01 HCAL Summaries',
                 'Hcal/Layouts/02 HCAL Events Processed',
                 'Hcal/Layouts/03 HCAL Sufficient Events',
                 'Hcal/Layouts/04 HCAL Raw Data',
                 'Hcal/Layouts/05 HCAL Digi Problems',
                 'Hcal/Layouts/06 HCAL Dead Cell Check',
                 'Hcal/Layouts/07 HCAL Hot Cell Check'
                 )

server.workspace('DQMContent', 20, 'Calorimeter', 'CASTOR', '^Castor/', '',
                 'Castor/Layouts/CASTOR Channel Status',
                 'Castor/Layouts/CASTOR RecHit Energies',
		 'Castor/Layouts/CASTOR RecHit Energy in modules',
		 'Castor/Layouts/CASTOR RecHit Energy in sectors',
		 'Castor/Layouts/CASTOR RecHitEnergy 2D Map',
                 'Castor/Layouts/CASTOR All Digi Values',
                 'Castor/Layouts/CASTOR average pulse in bunch crossings',
                 'Castor/Layouts/CASTOR hits 3D- cumulative',
                 'Castor/Layouts/CASTOR hits 3D- event with the largest deposited E'
                )

server.workspace('DQMContent', 31, 'Trigger/Lumi', 'L1T', '^L1T/', '')
server.workspace('DQMContent', 32, 'Trigger/Lumi', 'L1TEMU', '^L1TEMU/', '')
server.workspace('DQMContent', 33, 'Trigger/Lumi', 'HLT', '^HLT/', '')
server.workspace('DQMContent', 34, 'Trigger/Lumi', 'HLX', '^HLX', '')

server.workspace('DQMContent', 41, 'POG', 'Muons', '^Muons/', '')
server.workspace('DQMContent', 42, 'POG', 'JetMet', '^JetMET/', '')
server.workspace('DQMContent', 43, 'POG', 'EGamma', '^Egamma/', '')
server.workspace('DQMContent', 44, 'POG', 'Btag', '^Btag/', '',
                 'Btag/Layouts/00 - Jet Property',
                 'Btag/Layouts/01 - Tracks in Jet',
                 'Btag/Layouts/02 - Vertex Property',
                 'Btag/Layouts/03 - Flight Distance Summary',
                 'Btag/Layouts/04 - Discriminator Summary',
                 'Btag/Layouts/05 - 2D-Impact Parameter',
                 'Btag/Layouts/06 - 3D-Impact Parameter'
)

server.workspace('DQMContent', 45, 'POG', 'Tracking', '^(Tracking|AlcaBeamMonitor|OfflinePV)/', '',
                                  'Tracking/Layouts/01 - Tracking ReportSummary',
                                  'Tracking/Layouts/02 - Tracks (pp collisions)',
                 'Tracking/Layouts/03 - Tracks (Cosmic Tracking)',
                 'Tracking/Layouts/05 - Number of Seeds (pp collisions)'
                                  )

server.workspace('DQMContent', 46, 'POG', 'Tau', '^RecoTauV/', '',
        "RecoTauV/Layouts/SingleMu/00aa - Fake rate from muons vs pt",
        "RecoTauV/Layouts/SingleMu/00ab - Fake rate from muons vs pt",
        "RecoTauV/Layouts/SingleMu/01a - Muon rejection fake rate vs pt",
        "RecoTauV/Layouts/SingleMu/02aa - Fake rate from jets vs pt",
        "RecoTauV/Layouts/SingleMu/02ab - Fake rate from jets vs pt",
        "RecoTauV/Layouts/Jet/00aa - Fake rate from jets vs pt",
        "RecoTauV/Layouts/Jet/00ab - Fake rate from jets vs pt",
        "RecoTauV/Layouts/DoubleElectron_OR_TauPlusX/00aa - Fake rate from electrons vs pt",
        "RecoTauV/Layouts/DoubleElectron_OR_TauPlusX/00ab - Fake rate from electrons vs pt",
        "RecoTauV/Layouts/DoubleElectron_OR_TauPlusX/01a - Electron rejection fake rate vs pt",
        "RecoTauV/Layouts/SingleMu/00ba - Fake rate from muons vs pileup",
        "RecoTauV/Layouts/SingleMu/00bb - Fake rate from muons vs pileup",
        "RecoTauV/Layouts/SingleMu/02ba - Fake rate from jets vs pileup",
        "RecoTauV/Layouts/SingleMu/02bb - Fake rate from jets vs pileup",
        "RecoTauV/Layouts/Jet/00ba - Fake rate from jets vs pileup",
        "RecoTauV/Layouts/Jet/00bb - Fake rate from jets vs pileup",
        "RecoTauV/Layouts/DoubleElectron_OR_TauPlusX/00ba - Fake rate from electrons vs pileup",
        "RecoTauV/Layouts/DoubleElectron_OR_TauPlusX/00bb - Fake rate from electrons vs pileup",
    )

server.workspace('DQMContent', 51,'FeedBack for Collisions', 'Tracking FeedBack', '^(Collisions|SiStrip|Tracking|Pixel|AlcaBeamMonitor|OfflinePV)/', 'Collisions/TrackingFeedBack',
                 'Collisions/TrackingFeedBack/00 - Number Of Tracks',
                 'Collisions/TrackingFeedBack/01 - Track Pt',
                 'Collisions/TrackingFeedBack/02 - Track Phi',
                 'Collisions/TrackingFeedBack/03 - Track Eta',
                 'Collisions/TrackingFeedBack/04 - X-Position Of Closest Approach',
                 'Collisions/TrackingFeedBack/05 - Y-Position Of Closest Approach',
                 'Collisions/TrackingFeedBack/06 - Z-Position Of Closest Approach',
                 'Collisions/TrackingFeedBack/07 - Cluster y width vs. cluster eta'
)
server.workspace('DQMContent', 52,'FeedBack for Collisions', 'Ecal FeedBack', '^(Collisions|Ecal[^/]*)/', 'Collisions/EcalFeedBack',
                 "Collisions/EcalFeedBack/00 Single Event Timing EB",
                 "Collisions/EcalFeedBack/01 Single Event Timing EE",
                 "Collisions/EcalFeedBack/02 Timing Map EB",
                 "Collisions/EcalFeedBack/03 Timing Map EE -",
                 "Collisions/EcalFeedBack/04 Timing Map EE +",
                 "Collisions/EcalFeedBack/05 Timing ES",
                 "Collisions/EcalFeedBack/06 Occupancy EB",
                 "Collisions/EcalFeedBack/07 Occupancy EE -",
                 "Collisions/EcalFeedBack/08 Occupancy EE +",
                 "Collisions/EcalFeedBack/09 Occupancy ES",
                 "Collisions/EcalFeedBack/10 RecHit Energy EB",
                 "Collisions/EcalFeedBack/11 RecHit Energy EE",
                 "Collisions/EcalFeedBack/12 RecHit Energy ES"
                 )
server.workspace('DQMContent', 53,'FeedBack for Collisions', 'Hcal FeedBack', '^(Collisions|Hcal)/', 'Collisions/HcalFeedBack',
                 "Collisions/HcalFeedBack/01 - HF+,HF- coincidences (with BPTX)",
                 "Collisions/HcalFeedBack/02 - HF+,HF- coincidences (without BPTX)",
                 "Collisions/HcalFeedBack/03 - Digi Shapes for Total Digi Signals > N counts",
                 "Collisions/HcalFeedBack/04 - Lumi Bunch Crossing Checks",
                 "Collisions/HcalFeedBack/05 - Events Per Lumi Section",
                 "Collisions/HcalFeedBack/06 - Lumi Distributions",
                 )

server.workspace('DQMContent', 54,'FeedBack for Collisions', 'L1T FeedBack','^(Collisions|L1T)/', 'Collisions/L1TFeedBack',
                "Collisions/L1TFeedBack/00 Rate BSCL.BSCR",
                "Collisions/L1TFeedBack/01 Rate BSC splash right",
                "Collisions/L1TFeedBack/02 Rate BSC splash left",
                "Collisions/L1TFeedBack/03 Integ BSCL*BSCR Triggers vs LS",
                "Collisions/L1TFeedBack/04 Integ BSCL or BSCR Triggers vs LS",
                "Collisions/L1TFeedBack/05 Integ HF Triggers vs LS"
                )

server.workspace('DQMContent', 55,'FeedBack for Collisions', 'HLT FeedBack','^(Collisions|HLT)/', 'Collisions/HLTFeedBack',
                "Collisions/HLTFeedBack/00 HLT_Egamma_Pass_Any",
                "Collisions/HLTFeedBack/01 HLT_JetMet_Pass_Any",
                "Collisions/HLTFeedBack/02 HLT_Muon_Pass_Any",
                "Collisions/HLTFeedBack/03 HLT_Rest_Pass_Any",
                "Collisions/HLTFeedBack/04 HLT_Special_Pass_Any"
                )

server.workspace('DQMContent', 56, 'FeedBack for Collisions', 'CSC FeedBack', '^(Collisions|CSC)/', '',
                'CSC/Layouts/04 Timing/00 ALCT Timing',
                'CSC/Layouts/04 Timing/01 CLCT Timing'
                )
