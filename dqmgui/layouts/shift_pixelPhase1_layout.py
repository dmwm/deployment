def shiftpixelP1layout(i, p, *rows): i["00 Shift/PixelPhase1/" + p] = DQMItem(layout=rows)
shiftpixelP1layout(dqmitems, "00 - PixelPhase1 ReportSummary: Layer or Disk vs subdet",
   [{ 'path': "PixelPhase1/EventInfo/reportSummaryMap",
      'description': "Summary results of qulity tests: Layer/Disk (y-axis) vs. Subdetectors (x-axis). See the PixelPhase1/Summary/ directory for more details.",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}]
   )
shiftpixelP1layout(dqmitems, "01 - PixelPhase1_Error_Summary",
   [{ 'path': "PixelPhase1/FED/nerrors_per_type_per_FED",
      'description': "Number of Errors of each type per FED. Channel 0 is assigned for errors where the channel number is not known.",
      'draw': { 'withref': "no" }}]
   )
shiftpixelP1layout(dqmitems, "02 - PixelPhase1_Error_Summary",
   [{ 'path': "PixelPhase1/FED/errors_per_LinkInFed_per_FED",
      'description': "Total number of errors in a map of FED channels (y-axis) vs. FED (x-axis). Channel 0 is assigned for errors where the channel number is not known.",
      'draw': { 'withref': "no" }}]
   )
shiftpixelP1layout(dqmitems, "03 - PixelPhase1 Cluster Position: Z vs Phi barrel summary",
   [{'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/clusterposition_zphi_PXLayer_1",
     'description': "Cluster position in global coordinates by Global Phi (y-axis) vs Global Z (x-axis) in layer 1 of pixel endcap",
     'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    {'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/clusterposition_zphi_PXLayer_2",
     'description': "Cluster position in global coordinates by Global Phi (y-axis) vs Global Z (x-axis) in layer 2 of pixel endcap",
     'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
   [{'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/clusterposition_zphi_PXLayer_3",
     'description': "Cluster position in global coordinates by Global Phi (y-axis) vs Global Z (x-axis) in layer 3 of pixel endcap",
     'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    {'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/clusterposition_zphi_PXLayer_4",
     'description': "Cluster position in global coordinates by Global Phi (y-axis) vs Global Z (x-axis) in layer 4 of pixel endcap",
     'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
   )

shiftpixelP1layout(dqmitems, "04 - PixelPhase1 Cluster Position: X vs Y endcap summary",
   [{'path': "PixelPhase1/Phase1_MechanicalView/PXForward/clusterposition_xy_PXDisk_+1",
     'description': "Cluster position in global coordinates by Global Y (y-axis) vs Global X (x-axis) in disk +1 of pixel endcap",
     'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    {'path': "PixelPhase1/Phase1_MechanicalView/PXForward/clusterposition_xy_PXDisk_+2",
     'description': "Cluster position in global coordinates by Global Y (y-axis) vs Global X (x-axis) in disk +2 of pixel endcap",
     'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    {'path': "PixelPhase1/Phase1_MechanicalView/PXForward/clusterposition_xy_PXDisk_+3",
     'description': "Cluster position in global coordinates by Global Y (y-axis) vs Global X (x-axis) in disk +3 of pixel endcap",
     'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
   [{'path': "PixelPhase1/Phase1_MechanicalView/PXForward/clusterposition_xy_PXDisk_-1",
     'description': "Cluster position in global coordinates by Global Y (y-axis) vs Global X (x-axis) in disk -1 of pixel endcap",
     'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    {'path': "PixelPhase1/Phase1_MechanicalView/PXForward/clusterposition_xy_PXDisk_-2",
     'description': "Cluster position in global coordinates by Global Y (y-axis) vs Global X (x-axis) in disk -2 of pixel endcap",
     'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    {'path': "PixelPhase1/Phase1_MechanicalView/PXForward/clusterposition_xy_PXDisk_-3",
     'description': "Cluster position in global coordinates by Global Y (y-axis) vs Global X (x-axis) in disk -3 of pixel endcap",
     'draw': { 'withref': "no", 'drawopts': "COLZ" }}], 
   )

shiftpixelP1layout(dqmitems, "05 - PixelPhase1_Cluster_Charge",
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/charge_PXBarrel",
      'description': "Cluster charge in the BPix modules",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/charge_PXForward",
      'description': "Cluster charge in FPix modules",
      'draw': { 'withref': "no" }}]
   )
