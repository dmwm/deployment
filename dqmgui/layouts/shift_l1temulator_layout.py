def l1temulayout(i, p, *rows): i["00 Shift/L1TEMU/" + p] = DQMItem(layout=rows)

l1temulayout(dqmitems,"00 - uGMT - data vs emulator misMatch ratio",
             [{'path': "L1TEMU/L1TdeStage2uGMT/data_vs_emulator_comparison/mismatchRatio", 'description': "uGMT - data vs emulator misMatch ratio. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTriggerEmulator\">here</a>."}])

l1temulayout(dqmitems,"01 - BMTF - data vs emulator misMatch ratio",
             [{'path': "L1TEMU/L1TdeStage2BMTF/mismatchRatio", 'description': "BMTF - data vs emulator misMatch ratio. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTriggerEmulator\">here</a>."}])

l1temulayout(dqmitems,"02 - OMTF - data vs emulator misMatch ratio",
             [{'path': "L1TEMU/L1TdeStage2OMTF/mismatchRatio", 'description': "OMTF - data vs emulator misMatch ratio. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTriggerEmulator\">here</a>."}])

l1temulayout(dqmitems,"03 - EMTF - data vs emulator misMatch ratio",
             [{'path': "L1TEMU/L1TdeStage2EMTF/mismatchRatio", 'description': "EMTF - data vs emulator misMatch ratio. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTriggerEmulator\">here</a>."}])
