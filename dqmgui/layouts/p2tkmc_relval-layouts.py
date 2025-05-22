def phase2tkmclayout(i, p, *rows): i["MCLayouts/Phase2Tk/" + p] = DQMItem(layout=rows)

phase2tkmclayout(dqmitems, "000 - IT Cluster Barrel X",
                 [{'path':"TrackerPhase2ITClusterV/Barrel/Layer1/Delta_X_Pixel",
                   'description': "Layer 1 Delta X Pixel"},
                  {'path':"TrackerPhase2ITClusterV/Barrel/Layer2/Delta_X_Pixel",
                   'description': "Layer 2 Delta X Pixel"}],
                 [{'path':"TrackerPhase2ITClusterV/Barrel/Layer3/Delta_X_Pixel",
                   'description': "Layer 3 Delta X Pixel"},
                  {'path':"TrackerPhase2ITClusterV/Barrel/Layer4/Delta_X_Pixel",
                   'description': "Layer 4 Delta X Pixel"}]
                 )

phase2tkmclayout(dqmitems, "001 - IT Cluster Barrel Y",
                 [{'path':"TrackerPhase2ITClusterV/Barrel/Layer1/Delta_Y_Pixel",
                   'description': "Layer 1 Delta Y Pixel"},
                  {'path':"TrackerPhase2ITClusterV/Barrel/Layer2/Delta_Y_Pixel",
                   'description': "Layer 2 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2ITClusterV/Barrel/Layer3/Delta_Y_Pixel",
                   'description': "Layer 3 Delta Y Pixel"},
                  {'path':"TrackerPhase2ITClusterV/Barrel/Layer4/Delta_Y_Pixel",
                   'description': "Layer 4 Delta Y Pixel"}]
                 )

phase2tkmclayout(dqmitems, "002 - IT Cluster Endcap MINUS EPix X",
                 [{'path':"TrackerPhase2ITClusterV/EndCap_Side1/EPix/Ring1/Delta_X_Pixel",
                   'description': "Ring 1 Delta X Pixel"},
                  {'path':"TrackerPhase2ITClusterV/EndCap_Side1/EPix/Ring2/Delta_X_Pixel",
                   'description': "Ring 2 Delta X Pixel"}],
                 [{'path':"TrackerPhase2ITClusterV/EndCap_Side1/EPix/Ring3/Delta_X_Pixel",
                   'description': "Ring 3 Delta X Pixel"},
                  {'path':"TrackerPhase2ITClusterV/EndCap_Side1/EPix/Ring4/Delta_X_Pixel",
                   'description': "Ring 4 Delta X Pixel"}],
                 [{'path':"TrackerPhase2ITClusterV/EndCap_Side1/EPix/Ring5/Delta_X_Pixel",
                   'description': "Ring 5 Delta X Pixel"}]
                 )

phase2tkmclayout(dqmitems, "003 - IT Cluster Endcap MINUS EPix Y",
                 [{'path':"TrackerPhase2ITClusterV/EndCap_Side1/EPix/Ring1/Delta_Y_Pixel",
                   'description': "Ring 1 Delta Y Pixel"},
                  {'path':"TrackerPhase2ITClusterV/EndCap_Side1/EPix/Ring2/Delta_Y_Pixel",
                   'description': "Ring 2 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2ITClusterV/EndCap_Side1/EPix/Ring3/Delta_Y_Pixel",
                   'description': "Ring 3 Delta Y Pixel"},
                  {'path':"TrackerPhase2ITClusterV/EndCap_Side1/EPix/Ring4/Delta_Y_Pixel",
                   'description': "Ring 4 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2ITClusterV/EndCap_Side1/EPix/Ring5/Delta_Y_Pixel",
                   'description': "Ring 5 Delta Y Pixel"}]
                 )

phase2tkmclayout(dqmitems, "004 - IT Cluster Endcap MINUS FPix X",
                 [{'path':"TrackerPhase2ITClusterV/EndCap_Side1/FPix/Ring1/Delta_X_Pixel",
                   'description': "Ring 1 Delta X Pixel"},
                  {'path':"TrackerPhase2ITClusterV/EndCap_Side1/FPix/Ring2/Delta_X_Pixel",
                   'description': "Ring 2 Delta X Pixel"}],
                 [{'path':"TrackerPhase2ITClusterV/EndCap_Side1/FPix/Ring3/Delta_X_Pixel",
                   'description': "Ring 3 Delta X Pixel"},
                  {'path':"TrackerPhase2ITClusterV/EndCap_Side1/FPix/Ring4/Delta_X_Pixel",
                   'description': "Ring 4 Delta X Pixel"}]
                 )

phase2tkmclayout(dqmitems, "005 - IT Cluster Endcap MINUS FPix Y",
                 [{'path':"TrackerPhase2ITClusterV/EndCap_Side1/FPix/Ring1/Delta_Y_Pixel",
                   'description': "Ring 1 Delta Y Pixel"},
                  {'path':"TrackerPhase2ITClusterV/EndCap_Side1/FPix/Ring2/Delta_Y_Pixel",
                   'description': "Ring 2 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2ITClusterV/EndCap_Side1/FPix/Ring3/Delta_Y_Pixel",
                   'description': "Ring 3 Delta Y Pixel"},
                  {'path':"TrackerPhase2ITClusterV/EndCap_Side1/FPix/Ring4/Delta_Y_Pixel",
                   'description': "Ring 4 Delta Y Pixel"}]
                 )

phase2tkmclayout(dqmitems, "006 - IT Cluster Endcap PLUS EPix X",
                 [{'path':"TrackerPhase2ITClusterV/EndCap_Side2/EPix/Ring1/Delta_X_Pixel",
                   'description': "Ring 1 Delta X Pixel"},
                  {'path':"TrackerPhase2ITClusterV/EndCap_Side2/EPix/Ring2/Delta_X_Pixel",
                   'description': "Ring 2 Delta X Pixel"}],
                 [{'path':"TrackerPhase2ITClusterV/EndCap_Side2/EPix/Ring3/Delta_X_Pixel",
                   'description': "Ring 3 Delta X Pixel"},
                  {'path':"TrackerPhase2ITClusterV/EndCap_Side2/EPix/Ring4/Delta_X_Pixel",
                   'description': "Ring 4 Delta X Pixel"}],
                 [{'path':"TrackerPhase2ITClusterV/EndCap_Side2/EPix/Ring5/Delta_X_Pixel",
                   'description': "Ring 5 Delta X Pixel"}]
                 )

phase2tkmclayout(dqmitems, "007 - IT Cluster Endcap PLUS EPix Y",
                 [{'path':"TrackerPhase2ITClusterV/EndCap_Side2/EPix/Ring1/Delta_Y_Pixel",
                   'description': "Ring 1 Delta Y Pixel"},
                  {'path':"TrackerPhase2ITClusterV/EndCap_Side2/EPix/Ring2/Delta_Y_Pixel",
                   'description': "Ring 2 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2ITClusterV/EndCap_Side2/EPix/Ring3/Delta_Y_Pixel",
                   'description': "Ring 3 Delta Y Pixel"},
                  {'path':"TrackerPhase2ITClusterV/EndCap_Side2/EPix/Ring4/Delta_Y_Pixel",
                   'description': "Ring 4 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2ITClusterV/EndCap_Side2/EPix/Ring5/Delta_Y_Pixel",
                   'description': "Ring 5 Delta Y Pixel"}]
                 )

phase2tkmclayout(dqmitems, "008 - IT Cluster Endcap PLUS FPix X",
                 [{'path':"TrackerPhase2ITClusterV/EndCap_Side2/FPix/Ring1/Delta_X_Pixel",
                   'description': "Ring 1 Delta X Pixel"},
                  {'path':"TrackerPhase2ITClusterV/EndCap_Side2/FPix/Ring2/Delta_X_Pixel",
                   'description': "Ring 2 Delta X Pixel"}],
                 [{'path':"TrackerPhase2ITClusterV/EndCap_Side2/FPix/Ring3/Delta_X_Pixel",
                   'description': "Ring 3 Delta X Pixel"},
                  {'path':"TrackerPhase2ITClusterV/EndCap_Side2/FPix/Ring4/Delta_X_Pixel",
                   'description': "Ring 4 Delta X Pixel"}]
                 )

phase2tkmclayout(dqmitems, "009 - IT Cluster Endcap PLUS FPix Y",
                 [{'path':"TrackerPhase2ITClusterV/EndCap_Side2/FPix/Ring1/Delta_Y_Pixel",
                   'description': "Ring 1 Delta Y Pixel"},
                  {'path':"TrackerPhase2ITClusterV/EndCap_Side2/FPix/Ring2/Delta_Y_Pixel",
                   'description': "Ring 2 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2ITClusterV/EndCap_Side2/FPix/Ring3/Delta_Y_Pixel",
                   'description': "Ring 3 Delta Y Pixel"},
                  {'path':"TrackerPhase2ITClusterV/EndCap_Side2/FPix/Ring4/Delta_Y_Pixel",
                   'description': "Ring 4 Delta Y Pixel"}]
                 )

phase2tkmclayout(dqmitems, "100 - IT RecHit Barrel Delta Y v Delta X",
                 [{'path':"TrackerPhase2ITRecHitV/Barrel/Layer1/Delta_Y_vs_DeltaX",
                   'description': "Layer 1 Delta Y v Delta X"},
                  {'path':"TrackerPhase2ITRecHitV/Barrel/Layer2/Delta_Y_vs_DeltaX",
                   'description': "Layer 2 Delta Y v Delta X"}],
                 [{'path':"TrackerPhase2ITRecHitV/Barrel/Layer3/Delta_Y_vs_DeltaX",
                   'description': "Layer 3 Delta Y v Delta X"},
                  {'path':"TrackerPhase2ITRecHitV/Barrel/Layer4/Delta_Y_vs_DeltaX",
                   'description': "Layer 4 Delta Y v Delta X"}]
                 )

phase2tkmclayout(dqmitems, "101 - IT RecHit Endcap MINUS EPix Delta Y v Delta X",
                 [{'path':"TrackerPhase2ITRecHitV/EndCap_Side1/EPix/Ring1/Delta_Y_vs_DeltaX",
                   'description': "Ring 1 Delta Y v Delta X"},
                  {'path':"TrackerPhase2ITRecHitV/EndCap_Side1/EPix/Ring2/Delta_Y_vs_DeltaX",
                   'description': "Ring 2 Delta Y v Delta X"}],
                 [{'path':"TrackerPhase2ITRecHitV/EndCap_Side1/EPix/Ring3/Delta_Y_vs_DeltaX",
                   'description': "Ring 3 Delta Y v Delta X"},
                  {'path':"TrackerPhase2ITRecHitV/EndCap_Side1/EPix/Ring4/Delta_Y_vs_DeltaX",
                   'description': "Ring 4 Delta Y v Delta X"}],
                 [{'path':"TrackerPhase2ITRecHitV/EndCap_Side1/EPix/Ring5/Delta_Y_vs_DeltaX",
                   'description': "Ring 5 Delta Y v Delta X"}]
                 )

phase2tkmclayout(dqmitems, "102 - IT RecHit Endcap MINUS FPix Delta Y v Delta X",
                 [{'path':"TrackerPhase2ITRecHitV/EndCap_Side1/FPix/Ring1/Delta_Y_vs_DeltaX",
                   'description': "Ring 1 Delta Y v Delta X"},
                  {'path':"TrackerPhase2ITRecHitV/EndCap_Side1/FPix/Ring2/Delta_Y_vs_DeltaX",
                   'description': "Ring 2 Delta Y v Delta X"}],
                 [{'path':"TrackerPhase2ITRecHitV/EndCap_Side1/FPix/Ring3/Delta_Y_vs_DeltaX",
                   'description': "Ring 3 Delta Y v Delta X"},
                  {'path':"TrackerPhase2ITRecHitV/EndCap_Side1/FPix/Ring4/Delta_Y_vs_DeltaX",
                   'description': "Ring 4 Delta Y v Delta X"}]
                 )

phase2tkmclayout(dqmitems, "103 - IT RecHit Endcap PLUS EPix Delta Y v Delta X",
                 [{'path':"TrackerPhase2ITRecHitV/EndCap_Side2/EPix/Ring1/Delta_Y_vs_DeltaX",
                   'description': "Ring 1 Delta Y v Delta X"},
                  {'path':"TrackerPhase2ITRecHitV/EndCap_Side2/EPix/Ring2/Delta_Y_vs_DeltaX",
                   'description': "Ring 2 Delta Y v Delta X"}],
                 [{'path':"TrackerPhase2ITRecHitV/EndCap_Side2/EPix/Ring3/Delta_Y_vs_DeltaX",
                   'description': "Ring 3 Delta Y v Delta X"},
                  {'path':"TrackerPhase2ITRecHitV/EndCap_Side2/EPix/Ring4/Delta_Y_vs_DeltaX",
                   'description': "Ring 4 Delta Y v Delta X"}],
                 [{'path':"TrackerPhase2ITRecHitV/EndCap_Side2/EPix/Ring5/Delta_Y_vs_DeltaX",
                   'description': "Ring 5 Delta Y v Delta X"}]
                 )

phase2tkmclayout(dqmitems, "104 - IT RecHit Endcap PLUS FPix Delta Y v Delta X",
                 [{'path':"TrackerPhase2ITRecHitV/EndCap_Side2/FPix/Ring1/Delta_Y_vs_DeltaX",
                   'description': "Ring 1 Delta Y v Delta X"},
                  {'path':"TrackerPhase2ITRecHitV/EndCap_Side2/FPix/Ring2/Delta_Y_vs_DeltaX",
                   'description': "Ring 2 Delta Y v Delta X"}],
                 [{'path':"TrackerPhase2ITRecHitV/EndCap_Side2/FPix/Ring3/Delta_Y_vs_DeltaX",
                   'description': "Ring 3 Delta Y v Delta X"},
                  {'path':"TrackerPhase2ITRecHitV/EndCap_Side2/FPix/Ring4/Delta_Y_vs_DeltaX",
                   'description': "Ring 4 Delta Y v Delta X"}]
                 )

phase2tkmclayout(dqmitems, "200 - IT TrackingRecHit Barrel X",
                 [{'path':"TrackerPhase2ITTrackingRecHitV/Barrel/Layer1/Delta_X",
                   'description': "Layer 1 Delta X"},
                  {'path':"TrackerPhase2ITTrackingRecHitV/Barrel/Layer2/Delta_X",
                   'description': "Layer 2 Delta X"}],
                 [{'path':"TrackerPhase2ITTrackingRecHitV/Barrel/Layer3/Delta_X",
                   'description': "Layer 3 Delta X"},
                  {'path':"TrackerPhase2ITTrackingRecHitV/Barrel/Layer4/Delta_X",
                   'description': "Layer 4 Delta X"}]
                 )

phase2tkmclayout(dqmitems, "201 - IT TrackingRecHit Barrel Y",
                 [{'path':"TrackerPhase2ITTrackingRecHitV/Barrel/Layer1/Delta_Y",
                   'description': "Layer 1 Delta Y"},
                  {'path':"TrackerPhase2ITTrackingRecHitV/Barrel/Layer2/Delta_Y",
                   'description': "Layer 2 Delta Y"}],
                 [{'path':"TrackerPhase2ITTrackingRecHitV/Barrel/Layer3/Delta_Y",
                   'description': "Layer 3 Delta Y"},
                  {'path':"TrackerPhase2ITTrackingRecHitV/Barrel/Layer4/Delta_Y",
                   'description': "Layer 4 Delta Y"}]
                 )

phase2tkmclayout(dqmitems, "202 - IT TrackingRecHit Endcap MINUS EPix X",
                 [{'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side1/EPix/Ring1/Delta_X",
                   'description': "Ring 1 Delta X"},
                  {'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side1/EPix/Ring2/Delta_X",
                   'description': "Ring 2 Delta X"}],
                 [{'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side1/EPix/Ring3/Delta_X",
                   'description': "Ring 3 Delta X"},
                  {'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side1/EPix/Ring4/Delta_X",
                   'description': "Ring 4 Delta X"}],
                 [{'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side1/EPix/Ring5/Delta_X",
                   'description': "Ring 5 Delta X"}]
                 )

phase2tkmclayout(dqmitems, "203 - IT TrackingRecHit Endcap MINUS EPix Y",
                 [{'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side1/EPix/Ring1/Delta_Y",
                   'description': "Ring 1 Delta Y"},
                  {'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side1/EPix/Ring2/Delta_Y",
                   'description': "Ring 2 Delta Y"}],
                 [{'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side1/EPix/Ring3/Delta_Y",
                   'description': "Ring 3 Delta Y"},
                  {'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side1/EPix/Ring4/Delta_Y",
                   'description': "Ring 4 Delta Y"}],
                 [{'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side1/EPix/Ring5/Delta_Y",
                   'description': "Ring 5 Delta Y"}]
                 )

phase2tkmclayout(dqmitems, "204 - IT TrackingRecHit Endcap MINUS FPix X",
                 [{'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side1/FPix/Ring1/Delta_X",
                   'description': "Ring 1 Delta X"},
                  {'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side1/FPix/Ring2/Delta_X",
                   'description': "Ring 2 Delta X"}],
                 [{'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side1/FPix/Ring3/Delta_X",
                   'description': "Ring 3 Delta X"},
                  {'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side1/FPix/Ring4/Delta_X",
                   'description': "Ring 4 Delta X"}]
                 )

phase2tkmclayout(dqmitems, "205 - IT TrackingRecHit Endcap MINUS FPix Y",
                 [{'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side1/FPix/Ring1/Delta_Y",
                   'description': "Ring 1 Delta Y"},
                  {'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side1/FPix/Ring2/Delta_Y",
                   'description': "Ring 2 Delta Y"}],
                 [{'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side1/FPix/Ring3/Delta_Y",
                   'description': "Ring 3 Delta Y"},
                  {'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side1/FPix/Ring4/Delta_Y",
                   'description': "Ring 4 Delta Y"}]
                 )

phase2tkmclayout(dqmitems, "206 - IT TrackingRecHit Endcap PLUS EPix X",
                 [{'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side2/EPix/Ring1/Delta_X",
                   'description': "Ring 1 Delta X"},
                  {'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side2/EPix/Ring2/Delta_X",
                   'description': "Ring 2 Delta X"}],
                 [{'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side2/EPix/Ring3/Delta_X",
                   'description': "Ring 3 Delta X"},
                  {'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side2/EPix/Ring4/Delta_X",
                   'description': "Ring 4 Delta X"}],
                 [{'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side2/EPix/Ring5/Delta_X",
                   'description': "Ring 5 Delta X"}]
                 )

phase2tkmclayout(dqmitems, "207 - IT TrackingRecHit Endcap PLUS EPix Y",
                 [{'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side2/EPix/Ring1/Delta_Y",
                   'description': "Ring 1 Delta Y"},
                  {'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side2/EPix/Ring2/Delta_Y",
                   'description': "Ring 2 Delta Y"}],
                 [{'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side2/EPix/Ring3/Delta_Y",
                   'description': "Ring 3 Delta Y"},
                  {'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side2/EPix/Ring4/Delta_Y",
                   'description': "Ring 4 Delta Y"}],
                 [{'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side2/EPix/Ring5/Delta_Y",
                   'description': "Ring 5 Delta Y"}]
                 )

phase2tkmclayout(dqmitems, "208 - IT TrackingRecHit Endcap PLUS FPix X",
                 [{'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side2/FPix/Ring1/Delta_X",
                   'description': "Ring 1 Delta X"},
                  {'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side2/FPix/Ring2/Delta_X",
                   'description': "Ring 2 Delta X"}],
                 [{'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side2/FPix/Ring3/Delta_X",
                   'description': "Ring 3 Delta X"},
                  {'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side2/FPix/Ring4/Delta_X",
                   'description': "Ring 4 Delta X"}]
                 )

phase2tkmclayout(dqmitems, "209 - IT TrackingRecHit Endcap PLUS FPix Y",
                 [{'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side2/FPix/Ring1/Delta_Y",
                   'description': "Ring 1 Delta Y"},
                  {'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side2/FPix/Ring2/Delta_Y",
                   'description': "Ring 2 Delta Y"}],
                 [{'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side2/FPix/Ring3/Delta_Y",
                   'description': "Ring 3 Delta Y"},
                  {'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side2/FPix/Ring4/Delta_Y",
                   'description': "Ring 4 Delta Y"}]
                 )

phase2tkmclayout(dqmitems, "300 - OT Cluster Barrel Pixel X",
                 [{'path':"TrackerPhase2OTClusterV/Barrel/Layer1/Delta_X_Pixel",
                   'description': "Layer 1 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/Barrel/Layer2/Delta_X_Pixel",
                   'description': "Layer 2 Delta X Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/Barrel/Layer3/Delta_X_Pixel",
                   'description': "Layer 3 Delta X Pixel"}]
                 )

phase2tkmclayout(dqmitems, "301 - OT Cluster Barrel Pixel Y",
                 [{'path':"TrackerPhase2OTClusterV/Barrel/Layer1/Delta_Y_Pixel",
                   'description': "Layer 1 Delta Y Pixel"},
                  {'path':"TrackerPhase2OTClusterV/Barrel/Layer2/Delta_Y_Pixel",
                   'description': "Layer 2 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/Barrel/Layer3/Delta_Y_Pixel",
                   'description': "Layer 3 Delta Y Pixel"}]
                 )

phase2tkmclayout(dqmitems, "302 - OT Cluster Barrel Strip X",
                 [{'path':"TrackerPhase2OTClusterV/Barrel/Layer1/Delta_X_Strip",
                   'description': "Layer 1 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/Barrel/Layer2/Delta_X_Strip",
                   'description': "Layer 2 Delta X Strip"}],
                 [{'path':"TrackerPhase2OTClusterV/Barrel/Layer3/Delta_X_Strip",
                   'description': "Layer 3 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/Barrel/Layer4/Delta_X_Strip",
                   'description': "Layer 4 Delta X Strip"}],
                 [{'path':"TrackerPhase2OTClusterV/Barrel/Layer5/Delta_X_Strip",
                   'description': "Layer 5 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/Barrel/Layer6/Delta_X_Strip",
                   'description': "Layer 6 Delta X Strip"}]
                 )

phase2tkmclayout(dqmitems, "303 - OT Cluster Barrel Strip Y",
                 [{'path':"TrackerPhase2OTClusterV/Barrel/Layer1/Delta_Y_Strip",
                   'description': "Layer 1 Delta Y Strip"},
                  {'path':"TrackerPhase2OTClusterV/Barrel/Layer2/Delta_Y_Strip",
                   'description': "Layer 2 Delta Y Strip"}],
                 [{'path':"TrackerPhase2OTClusterV/Barrel/Layer3/Delta_Y_Strip",
                   'description': "Layer 3 Delta Y Strip"},
                  {'path':"TrackerPhase2OTClusterV/Barrel/Layer4/Delta_Y_Strip",
                   'description': "Layer 4 Delta Y Strip"}],
                 [{'path':"TrackerPhase2OTClusterV/Barrel/Layer5/Delta_Y_Strip",
                   'description': "Layer 5 Delta Y Strip"},
                  {'path':"TrackerPhase2OTClusterV/Barrel/Layer6/Delta_Y_Strip",
                   'description': "Layer 6 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring1/304 - OT Cluster Endcap MINUS TEDD1 Ring1 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring1/Delta_X_Pixel",
                   'description': "Ring 1 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring1/Delta_Y_Pixel",
                   'description': "Ring 1 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring1/Delta_X_Strip",
                   'description': "Ring 1 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring1/Delta_Y_Strip",
                   'description': "Ring 1 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring2/305 - OT Cluster Endcap MINUS TEDD1 Ring2 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring2/Delta_X_Pixel",
                   'description': "Ring 2 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring2/Delta_Y_Pixel",
                   'description': "Ring 2 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring2/Delta_X_Strip",
                   'description': "Ring 2 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring2/Delta_Y_Strip",
                   'description': "Ring 2 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring3/306 - OT Cluster Endcap MINUS TEDD1 Ring3 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring3/Delta_X_Pixel",
                   'description': "Ring 3 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring3/Delta_Y_Pixel",
                   'description': "Ring 3 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring3/Delta_X_Strip",
                   'description': "Ring 3 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring3/Delta_Y_Strip",
                   'description': "Ring 3 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring4/307 - OT Cluster Endcap MINUS TEDD1 Ring4 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring4/Delta_X_Pixel",
                   'description': "Ring 4 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring4/Delta_Y_Pixel",
                   'description': "Ring 4 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring4/Delta_X_Strip",
                   'description': "Ring 4 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring4/Delta_Y_Strip",
                   'description': "Ring 4 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring5/308 - OT Cluster Endcap MINUS TEDD1 Ring5 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring5/Delta_X_Pixel",
                   'description': "Ring 5 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring5/Delta_Y_Pixel",
                   'description': "Ring 5 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring5/Delta_X_Strip",
                   'description': "Ring 5 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring5/Delta_Y_Strip",
                   'description': "Ring 5 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring6/309 - OT Cluster Endcap MINUS TEDD1 Ring6 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring6/Delta_X_Pixel",
                   'description': "Ring 6 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring6/Delta_Y_Pixel",
                   'description': "Ring 6 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring6/Delta_X_Strip",
                   'description': "Ring 6 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring6/Delta_Y_Strip",
                   'description': "Ring 6 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring7/310 - OT Cluster Endcap MINUS TEDD1 Ring7 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring7/Delta_X_Pixel",
                   'description': "Ring 7 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring7/Delta_Y_Pixel",
                   'description': "Ring 7 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring7/Delta_X_Strip",
                   'description': "Ring 7 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring7/Delta_Y_Strip",
                   'description': "Ring 7 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring8/311 - OT Cluster Endcap MINUS TEDD1 Ring8 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring8/Delta_X_Pixel",
                   'description': "Ring 8 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring8/Delta_Y_Pixel",
                   'description': "Ring 8 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring8/Delta_X_Strip",
                   'description': "Ring 8 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring8/Delta_Y_Strip",
                   'description': "Ring 8 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring9/312 - OT Cluster Endcap MINUS TEDD1 Ring9 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring9/Delta_X_Pixel",
                   'description': "Ring 9 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring9/Delta_Y_Pixel",
                   'description': "Ring 9 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring9/Delta_X_Strip",
                   'description': "Ring 9 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring9/Delta_Y_Strip",
                   'description': "Ring 9 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring10/313 - OT Cluster Endcap MINUS TEDD1 Ring10 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring10/Delta_X_Pixel",
                   'description': "Ring 10 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring10/Delta_Y_Pixel",
                   'description': "Ring 10 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring10/Delta_X_Strip",
                   'description': "Ring 10 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring10/Delta_Y_Strip",
                   'description': "Ring 10 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring11/314 - OT Cluster Endcap MINUS TEDD1 Ring11 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring11/Delta_X_Strip",
                   'description': "Ring 11 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring11/Delta_Y_Strip",
                   'description': "Ring 11 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring12/315 - OT Cluster Endcap MINUS TEDD1 Ring12 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring12/Delta_X_Strip",
                   'description': "Ring 12 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring12/Delta_Y_Strip",
                   'description': "Ring 12 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring13/316 - OT Cluster Endcap MINUS TEDD1 Ring13 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring13/Delta_X_Strip",
                   'description': "Ring 13 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring13/Delta_Y_Strip",
                   'description': "Ring 13 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring14/317 - OT Cluster Endcap MINUS TEDD1 Ring14 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring14/Delta_X_Strip",
                   'description': "Ring 14 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring14/Delta_Y_Strip",
                   'description': "Ring 14 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring15/318 - OT Cluster Endcap MINUS TEDD1 Ring15 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring15/Delta_X_Strip",
                   'description': "Ring 15 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring15/Delta_Y_Strip",
                   'description': "Ring 15 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2-/Ring1/319 - OT Cluster Endcap MINUS TEDD2 Ring1 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring1/Delta_X_Pixel",
                   'description': "Ring 1 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring1/Delta_Y_Pixel",
                   'description': "Ring 1 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring1/Delta_X_Strip",
                   'description': "Ring 1 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring1/Delta_Y_Strip",
                   'description': "Ring 1 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2-/Ring2/320 - OT Cluster Endcap MINUS TEDD2 Ring2 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring2/Delta_X_Pixel",
                   'description': "Ring 2 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring2/Delta_Y_Pixel",
                   'description': "Ring 2 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring2/Delta_X_Strip",
                   'description': "Ring 2 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring2/Delta_Y_Strip",
                   'description': "Ring 2 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2-/Ring3/321 - OT Cluster Endcap MINUS TEDD2 Ring3 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring3/Delta_X_Pixel",
                   'description': "Ring 3 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring3/Delta_Y_Pixel",
                   'description': "Ring 3 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring3/Delta_X_Strip",
                   'description': "Ring 3 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring3/Delta_Y_Strip",
                   'description': "Ring 3 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2-/Ring4/322 - OT Cluster Endcap MINUS TEDD2 Ring4 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring4/Delta_X_Pixel",
                   'description': "Ring 4 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring4/Delta_Y_Pixel",
                   'description': "Ring 4 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring4/Delta_X_Strip",
                   'description': "Ring 4 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring4/Delta_Y_Strip",
                   'description': "Ring 4 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2-/Ring5/323 - OT Cluster Endcap MINUS TEDD2 Ring5 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring5/Delta_X_Pixel",
                   'description': "Ring 5 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring5/Delta_Y_Pixel",
                   'description': "Ring 5 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring5/Delta_X_Strip",
                   'description': "Ring 5 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring5/Delta_Y_Strip",
                   'description': "Ring 5 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2-/Ring6/324 - OT Cluster Endcap MINUS TEDD2 Ring6 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring6/Delta_X_Pixel",
                   'description': "Ring 6 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring6/Delta_Y_Pixel",
                   'description': "Ring 6 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring6/Delta_X_Strip",
                   'description': "Ring 6 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring6/Delta_Y_Strip",
                   'description': "Ring 6 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2-/Ring7/325 - OT Cluster Endcap MINUS TEDD2 Ring7 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring7/Delta_X_Pixel",
                   'description': "Ring 7 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring7/Delta_Y_Pixel",
                   'description': "Ring 7 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring7/Delta_X_Strip",
                   'description': "Ring 7 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring7/Delta_Y_Strip",
                   'description': "Ring 7 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2-/Ring8/326 - OT Cluster Endcap MINUS TEDD2 Ring8 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring8/Delta_X_Strip",
                   'description': "Ring 8 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring8/Delta_Y_Strip",
                   'description': "Ring 8 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2-/Ring9/327 - OT Cluster Endcap MINUS TEDD2 Ring9 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring9/Delta_X_Strip",
                   'description': "Ring 9 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring9/Delta_Y_Strip",
                   'description': "Ring 9 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2-/Ring10/328 - OT Cluster Endcap MINUS TEDD2 Ring10 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring10/Delta_X_Strip",
                   'description': "Ring 10 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring10/Delta_Y_Strip",
                   'description': "Ring 10 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2-/Ring11/329 - OT Cluster Endcap MINUS TEDD2 Ring11 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring11/Delta_X_Strip",
                   'description': "Ring 11 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring11/Delta_Y_Strip",
                   'description': "Ring 11 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2-/Ring12/330 - OT Cluster Endcap MINUS TEDD2 Ring12 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring12/Delta_X_Strip",
                   'description': "Ring 12 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring12/Delta_Y_Strip",
                   'description': "Ring 12 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring1/331 - OT Cluster Endcap PLUS TEDD1 Ring1 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring1/Delta_X_Pixel",
                   'description': "Ring 1 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring1/Delta_Y_Pixel",
                   'description': "Ring 1 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring1/Delta_X_Strip",
                   'description': "Ring 1 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring1/Delta_Y_Strip",
                   'description': "Ring 1 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring2/331 - OT Cluster Endcap PLUS TEDD1 Ring2 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring2/Delta_X_Pixel",
                   'description': "Ring 2 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring2/Delta_Y_Pixel",
                   'description': "Ring 2 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring2/Delta_X_Strip",
                   'description': "Ring 2 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring2/Delta_Y_Strip",
                   'description': "Ring 2 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring3/332 - OT Cluster Endcap PLUS TEDD1 Ring3 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring3/Delta_X_Pixel",
                   'description': "Ring 3 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring3/Delta_Y_Pixel",
                   'description': "Ring 3 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring3/Delta_X_Strip",
                   'description': "Ring 3 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring3/Delta_Y_Strip",
                   'description': "Ring 3 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring4/333 - OT Cluster Endcap PLUS TEDD1 Ring4 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring4/Delta_X_Pixel",
                   'description': "Ring 4 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring4/Delta_Y_Pixel",
                   'description': "Ring 4 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring4/Delta_X_Strip",
                   'description': "Ring 4 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring4/Delta_Y_Strip",
                   'description': "Ring 4 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring5/334 - OT Cluster Endcap PLUS TEDD1 Ring5 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring5/Delta_X_Pixel",
                   'description': "Ring 5 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring5/Delta_Y_Pixel",
                   'description': "Ring 5 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring5/Delta_X_Strip",
                   'description': "Ring 5 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring5/Delta_Y_Strip",
                   'description': "Ring 5 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring6/335 - OT Cluster Endcap PLUS TEDD1 Ring6 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring6/Delta_X_Pixel",
                   'description': "Ring 6 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring6/Delta_Y_Pixel",
                   'description': "Ring 6 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring6/Delta_X_Strip",
                   'description': "Ring 6 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring6/Delta_Y_Strip",
                   'description': "Ring 6 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring7/336 - OT Cluster Endcap PLUS TEDD1 Ring7 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring7/Delta_X_Pixel",
                   'description': "Ring 7 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring7/Delta_Y_Pixel",
                   'description': "Ring 7 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring7/Delta_X_Strip",
                   'description': "Ring 7 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring7/Delta_Y_Strip",
                   'description': "Ring 7 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring8/337 - OT Cluster Endcap PLUS TEDD1 Ring8 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring8/Delta_X_Pixel",
                   'description': "Ring 8 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring8/Delta_Y_Pixel",
                   'description': "Ring 8 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring8/Delta_X_Strip",
                   'description': "Ring 8 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring8/Delta_Y_Strip",
                   'description': "Ring 8 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring9/338 - OT Cluster Endcap PLUS TEDD1 Ring9 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring9/Delta_X_Pixel",
                   'description': "Ring 9 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring9/Delta_Y_Pixel",
                   'description': "Ring 9 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring9/Delta_X_Strip",
                   'description': "Ring 9 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring9/Delta_Y_Strip",
                   'description': "Ring 9 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring10/339 - OT Cluster Endcap PLUS TEDD1 Ring10 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring10/Delta_X_Pixel",
                   'description': "Ring 10 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring10/Delta_Y_Pixel",
                   'description': "Ring 10 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring10/Delta_X_Strip",
                   'description': "Ring 10 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring10/Delta_Y_Strip",
                   'description': "Ring 10 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring11/340 - OT Cluster Endcap PLUS TEDD1 Ring11 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring11/Delta_X_Strip",
                   'description': "Ring 11 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring11/Delta_Y_Strip",
                   'description': "Ring 11 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring12/341 - OT Cluster Endcap PLUS TEDD1 Ring12 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring12/Delta_X_Strip",
                   'description': "Ring 12 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring12/Delta_Y_Strip",
                   'description': "Ring 12 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring13/342 - OT Cluster Endcap PLUS TEDD1 Ring13 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring13/Delta_X_Strip",
                   'description': "Ring 13 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring13/Delta_Y_Strip",
                   'description': "Ring 13 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring14/343 - OT Cluster Endcap PLUS TEDD1 Ring14 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring14/Delta_X_Strip",
                   'description': "Ring 14 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring14/Delta_Y_Strip",
                   'description': "Ring 14 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring15/344 - OT Cluster Endcap PLUS TEDD1 Ring15 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring15/Delta_X_Strip",
                   'description': "Ring 15 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring15/Delta_Y_Strip",
                   'description': "Ring 15 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2+/Ring1/345 - OT Cluster Endcap PLUS TEDD2 Ring1 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring1/Delta_X_Pixel",
                   'description': "Ring 1 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring1/Delta_Y_Pixel",
                   'description': "Ring 1 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring1/Delta_X_Strip",
                   'description': "Ring 1 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring1/Delta_Y_Strip",
                   'description': "Ring 1 Delta Y Strip"}]
                 )


phase2tkmclayout(dqmitems, "TEDD2+/Ring2/346 - OT Cluster Endcap PLUS TEDD2 Ring2 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring2/Delta_X_Pixel",
                   'description': "Ring 2 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring2/Delta_Y_Pixel",
                   'description': "Ring 2 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring2/Delta_X_Strip",
                   'description': "Ring 2 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring2/Delta_Y_Strip",
                   'description': "Ring 2 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2+/Ring3/347 - OT Cluster Endcap PLUS TEDD2 Ring3 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring3/Delta_X_Pixel",
                   'description': "Ring 3 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring3/Delta_Y_Pixel",
                   'description': "Ring 3 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring3/Delta_X_Strip",
                   'description': "Ring 3 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring3/Delta_Y_Strip",
                   'description': "Ring 3 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2+/Ring4/348 - OT Cluster Endcap PLUS TEDD2 Ring4 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring4/Delta_X_Pixel",
                   'description': "Ring 4 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring4/Delta_Y_Pixel",
                   'description': "Ring 4 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring4/Delta_X_Strip",
                   'description': "Ring 4 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring4/Delta_Y_Strip",
                   'description': "Ring 4 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2+/Ring5/349 - OT Cluster Endcap PLUS TEDD2 Ring5 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring5/Delta_X_Pixel",
                   'description': "Ring 5 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring5/Delta_Y_Pixel",
                   'description': "Ring 5 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring5/Delta_X_Strip",
                   'description': "Ring 5 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring5/Delta_Y_Strip",
                   'description': "Ring 5 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2+/Ring6/350 - OT Cluster Endcap PLUS TEDD2 Ring6 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring6/Delta_X_Pixel",
                   'description': "Ring 6 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring6/Delta_Y_Pixel",
                   'description': "Ring 6 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring6/Delta_X_Strip",
                   'description': "Ring 6 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring6/Delta_Y_Strip",
                   'description': "Ring 6 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2+/Ring7/351 - OT Cluster Endcap PLUS TEDD2 Ring7 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring7/Delta_X_Pixel",
                   'description': "Ring 7 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring7/Delta_Y_Pixel",
                   'description': "Ring 7 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring7/Delta_X_Strip",
                   'description': "Ring 7 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring7/Delta_Y_Strip",
                   'description': "Ring 7 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2+/Ring8/352 - OT Cluster Endcap PLUS TEDD2 Ring8 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring8/Delta_X_Strip",
                   'description': "Ring 8 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring8/Delta_Y_Strip",
                   'description': "Ring 8 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2+/Ring9/353 - OT Cluster Endcap PLUS TEDD2 Ring9 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring9/Delta_X_Strip",
                   'description': "Ring 9 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring9/Delta_Y_Strip",
                   'description': "Ring 9 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2+/Ring10/354 - OT Cluster Endcap PLUS TEDD2 Ring10 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring10/Delta_X_Strip",
                   'description': "Ring 10 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring10/Delta_Y_Strip",
                   'description': "Ring 10 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2+/Ring11/355 - OT Cluster Endcap PLUS TEDD2 Ring11 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring11/Delta_X_Strip",
                   'description': "Ring 11 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring11/Delta_Y_Strip",
                   'description': "Ring 11 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2+/Ring12/356 - OT Cluster Endcap PLUS TEDD2 Ring12 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring12/Delta_X_Strip",
                   'description': "Ring 12 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring12/Delta_Y_Strip",
                   'description': "Ring 12 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "400 - OT RecHit Barrel Pixel X",
                 [{'path':"TrackerPhase2OTRecHitV/Barrel/Layer1/Delta_X_Pixel",
                   'description': "Layer 1 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/Barrel/Layer2/Delta_X_Pixel",
                   'description': "Layer 2 Delta X Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/Barrel/Layer3/Delta_X_Pixel",
                   'description': "Layer 3 Delta X Pixel"}]
                 )

phase2tkmclayout(dqmitems, "401 - OT RecHit Barrel Pixel Y",
                 [{'path':"TrackerPhase2OTRecHitV/Barrel/Layer1/Delta_Y_Pixel",
                   'description': "Layer 1 Delta Y Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/Barrel/Layer2/Delta_Y_Pixel",
                   'description': "Layer 2 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/Barrel/Layer3/Delta_Y_Pixel",
                   'description': "Layer 3 Delta Y Pixel"}]
                 )

phase2tkmclayout(dqmitems, "402 - OT RecHit Barrel Strip X",
                 [{'path':"TrackerPhase2OTRecHitV/Barrel/Layer1/Delta_X_Strip",
                   'description': "Layer 1 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/Barrel/Layer2/Delta_X_Strip",
                   'description': "Layer 2 Delta X Strip"}],
                 [{'path':"TrackerPhase2OTRecHitV/Barrel/Layer3/Delta_X_Strip",
                   'description': "Layer 3 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/Barrel/Layer4/Delta_X_Strip",
                   'description': "Layer 4 Delta X Strip"}],
                 [{'path':"TrackerPhase2OTRecHitV/Barrel/Layer5/Delta_X_Strip",
                   'description': "Layer 5 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/Barrel/Layer6/Delta_X_Strip",
                   'description': "Layer 6 Delta X Strip"}]
                 )

phase2tkmclayout(dqmitems, "403 - OT RecHit Barrel Strip Y",
                 [{'path':"TrackerPhase2OTRecHitV/Barrel/Layer1/Delta_Y_Strip",
                   'description': "Layer 1 Delta Y Strip"},
                  {'path':"TrackerPhase2OTRecHitV/Barrel/Layer2/Delta_Y_Strip",
                   'description': "Layer 2 Delta Y Strip"}],
                 [{'path':"TrackerPhase2OTRecHitV/Barrel/Layer3/Delta_Y_Strip",
                   'description': "Layer 3 Delta Y Strip"},
                  {'path':"TrackerPhase2OTRecHitV/Barrel/Layer4/Delta_Y_Strip",
                   'description': "Layer 4 Delta Y Strip"}],
                 [{'path':"TrackerPhase2OTRecHitV/Barrel/Layer5/Delta_Y_Strip",
                   'description': "Layer 5 Delta Y Strip"},
                  {'path':"TrackerPhase2OTRecHitV/Barrel/Layer6/Delta_Y_Strip",
                   'description': "Layer 6 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring1/404 - OT RecHit Endcap MINUS TEDD1 Ring1 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring1/Delta_X_Pixel",
                   'description': "Ring 1 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring1/Delta_Y_Pixel",
                   'description': "Ring 1 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring1/Delta_X_Strip",
                   'description': "Ring 1 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring1/Delta_Y_Strip",
                   'description': "Ring 1 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring2/405 - OT RecHit Endcap MINUS TEDD1 Ring2 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring2/Delta_X_Pixel",
                   'description': "Ring 2 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring2/Delta_Y_Pixel",
                   'description': "Ring 2 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring2/Delta_X_Strip",
                   'description': "Ring 2 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring2/Delta_Y_Strip",
                   'description': "Ring 2 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring3/406 - OT RecHit Endcap MINUS TEDD1 Ring3 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring3/Delta_X_Pixel",
                   'description': "Ring 3 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring3/Delta_Y_Pixel",
                   'description': "Ring 3 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring3/Delta_X_Strip",
                   'description': "Ring 3 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring3/Delta_Y_Strip",
                   'description': "Ring 3 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring4/407 - OT RecHit Endcap MINUS TEDD1 Ring4 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring4/Delta_X_Pixel",
                   'description': "Ring 4 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring4/Delta_Y_Pixel",
                   'description': "Ring 4 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring4/Delta_X_Strip",
                   'description': "Ring 4 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring4/Delta_Y_Strip",
                   'description': "Ring 4 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring5/408 - OT RecHit Endcap MINUS TEDD1 Ring5 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring5/Delta_X_Pixel",
                   'description': "Ring 5 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring5/Delta_Y_Pixel",
                   'description': "Ring 5 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring5/Delta_X_Strip",
                   'description': "Ring 5 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring5/Delta_Y_Strip",
                   'description': "Ring 5 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring6/409 - OT RecHit Endcap MINUS TEDD1 Ring6 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring6/Delta_X_Pixel",
                   'description': "Ring 6 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring6/Delta_Y_Pixel",
                   'description': "Ring 6 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring6/Delta_X_Strip",
                   'description': "Ring 6 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring6/Delta_Y_Strip",
                   'description': "Ring 6 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring7/410 - OT RecHit Endcap MINUS TEDD1 Ring7 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring7/Delta_X_Pixel",
                   'description': "Ring 7 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring7/Delta_Y_Pixel",
                   'description': "Ring 7 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring7/Delta_X_Strip",
                   'description': "Ring 7 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring7/Delta_Y_Strip",
                   'description': "Ring 7 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring8/411 - OT RecHit Endcap MINUS TEDD1 Ring8 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring8/Delta_X_Pixel",
                   'description': "Ring 8 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring8/Delta_Y_Pixel",
                   'description': "Ring 8 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring8/Delta_X_Strip",
                   'description': "Ring 8 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring8/Delta_Y_Strip",
                   'description': "Ring 8 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring9/412 - OT RecHit Endcap MINUS TEDD1 Ring9 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring9/Delta_X_Pixel",
                   'description': "Ring 9 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring9/Delta_Y_Pixel",
                   'description': "Ring 9 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring9/Delta_X_Strip",
                   'description': "Ring 9 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring9/Delta_Y_Strip",
                   'description': "Ring 9 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring10/413 - OT RecHit Endcap MINUS TEDD1 Ring10 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring10/Delta_X_Pixel",
                   'description': "Ring 10 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring10/Delta_Y_Pixel",
                   'description': "Ring 10 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring10/Delta_X_Strip",
                   'description': "Ring 10 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring10/Delta_Y_Strip",
                   'description': "Ring 10 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring11/414 - OT RecHit Endcap MINUS TEDD1 Ring11 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring11/Delta_X_Strip",
                   'description': "Ring 11 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring11/Delta_Y_Strip",
                   'description': "Ring 11 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring12/415 - OT RecHit Endcap MINUS TEDD1 Ring12 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring12/Delta_X_Strip",
                   'description': "Ring 12 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring12/Delta_Y_Strip",
                   'description': "Ring 12 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring13/416 - OT RecHit Endcap MINUS TEDD1 Ring13 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring13/Delta_X_Strip",
                   'description': "Ring 13 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring13/Delta_Y_Strip",
                   'description': "Ring 13 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring14/417 - OT RecHit Endcap MINUS TEDD1 Ring14 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring14/Delta_X_Strip",
                   'description': "Ring 14 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring14/Delta_Y_Strip",
                   'description': "Ring 14 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring15/418 - OT RecHit Endcap MINUS TEDD1 Ring15 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring15/Delta_X_Strip",
                   'description': "Ring 15 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring15/Delta_Y_Strip",
                   'description': "Ring 15 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2-/Ring1/419 - OT RecHit Endcap MINUS TEDD2 Ring1 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring1/Delta_X_Pixel",
                   'description': "Ring 1 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring1/Delta_Y_Pixel",
                   'description': "Ring 1 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring1/Delta_X_Strip",
                   'description': "Ring 1 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring1/Delta_Y_Strip",
                   'description': "Ring 1 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2-/Ring2/420 - OT RecHit Endcap MINUS TEDD2 Ring2 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring2/Delta_X_Pixel",
                   'description': "Ring 2 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring2/Delta_Y_Pixel",
                   'description': "Ring 2 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring2/Delta_X_Strip",
                   'description': "Ring 2 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring2/Delta_Y_Strip",
                   'description': "Ring 2 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2-/Ring3/421 - OT RecHit Endcap MINUS TEDD2 Ring3 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring3/Delta_X_Pixel",
                   'description': "Ring 3 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring3/Delta_Y_Pixel",
                   'description': "Ring 3 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring3/Delta_X_Strip",
                   'description': "Ring 3 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring3/Delta_Y_Strip",
                   'description': "Ring 3 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2-/Ring4/422 - OT RecHit Endcap MINUS TEDD2 Ring4 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring4/Delta_X_Pixel",
                   'description': "Ring 4 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring4/Delta_Y_Pixel",
                   'description': "Ring 4 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring4/Delta_X_Strip",
                   'description': "Ring 4 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring4/Delta_Y_Strip",
                   'description': "Ring 4 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2-/Ring5/423 - OT RecHit Endcap MINUS TEDD2 Ring5 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring5/Delta_X_Pixel",
                   'description': "Ring 5 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring5/Delta_Y_Pixel",
                   'description': "Ring 5 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring5/Delta_X_Strip",
                   'description': "Ring 5 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring5/Delta_Y_Strip",
                   'description': "Ring 5 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2-/Ring6/424 - OT RecHit Endcap MINUS TEDD2 Ring6 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring6/Delta_X_Pixel",
                   'description': "Ring 6 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring6/Delta_Y_Pixel",
                   'description': "Ring 6 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring6/Delta_X_Strip",
                   'description': "Ring 6 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring6/Delta_Y_Strip",
                   'description': "Ring 6 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2-/Ring7/425 - OT RecHit Endcap MINUS TEDD2 Ring7 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring7/Delta_X_Pixel",
                   'description': "Ring 7 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring7/Delta_Y_Pixel",
                   'description': "Ring 7 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring7/Delta_X_Strip",
                   'description': "Ring 7 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring7/Delta_Y_Strip",
                   'description': "Ring 7 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2-/Ring8/426 - OT RecHit Endcap MINUS TEDD2 Ring8 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring8/Delta_X_Strip",
                   'description': "Ring 8 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring8/Delta_Y_Strip",
                   'description': "Ring 8 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2-/Ring9/427 - OT RecHit Endcap MINUS TEDD2 Ring9 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring9/Delta_X_Strip",
                   'description': "Ring 9 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring9/Delta_Y_Strip",
                   'description': "Ring 9 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2-/Ring10/428 - OT RecHit Endcap MINUS TEDD2 Ring10 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring10/Delta_X_Strip",
                   'description': "Ring 10 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring10/Delta_Y_Strip",
                   'description': "Ring 10 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2-/Ring11/429 - OT RecHit Endcap MINUS TEDD2 Ring11 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring11/Delta_X_Strip",
                   'description': "Ring 11 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring11/Delta_Y_Strip",
                   'description': "Ring 11 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2-/Ring12/430 - OT RecHit Endcap MINUS TEDD2 Ring12 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring12/Delta_X_Strip",
                   'description': "Ring 12 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring12/Delta_Y_Strip",
                   'description': "Ring 12 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring1/431 - OT RecHit Endcap PLUS TEDD1 Ring1 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring1/Delta_X_Pixel",
                   'description': "Ring 1 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring1/Delta_Y_Pixel",
                   'description': "Ring 1 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring1/Delta_X_Strip",
                   'description': "Ring 1 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring1/Delta_Y_Strip",
                   'description': "Ring 1 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring2/432 - OT RecHit Endcap PLUS TEDD1 Ring2 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring2/Delta_X_Pixel",
                   'description': "Ring 2 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring2/Delta_Y_Pixel",
                   'description': "Ring 2 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring2/Delta_X_Strip",
                   'description': "Ring 2 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring2/Delta_Y_Strip",
                   'description': "Ring 2 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring3/433 - OT RecHit Endcap PLUS TEDD1 Ring3 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring3/Delta_X_Pixel",
                   'description': "Ring 3 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring3/Delta_Y_Pixel",
                   'description': "Ring 3 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring3/Delta_X_Strip",
                   'description': "Ring 3 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring3/Delta_Y_Strip",
                   'description': "Ring 3 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring4/434 - OT RecHit Endcap PLUS TEDD1 Ring4 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring4/Delta_X_Pixel",
                   'description': "Ring 4 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring4/Delta_Y_Pixel",
                   'description': "Ring 4 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring4/Delta_X_Strip",
                   'description': "Ring 4 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring4/Delta_Y_Strip",
                   'description': "Ring 4 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring5/435 - OT RecHit Endcap PLUS TEDD1 Ring5 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring5/Delta_X_Pixel",
                   'description': "Ring 5 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring5/Delta_Y_Pixel",
                   'description': "Ring 5 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring5/Delta_X_Strip",
                   'description': "Ring 5 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring5/Delta_Y_Strip",
                   'description': "Ring 5 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring6/436 - OT RecHit Endcap PLUS TEDD1 Ring6 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring6/Delta_X_Pixel",
                   'description': "Ring 6 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring6/Delta_Y_Pixel",
                   'description': "Ring 6 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring6/Delta_X_Strip",
                   'description': "Ring 6 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring6/Delta_Y_Strip",
                   'description': "Ring 6 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring7/437 - OT RecHit Endcap PLUS TEDD1 Ring7 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring7/Delta_X_Pixel",
                   'description': "Ring 7 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring7/Delta_Y_Pixel",
                   'description': "Ring 7 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring7/Delta_X_Strip",
                   'description': "Ring 7 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring7/Delta_Y_Strip",
                   'description': "Ring 7 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring8/438 - OT RecHit Endcap PLUS TEDD1 Ring8 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring8/Delta_X_Pixel",
                   'description': "Ring 8 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring8/Delta_Y_Pixel",
                   'description': "Ring 8 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring8/Delta_X_Strip",
                   'description': "Ring 8 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring8/Delta_Y_Strip",
                   'description': "Ring 8 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring9/439 - OT RecHit Endcap PLUS TEDD1 Ring9 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring9/Delta_X_Pixel",
                   'description': "Ring 9 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring9/Delta_Y_Pixel",
                   'description': "Ring 9 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring9/Delta_X_Strip",
                   'description': "Ring 9 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring9/Delta_Y_Strip",
                   'description': "Ring 9 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring10/440 - OT RecHit Endcap PLUS TEDD1 Ring10 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring10/Delta_X_Pixel",
                   'description': "Ring 10 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring10/Delta_Y_Pixel",
                   'description': "Ring 10 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring10/Delta_X_Strip",
                   'description': "Ring 10 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring10/Delta_Y_Strip",
                   'description': "Ring 10 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring11/441 - OT RecHit Endcap PLUS TEDD1 Ring11 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring11/Delta_X_Strip",
                   'description': "Ring 11 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring11/Delta_Y_Strip",
                   'description': "Ring 11 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring12/442 - OT RecHit Endcap PLUS TEDD1 Ring12 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring12/Delta_X_Strip",
                   'description': "Ring 12 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring12/Delta_Y_Strip",
                   'description': "Ring 12 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring13/443 - OT RecHit Endcap PLUS TEDD1 Ring13 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring13/Delta_X_Strip",
                   'description': "Ring 13 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring13/Delta_Y_Strip",
                   'description': "Ring 13 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring14/444 - OT RecHit Endcap PLUS TEDD1 Ring14 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring14/Delta_X_Strip",
                   'description': "Ring 14 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring14/Delta_Y_Strip",
                   'description': "Ring 14 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring15/445 - OT RecHit Endcap PLUS TEDD1 Ring15 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring15/Delta_X_Strip",
                   'description': "Ring 15 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring15/Delta_Y_Strip",
                   'description': "Ring 15 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2+/Ring1/446 - OT RecHit Endcap PLUS TEDD2 Ring1 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring1/Delta_X_Pixel",
                   'description': "Ring 1 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring1/Delta_Y_Pixel",
                   'description': "Ring 1 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring1/Delta_X_Strip",
                   'description': "Ring 1 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring1/Delta_Y_Strip",
                   'description': "Ring 1 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2+/Ring2/447 - OT RecHit Endcap PLUS TEDD2 Ring2 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring2/Delta_X_Pixel",
                   'description': "Ring 2 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring2/Delta_Y_Pixel",
                   'description': "Ring 2 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring2/Delta_X_Strip",
                   'description': "Ring 2 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring2/Delta_Y_Strip",
                   'description': "Ring 2 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2+/Ring3/448 - OT RecHit Endcap PLUS TEDD2 Ring3 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring3/Delta_X_Pixel",
                   'description': "Ring 3 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring3/Delta_Y_Pixel",
                   'description': "Ring 3 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring3/Delta_X_Strip",
                   'description': "Ring 3 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring3/Delta_Y_Strip",
                   'description': "Ring 3 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2+/Ring4/449 - OT RecHit Endcap PLUS TEDD2 Ring4 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring4/Delta_X_Pixel",
                   'description': "Ring 4 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring4/Delta_Y_Pixel",
                   'description': "Ring 4 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring4/Delta_X_Strip",
                   'description': "Ring 4 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring4/Delta_Y_Strip",
                   'description': "Ring 4 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2+/Ring5/450 - OT RecHit Endcap PLUS TEDD2 Ring5 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring5/Delta_X_Pixel",
                   'description': "Ring 5 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring5/Delta_Y_Pixel",
                   'description': "Ring 5 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring5/Delta_X_Strip",
                   'description': "Ring 5 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring5/Delta_Y_Strip",
                   'description': "Ring 5 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2+/Ring6/451 - OT RecHit Endcap PLUS TEDD2 Ring6 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring6/Delta_X_Pixel",
                   'description': "Ring 6 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring6/Delta_Y_Pixel",
                   'description': "Ring 6 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring6/Delta_X_Strip",
                   'description': "Ring 6 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring6/Delta_Y_Strip",
                   'description': "Ring 6 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2+/Ring7/452 - OT RecHit Endcap PLUS TEDD2 Ring7 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring7/Delta_X_Pixel",
                   'description': "Ring 7 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring7/Delta_Y_Pixel",
                   'description': "Ring 7 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring7/Delta_X_Strip",
                   'description': "Ring 7 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring7/Delta_Y_Strip",
                   'description': "Ring 7 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2+/Ring8/453 - OT RecHit Endcap PLUS TEDD2 Ring8 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring8/Delta_X_Strip",
                   'description': "Ring 8 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring8/Delta_Y_Strip",
                   'description': "Ring 8 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2+/Ring9/454 - OT RecHit Endcap PLUS TEDD2 Ring9 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring9/Delta_X_Strip",
                   'description': "Ring 9 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring9/Delta_Y_Strip",
                   'description': "Ring 9 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2+/Ring10/455 - OT RecHit Endcap PLUS TEDD2 Ring10 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring10/Delta_X_Strip",
                   'description': "Ring 10 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring10/Delta_Y_Strip",
                   'description': "Ring 10 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2+/Ring11/456 - OT RecHit Endcap PLUS TEDD2 Ring11 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring11/Delta_X_Strip",
                   'description': "Ring 11 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring11/Delta_Y_Strip",
                   'description': "Ring 11 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2+/Ring12/457 - OT RecHit Endcap PLUS TEDD2 Ring12 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring12/Delta_X_Strip",
                   'description': "Ring 12 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring12/Delta_Y_Strip",
                   'description': "Ring 12 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "500 - OT TrackingRecHit Barrel Pixel X",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/Barrel/Layer1/Delta_X_Pixel",
                   'description': "Layer 1 Delta X"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/Barrel/Layer2/Delta_X_Pixel",
                   'description': "Layer 2 Delta X"}],
                 [{'path':"TrackerPhase2OTTrackingRecHitV/Barrel/Layer3/Delta_X_Pixel",
                   'description': "Layer 3 Delta X"}]
                 )

phase2tkmclayout(dqmitems, "501 - OT TrackingRecHit Barrel Pixel Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/Barrel/Layer1/Delta_Y_Pixel",
                   'description': "Layer 1 Delta Y"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/Barrel/Layer2/Delta_Y_Pixel",
                   'description': "Layer 2 Delta Y"}],
                 [{'path':"TrackerPhase2OTTrackingRecHitV/Barrel/Layer3/Delta_Y_Pixel",
                   'description': "Layer 3 Delta Y"}]
                 )

phase2tkmclayout(dqmitems, "502 - OT TrackingRecHit Barrel Strip X",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/Barrel/Layer1/Delta_X_Strip",
                   'description': "Layer 1 Delta X"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/Barrel/Layer2/Delta_X_Strip",
                   'description': "Layer 2 Delta X"}],
                 [{'path':"TrackerPhase2OTTrackingRecHitV/Barrel/Layer3/Delta_X_Strip",
                   'description': "Layer 3 Delta X"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/Barrel/Layer4/Delta_X_Strip",
                   'description': "Layer 4 Delta X"}],
                 [{'path':"TrackerPhase2OTTrackingRecHitV/Barrel/Layer5/Delta_X_Strip",
                   'description': "Layer 5 Delta X"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/Barrel/Layer6/Delta_X_Strip",
                   'description': "Layer 6 Delta X"}]
                 )

phase2tkmclayout(dqmitems, "503 - OT TrackingRecHit Barrel Strip Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/Barrel/Layer1/Delta_Y_Strip",
                   'description': "Layer 1 Delta Y"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/Barrel/Layer2/Delta_Y_Strip",
                   'description': "Layer 2 Delta Y"}],
                 [{'path':"TrackerPhase2OTTrackingRecHitV/Barrel/Layer3/Delta_Y_Strip",
                   'description': "Layer 3 Delta Y"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/Barrel/Layer4/Delta_Y_Strip",
                   'description': "Layer 4 Delta Y"}],
                 [{'path':"TrackerPhase2OTTrackingRecHitV/Barrel/Layer5/Delta_Y_Strip",
                   'description': "Layer 5 Delta Y"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/Barrel/Layer6/Delta_Y_Strip",
                   'description': "Layer 6 Delta Y"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring1/504 - OT TrackingRecHit Endcap MINUS TEDD1 Ring1 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring1/Delta_X_Pixel",
                   'description': "Ring 1 Delta X Pixel"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring1/Delta_Y_Pixel",
                   'description': "Ring 1 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring1/Delta_X_Strip",
                   'description': "Ring 1 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring1/Delta_Y_Strip",
                   'description': "Ring 1 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring2/505 - OT TrackingRecHit Endcap MINUS TEDD1 Ring2 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring2/Delta_X_Pixel",
                   'description': "Ring 2 Delta X Pixel"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring2/Delta_Y_Pixel",
                   'description': "Ring 2 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring2/Delta_X_Strip",
                   'description': "Ring 2 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring2/Delta_Y_Strip",
                   'description': "Ring 2 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring3/506 - OT TrackingRecHit Endcap MINUS TEDD1 Ring3 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring3/Delta_X_Pixel",
                   'description': "Ring 3 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring3/Delta_Y_Pixel",
                   'description': "Ring 3 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring3/Delta_X_Strip",
                   'description': "Ring 3 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring3/Delta_Y_Strip",
                   'description': "Ring 3 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring4/507 - OT TrackingRecHit Endcap MINUS TEDD1 Ring4 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring4/Delta_X_Pixel",
                   'description': "Ring 4 Delta X Pixel"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring4/Delta_Y_Pixel",
                   'description': "Ring 4 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring4/Delta_X_Strip",
                   'description': "Ring 4 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring4/Delta_Y_Strip",
                   'description': "Ring 4 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring5/508 - OT TrackingRecHit Endcap MINUS TEDD1 Ring5 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring5/Delta_X_Pixel",
                   'description': "Ring 5 Delta X Pixel"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring5/Delta_Y_Pixel",
                   'description': "Ring 5 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring5/Delta_X_Strip",
                   'description': "Ring 5 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring5/Delta_Y_Strip",
                   'description': "Ring 5 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring6/509 - OT TrackingRecHit Endcap MINUS TEDD1 Ring6 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring6/Delta_X_Pixel",
                   'description': "Ring 6 Delta X Pixel"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring6/Delta_Y_Pixel",
                   'description': "Ring 6 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring6/Delta_X_Strip",
                   'description': "Ring 6 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring6/Delta_Y_Strip",
                   'description': "Ring 6 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring7/510 - OT TrackingRecHit Endcap MINUS TEDD1 Ring7 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring7/Delta_X_Pixel",
                   'description': "Ring 7 Delta X Pixel"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring7/Delta_Y_Pixel",
                   'description': "Ring 7 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring7/Delta_X_Strip",
                   'description': "Ring 7 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring7/Delta_Y_Strip",
                   'description': "Ring 7 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring8/511 - OT TrackingRecHit Endcap MINUS TEDD1 Ring8 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring8/Delta_X_Pixel",
                   'description': "Ring 8 Delta X Pixel"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring8/Delta_Y_Pixel",
                   'description': "Ring 8 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring8/Delta_X_Strip",
                   'description': "Ring 8 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring8/Delta_Y_Strip",
                   'description': "Ring 8 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring9/512 - OT TrackingRecHit Endcap MINUS TEDD1 Ring9 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring9/Delta_X_Pixel",
                   'description': "Ring 9 Delta X Pixel"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring9/Delta_Y_Pixel",
                   'description': "Ring 9 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring9/Delta_X_Strip",
                   'description': "Ring 9 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring9/Delta_Y_Strip",
                   'description': "Ring 9 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring10/513 - OT TrackingRecHit Endcap MINUS TEDD1 Ring10 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring10/Delta_X_Pixel",
                   'description': "Ring 10 Delta X Pixel"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring10/Delta_Y_Pixel",
                   'description': "Ring 10 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring10/Delta_X_Strip",
                   'description': "Ring 10 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring10/Delta_Y_Strip",
                   'description': "Ring 10 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring11/514 - OT TrackingRecHit Endcap MINUS TEDD1 Ring11 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring11/Delta_X_Strip",
                   'description': "Ring 11 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring11/Delta_Y_Strip",
                   'description': "Ring 11 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring12/515 - OT TrackingRecHit Endcap MINUS TEDD1 Ring12 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring12/Delta_X_Strip",
                   'description': "Ring 12 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring12/Delta_Y_Strip",
                   'description': "Ring 12 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring13/516 - OT TrackingRecHit Endcap MINUS TEDD1 Ring13 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring13/Delta_X_Strip",
                   'description': "Ring 13 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring13/Delta_Y_Strip",
                   'description': "Ring 13 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring14/517 - OT TrackingRecHit Endcap MINUS TEDD1 Ring14 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring14/Delta_X_Strip",
                   'description': "Ring 14 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring14/Delta_Y_Strip",
                   'description': "Ring 14 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1-/Ring15/518 - OT TrackingRecHit Endcap MINUS TEDD1 Ring15 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring15/Delta_X_Strip",
                   'description': "Ring 15 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_1/Ring15/Delta_Y_Strip",
                   'description': "Ring 15 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2-/Ring1/519 - OT TrackingRecHit Endcap MINUS TEDD2 Ring1 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_2/Ring1/Delta_X_Pixel",
                   'description': "Ring 1 Delta X Pixel"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_2/Ring1/Delta_Y_Pixel",
                   'description': "Ring 1 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_2/Ring1/Delta_X_Strip",
                   'description': "Ring 1 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_2/Ring1/Delta_Y_Strip",
                   'description': "Ring 1 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2-/Ring2/520 - OT TrackingRecHit Endcap MINUS TEDD2 Ring2 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_2/Ring2/Delta_X_Pixel",
                   'description': "Ring 2 Delta X Pixel"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_2/Ring2/Delta_Y_Pixel",
                   'description': "Ring 2 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_2/Ring2/Delta_X_Strip",
                   'description': "Ring 2 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_2/Ring2/Delta_Y_Strip",
                   'description': "Ring 2 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2-/Ring3/521 - OT TrackingRecHit Endcap MINUS TEDD2 Ring3 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_2/Ring3/Delta_X_Pixel",
                   'description': "Ring 3 Delta X Pixel"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_2/Ring3/Delta_Y_Pixel",
                   'description': "Ring 3 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_2/Ring3/Delta_X_Strip",
                   'description': "Ring 3 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_2/Ring3/Delta_Y_Strip",
                   'description': "Ring 3 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2-/Ring4/522 - OT TrackingRecHit Endcap MINUS TEDD2 Ring4 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_2/Ring4/Delta_X_Pixel",
                   'description': "Ring 4 Delta X Pixel"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_2/Ring4/Delta_Y_Pixel",
                   'description': "Ring 4 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_2/Ring4/Delta_X_Strip",
                   'description': "Ring 4 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_2/Ring4/Delta_Y_Strip",
                   'description': "Ring 4 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2-/Ring5/523 - OT TrackingRecHit Endcap MINUS TEDD2 Ring5 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_2/Ring5/Delta_X_Pixel",
                   'description': "Ring 5 Delta X Pixel"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_2/Ring5/Delta_Y_Pixel",
                   'description': "Ring 5 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_2/Ring5/Delta_X_Strip",
                   'description': "Ring 5 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_2/Ring5/Delta_Y_Strip",
                   'description': "Ring 5 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2-/Ring6/524 - OT TrackingRecHit Endcap MINUS TEDD2 Ring6 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_2/Ring6/Delta_X_Pixel",
                   'description': "Ring 6 Delta X Pixel"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_2/Ring6/Delta_Y_Pixel",
                   'description': "Ring 6 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_2/Ring6/Delta_X_Strip",
                   'description': "Ring 6 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_2/Ring6/Delta_Y_Strip",
                   'description': "Ring 6 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2-/Ring7/525 - OT TrackingRecHit Endcap MINUS TEDD2 Ring7 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_2/Ring7/Delta_X_Pixel",
                   'description': "Ring 7 Delta X Pixel"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_2/Ring7/Delta_Y_Pixel",
                   'description': "Ring 7 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_2/Ring7/Delta_X_Strip",
                   'description': "Ring 7 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_2/Ring7/Delta_Y_Strip",
                   'description': "Ring 7 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2-/Ring8/526 - OT TrackingRecHit Endcap MINUS TEDD2 Ring8 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_2/Ring8/Delta_X_Strip",
                   'description': "Ring 8 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_2/Ring8/Delta_Y_Strip",
                   'description': "Ring 8 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2-/Ring9/527 - OT TrackingRecHit Endcap MINUS TEDD2 Ring9 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_2/Ring9/Delta_X_Strip",
                   'description': "Ring 9 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_2/Ring9/Delta_Y_Strip",
                   'description': "Ring 9 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2-/Ring10/528 - OT TrackingRecHit Endcap MINUS TEDD2 Ring10 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_2/Ring10/Delta_X_Strip",
                   'description': "Ring 10 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_2/Ring10/Delta_Y_Strip",
                   'description': "Ring 10 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2-/Ring11/529 - OT TrackingRecHit Endcap MINUS TEDD2 Ring11 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_2/Ring11/Delta_X_Strip",
                   'description': "Ring 11 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_2/Ring11/Delta_Y_Strip",
                   'description': "Ring 11 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2-/Ring12/530 - OT TrackingRecHit Endcap MINUS TEDD2 Ring12 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_2/Ring12/Delta_X_Strip",
                   'description': "Ring 12 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side1/TEDD_2/Ring12/Delta_Y_Strip",
                   'description': "Ring 12 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring1/531 - OT TrackingRecHit Endcap PLUS TEDD1 Ring1 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring1/Delta_X_Pixel",
                   'description': "Ring 1 Delta X Pixel"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring1/Delta_Y_Pixel",
                   'description': "Ring 1 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring1/Delta_X_Strip",
                   'description': "Ring 1 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring1/Delta_Y_Strip",
                   'description': "Ring 1 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring2/532 - OT TrackingRecHit Endcap PLUS TEDD1 Ring2 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring2/Delta_X_Pixel",
                   'description': "Ring 2 Delta X Pixel"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring2/Delta_Y_Pixel",
                   'description': "Ring 2 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring2/Delta_X_Strip",
                   'description': "Ring 2 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring2/Delta_Y_Strip",
                   'description': "Ring 2 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring3/533 - OT TrackingRecHit Endcap PLUS TEDD1 Ring3 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring3/Delta_X_Pixel",
                   'description': "Ring 3 Delta X Pixel"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring3/Delta_Y_Pixel",
                   'description': "Ring 3 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring3/Delta_X_Strip",
                   'description': "Ring 3 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring3/Delta_Y_Strip",
                   'description': "Ring 3 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring4/534 - OT TrackingRecHit Endcap PLUS TEDD1 Ring4 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring4/Delta_X_Pixel",
                   'description': "Ring 4 Delta X Pixel"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring4/Delta_Y_Pixel",
                   'description': "Ring 4 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring4/Delta_X_Strip",
                   'description': "Ring 4 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring4/Delta_Y_Strip",
                   'description': "Ring 4 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring5/535 - OT TrackingRecHit Endcap PLUS TEDD1 Ring5 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring5/Delta_X_Pixel",
                   'description': "Ring 5 Delta X Pixel"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring5/Delta_Y_Pixel",
                   'description': "Ring 5 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring5/Delta_X_Strip",
                   'description': "Ring 5 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring5/Delta_Y_Strip",
                   'description': "Ring 5 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring6/536 - OT TrackingRecHit Endcap PLUS TEDD1 Ring6 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring6/Delta_X_Pixel",
                   'description': "Ring 6 Delta X Pixel"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring6/Delta_Y_Pixel",
                   'description': "Ring 6 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring6/Delta_X_Strip",
                   'description': "Ring 6 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring6/Delta_Y_Strip",
                   'description': "Ring 6 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring7/537 - OT TrackingRecHit Endcap PLUS TEDD1 Ring7 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring7/Delta_X_Pixel",
                   'description': "Ring 7 Delta X Pixel"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring7/Delta_Y_Pixel",
                   'description': "Ring 7 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring7/Delta_X_Strip",
                   'description': "Ring 7 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring7/Delta_Y_Strip",
                   'description': "Ring 7 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring8/538 - OT TrackingRecHit Endcap PLUS TEDD1 Ring8 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring8/Delta_X_Pixel",
                   'description': "Ring 8 Delta X Pixel"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring8/Delta_Y_Pixel",
                   'description': "Ring 8 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring8/Delta_X_Strip",
                   'description': "Ring 8 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring8/Delta_Y_Strip",
                   'description': "Ring 8 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring9/539 - OT TrackingRecHit Endcap PLUS TEDD1 Ring9 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring9/Delta_X_Pixel",
                   'description': "Ring 9 Delta X Pixel"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring9/Delta_Y_Pixel",
                   'description': "Ring 9 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring9/Delta_X_Strip",
                   'description': "Ring 9 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring9/Delta_Y_Strip",
                   'description': "Ring 9 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring10/540 - OT TrackingRecHit Endcap PLUS TEDD1 Ring10 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring10/Delta_X_Pixel",
                   'description': "Ring 10 Delta X Pixel"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring10/Delta_Y_Pixel",
                   'description': "Ring 10 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring10/Delta_X_Strip",
                   'description': "Ring 10 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring10/Delta_Y_Strip",
                   'description': "Ring 10 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring11/541 - OT TrackingRecHit Endcap PLUS TEDD1 Ring11 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring11/Delta_X_Strip",
                   'description': "Ring 11 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring11/Delta_Y_Strip",
                   'description': "Ring 11 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring12/542 - OT TrackingRecHit Endcap PLUS TEDD1 Ring12 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring12/Delta_X_Strip",
                   'description': "Ring 12 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring12/Delta_Y_Strip",
                   'description': "Ring 12 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring13/543 - OT TrackingRecHit Endcap PLUS TEDD1 Ring13 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring13/Delta_X_Strip",
                   'description': "Ring 13 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring13/Delta_Y_Strip",
                   'description': "Ring 13 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring14/544 - OT TrackingRecHit Endcap PLUS TEDD1 Ring14 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring14/Delta_X_Strip",
                   'description': "Ring 14 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring14/Delta_Y_Strip",
                   'description': "Ring 14 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD1+/Ring15/545 - OT TrackingRecHit Endcap PLUS TEDD1 Ring15 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring15/Delta_X_Strip",
                   'description': "Ring 15 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_1/Ring15/Delta_Y_Strip",
                   'description': "Ring 15 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2+/Ring1/546 - OT TrackingRecHit Endcap PLUS TEDD2 Ring1 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_2/Ring1/Delta_X_Pixel",
                   'description': "Ring 1 Delta X Pixel"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_2/Ring1/Delta_Y_Pixel",
                   'description': "Ring 1 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_2/Ring1/Delta_X_Strip",
                   'description': "Ring 1 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_2/Ring1/Delta_Y_Strip",
                   'description': "Ring 1 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2+/Ring2/547 - OT TrackingRecHit Endcap PLUS TEDD2 Ring2 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_2/Ring2/Delta_X_Pixel",
                   'description': "Ring 2 Delta X Pixel"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_2/Ring2/Delta_Y_Pixel",
                   'description': "Ring 2 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_2/Ring2/Delta_X_Strip",
                   'description': "Ring 2 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_2/Ring2/Delta_Y_Strip",
                   'description': "Ring 2 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2+/Ring3/548 - OT TrackingRecHit Endcap PLUS TEDD2 Ring3 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_2/Ring3/Delta_X_Pixel",
                   'description': "Ring 3 Delta X Pixel"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_2/Ring3/Delta_Y_Pixel",
                   'description': "Ring 3 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_2/Ring3/Delta_X_Strip",
                   'description': "Ring 3 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_2/Ring3/Delta_Y_Strip",
                   'description': "Ring 3 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2+/Ring4/549 - OT TrackingRecHit Endcap PLUS TEDD2 Ring4 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_2/Ring4/Delta_X_Pixel",
                   'description': "Ring 4 Delta X Pixel"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_2/Ring4/Delta_Y_Pixel",
                   'description': "Ring 4 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_2/Ring4/Delta_X_Strip",
                   'description': "Ring 4 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_2/Ring4/Delta_Y_Strip",
                   'description': "Ring 4 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2+/Ring5/550 - OT TrackingRecHit Endcap PLUS TEDD2 Ring5 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_2/Ring5/Delta_X_Pixel",
                   'description': "Ring 5 Delta X Pixel"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_2/Ring5/Delta_Y_Pixel",
                   'description': "Ring 5 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_2/Ring5/Delta_X_Strip",
                   'description': "Ring 5 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_2/Ring5/Delta_Y_Strip",
                   'description': "Ring 5 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2+/Ring6/551 - OT TrackingRecHit Endcap PLUS TEDD2 Ring6 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_2/Ring6/Delta_X_Pixel",
                   'description': "Ring 6 Delta X Pixel"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_2/Ring6/Delta_Y_Pixel",
                   'description': "Ring 6 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_2/Ring6/Delta_X_Strip",
                   'description': "Ring 6 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_2/Ring6/Delta_Y_Strip",
                   'description': "Ring 6 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2+/Ring7/552 - OT TrackingRecHit Endcap PLUS TEDD2 Ring7 Pixel and Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_2/Ring7/Delta_X_Pixel",
                   'description': "Ring 7 Delta X Pixel"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_2/Ring7/Delta_Y_Pixel",
                   'description': "Ring 7 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_2/Ring7/Delta_X_Strip",
                   'description': "Ring 7 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_2/Ring7/Delta_Y_Strip",
                   'description': "Ring 7 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2+/Ring8/553 - OT TrackingRecHit Endcap PLUS TEDD2 Ring8 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_2/Ring8/Delta_X_Strip",
                   'description': "Ring 8 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_2/Ring8/Delta_Y_Strip",
                   'description': "Ring 8 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2+/Ring9/554 - OT TrackingRecHit Endcap PLUS TEDD2 Ring9 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_2/Ring9/Delta_X_Strip",
                   'description': "Ring 9 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_2/Ring9/Delta_Y_Strip",
                   'description': "Ring 9 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2+/Ring10/555 - OT TrackingRecHit Endcap PLUS TEDD2 Ring10 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_2/Ring10/Delta_X_Strip",
                   'description': "Ring 10 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_2/Ring10/Delta_Y_Strip",
                   'description': "Ring 10 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2+/Ring11/556 - OT TrackingRecHit Endcap PLUS TEDD2 Ring11 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_2/Ring11/Delta_X_Strip",
                   'description': "Ring 11 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_2/Ring11/Delta_Y_Strip",
                   'description': "Ring 11 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "TEDD2+/Ring12/557 - OT TrackingRecHit Endcap PLUS TEDD2 Ring12 Strip Delta X and Y",
                 [{'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_2/Ring12/Delta_X_Strip",
                   'description': "Ring 12 Delta X Strip"},
                  {'path':"TrackerPhase2OTTrackingRecHitV/EndCap_Side2/TEDD_2/Ring12/Delta_Y_Strip",
                   'description': "Ring 12 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "600 - OT L1Track Eta Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Nominal_L1TF/FinalEfficiency/EtaEfficiency",
                   'description': "Eta Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/Nominal_L1TF/FinalResolution/EtaResolution",
                   'description': "Eta Resolution"}]
                 )

phase2tkmclayout(dqmitems, "601 - OT L1Track Phi Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Nominal_L1TF/FinalResolution/PhiResolution",
                   'description': "Phi Resolution"}]
                 )

phase2tkmclayout(dqmitems, "602 - OT L1Track Lxy Efficiency",
                 [{'path':"TrackerPhase2OTL1TrackV/Nominal_L1TF/FinalEfficiency/LxyEfficiency",
                   'description': "Lxy Efficiency"}]
                 )

phase2tkmclayout(dqmitems, "603 - OT L1Track d0 Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Nominal_L1TF/FinalEfficiency/d0Efficiency",
                   'description': "d0 Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/Nominal_L1TF/FinalResolution/d0Resolution",
                   'description': "d0 Resolution"}]
                 )

phase2tkmclayout(dqmitems, "604 - OT L1Track z0 Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Nominal_L1TF/FinalEfficiency/z0Efficiency",
                   'description': "z0 Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/Nominal_L1TF/FinalResolution/z0Resolution",
                   'description': "z0 Resolution"}]
                 )

phase2tkmclayout(dqmitems, "605 - OT Extended L1Track Displaced Eta Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Displaced/FinalEfficiency/EtaEfficiency",
                   'description': "Eta Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Displaced/FinalResolution/EtaResolution_displaced",
                   'description': "Eta Resolution"}]
                 )

phase2tkmclayout(dqmitems, "606 - OT Extended L1Track Displaced Phi Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Displaced/FinalResolution/PhiResolution_displaced",
                   'description': "Phi Resolution"}]
                 )

phase2tkmclayout(dqmitems, "607 - OT Extended L1Track Displaced Lxy Efficiency",
                 [{'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Displaced/FinalEfficiency/LxyEfficiency",
                   'description': "Lxy Efficiency"}]
                 )

phase2tkmclayout(dqmitems, "608 - OT Extended L1Track Displaced d0 Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Displaced/FinalEfficiency/d0Efficiency",
                   'description': "d0 Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Displaced/FinalResolution/d0Resolution_displaced",
                   'description': "d0 Resolution"}]
                 )

phase2tkmclayout(dqmitems, "609 - OT Extended L1Track Prompt Eta Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Prompt/FinalEfficiency/EtaEfficiency",
                   'description': "Eta Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Prompt/FinalResolution/EtaResolution_prompt",
                   'description': "Eta Resolution"}]
                 )

phase2tkmclayout(dqmitems, "610 - OT Extended L1Track Prompt Phi Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Prompt/FinalResolution/PhiResolution_prompt",
                   'description': "Phi Resolution"}]
                 )

phase2tkmclayout(dqmitems, "611 - OT Extended L1Track Prompt Lxy Efficiency",
                 [{'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Prompt/FinalEfficiency/LxyEfficiency",
                   'description': "Lxy Efficiency"}]
                 )

phase2tkmclayout(dqmitems, "612 - OT Extended L1Track Prompt d0 Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Prompt/FinalEfficiency/d0Efficiency",
                   'description': "d0 Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Prompt/FinalResolution/d0Resolution_prompt",
                   'description': "d0 Resolution"}]
                 )

