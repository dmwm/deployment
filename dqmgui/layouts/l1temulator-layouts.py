def l1temulayout(i, p, *rows): i["L1TEMU/Layouts/" + p] = DQMItem(layout=rows)

# The quick collection is defined in ../workspaces-online.py
# for Online DQM, but we want to also include descriptions
# So we reference the 'QuickCollection' layout created here
def l1t_quickCollection(i, name, *rows):
  i["L1TEMU/Layouts/Stage2-QuickCollection/%s" % name] = DQMItem(layout=rows)

# If you add a plot here, remember to add the reference to ../workspaces-online.py
l1t_quickCollection(dqmitems, "00 - CaloTower Data-Emulator Mismatch Status",
  [{
    'path': "L1T2016EMU/L1TdeStage2CaloLayer1/ecalOccupancy",
    'description': "This should be empty"
  }])


###############################################
### From here down is legacy/stage1 trigger ###
###           All in Legacy folder          ###
###############################################

def l1temucommon(i, dir, name):i["L1TEMU/Layouts/00-Global-Summary/%s" % name] = \
    DQMItem(layout=[["L1TEMU/%s/%s" % (dir, name)]])

l1temucommon(dqmitems, "common", "sysrates")
l1temucommon(dqmitems, "common", "errorflag")
l1temucommon(dqmitems, "common", "sysncandData")
l1temucommon(dqmitems, "common", "sysncandEmul")

def l1t_rct_expert(i, p, *rows): i["L1TEMU/Layouts/03-L1TdeRCT-Summary/" + p] = DQMItem(layout=rows)
l1t_rct_expert(dqmitems, "rctInputTPGEcalOcc",
  [{ 'path': "L1TEMU/L1TdeRCT/rctInputTPGEcalOcc", 'description': "Input ECAL TPs occupancy, For details see - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/RCTDataQualityMonitoring>RCTDQM</a> CAL/RCT/GCT mapping is here <a href=https://twiki.cern.ch/twiki/pub/CMS/RCTDataQualityMonitoring/RCTGCTCAL.jpeg> mapping </a>" }])

l1t_rct_expert(dqmitems, "rctInputTPGHcalOcc",
  [{ 'path': "L1TEMU/L1TdeRCT/rctInputTPGHcalOcc", 'description': "Input HCAL TPs occupancy, For details see - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/RCTDataQualityMonitoring>RCTDQM</a> CAL/RCT/GCT mapping is here <a href=https://twiki.cern.ch/twiki/pub/CMS/RCTDataQualityMonitoring/RCTGCTCAL.jpeg> mapping </a>" }])

l1t_rct_expert(dqmitems, "rctIsoEmEff1",
  [{ 'path': "L1TEMU/L1TdeRCT/IsoEm/rctIsoEmEff1", 'description': "Isolated electrons efficiency, For details see - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/RCTDataQualityMonitoring>RCTDQM</a> CAL/RCT/GCT mapping is here <a href=https://twiki.cern.ch/twiki/pub/CMS/RCTDataQualityMonitoring/RCTGCTCAL.jpeg> mapping </a>" }])

l1t_rct_expert(dqmitems, "rctNisoEmEff1",
  [{ 'path': "L1TEMU/L1TdeRCT/NisoEm/rctNisoEmEff1", 'description': "Non-Isolated electrons efficiency, For details see - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/RCTDataQualityMonitoring>RCTDQM</a> CAL/RCT/GCT mapping is here <a href=https://twiki.cern.ch/twiki/pub/CMS/RCTDataQualityMonitoring/RCTGCTCAL.jpeg> mapping </a>" }])

l1t_rct_expert(dqmitems, "rctRegEff2D",
  [{ 'path': "L1TEMU/L1TdeRCT/RegionData/rctRegEff2D", 'description': "Regional efficiency, For details see - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/RCTDataQualityMonitoring>RCTDQM</a> CAL/RCT/GCT mapping is here <a href=https://twiki.cern.ch/twiki/pub/CMS/RCTDataQualityMonitoring/RCTGCTCAL.jpeg> mapping </a>" }])

l1t_rct_expert(dqmitems, "rctIsoEmOvereff",
  [{ 'path': "L1TEMU/L1TdeRCT/IsoEm/rctIsoEmOvereff", 'description': "Isolated electrons overefficiency, For details see - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/RCTDataQualityMonitoring>RCTDQM</a> CAL/RCT/GCT mapping is here <a href=https://twiki.cern.ch/twiki/pub/CMS/RCTDataQualityMonitoring/RCTGCTCAL.jpeg> mapping </a>" }])

l1t_rct_expert(dqmitems, "rctNisoEmOvereff",
  [{ 'path': "L1TEMU/L1TdeRCT/NisoEm/rctNisoEmOvereff", 'description': "Non-Isolated electrons overefficiency, For details see - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/RCTDataQualityMonitoring>RCTDQM</a> CAL/RCT/GCT mapping is here <a href=https://twiki.cern.ch/twiki/pub/CMS/RCTDataQualityMonitoring/RCTGCTCAL.jpeg> mapping </a>" }])

l1t_rct_expert(dqmitems, "rctRegOvereff2D",
  [{ 'path': "L1TEMU/L1TdeRCT/RegionData/rctRegOvereff2D", 'description': "Regional overefficiency, For details see - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/RCTDataQualityMonitoring>RCTDQM</a> CAL/RCT/GCT mapping is here <a href=https://twiki.cern.ch/twiki/pub/CMS/RCTDataQualityMonitoring/RCTGCTCAL.jpeg> mapping </a>" }])

l1t_rct_expert(dqmitems, "RctEmIsoEmOccEtaPhi",
  [{ 'path': "L1TEMU/L1TdeRCT/IsoEm/ServiceData/rctIsoEmDataOcc", 'description': "EmIsoOcc, For details see - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/RCTDataQualityMonitoring>RCTDQM</a> CAL/RCT/GCT mapping is here <a href=https://twiki.cern.ch/twiki/pub/CMS/RCTDataQualityMonitoring/RCTGCTCAL.jpeg> mapping </a>" }])

l1t_rct_expert(dqmitems, "RctEmNonIsoEmOccEtaPhi",
  [{ 'path': "L1TEMU/L1TdeRCT/NisoEm/ServiceData/rctNisoEmDataOcc", 'description': "RctEmNonIsoEmOccEtaPhi, For details see - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/RCTDataQualityMonitoring>RCTDQM</a> CAL/RCT/GCT mapping is here <a href=https://twiki.cern.ch/twiki/pub/CMS/RCTDataQualityMonitoring/RCTGCTCAL.jpeg> mapping </a>" }])

l1t_rct_expert(dqmitems, "RctRegionsOccEtaPhi",
  [{ 'path': "L1TEMU/L1TdeRCT/RegionData/ServiceData/rctRegDataOcc2D", 'description': "RctRegionsOccEtaPhi, For details see - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/RCTDataQualityMonitoring>RCTDQM</a> CAL/RCT/GCT mapping is here <a href=https://twiki.cern.ch/twiki/pub/CMS/RCTDataQualityMonitoring/RCTGCTCAL.jpeg> mapping </a>" }])
