def l1tlayout(i, p, *rows):
    i["00 Shift/L1T/" + p] = DQMItem(layout=rows)

# BVB 20160314: Removed content of old L1T shift workspace from before the trigger upgrade.
# Left an example below as template for upcoming new content based on L1T2016

##l1tlayout(dqmitems,"00 Name of the plot for your shifter",
##    [{
##        'path': "L1T2016/path/to/plot",
##        'description': "Short explanation of the plot for the describe button. For more information please click <a href=\"https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftTrigger\">here</a>."
##    }])
