def phase2tkmclayout(i, p, *rows): i["MCLayouts/Phase2Tk/" + p] = DQMItem(layout=rows)

phase2tkmclayout(dqmitems, "00 - IT Cluster Barrel X",
                 [{'path':"TrackerPhase2ITClusterV/Barrel/Layer1/Delta_X_Pixel",
                   'description': "Layer 1 Delta X Pixel"},
                  {'path':"TrackerPhase2ITClusterV/Barrel/Layer2/Delta_X_Pixel",
                   'description': "Layer 2 Delta X Pixel"}],
                 [{'path':"TrackerPhase2ITClusterV/Barrel/Layer3/Delta_X_Pixel",
                   'description': "Layer 3 Delta X Pixel"},
                  {'path':"TrackerPhase2ITClusterV/Barrel/Layer4/Delta_X_Pixel",
                   'description': "Layer 4 Delta X Pixel"}]
                 )

phase2tkmclayout(dqmitems, "01 - IT Cluster Barrel Y",
                 [{'path':"TrackerPhase2ITClusterV/Barrel/Layer1/Delta_Y_Pixel",
                   'description': "Layer 1 Delta Y Pixel"},
                  {'path':"TrackerPhase2ITClusterV/Barrel/Layer2/Delta_Y_Pixel",
                   'description': "Layer 2 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2ITClusterV/Barrel/Layer3/Delta_Y_Pixel",
                   'description': "Layer 3 Delta Y Pixel"},
                  {'path':"TrackerPhase2ITClusterV/Barrel/Layer4/Delta_Y_Pixel",
                   'description': "Layer 4 Delta Y Pixel"}]
                 )

phase2tkmclayout(dqmitems, "02 - IT Cluster Endcap MINUS EPix X",
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

phase2tkmclayout(dqmitems, "03 - IT Cluster Endcap MINUS EPix Y",
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

phase2tkmclayout(dqmitems, "04 - IT Cluster Endcap MINUS FPix X",
                 [{'path':"TrackerPhase2ITClusterV/EndCap_Side1/FPix/Ring1/Delta_X_Pixel",
                   'description': "Ring 1 Delta X Pixel"},
                  {'path':"TrackerPhase2ITClusterV/EndCap_Side1/FPix/Ring2/Delta_X_Pixel",
                   'description': "Ring 2 Delta X Pixel"}],
                 [{'path':"TrackerPhase2ITClusterV/EndCap_Side1/FPix/Ring3/Delta_X_Pixel",
                   'description': "Ring 3 Delta X Pixel"},
                  {'path':"TrackerPhase2ITClusterV/EndCap_Side1/FPix/Ring4/Delta_X_Pixel",
                   'description': "Ring 4 Delta X Pixel"}]
                 )

phase2tkmclayout(dqmitems, "05 - IT Cluster Endcap MINUS FPix Y",
                 [{'path':"TrackerPhase2ITClusterV/EndCap_Side1/FPix/Ring1/Delta_Y_Pixel",
                   'description': "Ring 1 Delta Y Pixel"},
                  {'path':"TrackerPhase2ITClusterV/EndCap_Side1/FPix/Ring2/Delta_Y_Pixel",
                   'description': "Ring 2 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2ITClusterV/EndCap_Side1/FPix/Ring3/Delta_Y_Pixel",
                   'description': "Ring 3 Delta Y Pixel"},
                  {'path':"TrackerPhase2ITClusterV/EndCap_Side1/FPix/Ring4/Delta_Y_Pixel",
                   'description': "Ring 4 Delta Y Pixel"}]
                 )

phase2tkmclayout(dqmitems, "06 - IT Cluster Endcap PLUS EPix X",
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

phase2tkmclayout(dqmitems, "07 - IT Cluster Endcap PLUS EPix Y",
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

phase2tkmclayout(dqmitems, "08 - IT Cluster Endcap PLUS FPix X",
                 [{'path':"TrackerPhase2ITClusterV/EndCap_Side2/FPix/Ring1/Delta_X_Pixel",
                   'description': "Ring 1 Delta X Pixel"},
                  {'path':"TrackerPhase2ITClusterV/EndCap_Side2/FPix/Ring2/Delta_X_Pixel",
                   'description': "Ring 2 Delta X Pixel"}],
                 [{'path':"TrackerPhase2ITClusterV/EndCap_Side2/FPix/Ring3/Delta_X_Pixel",
                   'description': "Ring 3 Delta X Pixel"},
                  {'path':"TrackerPhase2ITClusterV/EndCap_Side2/FPix/Ring4/Delta_X_Pixel",
                   'description': "Ring 4 Delta X Pixel"}]
                 )

phase2tkmclayout(dqmitems, "09 - IT Cluster Endcap PLUS FPix Y",
                 [{'path':"TrackerPhase2ITClusterV/EndCap_Side2/FPix/Ring1/Delta_Y_Pixel",
                   'description': "Ring 1 Delta Y Pixel"},
                  {'path':"TrackerPhase2ITClusterV/EndCap_Side2/FPix/Ring2/Delta_Y_Pixel",
                   'description': "Ring 2 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2ITClusterV/EndCap_Side2/FPix/Ring3/Delta_Y_Pixel",
                   'description': "Ring 3 Delta Y Pixel"},
                  {'path':"TrackerPhase2ITClusterV/EndCap_Side2/FPix/Ring4/Delta_Y_Pixel",
                   'description': "Ring 4 Delta Y Pixel"}]
                 )

phase2tkmclayout(dqmitems, "10 - IT RecHit Barrel Delta Y v Delta X",
                 [{'path':"TrackerPhase2ITRecHitV/Barrel/Layer1/Delta_Y_vs_DeltaX",
                   'description': "Layer 1 Delta Y v Delta X"},
                  {'path':"TrackerPhase2ITRecHitV/Barrel/Layer2/Delta_Y_vs_DeltaX",
                   'description': "Layer 2 Delta Y v Delta X"}],
                 [{'path':"TrackerPhase2ITRecHitV/Barrel/Layer3/Delta_Y_vs_DeltaX",
                   'description': "Layer 3 Delta Y v Delta X"},
                  {'path':"TrackerPhase2ITRecHitV/Barrel/Layer4/Delta_Y_vs_DeltaX",
                   'description': "Layer 4 Delta Y v Delta X"}]
                 )

phase2tkmclayout(dqmitems, "11 - IT RecHit Endcap MINUS EPix Delta Y v Delta X",
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

phase2tkmclayout(dqmitems, "12 - IT RecHit Endcap MINUS FPix Delta Y v Delta X",
                 [{'path':"TrackerPhase2ITRecHitV/EndCap_Side1/FPix/Ring1/Delta_Y_vs_DeltaX",
                   'description': "Ring 1 Delta Y v Delta X"},
                  {'path':"TrackerPhase2ITRecHitV/EndCap_Side1/FPix/Ring2/Delta_Y_vs_DeltaX",
                   'description': "Ring 2 Delta Y v Delta X"}],
                 [{'path':"TrackerPhase2ITRecHitV/EndCap_Side1/FPix/Ring3/Delta_Y_vs_DeltaX",
                   'description': "Ring 3 Delta Y v Delta X"},
                  {'path':"TrackerPhase2ITRecHitV/EndCap_Side1/FPix/Ring4/Delta_Y_vs_DeltaX",
                   'description': "Ring 4 Delta Y v Delta X"}]
                 )

phase2tkmclayout(dqmitems, "13 - IT RecHit Endcap PLUS EPix Delta Y v Delta X",
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

phase2tkmclayout(dqmitems, "14 - IT RecHit Endcap PLUS FPix Delta Y v Delta X",
                 [{'path':"TrackerPhase2ITRecHitV/EndCap_Side2/FPix/Ring1/Delta_Y_vs_DeltaX",
                   'description': "Ring 1 Delta Y v Delta X"},
                  {'path':"TrackerPhase2ITRecHitV/EndCap_Side2/FPix/Ring2/Delta_Y_vs_DeltaX",
                   'description': "Ring 2 Delta Y v Delta X"}],
                 [{'path':"TrackerPhase2ITRecHitV/EndCap_Side2/FPix/Ring3/Delta_Y_vs_DeltaX",
                   'description': "Ring 3 Delta Y v Delta X"},
                  {'path':"TrackerPhase2ITRecHitV/EndCap_Side2/FPix/Ring4/Delta_Y_vs_DeltaX",
                   'description': "Ring 4 Delta Y v Delta X"}]
                 )

phase2tkmclayout(dqmitems, "20 - IT TrackingRecHit Barrel X",
                 [{'path':"TrackerPhase2ITTrackingRecHitV/Barrel/Layer1/Delta_X",
                   'description': "Layer 1 Delta X"},
                  {'path':"TrackerPhase2ITTrackingRecHitV/Barrel/Layer2/Delta_X",
                   'description': "Layer 2 Delta X"}],
                 [{'path':"TrackerPhase2ITTrackingRecHitV/Barrel/Layer3/Delta_X",
                   'description': "Layer 3 Delta X"},
                  {'path':"TrackerPhase2ITTrackingRecHitV/Barrel/Layer4/Delta_X",
                   'description': "Layer 4 Delta X"}]
                 )

phase2tkmclayout(dqmitems, "21 - IT TrackingRecHit Barrel Y",
                 [{'path':"TrackerPhase2ITTrackingRecHitV/Barrel/Layer1/Delta_Y",
                   'description': "Layer 1 Delta Y"},
                  {'path':"TrackerPhase2ITTrackingRecHitV/Barrel/Layer2/Delta_Y",
                   'description': "Layer 2 Delta Y"}],
                 [{'path':"TrackerPhase2ITTrackingRecHitV/Barrel/Layer3/Delta_Y",
                   'description': "Layer 3 Delta Y"},
                  {'path':"TrackerPhase2ITTrackingRecHitV/Barrel/Layer4/Delta_Y",
                   'description': "Layer 4 Delta Y"}]
                 )

phase2tkmclayout(dqmitems, "22 - IT TrackingRecHit Endcap MINUS EPix X",
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

phase2tkmclayout(dqmitems, "23 - IT TrackingRecHit Endcap MINUS EPix Y",
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

phase2tkmclayout(dqmitems, "24 - IT TrackingRecHit Endcap MINUS FPix X",
                 [{'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side1/FPix/Ring1/Delta_X",
                   'description': "Ring 1 Delta X"},
                  {'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side1/FPix/Ring2/Delta_X",
                   'description': "Ring 2 Delta X"}],
                 [{'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side1/FPix/Ring3/Delta_X",
                   'description': "Ring 3 Delta X"},
                  {'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side1/FPix/Ring4/Delta_X",
                   'description': "Ring 4 Delta X"}]
                 )

phase2tkmclayout(dqmitems, "25 - IT TrackingRecHit Endcap MINUS FPix Y",
                 [{'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side1/FPix/Ring1/Delta_Y",
                   'description': "Ring 1 Delta Y"},
                  {'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side1/FPix/Ring2/Delta_Y",
                   'description': "Ring 2 Delta Y"}],
                 [{'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side1/FPix/Ring3/Delta_Y",
                   'description': "Ring 3 Delta Y"},
                  {'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side1/FPix/Ring4/Delta_Y",
                   'description': "Ring 4 Delta Y"}]
                 )

phase2tkmclayout(dqmitems, "26 - IT TrackingRecHit Endcap PLUS EPix X",
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

phase2tkmclayout(dqmitems, "27 - IT TrackingRecHit Endcap PLUS EPix Y",
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

phase2tkmclayout(dqmitems, "28 - IT TrackingRecHit Endcap PLUS FPix X",
                 [{'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side2/FPix/Ring1/Delta_X",
                   'description': "Ring 1 Delta X"},
                  {'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side2/FPix/Ring2/Delta_X",
                   'description': "Ring 2 Delta X"}],
                 [{'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side2/FPix/Ring3/Delta_X",
                   'description': "Ring 3 Delta X"},
                  {'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side2/FPix/Ring4/Delta_X",
                   'description': "Ring 4 Delta X"}]
                 )

phase2tkmclayout(dqmitems, "29 - IT TrackingRecHit Endcap PLUS FPix Y",
                 [{'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side2/FPix/Ring1/Delta_Y",
                   'description': "Ring 1 Delta Y"},
                  {'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side2/FPix/Ring2/Delta_Y",
                   'description': "Ring 2 Delta Y"}],
                 [{'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side2/FPix/Ring3/Delta_Y",
                   'description': "Ring 3 Delta Y"},
                  {'path':"TrackerPhase2ITTrackingRecHitV/EndCap_Side2/FPix/Ring4/Delta_Y",
                   'description': "Ring 4 Delta Y"}]
                 )

phase2tkmclayout(dqmitems, "30 - OT Cluster Barrel Pixel X",
                 [{'path':"TrackerPhase2OTClusterV/Barrel/Layer1/Delta_X_Pixel",
                   'description': "Layer 1 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/Barrel/Layer2/Delta_X_Pixel",
                   'description': "Layer 2 Delta X Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/Barrel/Layer3/Delta_X_Pixel",
                   'description': "Layer 3 Delta X Pixel"}]
                 )

phase2tkmclayout(dqmitems, "31 - OT Cluster Barrel Pixel Y",
                 [{'path':"TrackerPhase2OTClusterV/Barrel/Layer1/Delta_Y_Pixel",
                   'description': "Layer 1 Delta Y Pixel"},
                  {'path':"TrackerPhase2OTClusterV/Barrel/Layer2/Delta_Y_Pixel",
                   'description': "Layer 2 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/Barrel/Layer3/Delta_Y_Pixel",
                   'description': "Layer 3 Delta Y Pixel"}]
                 )

phase2tkmclayout(dqmitems, "32 - OT Cluster Barrel Strip X",
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

phase2tkmclayout(dqmitems, "33 - OT Cluster Barrel Strip Y",
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

phase2tkmclayout(dqmitems, "34 - OT Cluster Endcap MINUS TEDD1 Pixel and Strip XY",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring1/Delta_X_Pixel",
                   'description': "Ring 1 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring1/Delta_Y_Pixel",
                   'description': "Ring 1 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring1/Delta_X_Strip",
                   'description': "Ring 1 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_1/Ring1/Delta_Y_Strip",
                   'description': "Ring 1 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "35 - OT Cluster Endcap MINUS TEDD2 Pixel and Strip XY",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring1/Delta_X_Pixel",
                   'description': "Ring 1 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring1/Delta_Y_Pixel",
                   'description': "Ring 1 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring1/Delta_X_Strip",
                   'description': "Ring 1 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side1/TEDD_2/Ring1/Delta_Y_Strip",
                   'description': "Ring 1 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "36 - OT Cluster Endcap PLUS TEDD1 Pixel and Strip XY",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring1/Delta_X_Pixel",
                   'description': "Ring 1 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring1/Delta_Y_Pixel",
                   'description': "Ring 1 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring1/Delta_X_Strip",
                   'description': "Ring 1 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_1/Ring1/Delta_Y_Strip",
                   'description': "Ring 1 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "37 - OT Cluster Endcap PLUS TEDD2 Pixel and Strip XY",
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring1/Delta_X_Pixel",
                   'description': "Ring 1 Delta X Pixel"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring1/Delta_Y_Pixel",
                   'description': "Ring 1 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring1/Delta_X_Strip",
                   'description': "Ring 1 Delta X Strip"},
                  {'path':"TrackerPhase2OTClusterV/EndCap_Side2/TEDD_2/Ring1/Delta_Y_Strip",
                   'description': "Ring 1 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "40 - OT L1Track Eta Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/NominalL1TF/FinalEfficiency/EtaEfficiency",
                   'description': "Eta Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/NominalL1TF/FinalResolution/EtaResolution",
                   'description': "Eta Resolution"}]
                 )

phase2tkmclayout(dqmitems, "41 - OT L1Track Phi Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/NominalL1TF/FinalEfficiency/PhiEfficiency",
                   'description': "Phi Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/NominalL1TF/FinalResolution/PhiResolution",
                   'description': "Phi Resolution"}]
                 )

phase2tkmclayout(dqmitems, "42 - OT L1Track VtxZ Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/NominalL1TF/FinalEfficiency/VtxZEfficiency",
                   'description': "VtxZ Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/NominalL1TF/FinalResolution/VtxZResolution",
                   'description': "VtxZ Resolution"}]
                 )

phase2tkmclayout(dqmitems, "43 - OT L1Track d0 Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/NominalL1TF/FinalEfficiency/d0Efficiency",
                   'description': "d0 Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/NominalL1TF/FinalResolution/d0Resolution",
                   'description': "d0 Resolution"}]
                 )

phase2tkmclayout(dqmitems, "44 - OT Extended L1Track Displaced Eta Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Displaced/FinalEfficiency/EtaEfficiency",
                   'description': "Eta Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Displaced/FinalResolution/EtaResolution",
                   'description': "Eta Resolution"}]
                 )

phase2tkmclayout(dqmitems, "45 - OT Extended L1Track Displaced Phi Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Displaced/FinalEfficiency/PhiEfficiency",
                   'description': "Phi Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Displaced/FinalResolution/PhiResolution",
                   'description': "Phi Resolution"}]
                 )

phase2tkmclayout(dqmitems, "46 - OT Extended L1Track Displaced VtxZ Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Displaced/FinalEfficiency/VtxZEfficiency",
                   'description': "VtxZ Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Displaced/FinalResolution/VtxZResolution",
                   'description': "VtxZ Resolution"}]
                 )

phase2tkmclayout(dqmitems, "47 - OT Extended L1Track Displaced d0 Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Displaced/FinalEfficiency/d0Efficiency",
                   'description': "d0 Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Displaced/FinalResolution/d0Resolution",
                   'description': "d0 Resolution"}]
                 )

phase2tkmclayout(dqmitems, "48 - OT Extended L1Track Prompt Eta Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Prompt/FinalEfficiency/EtaEfficiency",
                   'description': "Eta Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Prompt/FinalResolution/EtaResolution",
                   'description': "Eta Resolution"}]
                 )

phase2tkmclayout(dqmitems, "49 - OT Extended L1Track Prompt Phi Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Prompt/FinalEfficiency/PhiEfficiency",
                   'description': "Phi Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Prompt/FinalResolution/PhiResolution",
                   'description': "Phi Resolution"}]
                 )

phase2tkmclayout(dqmitems, "410 - OT Extended L1Track Prompt VtxZ Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Prompt/FinalEfficiency/VtxZEfficiency",
                   'description': "VtxZ Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Prompt/FinalResolution/VtxZResolution",
                   'description': "VtxZ Resolution"}]
                 )

phase2tkmclayout(dqmitems, "411 - OT Extended L1Track Prompt d0 Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Prompt/FinalEfficiency/d0Efficiency",
                   'description': "d0 Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Prompt/FinalResolution/d0Resolution",
                   'description': "d0 Resolution"}]
                 )

phase2tkmclayout(dqmitems, "50 - OT RecHit Barrel Pixel X",
                 [{'path':"TrackerPhaseOTRecHitV/Barrel/Layer1/Delta_X_Pixel",
                   'description': "Layer 1 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/Barrel/Layer2/Delta_X_Pixel",
                   'description': "Layer 2 Delta X Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/Barrel/Layer3/Delta_X_Pixel",
                   'description': "Layer 3 Delta X Pixel"}]
                 )

phase2tkmclayout(dqmitems, "51 - OT RecHit Barrel Pixel Y",
                 [{'path':"TrackerPhase2OTRecHitV/Barrel/Layer1/Delta_Y_Pixel",
                   'description': "Layer 1 Delta Y Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/Barrel/Layer2/Delta_Y_Pixel",
                   'description': "Layer 2 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/Barrel/Layer3/Delta_Y_Pixel",
                   'description': "Layer 3 Delta Y Pixel"}]
                 )

phase2tkmclayout(dqmitems, "52 - OT RecHit Barrel Strip X",
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

phase2tkmclayout(dqmitems, "53 - OT RecHit Barrel Strip Y",
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

phase2tkmclayout(dqmitems, "54 - OT RecHit Endcap MINUS TEDD1 Pixel and Strip XY",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring1/Delta_X_Pixel",
                   'description': "Ring 1 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring1/Delta_Y_Pixel",
                   'description': "Ring 1 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring1/Delta_X_Strip",
                   'description': "Ring 1 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_1/Ring1/Delta_Y_Strip",
                   'description': "Ring 1 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "55 - OT RecHit Endcap MINUS TEDD2 Pixel and Strip XY",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring1/Delta_X_Pixel",
                   'description': "Ring 1 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring1/Delta_Y_Pixel",
                   'description': "Ring 1 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring1/Delta_X_Strip",
                   'description': "Ring 1 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side1/TEDD_2/Ring1/Delta_Y_Strip",
                   'description': "Ring 1 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "56 - OT RecHit Endcap PLUS TEDD1 Pixel and Strip XY",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring1/Delta_X_Pixel",
                   'description': "Ring 1 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring1/Delta_Y_Pixel",
                   'description': "Ring 1 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring1/Delta_X_Strip",
                   'description': "Ring 1 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_1/Ring1/Delta_Y_Strip",
                   'description': "Ring 1 Delta Y Strip"}]
                 )

phase2tkmclayout(dqmitems, "57 - OT RecHit Endcap PLUS TEDD2 Pixel and Strip XY",
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring1/Delta_X_Pixel",
                   'description': "Ring 1 Delta X Pixel"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring1/Delta_Y_Pixel",
                   'description': "Ring 1 Delta Y Pixel"}],
                 [{'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring1/Delta_X_Strip",
                   'description': "Ring 1 Delta X Strip"},
                  {'path':"TrackerPhase2OTRecHitV/EndCap_Side2/TEDD_2/Ring1/Delta_Y_Strip",
                   'description': "Ring 1 Delta Y Strip"}]
                 )