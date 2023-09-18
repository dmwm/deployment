def alignmentvalidationlayout(i, p, *rows): i["DataLayouts/TkAli/" + p] = DQMItem(layout=rows)

alignmentvalidationlayout(dqmitems, "00 - Vertex and vertex tracks quality",
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

alignmentvalidationlayout(dqmitems, "01 - Impact parameters and errors",
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

alignmentvalidationlayout(dqmitems, "02 - Impact parameters projections (pT>1 GeV)",
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

alignmentvalidationlayout(dqmitems, "03 - Impact parameters projections (pT>10 GeV)",
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

alignmentvalidationlayout(dqmitems, "04 - 2D impact parameters projections",
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
                      
alignmentvalidationlayout(dqmitems, "05 - Impact parameters error projections (pT>1 GeV)",
                   [{ 'path': "OfflinePV/Alignment/dxyErrVsPhi_pt1",
                      'description': "transverse impact parameter vs track azimuth (track momentum > 1 GeV)",
                      'draw': { 'withref': "no" }
                      },
                    { 'path': "OfflinePV/Alignment/dxyErrVsEta_pt1",
                      'description': "transverse impact parameter vs track pseudorapitidy (track momentum > 1 GeV)",
                      'draw': { 'withref': "no" }
                      }],
                   [{ 'path': "OfflinePV/Alignment/dzErrVsPhi_pt1",
                      'description': "longitudinal impact parameter vs track azimuth (track momentum > 1 GeV)",
                      'draw': { 'withref': "no" }
                      },
                    { 'path': "OfflinePV/Alignment/dzErrVsEta_pt1",
                      'description': "longidutinal impact parameter vs track pseudorapidity (track momentum > 1 GeV)",
                      'draw': { 'withref': "no" }
                      }])

alignmentvalidationlayout(dqmitems, "06 - Impact parameters error projections (pT>10 GeV)",
                   [{ 'path': "OfflinePV/Alignment/dxyErrVsPhi_pt10",
                      'description': "transverse impact parameter vs track azimuth (track momentum > 10 GeV)",
                      'draw': { 'withref': "no" }
                      },
                    { 'path': "OfflinePV/Alignment/dxyErrVsEta_pt10",
                      'description': "transverse impact parameter vs track pseudorapitidy (track momentum > 10 GeV)",
                      'draw': { 'withref': "no" }
                      }],
                   [{ 'path': "OfflinePV/Alignment/dzErrVsPhi_pt10",
                      'description': "longitudinal impact parameter vs track azimuth (track momentum > 10 GeV)",
                      'draw': { 'withref': "no" }
                      },
                    { 'path': "OfflinePV/Alignment/dzErrVsEta_pt10",
                      'description': "longidutinal impact parameter vs track pseudorapidity (track momentum > 10 GeV)",
                      'draw': { 'withref': "no" }
                      }])

alignmentvalidationlayout(dqmitems, "07 - 2D impact parameters error projections",
                   [{ 'path': "OfflinePV/Alignment/dxyErrVsEtaVsPhi_pt1",
                      'description': "transverse impact parameter vs track pseudorapitidy vs track azimuth (track momentum > 1 GeV)",
                      'draw': { 'withref': "no" }
                      },
                    { 'path': "OfflinePV/Alignment/dxyErrVsEtaVsPhi_pt10",
                      'description': "transverse impact parameter vs track pseudorapitidy vs track azimuth (track momentum > 10 GeV)",
                      'draw': { 'withref': "no" }
                      }],
                   [{ 'path': "OfflinePV/Alignment/dzErrVsEtaVsPhi_pt1",
                      'description': "longidutinal impact parameter vs track pseudorapitidy vs track azimuth (track momentum > 1 GeV)",
                      'draw': { 'withref': "no" }
                      },
                    { 'path': "OfflinePV/Alignment/dzErrVsEtaVsPhi_pt10",
                      'description': "longidutinal impact parameter vs track pseudorapitidy vs track azimuth (track momentum > 10 GeV)",
                      'draw': { 'withref': "no" }
                      }])

alignmentvalidationlayout(dqmitems, "38 - PixelPhase1 Residuals",
   [{ 'path': "PixelPhase1/Tracks/residual_x_PXBarrel",
      'description': "Track residuals x in PXBarrel",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Tracks/residual_x_PXForward",
      'description': "Track residuals x in PXForward",
      'draw': { 'withref': "no" }}],
   [{ 'path': "PixelPhase1/Tracks/residual_y_PXBarrel",
      'description': "Track residuals y in PXBarrel",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Tracks/residual_y_PXForward",
      'description': "Track residuals y in PXForward",
      'draw': { 'withref': "no" }}]
   )

alignmentvalidationlayout(dqmitems, "38aa - Residuals x per Layer",
   [{ 'path': "PixelPhase1/Tracks/PXBarrel/residual_x_PXLayer_1",
      'description': "Track residuals x in PXBarrel Layer 1",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Tracks/PXBarrel/residual_x_PXLayer_2",
      'description': "Track residuals x in PXBarrel Layer 2",
      'draw': { 'withref': "no" }},],
   [{ 'path': "PixelPhase1/Tracks/PXBarrel/residual_x_PXLayer_3",
      'description': "Track residuals x in PXBarrel Layer 3",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Tracks/PXBarrel/residual_x_PXLayer_4",
      'description': "Track residuals x in PXBarrel Layer 4",
      'draw': { 'withref': "no" }},]
   )

alignmentvalidationlayout(dqmitems, "38ab - Residuals y per Layer",
   [{ 'path': "PixelPhase1/Tracks/PXBarrel/residual_y_PXLayer_1",
      'description': "Track residuals y in PXBarrel Layer 1",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Tracks/PXBarrel/residual_y_PXLayer_2",
      'description': "Track residuals y in PXBarrel Layer 2",
      'draw': { 'withref': "no" }},],
   [{ 'path': "PixelPhase1/Tracks/PXBarrel/residual_y_PXLayer_3",
      'description': "Track residuals y in PXBarrel Layer 3",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Tracks/PXBarrel/residual_y_PXLayer_4",
      'description': "Track residuals y in PXBarrel Layer 4",
      'draw': { 'withref': "no" }},]
   )

alignmentvalidationlayout(dqmitems, "38ba - Profile Residuals x PXBarrel",
   [{ 'path': "PixelPhase1/Tracks/PXBarrel/residual_x_per_SignedModule_per_SignedLadder_PXLayer_1",
      'description': "Mean track residuals x in PXBarrel Layer 1",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Tracks/PXBarrel/residual_x_per_SignedModule_per_SignedLadder_PXLayer_2",
      'description': "Mean track residuals x in PXBarrel Layer 2",
      'draw': { 'withref': "no" }},],
   [{ 'path': "PixelPhase1/Tracks/PXBarrel/residual_x_per_SignedModule_per_SignedLadder_PXLayer_3",
      'description': "Mean track residuals x in PXBarrel Layer 3",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Tracks/PXBarrel/residual_x_per_SignedModule_per_SignedLadder_PXLayer_4",
      'description': "Mean track residuals x in PXBarrel Layer 4",
      'draw': { 'withref': "no" }},]
   )

alignmentvalidationlayout(dqmitems, "38bb - Profile Residuals y PXBarrel",
   [{ 'path': "PixelPhase1/Tracks/PXBarrel/residual_y_per_SignedModule_per_SignedLadder_PXLayer_1",
      'description': "Mean track residuals y in PXBarrel Layer 1",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Tracks/PXBarrel/residual_y_per_SignedModule_per_SignedLadder_PXLayer_2",
      'description': "Mean track residuals y in PXBarrel Layer 2",
      'draw': { 'withref': "no" }},],
   [{ 'path': "PixelPhase1/Tracks/PXBarrel/residual_y_per_SignedModule_per_SignedLadder_PXLayer_3",
      'description': "Mean track residuals y in PXBarrel Layer 3",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Tracks/PXBarrel/residual_y_per_SignedModule_per_SignedLadder_PXLayer_4",
      'description': "Mean track residuals y in PXBarrel Layer 4",
      'draw': { 'withref': "no" }},]
   )

alignmentvalidationlayout(dqmitems, "38ca - Mean Residuals x inner Modules per Layer",
   [{ 'path': "PixelPhase1/Tracks/ResidualsExtra/PXBarrel/residual_mean_x_Inner_PXLayer_1",
      'description': "Mean track residuals x for inner Modules in PXBarrel Layer 1",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Tracks/ResidualsExtra/PXBarrel/residual_mean_x_Inner_PXLayer_2",
      'description': "Mean track residuals x for inner Modules in PXBarrel Layer 2",
      'draw': { 'withref': "no" }},],
   [{ 'path': "PixelPhase1/Tracks/ResidualsExtra/PXBarrel/residual_mean_x_Inner_PXLayer_3",
      'description': "Mean track residuals x for inner Modules in PXBarrel Layer 3",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Tracks/ResidualsExtra/PXBarrel/residual_mean_x_Inner_PXLayer_4",
      'description': "Mean track residuals x for inner Modules in PXBarrel Layer 4",
      'draw': { 'withref': "no" }},]
   )

alignmentvalidationlayout(dqmitems, "38cb - Mean Residuals x outer Modules per Layer",
   [{ 'path': "PixelPhase1/Tracks/ResidualsExtra/PXBarrel/residual_mean_x_Outer_PXLayer_1",
      'description': "Mean track residuals x for outer Modules in PXBarrel Layer 1",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Tracks/ResidualsExtra/PXBarrel/residual_mean_x_Outer_PXLayer_2",
      'description': "Mean track residuals x for outer Modules in PXBarrel Layer 2",
      'draw': { 'withref': "no" }},],
   [{ 'path': "PixelPhase1/Tracks/ResidualsExtra/PXBarrel/residual_mean_x_Outer_PXLayer_3",
      'description': "Mean track residuals x for outer Modules in PXBarrel Layer 3",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Tracks/ResidualsExtra/PXBarrel/residual_mean_x_Outer_PXLayer_4",
      'description': "Mean track residuals x for outer Modules in PXBarrel Layer 4",
      'draw': { 'withref': "no" }},]
   )

alignmentvalidationlayout(dqmitems, "38cc - Mean Residuals y inner Modules per Layer",
   [{ 'path': "PixelPhase1/Tracks/ResidualsExtra/PXBarrel/residual_mean_y_Inner_PXLayer_1",
      'description': "Mean track residuals y for inner Modules in PXBarrel Layer 1",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Tracks/ResidualsExtra/PXBarrel/residual_mean_y_Inner_PXLayer_2",
      'description': "Mean track residuals y for inner Modules in PXBarrel Layer 2",
      'draw': { 'withref': "no" }},],
   [{ 'path': "PixelPhase1/Tracks/ResidualsExtra/PXBarrel/residual_mean_y_Inner_PXLayer_3",
      'description': "Mean track residuals y for inner Modules in PXBarrel Layer 3",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Tracks/ResidualsExtra/PXBarrel/residual_mean_y_Inner_PXLayer_4",
      'description': "Mean track residuals y for inner Modules in PXBarrel Layer 4",
      'draw': { 'withref': "no" }},]
   )

alignmentvalidationlayout(dqmitems, "38cd - Mean Residuals y outer Modules per Layer",
   [{ 'path': "PixelPhase1/Tracks/ResidualsExtra/PXBarrel/residual_mean_y_Outer_PXLayer_1",
      'description': "Mean track residuals y for outer Modules in PXBarrel Layer 1",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Tracks/ResidualsExtra/PXBarrel/residual_mean_y_Outer_PXLayer_2",
      'description': "Mean track residuals y for outer Modules in PXBarrel Layer 2",
      'draw': { 'withref': "no" }},],
   [{ 'path': "PixelPhase1/Tracks/ResidualsExtra/PXBarrel/residual_mean_y_Outer_PXLayer_3",
      'description': "Mean track residuals y for outer Modules in PXBarrel Layer 3",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Tracks/ResidualsExtra/PXBarrel/residual_mean_y_Outer_PXLayer_4",
      'description': "Mean track residuals y for outer Modules in PXBarrel Layer 4",
      'draw': { 'withref': "no" }},]
   )
   
alignmentvalidationlayout(dqmitems, "38da - Residuals x per Disk",
   [{ 'path': "PixelPhase1/Tracks/PXForward/residual_x_PXDisk_+1",
      'description': "Track residuals x in PXForward Disk +1",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Tracks/PXForward/residual_x_PXDisk_+2",
      'description': "Track residuals x in PXForward Disk +2",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Tracks/PXForward/residual_x_PXDisk_+3",
      'description': "Track residuals x in PXForward Disk +3",
      'draw': { 'withref': "no" }},],
   [{ 'path': "PixelPhase1/Tracks/PXForward/residual_x_PXDisk_-1",
      'description': "Track residuals x in PXForward Disk -1",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Tracks/PXForward/residual_x_PXDisk_-2",
      'description': "Track residuals x in PXForward Disk -2",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Tracks/PXForward/residual_x_PXDisk_-3",
      'description': "Track residuals x in PXForward Disk -3",
      'draw': { 'withref': "no" }},]
   )

alignmentvalidationlayout(dqmitems, "38db - Residuals y per Disk",
   [{ 'path': "PixelPhase1/Tracks/PXForward/residual_y_PXDisk_+1",
      'description': "Track residuals y in PXForward Disk +1",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Tracks/PXForward/residual_y_PXDisk_+2",
      'description': "Track residuals y in PXForward Disk +2",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Tracks/PXForward/residual_y_PXDisk_+3",
      'description': "Track residuals y in PXForward Disk +3",
      'draw': { 'withref': "no" }},],
   [{ 'path': "PixelPhase1/Tracks/PXForward/residual_y_PXDisk_-1",
      'description': "Track residuals y in PXForward Disk -1",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Tracks/PXForward/residual_y_PXDisk_-2",
      'description': "Track residuals y in PXForward Disk -2",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Tracks/PXForward/residual_y_PXDisk_-3",
      'description': "Track residuals y in PXForward Disk -3",
      'draw': { 'withref': "no" }},]
   )
   
alignmentvalidationlayout(dqmitems, "38e - Profile Residuals PXFoward",
   [{ 'path': "PixelPhase1/Tracks/PXForward/residual_x_per_PXDisk_per_SignedBladePanel_PXRing_1",
      'description': "Mean track residuals x in PXFoward Ring 1",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Tracks/PXForward/residual_x_per_PXDisk_per_SignedBladePanel_PXRing_2",
      'description': "Mean track residuals x in PXFoward Ring 2",
      'draw': { 'withref': "no" }},],
   [{ 'path': "PixelPhase1/Tracks/PXForward/residual_y_per_PXDisk_per_SignedBladePanel_PXRing_1",
      'description': "Mean track residuals y in PXFoward Ring 1",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Tracks/PXForward/residual_y_per_PXDisk_per_SignedBladePanel_PXRing_2",
      'description': "Mean track residuals y in PXFoward Ring 2",
      'draw': { 'withref': "no" }},]
   )

alignmentvalidationlayout(dqmitems, "38fa - Mean Residuals InnerOuter Modules PXForward",
   [{ 'path': "PixelPhase1/Tracks/ResidualsExtra/PXForward/residual_mean_x_Inner",
      'description': "Mean track residuals x for inner Modules in PXFoward",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Tracks/ResidualsExtra/PXForward/residual_mean_x_Outer",
      'description': "Mean track residuals x for inner Modules in PXFoward",
      'draw': { 'withref': "no" }},],
   [{ 'path': "PixelPhase1/Tracks/ResidualsExtra/PXForward/residual_mean_y_Inner",
      'description': "Mean track residuals y for inner Modules in PXFoward",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Tracks/ResidualsExtra/PXForward/residual_mean_y_Outer",
      'description': "Mean track residuals y for inner Modules in PXFoward",
      'draw': { 'withref': "no" }},]
   )

alignmentvalidationlayout(dqmitems, "38fb - Mean Residuals pos.neg. Side PXForward",
   [{ 'path': "PixelPhase1/Tracks/ResidualsExtra/PXForward/residual_mean_x_pos",
      'description': "Mean track residuals x for pos. Side in PXFoward",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Tracks/ResidualsExtra/PXForward/residual_mean_x_neg",
      'description': "Mean track residuals x for neg. Side in PXFoward",
      'draw': { 'withref': "no" }},],
   [{ 'path': "PixelPhase1/Tracks/ResidualsExtra/PXForward/residual_mean_y_pos",
      'description': "Mean track residuals y for pos. Side in PXFoward",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Tracks/ResidualsExtra/PXForward/residual_mean_y_neg",
      'description': "Mean track residuals y for neg. Side in PXFoward",
      'draw': { 'withref': "no" }},]
   )

alignmentvalidationlayout(dqmitems, "42a - Barycenter coordinates",
  [{ 'path': "PixelPhase1/Barycenter/barycenters_BPIX",
     'description': "Barycenter coordinates derived from PXBarrel",
     'draw': {'withref' : "no"}},
   { 'path': "PixelPhase1/Barycenter/barycenters_FPIX_zm",
     'description': "Barycenter coordinates derived from PXForward z-",
     'draw': {'withref' : "no"}},
     { 'path': "PixelPhase1/Barycenter/barycenters_FPIX_zp",
     'description': "Barycenter coordinates derived from PXForward z-",
     'draw': {'withref' : "no"}}],
  )
  
alignmentvalidationlayout(dqmitems, "42b - Barycenter coordinates",
  [{ 'path': "PixelPhase1/Barycenter/barycenters_BPIX_xm",
     'description': "Barycenter coordinates derived from PXBarrel x-",
     'draw': {'withref' : "no"}},
   { 'path': "PixelPhase1/Barycenter/barycenters_BPIX_xp",
     'description': "Barycenter coordinates derived from PXBarrel x+",
     'draw': {'withref' : "no"}},
     { 'path': "PixelPhase1/Barycenter/barycenters_FPIX_zm_xm",
     'description': "Barycenter coordinates derived from PXForward z-,x-",
     'draw': {'withref' : "no"}}],
  [{ 'path': "PixelPhase1/Barycenter/barycenters_FPIX_zm_xp",
     'description': "Barycenter coordinates derived from PXForward z-,x+",
     'draw': {'withref' : "no"}},
   { 'path': "PixelPhase1/Barycenter/barycenters_FPIX_zp_xm",
     'description': "Barycenter coordinates derived from PXForward z+,x-",
     'draw': {'withref' : "no"}},
     { 'path': "PixelPhase1/Barycenter/barycenters_FPIX_zp_xp",
     'description': "Barycenter coordinates derived from PXForward z+,x+",
     'draw': {'withref' : "no"}}],
  )
  
alignmentvalidationlayout(dqmitems, "21 - TIB Residuals",
  [{ 'path': "SiStrip/MechanicalView/TIB/layer_1/HitResiduals_TIB__Layer__1",
     'description': "Hit Residual in TIB Layer #1"},
   { 'path': "SiStrip/MechanicalView/TIB/layer_2/HitResiduals_TIB__Layer__2",
     'description': "Hit Residual in TIB Layer #2"}],
  [{ 'path': "SiStrip/MechanicalView/TIB/layer_3/HitResiduals_TIB__Layer__3",
     'description': "Hit Residual in TIB Layer #3"},
   { 'path': "SiStrip/MechanicalView/TIB/layer_4/HitResiduals_TIB__Layer__4",
     'description': "Hit Residual in TIB Layer #4"}])
alignmentvalidationlayout(dqmitems, "22 - TOB Residuals",
  [{ 'path': "SiStrip/MechanicalView/TOB/layer_1/HitResiduals_TOB__Layer__1",
     'description': "Hit Residual in TOB Layer #1"},
   { 'path': "SiStrip/MechanicalView/TOB/layer_2/HitResiduals_TOB__Layer__2",
     'description': "Hit Residual in TOB Layer #2"},
   { 'path': "SiStrip/MechanicalView/TOB/layer_3/HitResiduals_TOB__Layer__3",
     'description': "Hit Residual in TOB Layer #3"}],
  [{ 'path': "SiStrip/MechanicalView/TOB/layer_4/HitResiduals_TOB__Layer__4",
     'description': "Hit Residual in TOB Layer #4"},
   { 'path': "SiStrip/MechanicalView/TOB/layer_5/HitResiduals_TOB__Layer__5",
     'description': "Hit Residual in TOB Layer #5"},
   { 'path': "SiStrip/MechanicalView/TOB/layer_6/HitResiduals_TOB__Layer__6",
     'description': "Hit Residual in TOB Layer #6"}])
alignmentvalidationlayout(dqmitems, "23 - TID+ Residuals",
  [{ 'path': "SiStrip/MechanicalView/TID/PLUS/wheel_1/HitResiduals_TID__wheel__1",
     'description': "Hit Residuals in TID+ Wheel #1"},
   { 'path': "SiStrip/MechanicalView/TID/PLUS/wheel_2/HitResiduals_TID__wheel__2",
     'description': "Hit Residuals in TID+ Wheel #2"},
   { 'path': "SiStrip/MechanicalView/TID/PLUS/wheel_3/HitResiduals_TID__wheel__3",
     'description': "Hit Residuals in TID+ Wheel #3 "}])
alignmentvalidationlayout(dqmitems, "24 - TID- Residuals",
  [{ 'path': "SiStrip/MechanicalView/TID/MINUS/wheel_1/HitResiduals_TID__wheel__1",
     'description': "Hit Residuals in TID- Wheel #1"},
   { 'path': "SiStrip/MechanicalView/TID/MINUS/wheel_2/HitResiduals_TID__wheel__2",
     'description': "Hit Residuals in TID- Wheel #2"},
   { 'path': "SiStrip/MechanicalView/TID/MINUS/wheel_3/HitResiduals_TID__wheel__3",
     'description': "Hit Residuals in TID- Wheel #3 "}])
alignmentvalidationlayout(dqmitems, "25 - TEC+ Residual",
  [{ 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_1/HitResiduals_TEC__wheel__1",
     'description': "Hit Residual in TEC+ Wheel #1"},
   { 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_2/HitResiduals_TEC__wheel__2",
     'description': "Hit Residual in TEC+ Wheel #2"},
   { 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_3/HitResiduals_TEC__wheel__3",
     'description': "Hit Residual in TEC+ Wheel #3"}],
  [{ 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_4/HitResiduals_TEC__wheel__4",
     'description': "Hit Residual in TEC+ Wheel #4"},
   { 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_5/HitResiduals_TEC__wheel__5",
     'description': "Hit Residual in TEC+ Wheel #5"},
   { 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_6/HitResiduals_TEC__wheel__6",
     'description': "Hit Residual in TEC+ Wheel #6"}],
  [{ 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_7/HitResiduals_TEC__wheel__7",
     'description': "Hit Residual in TEC+ Wheel #7"},
   { 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_8/HitResiduals_TEC__wheel__8",
     'description': "Hit Residual in TEC+ Wheel #8"},
   { 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_9/HitResiduals_TEC__wheel__9",
     'description': "Hit Residual in TEC+ Wheel #9"}])
alignmentvalidationlayout(dqmitems, "26 - TEC- Residual",
  [{ 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_1/HitResiduals_TEC__wheel__1",
     'description': "Hit Residual in TEC- Wheel #1"},
   { 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_2/HitResiduals_TEC__wheel__2",
     'description': "Hit Residual in TEC- Wheel #2"},
   { 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_3/HitResiduals_TEC__wheel__3",
     'description': "Hit Residual in TEC- Wheel #3"}],
  [{ 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_4/HitResiduals_TEC__wheel__4",
     'description': "Hit Residual in TEC- Wheel #4"},
   { 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_5/HitResiduals_TEC__wheel__5",
     'description': "Hit Residual in TEC- Wheel #5"},
   { 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_6/HitResiduals_TEC__wheel__6",
     'description': "Hit Residual in TEC- Wheel #6"}],
  [{ 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_7/HitResiduals_TEC__wheel__7",
     'description': "Hit Residual in TEC- Wheel #7"},
   { 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_8/HitResiduals_TEC__wheel__8",
     'description': "Hit Residual in TEC- Wheel #8"},
   { 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_9/HitResiduals_TEC__wheel__9",
     'description': "Hit Residual in TEC- Wheel #9"}])
