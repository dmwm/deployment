def p2trackervalidationlayout(i, p, *rows): i["MCLayouts/Tk_Phase2/" + p] = DQMItem(layout=rows)

p2trackervalidationlayout(dqmitems, "01 - IT Cluster Delta Phi",
                        [{ 'path':"TrackerPhase2ITClusterV/Delta_Phi_Pixel_Barrel",
                           'description': "Delta Phi of Clusters in the barrel (Pixels)"},
                         {'path':"TrackerPhase2ITClusterV/Delta_Phi_Pixel_Endcaps",
                          'description': "Delta Phi of Clusters in the endcaps (Pixels)"}])

p2trackervalidationlayout(dqmitems, "02 - IT RecHit Delta Phi",
                        [{ 'path':"TrackerPhase2ITRecHitV/Delta_Phi_Pixel_Barrel",
                           'description': "Delta Phi of RecHits in the barrel (Pixels)"},
                         {'path':"TrackerPhase2ITRecHitV/Delta_Phi_Pixel_Endcaps",
                          'description': "Delta Phi of RecHits in the endcaps (Pixels)"}])

p2trackervalidationlayout(dqmitems, "03 - IT TrackingRecHit Delta Phi",
                        [{ 'path':"TrackerPhase2ITTrackingRecHitV/Delta_Phi_Pixel_Barrel",
                           'description': "Delta Phi of TrackingRecHits in the barrel (Pixels)"},
                         {'path':"TrackerPhase2ITTrackingRecHitV/Delta_Phi_Pixel_Endcaps",
                          'description': "Delta Phi of TrackingRecHits in the endcaps (Pixels)"}])

p2trackervalidationlayout(dqmitems, "04 - OT Cluster Delta Phi",
                        [{ 'path':"TrackerPhase2OTClusterV/Delta_Phi_Pixel_Barrel",
                           'description': "Delta Phi of Clusters in the barrel (Pixels)"},
                         {'path':"TrackerPhase2OTClusterV/Delta_Phi_Pixel_Endcaps",
                          'description': "Delta Phi of Clusters in the endcaps (Pixels)"}],
                        [{ 'path':"TrackerPhase2OTClusterV/Delta_Phi_Strip_Barrel",
                           'description': "Delta Phi of Clusters in the barrel (Strips)"},
                         {'path':"TrackerPhase2OTClusterV/Delta_Phi_Strip_Endcaps",
                          'description': "Delta Phi of Clusters in the endcaps (Strips)"}])

p2trackervalidationlayout(dqmitems, "05 - OT RecHit Delta Phi",
                        [{ 'path':"TrackerPhase2OTRecHitV/Delta_Phi_Pixel_Barrel",
                           'description': "Delta Phi of RecHits in the barrel (Pixels)"},
                         {'path':"TrackerPhase2OTRecHitV/Delta_Phi_Pixel_Endcaps",
                          'description': "Delta Phi of RecHits in the endcaps (Pixels)"}],
                        [{ 'path':"TrackerPhase2OTRecHitV/Delta_Phi_Strip_Barrel",
                           'description': "Delta Phi of RecHits in the barrel (Strips)"},
                         {'path':"TrackerPhase2OTRecHitV/Delta_Phi_Strip_Endcaps",
                          'description': "Delta Phi of RecHits in the endcaps (Strips)"}])

p2trackervalidationlayout(dqmitems, "06 - OT TrackingRecHit Delta Phi",
                        [{ 'path':"TrackerPhase2OTTrackingRecHitV/Delta_Phi_Pixel_Barrel",
                           'description': "Delta Phi of TrackingRecHits in the barrel (Pixels)"},
                         {'path':"TrackerPhase2OTTrackingRecHitV/Delta_Phi_Pixel_Endcaps",
                          'description': "Delta Phi of TrackingRecHits in the endcaps (Pixels)"}],
                        [{ 'path':"TrackerPhase2OTTrackingRecHitV/Delta_Phi_Strip_Barrel",
                           'description': "Delta Phi of TrackingRecHits in the barrel (Strips)"},
                         {'path':"TrackerPhase2OTTrackingRecHitV/Delta_Phi_Strip_Endcaps",
                          'description': "Delta Phi of TrackingRecHits in the endcaps (Strips)"}])

p2trackervalidationlayout(dqmitems, "07 - OT Stub Delta Phi",
                        [{ 'path':"TrackerPhase2OTStubV/Residual/#Delta #phi Barrel PS modules",
                           'description': "Delta Phi of Stubs in the barrel (Pixels)"},
                         {'path':"TrackerPhase2OTStubV/Residual/#Delta #phi Endcaps PS modules",
                          'description': "Delta Phi of Stubs in the endcaps (Pixels)"}],
                        [{ 'path':"TrackerPhase2OTStubV/Residual/#Delta #phi Barrel 2S modules",
                           'description': "Delta Phi of Stubs in the barrel (Strips)"},
                         {'path':"TrackerPhase2OTStubV/Residual/#Delta #phi Endcaps 2S modules",
                          'description': "Delta Phi of Stubs in the endcaps (Strips)"}])

p2trackervalidationlayout(dqmitems, "08 - OT Stub Delta R",
                        [{'path':"TrackerPhase2OTStubV/Residual/#Delta r Endcaps PS modules",
                          'description': "Delta R of Stubs in the endcaps (Pixels)"}],
                        [{'path':"TrackerPhase2OTStubV/Residual/#Delta r Endcaps 2S modules",
                          'description': "Delta R of Stubs in the endcaps (Strips)"}])

p2trackervalidationlayout(dqmitems, "09 - OT Stub Rate",
                        [{ 'path':"TrackerPhase2OTStubV/number_of_stubs",
                           'description': "Stub rate"}])

p2trackervalidationlayout(dqmitems, "10 - OT L1Tracking Nominal eta",
                        [{ 'path':"TrackerPhase2OTL1TrackV/Nominal_L1TF/FinalEfficiency/EtaEfficiency",
                           'description': "eta efficiency of L1Tracks (Nominal)"},
                         {'path':"TrackerPhase2OTL1TrackV/Nominal_L1TF/FinalResolution/EtaResolution",
                          'description': "eta resolution of L1Tracks (Nominal)"}])

p2trackervalidationlayout(dqmitems, "11 - OT L1Tracking Nominal d0",
                        [{ 'path':"TrackerPhase2OTL1TrackV/Nominal_L1TF/FinalEfficiency/d0Efficiency",
                           'description': "d0 efficiency of L1Tracks (Nominal)"},
                         {'path':"TrackerPhase2OTL1TrackV/Nominal_L1TF/FinalResolution/d0Resolution",
                          'description': "d0 resolution of L1Tracks (Nominal)"}])

p2trackervalidationlayout(dqmitems, "12 - OT L1Tracking Nominal z0",
                        [{ 'path':"TrackerPhase2OTL1TrackV/Nominal_L1TF/FinalEfficiency/z0Efficiency",
                           'description': "z0 efficiency of L1Tracks (Nominal)"},
                         {'path':"TrackerPhase2OTL1TrackV/Nominal_L1TF/FinalResolution/z0Resolution",
                          'description': "z0 resolution of L1Tracks (Nominal)"}])

p2trackervalidationlayout(dqmitems, "13 - OT extended L1Tracking displaced eta",
                        [{ 'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Displaced/FinalEfficiency/EtaEfficiency",
                           'description': "eta efficiency of extended L1Tracks (displaced)"},
                         {'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Displaced/FinalResolution/EtaResolution_displaced",
                          'description': "eta resolution of extended L1Tracks (displaced)"}])

p2trackervalidationlayout(dqmitems, "14 - OT extended L1Tracking displaced d0",
                        [{ 'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Displaced/FinalEfficiency/d0Efficiency",
                           'description': "d0 efficiency of extended L1Tracks (displaced)"},
                         {'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Displaced/FinalResolution/d0Resolution_displaced",
                          'description': "d0 resolution of extended L1Tracks (displaced)"}])

p2trackervalidationlayout(dqmitems, "15 - OT extended L1Tracking displaced z0",
                        [{ 'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Displaced/FinalEfficiency/z0Efficiency",
                           'description': "z0 efficiency of extended L1Tracks (displaced)"},
                         {'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Displaced/FinalResolution/z0Resolution_displaced",
                          'description': "z0 resolution of extended L1Tracks (displaced)"}])

p2trackervalidationlayout(dqmitems, "16 - OT extended L1Tracking prompt eta",
                        [{ 'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Prompt/FinalEfficiency/EtaEfficiency",
                           'description': "eta efficiency of extended L1Tracks (prompt)"},
                         {'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Prompt/FinalResolution/EtaResolution_prompt",
                          'description': "eta resolution of extended L1Tracks (prompt)"}])

p2trackervalidationlayout(dqmitems, "17 - OT extended L1Tracking prompt d0",
                        [{ 'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Prompt/FinalEfficiency/d0Efficiency",
                           'description': "d0 efficiency of extended L1Tracks (prompt)"},
                         {'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Prompt/FinalResolution/d0Resolution_prompt",
                          'description': "d0 resolution of extended L1Tracks (prompt)"}])

p2trackervalidationlayout(dqmitems, "18 - OT extended L1Tracking prompt z0",
                        [{ 'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Prompt/FinalEfficiency/z0Efficiency",
                           'description': "z0 efficiency of extended L1Tracks (prompt)"},
                         {'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Prompt/FinalResolution/z0Resolution_prompt",
                          'description': "z0 resolution of extended L1Tracks (prompt)"}])

p2trackervalidationlayout(dqmitems, "19 - OT number of L1Track Particles",
                        [{ 'path':"TrackerPhase2OTL1TrackV/trackParticles/trackParts_Num",
                           'description': "Number of L1Track Particles"}])
