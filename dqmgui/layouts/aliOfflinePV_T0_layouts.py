def aliOfflinePVLayout(i, p, *rows): i["OfflinePV/AlignmentValidation/" + p] = DQMItem(layout=rows) 

aliOfflinePVLayout(dqmitems, "00 - Vertex and vertex tracks quality",
                   [{ 'path': "OfflinePV/Alignment/chi2ndf",
                      'description': "Chi square of vertex tracks (pT>1GeV)",
                      'draw': { 'withref': "no" }
                      },
                    { 'path': "OfflinePV/Alignment/chi2prob",
                      'description': "Chi square probability of vertex tracks (pT>1GeV)",
                      'draw': { 'withref': "no" }
                      }],
                   [{ 'path': "OfflinePV/Alignment/sumpt",
                      'description': "sum of transverse momentum squared of vertex tracks (pT>1GeV)",
                      'draw': { 'withref': "no" }
                      },
                    { 'path': "OfflinePV/Alignment/weight",
                      'description': "weight of track in vertex fit",
                      'draw': { 'withref': "no" }
                      }],
                   [{ 'path': "OfflinePV/Alignment/ntracks",
                      'description': "number of tracks in vertex",
                      'draw': { 'withref': "no" }
                      },
                    { 'path': "OfflinePV/Alignment/dxyzoom",
                      'description': "transverse impact parameter",
                      'draw': { 'withref': "no" }
                      }])

aliOfflinePVLayout(dqmitems, "01 - Impact parameters and errors",
                   [{ 'path': "OfflinePV/Alignment/dxy_pt1",
                      'description': "transverse impact parameter w.r.t vertex",
                      'draw': { 'withref': "no" }
                      },
                    { 'path': "OfflinePV/Alignment/dxyErr_pt1",
                      'description': "error on transverse impact parameter w.r.t vertex",
                      'draw': { 'withref': "no" }
                      }],
                   [{ 'path': "OfflinePV/Alignment/dz_pt1",
                      'description': "longitudinal impact parameter w.r.t vertex",
                      'draw': { 'withref': "no" }
                      },
                    { 'path': "OfflinePV/Alignment/dzErr_pt1",
                      'description': "error on longitudinal impact parameter w.r.t vertex",
                      'draw': { 'withref': "no" }
                      }])

aliOfflinePVLayout(dqmitems, "02 - Impact parameters projections (pT>1 GeV)",
                   [{ 'path': "OfflinePV/Alignment/dxyVsPhi_pt1",
                      'description': "transverse impact parameter vs track azimuth (track momentum > 1 GeV)",
                      'draw': { 'withref': "no" }
                      },
                    { 'path': "OfflinePV/Alignment/dxyVsEta_pt1",
                      'description': "transverse impact parameter vs track pseudorapitidy (track momentum > 1 GeV)",
                      'draw': { 'withref': "no" }
                      }],
                   [{ 'path': "OfflinePV/Alignment/dzVsPhi_pt1",
                      'description': "longitudinal impact parameter vs track azimuth (track momentum > 1 GeV)",
                      'draw': { 'withref': "no" }
                      },
                    { 'path': "OfflinePV/Alignment/dzVsEta_pt1",
                      'description': "longidutinal impact parameter vs track pseudorapidity (track momentum > 1 GeV)",
                      'draw': { 'withref': "no" }
                      }])

aliOfflinePVLayout(dqmitems, "03 - Impact parameters projections (pT>10 GeV)",
                   [{ 'path': "OfflinePV/Alignment/dxyVsPhi_pt10",
                      'description': "transverse impact parameter vs track azimuth (track momentum > 10 GeV)",
                      'draw': { 'withref': "no" }
                      },
                    { 'path': "OfflinePV/Alignment/dxyVsEta_pt10",
                      'description': "transverse impact parameter vs track pseudorapitidy (track momentum > 10 GeV)",
                      'draw': { 'withref': "no" }
                      }],
                   [{ 'path': "OfflinePV/Alignment/dzVsPhi_pt10",
                      'description': "longitudinal impact parameter vs track azimuth (track momentum > 10 GeV)",
                      'draw': { 'withref': "no" }
                      },
                    { 'path': "OfflinePV/Alignment/dzVsEta_pt10",
                      'description': "longidutinal impact parameter vs track pseudorapidity (track momentum > 10 GeV)",
                      'draw': { 'withref': "no" }
                      }])

aliOfflinePVLayout(dqmitems, "04 - 2D impact parameters projections",
                   [{ 'path': "OfflinePV/Alignment/dxyVsEtaVsPhi_pt1",
                      'description': "transverse impact parameter vs track pseudorapitidy vs track azimuth (track momentum > 1 GeV)",
                      'draw': { 'withref': "no" }
                      },
                    { 'path': "OfflinePV/Alignment/dxyVsEtaVsPhi_pt10",
                      'description': "transverse impact parameter vs track pseudorapitidy vs track azimuth (track momentum > 10 GeV)",
                      'draw': { 'withref': "no" }
                      }],
                   [{ 'path': "OfflinePV/Alignment/dzVsEtaVsPhi_pt1",
                      'description': "longidutinal impact parameter vs track pseudorapitidy vs track azimuth (track momentum > 1 GeV)",
                      'draw': { 'withref': "no" }
                      },
                    { 'path': "OfflinePV/Alignment/dzVsEtaVsPhi_pt10",
                      'description': "longidutinal impact parameter vs track pseudorapitidy vs track azimuth (track momentum > 10 GeV)",
                      'draw': { 'withref': "no" }
                      }])

aliOfflinePVLayout(dqmitems, "05 - Impact parameters error projections (pT>1 GeV)",
                   [{ 'path': "OfflinePV/Alignment/dxyErrVsPhi_pt1",
                      'description': "transverse impact parameter error vs track azimuth (track momentum > 1 GeV)",
                      'draw': { 'withref': "no" }
                      },
                    { 'path': "OfflinePV/Alignment/dxyErrVsEta_pt1",
                      'description': "transverse impact parameter error vs track pseudorapitidy (track momentum > 1 GeV)",
                      'draw': { 'withref': "no" }
                      }],
                   [{ 'path': "OfflinePV/Alignment/dzErrVsPhi_pt1",
                      'description': "longitudinal impact parameter error vs track azimuth (track momentum > 1 GeV)",
                      'draw': { 'withref': "no" }
                      },
                    { 'path': "OfflinePV/Alignment/dzErrVsEta_pt1",
                      'description': "longidutinal impact parameter error vs track pseudorapidity (track momentum > 1 GeV)",
                      'draw': { 'withref': "no" }
                      }])

aliOfflinePVLayout(dqmitems, "06 - Impact parameters error projections (pT>10 GeV)",
                   [{ 'path': "OfflinePV/Alignment/dxyErrVsPhi_pt10",
                      'description': "transverse impact parameter error vs track azimuth (track momentum > 10 GeV)",
                      'draw': { 'withref': "no" }
                      },
                    { 'path': "OfflinePV/Alignment/dxyErrVsEta_pt10",
                      'description': "transverse impact parameter error vs track pseudorapitidy (track momentum > 10 GeV)",
                      'draw': { 'withref': "no" }
                      }],
                   [{ 'path': "OfflinePV/Alignment/dzErrVsPhi_pt10",
                      'description': "longitudinal impact parameter error vs track azimuth (track momentum > 10 GeV)",
                      'draw': { 'withref': "no" }
                      },
                    { 'path': "OfflinePV/Alignment/dzErrVsEta_pt10",
                      'description': "longidutinal impact parameter error vs track pseudorapidity (track momentum > 10 GeV)",
                      'draw': { 'withref': "no" }
                      }])

aliOfflinePVLayout(dqmitems, "07 - 2D impact parameters error projections",
                   [{ 'path': "OfflinePV/Alignment/dxyErrVsEtaVsPhi_pt1",
                      'description': "transverse impact parameter error vs track pseudorapitidy vs track azimuth (track momentum > 1 GeV)",
                      'draw': { 'withref': "no" }
                      },
                    { 'path': "OfflinePV/Alignment/dxyErrVsEtaVsPhi_pt10",
                      'description': "transverse impact parameter error vs track pseudorapitidy vs track azimuth (track momentum > 10 GeV)",
                      'draw': { 'withref': "no" }
                      }],
                   [{ 'path': "OfflinePV/Alignment/dzErrVsEtaVsPhi_pt1",
                      'description': "longidutinal impact parameter error vs track pseudorapitidy vs track azimuth (track momentum > 1 GeV)",
                      'draw': { 'withref': "no" }
                      },
                    { 'path': "OfflinePV/Alignment/dzErrVsEtaVsPhi_pt10",
                      'description': "longidutinal impact parameter error vs track pseudorapitidy vs track azimuth (track momentum > 10 GeV)",
                      'draw': { 'withref': "no" }
                      }])



