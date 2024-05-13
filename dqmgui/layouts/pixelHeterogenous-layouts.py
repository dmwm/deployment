def pixelHeterolayout(i, p, *rows): i["SiPixelHeterogeneous/Layouts/" + p] = DQMItem(layout=rows)

pixelHeterolayout(dqmitems, "000 - Compare number of RecHits",
   [{ 'path':  "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/nHits",
      'description': "No of RecHits GPU vs CPU",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}]
   )

pixelHeterolayout(dqmitems, "00a - Compare number of tracks",
   [{ 'path':  "SiPixelHeterogeneous/PixelTrackCompareGPUvsCPU/nLooseAndAboveTracks",
      'description': "No of pixel tracks with quality >= loose GPU vs CPU",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}]
   )

pixelHeterolayout(dqmitems, "00b - Compare number of vertices",
   [{ 'path':  "SiPixelHeterogeneous/PixelVertexCompareGPUvsCPU/nVertex",
      'description': "No of reconstructed vertices GPU vs CPU",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}]
   )

pixelHeterolayout(dqmitems, "00c - Compare number of FE errors per FEDid",
   [{ 'path':  "SiPixelHeterogeneous/PixelErrorCompareGPUvsCPU/FEErrorVsFEDIdUnbalance",
      'description': "Unbalance of Pixel FED Raw Data errors in GPU vs CPU",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}]
   )

pixelHeterolayout(dqmitems, "01a - Compare rechit charge in Barrel",
   [{ 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsBLay1Charge",
      'description': "Compare rechit charge in layer 1 of pixel barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsBLay2Charge",
      'description': "Compare rechit charge in layer 2 of pixel barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
   [{ 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsBLay3Charge",
      'description': "Compare rechit charge in layer 3 of pixel barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsBLay4Charge",
      'description': "Compare rechit charge in layer 4 of pixel barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}]
   )

pixelHeterolayout(dqmitems, "01b - Compare rechit charge in Endcap",
   [{ 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsFDisk+1Charge",
      'description': "Compare rechit charge in disk +1 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsFDisk+2Charge",
      'description': "Compare rechit charge in disk +2 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsFDisk+3Charge",
      'description': "Compare rechit charge in disk +3 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
   [{ 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsFDisk-1Charge",
      'description': "Compare rechit charge in disk -1 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsFDisk-2Charge",
      'description': "Compare rechit charge in disk -2 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsFDisk-3Charge",
      'description': "Compare rechit charge in disk -2 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}]
   )

pixelHeterolayout(dqmitems, "02a - Compare rechit x-position in Barrel",
   [{ 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsBLay1Posx",
      'description': "Compare rechit x-position in layer 1 of pixel barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsBLay2Posx",
      'description': "Compare rechit x-position in layer 2 of pixel barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
   [{ 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsBLay3Posx",
      'description': "Compare rechit x-position in layer 3 of pixel barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsBLay4Posx",
      'description': "Compare rechit x-position in layer 4 of pixel barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}]
   )

pixelHeterolayout(dqmitems, "02b - Compare rechit x-position in Endcap",
   [{ 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsFDisk+1Posx",
      'description': "Compare rechit x-position in disk +1 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsFDisk+1Posx",
      'description': "Compare rechit x-position in disk +2 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsFDisk+1Posx",
      'description': "Compare rechit x-position in disk +3 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
   [{ 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsFDisk-1Posx",
      'description': "Compare rechit x-position in disk -1 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsFDisk-2Posx",
      'description': "Compare rechit x-position in disk -2 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsFDisk-3Posx",
      'description': "Compare rechit x-position in disk -2 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}]
   )


pixelHeterolayout(dqmitems, "03a - Compare rechit y-position in Barrel",
   [{ 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsBLay1Posy",
      'description': "Compare rechit y-position in layer 1 of pixel barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsBLay2Posy",
      'description': "Compare rechit y-position in layer 2 of pixel barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
   [{ 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsBLay3Posy",
      'description': "Compare rechit y-position in layer 3 of pixel barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsBLay4Posy",
      'description': "Compare rechit y-position in layer 4 of pixel barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}]
   )

pixelHeterolayout(dqmitems, "03b - Compare rechit y-position in Endcap",
   [{ 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsFDisk+1Posy",
      'description': "Compare rechit y-position in disk +1 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsFDisk+1Posy",
      'description': "Compare rechit y-position in disk +2 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsFDisk+1Posy",
      'description': "Compare rechit y-position in disk +3 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
   [{ 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsFDisk-1Posy",
      'description': "Compare rechit y-position in disk -1 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsFDisk-2Posy",
      'description': "Compare rechit y-position in disk -2 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsFDisk-3Posy",
      'description': "Compare rechit y-position in disk -2 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}]
   )


pixelHeterolayout(dqmitems, "04a - Compare rechit size x in Barrel",
   [{ 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsBLay1Sizex",
      'description': "Compare rechit size x in layer 1 of pixel barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsBLay2Sizex",
      'description': "Compare rechit size x in layer 2 of pixel barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
   [{ 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsBLay3Sizex",
      'description': "Compare rechit size x in layer 3 of pixel barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsBLay4Sizex",
      'description': "Compare rechit size x in layer 4 of pixel barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}]
   )

pixelHeterolayout(dqmitems, "04b - Compare rechit size x in Endcap",
   [{ 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsFDisk+1Sizex",
      'description': "Compare rechit size x in disk +1 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsFDisk+1Sizex",
      'description': "Compare rechit size x in disk +2 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsFDisk+1Sizex",
      'description': "Compare rechit size x in disk +3 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
   [{ 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsFDisk-1Sizex",
      'description': "Compare rechit size x in disk -1 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsFDisk-2Sizex",
      'description': "Compare rechit size x in disk -2 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsFDisk-3Sizex",
      'description': "Compare rechit size x in disk -2 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}]
   )

pixelHeterolayout(dqmitems, "05a - Compare rechit size y in Barrel",
   [{ 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsBLay1Sizey",
      'description': "Compare rechit size y in layer 1 of pixel barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsBLay2Sizey",
      'description': "Compare rechit size y in layer 2 of pixel barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
   [{ 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsBLay3Sizey",
      'description': "Compare rechit size y in layer 3 of pixel barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsBLay4Sizey",
      'description': "Compare rechit size y in layer 4 of pixel barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}]
   )

pixelHeterolayout(dqmitems, "05b - Compare rechit size y in Endcap",
   [{ 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsFDisk+1Sizey",
      'description': "Compare rechit size y in disk +1 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsFDisk+1Sizey",
      'description': "Compare rechit size y in disk +2 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsFDisk+1Sizey",
      'description': "Compare rechit size y in disk +3 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
   [{ 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsFDisk-1Sizey",
      'description': "Compare rechit size y in disk -1 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsFDisk-2Sizey",
      'description': "Compare rechit size y in disk -2 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsFDisk-3Sizey",
      'description': "Compare rechit size y in disk -2 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}]
   )


pixelHeterolayout(dqmitems, "06 - Difference in rechit charge",
   [{ 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/rechitChargeDiffBpix",
      'description': "Charge difference(CPU - GPU) in Barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/rechitChargeDiffFpix",
      'description': "Charge difference(CPU - GPU) in Forward",
      'draw': { 'withref': "no" }}]
   )

pixelHeterolayout(dqmitems, "07 - Difference in rechit position",
   [{ 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/rechitsposXDiffBpix",
      'description': "x-position difference in Barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/rechitsposXDiffFpix",
      'description': "x-position difference in Forward",
      'draw': { 'withref': "no" }}],
   [{ 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/rechitsposYDiffBpix",
      'description': "y-position difference in Barrel",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/rechitsposYDiffFpix",
      'description': "y-position difference in Forward",
      'draw': { 'withref': "no" }}]
   )

pixelHeterolayout(dqmitems, "08 - Difference in rechit size",
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

pixelHeterolayout(dqmitems, "09a - Compare track properties",
   [{ 'path': "SiPixelHeterogeneous/PixelTrackCompareGPUvsCPU/eta",
      'description': "Compare track #eta",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelTrackCompareGPUvsCPU/phi",
      'description': "Compare track #phi",
      'draw': { 'withref': "no" }},
    { 'path': "SiPixelHeterogeneous/PixelTrackCompareGPUvsCPU/pt",
      'description': "Compare track pt",
      'draw': { 'withref': "no" }}],
   [{ 'path': "SiPixelHeterogeneous/PixelTrackCompareGPUvsCPU/ptLogLog",
      'description': "Compare track pt in log scale",
      'draw': { 'withref': "no" }},
     { 'path': "SiPixelHeterogeneous/PixelTrackCompareGPUvsCPU/nChi2ndof",
      'description': "Compare track Chi2ndof",
      'draw': { 'withref': "no" }},
     { 'path': "SiPixelHeterogeneous/PixelTrackCompareGPUvsCPU/nLayers",
      'description': "Compare number of layers per track",
      'draw': { 'withref': "no" }}]
   )

pixelHeterolayout(dqmitems, "09b - Compare track properties",
    [{ 'path': "SiPixelHeterogeneous/PixelTrackCompareGPUvsCPU/z",
      'description': "Compare track z",
      'draw': { 'withref': "no" }},
     { 'path': "SiPixelHeterogeneous/PixelTrackCompareGPUvsCPU/tip",
      'description': "Compare track TIP [cm]",
      'draw': { 'withref': "no" }},
     { 'path': "SiPixelHeterogeneous/PixelTrackCompareGPUvsCPU/nRecHits",
      'description': "Compare number of rechits per track",
      'draw': { 'withref': "no" }}],
   [{ 'path': "SiPixelHeterogeneous/PixelTrackCompareGPUvsCPU/nTracks",
      'description': "Number of tracks (no quality cut)",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelTrackCompareGPUvsCPU/nLooseAndAboveTracks_matched",
      'description': "Number of tracks with quality >= loose on CPU matched to GPU track",
      'draw': { 'withref': "no" }}]
   )

pixelHeterolayout(dqmitems, "10 - Track matching phase space",
    [{ 'path': "SiPixelHeterogeneous/PixelTrackCompareGPUvsCPU/phiztrkAllHost",
      'description': "phi-z map of CPU tracks(with >= loose quality)",
      'draw': { 'withref': "no" }},
     { 'path': "SiPixelHeterogeneous/PixelTrackCompareGPUvsCPU/phiztrkAllHostmatched",
      'description': "phi-z map of CPU tracks(with >= loose quality) matched to a GPU track",
      'draw': { 'withref': "no" }}],
   [{ 'path': "SiPixelHeterogeneous/PixelTrackCompareGPUvsCPU/ptetatrkAllHost",
      'description': "pt-eta map of CPU tracks(with >= loose quality)",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelTrackCompareGPUvsCPU/nLooseAndAboveTracks_matched",
      'description': "pt-eta map of CPU tracks(with >= loose quality) matched to a GPU track",
      'draw': { 'withref': "no" }}]
   )

pixelHeterolayout(dqmitems, "11 - Differences in track properties",
    [{ 'path': "SiPixelHeterogeneous/PixelTrackCompareGPUvsCPU/etadiffmatched",
      'description': "Difference in eta for matched tracks",
      'draw': { 'withref': "no" }},
     { 'path': "SiPixelHeterogeneous/PixelTrackCompareGPUvsCPU/phidiffmatched",
      'description': "Difference in phi for matched tracks",
      'draw': { 'withref': "no" }}],
   [{ 'path': "SiPixelHeterogeneous/PixelTrackCompareGPUvsCPU/ptdiffmatched",
      'description': "Difference in pt for matched tracks",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelTrackCompareGPUvsCPU/zdiffmatched",
      'description': "Difference in z for matched tracks",
      'draw': { 'withref': "no" }}]
   )

pixelHeterolayout(dqmitems, "12a - Compare vertices",
    [{ 'path': "SiPixelHeterogeneous/PixelVertexCompareGPUvsCPU/chi2",
      'description': "Compare vertex chi-squared",
      'draw': { 'withref': "no" }},
     { 'path': "SiPixelHeterogeneous/PixelVertexCompareGPUvsCPU/chi2oNdof",
      'description': "Compare Vertex chi-squared/Ndof",
      'draw': { 'withref': "no" }}],
   [{ 'path': "SiPixelHeterogeneous/PixelVertexCompareGPUvsCPU/ntrk",
      'description': "Compare number of tracks associated to a vertex",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
    { 'path': "SiPixelHeterogeneous/PixelVertexCompareGPUvsCPU/ptsq",
      'description': "Compare vertex pt squared",
      'draw': { 'withref': "no" }}]
   )


pixelHeterolayout(dqmitems, "12b - Compare vertices",
    [{ 'path': "SiPixelHeterogeneous/PixelVertexCompareGPUvsCPU/vz",
      'description': "Compare vertex z",
      'draw': { 'withref': "no" }}],
    [{ 'path': "SiPixelHeterogeneous/PixelVertexCompareGPUvsCPU/vx",
      'description': "Compare vertex x",
      'draw': { 'withref': "no" }},
     { 'path': "SiPixelHeterogeneous/PixelVertexCompareGPUvsCPU/vx",
      'description': "Compare vertex y",
      'draw': { 'withref': "no" }}]
   )


