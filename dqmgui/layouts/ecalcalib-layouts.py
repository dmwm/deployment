def ecalcaliblayout(i, p, *rows): i["EcalCalibration/Layouts/" + p] = DQMItem(layout=rows)
def ecalcaliblclayout(i, p, *rows): i["EcalCalibration/Layouts/00 Light Checker/" + p] = DQMItem(layout=rows)

# Quick Collections
ecalcaliblayout(dqmitems, "00 Laser Sequence Validation",
                [{ 'path': "EcalCalibration/Laser/EcalLaser sequence validation", 'description': "EcalLaser: time, FED number, and status of the laser sequence. Legend: green = good; yellow = warning; red = bad" }])

# Light Checker Layout
ecalcaliblclayout(dqmitems, "00 Laser Sequence Validation",
                [{ 'path': "EcalCalibration/Laser/EcalLaser sequence validation", 'description': "EcalLaser: time, FED number, and status of the laser sequence. Legend: green = good; yellow = warning; red = bad" }])

ecalcaliblclayout(dqmitems, "01 Blue Quantronix (L1) Amplitude",
                  [{ 'path': "EcalCalibration/Laser/EcalLaser L1 amplitude trend", 'description': "Amplitude of the laser measured at the source" }],
                  [{ 'path': "EcalCalibration/Laser/EcalLaser L1 amplitude RMS trend", 'description': "RMS of the amplitude of the laser measured at the source"}])

ecalcaliblclayout(dqmitems, "02 Green (L2) Amplitude",
                  [{ 'path': "EcalCalibration/Laser/EcalLaser L2 amplitude trend", 'description': "Amplitude of the laser measured at the source" }],
                  [{ 'path': "EcalCalibration/Laser/EcalLaser L2 amplitude RMS trend", 'description': "RMS of the amplitude of the laser measured at the source"}])

ecalcaliblclayout(dqmitems, "03 Blue Photonics (L3) Amplitude",
                  [{ 'path': "EcalCalibration/Laser/EcalLaser L3 amplitude trend", 'description': "Amplitude of the laser measured at the source" }],
                  [{ 'path': "EcalCalibration/Laser/EcalLaser L3 amplitude RMS trend", 'description': "RMS of the amplitude of the laser measured at the source"}])

ecalcaliblclayout(dqmitems, "04 Blue Quantronix (L1) Fluctuation",
                  [{ 'path': "EcalCalibration/Laser/EcalLaser L1 jitter trend", 'description': "Jitter of the laser measured at the source"}],
                  [{ 'path': "EcalCalibration/Laser/EcalLaser L1 FWHM trend", 'description': "FWHM of the laser pulse measured at the source"}])

ecalcaliblclayout(dqmitems, "05 Green (L2) Fluctuation",
                  [{ 'path': "EcalCalibration/Laser/EcalLaser L2 jitter trend", 'description': "Jitter of the laser measured at the source"}],
                  [{ 'path': "EcalCalibration/Laser/EcalLaser L2 FWHM trend", 'description': "FWHM of the laser pulse measured at the source"}])

ecalcaliblclayout(dqmitems, "06 Blue Photonics (L3) Fluctuation",
                  [{ 'path': "EcalCalibration/Laser/EcalLaser L3 jitter trend", 'description': "Jitter of the laser measured at the source"}],
                  [{ 'path': "EcalCalibration/Laser/EcalLaser L3 FWHM trend", 'description': "FWHM of the laser pulse measured at the source"}])

ecalcaliblclayout(dqmitems, "07 Timing",
                  [{ 'path': "EcalCalibration/Laser/EcalLaser L1 timing trend", 'description': "Timing of the laser measured at the source"},
                   { 'path': "EcalCalibration/Laser/EcalLaser L2 timing trend", 'description': "Timing of the laser measured at the source"}],
                  [{ 'path': "EcalCalibration/Laser/EcalLaser L3 timing trend", 'description': "Timing of the laser measured at the source"},
                   None])

ecalcaliblclayout(dqmitems, "08 Pre-pulse Amplitude",
                  [{ 'path': "EcalCalibration/Laser/EcalLaser L1 prepulse amplitude trend", 'description': "Amplitude of the pre-pulse of the laser measured at the source"},
                   { 'path': "EcalCalibration/Laser/EcalLaser L2 prepulse amplitude trend", 'description': "Amplitude of the pre-pulse of the laser measured at the source"}],
                  [{ 'path': "EcalCalibration/Laser/EcalLaser L3 prepulse amplitude trend", 'description': "Amplitude of the pre-pulse of the laser measured at the source"},
                   None])

ecalcaliblclayout(dqmitems, "09 Laser Pre-pulse Width",
                  [{ 'path': "EcalCalibration/Laser/EcalLaser L1 prepulse width trend", 'description': "Width of the pre-pulse of the laser measured at the source"},
                   { 'path': "EcalCalibration/Laser/EcalLaser L2 prepulse width trend", 'description': "Width of the pre-pulse of the laser measured at the source"}],
                  [{ 'path': "EcalCalibration/Laser/EcalLaser L3 prepulse width trend", 'description': "Width of the pre-pulse of the laser measured at the source"},
                   None])

ecalcaliblclayout(dqmitems, "10 Laser GPIB Action Duration",
                  [{ 'path': "EcalCalibration/Laser/EcalLaser region move duration", 'description': "" }],
                  [{ 'path': "EcalCalibration/Laser/EcalLaser attenuator change duration", 'description': "" }],
                  [{ 'path': "EcalCalibration/Laser/EcalLaser color change duration", 'description': "" }])

ecalcaliblclayout(dqmitems, "11 Laser Amplitude Map Barrel",
                  [{ 'path': "EcalBarrel/EBLaserTask/Laser1/EBLT amplitude map L1", 'description': "Amplitude of the blue laser measured at the detector"}],
                  [{ 'path': "EcalBarrel/EBLaserTask/Laser4/EBLT amplitude map L4", 'description': "Amplitude of the IR laser measured at the detector"}])

ecalcaliblclayout(dqmitems, "12 Laser Amplitude Map Endcap",
                  [{ 'path': "EcalEndcap/EELaserTask/Laser1/EELT amplitude map L1 EE -", 'description': "Amplitude of the blue laser measured at the detector EE -"},
                   { 'path': "EcalEndcap/EELaserTask/Laser1/EELT amplitude map L1 EE +", 'description': "Amplitude of the blue laser measured at the detector EE +" }],
                  [{ 'path': "EcalEndcap/EELaserTask/Laser4/EELT amplitude map L4 EE -", 'description': "Amplitude of the IR laser measured at the detector EE -"},
                   { 'path': "EcalEndcap/EELaserTask/Laser4/EELT amplitude map L4 EE +", 'description': "Amplitude of the IR laser measured at the detector EE +" }])
