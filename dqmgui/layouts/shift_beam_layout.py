def shiftbeamlayout(i, p, *rows): i["00 Shift/BeamMonitor/" + p] = DQMItem(layout=rows)

shiftbeamlayout(dqmitems, "00 - BeamMonitorHLT ReportSummary",
 [{ 'path': "BeamMonitorHLT/EventInfo/reportSummaryMap",
    'description': "BeamSpot summary map"}])
shiftbeamlayout(dqmitems, "01 - d0-phi0 of selected tracks",
 [{ 'path': "BeamMonitorHLT/Fit/d0_phi0",
    'description': "d0-phi0 correlation of selected tracks - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftBeamMonitor>BeamMonitorOnlineDQMInstructions</a> "}])
shiftbeamlayout(dqmitems, "02 - z0 of selected tracks",
 [{ 'path': "BeamMonitorHLT/Fit/trk_z0",
    'description': "Z0 distribution of selected tracks  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftBeamMonitor>BeamMonitorOnlineDQMInstructions</a> "}])
shiftbeamlayout(dqmitems, "03 - fit results beam spot",
 [{ 'path': "BeamMonitorHLT/Fit/fitResults",
    'description': "d_{0}-#phi correlation fit results of beam spot",
    'draw': { 'drawopts': "TEXT" } }])
shiftbeamlayout(dqmitems, "04 - fitted x0, sigma(x0) vs LS",
 [{ 'path': "BeamMonitorHLT/Fit/x0_lumi",'description': "x coordinate of beamspot vs LS"}],
 [{ 'path': "BeamMonitorHLT/Fit/sigmaX0_lumi",'description': "sigma X of beamspot vs LS"}])
shiftbeamlayout(dqmitems, "05 - fitted y0, sigma(y0) vs LS",
 [{ 'path': "BeamMonitorHLT/Fit/y0_lumi",'description': "y coordinate of beamspot vs LS"}],
 [{ 'path': "BeamMonitorHLT/Fit/sigmaY0_lumi",'description': "sigma Y of beamspot vs LS"}])
shiftbeamlayout(dqmitems, "06 - fitted z0, sigma(z0) vs LS",
 [{ 'path': "BeamMonitorHLT/Fit/z0_lumi",'description': "z coordinate of beamspot vs LS"}],
 [{ 'path': "BeamMonitorHLT/Fit/sigmaZ0_lumi",'description': "sigma Z of beamspot vs LS"}])
shiftbeamlayout(dqmitems, "07 - chosen beam spot fit",
 [{ 'path': "OnlineBeamMonitor/Validation/bsChoice",
    'description': "chosen beam spot between Legacy or HLT fit, or fake beam spot"}])
