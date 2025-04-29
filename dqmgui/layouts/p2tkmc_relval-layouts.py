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

phase2tkmclayout(dqmitems, "304 - OT Cluster Endcap MINUS TEDD1 Pixel and Strip XY",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring1/Delta_X_Pixel",
                   'description': "Ring 1 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring1/Delta_Y_Pixel",
                   'description': "Ring 1 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring1/Delta_X_Strip",
                   'description': "Ring 1 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring1/Delta_Y_Strip",
                   'description': "Ring 1 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "305 - OT Cluster Endcap MINUS TEDD2 Pixel and Strip XY",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring1/Delta_X_Pixel",
                   'description': "Ring 1 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring1/Delta_Y_Pixel",
                   'description': "Ring 1 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring1/Delta_X_Strip",
                   'description': "Ring 1 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring1/Delta_Y_Strip",
                   'description': "Ring 1 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "306 - OT Cluster Endcap PLUS TEDD1 Pixel and Strip XY",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring1/Delta_X_Pixel",
                   'description': "Ring 1 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring1/Delta_Y_Pixel",
                   'description': "Ring 1 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring1/Delta_X_Strip",
                   'description': "Ring 1 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring1/Delta_Y_Strip",
                   'description': "Ring 1 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "307 - OT Cluster Endcap PLUS TEDD2 Pixel and Strip XY",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring1/Delta_X_Pixel",
                   'description': "Ring 1 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring1/Delta_Y_Pixel",
                   'description': "Ring 1 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring1/Delta_X_Strip",
                   'description': "Ring 1 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring1/Delta_Y_Strip",
                   'description': "Ring 1 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "400 - OT L1Track Eta Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Nominal_L1TF/FinalEfficiency/EtaEfficiency",
                   'description': "Eta Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/Nominal_L1TF/FinalResolution/EtaResolution",
                   'description': "Eta Resolution"}]
                 )

phase2tkmclayout(dqmitems, "401 - OT L1Track Phi Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Nominal_L1TF/FinalEfficiency/PhiEfficiency",
                   'description': "Phi Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/Nominal_L1TF/FinalResolution/PhiResolution",
                   'description': "Phi Resolution"}]
                 )

phase2tkmclayout(dqmitems, "402 - OT L1Track Lxy Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Nominal_L1TF/FinalEfficiency/LxyEfficiency",
                   'description': "Lxy Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/Nominal_L1TF/FinalResolution/LxyResolution",
                   'description': "Lxy Resolution"}]
                 )

phase2tkmclayout(dqmitems, "403 - OT L1Track d0 Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Nominal_L1TF/FinalEfficiency/d0Efficiency",
                   'description': "d0 Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/Nominal_L1TF/FinalResolution/d0Resolution",
                   'description': "d0 Resolution"}]
                 )

phase2tkmclayout(dqmitems, "404 - OT L1Track z0 Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Nominal_L1TF/FinalEfficiency/z0Efficiency",
                   'description': "z0 Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/Nominal_L1TF/FinalResolution/z0Resolution",
                   'description': "z0 Resolution"}]
                 )

phase2tkmclayout(dqmitems, "405 - OT Extended L1Track Displaced Eta Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Displaced/FinalEfficiency/EtaEfficiency",
                   'description': "Eta Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Displaced/FinalResolution/EtaResolution",
                   'description': "Eta Resolution"}]
                 )

phase2tkmclayout(dqmitems, "406 - OT Extended L1Track Displaced Phi Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Displaced/FinalEfficiency/PhiEfficiency",
                   'description': "Phi Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Displaced/FinalResolution/PhiResolution",
                   'description': "Phi Resolution"}]
                 )

phase2tkmclayout(dqmitems, "407 - OT Extended L1Track Displaced Lxy Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Displaced/FinalEfficiency/LxyEfficiency",
                   'description': "Lxy Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Displaced/FinalResolution/LxyResolution",
                   'description': "Lxy Resolution"}]
                 )

phase2tkmclayout(dqmitems, "408 - OT Extended L1Track Displaced d0 Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Displaced/FinalEfficiency/d0Efficiency",
                   'description': "d0 Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Displaced/FinalResolution/d0Resolution",
                   'description': "d0 Resolution"}]
                 )

phase2tkmclayout(dqmitems, "409 - OT Extended L1Track Prompt Eta Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Prompt/FinalEfficiency/EtaEfficiency",
                   'description': "Eta Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Prompt/FinalResolution/EtaResolution",
                   'description': "Eta Resolution"}]
                 )

phase2tkmclayout(dqmitems, "410 - OT Extended L1Track Prompt Phi Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Prompt/FinalEfficiency/PhiEfficiency",
                   'description': "Phi Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Prompt/FinalResolution/PhiResolution",
                   'description': "Phi Resolution"}]
                 )

phase2tkmclayout(dqmitems, "411 - OT Extended L1Track Prompt Lxy Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Prompt/FinalEfficiency/LxyEfficiency",
                   'description': "Lxy Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Prompt/FinalResolution/LxyResolution",
                   'description': "Lxy Resolution"}]
                 )

phase2tkmclayout(dqmitems, "412 - OT Extended L1Track Prompt d0 Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Prompt/FinalEfficiency/d0Efficiency",
                   'description': "d0 Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Prompt/FinalResolution/d0Resolution",
                   'description': "d0 Resolution"}]
                 )

phase2tkmclayout(dqmitems, "500 - OT RecHit Barrel Pixel X",
                 [{'path':"TrackerPhase2OTRecHitV/Barrel/Layer1/Delta_X_Pixel",
                   'description': "Layer 1 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/Barrel/Layer2/Delta_X_Pixel",
                   'description': "Layer 2 Delta X Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/Barrel/Layer3/Delta_X_Pixel",
                   'description': "Layer 3 Delta X Pixel"}]
                 )

phase2tkmclayout(dqmitems, "501 - OT RecHit Barrel Pixel Y",
                 [{'path':"TrackerPhase2OTRecHitV/Barrel/Layer1/Delta_Y_Pixel",
                   'description': "Layer 1 Delta Y Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/Barrel/Layer2/Delta_Y_Pixel",
                   'description': "Layer 2 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/Barrel/Layer3/Delta_Y_Pixel",
                   'description': "Layer 3 Delta Y Pixel"}]
                 )

phase2tkmclayout(dqmitems, "502 - OT RecHit Barrel Strip X",
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

phase2tkmclayout(dqmitems, "503 - OT RecHit Barrel Strip Y",
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

phase2tkmclayout(dqmitems, "504 - OT RecHit Endcap MINUS TEDD1 Pixel and Strip XY",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring1/Delta_X_Pixel",
                   'description': "Ring 1 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring1/Delta_Y_Pixel",
                   'description': "Ring 1 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring1/Delta_X_Strip",
                   'description': "Ring 1 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring1/Delta_Y_Strip",
                   'description': "Ring 1 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "505 - OT RecHit Endcap MINUS TEDD2 Pixel and Strip XY",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring1/Delta_X_Pixel",
                   'description': "Ring 1 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring1/Delta_Y_Pixel",
                   'description': "Ring 1 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring1/Delta_X_Strip",
                   'description': "Ring 1 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring1/Delta_Y_Strip",
                   'description': "Ring 1 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "506 - OT RecHit Endcap PLUS TEDD1 Pixel and Strip XY",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring1/Delta_X_Pixel",
                   'description': "Ring 1 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring1/Delta_Y_Pixel",
                   'description': "Ring 1 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring1/Delta_X_Strip",
                   'description': "Ring 1 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring1/Delta_Y_Strip",
                   'description': "Ring 1 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "507 - OT RecHit Endcap PLUS TEDD2 Pixel and Strip XY",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring1/Delta_X_Pixel",
                   'description': "Ring 1 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring1/Delta_Y_Pixel",
                   'description': "Ring 1 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring1/Delta_X_Strip",
                   'description': "Ring 1 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring1/Delta_Y_Strip",
                   'description': "Ring 1 Delta Y Strip"}]
                 )