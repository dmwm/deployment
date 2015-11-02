# Dummy check of python syntax within file when run stand-alone
if __name__=="__main__":
    class DQMItem:
        def __init__(self,layout):
            print layout

    dqmitems={}

def shifthcalcaliblayout(i, p, *rows): i["00 Shift/HcalCalib/" + p] = DQMItem(layout=rows)

# BVB:
# This shift layout is clearly not up to date anymore with what is currently
# produced. Since all these plots don't exist and always show up empty and
# the instructions ask not to look at it, it's better to just simply remove
# the folder from the shift folder, so that the shifter doesn't have to wonder
# each time why it's there.
# So I'm commenting them out now.
# If one day it is decided to have the online shifters look at HCAL calibration
# plots again, we can start from here.

##shifthcalcaliblayout(dqmitems, "01 HcalCalib Summary",
##           [{ 'path':"HcalCalib/EventInfo/reportSummaryMap",
##             'description':"This shows the fraction of bad cells in each subdetector.  All subdetectors should appear green.  Values should all be above 98%."}]
##           )
##
##shifthcalcaliblayout(dqmitems, "02 HcalCalib Problem Pedestals",
##                [{ 'path':"HcalCalib/DetDiagPedestalMonitor_Hcal/ ProblemDetDiagPedestal",
##                   'description': "Channels with pedestals that have some kind of problem (bad mean or RMS, unstable, or missing).  This histogram should normally be empty."}]
##                )
##
##shifthcalcaliblayout(dqmitems, "03 HcalCalib Problem Laser",
##                [{ 'path':"HcalCalib/DetDiagLaserMonitor_Hcal/ ProblemDetDiagLaser",
##                   'description': "Channels that are outside reference bounds in either time or energy.  This histogram should normally be empty."}]
##)
##
##shifthcalcaliblayout(dqmitems, "04 HcalCalib Pedestal Reference Comparison",
##                [{'path':"HcalCalib/DetDiagPedestalMonitor_Hcal/Summary Plots/HB Pedestal-Reference Distribution (average over 4 caps)",
##                  'description':"Distribution of calculated pedestals - reference values in the Hcal Barrel detector."},
##                 {'path':"HcalCalib/DetDiagPedestalMonitor_Hcal/Summary Plots/HE Pedestal-Reference Distribution (average over 4 caps)",
##                  'description':"Distribution of calculated pedestals - reference values in the Hcal Endcap detector."}],
##                [{'path':"HcalCalib/DetDiagPedestalMonitor_Hcal/Summary Plots/HF Pedestal-Reference Distribution (average over 4 caps)",
##                'description':"Distribution of calculated pedestals - reference values in the Hcal Forward detector."},
##                 {'path':"HcalCalib/DetDiagPedestalMonitor_Hcal/Summary Plots/HO Pedestal-Reference Distribution (average over 4 caps)",
##                 'description':"Distribution of calculated pedestals - reference values in the Hcal Outer detector."} ]
##                )
##
##shifthcalcaliblayout(dqmitems, "05 HcalCalib Laser RBX Plots",
##                [{ 'path':"HcalCalib/DetDiagLaserMonitor_Hcal/Summary Plots/HB RBX average Time-Ref",
##                   'description':"1D Laser RBX energy - reference in HB"},
##                 { 'path':"HcalCalib/DetDiagLaserMonitor_Hcal/Summary Plots/HE RBX average Time-Ref",
##                   'description':"1D Laser RBX energy - reference in HE"}],
##                [{ 'path':"HcalCalib/DetDiagLaserMonitor_Hcal/Summary Plots/HF RoBox average Time-Ref",
##                   'description':"1D Laser RBX energy - reference in HF"},
##                 { 'path':"HcalCalib/DetDiagLaserMonitor_Hcal/Summary Plots/HO RBX average Time-Ref",
##                   'description':"1D Laser RBX energy - reference in HO"}]
##                )
