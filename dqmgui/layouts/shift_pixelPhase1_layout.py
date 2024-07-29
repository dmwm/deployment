def shiftpixelP1layout(i, p, *rows): i["00 Shift/PixelPhase1/" + p] = DQMItem(layout=rows)
shiftpixelP1layout(dqmitems, "00 - PixelPhase1 ReportSummary: Layer or Disk vs subdet",
   [{ 'path': "PixelPhase1/EventInfo/reportSummaryMap",
      'description': "Summary results of qulity tests: Layer/Disk (y-axis) vs. Subdetectors (x-axis). See the PixelPhase1/Summary/ directory for more details.",
      'draw': { 'withref': "no", 'drawopts': "COLZTEXT" }}]
   )
shiftpixelP1layout(dqmitems, "02 - PixelPhase1 Digis: Ladder vs Module barrel summary",
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/num_digis_per_SignedModule_per_SignedLadder_PXLayer_1",
      'description': "Profile of digis per event and DetID by signed ladder (y-axis) vs signed module (x-axis) in layer 1 of barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/num_digis_per_SignedModule_per_SignedLadder_PXLayer_2",
      'description': "Profile of digis per event and DetID by signed ladder (y-axis) vs signed module (x-axis) in layer 2 of barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/num_digis_per_SignedModule_per_SignedLadder_PXLayer_3",
      'description': "Profile of digis per event and DetID by signed ladder (y-axis) vs signed module (x-axis) in layer 3 of barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/num_digis_per_SignedModule_per_SignedLadder_PXLayer_4",
      'description': "Profile of digis per event and DetID by signed ladder (y-axis) vs signed module (x-axis) in layer 4 of barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
   )

shiftpixelP1layout(dqmitems,"03 - PixelPhase1 Digis: BladePannel vs Disk endcap summary",
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/PXForward/num_digis_per_PXDisk_per_SignedBladePanel_PXRing_1",
      'description': "Profile of number of digis per event and detId by signed blade pannel (y-axis) vs signed disk (x-axis) in ring 1 of endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/PXForward/num_digis_per_PXDisk_per_SignedBladePanel_PXRing_2",
      'description': "Profile of number of digis per event and detId by signed blade pannel (y-axis) vs signed disk (x-axis) in ring 2 of endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
   )

shiftpixelP1layout(dqmitems, "06 - PixelPhase1 Dead Channels per ROC: Ladder vs Module barrel summary",
   [{ 'path': "PixelPhase1/FED/Dead Channels per ROC_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_1",
      'description': "Profile of dead channels per ROC by signed ladder (y-axis) vs signed module (x-axis) in layer 1 of barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ"}},
    { 'path': "PixelPhase1/FED/Dead Channels per ROC_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_2",
      'description': "Profile of dead channels per ROC by signed ladder (y-axis) vs signed module (x-axis) in layer 2 of barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
   [{ 'path': "PixelPhase1/FED/Dead Channels per ROC_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_3",
      'description': "Profile of dead channels per ROC by signed ladder (y-axis) vs signed module (x-axis) in layer 3 of barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "PixelPhase1/FED/Dead Channels per ROC_per_SignedModuleCoord_per_SignedLadderCoord_PXLayer_4",
      'description': "Profile of dead channels per ROC by signed ladder (y-axis) vs signed module (x-axis) in layer 4 of barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
   )

shiftpixelP1layout(dqmitems,"07 - PixelPhase1 Dead Channels per ROC: BladePannel vs Disk endcap summary",
   [{ 'path': "PixelPhase1/FED/Dead Channels per ROC_per_SignedDiskCoord_per_SignedBladePanelCoord_PXRing_1",
      'description': "Profile of number of dead Channels per ROC by signed blade pannel (y-axis) vs signed disk (x-axis) in ring 1 of endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "PixelPhase1/FED/Dead Channels per ROC_per_SignedDiskCoord_per_SignedBladePanelCoord_PXRing_2",
      'description': "Profile of number of dead Channels per ROC by signed blade pannel (y-axis) vs signed disk (x-axis) in ring 2 of endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
   )
shiftpixelP1layout(dqmitems, "08 - Compare number of objects GPUvsCPU",
   [{ 'path':  "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/nHits",
      'description': "No of RecHits GPU vs CPU",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path':  "SiPixelHeterogeneous/PixelTrackCompareGPUvsCPU/nLooseAndAboveTracks",
      'description': "No of pixel tracks with quality >= loose GPU vs CPU",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path':  "SiPixelHeterogeneous/PixelVertexCompareGPUvsCPU/nVertex",
      'description': "No of reconstructed vertices GPU vs CPU",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}]
    )

shiftpixelP1layout(dqmitems, "09 - FED error unbalance GPUvsCPU",
   [{ 'path':  "SiPixelHeterogeneous/PixelErrorCompareGPUvsCPU/FEErrorVsFEDIdUnbalance",
      'description': "Unbalance of Pixel FED Raw Data errors in GPU vs CPU",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}]
   )


shiftpixelP1layout(dqmitems, "10 - Compare track properties",
   [{ 'path': "SiPixelHeterogeneous/PixelTrackCompareGPUvsCPU/eta",
      'description': "Compare track #eta",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelTrackCompareGPUvsCPU/phi",
      'description': "Compare track #phi",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
   [{ 'path': "SiPixelHeterogeneous/PixelTrackCompareGPUvsCPU/pt",
      'description': "Compare track pt",
      'draw': { 'withref': "no", 'drawopts': "COLZ", 'ztype': 'log' }},
    { 'path': "SiPixelHeterogeneous/PixelTrackCompareGPUvsCPU/nRecHits",
      'description': "Compare number of rechits per track",
      'draw': { 'withref': "no", 'drawopts': "COLZ", 'ztype': 'log' }}]
   )

shiftpixelP1layout(dqmitems, "11 - Compare vertices",
    [{ 'path': "SiPixelHeterogeneous/PixelVertexCompareGPUvsCPU/chi2oNdof",
       'description': "Compare Vertex chi-squared/Ndof",
       'draw': { 'withref': "no", 'drawopts': "COLZ", 'ztype': 'log' }},
     { 'path': "SiPixelHeterogeneous/PixelVertexCompareGPUvsCPU/vz",
       'description': "Compare vertex z",
       'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
   [{ 'path': "SiPixelHeterogeneous/PixelVertexCompareGPUvsCPU/ntrk",
      'description': "Compare number of tracks associated to a vertex",
      'draw': { 'withref': "no", 'drawopts': "COLZ", 'ztype': 'log' }},
    { 'path': "SiPixelHeterogeneous/PixelVertexCompareGPUvsCPU/ptsq",
      'description': "Compare vertex pt squared",
      'draw': { 'withref': "no", 'drawopts': "COLZ", 'ztype': 'log' }}]
   )

shiftpixelP1layout(dqmitems, "12 - Difference in rechit position",
   [{ 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/rechitsposXDiffBpix",
      'description': "x-position difference in Barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ", 'ytype': 'log' }},
    { 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/rechitsposXDiffFpix",
      'description': "x-position difference in Forward",
      'draw': { 'withref': "no", 'drawopts': "COLZ", 'ytype': 'log' }}],
   [{ 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/rechitsposYDiffBpix",
      'description': "y-position difference in Barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ", 'ytype': 'log' }},
    { 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/rechitsposYDiffFpix",
      'description': "y-position difference in Forward",
      'draw': { 'withref': "no", 'drawopts': "COLZ", 'ytype': 'log' }}]
   )

shiftpixelP1layout(dqmitems, "13 - Difference in rechit size",
   [{ 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/rechitsizeXDiffBpix",
      'description': "size x difference in Barrel",
      'draw': { 'withref': "no" }},
    { 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/rechitsizeXDiffFpix",
      'description': "size x difference in Forward",
      'draw': { 'withref': "no" }}],
   [{ 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/rechitsizeYDiffBpix",
      'description': "size y difference in Barrel",
      'draw': { 'withref': "no" }},
    { 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/rechitsizeYDiffFpix",
      'description': "size y difference in Forward",
      'draw': { 'withref': "no" }}]
   )
