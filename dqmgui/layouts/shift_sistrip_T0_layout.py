def shiftsistriplayout(i, p, *rows): i["00 Shift/SiStrip/" + p] = DQMItem(layout=rows)

shiftsistriplayout(dqmitems, "00 - SiStrip ReportSummary",
 [{ 'path': "SiStrip/MechanicalView/detFractionReportMap",
    'description': "Fraction of Good Detector Modules plotted in different parts of the Tracker - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiStrip>DQMShiftOfflineSiStrip</a> ", 'draw': { 'withref': "no" }},
  { 'path': "SiStrip/MechanicalView/sToNReportMap",
    'description': "Accepted S/N Ratios in different parts of the Tracker. The values are 1 if the ratio is within the accepted range otherwise it is 0  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiStrip>DQMShiftOfflineSiStrip</a> ", 'draw': { 'withref': "yes" }}],
 [{ 'path': "SiStrip/EventInfo/reportSummaryMap",
    'description': "Overall Report Summary where detector fraction and S/N flags are combined together -  <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiStrip>DQMShiftOfflineSiStrip</a> ", 'draw': { 'withref': "no" }}])
shiftsistriplayout(dqmitems, "01 - FED Errors vs FED ID and APV ID",
 [{ 'path': "SiStrip/ReadoutView/FEDErrorsVsId",
    'description': "Type of FED errors vs FED ID",
    'draw': {'withref': "no" }}],
 [{'path': "SiStrip/ReadoutView/FedIdVsApvId",
   'description': "APV error: FED ID vs APV ID - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}])
shiftsistriplayout(dqmitems, "01a - FED-Detected Errors Summary",
 [{ 'path': "SiStrip/ReadoutView/FED/nFEDErrors",
    'description': "# of FEDs with any FED level error per event - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a>"}],
 [{ 'path': "SiStrip/ReadoutView/Fiber/nBadActiveChannelStatusBits",
    'description': "# of active channels with bad status bits per event - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a>"}])
shiftsistriplayout(dqmitems, "01b - FED-Detected Errors",
 [{ 'path': "SiStrip/ReadoutView/Fiber/VsId/BadActiveChannelStatusBits",
  'description': "FED IDs having connected channels, with a detected tickmark, with APV/Link errors - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
  { 'path': "SiStrip/ReadoutView/Fiber/VsId/BadChannelStatusBits",
  'description': "FED IDs having connected channels with APV/Link Errors - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
  { 'path': "SiStrip/ReadoutView/FED/VsId/AnyFEDErrors",
  'description': "FED IDs having any FED level error - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}],
 [{ 'path': "SiStrip/ReadoutView/Fiber/nUnlocked",
    'description': "Number of connected channels per event being without a detected tickmark - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
  { 'path': "SiStrip/ReadoutView/Fiber/nOutOfSync",
    'description': "Number of connected channels per event being out-of-sync - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
  { 'path': "SiStrip/ReadoutView/APV/nAPVAddressError",
    'description': "Number of connected APVs per event having wrong pipeline address tickmark - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}])
shiftsistriplayout(dqmitems, "02 - # of Cluster Trend",
  [{ 'path': "SiStrip/MechanicalView/TIB/TotalNumberOfClusterProfile__TIB",
     'description': "Total # of Clusters in TIB with event time in Seconds  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TOB/TotalNumberOfClusterProfile__TOB",
     'description': "Total # of Clusters in TOB with event time in Seconds  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}],
  [{ 'path': "SiStrip/MechanicalView/TID/MINUS/TotalNumberOfClusterProfile__TID__MINUS",
     'description': "Total # of Clusters in TID -ve side with event time in Seconds  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TID/PLUS/TotalNumberOfClusterProfile__TID__PLUS",
     'description': "Total # of Clusters in TID +ve side with event time in Seconds  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}],
  [{  'path':"SiStrip/MechanicalView/TEC/MINUS/TotalNumberOfClusterProfile__TEC__MINUS",
     'description': "Total # of Clusters in TEC -ve side with event time in Seconds  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   {  'path':"SiStrip/MechanicalView/TEC/PLUS/TotalNumberOfClusterProfile__TEC__PLUS",
     'description': "Total # of Clusters in TEC +ve side with event time in Seconds  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}])
shiftsistriplayout(dqmitems, "03 OnTrackCluster (StoN)",
  [{ 'path': "SiStrip/MechanicalView/TIB/Summary_ClusterStoNCorr_OnTrack__TIB",
     'description': "Signal-to-Noise (corrected for the angle) for On-Track clusters in TIB  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiStrip>DQMShiftOfflineSiStrip</a> ", 'draw': { 'withref': "yes" }},
   { 'path': "SiStrip/MechanicalView/TOB/Summary_ClusterStoNCorr_OnTrack__TOB",
     'description': "Signal-to-Noise (corrected for the angle) for On-Track clusters in TOB  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiStrip>DQMShiftOfflineSiStrip</a> ", 'draw': { 'withref': "yes" } }],
  [{ 'path': "SiStrip/MechanicalView/TID/MINUS/Summary_ClusterStoNCorr_OnTrack__TID__MINUS",
     'description': "Signal-to-Noise (corrected for the angle) for On-Track clusters in TID -ve side - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiStrip>DQMShiftOfflineSiStrip</a> ", 'draw': { 'withref': "yes" }},
   { 'path': "SiStrip/MechanicalView/TID/PLUS/Summary_ClusterStoNCorr_OnTrack__TID__PLUS",
     'description': "Signal-to-Noise (corrected for the angle) for On-Track clusters in TID +ve side - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiStrip>DQMShiftOfflineSiStrip</a> ", 'draw': { 'withref': "yes" } }],
  [{ 'path': "SiStrip/MechanicalView/TEC/MINUS/Summary_ClusterStoNCorr_OnTrack__TEC__MINUS",
     'description': "Signal-to-Noise (corrected for the angle) for On-Track clusters in TEC -ve side - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiStrip>DQMShiftOfflineSiStrip</a> ", 'draw': { 'withref': "yes" }},
   { 'path': "SiStrip/MechanicalView/TEC/PLUS/Summary_ClusterStoNCorr_OnTrack__TEC__PLUS",
     'description': "Signal-to-Noise (corrected for the angle) for On-Track clusters in TEC +ve side - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiStrip>DQMShiftOfflineSiStrip</a> ", 'draw': { 'withref': "yes" } }])
shiftsistriplayout(dqmitems, "04a - TIB Residuals",
  [{ 'path': "SiStrip/MechanicalView/TIB/layer_1/HitResiduals_TIB__Layer__1",
     'description': "Hit Residual in TIB Layer #1"},
   { 'path': "SiStrip/MechanicalView/TIB/layer_2/HitResiduals_TIB__Layer__2",
     'description': "Hit Residual in TIB Layer #2"}],
  [{ 'path': "SiStrip/MechanicalView/TIB/layer_3/HitResiduals_TIB__Layer__3",
     'description': "Hit Residual in TIB Layer #3"},
   { 'path': "SiStrip/MechanicalView/TIB/layer_4/HitResiduals_TIB__Layer__4",
     'description': "Hit Residual in TIB Layer #4"}])
shiftsistriplayout(dqmitems, "04b - TOB Residuals",
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
shiftsistriplayout(dqmitems, "04c - TID+ Residuals",
  [{ 'path': "SiStrip/MechanicalView/TID/PLUS/wheel_1/HitResiduals_TID__wheel__1",
     'description': "Hit Residuals in TID+ Wheel #1"},
   { 'path': "SiStrip/MechanicalView/TID/PLUS/wheel_2/HitResiduals_TID__wheel__2",
     'description': "Hit Residuals in TID+ Wheel #2"},
   { 'path': "SiStrip/MechanicalView/TID/PLUS/wheel_3/HitResiduals_TID__wheel__3",
     'description': "Hit Residuals in TID+ Wheel #3 "}])
shiftsistriplayout(dqmitems, "04d - TID- Residuals",
  [{ 'path': "SiStrip/MechanicalView/TID/MINUS/wheel_1/HitResiduals_TID__wheel__1",
     'description': "Hit Residuals in TID- Wheel #1"},
   { 'path': "SiStrip/MechanicalView/TID/MINUS/wheel_2/HitResiduals_TID__wheel__2",
     'description': "Hit Residuals in TID- Wheel #2"},
   { 'path': "SiStrip/MechanicalView/TID/MINUS/wheel_3/HitResiduals_TID__wheel__3",
     'description': "Hit Residuals in TID- Wheel #3 "}])

shiftsistriplayout(dqmitems, "04e - TEC+ Residual",
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
shiftsistriplayout(dqmitems, "04f - TEC- Residual",
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
shiftsistriplayout(dqmitems, "05 Strip Clusters Vs Pixel Clusters",
 [{ 'path': "SiStrip/MechanicalView/StripClusVsPixClus",
     'description': "Total number of clusters in Strip versus the total number of clusters in Pixels", 'draw': { 'withref': "no" }}])
shiftsistriplayout(dqmitems, "06 DeltaBx_vs_ApvCycle",
 [{ 'path': "SiStrip/MechanicalView/DeltaBx_vs_ApvCycle",
     'description': "This plot is to be checked only for cosmic runs with a number of LS>100, the red rectangles should be empty, if not please inform tracker experts", 'draw': { 'withref': "no" }}])
