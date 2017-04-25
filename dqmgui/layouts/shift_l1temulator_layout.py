def l1temulayout(i, p, *rows): i["00 Shift/L1TEMU/" + p] = DQMItem(layout=rows)

l1temulayout(dqmitems,"00 - uGMT summary - data vs emulator comparison",
             [{'path': "L1TEMU/L1TdeStage2uGMT/data_vs_emulator_comparison/summary", 'description': "uGMT summary - data vs emulator comparison . For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTriggerEmulator\">here</a>."}])

l1temulayout(dqmitems,"01 - BMTF summary - data vs emulator comparison",
             [{'path': "L1TEMU/L1TdeStage2BMTF/summary", 'description': "BMTF summary - data vs emulator comparison . For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTriggerEmulator\">here</a>."}])

l1temulayout(dqmitems,"02 - OMTF summary - data vs emulator comparison",
             [{'path': "L1TEMU/L1TdeStage2OMTF/summary", 'description': "OMTF summary - data vs emulator comparison . For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTriggerEmulator\">here</a>."}])

l1temulayout(dqmitems,"03 - EMTF summary - data vs emulator comparison",
             [{'path': "L1TEMU/L1TdeStage2EMTF/summary", 'description': "EMTF summary - data vs emulator comparison . For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTriggerEmulator\">here</a>."}])
