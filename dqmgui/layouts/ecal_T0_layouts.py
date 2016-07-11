##### ECAL DQM Layout file / Offline DQM #####

def ecallayout(i, p, *rows): i[p] = DQMItem(layout=rows)

#____________________ Layouts ____________________
ecallayout(dqmitems, 'Ecal/Layouts/00 Summary',
	   [{'path': 'EcalBarrel/EBSummaryClient/EB global summary', 'description': 'Summary of the data quality. A channel is red if it is red in any one of RawData, Integrity, Timing, TriggerPrimitives, and HotCells task. A cluster of bad towers in this plot will cause the ReportSummary for the FED to go to 0 in online DQM.'}],
	   [{'path': 'EcalEndcap/EESummaryClient/EE global summary EE -', 'description': 'Summary of the data quality. A channel is red if it is red in any one of RawData, Integrity, Timing, TriggerPrimitives, and HotCells task. A cluster of bad towers in this plot will cause the ReportSummary for the FED to go to 0 in online DQM.'},
	    {'path': 'EcalEndcap/EESummaryClient/EE global summary EE +', 'description': 'Summary of the data quality. A channel is red if it is red in any one of RawData, Integrity, Timing, TriggerPrimitives, and HotCells task. A cluster of bad towers in this plot will cause the ReportSummary for the FED to go to 0 in online DQM.'}])
ecallayout(dqmitems, 'Ecal/Layouts/01 Occupancy Summary',
	   [{'path': 'EcalBarrel/EBOccupancyTask/EBOT digi occupancy','description': 'Digi occupancy.'}],
	   [{'path': 'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE -','description': 'Digi occupancy.'},
	    {'path': 'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE +','description': 'Digi occupancy.'}])
ecallayout(dqmitems, 'Ecal/Layouts/02 Calibration Summary',
	   [{'path': 'EcalBarrel/EBSummaryClient/EB global calibration quality', 'description': 'Summary of the calibration data quality. Channel is red if it is red in any of the Laser 3, Led 1 and 2, and Pedestal gain 12 quality summaries.'}],
	   [{'path': 'EcalEndcap/EESummaryClient/EE global calibration quality EE -', 'description': 'Summary of the calibration data quality. Channel is red if it is red in any of the Laser 3, Led 1 and 2, and Pedestal gain 12 quality summaries.'},
	    {'path': 'EcalEndcap/EESummaryClient/EE global calibration quality EE +', 'description': 'Summary of the calibration data quality. Channel is red if it is red in any of the Laser 3, Led 1 and 2, and Pedestal gain 12 quality summaries.'}])

#____________________ Layouts / 00 Overview ____________________
ecallayout(dqmitems, 'Ecal/Layouts/00 Overview/00 Summary',
	   [{'path': 'EcalBarrel/EBSummaryClient/EB global summary', 'description': 'Summary of the data quality. A channel is red if it is red in any one of RawData, Integrity, Timing, TriggerPrimitives, and HotCells task. A cluster of bad towers in this plot will cause the ReportSummary for the FED to go to 0 in online DQM.'}],
	   [{'path': 'EcalEndcap/EESummaryClient/EE global summary EE -', 'description': 'Summary of the data quality. A channel is red if it is red in any one of RawData, Integrity, Timing, TriggerPrimitives, and HotCells task. A cluster of bad towers in this plot will cause the ReportSummary for the FED to go to 0 in online DQM.'},
	    {'path': 'EcalEndcap/EESummaryClient/EE global summary EE +', 'description': 'Summary of the data quality. A channel is red if it is red in any one of RawData, Integrity, Timing, TriggerPrimitives, and HotCells task. A cluster of bad towers in this plot will cause the ReportSummary for the FED to go to 0 in online DQM.'}])
ecallayout(dqmitems, 'Ecal/Layouts/00 Overview/01 FE Status',
	   [{'path': 'EcalBarrel/EBSummaryClient/EBSFT front-end status summary', 'description': 'Summary of the raw data (DCC and front-end) quality. A channel is red if it has nonzero events with FE status that is different from any of ENABLED, DISABLED, SUPPRESSED, FIFOFULL, FIFOFULL_L1ADESYNC, and FORCEDZS. A FED can also go red if its number of L1A desynchronization errors is greater than 1.0 * log10(total entries).'}],
	   [{'path': 'EcalEndcap/EESummaryClient/EESFT EE - front-end status summary', 'description': 'Summary of the raw data (DCC and front-end) quality. A channel is red if it has nonzero events with FE status that is different from any of ENABLED, DISABLED, SUPPRESSED, FIFOFULL, FIFOFULL_L1ADESYNC, and FORCEDZS. A FED can also go red if its number of L1A desynchronization errors is greater than 1.0 * log10(total entries).'},
	    {'path': 'EcalEndcap/EESummaryClient/EESFT EE + front-end status summary', 'description': 'Summary of the raw data (DCC and front-end) quality. A channel is red if it has nonzero events with FE status that is different from any of ENABLED, DISABLED, SUPPRESSED, FIFOFULL, FIFOFULL_L1ADESYNC, and FORCEDZS. A FED can also go red if its number of L1A desynchronization errors is greater than 1.0 * log10(total entries).'}])
ecallayout(dqmitems, 'Ecal/Layouts/00 Overview/02 Integrity',
	   [{'path': 'EcalBarrel/EBSummaryClient/EBIT integrity quality summary', 'description': 'Summary of the data integrity. A channel is red if more than 0.01 of its entries have integrity errors.'}],
	   [{'path': 'EcalEndcap/EESummaryClient/EEIT EE - integrity quality summary', 'description': 'Summary of the data integrity. A channel is red if more than 0.01 of its entries have integrity errors.'}, 
	    {'path': 'EcalEndcap/EESummaryClient/EEIT EE + integrity quality summary', 'description': 'Summary of the data integrity. A channel is red if more than 0.01 of its entries have integrity errors.'}])
ecallayout(dqmitems, 'Ecal/Layouts/00 Overview/03 Occupancy',
	   [{'path': 'EcalBarrel/EBOccupancyTask/EBOT digi occupancy', 'description': 'Digi occupancy.'}],
	   [{'path': 'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE -', 'description': 'Digi occupancy.'},
	    {'path': 'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE +', 'description': 'Digi occupancy.'}])
ecallayout(dqmitems, 'Ecal/Layouts/00 Overview/04 Noise',
	   [{'path': 'EcalBarrel/EBSummaryClient/EBPOT pedestal quality summary G12', 'description': 'Summary of the presample data quality. A channel is red if presample mean is off by 25.0 from 200.0 or RMS is greater than 3.0. RMS threshold is 6.0 in the forward region (|eta| > 2.1). Channels with entries less than 6 are not considered.'}],
	   [{'path': 'EcalEndcap/EESummaryClient/EEPOT EE - pedestal quality summary G12', 'description': 'Summary of the presample data quality. A channel is red if presample mean is off by 25.0 from 200.0 or RMS is greater than 3.0. RMS threshold is 6.0 in the forward region (|eta| > 2.1). Channels with entries less than 6 are not considered.'},
	    {'path': 'EcalEndcap/EESummaryClient/EEPOT EE + pedestal quality summary G12', 'description': 'Summary of the presample data quality. A channel is red if presample mean is off by 25.0 from 200.0 or RMS is greater than 3.0. RMS threshold is 6.0 in the forward region (|eta| > 2.1). Channels with entries less than 6 are not considered.'}])
ecallayout(dqmitems, 'Ecal/Layouts/00 Overview/05 RecHit Energy',
	   [{'path': 'EcalBarrel/EBSummaryClient/EBOT energy summary', 'description': '2D distribution of the mean rec hit energy.'}],
	   [{'path': 'EcalEndcap/EESummaryClient/EEOT EE - energy summary', 'description': '2D distribution of the mean rec hit energy.'},
	    {'path': 'EcalEndcap/EESummaryClient/EEOT EE + energy summary', 'description': '2D distribution of the mean rec hit energy.'}])
ecallayout(dqmitems, 'Ecal/Layouts/00 Overview/06 Timing',
	   [{'path': 'EcalBarrel/EBSummaryClient/EBTMT timing quality summary', 'description': 'Summary of the timing data quality. A 5x5 tower is red if the mean timing of the tower is off by more than 2.0 or RMS is greater than 6.0 (6.0 and 12.0 in forward region). Towers with total entries less than 15 are not subject to this evaluation. Since 5x5 tower timings are calculated with a tighter time-window than per-channel timings, a tower can additionally become red if its the sum of per-channel timing histogram entries is greater than per-tower histogram entries by factor 1.66666666667 (significant fraction of events fall outside the tight time-window).'}],
	   [{'path': 'EcalEndcap/EESummaryClient/EETMT EE - timing quality summary', 'description': 'Summary of the timing data quality. A 5x5 tower is red if the mean timing of the tower is off by more than 2.0 or RMS is greater than 6.0 (6.0 and 12.0 in forward region). Towers with total entries less than 15 are not subject to this evaluation. Since 5x5 tower timings are calculated with a tighter time-window than per-channel timings, a tower can additionally become red if its the sum of per-channel timing histogram entries is greater than per-tower histogram entries by factor 1.66666666667 (significant fraction of events fall outside the tight time-window).'},
	    {'path': 'EcalEndcap/EESummaryClient/EETMT EE + timing quality summary', 'description': 'Summary of the timing data quality. A 5x5 tower is red if the mean timing of the tower is off by more than 2.0 or RMS is greater than 6.0 (6.0 and 12.0 in forward region). Towers with total entries less than 15 are not subject to this evaluation. Since 5x5 tower timings are calculated with a tighter time-window than per-channel timings, a tower can additionally become red if its the sum of per-channel timing histogram entries is greater than per-tower histogram entries by factor 1.66666666667 (significant fraction of events fall outside the tight time-window).'}])
ecallayout(dqmitems, 'Ecal/Layouts/00 Overview/07 Trigger Primitives',
	   [{'path': 'EcalBarrel/EBSummaryClient/EBTTT emulator error quality summary', 'description': 'Summary of emulator matching quality. A tower is red if the number of events with Et emulation error is greater than 0.1 of total events. Towers with entries less than 3 are not considered.'}],
	   [{'path': 'EcalEndcap/EESummaryClient/EETTT EE - emulator error quality summary', 'description': 'Summary of emulator matching quality. A tower is red if the number of events with Et emulation error is greater than 0.1 of total events. Towers with entries less than 3 are not considered.'},
	    {'path': 'EcalEndcap/EESummaryClient/EETTT EE + emulator error quality summary', 'description': 'Summary of emulator matching quality. A tower is red if the number of events with Et emulation error is greater than 0.1 of total events. Towers with entries less than 3 are not considered.'}])
ecallayout(dqmitems, 'Ecal/Layouts/00 Overview/08 Hot Cells',
	   [{'path': 'EcalBarrel/EBSummaryClient/EBOT hot cell quality summary', 'description': 'Summary of the hot cell monitor. A channel is red if it has more than 100.0 times more entries than phi-ring mean in either digi, rec hit (filtered), or TP digi (filtered). Channels with less than 20 entries are not considered. Channel names of the hot cells are available in (Top) / Ecal / Errors / HotCells.'}],
	   [{'path': 'EcalEndcap/EESummaryClient/EEOT EE - hot cell quality summary', 'description': 'Summary of the hot cell monitor. A channel is red if it has more than 100.0 times more entries than phi-ring mean in either digi, rec hit (filtered), or TP digi (filtered). Channels with less than 20 entries are not considered. Channel names of the hot cells are available in (Top) / Ecal / Errors / HotCells.'},
	    {'path': 'EcalEndcap/EESummaryClient/EEOT EE + hot cell quality summary', 'description': 'Summary of the hot cell monitor. A channel is red if it has more than 100.0 times more entries than phi-ring mean in either digi, rec hit (filtered), or TP digi (filtered). Channels with less than 20 entries are not considered. Channel names of the hot cells are available in (Top) / Ecal / Errors / HotCells.'}])
ecallayout(dqmitems, 'Ecal/Layouts/00 Overview/09 Laser 2 (Green)',
	   [{'path': 'EcalBarrel/EBSummaryClient/EBLT laser quality summary L2', 'description': 'Summary of the laser data quality. A channel is red either if mean / expected < 0.1, or if mean / expected > 2.06, or if RMS / expected > 0.3, or if mean timing is off from expected by 0.5. Expected amplitudes and timings are 1700.0, 1300.0, 1700.0, 1700.0 and 4.2, 4.2, 4.2, 4.2 for lasers 1, 2, 3, and 4 respectively. Channels with less than 3 are not considered.'}],
	   [{'path': 'EcalEndcap/EESummaryClient/EELT EE - laser quality summary L2', 'description': 'Summary of the laser data quality. A channel is red either if mean / expected < 0.1, or if mean / expected > 2.06, or if RMS / expected > 0.3, or if mean timing is off from expected by 0.5. Expected amplitudes and timings are 1700.0, 1300.0, 1700.0, 1700.0 and 4.2, 4.2, 4.2, 4.2 for lasers 1, 2, 3, and 4 respectively. Channels with less than 3 are not considered.'},
	    {'path': 'EcalEndcap/EESummaryClient/EELT EE + laser quality summary L2', 'description': 'Summary of the laser data quality. A channel is red either if mean / expected < 0.1, or if mean / expected > 2.06, or if RMS / expected > 0.3, or if mean timing is off from expected by 0.5. Expected amplitudes and timings are 1700.0, 1300.0, 1700.0, 1700.0 and 4.2, 4.2, 4.2, 4.2 for lasers 1, 2, 3, and 4 respectively. Channels with less than 3 are not considered.'}])
ecallayout(dqmitems, 'Ecal/Layouts/00 Overview/09 Laser 3 (Blue)',
	   [{'path': 'EcalBarrel/EBSummaryClient/EBLT laser quality summary L3', 'description': 'Summary of the laser data quality. A channel is red either if mean / expected < 0.1, or if mean / expected > 2.06, or if RMS / expected > 0.3, or if mean timing is off from expected by 0.5. Expected amplitudes and timings are 1700.0, 1300.0, 1700.0, 1700.0 and 4.2, 4.2, 4.2, 4.2 for lasers 1, 2, 3, and 4 respectively. Channels with less than 3 are not considered.'}],
	   [{'path': 'EcalEndcap/EESummaryClient/EELT EE - laser quality summary L3', 'description': 'Summary of the laser data quality. A channel is red either if mean / expected < 0.1, or if mean / expected > 2.06, or if RMS / expected > 0.3, or if mean timing is off from expected by 0.5. Expected amplitudes and timings are 1700.0, 1300.0, 1700.0, 1700.0 and 4.2, 4.2, 4.2, 4.2 for lasers 1, 2, 3, and 4 respectively. Channels with less than 3 are not considered.'},
	    {'path': 'EcalEndcap/EESummaryClient/EELT EE + laser quality summary L3', 'description': 'Summary of the laser data quality. A channel is red either if mean / expected < 0.1, or if mean / expected > 2.06, or if RMS / expected > 0.3, or if mean timing is off from expected by 0.5. Expected amplitudes and timings are 1700.0, 1300.0, 1700.0, 1700.0 and 4.2, 4.2, 4.2, 4.2 for lasers 1, 2, 3, and 4 respectively. Channels with less than 3 are not considered.'}])
ecallayout(dqmitems, 'Ecal/Layouts/00 Overview/10 Laser 2 PN',
	   [{'path': 'EcalBarrel/EBSummaryClient/EBLT PN laser quality summary L2', 'description': 'Summary of the laser data quality in the PN diodes. A channel is red if mean / expected < 0.1 or RMS / expected > 1.0. Expected amplitudes are 800.0, 800.0, 800.0, 800.0 for laser 1, 2, 3, and 4 respectively. Channels with less than 3 are not considered.'}],
	   [{'path': 'EcalEndcap/EESummaryClient/EELT PN laser quality summary L2', 'description': 'Summary of the laser data quality in the PN diodes. A channel is red if mean / expected < 0.1 or RMS / expected > 1.0. Expected amplitudes are 800.0, 800.0, 800.0, 800.0 for laser 1, 2, 3, and 4 respectively. Channels with less than 3 are not considered.'}])
ecallayout(dqmitems, 'Ecal/Layouts/00 Overview/10 Laser 3 PN',
	   [{'path': 'EcalBarrel/EBSummaryClient/EBLT PN laser quality summary L3', 'description': 'Summary of the laser data quality in the PN diodes. A channel is red if mean / expected < 0.1 or RMS / expected > 1.0. Expected amplitudes are 800.0, 800.0, 800.0, 800.0 for laser 1, 2, 3, and 4 respectively. Channels with less than 3 are not considered.'}],
	   [{'path': 'EcalEndcap/EESummaryClient/EELT PN laser quality summary L3', 'description': 'Summary of the laser data quality in the PN diodes. A channel is red if mean / expected < 0.1 or RMS / expected > 1.0. Expected amplitudes are 800.0, 800.0, 800.0, 800.0 for laser 1, 2, 3, and 4 respectively. Channels with less than 3 are not considered.'}])
ecallayout(dqmitems, 'Ecal/Layouts/00 Overview/11 Test Pulse PN G16',
	   [{'path': 'EcalBarrel/EBSummaryClient/EBTPT PN test pulse quality G16 summary', 'description': 'Summary of test pulse data quality for PN diodes. A channel is red if mean amplitude is lower than the threshold, or RMS is greater than threshold. The mean and RMS thresholds are 12.5, 200.0 and 20.0, 20.0 for gains 1 and 16 respectively. Channels with entries less than 3 are not considered.'}],
	   [{'path': 'EcalEndcap/EESummaryClient/EETPT PN test pulse quality G16 summary', 'description': 'Summary of test pulse data quality for PN diodes. A channel is red if mean amplitude is lower than the threshold, or RMS is greater than threshold. The mean and RMS thresholds are 12.5, 200.0 and 20.0, 20.0 for gains 1 and 16 respectively. Channels with entries less than 3 are not considered.'}])
ecallayout(dqmitems, 'Ecal/Layouts/00 Overview/12 Led 1',
	   [{'path': 'EcalEndcap/EESummaryClient/EELDT EE - led quality summary L1', 'description': 'Summary of the led data quality. A channel is red either if mean / expected < 0.1, or if RMS / expected > 0.5, or if mean timing is off from expected by 1.0. Expected amplitudes and timings are 200.0, 10.0 and 4.4, 4.5 for leds 1 and 2 respectively. Channels with less than 3 are not considered.'},
	    {'path': 'EcalEndcap/EESummaryClient/EELDT EE + led quality summary L1', 'description': 'Summary of the led data quality. A channel is red either if mean / expected < 0.1, or if RMS / expected > 0.5, or if mean timing is off from expected by 1.0. Expected amplitudes and timings are 200.0, 10.0 and 4.4, 4.5 for leds 1 and 2 respectively. Channels with less than 3 are not considered.'}])
ecallayout(dqmitems, 'Ecal/Layouts/00 Overview/12 Led 2',
	   [{'path': 'EcalEndcap/EESummaryClient/EELDT EE - led quality summary L2', 'description': 'Summary of the led data quality. A channel is red either if mean / expected < 0.1, or if RMS / expected > 0.5, or if mean timing is off from expected by 1.0. Expected amplitudes and timings are 200.0, 10.0 and 4.4, 4.5 for leds 1 and 2 respectively. Channels with less than 3 are not considered.'},
	    {'path': 'EcalEndcap/EESummaryClient/EELDT EE + led quality summary L2', 'description': 'Summary of the led data quality. A channel is red either if mean / expected < 0.1, or if RMS / expected > 0.5, or if mean timing is off from expected by 1.0. Expected amplitudes and timings are 200.0, 10.0 and 4.4, 4.5 for leds 1 and 2 respectively. Channels with less than 3 are not considered.'}])
ecallayout(dqmitems, 'Ecal/Layouts/00 Overview/13 Led 1 PN',
	   [{'path': 'EcalEndcap/EESummaryClient/EELDT PN led quality summary L1', 'description': 'Summary of the led data quality in the PN diodes. A channel is red if mean / expected < 0.1 or RMS / expected > 1.0. Expected amplitudes are 800.0, 800.0 for led 1 and 2 respectively. Channels with less than 3 are not considered.'}])
ecallayout(dqmitems, 'Ecal/Layouts/00 Overview/13 Led 2 PN',
	   [{'path': 'EcalEndcap/EESummaryClient/EELDT PN led quality summary L2', 'description': 'Summary of the led data quality in the PN diodes. A channel is red if mean / expected < 0.1 or RMS / expected > 1.0. Expected amplitudes are 800.0, 800.0 for led 1 and 2 respectively. Channels with less than 3 are not considered.'}])
ecallayout(dqmitems, 'Ecal/Layouts/00 Overview/14 Error Trends',
	   [{'path': 'Ecal/Trends/RawDataTask accumulated number of sync errors', 'description': 'Accumulated trend of the number of synchronization errors (L1A & BX mismatches) between DCC and FE in this run.'}],[{'path': 'Ecal/Trends/IntegrityTask number of integrity errors', 'description': 'Trend of the number of integrity errors.'}])

#____________________ Layouts / 01 Raw Data ____________________
ecallayout(dqmitems, 'Ecal/Layouts/01 Raw Data/00 FEStatus Summary',
	   [{'path': 'EcalBarrel/EBSummaryClient/EBSFT front-end status summary', 'description': 'Summary of the raw data (DCC and front-end) quality. A channel is red if it has nonzero events with FE status that is different from any of ENABLED, DISABLED, SUPPRESSED, FIFOFULL, FIFOFULL_L1ADESYNC, and FORCEDZS. A FED can also go red if its number of L1A desynchronization errors is greater than 1.0 * log10(total entries).'}],
	   [{'path': 'EcalEndcap/EESummaryClient/EESFT EE - front-end status summary', 'description': 'Summary of the raw data (DCC and front-end) quality. A channel is red if it has nonzero events with FE status that is different from any of ENABLED, DISABLED, SUPPRESSED, FIFOFULL, FIFOFULL_L1ADESYNC, and FORCEDZS. A FED can also go red if its number of L1A desynchronization errors is greater than 1.0 * log10(total entries).'},
	    {'path': 'EcalEndcap/EESummaryClient/EESFT EE + front-end status summary', 'description': 'Summary of the raw data (DCC and front-end) quality. A channel is red if it has nonzero events with FE status that is different from any of ENABLED, DISABLED, SUPPRESSED, FIFOFULL, FIFOFULL_L1ADESYNC, and FORCEDZS. A FED can also go red if its number of L1A desynchronization errors is greater than 1.0 * log10(total entries).'}])
ecallayout(dqmitems, 'Ecal/Layouts/01 Raw Data/01 Total FE Sync Errors',
	   [{'path': 'EcalBarrel/EBRawDataTask/EBRDT total FE synchronization errors', 'description': 'Total number of synchronization errors (L1A & BX mismatches) between DCC and FE.'}],
	   [{'path': 'EcalEndcap/EERawDataTask/EERDT total FE synchronization errors', 'description': 'Total number of synchronization errors (L1A & BX mismatches) between DCC and FE.'}])
ecallayout(dqmitems, 'Ecal/Layouts/01 Raw Data/02 FE Errors in this LS',
	   [{'path': 'EcalBarrel/EBRawDataTask/EBRDT FE synchronization errors by lumi', 'description': 'Total number of synchronization errors (L1A & BX mismatches) between DCC and FE in this lumi section.'},
	    {'path': 'EcalBarrel/EBStatusFlagsTask/FEStatus/EBSFT weighted frontend errors by lumi', 'description': 'Total number of front-ends in error status in this lumi section.'}],
	   [{'path': 'EcalEndcap/EERawDataTask/EERDT FE synchronization errors by lumi', 'description': 'Total number of synchronization errors (L1A & BX mismatches) between DCC and FE in this lumi section.'},
	    {'path': 'EcalEndcap/EEStatusFlagsTask/FEStatus/EESFT weighted frontend errors by lumi', 'description': 'Total number of front-ends in error status in this lumi section.'}])
ecallayout(dqmitems, 'Ecal/Layouts/01 Raw Data/03 Integrity Summary',
	   [{'path': 'EcalBarrel/EBSummaryClient/EBIT integrity quality summary', 'description': 'Summary of the data integrity. A channel is red if more than 0.01 of its entries have integrity errors.'}],
	   [{'path': 'EcalEndcap/EESummaryClient/EEIT EE - integrity quality summary', 'description': 'Summary of the data integrity. A channel is red if more than 0.01 of its entries have integrity errors.'},
	    {'path': 'EcalEndcap/EESummaryClient/EEIT EE + integrity quality summary', 'description': 'Summary of the data integrity. A channel is red if more than 0.01 of its entries have integrity errors.'}])
ecallayout(dqmitems, 'Ecal/Layouts/01 Raw Data/04 Total Integrity Errors',
	   [{'path': 'EcalBarrel/EBSummaryClient/EBIT integrity quality errors summary', 'description': 'Total number of integrity errors for each FED.'}],
	   [{'path': 'EcalEndcap/EESummaryClient/EEIT integrity quality errors summary', 'description': 'Total number of integrity errors for each FED.'}])
ecallayout(dqmitems, 'Ecal/Layouts/01 Raw Data/05 Integrity Errors in this LS',
	   [{'path': 'EcalBarrel/EBIntegrityTask/EBIT weighted integrity errors by lumi', 'description': 'Total number of integrity errors for each FED in this lumi section.'}],
	   [{'path': 'EcalEndcap/EEIntegrityTask/EEIT weighted integrity errors by lumi', 'description': 'Total number of integrity errors for each FED in this lumi section.'}])
ecallayout(dqmitems, 'Ecal/Layouts/01 Raw Data/06 Error Trends',
	   [{'path': 'Ecal/Trends/RawDataTask accumulated number of sync errors', 'description': 'Accumulated trend of the number of synchronization errors (L1A & BX mismatches) between DCC and FE in this run.'}],
	   [{'path': 'Ecal/Trends/IntegrityTask number of integrity errors', 'description': 'Trend of the number of integrity errors.'}])
ecallayout(dqmitems, 'Ecal/Layouts/01 Raw Data/07 Event Type',
	   [{'path': 'EcalBarrel/EBRawDataTask/EBRDT event type pre calibration BX', 'description': 'Event type recorded in the DCC for events in bunch crossing < 3490'}, {'path': 'EcalBarrel/EBRawDataTask/EBRDT event type calibration BX', 'description': 'Event type recorded in the DCC for events in bunch crossing == 3490. This plot is filled using data from the physics data stream during physics runs. It is normal to have very few entries in these cases.'},
	    {'path': 'EcalBarrel/EBRawDataTask/EBRDT event type post calibration BX', 'description': 'Event type recorded in the DCC for events in bunch crossing > 3490.'}],
	   [{'path': 'EcalEndcap/EERawDataTask/EERDT event type pre calibration BX', 'description': 'Event type recorded in the DCC for events in bunch crossing < 3490'}, {'path': 'EcalEndcap/EERawDataTask/EERDT event type calibration BX', 'description': 'Event type recorded in the DCC for events in bunch crossing == 3490. This plot is filled using data from the physics data stream during physics runs. It is normal to have very few entries in these cases.'},
	    {'path': 'EcalEndcap/EERawDataTask/EERDT event type post calibration BX', 'description': 'Event type recorded in the DCC for events in bunch crossing > 3490.'}])
ecallayout(dqmitems, 'Ecal/Layouts/01 Raw Data/08 FED Entries',
	   [{'path': 'EcalBarrel/EBRawDataTask/EBRDT raw data entries', 'description': 'Number of events recorded by each FED.'}],
 	   [{'path': 'EcalEndcap/EERawDataTask/EERDT raw data entries', 'description': 'Number of events recorded by each FED.'}])
ecallayout(dqmitems, 'Ecal/Layouts/01 Raw Data/09 Channel Status Map',
	   [{'path': 'EcalBarrel/EBIntegrityClient/EBIT channel status map', 'description': 'Map of channel status as given by the Ecal Channel Status Record. LEGEND:<br/>0: Channel ok,<br/>1: DAC settings problem, pedestal not in the design range,<br/>2: Channel with no laser, ok elsewhere,<br/>3: Noisy,<br/>4: Very noisy,<br/>5-7: Reserved for more categories of noisy channels,<br/>8: Channel at fixed gain 6 (or 6 and 1),<br/>9: Channel at fixed gain 1,<br/>10: Channel at fixed gain 0 (dead of type this),<br/>11: Non-responding isolated channel (dead of type other),<br/>12: Channel and one or more neigbors not responding (e.g.: in a dead VFE 5x1 channel),<br/>13: Channel in TT with no data link, TP data ok,<br/>14: Channel in TT with no data link and no TP data.'}],
	   [{'path': 'EcalEndcap/EEIntegrityClient/EEIT EE - channel status map', 'description': 'Map of channel status as given by the Ecal Channel Status Record. LEGEND:<br/>0: Channel ok,<br/>1: DAC settings problem, pedestal not in the design range,<br/>2: Channel with no laser, ok elsewhere,<br/>3: Noisy,<br/>4: Very noisy,<br/>5-7: Reserved for more categories of noisy channels,<br/>8: Channel at fixed gain 6 (or 6 and 1),<br/>9: Channel at fixed gain 1,<br/>10: Channel at fixed gain 0 (dead of type this),<br/>11: Non-responding isolated channel (dead of type other),<br/>12: Channel and one or more neigbors not responding (e.g.: in a dead VFE 5x1 channel),<br/>13: Channel in TT with no data link, TP data ok,<br/>14: Channel in TT with no data link and no TP data.'},
	    {'path': 'EcalEndcap/EEIntegrityClient/EEIT EE + channel status map', 'description': 'Map of channel status as given by the Ecal Channel Status Record. LEGEND:<br/>0: Channel ok,<br/>1: DAC settings problem, pedestal not in the design range,<br/>2: Channel with no laser, ok elsewhere,<br/>3: Noisy,<br/>4: Very noisy,<br/>5-7: Reserved for more categories of noisy channels,<br/>8: Channel at fixed gain 6 (or 6 and 1),<br/>9: Channel at fixed gain 1,<br/>10: Channel at fixed gain 0 (dead of type this),<br/>11: Non-responding isolated channel (dead of type other),<br/>12: Channel and one or more neigbors not responding (e.g.: in a dead VFE 5x1 channel),<br/>13: Channel in TT with no data link, TP data ok,<br/>14: Channel in TT with no data link and no TP data.'}])
ecallayout(dqmitems, 'Ecal/Layouts/01 Raw Data/Desync Errors/00 CRC',
	   [{'path': 'EcalBarrel/EBRawDataTask/EBRDT CRC errors', 'description': 'Number of CRC errors.'}],
	   [{'path': 'EcalEndcap/EERawDataTask/EERDT CRC errors', 'description': 'Number of CRC errors.'}])
ecallayout(dqmitems, 'Ecal/Layouts/01 Raw Data/Desync Errors/01 DCC-GT Mismatch',
	   [{'path': 'EcalBarrel/EBRawDataTask/EBRDT run number errors', 'description': 'Number of discrepancies between run numbers recorded in the DCC and that in CMS Event.'},
	    {'path': 'EcalBarrel/EBRawDataTask/EBRDT orbit number errors', 'description': 'Number of discrepancies between LHC orbit numbers recorded in the DCC and that in CMS Event.'}],
	   [{'path': 'EcalEndcap/EERawDataTask/EERDT run number errors', 'description': 'Number of discrepancies between run numbers recorded in the DCC and that in CMS Event.'},
	    {'path': 'EcalEndcap/EERawDataTask/EERDT orbit number errors', 'description': 'Number of discrepancies between LHC orbit numbers recorded in the DCC and that in CMS Event.'}])
ecallayout(dqmitems, 'Ecal/Layouts/01 Raw Data/Desync Errors/02 DCC-GT Mismatch',
	   [{'path': 'EcalBarrel/EBRawDataTask/EBRDT bunch crossing DCC errors', 'description': 'Number of discrepancies between bunch crossing numbers recorded in the DCC and that in CMS Event.'},
	    {'path': 'EcalBarrel/EBRawDataTask/EBRDT L1A DCC errors', 'description': 'Number of discrepancies between L1A recorded in the DCC and that in CMS Event.'}, 
	    {'path': 'EcalBarrel/EBRawDataTask/EBRDT trigger type errors', 'description': 'Number of discrepancies between trigger type recorded in the DCC and that in CMS Event.'}],
	   [{'path': 'EcalEndcap/EERawDataTask/EERDT bunch crossing DCC errors', 'description': 'Number of discrepancies between bunch crossing numbers recorded in the DCC and that in CMS Event.'},
	    {'path': 'EcalEndcap/EERawDataTask/EERDT L1A DCC errors', 'description': 'Number of discrepancies between L1A recorded in the DCC and that in CMS Event.'},
	    {'path': 'EcalEndcap/EERawDataTask/EERDT trigger type errors', 'description': 'Number of discrepancies between trigger type recorded in the DCC and that in CMS Event.'}])
ecallayout(dqmitems, 'Ecal/Layouts/01 Raw Data/Desync Errors/03 DCC-TCC Mismatch',
	   [{'path': 'EcalBarrel/EBRawDataTask/EBRDT bunch crossing TCC errors', 'description': 'Number of bunch corssing value mismatches between DCC and TCC.'},
	    {'path': 'EcalBarrel/EBRawDataTask/EBRDT L1A TCC errors', 'description': 'Number of L1A value mismatches between DCC and TCC.'}],
	   [{'path': 'EcalEndcap/EERawDataTask/EERDT bunch crossing TCC errors', 'description': 'Number of bunch corssing value mismatches between DCC and TCC.'},
	    {'path': 'EcalEndcap/EERawDataTask/EERDT L1A TCC errors', 'description': 'Number of L1A value mismatches between DCC and TCC.'}])
ecallayout(dqmitems, 'Ecal/Layouts/01 Raw Data/Desync Errors/04 DCC-SRP Mismatch',
	   [{'path': 'EcalBarrel/EBRawDataTask/EBRDT bunch crossing SRP errors', 'description': 'Number of bunch crossing value mismatches between DCC and SRP.'},
	    {'path': 'EcalBarrel/EBRawDataTask/EBRDT L1A SRP errors', 'description': 'Number of L1A value mismatches between DCC and SRP.'}],
	   [{'path': 'EcalEndcap/EERawDataTask/EERDT bunch crossing SRP errors', 'description': 'Number of bunch crossing value mismatches between DCC and SRP.'},
	    {'path': 'EcalEndcap/EERawDataTask/EERDT L1A SRP errors', 'description': 'Number of L1A value mismatches between DCC and SRP.'}])
ecallayout(dqmitems, 'Ecal/Layouts/01 Raw Data/Desync Errors/05 DCC-FE Mismatch',
	   [{'path': 'EcalBarrel/EBRawDataTask/EBRDT bunch crossing FE errors', 'description': 'Number of bunch crossing value mismatches between DCC and FE.'},
	    {'path': 'EcalBarrel/EBRawDataTask/EBRDT L1A FE errors', 'description': 'Number of L1A value mismatches between DCC and FE.'}],
	   [{'path': 'EcalEndcap/EERawDataTask/EERDT bunch crossing FE errors', 'description': 'Number of bunch crossing value mismatches between DCC and FE.'},
	    {'path': 'EcalEndcap/EERawDataTask/EERDT L1A FE errors', 'description': 'Number of L1A value mismatches between DCC and FE.'}])
# By SuperModule _______________
for (detector, label, maxchannel) in [('Endcap', 'EE', 9), ('Barrel', 'EB', 18)]: # Loop over EB,EE
  for sign in ['-', '+']: # Loop over z-side
    for channel in range(1, maxchannel+1): # Loop over channels
      channellabel = '%s%s%02d' % (label, sign, channel) # e.g. "EE+05"
      ecallayout(dqmitems,'Ecal/Layouts/01 Raw Data/By SuperModule/Integrity Quality/Integrity %s' % channellabel,
                 [{'path': 'Ecal%s/%sIntegrityClient/%sIT data integrity quality %s' % (detector, label, label, channellabel),
                   'description': 'Summary of the data integrity. A channel is red if more than 0.01 of its entries have integrity errors.'}])
      ecallayout(dqmitems,'Ecal/Layouts/01 Raw Data/By SuperModule/FEStatus/FE Status Flags %s' % channellabel,
                 [{'path': 'Ecal%s/%sStatusFlagsTask/FEStatus/%sSFT front-end status bits %s' % (detector, label, label, channellabel),
                   'description': 'FE status counter.'}])

#____________________ Layouts / 02 Occupancy ____________________
ecallayout(dqmitems, 'Ecal/Layouts/02 Occupancy/00 Hot Cells',
	   [{'path': 'EcalBarrel/EBSummaryClient/EBOT hot cell quality summary', 'description': 'Summary of the hot cell monitor. A channel is red if it has more than 100.0 times more entries than phi-ring mean in either digi, rec hit (filtered), or TP digi (filtered). Channels with less than 20 entries are not considered. Channel names of the hot cells are available in (Top) / Ecal / Errors / HotCells.'}],
	   [{'path': 'EcalEndcap/EESummaryClient/EEOT EE - hot cell quality summary', 'description': 'Summary of the hot cell monitor. A channel is red if it has more than 100.0 times more entries than phi-ring mean in either digi, rec hit (filtered), or TP digi (filtered). Channels with less than 20 entries are not considered. Channel names of the hot cells are available in (Top) / Ecal / Errors / HotCells.'},
	    {'path': 'EcalEndcap/EESummaryClient/EEOT EE + hot cell quality summary', 'description': 'Summary of the hot cell monitor. A channel is red if it has more than 100.0 times more entries than phi-ring mean in either digi, rec hit (filtered), or TP digi (filtered). Channels with less than 20 entries are not considered. Channel names of the hot cells are available in (Top) / Ecal / Errors / HotCells.'}])
ecallayout(dqmitems, 'Ecal/Layouts/02 Occupancy/01 Digi EB',
	   [{'path': 'EcalBarrel/EBOccupancyTask/EBOT digi occupancy', 'description': 'Digi occupancy.'}],
	   [{'path': 'EcalBarrel/EBOccupancyTask/EBOT digi occupancy projection eta', 'description': 'Projection of digi occupancy.'},
	    {'path': 'EcalBarrel/EBOccupancyTask/EBOT digi occupancy projection phi', 'description': 'Projection of digi occupancy.'}])
ecallayout(dqmitems, 'Ecal/Layouts/02 Occupancy/02 Digi EE -',
	   [{'path': 'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE -', 'description': 'Digi occupancy.'}],
	   [{'path': 'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE - projection eta', 'description': 'Projection of digi occupancy.'},
	    {'path': 'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE - projection phi', 'description': 'Projection of digi occupancy.'}])
ecallayout(dqmitems, 'Ecal/Layouts/02 Occupancy/03 Digi EE +',
	   [{'path': 'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE +', 'description': 'Digi occupancy.'}],
	   [{'path': 'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE + projection eta', 'description': 'Projection of digi occupancy.'},
	    {'path': 'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE + projection phi', 'description': 'Projection of digi occupancy.'}])
ecallayout(dqmitems, 'Ecal/Layouts/02 Occupancy/04 RecHit EB',
	   [{'path': 'EcalBarrel/EBOccupancyTask/EBOT rec hit occupancy', 'description': 'Rec hit occupancy.'}],
	   [{'path': 'EcalBarrel/EBOccupancyTask/EBOT rec hit occupancy projection eta', 'description': 'Projection of the occupancy of all rec hits.'},
	    {'path': 'EcalBarrel/EBOccupancyTask/EBOT rec hit occupancy projection phi', 'description': 'Projection of the rec hit occupancy.'}])
ecallayout(dqmitems, 'Ecal/Layouts/02 Occupancy/05 RecHit EE -',
	   [{'path': 'EcalEndcap/EEOccupancyTask/EEOT rec hit occupancy EE -', 'description': 'Rec hit occupancy.'}],
	   [{'path': 'EcalEndcap/EEOccupancyTask/EEOT rec hit occupancy EE - projection eta', 'description': 'Projection of the occupancy of all rec hits.'},
	    {'path': 'EcalEndcap/EEOccupancyTask/EEOT rec hit occupancy EE - projection phi', 'description': 'Projection of the rec hit occupancy.'}])
ecallayout(dqmitems, 'Ecal/Layouts/02 Occupancy/06 RecHit EE +',
	   [{'path': 'EcalEndcap/EEOccupancyTask/EEOT rec hit occupancy EE +', 'description': 'Rec hit occupancy.'}],
	   [{'path': 'EcalEndcap/EEOccupancyTask/EEOT rec hit occupancy EE + projection eta', 'description': 'Projection of the occupancy of all rec hits.'},
	    {'path': 'EcalEndcap/EEOccupancyTask/EEOT rec hit occupancy EE + projection phi', 'description': 'Projection of the rec hit occupancy.'}])
ecallayout(dqmitems, 'Ecal/Layouts/02 Occupancy/07 RecHit (Filtered) EB',
	   [{'path': 'EcalBarrel/EBOccupancyTask/EBOT rec hit thr occupancy', 'description': 'Occupancy for rec hits with GOOD reconstruction flag and E > 0.5 GeV.'}],
	   [{'path': 'EcalBarrel/EBOccupancyTask/EBOT rec hit thr occupancy projection eta', 'description': 'Projection of the occupancy of rec hits with GOOD reconstruction flag and E > 0.5 GeV.'},
	    {'path': 'EcalBarrel/EBOccupancyTask/EBOT rec hit thr occupancy projection phi', 'description': 'Projection of the occupancy of rec hits with GOOD reconstruction flag and E > 0.5 GeV.'}])
ecallayout(dqmitems, 'Ecal/Layouts/02 Occupancy/08 RecHit (Filtered) EE -',
	   [{'path': 'EcalEndcap/EEOccupancyTask/EEOT rec hit thr occupancy EE -', 'description': 'Occupancy for rec hits with GOOD reconstruction flag and E > 0.5 GeV.'}],
	   [{'path': 'EcalEndcap/EEOccupancyTask/EEOT rec hit thr occupancy EE - projection eta', 'description': 'Projection of the occupancy of rec hits with GOOD reconstruction flag and E > 0.5 GeV.'},
	    {'path': 'EcalEndcap/EEOccupancyTask/EEOT rec hit thr occupancy EE - projection phi', 'description': 'Projection of the occupancy of rec hits with GOOD reconstruction flag and E > 0.5 GeV.'}])
ecallayout(dqmitems, 'Ecal/Layouts/02 Occupancy/09 RecHit (Filtered) EE +',
	   [{'path': 'EcalEndcap/EEOccupancyTask/EEOT rec hit thr occupancy EE +', 'description': 'Occupancy for rec hits with GOOD reconstruction flag and E > 0.5 GeV.'}],
	   [{'path': 'EcalEndcap/EEOccupancyTask/EEOT rec hit thr occupancy EE + projection eta', 'description': 'Projection of the occupancy of rec hits with GOOD reconstruction flag and E > 0.5 GeV.'},
	    {'path': 'EcalEndcap/EEOccupancyTask/EEOT rec hit thr occupancy EE + projection phi', 'description': 'Projection of the occupancy of rec hits with GOOD reconstruction flag and E > 0.5 GeV.'}])
ecallayout(dqmitems, 'Ecal/Layouts/02 Occupancy/10 Trigger Primitive (Filtered) EB',
	   [{'path': 'EcalBarrel/EBOccupancyTask/EBOT TP digi thr occupancy', 'description': 'Occupancy for TP digis with Et > 4.0 GeV.'}],
	   [{'path': 'EcalBarrel/EBOccupancyTask/EBOT TP digi thr occupancy projection eta', 'description': 'Projection of the occupancy of TP digis with Et > 4.0 GeV.'},
	    {'path': 'EcalBarrel/EBOccupancyTask/EBOT TP digi thr occupancy projection phi', 'description': 'Projection of the occupancy of TP digis with Et > 4.0 GeV.'}])
ecallayout(dqmitems, 'Ecal/Layouts/02 Occupancy/11 Trigger Primitive (Filtered) EE -',
	   [{'path': 'EcalEndcap/EEOccupancyTask/EEOT TP digi thr occupancy EE -', 'description': 'Occupancy for TP digis with Et > 4.0 GeV.'}],
	   [{'path': 'EcalEndcap/EEOccupancyTask/EEOT TP digi thr occupancy EE - projection eta', 'description': 'Projection of the occupancy of TP digis with Et > 4.0 GeV.'},
	    {'path': 'EcalEndcap/EEOccupancyTask/EEOT TP digi thr occupancy EE - projection phi', 'description': 'Projection of the occupancy of TP digis with Et > 4.0 GeV.'}])
ecallayout(dqmitems, 'Ecal/Layouts/02 Occupancy/12 Trigger Primitive (Filtered) EE +',
	   [{'path': 'EcalEndcap/EEOccupancyTask/EEOT TP digi thr occupancy EE +', 'description': 'Occupancy for TP digis with Et > 4.0 GeV.'}],
	   [{'path': 'EcalEndcap/EEOccupancyTask/EEOT TP digi thr occupancy EE + projection eta', 'description': 'Projection of the occupancy of TP digis with Et > 4.0 GeV.'},
	    {'path': 'EcalEndcap/EEOccupancyTask/EEOT TP digi thr occupancy EE + projection phi', 'description': 'Projection of the occupancy of TP digis with Et > 4.0 GeV.'}])
ecallayout(dqmitems, 'Ecal/Layouts/02 Occupancy/13 Basic Cluster EB',
	   [{'path': 'EcalBarrel/EBClusterTask/EBCLT BC number map', 'description': 'Basic cluster occupancy.'}],
	   [{'path': 'EcalBarrel/EBClusterTask/EBCLT BC number projection eta', 'description': 'Projection of the basic cluster occupancy.'},
	    {'path': 'EcalBarrel/EBClusterTask/EBCLT BC number projection phi', 'description': 'Projection of the basic cluster occupancy.'}])
ecallayout(dqmitems, 'Ecal/Layouts/02 Occupancy/14 Basic Cluster EE -',
	   [{'path': 'EcalEndcap/EEClusterTask/EECLT BC number map EE -', 'description': 'Basic cluster occupancy.'}],
	   [{'path': 'EcalEndcap/EEClusterTask/EECLT BC number projection eta EE -', 'description': 'Projection of the basic cluster occupancy.'},
	    {'path': 'EcalEndcap/EEClusterTask/EECLT BC number projection phi EE -', 'description': 'Projection of the basic cluster occupancy.'}])
ecallayout(dqmitems, 'Ecal/Layouts/02 Occupancy/15 Basic Cluster EE +',
	   [{'path': 'EcalEndcap/EEClusterTask/EECLT BC number map EE +', 'description': 'Basic cluster occupancy.'}],
	   [{'path': 'EcalEndcap/EEClusterTask/EECLT BC number projection eta EE +', 'description': 'Projection of the basic cluster occupancy.'},
	    {'path': 'EcalEndcap/EEClusterTask/EECLT BC number projection phi EE +', 'description': 'Projection of the basic cluster occupancy.'}])
ecallayout(dqmitems, 'Ecal/Layouts/02 Occupancy/16 Hit Multiplicity',
	   [{'path': 'EcalBarrel/EBOccupancyTask/EBOT number of digis in event', 'description': 'Distribution of the number of digis per event.'},
	    {'path': 'EcalBarrel/EBOccupancyTask/EBOT number of filtered rec hits in event', 'description': 'Occupancy of rec hits with GOOD reconstruction flag and E > 0.5 GeV.'}],
	   [{'path': 'EcalEndcap/EEOccupancyTask/EEOT number of digis in event', 'description': 'Distribution of the number of digis per event.'},
	    {'path': 'EcalEndcap/EEOccupancyTask/EEOT number of filtered rec hits in event', 'description': 'Occupancy of rec hits with GOOD reconstruction flag and E > 0.5 GeV.'}])
ecallayout(dqmitems, 'Ecal/Layouts/02 Occupancy/17 Multiplicity Trend',
	   [{'path': 'Ecal/Trends/OccupancyTask EB number of digis', 'description': 'Trend of the per-event number of digis.'},
	    {'path': 'Ecal/Trends/OccupancyTask EB number of filtered recHits', 'description': 'Trend of the per-event number of rec hits with GOOD reconstruction flag and E > 0.5 GeV.'},
	    {'path': 'Ecal/Trends/OccupancyTask EB number of filtered TP digis', 'description': 'Trend of the per-event number of TP digis with Et > 4.0 GeV.'}],
	   [{'path': 'Ecal/Trends/OccupancyTask EE number of digis', 'description': 'Trend of the per-event number of digis.'},
	    {'path': 'Ecal/Trends/OccupancyTask EE number of filtered recHits', 'description': 'Trend of the per-event number of rec hits with GOOD reconstruction flag and E > 0.5 GeV.'},
	    {'path': 'Ecal/Trends/OccupancyTask EE number of filtered TP digis', 'description': 'Trend of the per-event number of TP digis with Et > 4.0 GeV.'}])
ecallayout(dqmitems, 'Ecal/Layouts/02 Occupancy/18 FED Total',
	   [{'path': 'EcalBarrel/EBOccupancyTask/EBOT digi occupancy by DCC', 'description': 'DCC digi occupancy.'}],
	   [{'path': 'EcalEndcap/EEOccupancyTask/EEOT digi occupancy by DCC', 'description': 'DCC digi occupancy.'}])
ecallayout(dqmitems, 'Ecal/Layouts/02 Occupancy/19 Basic Cluster Multiplicity',
	   [{'path': 'EcalBarrel/EBClusterTask/EBCLT BC number', 'description': 'Distribution of the number of basic clusters per event.'}],
	   [{'path': 'EcalEndcap/EEClusterTask/EECLT BC number', 'description': 'Distribution of the number of basic clusters per event.'}])
ecallayout(dqmitems, 'Ecal/Layouts/02 Occupancy/20 Super Cluster Seed',
	   [{'path': 'EcalBarrel/EBClusterTask/EBCLT SC seed occupancy map', 'description': 'Occupancy map of the crystals that seeded super clusters.'}],
	   [{'path': 'EcalEndcap/EEClusterTask/EECLT SC seed occupancy map EE -', 'description': 'Occupancy map of the crystals that seeded super clusters.'},
	    {'path': 'EcalEndcap/EEClusterTask/EECLT SC seed occupancy map EE +', 'description': 'Occupancy map of the crystals that seeded super clusters.'}])
ecallayout(dqmitems, 'Ecal/Layouts/02 Occupancy/21 Super Cluster Multiplicity',
	   [{'path': 'EcalBarrel/EBClusterTask/EBCLT SC number', 'description': 'Distribution of the number of super clusters per event in EB/EE.'}],
	   [{'path': 'EcalEndcap/EEClusterTask/EECLT SC number', 'description': 'Distribution of the number of super clusters per event in EB/EE.'}])
ecallayout(dqmitems, 'Ecal/Layouts/02 Occupancy/22 Single Crystal Cluster',
	   [{'path': 'EcalBarrel/EBClusterTask/EBCLT SC single crystal cluster seed occupancy map', 'description': 'Occupancy map of the occurrence of super clusters with only one constituent'}],
	   [{'path': 'EcalEndcap/EEClusterTask/EECLT SC single crystal cluster seed occupancy map EE -', 'description': 'Occupancy map of the occurrence of super clusters with only one constituent'},
	    {'path': 'EcalEndcap/EEClusterTask/EECLT SC single crystal cluster seed occupancy map EE +', 'description': 'Occupancy map of the occurrence of super clusters with only one constituent'}])
ecallayout(dqmitems, 'Ecal/Layouts/02 Occupancy/23 Cluster Multiplicity Trends',
	   [{'path': 'Ecal/Trends/ClusterTask EB number of basic clusters', 'description': 'Trend of the number of basic clusters per event in EB/EE.'},
	    {'path': 'Ecal/Trends/ClusterTask EB number of super clusters', 'description': 'Trend of the number of super clusters per event in EB/EE.'}],
	   [{'path': 'Ecal/Trends/ClusterTask EE number of basic clusters', 'description': 'Trend of the number of basic clusters per event in EB/EE.'},
	    {'path': 'Ecal/Trends/ClusterTask EE number of super clusters', 'description': 'Trend of the number of super clusters per event in EB/EE.'}])
ecallayout(dqmitems, 'Ecal/Layouts/02 Occupancy/24 Laser',
	   [{'path': 'EcalBarrel/EBOccupancyTask/EBOT laser digi occupancy', 'description': 'Laser signal digi occupancy. Channels are filled regardless of the existance of the actual laser pulses.'}],
	   [{'path': 'EcalEndcap/EEOccupancyTask/EEOT laser digi occupancy EE -', 'description': 'Laser signal digi occupancy. Channels are filled regardless of the existance of the actual laser pulses.'},
	    {'path': 'EcalEndcap/EEOccupancyTask/EEOT laser digi occupancy EE +', 'description': 'Laser signal digi occupancy. Channels are filled regardless of the existance of the actual laser pulses.'}])
ecallayout(dqmitems, 'Ecal/Layouts/02 Occupancy/25 Led',
	   [{'path': 'EcalEndcap/EEOccupancyTask/EEOT led digi occupancy EE -', 'description': 'Led signal digi occupancy. Channels are filled regardless of the existance of the actual led pulses.'},
	    {'path': 'EcalEndcap/EEOccupancyTask/EEOT led digi occupancy EE +', 'description': 'Led signal digi occupancy. Channels are filled regardless of the existance of the actual led pulses.'}])
ecallayout(dqmitems, 'Ecal/Layouts/02 Occupancy/26 Test Pulse',
	   [{'path': 'EcalBarrel/EBOccupancyTask/EBOT test pulse digi occupancy', 'description': 'Occupancy in test pulse events.'}],
	   [{'path': 'EcalEndcap/EEOccupancyTask/EEOT test pulse digi occupancy EE -', 'description': 'Occupancy in test pulse events.'},
	    {'path': 'EcalEndcap/EEOccupancyTask/EEOT test pulse digi occupancy EE +', 'description': 'Occupancy in test pulse events.'}])
ecallayout(dqmitems, 'Ecal/Layouts/02 Occupancy/27 PN Digi',
	   [{'path': 'EcalBarrel/EBSummaryClient/EBOT PN digi occupancy summary', 'description': 'Occupancy of PN digis in calibration events.'}],
	   [{'path': 'EcalEndcap/EESummaryClient/EEOT PN digi occupancy summary', 'description': 'Occupancy of PN digis in calibration events.'}])
ecallayout(dqmitems, 'Ecal/Layouts/02 Occupancy/SR and TT Flags/00 Zero Suppression',
	   [{'path': 'EcalBarrel/EBSelectiveReadoutTask/Counters/EBSRT tower ZS1 counter', 'description': 'Tower occupancy with ZS1 flags.'}],
	   [{'path': 'EcalBarrel/EBSelectiveReadoutTask/Counters/EBSRT tower ZS1+ZS2 counter', 'description': 'Tower occupancy of ZS1 and ZS2 flags.'}],
	   [{'path': 'EcalEndcap/EESelectiveReadoutTask/Counters/EESRT tower ZS1 counter EE -', 'description': 'Tower occupancy with ZS1 flags.'},
	    {'path': 'EcalEndcap/EESelectiveReadoutTask/Counters/EESRT tower ZS1 counter EE +', 'description': 'Tower occupancy with ZS1 flags.'}],
	   [{'path': 'EcalEndcap/EESelectiveReadoutTask/Counters/EESRT tower ZS1+ZS2 counter EE -', 'description': 'Tower occupancy of ZS1 and ZS2 flags.'},
	    {'path': 'EcalEndcap/EESelectiveReadoutTask/Counters/EESRT tower ZS1+ZS2 counter EE +', 'description': 'Tower occupancy of ZS1 and ZS2 flags.'}])
ecallayout(dqmitems, 'Ecal/Layouts/02 Occupancy/SR and TT Flags/01 Full Readout',
	   [{'path': 'EcalBarrel/EBSelectiveReadoutTask/Counters/EBSRT tower full readout counter', 'description': 'Tower occupancy with FR flags.'}],
	   [{'path': 'EcalEndcap/EESelectiveReadoutTask/Counters/EESRT tower full readout counter EE -', 'description': 'Tower occupancy with FR flags.'},
	    {'path': 'EcalEndcap/EESelectiveReadoutTask/Counters/EESRT tower full readout counter EE +', 'description': 'Tower occupancy with FR flags.'}])
ecallayout(dqmitems, 'Ecal/Layouts/02 Occupancy/SR and TT Flags/02 Forced Readout',
	   [{'path': 'EcalBarrel/EBSelectiveReadoutTask/Counters/EBSRT RU with forced SR counter', 'description': 'Tower occupancy of FORCED flag.'}],
	   [{'path': 'EcalEndcap/EESelectiveReadoutTask/Counters/EESRT RU with forced SR counter EE -', 'description': 'Tower occupancy of FORCED flag.'},
	    {'path': 'EcalEndcap/EESelectiveReadoutTask/Counters/EESRT RU with forced SR counter EE +', 'description': 'Tower occupancy of FORCED flag.'}])
ecallayout(dqmitems, 'Ecal/Layouts/02 Occupancy/SR and TT Flags/03 All SR Flags',
	   [{'path': 'EcalBarrel/EBSelectiveReadoutTask/Counters/EBSRT tower flag counter', 'description': 'Tower occupancy of any SR flag.'}],
	   [{'path': 'EcalEndcap/EESelectiveReadoutTask/Counters/EESRT tower flag counter EE -', 'description': 'Tower occupancy of any SR flag.'},
	    {'path': 'EcalEndcap/EESelectiveReadoutTask/Counters/EESRT tower flag counter EE +', 'description': 'Tower occupancy of any SR flag.'}])
ecallayout(dqmitems, 'Ecal/Layouts/02 Occupancy/SR and TT Flags/04 TT High Interest',
	   [{'path': 'EcalBarrel/EBSelectiveReadoutTask/Counters/EBSRT tower high interest counter', 'description': 'Tower occupancy of high interest flags.'}],
	   [{'path': 'EcalEndcap/EESelectiveReadoutTask/Counters/EESRT tower high interest counter EE -', 'description': 'Tower occupancy of high interest flags.'},
	    {'path': 'EcalEndcap/EESelectiveReadoutTask/Counters/EESRT tower high interest counter EE +', 'description': 'Tower occupancy of high interest flags.'}])
ecallayout(dqmitems, 'Ecal/Layouts/02 Occupancy/SR and TT Flags/05 TT Medium Interest',
	   [{'path': 'EcalBarrel/EBSelectiveReadoutTask/Counters/EBSRT tower med interest counter', 'description': 'Tower occupancy of medium interest flags.'}],
	   [{'path': 'EcalEndcap/EESelectiveReadoutTask/Counters/EESRT tower med interest counter EE -', 'description': 'Tower occupancy of medium interest flags.'},
	    {'path': 'EcalEndcap/EESelectiveReadoutTask/Counters/EESRT tower med interest counter EE +', 'description': 'Tower occupancy of medium interest flags.'}])
ecallayout(dqmitems, 'Ecal/Layouts/02 Occupancy/SR and TT Flags/06 TT Low Interest',
	   [{'path': 'EcalBarrel/EBSelectiveReadoutTask/Counters/EBSRT tower low interest counter', 'description': 'Tower occupancy of low interest flags.'}],
	   [{'path': 'EcalEndcap/EESelectiveReadoutTask/Counters/EESRT tower low interest counter EE -', 'description': 'Tower occupancy of low interest flags.'},
	    {'path': 'EcalEndcap/EESelectiveReadoutTask/Counters/EESRT tower low interest counter EE +', 'description': 'Tower occupancy of low interest flags.'}])
# By SuperModule _______________
for (detector, label, maxchannel) in [('Endcap', 'EE', 9), ('Barrel', 'EB', 18)]: # Loop over EB,EE
  for sign in ['-', '+']:  # Loop over z-side
    for channel in range(1, maxchannel+1): # Loop over channels
      channellabel = '%s%s%02d' % (label, sign, channel) # e.g. "EE+05"
      ecallayout(dqmitems,'Ecal/Layouts/02 Occupancy/By SuperModule/Digi/Digi Occupancy %s' % channellabel,
                 [{'path': 'Ecal%s/%sOccupancyTask/%sOT digi occupancy %s' % (detector, label, label, channellabel),
                   'description': 'Digi occupancy.'}])
      # Exclude EE[+-]01,04,05,06,09
      if detector == 'Endcap':
        if channel == 1 or channel == 4 or channel == 5 or channel == 6 or channel == 9:
	        continue
      ecallayout(dqmitems,'Ecal/Layouts/02 Occupancy/By SuperModule/PN Digi/PN Digi Occupancy %s' % channellabel,
                 [{'path': 'Ecal%s/%sOccupancyTask/%sOT MEM digi occupancy %s' % (detector, label, label, channellabel),
                   'description': 'Digi occupancy.'}])

#____________________ Layouts / 03 Noise ____________________
ecallayout(dqmitems, 'Ecal/Layouts/03 Noise/00 Presample Quality',
	   [{'path': 'EcalBarrel/EBSummaryClient/EBPOT pedestal quality summary G12', 'description': 'Summary of the presample data quality. A channel is red if presample mean is off by 25.0 from 200.0 or RMS is greater than 3.0. RMS threshold is 6.0 in the forward region (|eta| > 2.1). Channels with entries less than 6 are not considered.'}],
	   [{'path': 'EcalEndcap/EESummaryClient/EEPOT EE - pedestal quality summary G12', 'description': 'Summary of the presample data quality. A channel is red if presample mean is off by 25.0 from 200.0 or RMS is greater than 3.0. RMS threshold is 6.0 in the forward region (|eta| > 2.1). Channels with entries less than 6 are not considered.'},
	    {'path': 'EcalEndcap/EESummaryClient/EEPOT EE + pedestal quality summary G12', 'description': 'Summary of the presample data quality. A channel is red if presample mean is off by 25.0 from 200.0 or RMS is greater than 3.0. RMS threshold is 6.0 in the forward region (|eta| > 2.1). Channels with entries less than 6 are not considered.'}])
ecallayout(dqmitems, 'Ecal/Layouts/03 Noise/01 RMS Map',
	   [{'path': 'EcalBarrel/EBSummaryClient/EBPOT pedestal G12 RMS map', 'description': '2D distribution of the presample RMS. Channels with entries less than 6 are not considered.'}],
	   [{'path': 'EcalEndcap/EESummaryClient/EEPOT EE - pedestal G12 RMS map', 'description': '2D distribution of the presample RMS. Channels with entries less than 6 are not considered.'},
	    {'path': 'EcalEndcap/EESummaryClient/EEPOT EE + pedestal G12 RMS map', 'description': '2D distribution of the presample RMS. Channels with entries less than 6 are not considered.'}])
ecallayout(dqmitems, 'Ecal/Layouts/03 Noise/02 Reconstructed',
	   [{'path': 'EcalBarrel/EBOccupancyTask/EBOT rec hit occupancy', 'description': 'Rec hit occupancy.'}],
	   [{'path': 'EcalBarrel/EBClusterTask/EBCLT SC single crystal cluster seed occupancy map', 'description': 'Occupancy map of the occurrence of super clusters with only one constituent'}],
	   [{'path': 'EcalEndcap/EEOccupancyTask/EEOT rec hit occupancy EE -', 'description': 'Rec hit occupancy.'},
	    {'path': 'EcalEndcap/EEOccupancyTask/EEOT rec hit occupancy EE +', 'description': 'Rec hit occupancy.'}],
	   [{'path': 'EcalEndcap/EEClusterTask/EECLT SC single crystal cluster seed occupancy map EE -', 'description': 'Occupancy map of the occurrence of super clusters with only one constituent'},
	    {'path': 'EcalEndcap/EEClusterTask/EECLT SC single crystal cluster seed occupancy map EE +', 'description': 'Occupancy map of the occurrence of super clusters with only one constituent'}])
ecallayout(dqmitems, 'Ecal/Layouts/03 Noise/03 Trend',
	   [{'path': 'Ecal/Trends/PresampleClient EB pedestal mean max - min', 'description': 'Trend of presample spread in EB / EE. Y value indicates the difference between maximum and minimum presample mean values within the subdetector.'},
	    {'path': 'Ecal/Trends/PresampleClient EB pedestal rms max', 'description': 'Trend of presample RMS averaged over all channels in EB / EE.'}],
	   [{'path': 'Ecal/Trends/PresampleClient EE pedestal mean max - min', 'description': 'Trend of presample spread in EB / EE. Y value indicates the difference between maximum and minimum presample mean values within the subdetector.'},
	    {'path': 'Ecal/Trends/PresampleClient EE pedestal rms max', 'description': 'Trend of presample RMS averaged over all channels in EB / EE.'}])
ecallayout(dqmitems, 'Ecal/Layouts/03 Noise/04 EB Rechit Occupancy Near vs Far',
           [{'path': 'EcalBarrel/EBOccupancyTask/EBOT rec hit thr occupancy correlation', 'description': 'Filtered rechit occupancy correlation: near vs far barrel.'}])
ecallayout(dqmitems, 'Ecal/Layouts/03 Noise/04 EE Rechit Occupancy z- vs z+',
           [{'path': 'EcalEndcap/EEOccupancyTask/EEOT rec hit thr occupancy correlation', 'description': 'Filtered rechit occupancy correlation: z- vs z+.'}])
ecallayout(dqmitems, 'Ecal/Layouts/03 Noise/05 Rechit Occupancy difference',
           [{'path': 'EcalBarrel/EBOccupancyTask/EBOT rec hit thr occupancy z+(far) - z-(near)', 'description': 'Filtered rechit occupancy difference: far - near.'}],
           [{'path': 'EcalEndcap/EEOccupancyTask/EEOT rec hit thr occupancy z+(far) - z-(near)', 'description': 'Filtered rechit occupancy difference: z+ - z-.'}])
# By SuperModule _______________
for (detector, label, maxchannel) in [('Endcap', 'EE', 9), ('Barrel', 'EB', 18)]: # Loop over EB,EE
  for sign in ['-', '+']: # Loop over z-side
    for channel in range(1, maxchannel+1): # Loop over channels
      channellabel = '%s%s%02d' % (label, sign, channel) # e.g. "EE+05"
      ecallayout(dqmitems,'Ecal/Layouts/03 Noise/By SuperModule/Quality/Quality %s' % channellabel,
                 [{'path': 'Ecal%s/%sPedestalOnlineClient/%sPOT pedestal quality G12 %s' % (detector, label, label, channellabel),
                   'description': 'Summary of the presample data quality. A channel is red if presample mean is off by 25.0 from 200.0 or RMS is greater than 3.0. RMS threshold is 6.0 in the forward region (|eta| > 2.1). Channels with entries less than 6 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/03 Noise/By SuperModule/Mean/Mean %s' % channellabel,
                 [{'path': 'Ecal%s/%sPedestalOnlineTask/Gain12/%sPOT pedestal %s G12' % (detector, label, label, channellabel),
                   'description': '2D distribution of mean presample value.'}],
                 [{'path': 'Ecal%s/%sPedestalOnlineClient/%sPOT pedestal mean G12 %s' % (detector, label, label, channellabel),
                   'description': '1D distribution of the mean presample value in each crystal. Channels with entries less than 6 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/03 Noise/By SuperModule/RMS/RMS %s' % channellabel,
                 [{'path': 'Ecal%s/%sPedestalOnlineClient/%sPOT pedestal rms map G12 %s' % (detector, label, label, channellabel),
                   'description': '2D distribution of mean presample value.'}],
                 [{'path': 'Ecal%s/%sPedestalOnlineClient/%sPOT pedestal rms G12 %s' % (detector, label, label, channellabel),
                   'description': 'Distribution of the presample RMS of each channel. Channels with entries less than 6 are not considered.'}])
      # Exclude EE[+-]01,04,05,06,09
      if detector == 'Endcap':
        if channel == 1 or channel == 4 or channel == 5 or channel == 6 or channel == 9:
	        continue
      ecallayout(dqmitems,'Ecal/Layouts/03 Noise/By SuperModule/PN/PN Presample %s' % channellabel,
                 [{'path': 'Ecal%s/%sPedestalOnlineTask/PN/%sPOT PN pedestal %s G16' % (detector, label, label, channellabel),
                   'description': 'Presample mean of PN signals.'}])

#____________________ Layouts / 04 Energy ____________________
ecallayout(dqmitems, 'Ecal/Layouts/04 Energy/00 RecHit Energy',
	   [{'path': 'EcalBarrel/EBSummaryClient/EBOT energy summary', 'description': '2D distribution of the mean rec hit energy.'}],
	   [{'path': 'EcalEndcap/EESummaryClient/EEOT EE - energy summary', 'description': '2D distribution of the mean rec hit energy.'},
	    {'path': 'EcalEndcap/EESummaryClient/EEOT EE + energy summary', 'description': '2D distribution of the mean rec hit energy.'}])
ecallayout(dqmitems, 'Ecal/Layouts/04 Energy/01 RecHit Energy Spectrum',
	   [{'path': 'EcalBarrel/EBOccupancyTask/EBOT rec hit spectrum', 'description': 'Rec hit energy distribution.'}],
	   [{'path': 'EcalEndcap/EEOccupancyTask/EEOT rec hit spectrum EE -', 'description': 'Rec hit energy distribution.'},
	    {'path': 'EcalEndcap/EEOccupancyTask/EEOT rec hit spectrum EE +', 'description': 'Rec hit energy distribution.'}])
ecallayout(dqmitems, 'Ecal/Layouts/04 Energy/02 Basic Cluster Energy EB',
	   [{'path': 'EcalBarrel/EBClusterTask/EBCLT BC energy map', 'description': '2D distribution of the mean energy of the basic clusters.'}],
	   [{'path': 'EcalBarrel/EBClusterTask/EBCLT BC energy projection eta', 'description': 'Projection of the mean energy of the basic clusters.'},
	    {'path': 'EcalBarrel/EBClusterTask/EBCLT BC energy projection phi', 'description': 'Projection of the mean energy of the basic clusters.'}])
ecallayout(dqmitems, 'Ecal/Layouts/04 Energy/03 Basic Cluster Energy EE -',
	   [{'path': 'EcalEndcap/EEClusterTask/EECLT BC energy map EE -', 'description': '2D distribution of the mean energy of the basic clusters.'}],
	   [{'path': 'EcalEndcap/EEClusterTask/EECLT BC energy projection eta EE -', 'description': 'Projection of the mean energy of the basic clusters.'},
	    {'path': 'EcalEndcap/EEClusterTask/EECLT BC energy projection phi EE -', 'description': 'Projection of the mean energy of the basic clusters.'}])
ecallayout(dqmitems, 'Ecal/Layouts/04 Energy/04 Basic Cluster Energy EE +',
	   [{'path': 'EcalEndcap/EEClusterTask/EECLT BC energy map EE +', 'description': '2D distribution of the mean energy of the basic clusters.'}],
	   [{'path': 'EcalEndcap/EEClusterTask/EECLT BC energy projection eta EE +', 'description': 'Projection of the mean energy of the basic clusters.'},
	    {'path': 'EcalEndcap/EEClusterTask/EECLT BC energy projection phi EE +', 'description': 'Projection of the mean energy of the basic clusters.'}])
ecallayout(dqmitems, 'Ecal/Layouts/04 Energy/05 Basic Cluster Size EB',
	   [{'path': 'EcalBarrel/EBClusterTask/EBCLT BC size map', 'description': '2D distribution of the mean size (number of crystals) of the basic clusters.'}],
	   [{'path': 'EcalBarrel/EBClusterTask/EBCLT BC size projection eta', 'description': 'Projection of the mean size (number of crystals) of the basic clusters.'},
	    {'path': 'EcalBarrel/EBClusterTask/EBCLT BC size projection phi', 'description': 'Projection of the mean size (number of crystals) of the basic clusters.'}])
ecallayout(dqmitems, 'Ecal/Layouts/04 Energy/06 Basic Cluster Size EE -',
	   [{'path': 'EcalEndcap/EEClusterTask/EECLT BC size map EE -', 'description': '2D distribution of the mean size (number of crystals) of the basic clusters.'}],
	   [{'path': 'EcalEndcap/EEClusterTask/EECLT BC size projection eta EE -', 'description': 'Projection of the mean size (number of crystals) of the basic clusters.'},
	    {'path': 'EcalEndcap/EEClusterTask/EECLT BC size projection phi EE -', 'description': 'Projection of the mean size (number of crystals) of the basic clusters.'}])
ecallayout(dqmitems, 'Ecal/Layouts/04 Energy/07 Basic Cluster Size EE +',
	   [{'path': 'EcalEndcap/EEClusterTask/EECLT BC size map EE +', 'description': '2D distribution of the mean size (number of crystals) of the basic clusters.'}],
	   [{'path': 'EcalEndcap/EEClusterTask/EECLT BC size projection eta EE +', 'description': 'Projection of the mean size (number of crystals) of the basic clusters.'},
	    {'path': 'EcalEndcap/EEClusterTask/EECLT BC size projection phi EE +', 'description': 'Projection of the mean size (number of crystals) of the basic clusters.'}])
ecallayout(dqmitems, 'Ecal/Layouts/04 Energy/08 Basic Cluster Energy',
	   [{'path': 'EcalBarrel/EBClusterTask/EBCLT BC energy', 'description': 'Basic cluster energy distribution.'}],
	   [{'path': 'EcalEndcap/EEClusterTask/EECLT BC energy', 'description': 'Basic cluster energy distribution.'}])
ecallayout(dqmitems, 'Ecal/Layouts/04 Energy/09 Basic Cluster Size',
	   [{'path': 'EcalBarrel/EBClusterTask/EBCLT BC size', 'description': 'Distribution of the basic cluster size (number of crystals).'}],
	   [{'path': 'EcalEndcap/EEClusterTask/EECLT BC size', 'description': 'Distribution of the basic cluster size (number of crystals).'}])
ecallayout(dqmitems, 'Ecal/Layouts/04 Energy/10 Basic Cluster Size Trend',
	   [{'path': 'Ecal/Trends/ClusterTask EB size of basic clusters', 'description': 'Trend of the mean size of the basic clusters.'}],
	   [{'path': 'Ecal/Trends/ClusterTask EE size of basic clusters', 'description': 'Trend of the mean size of the basic clusters.'}])
ecallayout(dqmitems, 'Ecal/Layouts/04 Energy/11 Super Cluster Energy',
	   [{'path': 'EcalBarrel/EBClusterTask/EBCLT SC energy', 'description': 'Super cluster energy distribution.'}],
	   [{'path': 'EcalEndcap/EEClusterTask/EECLT SC energy', 'description': 'Super cluster energy distribution.'}])
ecallayout(dqmitems, 'Ecal/Layouts/04 Energy/12 Super Cluster Energy Low',
	   [{'path': 'EcalBarrel/EBClusterTask/EBCLT SC energy (low scale)', 'description': 'Energy distribution of the super clusters (low scale).'}],
	   [{'path': 'EcalEndcap/EEClusterTask/EECLT SC energy (low scale)', 'description': 'Energy distribution of the super clusters (low scale).'}])
ecallayout(dqmitems, 'Ecal/Layouts/04 Energy/13 Super Cluster Seed Energy',
	   [{'path': 'EcalBarrel/EBClusterTask/EBCLT SC seed crystal energy', 'description': 'Energy distribution of the crystals that seeded super clusters.'}],
	   [{'path': 'EcalEndcap/EEClusterTask/EECLT SC seed crystal energy', 'description': 'Energy distribution of the crystals that seeded super clusters.'}])
ecallayout(dqmitems, 'Ecal/Layouts/04 Energy/14 Super Cluster R9',
	   [{'path': 'EcalBarrel/EBClusterTask/EBCLT SC R9', 'description': 'Distribution of E_seed / E_3x3 of the super clusters.'}],
	   [{'path': 'EcalEndcap/EEClusterTask/EECLT SC R9', 'description': 'Distribution of E_seed / E_3x3 of the super clusters.'}])
ecallayout(dqmitems, 'Ecal/Layouts/04 Energy/15 Super Cluster Size',
	   [{'path': 'EcalBarrel/EBClusterTask/EBCLT SC size', 'description': 'Distribution of the super cluster size (number of basic clusters)'},
	    {'path': 'EcalBarrel/EBClusterTask/EBCLT SC size (crystal)', 'description': 'Distribution of the super cluster size (number of crystals).'}],
	   [{'path': 'EcalEndcap/EEClusterTask/EECLT SC size', 'description': 'Distribution of the super cluster size (number of basic clusters)'},
	    {'path': 'EcalEndcap/EEClusterTask/EECLT SC size (crystal)', 'description': 'Distribution of the super cluster size (number of crystals).'}])
ecallayout(dqmitems, 'Ecal/Layouts/04 Energy/16 Cluster Energy vs Seed Energy',
	   [{'path': 'EcalBarrel/EBClusterTask/EBCLT SC energy vs seed crystal energy', 'description': 'Relation between super cluster energy and its seed crystal energy.'}],
	   [{'path': 'EcalEndcap/EEClusterTask/EECLT SC energy vs seed crystal energy', 'description': 'Relation between super cluster energy and its seed crystal energy.'}])
# By SuperModule _______________
for (detector, label, maxchannel) in [('Endcap', 'EE', 9), ('Barrel', 'EB', 18)]: # Loop over EB,EE
  for sign in ['-', '+']: # Loop over z-side
    for channel in range(1, maxchannel+1): # Loop over channels
      channellabel = '%s%s%02d' % (label, sign, channel) # e.g. "EE+05"
      ecallayout(dqmitems,'Ecal/Layouts/04 Energy/By SuperModule/RecHit %s' % channellabel,
                 [{'path': 'Ecal%s/%sOccupancyTask/%sOT rec hit energy %s' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean rec hit energy.'}],
                 [{'path': 'Ecal%s/%sOccupancyTask/%sOT energy spectrum %s' % (detector, label, label, channellabel),
                   'description': 'Rec hit energy distribution.'}])

#____________________ Layouts / 05 Timing ____________________
ecallayout(dqmitems, 'Ecal/Layouts/05 Timing/00 Quality Summary',
	   [{'path': 'EcalBarrel/EBSummaryClient/EBTMT timing quality summary', 'description': 'Summary of the timing data quality. A 5x5 tower is red if the mean timing of the tower is off by more than 2.0 or RMS is greater than 6.0 (6.0 and 12.0 in forward region). Towers with total entries less than 15 are not subject to this evaluation. Since 5x5 tower timings are calculated with a tighter time-window than per-channel timings, a tower can additionally become red if its the sum of per-channel timing histogram entries is greater than per-tower histogram entries by factor 1.66666666667 (significant fraction of events fall outside the tight time-window).'}],
	   [{'path': 'EcalEndcap/EESummaryClient/EETMT EE - timing quality summary', 'description': 'Summary of the timing data quality. A 5x5 tower is red if the mean timing of the tower is off by more than 2.0 or RMS is greater than 6.0 (6.0 and 12.0 in forward region). Towers with total entries less than 15 are not subject to this evaluation. Since 5x5 tower timings are calculated with a tighter time-window than per-channel timings, a tower can additionally become red if its the sum of per-channel timing histogram entries is greater than per-tower histogram entries by factor 1.66666666667 (significant fraction of events fall outside the tight time-window).'},
	    {'path': 'EcalEndcap/EESummaryClient/EETMT EE + timing quality summary', 'description': 'Summary of the timing data quality. A 5x5 tower is red if the mean timing of the tower is off by more than 2.0 or RMS is greater than 6.0 (6.0 and 12.0 in forward region). Towers with total entries less than 15 are not subject to this evaluation. Since 5x5 tower timings are calculated with a tighter time-window than per-channel timings, a tower can additionally become red if its the sum of per-channel timing histogram entries is greater than per-tower histogram entries by factor 1.66666666667 (significant fraction of events fall outside the tight time-window).'}])
ecallayout(dqmitems, 'Ecal/Layouts/05 Timing/01 Mean',
	   [{'path': 'EcalBarrel/EBSummaryClient/EBTMT timing mean 1D summary', 'description': 'Distribution of per-channel timing mean. Channels with entries less than 5 are not considered.'}],
	   [{'path': 'EcalEndcap/EESummaryClient/EETMT EE - timing mean 1D summary', 'description': 'Distribution of per-channel timing mean. Channels with entries less than 5 are not considered.'},
	    {'path': 'EcalEndcap/EESummaryClient/EETMT EE + timing mean 1D summary', 'description': 'Distribution of per-channel timing mean. Channels with entries less than 5 are not considered.'}])
ecallayout(dqmitems, 'Ecal/Layouts/05 Timing/02 RMS',
	   [{'path': 'EcalBarrel/EBSummaryClient/EBTMT timing rms 1D summary', 'description': 'Distribution of per-channel timing RMS. Channels with entries less than 5 are not considered.'}],
	   [{'path': 'EcalEndcap/EESummaryClient/EETMT EE - timing rms 1D summary', 'description': 'Distribution of per-channel timing RMS. Channels with entries less than 5 are not considered.'},
	    {'path': 'EcalEndcap/EESummaryClient/EETMT EE + timing rms 1D summary', 'description': 'Distribution of per-channel timing RMS. Channels with entries less than 5 are not considered.'}])
ecallayout(dqmitems, 'Ecal/Layouts/05 Timing/03 Map EB',
	   [{'path': 'EcalBarrel/EBTimingTask/EBTMT timing map', 'description': '2D distribution of the mean rec hit timing. Only hits with GOOD or OUT_OF_TIME reconstruction flags and energy above threshold are used. Hits with |t| > 7.0 ns are discarded. The energy thresholds are 1.000000 and 3.000000 for EB and EE respectively.'}],
	   [{'path': 'EcalBarrel/EBTimingClient/EBTMT timing projection eta', 'description': 'Projection of per-channel mean timing. Channels with entries less than 5 are not considered.'},
	    {'path': 'EcalBarrel/EBTimingClient/EBTMT timing projection phi', 'description': 'Projection of per-channel mean timing. Channels with entries less than 5 are not considered.'}])
ecallayout(dqmitems, 'Ecal/Layouts/05 Timing/04 Map EE -',
	   [{'path': 'EcalEndcap/EETimingTask/EETMT timing map EE -', 'description': '2D distribution of the mean rec hit timing. Only hits with GOOD or OUT_OF_TIME reconstruction flags and energy above threshold are used. Hits with |t| > 7.0 ns are discarded. The energy thresholds are 1.000000 and 3.000000 for EB and EE respectively.'}],
	   [{'path': 'EcalEndcap/EETimingClient/EETMT timing projection eta EE -', 'description': 'Projection of per-channel mean timing. Channels with entries less than 5 are not considered.'},
	    {'path': 'EcalEndcap/EETimingClient/EETMT timing projection phi EE -', 'description': 'Projection of per-channel mean timing. Channels with entries less than 5 are not considered.'}])
ecallayout(dqmitems, 'Ecal/Layouts/05 Timing/05 Map EE +',
	   [{'path': 'EcalEndcap/EETimingTask/EETMT timing map EE +', 'description': '2D distribution of the mean rec hit timing. Only hits with GOOD or OUT_OF_TIME reconstruction flags and energy above threshold are used. Hits with |t| > 7.0 ns are discarded. The energy thresholds are 1.000000 and 3.000000 for EB and EE respectively.'}],
	   [{'path': 'EcalEndcap/EETimingClient/EETMT timing projection eta EE +', 'description': 'Projection of per-channel mean timing. Channels with entries less than 5 are not considered.'},
	    {'path': 'EcalEndcap/EETimingClient/EETMT timing projection phi EE +', 'description': 'Projection of per-channel mean timing. Channels with entries less than 5 are not considered.'}])
ecallayout(dqmitems, 'Ecal/Layouts/05 Timing/06 Forward-Backward',
	   [{'path': 'EcalBarrel/EBTimingTask/EBTMT timing EB+ - EB-', 'description': 'Forward-backward asymmetry of per-channel mean timing. Channels with entries less than 5 are not considered.'},
	    {'path': 'EcalBarrel/EBTimingTask/EBTMT timing EB+ vs EB-', 'description': 'Forward-backward correlation of per-channel mean timing. Channels with entries less than 5 are not considered.'}],
	   [{'path': 'EcalEndcap/EETimingTask/EETMT timing EE+ - EE-', 'description': 'Forward-backward asymmetry of per-channel mean timing. Channels with entries less than 5 are not considered.'},
	    {'path': 'EcalEndcap/EETimingTask/EETMT timing EE+ vs EE-', 'description': 'Forward-backward correlation of per-channel mean timing. Channels with entries less than 5 are not considered.'}])
ecallayout(dqmitems, 'Ecal/Layouts/05 Timing/07 Distribution',
	   [{'path': 'EcalBarrel/EBTimingTask/EBTMT timing 1D summary', 'description': 'Distribution of the mean rec hit timing. Only hits with GOOD or OUT_OF_TIME reconstruction flags and energy above threshold are used. The energy thresholds are 1.000000 and 3.000000 for EB and EE respectively.'}],
	   [{'path': 'EcalEndcap/EETimingTask/EETMT timing 1D summary EE -', 'description': 'Distribution of the mean rec hit timing. Only hits with GOOD or OUT_OF_TIME reconstruction flags and energy above threshold are used. The energy thresholds are 1.000000 and 3.000000 for EB and EE respectively.'},
	    {'path': 'EcalEndcap/EETimingTask/EETMT timing 1D summary EE +', 'description': 'Distribution of the mean rec hit timing. Only hits with GOOD or OUT_OF_TIME reconstruction flags and energy above threshold are used. The energy thresholds are 1.000000 and 3.000000 for EB and EE respectively.'}])
ecallayout(dqmitems, 'Ecal/Layouts/05 Timing/08 Vs Amptlitude',
	   [{'path': 'EcalBarrel/EBTimingTask/EBTMT timing vs amplitude summary', 'description': 'Correlation between hit timing and energy. Only hits with GOOD or OUT_OF_TIME reconstruction flags are used.'}],
	   [{'path': 'EcalEndcap/EETimingTask/EETMT timing vs amplitude summary EE -', 'description': 'Correlation between hit timing and energy. Only hits with GOOD or OUT_OF_TIME reconstruction flags are used.'},
	    {'path': 'EcalEndcap/EETimingTask/EETMT timing vs amplitude summary EE +', 'description': 'Correlation between hit timing and energy. Only hits with GOOD or OUT_OF_TIME reconstruction flags are used.'}])
ecallayout(dqmitems, 'Ecal/Layouts/05 Timing/09 Amplitude Correlation, BX-1',
	   [{'path': 'EcalBarrel/EBTimingTask/EBTMT in-time vs BX-1 amplitude', 'description': 'Correlation between in-time amplitude and BX-1 out-of-time amplitude. Only events with kGood reconstruction flag set, energy above ( EB:1, EE:3 ) GeV, and chi2 less than ( EB:16, EE:50 ) are used.'}],
	   [{'path': 'EcalEndcap/EETimingTask/EETMT in-time vs BX-1 amplitude EE -', 'description': 'Correlation between in-time amplitude and BX-1 out-of-time amplitude. Only events with kGood reconstruction flag set, energy above ( EB:1, EE:3 ) GeV, and chi2 less than ( EB:16, EE:50 ) are used.'},
	    {'path': 'EcalEndcap/EETimingTask/EETMT in-time vs BX-1 amplitude EE +', 'description': 'Correlation between in-time amplitude and BX-1 out-of-time amplitude. Only events with kGood reconstruction flag set, energy above ( EB:1, EE:3 ) GeV, and chi2 less than ( EB:16, EE:50 ) are used.'}])
ecallayout(dqmitems, 'Ecal/Layouts/05 Timing/10 Amplitude Correlation, BX+1',
	   [{'path': 'EcalBarrel/EBTimingTask/EBTMT in-time vs BX+1 amplitude', 'description': 'Correlation between in-time amplitude and BX+1 out-of-time amplitude. Only events with kGood reconstruction flag set, energy above ( EB:1, EE:3 ) GeV, and chi2 less than ( EB:16, EE:50 ) are used.'}],
	   [{'path': 'EcalEndcap/EETimingTask/EETMT in-time vs BX+1 amplitude EE -', 'description': 'Correlation between in-time amplitude and BX+1 out-of-time amplitude. Only events with kGood reconstruction flag set, energy above ( EB:1, EE:3 ) GeV, and chi2 less than ( EB:16, EE:50 ) are used.'},
	    {'path': 'EcalEndcap/EETimingTask/EETMT in-time vs BX+1 amplitude EE +', 'description': 'Correlation between in-time amplitude and BX+1 out-of-time amplitude. Only events with kGood reconstruction flag set, energy above ( EB:1, EE:3 ) GeV, and chi2 less than ( EB:16, EE:50 ) are used.'}])      
ecallayout(dqmitems, 'Ecal/Layouts/05 Timing/11 Pulse Shape Chi2',
           [{'path': 'EcalBarrel/EBTimingTask/EBTMT EB Chi2', 'description': 'Chi2 of the pulse reconstruction.'}],
           [{'path': 'EcalEndcap/EETimingTask/EETMT EEM Chi2', 'description': 'Chi2 of the pulse reconstruction.'},
            {'path': 'EcalEndcap/EETimingTask/EETMT EEP Chi2', 'description': 'Chi2 of the pulse reconstruction.'}])
# By SuperModule _______________
for (detector, label, maxchannel) in [('Endcap', 'EE', 9), ('Barrel', 'EB', 18)]: # Loop over EB,EE
  for sign in ['-', '+']: # Loop over z-side
    for channel in range(1, maxchannel+1): # Loop over channels
      channellabel = '%s%s%02d' % (label, sign, channel) # e.g. "EE+05"
      ecallayout(dqmitems,'Ecal/Layouts/05 Timing/By SuperModule/Quality/Quality %s' % channellabel,
                 [{'path': 'Ecal%s/%sTimingClient/%sTMT timing quality %s' % (detector, label, label, channellabel),
                   'description': 'Summary of the timing data quality. A channel is red if its mean timing is off by more than 2.0 or RMS is greater than 6.0. Channels with entries less than 5 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/05 Timing/By SuperModule/Distribution/Distribution %s' % channellabel,
                 [{'path': 'Ecal%s/%sTimingTask/%sTMT timing 1D %s' % (detector, label, label, channellabel),
                   'description': 'Distribution of the mean rec hit timing. Only hits with GOOD or OUT_OF_TIME reconstruction flags and energy above threshold are used. The energy thresholds are 1.000000 and 3.000000 for EB and EE respectively.'}])
      ecallayout(dqmitems,'Ecal/Layouts/05 Timing/By SuperModule/Mean/Mean %s' % channellabel,
                 [{'path': 'Ecal%s/%sTimingTask/%sTMT timing %s' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean rec hit timing. Only hits with GOOD or OUT_OF_TIME reconstruction flags and energy above threshold are used. Hits with |t| > 25.0 ns are discarded. The energy thresholds are 1.000000 and 3.000000 for EB and EE respectively.'}],
                 [{'path': 'Ecal%s/%sTimingClient/%sTMT timing mean %s' % (detector, label, label, channellabel),
                   'description': 'Distribution of per-channel timing mean. Channels with entries less than 5 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/05 Timing/By SuperModule/RMS/RMS %s' % channellabel,
                 [{'path': 'Ecal%s/%sTimingClient/%sTMT timing rms %s' % (detector, label, label, channellabel),
                   'description': '2D distribution of per-channel timing RMS. Channels with entries less than 5 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/05 Timing/By SuperModule/Vs Amplitude/Time vs Amplitude %s' % channellabel,
                 [{'path': 'Ecal%s/%sTimingTask/%sTMT timing vs amplitude %s' % (detector, label, label, channellabel),
                   'description': 'Correlation between hit timing and energy. Only hits with GOOD or OUT_OF_TIME reconstruction flags are used.'}])
      ecallayout(dqmitems,'Ecal/Layouts/05 Timing/By SuperModule/Laser/Blue Laser %s' % channellabel,
                 [{'path': 'Ecal%s/%sLaserTask/Laser3/%sLT timing %s L3' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean laser timing. Z scale is in LHC clocks. Due to the difference in pulse shape between laser and physics events, fit-based reconstruction is not completely reliable in extracting the timing. In general, a channel is filled only when a laser pulse was observed in it. When no laser signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the timing to spread randomly.'}])
      if detector == 'Barrel':
        continue
      ecallayout(dqmitems,'Ecal/Layouts/05 Timing/By SuperModule/Led/Led 1 %s' % channellabel,
                 [{'path': 'Ecal%s/%sLedTask/Led1/%sLDT timing %s L1' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean led timing. Z scale is in LHC clocks. Due to the difference in pulse shape between led and physics events, fit-based reconstruction is not completely reliable in extracting the timing. In general, a channel is filled only when a led pulse was observed in it. When no led signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the timing to spread randomly.'}])

#____________________ Layouts / 06 Trigger Primitives ____________________
ecallayout(dqmitems,'Ecal/Layouts/06 Trigger Primitives/00 Emulation Quality',
	   [{'path': 'EcalBarrel/EBSummaryClient/EBTTT emulator error quality summary','description': 'Summary of emulator matching quality. A tower is red if the number of events with Et emulation error is greater than 0.1 of total events. Towers with entries less than 3 are not considered.'}],
	   [{'path': 'EcalEndcap/EESummaryClient/EETTT EE - emulator error quality summary','description': 'Summary of emulator matching quality. A tower is red if the number of events with Et emulation error is greater than 0.1 of total events. Towers with entries less than 3 are not considered.'},
	    {'path': 'EcalEndcap/EESummaryClient/EETTT EE + emulator error quality summary','description': 'Summary of emulator matching quality. A tower is red if the number of events with Et emulation error is greater than 0.1 of total events. Towers with entries less than 3 are not considered.'}])
ecallayout(dqmitems, 'Ecal/Layouts/06 Trigger Primitives/01 Occupancy (Filtered)',
	   [{'path': 'EcalBarrel/EBOccupancyTask/EBOT TP digi thr occupancy', 'description': 'Occupancy for TP digis with Et > 4.0 GeV.'}],
	   [{'path': 'EcalEndcap/EEOccupancyTask/EEOT TP digi thr occupancy EE -', 'description': 'Occupancy for TP digis with Et > 4.0 GeV.'},
	    {'path': 'EcalEndcap/EEOccupancyTask/EEOT TP digi thr occupancy EE +', 'description': 'Occupancy for TP digis with Et > 4.0 GeV.'}])
ecallayout(dqmitems, 'Ecal/Layouts/06 Trigger Primitives/01 Occupancy (Filtered) in RCT Coordinates',
	   [{'path': 'EcalBarrel/EBOccupancyTask/TP digi thr occupancy in RCT coordinates', 'description': 'Occupancy for TP digis with Et > 4.0 GeV in RCT Coordinates.'}])
ecallayout(dqmitems, 'Ecal/Layouts/06 Trigger Primitives/02 Et Spectrum',
	   [{'path': 'EcalBarrel/EBTriggerTowerTask/EBTTT Et spectrum Real Digis', 'description': 'Distribution of the trigger primitive Et.'}],
	   [{'path': 'EcalEndcap/EETriggerTowerTask/EETTT Et spectrum Real Digis EE -', 'description': 'Distribution of the trigger primitive Et.'},
	    {'path': 'EcalEndcap/EETriggerTowerTask/EETTT Et spectrum Real Digis EE +', 'description': 'Distribution of the trigger primitive Et.'}])
ecallayout(dqmitems, 'Ecal/Layouts/06 Trigger Primitives/03 Emulation Et Spectrum',
	   [{'path': 'EcalBarrel/EBTriggerTowerTask/Emulated/EBTTT Et spectrum Emulated Digis max', 'description': 'Distribution of the maximum Et value within one emulated TP'}],
	   [{'path': 'EcalEndcap/EETriggerTowerTask/Emulated/EETTT Et spectrum Emulated Digis max EE -', 'description': 'Distribution of the maximum Et value within one emulated TP'},
	    {'path': 'EcalEndcap/EETriggerTowerTask/Emulated/EETTT Et spectrum Emulated Digis max EE +', 'description': 'Distribution of the maximum Et value within one emulated TP'}])
ecallayout(dqmitems, 'Ecal/Layouts/06 Trigger Primitives/04 Et Map',
	   [{'path': 'EcalBarrel/EBSummaryClient/EBTTT Et trigger tower summary', 'description': '2D distribution of the trigger primitive Et.'}],
	   [{'path': 'EcalEndcap/EESummaryClient/EETTT EE - Et trigger tower summary', 'description': '2D distribution of the trigger primitive Et.'},
	    {'path': 'EcalEndcap/EESummaryClient/EETTT EE + Et trigger tower summary', 'description': '2D distribution of the trigger primitive Et.'}])
ecallayout(dqmitems, 'Ecal/Layouts/06 Trigger Primitives/05 Timing',
	   [{'path': 'EcalBarrel/EBSummaryClient/EBTTT Trigger Primitives Timing summary', 'description': 'Emulator TP timing where the largest number of events had Et matches. Towers with entries less than 3 are not considered.'}],
	   [{'path': 'EcalEndcap/EESummaryClient/EETTT EE - Trigger Primitives Timing summary', 'description': 'Emulator TP timing where the largest number of events had Et matches. Towers with entries less than 3 are not considered.'},
	    {'path': 'EcalEndcap/EESummaryClient/EETTT EE + Trigger Primitives Timing summary', 'description': 'Emulator TP timing where the largest number of events had Et matches. Towers with entries less than 3 are not considered.'}])
ecallayout(dqmitems, 'Ecal/Layouts/06 Trigger Primitives/06 Non Single Timing',
	   [{'path': 'EcalBarrel/EBSummaryClient/EBTTT Trigger Primitives Non Single Timing summary', 'description': 'Fraction of events whose emulator TP timing did not agree with the majority. Towers with entries less than 3 are not considered.'}],
	   [{'path': 'EcalEndcap/EESummaryClient/EETTT EE - Trigger Primitives Non Single Timing summary', 'description': 'Fraction of events whose emulator TP timing did not agree with the majority. Towers with entries less than 3 are not considered.'},
	    {'path': 'EcalEndcap/EESummaryClient/EETTT EE + Trigger Primitives Non Single Timing summary', 'description': 'Fraction of events whose emulator TP timing did not agree with the majority. Towers with entries less than 3 are not considered.'}])
ecallayout(dqmitems, 'Ecal/Layouts/06 Trigger Primitives/07 Occupancy vs BX',
	   [{'path': 'EcalBarrel/EBTriggerTowerTask/EBTTT TP occupancy vs bx Real Digis', 'description': 'TP occupancy in different bunch crossing intervals. This plot is filled by data from physics data stream. It is normal to have very little entries in BX >= 3490.'}],
	   [{'path': 'EcalEndcap/EETriggerTowerTask/EETTT TP occupancy vs bx Real Digis EE -', 'description': 'TP occupancy in different bunch crossing intervals. This plot is filled by data from physics data stream. It is normal to have very little entries in BX >= 3490.'},
	    {'path': 'EcalEndcap/EETriggerTowerTask/EETTT TP occupancy vs bx Real Digis EE +', 'description': 'TP occupancy in different bunch crossing intervals. This plot is filled by data from physics data stream. It is normal to have very little entries in BX >= 3490.'}])
ecallayout(dqmitems, 'Ecal/Layouts/06 Trigger Primitives/08 Et vs BX',
	   [{'path': 'EcalBarrel/EBTriggerTowerTask/EBTTT Et vs bx Real Digis', 'description': 'Mean TP Et in different bunch crossing intervals. This plot is filled by data from physics data stream. It is normal to have very little entries in BX >= 3490.'}],
	   [{'path': 'EcalEndcap/EETriggerTowerTask/EETTT Et vs bx Real Digis EE -', 'description': 'Mean TP Et in different bunch crossing intervals. This plot is filled by data from physics data stream. It is normal to have very little entries in BX >= 3490.'},
	    {'path': 'EcalEndcap/EETriggerTowerTask/EETTT Et vs bx Real Digis EE +', 'description': 'Mean TP Et in different bunch crossing intervals. This plot is filled by data from physics data stream. It is normal to have very little entries in BX >= 3490.'}])
ecallayout(dqmitems, 'Ecal/Layouts/06 Trigger Primitives/09 Emulation Timing',
	   [{'path': 'EcalBarrel/EBTriggerTowerTask/EBTTT max TP matching index', 'description': 'Distribution of the index of emulated TP with the highest Et value.'}],
	   [{'path': 'EcalEndcap/EETriggerTowerTask/EETTT max TP matching index EE -', 'description': 'Distribution of the index of emulated TP with the highest Et value.'},
	    {'path': 'EcalEndcap/EETriggerTowerTask/EETTT max TP matching index EE +', 'description': 'Distribution of the index of emulated TP with the highest Et value.'}])
ecallayout(dqmitems, 'Ecal/Layouts/06 Trigger Primitives/10 TTF4 Occupancy',
	   [{'path': 'EcalBarrel/EBTriggerTowerTask/EBTTT TTF4 Occupancy',      'description': 'Occupancy for TP digis with TTF=4.'}],
	   [{'path': 'EcalEndcap/EETriggerTowerTask/EETTT TTF4 Occupancy EE -', 'description': 'Occupancy for TP digis with TTF=4.'},
	    {'path': 'EcalEndcap/EETriggerTowerTask/EETTT TTF4 Occupancy EE +', 'description': 'Occupancy for TP digis with TTF=4.'}])
ecallayout(dqmitems, 'Ecal/Layouts/06 Trigger Primitives/11 TTF4 vs Masking Status',
     [{'path': 'EcalBarrel/EBTriggerTowerTask/EBTTT TTF4 vs Masking Status',      'description': 'Summarizes whether a TT was masked in either the TPG TT or Strips records, or had an instance of TT Flag=4.<br/>GRAY: Masked, no TTF4,<br/>BLACK: Masked, has TTF4,<br/>BLUE: Not Masked, has TTF4.'}],
     [{'path': 'EcalEndcap/EETriggerTowerTask/EETTT TTF4 vs Masking Status EE -', 'description': 'Summarizes whether a TT was masked in either the TPG TT or Strips records, or had an instance of TT Flag=4.<br/>GRAY: Masked, no TTF4,<br/>BLACK: Masked, has TTF4,<br/>BLUE: Not Masked, has TTF4.'},
      {'path': 'EcalEndcap/EETriggerTowerTask/EETTT TTF4 vs Masking Status EE +', 'description': 'Summarizes whether a TT was masked in either the TPG TT or Strips records, or had an instance of TT Flag=4.<br/>GRAY: Masked, no TTF4,<br/>BLACK: Masked, has TTF4,<br/>BLUE: Not Masked, has TTF4.'}])
ecallayout(dqmitems, 'Ecal/Layouts/06 Trigger Primitives/12 TT Masking Status',
     [{'path': 'EcalBarrel/EBTriggerTowerTask/EBTTT TT Masking Status',      'description': 'Trigger tower masking status: a TT or strip is red if it is masked.'}],
     [{'path': 'EcalEndcap/EETriggerTowerTask/EETTT TT Masking Status EE -', 'description': 'Trigger tower masking status: a TT or strip is red if it is masked.'},
      {'path': 'EcalEndcap/EETriggerTowerTask/EETTT TT Masking Status EE +', 'description': 'Trigger tower masking status: a TT or strip is red if it is masked.'}])

# By SuperModule _______________
for (detector, label, maxchannel) in [('Endcap', 'EE', 9), ('Barrel', 'EB', 18)]: # Loop over EB,EE
  for sign in ['-', '+']: # Loop over z-side
    # Get initial FED and TCC offset
    if detector == 'Barrel':
      fed0 = 609 if sign == '-' else 627
      tcc0 = 36  if sign == '-' else 54
    else:
      fed0 = 603 if sign == '-' else 648
    for channel in range(1, maxchannel+1): # Loop over channels
      channellabel = '%s%s%02d' % (label, sign, channel) # e.g. 'EE+05'
      if detector == 'Endcap' and channel > 6: # in EE, FED number jumps after SuperModule 6
        fed0 = 594 if sign == '-' else 639
      fedNo = 'FED%3d TCC%2d' % (fed0+channel,tcc0+channel) if detector == 'Barrel' else 'FED%3d' % (fed0+channel) # e.g. EB:'TCC610 TCC37' / EE:'TCC604'
      ecallayout(dqmitems,'Ecal/Layouts/06 Trigger Primitives/By SuperModule/EmulMatching/Match %s' % channellabel,
                 [{'path': 'Ecal%s/%sTriggerTowerTask/%sTTT EmulMatch %s' % (detector, label, label, channellabel),
                   'description': 'Counter for TP "timing" (= index withing the emulated TP whose Et matched that of the real TP).'}])
      ecallayout(dqmitems,'Ecal/Layouts/06 Trigger Primitives/By SuperModule/Et/TP Et %s %s' % (channellabel, fedNo),
                 [{'path': 'Ecal%s/%sTriggerTowerTask/%sTTT Et map Real Digis %s' % (detector, label, label, channellabel),
                   'description': '2D distribution of the trigger primitive Et.'}])
      ecallayout(dqmitems,'Ecal/Layouts/06 Trigger Primitives/By SuperModule/Mask/TT Masking Status%s %s' % (channellabel, fedNo),
                 [{'path': 'Ecal%s/%sTriggerTowerTask/TTStatus/%sTTT TT Masking Status%s' % (detector, label, label, channellabel),
                   'description': 'A trigger tower or pseudo-strip is filled if it is masked.'}])

#____________________ Layouts / 07 Selective Readout ____________________
ecallayout(dqmitems, 'Ecal/Layouts/07 Selective Readout/00 DCC Data Size',
	   [{'path': 'EcalBarrel/EBSelectiveReadoutTask/EBSRT event size vs DCC', 'description': 'Distribution of the per-DCC data size.'}],
	   [{'path': 'EcalEndcap/EESelectiveReadoutTask/EESRT event size vs DCC', 'description': 'Distribution of the per-DCC data size.'}])
ecallayout(dqmitems, 'Ecal/Layouts/07 Selective Readout/01 DCC Data Size',
	   [{'path': 'EcalBarrel/EBSelectiveReadoutTask/EBSRT DCC event size', 'description': 'Mean and spread of the per-DCC data size.'}],
	   [{'path': 'EcalEndcap/EESelectiveReadoutTask/EESRT DCC event size', 'description': 'Mean and spread of the per-DCC data size.'}])
ecallayout(dqmitems, 'Ecal/Layouts/07 Selective Readout/02 DCC Data Size',
	   [{'path': 'EcalBarrel/EBSelectiveReadoutTask/EBSRT event size', 'description': 'Distribution of per-DCC data size.'}],
	   [{'path': 'EcalEndcap/EESelectiveReadoutTask/EESRT event size EE -', 'description': 'Distribution of per-DCC data size.'},
	    {'path': 'EcalEndcap/EESelectiveReadoutTask/EESRT event size EE +', 'description': 'Distribution of per-DCC data size.'}])
ecallayout(dqmitems, 'Ecal/Layouts/07 Selective Readout/03 Tower Data Size',
	   [{'path': 'EcalBarrel/EBSelectiveReadoutTask/EBSRT tower event size', 'description': '2D distribution of the mean data size from each readout unit.'}],
	   [{'path': 'EcalEndcap/EESelectiveReadoutTask/EESRT tower event size EE -', 'description': '2D distribution of the mean data size from each readout unit.'},
	    {'path': 'EcalEndcap/EESelectiveReadoutTask/EESRT tower event size EE +', 'description': '2D distribution of the mean data size from each readout unit.'}])
ecallayout(dqmitems, 'Ecal/Layouts/07 Selective Readout/04 Payload High Interest',
	   [{'path': 'EcalBarrel/EBSelectiveReadoutTask/EBSRT high interest payload', 'description': 'Total data size from all high interest towers.'}],
	   [{'path': 'EcalEndcap/EESelectiveReadoutTask/EESRT high interest payload EE -', 'description': 'Total data size from all high interest towers.'},
	    {'path': 'EcalEndcap/EESelectiveReadoutTask/EESRT high interest payload EE +', 'description': 'Total data size from all high interest towers.'}])
ecallayout(dqmitems, 'Ecal/Layouts/07 Selective Readout/05 Payload Low Interest',
	   [{'path': 'EcalBarrel/EBSelectiveReadoutTask/EBSRT low interest payload', 'description': 'Total data size from all low interest towers.'}],
	   [{'path': 'EcalEndcap/EESelectiveReadoutTask/EESRT low interest payload EE -', 'description': 'Total data size from all low interest towers.'},
	    {'path': 'EcalEndcap/EESelectiveReadoutTask/EESRT low interest payload EE +', 'description': 'Total data size from all low interest towers.'}])
ecallayout(dqmitems, 'Ecal/Layouts/07 Selective Readout/06 ZS Filter Output (High Int.)',
	   [{'path': 'EcalBarrel/EBSelectiveReadoutTask/EBSRT high interest ZS filter output', 'description': 'Output of the ZS filter for high interest towers.'}],
	   [{'path': 'EcalEndcap/EESelectiveReadoutTask/EESRT high interest ZS filter output EE -', 'description': 'Output of the ZS filter for high interest towers.'},
	    {'path': 'EcalEndcap/EESelectiveReadoutTask/EESRT high interest ZS filter output EE +', 'description': 'Output of the ZS filter for high interest towers.'}])
ecallayout(dqmitems, 'Ecal/Layouts/07 Selective Readout/07 ZS Filter Output (Low Int.)',
	   [{'path': 'EcalBarrel/EBSelectiveReadoutTask/EBSRT low interest ZS filter output', 'description': 'Output of the ZS filter for low interest towers.'}],
	   [{'path': 'EcalEndcap/EESelectiveReadoutTask/EESRT low interest ZS filter output EE -', 'description': 'Output of the ZS filter for low interest towers.'},
	    {'path': 'EcalEndcap/EESelectiveReadoutTask/EESRT low interest ZS filter output EE +', 'description': 'Output of the ZS filter for low interest towers.'}])
ecallayout(dqmitems, 'Ecal/Layouts/07 Selective Readout/08 High Interest Rate',
	   [{'path': 'EcalBarrel/EBSelectiveReadoutTask/EBSRT high interest TT Flags', 'description': 'Occurrence rate of high interest TT flags.'}],
	   [{'path': 'EcalEndcap/EESelectiveReadoutTask/EESRT high interest TT Flags EE -', 'description': 'Occurrence rate of high interest TT flags.'},
	    {'path': 'EcalEndcap/EESelectiveReadoutTask/EESRT high interest TT Flags EE +', 'description': 'Occurrence rate of high interest TT flags.'}])
ecallayout(dqmitems, 'Ecal/Layouts/07 Selective Readout/09 Medium Interest Rate',
	   [{'path': 'EcalBarrel/EBSelectiveReadoutTask/EBSRT medium interest TT Flags', 'description': 'Occurrence rate of medium interest TT flags.'}],
	   [{'path': 'EcalEndcap/EESelectiveReadoutTask/EESRT medium interest TT Flags EE -', 'description': 'Occurrence rate of medium interest TT flags.'},
	    {'path': 'EcalEndcap/EESelectiveReadoutTask/EESRT medium interest TT Flags EE +', 'description': 'Occurrence rate of medium interest TT flags.'}])
ecallayout(dqmitems, 'Ecal/Layouts/07 Selective Readout/10 Low Interest Rate',
	   [{'path': 'EcalBarrel/EBSelectiveReadoutTask/EBSRT low interest TT Flags', 'description': 'Occurrence rate of low interest TT flags.'}],
	   [{'path': 'EcalEndcap/EESelectiveReadoutTask/EESRT low interest TT Flags EE -', 'description': 'Occurrence rate of low interest TT flags.'},
	    {'path': 'EcalEndcap/EESelectiveReadoutTask/EESRT low interest TT Flags EE +', 'description': 'Occurrence rate of low interest TT flags.'}])
ecallayout(dqmitems, 'Ecal/Layouts/07 Selective Readout/11 TT Flags',
	   [{'path': 'EcalBarrel/EBSelectiveReadoutTask/EBSRT TT Flags', 'description': 'Distribution of the trigger tower flags.'}],
	   [{'path': 'EcalEndcap/EESelectiveReadoutTask/EESRT TT Flags EE -', 'description': 'Distribution of the trigger tower flags.'},
	    {'path': 'EcalEndcap/EESelectiveReadoutTask/EESRT TT Flags EE +', 'description': 'Distribution of the trigger tower flags.'}])
ecallayout(dqmitems, 'Ecal/Layouts/07 Selective Readout/12 Full Readout Flags',
	   [{'path': 'EcalBarrel/EBSelectiveReadoutTask/EBSRT full readout SR Flags', 'description': 'Occurrence rate of full readout flag.'}],
	   [{'path': 'EcalEndcap/EESelectiveReadoutTask/EESRT full readout SR Flags EE -', 'description': 'Occurrence rate of full readout flag.'},
	    {'path': 'EcalEndcap/EESelectiveReadoutTask/EESRT full readout SR Flags EE +', 'description': 'Occurrence rate of full readout flag.'}])
ecallayout(dqmitems, 'Ecal/Layouts/07 Selective Readout/13 Zero Suppression Flags',
	   [{'path': 'EcalBarrel/EBSelectiveReadoutTask/EBSRT zero suppression 1 SR Flags', 'description': 'Occurrence rate of zero suppression 1 flags.'}],
	   [{'path': 'EcalEndcap/EESelectiveReadoutTask/EESRT zero suppression 1 SR Flags EE -', 'description': 'Occurrence rate of zero suppression 1 flags.'},
	    {'path': 'EcalEndcap/EESelectiveReadoutTask/EESRT zero suppression 1 SR Flags EE +', 'description': 'Occurrence rate of zero suppression 1 flags.'}])
ecallayout(dqmitems, 'Ecal/Layouts/07 Selective Readout/14 Forced Readout Flags',
	   [{'path': 'EcalBarrel/EBSelectiveReadoutTask/EBSRT readout unit with SR forced', 'description': 'Occurrence rate of forced selective readout.'}],
	   [{'path': 'EcalEndcap/EESelectiveReadoutTask/EESRT readout unit with SR forced EE -', 'description': 'Occurrence rate of forced selective readout.'},
	    {'path': 'EcalEndcap/EESelectiveReadoutTask/EESRT readout unit with SR forced EE +', 'description': 'Occurrence rate of forced selective readout.'}])
ecallayout(dqmitems, 'Ecal/Layouts/07 Selective Readout/15 Full Readout Flag Dropped',
	   [{'path': 'EcalBarrel/EBSelectiveReadoutTask/EBSRT FR Flagged Dropped Readout', 'description': 'Occurrence rate of unit drop when the unit is flagged as full-readout.'}],
	   [{'path': 'EcalEndcap/EESelectiveReadoutTask/EESRT FR Flagged Dropped Readout EE -', 'description': 'Occurrence rate of unit drop when the unit is flagged as full-readout.'},
	    {'path': 'EcalEndcap/EESelectiveReadoutTask/EESRT FR Flagged Dropped Readout EE +', 'description': 'Occurrence rate of unit drop when the unit is flagged as full-readout.'}])
ecallayout(dqmitems, 'Ecal/Layouts/07 Selective Readout/16 ZS Flag Readout',
	   [{'path': 'EcalBarrel/EBSelectiveReadoutTask/EBSRT ZS Flagged Fully Readout', 'description': 'Occurrence rate of full readout when unit is flagged as zero-suppressed.'}],
	   [{'path': 'EcalEndcap/EESelectiveReadoutTask/EESRT ZS Flagged Fully Readout EE -', 'description': 'Occurrence rate of full readout when unit is flagged as zero-suppressed.'},
	    {'path': 'EcalEndcap/EESelectiveReadoutTask/EESRT ZS Flagged Fully Readout EE +', 'description': 'Occurrence rate of full readout when unit is flagged as zero-suppressed.'}])

#____________________ Layouts / 08 Laser ____________________
ecallayout(dqmitems, 'Ecal/Layouts/08 Laser/00 Calibration Event Rate',
	   [{'path': 'EcalCalibration/EventInfo/Calibration event rate', 'description': 'Status of each element of the calibration sequence. This histogram shows the fraction of a calibration element being triggered in the laser or LED sequence. Green laser + Blue laser + IR laser = 1. LED 1+ LED 2 = 1.'}])
ecallayout(dqmitems, 'Ecal/Layouts/08 Laser/01 Quality Summary L2 (Green)',
	   [{'path': 'EcalBarrel/EBSummaryClient/EBLT laser quality summary L2', 'description': 'Summary of the laser data quality. A channel is red either if mean / expected < 0.1, or if mean / expected > 2.06, or if RMS / expected > 0.3, or if mean timing is off from expected by 0.5. Expected amplitudes and timings are 1700.0, 1300.0, 1700.0, 1700.0 and 4.2, 4.2, 4.2, 4.2 for lasers 1, 2, 3, and 4 respectively. Channels with less than 3 are not considered.'}],
	   [{'path': 'EcalEndcap/EESummaryClient/EELT EE - laser quality summary L2', 'description': 'Summary of the laser data quality. A channel is red either if mean / expected < 0.1, or if mean / expected > 2.06, or if RMS / expected > 0.3, or if mean timing is off from expected by 0.5. Expected amplitudes and timings are 1700.0, 1300.0, 1700.0, 1700.0 and 4.2, 4.2, 4.2, 4.2 for lasers 1, 2, 3, and 4 respectively. Channels with less than 3 are not considered.'},
	    {'path': 'EcalEndcap/EESummaryClient/EELT EE + laser quality summary L2', 'description': 'Summary of the laser data quality. A channel is red either if mean / expected < 0.1, or if mean / expected > 2.06, or if RMS / expected > 0.3, or if mean timing is off from expected by 0.5. Expected amplitudes and timings are 1700.0, 1300.0, 1700.0, 1700.0 and 4.2, 4.2, 4.2, 4.2 for lasers 1, 2, 3, and 4 respectively. Channels with less than 3 are not considered.'}])
ecallayout(dqmitems, 'Ecal/Layouts/08 Laser/01 Quality Summary L3 (Blue)',
	   [{'path': 'EcalBarrel/EBSummaryClient/EBLT laser quality summary L3', 'description': 'Summary of the laser data quality. A channel is red either if mean / expected < 0.1, or if mean / expected > 2.06, or if RMS / expected > 0.3, or if mean timing is off from expected by 0.5. Expected amplitudes and timings are 1700.0, 1300.0, 1700.0, 1700.0 and 4.2, 4.2, 4.2, 4.2 for lasers 1, 2, 3, and 4 respectively. Channels with less than 3 are not considered.'}],
	   [{'path': 'EcalEndcap/EESummaryClient/EELT EE - laser quality summary L3', 'description': 'Summary of the laser data quality. A channel is red either if mean / expected < 0.1, or if mean / expected > 2.06, or if RMS / expected > 0.3, or if mean timing is off from expected by 0.5. Expected amplitudes and timings are 1700.0, 1300.0, 1700.0, 1700.0 and 4.2, 4.2, 4.2, 4.2 for lasers 1, 2, 3, and 4 respectively. Channels with less than 3 are not considered.'},
	    {'path': 'EcalEndcap/EESummaryClient/EELT EE + laser quality summary L3', 'description': 'Summary of the laser data quality. A channel is red either if mean / expected < 0.1, or if mean / expected > 2.06, or if RMS / expected > 0.3, or if mean timing is off from expected by 0.5. Expected amplitudes and timings are 1700.0, 1300.0, 1700.0, 1700.0 and 4.2, 4.2, 4.2, 4.2 for lasers 1, 2, 3, and 4 respectively. Channels with less than 3 are not considered.'}])
ecallayout(dqmitems, 'Ecal/Layouts/08 Laser/02 Amplitude L2 (Green)',
	   [{'path': 'EcalBarrel/EBLaserTask/Laser2/EBLT amplitude map L2', 'description': '2D distribution of the mean laser amplitude. In general, a channel is filled only when a laser pulse was observed in it. When no laser signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the mean to drop.'}],
	   [{'path': 'EcalEndcap/EELaserTask/Laser2/EELT amplitude map L2 EE -', 'description': '2D distribution of the mean laser amplitude. In general, a channel is filled only when a laser pulse was observed in it. When no laser signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the mean to drop.'},
	    {'path': 'EcalEndcap/EELaserTask/Laser2/EELT amplitude map L2 EE +', 'description': '2D distribution of the mean laser amplitude. In general, a channel is filled only when a laser pulse was observed in it. When no laser signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the mean to drop.'}])
ecallayout(dqmitems, 'Ecal/Layouts/08 Laser/02 Amplitude L3 (Blue)',
	   [{'path': 'EcalBarrel/EBLaserTask/Laser3/EBLT amplitude map L3', 'description': '2D distribution of the mean laser amplitude. In general, a channel is filled only when a laser pulse was observed in it. When no laser signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the mean to drop.'}],
	   [{'path': 'EcalEndcap/EELaserTask/Laser3/EELT amplitude map L3 EE -', 'description': '2D distribution of the mean laser amplitude. In general, a channel is filled only when a laser pulse was observed in it. When no laser signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the mean to drop.'},
	    {'path': 'EcalEndcap/EELaserTask/Laser3/EELT amplitude map L3 EE +', 'description': '2D distribution of the mean laser amplitude. In general, a channel is filled only when a laser pulse was observed in it. When no laser signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the mean to drop.'}])
ecallayout(dqmitems, 'Ecal/Layouts/08 Laser/03 Amplitude RMS L2 (Green)',
	   [{'path': 'EcalBarrel/EBLaserClient/EBLT amplitude rms L2', 'description': '2D distribution of the amplitude RMS. Channels with less than 3 are not considered.'}],
	   [{'path': 'EcalEndcap/EELaserClient/EELT amplitude rms L2', 'description': '2D distribution of the amplitude RMS. Channels with less than 3 are not considered.'}])
ecallayout(dqmitems, 'Ecal/Layouts/08 Laser/03 Amplitude RMS L3 (Blue)',
	   [{'path': 'EcalBarrel/EBLaserClient/EBLT amplitude rms L3', 'description': '2D distribution of the amplitude RMS. Channels with less than 3 are not considered.'}],
	   [{'path': 'EcalEndcap/EELaserClient/EELT amplitude rms L3', 'description': '2D distribution of the amplitude RMS. Channels with less than 3 are not considered.'}])
ecallayout(dqmitems, 'Ecal/Layouts/08 Laser/04 Occupancy',
	   [{'path': 'EcalBarrel/EBOccupancyTask/EBOT laser digi occupancy', 'description': 'Laser signal digi occupancy. Channels are filled regardless of the existance of the actual laser pulses.'}],
	   [{'path': 'EcalEndcap/EEOccupancyTask/EEOT laser digi occupancy EE -', 'description': 'Laser signal digi occupancy. Channels are filled regardless of the existance of the actual laser pulses.'},
	    {'path': 'EcalEndcap/EEOccupancyTask/EEOT laser digi occupancy EE +', 'description': 'Laser signal digi occupancy. Channels are filled regardless of the existance of the actual laser pulses.'}])
ecallayout(dqmitems, 'Ecal/Layouts/08 Laser/05 Timing Spread L2 (Green)',
	   [{'path': 'EcalBarrel/EBLaserClient/EBLT laser timing rms map L2', 'description': '2D distribution of the laser timing RMS. Z scale is in LHC clocks. Channels with less than 3 are not considered.'}],
	   [{'path': 'EcalEndcap/EELaserClient/EELT laser timing rms map L2', 'description': '2D distribution of the laser timing RMS. Z scale is in LHC clocks. Channels with less than 3 are not considered.'}])
ecallayout(dqmitems, 'Ecal/Layouts/08 Laser/05 Timing Spread L3 (Blue)',
	   [{'path': 'EcalBarrel/EBLaserClient/EBLT laser timing rms map L3', 'description': '2D distribution of the laser timing RMS. Z scale is in LHC clocks. Channels with less than 3 are not considered.'}],
	   [{'path': 'EcalEndcap/EELaserClient/EELT laser timing rms map L3', 'description': '2D distribution of the laser timing RMS. Z scale is in LHC clocks. Channels with less than 3 are not considered.'}])
ecallayout(dqmitems, 'Ecal/Layouts/08 Laser/06 PN Quality Summary L2 (Green)',
	   [{'path': 'EcalBarrel/EBSummaryClient/EBLT PN laser quality summary L2', 'description': 'Summary of the laser data quality in the PN diodes. A channel is red if mean / expected < 0.1 or RMS / expected > 1.0. Expected amplitudes are 800.0, 800.0, 800.0, 800.0 for laser 1, 2, 3, and 4 respectively. Channels with less than 3 are not considered.'}],
	   [{'path': 'EcalEndcap/EESummaryClient/EELT PN laser quality summary L2', 'description': 'Summary of the laser data quality in the PN diodes. A channel is red if mean / expected < 0.1 or RMS / expected > 1.0. Expected amplitudes are 800.0, 800.0, 800.0, 800.0 for laser 1, 2, 3, and 4 respectively. Channels with less than 3 are not considered.'}])
ecallayout(dqmitems, 'Ecal/Layouts/08 Laser/06 PN Quality Summary L3 (Blue)',
	   [{'path': 'EcalBarrel/EBSummaryClient/EBLT PN laser quality summary L3', 'description': 'Summary of the laser data quality in the PN diodes. A channel is red if mean / expected < 0.1 or RMS / expected > 1.0. Expected amplitudes are 800.0, 800.0, 800.0, 800.0 for laser 1, 2, 3, and 4 respectively. Channels with less than 3 are not considered.'}],
	   [{'path': 'EcalEndcap/EESummaryClient/EELT PN laser quality summary L3', 'description': 'Summary of the laser data quality in the PN diodes. A channel is red if mean / expected < 0.1 or RMS / expected > 1.0. Expected amplitudes are 800.0, 800.0, 800.0, 800.0 for laser 1, 2, 3, and 4 respectively. Channels with less than 3 are not considered.'}])
# By SuperModule _______________
for (detector, label, maxchannel) in [('Endcap', 'EE', 9), ('Barrel', 'EB', 18)]: # Loop over EB,EE
  for sign in ['-', '+']: # Loop over z-side
    for channel in range(1, maxchannel+1): # Loop over channels
      channellabel = '%s%s%02d' % (label, sign, channel) # e.g. "EE+05"
      # Laser2 ___________
      ecallayout(dqmitems,'Ecal/Layouts/08 Laser/Laser2 (Green)/Quality/Quality %s' % channellabel,
                 [{'path': 'Ecal%s/%sLaserClient/%sLT laser quality L2 %s' % (detector, label, label, channellabel),
                   'description': 'Summary of the laser data quality. A channel is red either if mean / expected < 0.1, or if mean / expected > 2.06, or if RMS / expected > 0.3, or if mean timing is off from expected by 0.5. Expected amplitudes and timings are 1700.0, 1300.0, 1700.0, 1700.0 and 4.2, 4.2, 4.2, 4.2 for lasers 1, 2, 3, and 4 respectively. Channels with less than 3 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/08 Laser/Laser2 (Green)/Amplitude/Amplitude %s' % channellabel,
                 [{'path': 'Ecal%s/%sLaserTask/Laser2/%sLT amplitude %s L2' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean laser amplitude. In general, a channel is filled only when a laser pulse was observed in it. When no laser signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the mean to drop.'}],
                 [{'path': 'Ecal%s/%sLaserClient/%sLT amplitude L2 %s' % (detector, label, label, channellabel),
                   'description': 'Distribution of the mean amplitude seen in each crystal. Channels with less than 3 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/08 Laser/Laser2 (Green)/Timing/Timing %s' % channellabel,
                 [{'path': 'Ecal%s/%sLaserTask/Laser2/%sLT timing %s L2' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean laser timing. Z scale is in LHC clocks. Due to the difference in pulse shape between laser and physics events, fit-based reconstruction is not completely reliable in extracting the timing. In general, a channel is filled only when a laser pulse was observed in it. When no laser signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the timing to spread randomly.'}],
                 [{'path': 'Ecal%s/%sLaserClient/%sLT laser timing mean L2 %s' % (detector, label, label, channellabel),
                   'description': 'Distribution of the timing in each crystal channel. X scale is in LHC clocks. Channels with less than 3 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/08 Laser/Laser2 (Green)/APD Over PN/APD Over PN %s' % channellabel,
                 [{'path': 'Ecal%s/%sLaserTask/Laser2/%sLT amplitude over PN %s L2' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean APD/PN value (event mean of per-event ratio).'}])
      ecallayout(dqmitems,'Ecal/Layouts/08 Laser/Laser2 (Green)/Shape/Shape %s' % channellabel,
                 [{'path': 'Ecal%s/%sLaserTask/Laser2/%sLT shape %s L2' % (detector, label, label, channellabel),
                   'description': 'Laser mean pulse shape. One slice corresponds to one readout tower (5x5 crystals). In general, a slice is filled only when a laser pulse was observed in the tower. When no laser signal was observed for longer than 3 lumi sections, the slices start to get filled with 0 amplitude, causing the shape to flatten.'}])
      # Laser3 ___________
      ecallayout(dqmitems,'Ecal/Layouts/08 Laser/Laser3 (Blue)/Quality/Quality %s' % channellabel,
                 [{'path': 'Ecal%s/%sLaserClient/%sLT laser quality L3 %s' % (detector, label, label, channellabel),
                   'description': 'Summary of the laser data quality. A channel is red either if mean / expected < 0.1, or if mean / expected > 2.06, or if RMS / expected > 0.3, or if mean timing is off from expected by 0.5. Expected amplitudes and timings are 1700.0, 1300.0, 1700.0, 1700.0 and 4.2, 4.2, 4.2, 4.2 for lasers 1, 2, 3, and 4 respectively. Channels with less than 3 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/08 Laser/Laser3 (Blue)/Amplitude/Amplitude %s' % channellabel,
                 [{'path': 'Ecal%s/%sLaserTask/Laser3/%sLT amplitude %s L3' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean laser amplitude. In general, a channel is filled only when a laser pulse was observed in it. When no laser signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the mean to drop.'}],
                 [{'path': 'Ecal%s/%sLaserClient/%sLT amplitude L3 %s' % (detector, label, label, channellabel),
                   'description': 'Distribution of the mean amplitude seen in each crystal. Channels with less than 3 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/08 Laser/Laser3 (Blue)/Timing/Timing %s' % channellabel,
                 [{'path': 'Ecal%s/%sLaserTask/Laser3/%sLT timing %s L3' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean laser timing. Z scale is in LHC clocks. Due to the difference in pulse shape between laser and physics events, fit-based reconstruction is not completely reliable in extracting the timing. In general, a channel is filled only when a laser pulse was observed in it. When no laser signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the timing to spread randomly.'}],
                 [{'path': 'Ecal%s/%sLaserClient/%sLT laser timing mean L3 %s' % (detector, label, label, channellabel),
                   'description': 'Distribution of the timing in each crystal channel. X scale is in LHC clocks. Channels with less than 3 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/08 Laser/Laser3 (Blue)/APD Over PN/APD Over PN %s' % channellabel,
                 [{'path': 'Ecal%s/%sLaserTask/Laser3/%sLT amplitude over PN %s L3' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean APD/PN value (event mean of per-event ratio).'}])
      ecallayout(dqmitems,'Ecal/Layouts/08 Laser/Laser3 (Blue)/Shape/Shape %s' % channellabel,
                 [{'path': 'Ecal%s/%sLaserTask/Laser3/%sLT shape %s L3' % (detector, label, label, channellabel),
                   'description': 'Laser mean pulse shape. One slice corresponds to one readout tower (5x5 crystals). In general, a slice is filled only when a laser pulse was observed in the tower. When no laser signal was observed for longer than 3 lumi sections, the slices start to get filled with 0 amplitude, causing the shape to flatten.'}])
      # Laser4 ___________
      ecallayout(dqmitems,'Ecal/Layouts/08 Laser/Laser4 (IR)/Quality/Quality %s' % channellabel,
                 [{'path': 'Ecal%s/%sLaserClient/%sLT laser quality L4 %s' % (detector, label, label, channellabel),
                   'description': 'Summary of the laser data quality. A channel is red either if mean / expected < 0.1, or if mean / expected > 2.06, or if RMS / expected > 0.3, or if mean timing is off from expected by 0.5. Expected amplitudes and timings are 1700.0, 1300.0, 1700.0, 1700.0 and 4.2, 4.2, 4.2, 4.2 for lasers 1, 2, 3, and 4 respectively. Channels with less than 3 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/08 Laser/Laser4 (IR)/Amplitude/Amplitude %s' % channellabel,
                 [{'path': 'Ecal%s/%sLaserTask/Laser4/%sLT amplitude %s L4' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean laser amplitude. In general, a channel is filled only when a laser pulse was observed in it. When no laser signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the mean to drop.'}],
                 [{'path': 'Ecal%s/%sLaserClient/%sLT amplitude L4 %s' % (detector, label, label, channellabel),
                   'description': 'Distribution of the mean amplitude seen in each crystal. Channels with less than 3 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/08 Laser/Laser4 (IR)/Timing/Timing %s' % channellabel,
                 [{'path': 'Ecal%s/%sLaserTask/Laser4/%sLT timing %s L4' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean laser timing. Z scale is in LHC clocks. Due to the difference in pulse shape between laser and physics events, fit-based reconstruction is not completely reliable in extracting the timing. In general, a channel is filled only when a laser pulse was observed in it. When no laser signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the timing to spread randomly.'}],
                 [{'path': 'Ecal%s/%sLaserClient/%sLT laser timing mean L4 %s' % (detector, label, label, channellabel),
                   'description': 'Distribution of the timing in each crystal channel. X scale is in LHC clocks. Channels with less than 3 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/08 Laser/Laser4 (IR)/APD Over PN/APD Over PN %s' % channellabel,
                 [{'path': 'Ecal%s/%sLaserTask/Laser4/%sLT amplitude over PN %s L4' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean APD/PN value (event mean of per-event ratio).'}])
      ecallayout(dqmitems,'Ecal/Layouts/08 Laser/Laser4 (IR)/Shape/Shape %s' % channellabel,
                 [{'path': 'Ecal%s/%sLaserTask/Laser4/%sLT shape %s L4' % (detector, label, label, channellabel),
                   'description': 'Laser mean pulse shape. One slice corresponds to one readout tower (5x5 crystals). In general, a slice is filled only when a laser pulse was observed in the tower. When no laser signal was observed for longer than 3 lumi sections, the slices start to get filled with 0 amplitude, causing the shape to flatten.'}])
      # Exclude EE[+-]01,04,05,06,09
      if detector == 'Endcap':
        if channel == 1 or channel == 4 or channel == 5 or channel == 6 or channel == 9:
	        continue
      ecallayout(dqmitems,'Ecal/Layouts/08 Laser/Laser2 (Green)/PN Amplitude/Amplitude %s' % channellabel,
                 [{'path': 'Ecal%s/%sLaserTask/Laser2/PN/Gain16/%sLT PNs amplitude %s G16 L2' % (detector, label, label, channellabel),
                   'description': 'Mean laser pulse amplitude in the PN diodes. In general, a PN channel is filled only when a laser pulse was observed in the crystals that are associated to the diode. When no laser signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the mean to drop.'}])
      ecallayout(dqmitems,'Ecal/Layouts/08 Laser/Laser3 (Blue)/PN Amplitude/Amplitude %s' % channellabel,
                 [{'path': 'Ecal%s/%sLaserTask/Laser3/PN/Gain16/%sLT PNs amplitude %s G16 L3' % (detector, label, label, channellabel),
                   'description': 'Mean laser pulse amplitude in the PN diodes. In general, a PN channel is filled only when a laser pulse was observed in the crystals that are associated to the diode. When no laser signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the mean to drop.'}])
      ecallayout(dqmitems,'Ecal/Layouts/08 Laser/Laser4 (IR)/PN Amplitude/Amplitude %s' % channellabel,
                 [{'path': 'Ecal%s/%sLaserTask/Laser4/PN/Gain16/%sLT PNs amplitude %s G16 L4' % (detector, label, label, channellabel),
                   'description': 'Mean laser pulse amplitude in the PN diodes. In general, a PN channel is filled only when a laser pulse was observed in the crystals that are associated to the diode. When no laser signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the mean to drop.'}])

#____________________ Layouts / 09 Led ____________________
ecallayout(dqmitems, 'Ecal/Layouts/09 Led/00 Calibration Event Rate',
	   [{'path': 'EcalCalibration/EventInfo/Calibration event rate', 'description': 'Status of each element of the calibration sequence. This histogram shows the rate of a cerntain element being triggered in calibration sequence.'}])
ecallayout(dqmitems, 'Ecal/Layouts/09 Led/01 Quality Summary L1',
	   [{'path': 'EcalEndcap/EESummaryClient/EELDT EE - led quality summary L1', 'description': 'Summary of the led data quality. A channel is red either if mean / expected < 0.1, or if RMS / expected > 0.5, or if mean timing is off from expected by 1.0. Expected amplitudes and timings are 200.0, 10.0 and 4.4, 4.5 for leds 1 and 2 respectively. Channels with less than 3 are not considered.'},
	    {'path': 'EcalEndcap/EESummaryClient/EELDT EE + led quality summary L1', 'description': 'Summary of the led data quality. A channel is red either if mean / expected < 0.1, or if RMS / expected > 0.5, or if mean timing is off from expected by 1.0. Expected amplitudes and timings are 200.0, 10.0 and 4.4, 4.5 for leds 1 and 2 respectively. Channels with less than 3 are not considered.'}])
ecallayout(dqmitems, 'Ecal/Layouts/09 Led/01 Quality Summary L2',
	   [{'path': 'EcalEndcap/EESummaryClient/EELDT EE - led quality summary L2', 'description': 'Summary of the led data quality. A channel is red either if mean / expected < 0.1, or if RMS / expected > 0.5, or if mean timing is off from expected by 1.0. Expected amplitudes and timings are 200.0, 10.0 and 4.4, 4.5 for leds 1 and 2 respectively. Channels with less than 3 are not considered.'},
	    {'path': 'EcalEndcap/EESummaryClient/EELDT EE + led quality summary L2', 'description': 'Summary of the led data quality. A channel is red either if mean / expected < 0.1, or if RMS / expected > 0.5, or if mean timing is off from expected by 1.0. Expected amplitudes and timings are 200.0, 10.0 and 4.4, 4.5 for leds 1 and 2 respectively. Channels with less than 3 are not considered.'}])
ecallayout(dqmitems, 'Ecal/Layouts/09 Led/02 Amplitude L1',
	   [{'path': 'EcalEndcap/EELedTask/Led1/EELDT amplitude map L1 EE -', 'description': '2D distribution of the mean led amplitude. In general, a channel is filled only when a led pulse was observed in it. When no led signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the mean to drop.'},
	    {'path': 'EcalEndcap/EELedTask/Led1/EELDT amplitude map L1 EE +', 'description': '2D distribution of the mean led amplitude. In general, a channel is filled only when a led pulse was observed in it. When no led signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the mean to drop.'}])
ecallayout(dqmitems, 'Ecal/Layouts/09 Led/02 Amplitude L2',
	   [{'path': 'EcalEndcap/EELedTask/Led2/EELDT amplitude map L2 EE -', 'description': '2D distribution of the mean led amplitude. In general, a channel is filled only when a led pulse was observed in it. When no led signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the mean to drop.'},
	    {'path': 'EcalEndcap/EELedTask/Led2/EELDT amplitude map L2 EE +', 'description': '2D distribution of the mean led amplitude. In general, a channel is filled only when a led pulse was observed in it. When no led signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the mean to drop.'}])
ecallayout(dqmitems, 'Ecal/Layouts/09 Led/03 Amplitude RMS L1',
	   [{'path': 'EcalEndcap/EELedClient/EELDT amplitude RMS L1', 'description': '2D distribution of the amplitude RMS. Channels with less than 3 are not considered.'}])
ecallayout(dqmitems, 'Ecal/Layouts/09 Led/03 Amplitude RMS L2',
	   [{'path': 'EcalEndcap/EELedClient/EELDT amplitude RMS L2', 'description': '2D distribution of the amplitude RMS. Channels with less than 3 are not considered.'}])
ecallayout(dqmitems, 'Ecal/Layouts/09 Led/04 Occupancy',
	   [{'path': 'EcalEndcap/EEOccupancyTask/EEOT led digi occupancy EE -', 'description': 'Led signal digi occupancy. Channels are filled regardless of the existance of the actual led pulses.'},
	    {'path': 'EcalEndcap/EEOccupancyTask/EEOT led digi occupancy EE +', 'description': 'Led signal digi occupancy. Channels are filled regardless of the existance of the actual led pulses.'}])
ecallayout(dqmitems, 'Ecal/Layouts/09 Led/05 Timing Spread L1',
	   [{'path': 'EcalEndcap/EELedClient/EELDT timing RMS L1', 'description': '2D distribution of the led timing RMS. Z scale is in LHC clocks. Channels with less than 3 are not considered.'}])
ecallayout(dqmitems, 'Ecal/Layouts/09 Led/05 Timing Spread L2',
	   [{'path': 'EcalEndcap/EELedClient/EELDT timing RMS L2', 'description': '2D distribution of the led timing RMS. Z scale is in LHC clocks. Channels with less than 3 are not considered.'}])
ecallayout(dqmitems, 'Ecal/Layouts/09 Led/06 PN Quality Summary L1',
	   [{'path': 'EcalEndcap/EESummaryClient/EELDT PN led quality summary L1', 'description': 'Summary of the led data quality in the PN diodes. A channel is red if mean / expected < 0.1 or RMS / expected > 1.0. Expected amplitudes are 800.0, 800.0 for led 1 and 2 respectively. Channels with less than 3 are not considered.'}])
ecallayout(dqmitems, 'Ecal/Layouts/09 Led/06 PN Quality Summary L2',
	   [{'path': 'EcalEndcap/EESummaryClient/EELDT PN led quality summary L2', 'description': 'Summary of the led data quality in the PN diodes. A channel is red if mean / expected < 0.1 or RMS / expected > 1.0. Expected amplitudes are 800.0, 800.0 for led 1 and 2 respectively. Channels with less than 3 are not considered.'}])
# By SuperModule _______________
for (detector, label, maxchannel) in [('Endcap', 'EE', 9)]: # Loop over EE
  for sign in ['-', '+']: # Loop over z-side
    for channel in range(1, maxchannel+1): # Loop over channels
      channellabel = '%s%s%02d' % (label, sign, channel) # e.g. "EE+05"
      # Led1 ___________
      ecallayout(dqmitems,'Ecal/Layouts/09 Led/Led1(Blue)/Quality/Quality %s' % channellabel,
                 [{'path': 'Ecal%s/%sLedClient/%sLDT led quality L1 %s' % (detector, label, label, channellabel),
                   'description': 'Summary of the led data quality. A channel is red either if mean / expected < 0.1, or if RMS / expected > 0.5, or if mean timing is off from expected by 1.0. Expected amplitudes and timings are 200.0, 10.0 and 4.4, 4.5 for leds 1 and 2 respectively. Channels with less than 3 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/09 Led/Led1(Blue)/Amplitude/Amplitude %s' % channellabel,
                 [{'path': 'Ecal%s/%sLedTask/Led1/%sLDT amplitude %s L1' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean led amplitude. In general, a channel is filled only when a led pulse was observed in it. When no led signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the mean to drop.'}],
                 [{'path': 'Ecal%s/%sLedClient/%sLDT amplitude L1 %s' % (detector, label, label, channellabel),
                   'description': 'Distribution of the mean amplitude seen in each crystal. Channels with less than 3 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/09 Led/Led1(Blue)/Timing/Timing %s' % channellabel,
                 [{'path': 'Ecal%s/%sLedTask/Led1/%sLDT timing %s L1' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean led timing. Z scale is in LHC clocks. Due to the difference in pulse shape between led and physics events, fit-based reconstruction is not completely reliable in extracting the timing. In general, a channel is filled only when a led pulse was observed in it. When no led signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the timing to spread randomly.'}],
                 [{'path': 'Ecal%s/%sLedClient/%sLDT led timing L1 %s' % (detector, label, label, channellabel),
                   'description': 'Distribution of the timing in each crystal channel. Z scale is in LHC clocks. Channels with less than 3 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/09 Led/Led1(Blue)/APD Over PN/APD Over PN %s' % channellabel,
                 [{'path': 'Ecal%s/%sLedTask/Led1/%sLDT amplitude over PN %s L1' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean APD/PN value (event mean of per-event ratio).'}])
      ecallayout(dqmitems,'Ecal/Layouts/09 Led/Led1(Blue)/Shape/Shape %s' % channellabel,
                 [{'path': 'Ecal%s/%sLedTask/Led1/%sLDT shape %s L1' % (detector, label, label, channellabel),
                   'description': 'Led mean pulse shape. One slice corresponds to one readout tower (5x5 crystals). In general, a slice is filled only when a led pulse was observed in the tower. When no led signal was observed for longer than 3 lumi sections, the slices start to get filled with 0 amplitude, causing the shape to flatten.'}])
      # Led2 ___________
      ecallayout(dqmitems,'Ecal/Layouts/09 Led/Led2(Orange)/Quality/Quality %s' % channellabel,
                 [{'path': 'Ecal%s/%sLedClient/%sLDT led quality L2 %s' % (detector, label, label, channellabel),
                   'description': 'Summary of the led data quality. A channel is red either if mean / expected < 0.1, or if RMS / expected > 0.5, or if mean timing is off from expected by 1.0. Expected amplitudes and timings are 200.0, 10.0 and 4.4, 4.5 for leds 1 and 2 respectively. Channels with less than 3 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/09 Led/Led2(Orange)/Amplitude/Amplitude %s' % channellabel,
                 [{'path': 'Ecal%s/%sLedTask/Led2/%sLDT amplitude %s L2' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean led amplitude. In general, a channel is filled only when a led pulse was observed in it. When no led signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the mean to drop.'}],
                 [{'path': 'Ecal%s/%sLedClient/%sLDT amplitude L2 %s' % (detector, label, label, channellabel),
                   'description': 'Distribution of the mean amplitude seen in each crystal. Channels with less than 3 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/09 Led/Led2(Orange)/Timing/Timing %s' % channellabel,
                 [{'path': 'Ecal%s/%sLedTask/Led2/%sLDT timing %s L2' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean led timing. Z scale is in LHC clocks. Due to the difference in pulse shape between led and physics events, fit-based reconstruction is not completely reliable in extracting the timing. In general, a channel is filled only when a led pulse was observed in it. When no led signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the timing to spread randomly.'}],
                 [{'path': 'Ecal%s/%sLedClient/%sLDT led timing L2 %s' % (detector, label, label, channellabel),
                   'description': 'Distribution of the timing in each crystal channel. Z scale is in LHC clocks. Channels with less than 3 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/09 Led/Led2(Orange)/APD Over PN/APD Over PN %s' % channellabel,
                 [{'path': 'Ecal%s/%sLedTask/Led2/%sLDT amplitude over PN %s L2' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean APD/PN value (event mean of per-event ratio).'}])
      ecallayout(dqmitems,'Ecal/Layouts/09 Led/Led2(Orange)/Shape/Shape %s' % channellabel,
                 [{'path': 'Ecal%s/%sLedTask/Led2/%sLDT shape %s L2' % (detector, label, label, channellabel),
                   'description': 'Led mean pulse shape. One slice corresponds to one readout tower (5x5 crystals). In general, a slice is filled only when a led pulse was observed in the tower. When no led signal was observed for longer than 3 lumi sections, the slices start to get filled with 0 amplitude, causing the shape to flatten.'}])
      # Exclude EE[+-]01,04,05,06,09
      if detector == 'Endcap':
        if channel == 1 or channel == 4 or channel == 5 or channel == 6 or channel == 9:
	        continue
      ecallayout(dqmitems,'Ecal/Layouts/09 Led/Led1(Blue)/PN Amplitude/Amplitude %s' % channellabel,
                 [{'path': 'Ecal%s/%sLedTask/Led1/PN/Gain16/%sLDT PNs amplitude %s G16 L1' % (detector, label, label, channellabel),
                   'description': 'Mean led pulse amplitude in the PN diodes. In general, a PN channel is filled only when a led pulse was observed in the crystals that are associated to the diode. When no led signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the mean to drop.'}])
      ecallayout(dqmitems,'Ecal/Layouts/09 Led/Led2(Orange)/PN Amplitude/Amplitude %s' % channellabel,
                 [{'path': 'Ecal%s/%sLedTask/Led2/PN/Gain16/%sLDT PNs amplitude %s G16 L2' % (detector, label, label, channellabel),
                   'description': 'Mean led pulse amplitude in the PN diodes. In general, a PN channel is filled only when a led pulse was observed in the crystals that are associated to the diode. When no led signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the mean to drop.'}])

#____________________ Layouts / 10 Test Pulse ____________________
ecallayout(dqmitems, 'Ecal/Layouts/10 Test Pulse/00 PN Quality Summary G16',[{'path': 'EcalBarrel/EBSummaryClient/EBTPT PN test pulse quality G16 summary', 'description': 'Summary of test pulse data quality for PN diodes. A channel is red if mean amplitude is lower than the threshold, or RMS is greater than threshold. The mean and RMS thresholds are 12.5, 200.0 and 20.0, 20.0 for gains 1 and 16 respectively. Channels with entries less than 3 are not considered.'}],[{'path': 'EcalEndcap/EESummaryClient/EETPT PN test pulse quality G16 summary', 'description': 'Summary of test pulse data quality for PN diodes. A channel is red if mean amplitude is lower than the threshold, or RMS is greater than threshold. The mean and RMS thresholds are 12.5, 200.0 and 20.0, 20.0 for gains 1 and 16 respectively. Channels with entries less than 3 are not considered.'}])
# By SuperModule _______________
for (detector, label, maxchannel) in [('Endcap', 'EE', 9), ('Barrel', 'EB', 18)]: # Loop over EB,EE
  for sign in ['-', '+']: # Loop over z-side
    for channel in range(1, maxchannel+1): # Loop over channels
      channellabel = '%s%s%02d' % (label, sign, channel) # e.g. "EE+05"
      ecallayout(dqmitems,'Ecal/Layouts/10 Test Pulse/Gain12/Amplitude/Amplitude %s' % channellabel,
                 [{'path': 'Ecal%s/%sTestPulseTask/Gain12/%sTPT amplitude %s G12' % (detector, label, label, channellabel),
                   'description': 'Test pulse amplitude.'}])
      # Exclude EE[+-]01,04,05,06,09
      if detector == 'Endcap':
        if channel == 1 or channel == 4 or channel == 5 or channel == 6 or channel == 9:
	        continue
      ecallayout(dqmitems,'Ecal/Layouts/10 Test Pulse/PNGain16/Amplitude %s' % channellabel,
                 [{'path': 'Ecal%s/%sTestPulseTask/PN/Gain16/%sTPT PNs amplitude %s G16' % (detector, label, label, channellabel),
                   'description': 'Test pulse amplitude in the PN diodes.'}])

#____________________ Layouts / 11 Trend ____________________
ecallayout(dqmitems, 'Ecal/Layouts/11 Trend/00 Errors',
	   [{'path': 'Ecal/Trends/RawDataTask accumulated number of sync errors', 'description': 'Accumulated trend of the number of synchronization errors (L1A & BX mismatches) between DCC and FE in this run.'}],
	   [{'path': 'Ecal/Trends/IntegrityTask number of integrity errors', 'description': 'Trend of the number of integrity errors.'}])
ecallayout(dqmitems, 'Ecal/Layouts/11 Trend/01 Number of Digis',
	   [{'path': 'Ecal/Trends/OccupancyTask EB number of digis', 'description': 'Trend of the per-event number of digis.'}],
	   [{'path': 'Ecal/Trends/OccupancyTask EE number of digis', 'description': 'Trend of the per-event number of digis.'}])
ecallayout(dqmitems, 'Ecal/Layouts/11 Trend/02 Number of RecHits',
	   [{'path': 'Ecal/Trends/OccupancyTask EB number of filtered recHits', 'description': 'Trend of the per-event number of rec hits with GOOD reconstruction flag and E > 0.5 GeV.'}],
	   [{'path': 'Ecal/Trends/OccupancyTask EE number of filtered recHits', 'description': 'Trend of the per-event number of rec hits with GOOD reconstruction flag and E > 0.5 GeV.'}])
ecallayout(dqmitems, 'Ecal/Layouts/11 Trend/03 Number of TPs',
	   [{'path': 'Ecal/Trends/OccupancyTask EB number of filtered TP digis', 'description': 'Trend of the per-event number of TP digis with Et > 4.0 GeV.'}],
	   [{'path': 'Ecal/Trends/OccupancyTask EE number of filtered TP digis', 'description': 'Trend of the per-event number of TP digis with Et > 4.0 GeV.'}])
ecallayout(dqmitems, 'Ecal/Layouts/11 Trend/04 Presample Mean',
	   [{'path': 'Ecal/Trends/PresampleClient EB pedestal mean max - min', 'description': 'Trend of presample spread in EB / EE. Y value indicates the difference between maximum and minimum presample mean values within the subdetector.'}],
	   [{'path': 'Ecal/Trends/PresampleClient EE pedestal mean max - min', 'description': 'Trend of presample spread in EB / EE. Y value indicates the difference between maximum and minimum presample mean values within the subdetector.'}])
ecallayout(dqmitems, 'Ecal/Layouts/11 Trend/05 Presample RMS',
	   [{'path': 'Ecal/Trends/PresampleClient EB pedestal rms max', 'description': 'Trend of presample RMS averaged over all channels in EB / EE.'}],
	   [{'path': 'Ecal/Trends/PresampleClient EE pedestal rms max', 'description': 'Trend of presample RMS averaged over all channels in EB / EE.'}])
ecallayout(dqmitems, 'Ecal/Layouts/11 Trend/06 Basic Clusters',
	   [{'path': 'Ecal/Trends/ClusterTask EB number of basic clusters', 'description': 'Trend of the number of basic clusters per event in EB/EE.'},
	    {'path': 'Ecal/Trends/ClusterTask EB size of basic clusters', 'description': 'Trend of the mean size of the basic clusters.'}],
	   [{'path': 'Ecal/Trends/ClusterTask EE number of basic clusters', 'description': 'Trend of the number of basic clusters per event in EB/EE.'},
	    {'path': 'Ecal/Trends/ClusterTask EE size of basic clusters', 'description': 'Trend of the mean size of the basic clusters.'}])
ecallayout(dqmitems, 'Ecal/Layouts/11 Trend/07 Super Clusters',
	   [{'path': 'Ecal/Trends/ClusterTask EB number of super clusters', 'description': 'Trend of the number of super clusters per event in EB/EE.'},
	    {'path': 'Ecal/Trends/ClusterTask EB size of super clusters', 'description': 'Trend of the mean size (number of crystals) of the super clusters.'}],
	   [{'path': 'Ecal/Trends/ClusterTask EE number of super clusters', 'description': 'Trend of the number of super clusters per event in EB/EE.'},
	    {'path': 'Ecal/Trends/ClusterTask EE size of super clusters', 'description': 'Trend of the mean size (number of crystals) of the super clusters.'}])
ecallayout(dqmitems, 'Ecal/Layouts/11 Trend/08 Timing mean',
	   [{'path': 'Ecal/Trends/TimingClient EB timing mean', 'description': 'Trend of timing mean. Plots simple average of all channel timing means at each lumisection.'}],
	   [{'path': 'Ecal/Trends/TimingClient EE timing mean', 'description': 'Trend of timing mean. Plots simple average of all channel timing means at each lumisection.'}])
ecallayout(dqmitems, 'Ecal/Layouts/11 Trend/09 Timing rms',
	   [{'path': 'Ecal/Trends/TimingClient EB timing rms', 'description': 'Trend of timing rms. Plots simple average of all channel timing rms at each lumisection.'}],
	   [{'path': 'Ecal/Trends/TimingClient EE timing rms', 'description': 'Trend of timing rms. Plots simple average of all channel timing rms at each lumisection.'}])

#____________________ Layouts / 12 By SuperModule ____________________
for (detector, label, maxchannel) in [('Endcap', 'EE', 9), ('Barrel', 'EB', 18)]: # Loop over EB,EE
  for sign in ['-', '+']: # Loop over z-side
    for channel in range(1, maxchannel+1): # Loop over channels
      channellabel = '%s%s%02d' % (label, sign, channel) # e.g. "EE+05"
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/00 Integrity' % channellabel,
                 [{'path': 'Ecal%s/%sIntegrityClient/%sIT data integrity quality %s' % (detector, label, label, channellabel),
                   'description': 'Summary of the data integrity. A channel is red if more than 0.01 of its entries have integrity errors.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/01 FEStatus' % channellabel,
                 [{'path': 'Ecal%s/%sStatusFlagsTask/FEStatus/%sSFT front-end status bits %s' % (detector, label, label, channellabel),
                   'description': 'FE status counter.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/02 Digi Occupancy' % channellabel,
                 [{'path': 'Ecal%s/%sOccupancyTask/%sOT digi occupancy %s' % (detector, label, label, channellabel),
                   'description': 'Digi occupancy.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/03 Presample Quality' % channellabel,
                 [{'path': 'Ecal%s/%sPedestalOnlineClient/%sPOT pedestal quality G12 %s' % (detector, label, label, channellabel),
                   'description': 'Summary of the presample data quality. A channel is red if presample mean is off by 25.0 from 200.0 or RMS is greater than 3.0. RMS threshold is 6.0 in the forward region (|eta| > 2.1). Channels with entries less than 6 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/04 Presample Mean' % channellabel,
                 [{'path': 'Ecal%s/%sPedestalOnlineTask/Gain12/%sPOT pedestal %s G12' % (detector, label, label, channellabel),
                   'description': '2D distribution of mean presample value.'}],
		 [{'path': 'Ecal%s/%sPedestalOnlineClient/%sPOT pedestal mean G12 %s' % (detector, label, label, channellabel),
                   'description': '1D distribution of the mean presample value in each crystal. Channels with entries less than 6 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/05 Presample RMS' % channellabel,
                 [{'path': 'Ecal%s/%sPedestalOnlineClient/%sPOT pedestal rms G12 %s' % (detector, label, label, channellabel),
                   'description': 'Distribution of the presample RMS of each channel. Channels with entries less than 6 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/06 Energy' % channellabel,
                 [{'path': 'Ecal%s/%sOccupancyTask/%sOT rec hit energy %s' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean rec hit energy.'}],
		 [{'path': 'Ecal%s/%sOccupancyTask/%sOT energy spectrum %s' % (detector, label, label, channellabel),
                   'description': 'Rec hit energy distribution.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/07 Timing Quality' % channellabel,
                 [{'path': 'Ecal%s/%sTimingClient/%sTMT timing quality %s' % (detector, label, label, channellabel),
                   'description': 'Summary of the timing data quality. A channel is red if its mean timing is off by more than 2.0 or RMS is greater than 6.0. Channels with entries less than 5 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/08 Timing All' % channellabel,
                 [{'path': 'Ecal%s/%sTimingTask/%sTMT timing 1D %s' % (detector, label, label, channellabel),
                   'description': 'Distribution of the mean rec hit timing. Only hits with GOOD or OUT_OF_TIME reconstruction flags and energy above threshold are used. The energy thresholds are 1.000000 and 3.000000 for EB and EE respectively.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/09 Timing Mean' % channellabel,
                 [{'path': 'Ecal%s/%sTimingTask/%sTMT timing %s' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean rec hit timing. Only hits with GOOD or OUT_OF_TIME reconstruction flags and energy above threshold are used. Hits with |t| > 25.0 ns are discarded. The energy thresholds are 1.000000 and 3.000000 for EB and EE respectively.'}],
		 [{'path': 'Ecal%s/%sTimingClient/%sTMT timing mean %s' % (detector, label, label, channellabel),
                   'description': 'Distribution of per-channel timing mean. Channels with entries less than 5 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/10 Timing RMS' % channellabel,
                 [{'path': 'Ecal%s/%sTimingClient/%sTMT timing rms %s' % (detector, label, label, channellabel),
                   'description': '2D distribution of per-channel timing RMS. Channels with entries less than 5 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/11 Timing Vs Amplitude' % channellabel,
                 [{'path': 'Ecal%s/%sTimingTask/%sTMT timing vs amplitude %s' % (detector, label, label, channellabel),
                   'description': 'Correlation between hit timing and energy. Only hits with GOOD or OUT_OF_TIME reconstruction flags are used.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/12 Trigger Primitives' % channellabel,
                 [{'path': 'Ecal%s/%sTriggerTowerTask/%sTTT Et map Real Digis %s' % (detector, label, label, channellabel),
                   'description': '2D distribution of the trigger primitive Et.'}],
                 [{'path': 'Ecal%s/%sTriggerTowerTask/%sTTT EmulMatch %s' % (detector, label, label, channellabel),
                   'description': 'Counter for TP "timing" (= index withing the emulated TP whose Et matched that of the real TP).'}])
      # Laser ___________
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Laser/00 Quality L2 (Green)' % channellabel,
                 [{'path': 'Ecal%s/%sLaserClient/%sLT laser quality L2 %s' % (detector, label, label, channellabel),
                   'description': 'Summary of the laser data quality. A channel is red either if mean / expected < 0.1, or if mean / expected > 2.06, or if RMS / expected > 0.3, or if mean timing is off from expected by 0.5. Expected amplitudes and timings are 1700.0, 1300.0, 1700.0, 1700.0 and 4.2, 4.2, 4.2, 4.2 for lasers 1, 2, 3, and 4 respectively. Channels with less than 3 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Laser/00 Quality L3 (Blue)' % channellabel,
                 [{'path': 'Ecal%s/%sLaserClient/%sLT laser quality L3 %s' % (detector, label, label, channellabel),
                   'description': 'Summary of the laser data quality. A channel is red either if mean / expected < 0.1, or if mean / expected > 2.06, or if RMS / expected > 0.3, or if mean timing is off from expected by 0.5. Expected amplitudes and timings are 1700.0, 1300.0, 1700.0, 1700.0 and 4.2, 4.2, 4.2, 4.2 for lasers 1, 2, 3, and 4 respectively. Channels with less than 3 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Laser/00 Quality L4 (IR)' % channellabel,
                 [{'path': 'Ecal%s/%sLaserClient/%sLT laser quality L4 %s' % (detector, label, label, channellabel),
                   'description': 'Summary of the laser data quality. A channel is red either if mean / expected < 0.1, or if mean / expected > 2.06, or if RMS / expected > 0.3, or if mean timing is off from expected by 0.5. Expected amplitudes and timings are 1700.0, 1300.0, 1700.0, 1700.0 and 4.2, 4.2, 4.2, 4.2 for lasers 1, 2, 3, and 4 respectively. Channels with less than 3 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Laser/01 Amplitude L2 (Green)' % channellabel,
                 [{'path': 'Ecal%s/%sLaserTask/Laser2/%sLT amplitude %s L2' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean laser amplitude. In general, a channel is filled only when a laser pulse was observed in it. When no laser signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the mean to drop.'}],
                 [{'path': 'Ecal%s/%sLaserClient/%sLT amplitude L2 %s' % (detector, label, label, channellabel),
                   'description': 'Distribution of the mean amplitude seen in each crystal. Channels with less than 3 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Laser/01 Amplitude L3 (Blue)' % channellabel,
                 [{'path': 'Ecal%s/%sLaserTask/Laser3/%sLT amplitude %s L3' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean laser amplitude. In general, a channel is filled only when a laser pulse was observed in it. When no laser signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the mean to drop.'}],
                 [{'path': 'Ecal%s/%sLaserClient/%sLT amplitude L3 %s' % (detector, label, label, channellabel),
                   'description': 'Distribution of the mean amplitude seen in each crystal. Channels with less than 3 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Laser/01 Amplitude L4 (IR)' % channellabel,
                 [{'path': 'Ecal%s/%sLaserTask/Laser4/%sLT amplitude %s L4' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean laser amplitude. In general, a channel is filled only when a laser pulse was observed in it. When no laser signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the mean to drop.'}],
                 [{'path': 'Ecal%s/%sLaserClient/%sLT amplitude L4 %s' % (detector, label, label, channellabel),
                   'description': 'Distribution of the mean amplitude seen in each crystal. Channels with less than 3 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Laser/02 Timing L2 (Green)' % channellabel,
                 [{'path': 'Ecal%s/%sLaserTask/Laser2/%sLT timing %s L2' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean laser timing. Z scale is in LHC clocks. Due to the difference in pulse shape between laser and physics events, fit-based reconstruction is not completely reliable in extracting the timing. In general, a channel is filled only when a laser pulse was observed in it. When no laser signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the timing to spread randomly.'}],
                 [{'path': 'Ecal%s/%sLaserClient/%sLT laser timing mean L2 %s' % (detector, label, label, channellabel),
                   'description': 'Distribution of the timing in each crystal channel. X scale is in LHC clocks. Channels with less than 3 are not considered.'}],
                 [{'path': 'Ecal%s/%sLaserClient/%sLT laser timing rms L2 %s' % (detector, label, label, channellabel),
                   'description': 'Distribution of the timing RMS in each crystal channel. X scale is in LHC clocks. Channels with less than 3 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Laser/02 Timing L3 (Blue)' % channellabel,
                 [{'path': 'Ecal%s/%sLaserTask/Laser3/%sLT timing %s L3' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean laser timing. Z scale is in LHC clocks. Due to the difference in pulse shape between laser and physics events, fit-based reconstruction is not completely reliable in extracting the timing. In general, a channel is filled only when a laser pulse was observed in it. When no laser signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the timing to spread randomly.'}],
                 [{'path': 'Ecal%s/%sLaserClient/%sLT laser timing mean L3 %s' % (detector, label, label, channellabel),
                   'description': 'Distribution of the timing in each crystal channel. X scale is in LHC clocks. Channels with less than 3 are not considered.'}],
                 [{'path': 'Ecal%s/%sLaserClient/%sLT laser timing rms L3 %s' % (detector, label, label, channellabel),
                   'description': 'Distribution of the timing RMS in each crystal channel. X scale is in LHC clocks. Channels with less than 3 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Laser/02 Timing L4 (IR)' % channellabel,
                 [{'path': 'Ecal%s/%sLaserTask/Laser4/%sLT timing %s L4' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean laser timing. Z scale is in LHC clocks. Due to the difference in pulse shape between laser and physics events, fit-based reconstruction is not completely reliable in extracting the timing. In general, a channel is filled only when a laser pulse was observed in it. When no laser signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the timing to spread randomly.'}],
                 [{'path': 'Ecal%s/%sLaserClient/%sLT laser timing mean L4 %s' % (detector, label, label, channellabel),
                   'description': 'Distribution of the timing in each crystal channel. X scale is in LHC clocks. Channels with less than 3 are not considered.'}],
                 [{'path': 'Ecal%s/%sLaserClient/%sLT laser timing rms L4 %s' % (detector, label, label, channellabel),
                   'description': 'Distribution of the timing RMS in each crystal channel. X scale is in LHC clocks. Channels with less than 3 are not considered.'}])                   
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Laser/03 APD Over PN L2 (Green)' % channellabel,
                 [{'path': 'Ecal%s/%sLaserTask/Laser2/%sLT amplitude over PN %s L2' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean APD/PN value (event mean of per-event ratio).'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Laser/03 APD Over PN L3 (Blue)' % channellabel,
                 [{'path': 'Ecal%s/%sLaserTask/Laser3/%sLT amplitude over PN %s L3' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean APD/PN value (event mean of per-event ratio).'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Laser/03 APD Over PN L4 (IR)' % channellabel,
                 [{'path': 'Ecal%s/%sLaserTask/Laser4/%sLT amplitude over PN %s L4' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean APD/PN value (event mean of per-event ratio).'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Laser/04 Shape L2 (Green)' % channellabel,
                 [{'path': 'Ecal%s/%sLaserTask/Laser2/%sLT shape %s L2' % (detector, label, label, channellabel),
                   'description': 'Laser mean pulse shape. One slice corresponds to one readout tower (5x5 crystals). In general, a slice is filled only when a laser pulse was observed in the tower. When no laser signal was observed for longer than 3 lumi sections, the slices start to get filled with 0 amplitude, causing the shape to flatten.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Laser/04 Shape L3 (Blue)' % channellabel,
                 [{'path': 'Ecal%s/%sLaserTask/Laser3/%sLT shape %s L3' % (detector, label, label, channellabel),
                   'description': 'Laser mean pulse shape. One slice corresponds to one readout tower (5x5 crystals). In general, a slice is filled only when a laser pulse was observed in the tower. When no laser signal was observed for longer than 3 lumi sections, the slices start to get filled with 0 amplitude, causing the shape to flatten.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Laser/04 Shape L4 (IR)' % channellabel,
                 [{'path': 'Ecal%s/%sLaserTask/Laser4/%sLT shape %s L4' % (detector, label, label, channellabel),
                   'description': 'Laser mean pulse shape. One slice corresponds to one readout tower (5x5 crystals). In general, a slice is filled only when a laser pulse was observed in the tower. When no laser signal was observed for longer than 3 lumi sections, the slices start to get filled with 0 amplitude, causing the shape to flatten.'}])
      # Pedestal ___________
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Pedestal/00 Quality G01' % channellabel,
                 [{'path': 'Ecal%s/%sPedestalOnlineClient/%sPOT pedestal quality G01 %s' % (detector, label, label, channellabel),
                   'description': 'Summary of the pedestal quality for crystals. A channel is red if the pedestal mean is off from 200.0 by 25.0 or if the pedestal RMS is greater than threshold. RMS thresholds are 1.0, 1.2, 2.0 for gains 1, 6, and 12 respectively. Channels with entries less than 3 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Pedestal/00 Quality G06' % channellabel,
                 [{'path': 'Ecal%s/%sPedestalOnlineClient/%sPOT pedestal quality G06 %s' % (detector, label, label, channellabel),
                   'description': 'Summary of the pedestal quality for crystals. A channel is red if the pedestal mean is off from 200.0 by 25.0 or if the pedestal RMS is greater than threshold. RMS thresholds are 1.0, 1.2, 2.0 for gains 1, 6, and 12 respectively. Channels with entries less than 3 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Pedestal/00 Quality G12' % channellabel,
                 [{'path': 'Ecal%s/%sPedestalOnlineClient/%sPOT pedestal quality G12 %s' % (detector, label, label, channellabel),
                   'description': 'Summary of the pedestal quality for crystals. A channel is red if the pedestal mean is off from 200.0 by 25.0 or if the pedestal RMS is greater than threshold. RMS thresholds are 1.0, 1.2, 2.0 for gains 1, 6, and 12 respectively. Channels with entries less than 3 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Pedestal/01 Mean G01' % channellabel,
                 [{'path': 'Ecal%s/%sPedestalTask/Gain01/%sPT pedestal %s G01' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean pedestal.'}],
                 [{'path': 'Ecal%s/%sPedestalClient/%sPT pedestal mean G01 %s' % (detector, label, label, channellabel),
                   'description': 'Distribution of pedestal mean in each channel. Channels with entries less than 3 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Pedestal/01 Mean G06' % channellabel,
                 [{'path': 'Ecal%s/%sPedestalTask/Gain06/%sPT pedestal %s G06' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean pedestal.'}],
                 [{'path': 'Ecal%s/%sPedestalClient/%sPT pedestal mean G06 %s' % (detector, label, label, channellabel),
                   'description': 'Distribution of pedestal mean in each channel. Channels with entries less than 3 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Pedestal/01 Mean G12' % channellabel,
                 [{'path': 'Ecal%s/%sPedestalTask/Gain12/%sPT pedestal %s G12' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean pedestal.'}],
                 [{'path': 'Ecal%s/%sPedestalOnlineClient/%sPOT pedestal mean G12 %s' % (detector, label, label, channellabel),
                   'description': 'Distribution of pedestal mean in each channel. Channels with entries less than 3 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Pedestal/02 RMS G01' % channellabel,
                 [{'path': 'Ecal%s/%sPedestalOnlineClient/%sPOT pedestal rms G01 %s' % (detector, label, label, channellabel),
                   'description': 'Distribution of the pedestal RMS for each crystal channel. Channels with entries less than 3 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Pedestal/02 RMS G06' % channellabel,
                 [{'path': 'Ecal%s/%sPedestalOnlineClient/%sPOT pedestal rms G06 %s' % (detector, label, label, channellabel),
                   'description': 'Distribution of the pedestal RMS for each crystal channel. Channels with entries less than 3 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Pedestal/02 RMS G12' % channellabel,
                 [{'path': 'Ecal%s/%sPedestalOnlineClient/%sPOT pedestal rms G12 %s' % (detector, label, label, channellabel),
                   'description': 'Distribution of the pedestal RMS for each crystal channel. Channels with entries less than 3 are not considered.'}])
      if detector == 'Barrel':
	      continue
      # LED ___________
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Led/00 Quality L1' % channellabel,
                 [{'path': 'Ecal%s/%sLedClient/%sLDT led quality L1 %s' % (detector, label, label, channellabel),
                   'description': 'Summary of the led data quality. A channel is red either if mean / expected < 0.1, or if RMS / expected > 0.5, or if mean timing is off from expected by 1.0. Expected amplitudes and timings are 200.0, 10.0 and 4.4, 4.5 for leds 1 and 2 respectively. Channels with less than 3 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Led/00 Quality L2' % channellabel,
                 [{'path': 'Ecal%s/%sLedClient/%sLDT led quality L2 %s' % (detector, label, label, channellabel),
                   'description': 'Summary of the led data quality. A channel is red either if mean / expected < 0.1, or if RMS / expected > 0.5, or if mean timing is off from expected by 1.0. Expected amplitudes and timings are 200.0, 10.0 and 4.4, 4.5 for leds 1 and 2 respectively. Channels with less than 3 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Led/01 Amplitude L1' % channellabel,
                 [{'path': 'Ecal%s/%sLedTask/Led1/%sLDT amplitude %s L1' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean led amplitude. In general, a channel is filled only when a led pulse was observed in it. When no led signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the mean to drop.'}],
                 [{'path': 'Ecal%s/%sLedClient/%sLDT amplitude L1 %s' % (detector, label, label, channellabel),
                   'description': 'Distribution of the mean amplitude seen in each crystal. Channels with less than 3 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Led/01 Amplitude L2' % channellabel,
                 [{'path': 'Ecal%s/%sLedTask/Led2/%sLDT amplitude %s L2' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean led amplitude. In general, a channel is filled only when a led pulse was observed in it. When no led signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the mean to drop.'}],
                 [{'path': 'Ecal%s/%sLedClient/%sLDT amplitude L2 %s' % (detector, label, label, channellabel),
                   'description': 'Distribution of the mean amplitude seen in each crystal. Channels with less than 3 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Led/02 Timing L1' % channellabel,
                 [{'path': 'Ecal%s/%sLedTask/Led1/%sLDT timing %s L1' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean led timing. Z scale is in LHC clocks. Due to the difference in pulse shape between led and physics events, fit-based reconstruction is not completely reliable in extracting the timing. In general, a channel is filled only when a led pulse was observed in it. When no led signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the timing to spread randomly.'}],
                 [{'path': 'Ecal%s/%sLedClient/%sLDT led timing L1 %s' % (detector, label, label, channellabel),
                   'description': 'Distribution of the timing in each crystal channel. Z scale is in LHC clocks. Channels with less than 3 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Led/02 Timing L2' % channellabel,
                 [{'path': 'Ecal%s/%sLedTask/Led2/%sLDT timing %s L2' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean led timing. Z scale is in LHC clocks. Due to the difference in pulse shape between led and physics events, fit-based reconstruction is not completely reliable in extracting the timing. In general, a channel is filled only when a led pulse was observed in it. When no led signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the timing to spread randomly.'}],
                 [{'path': 'Ecal%s/%sLedClient/%sLDT led timing L2 %s' % (detector, label, label, channellabel),
                   'description': 'Distribution of the timing in each crystal channel. Z scale is in LHC clocks. Channels with less than 3 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Led/03 APD Over PN L1' % channellabel,
                 [{'path': 'Ecal%s/%sLedTask/Led1/%sLDT amplitude over PN %s L1' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean APD/PN value (event mean of per-event ratio).'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Led/03 APD Over PN L2' % channellabel,
                 [{'path': 'Ecal%s/%sLedTask/Led2/%sLDT amplitude over PN %s L2' % (detector, label, label, channellabel),
                   'description': '2D distribution of the mean APD/PN value (event mean of per-event ratio).'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Led/04 Shape L1' % channellabel,
                 [{'path': 'Ecal%s/%sLedTask/Led1/%sLDT shape %s L1' % (detector, label, label, channellabel),
                   'description': 'Led mean pulse shape. One slice corresponds to one readout tower (5x5 crystals). In general, a slice is filled only when a led pulse was observed in the tower. When no led signal was observed for longer than 3 lumi sections, the slices start to get filled with 0 amplitude, causing the shape to flatten.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Led/04 Shape L2' % channellabel,
                 [{'path': 'Ecal%s/%sLedTask/Led2/%sLDT shape %s L2' % (detector, label, label, channellabel),
                   'description': 'Led mean pulse shape. One slice corresponds to one readout tower (5x5 crystals). In general, a slice is filled only when a led pulse was observed in the tower. When no led signal was observed for longer than 3 lumi sections, the slices start to get filled with 0 amplitude, causing the shape to flatten.'}])
# PNs _______________
for (detector, label, maxchannel) in [('Endcap', 'EE', 9), ('Barrel', 'EB', 18)]: # Loop over EB,EE
  for sign in ['-', '+']: # Loop over z-side
    for channel in range(1, maxchannel+1): # Loop over channels
      # Exclude EE[+-]01,04,05,06,09
      if detector == 'Endcap':
        if channel == 1 or channel == 4 or channel == 5 or channel == 6 or channel == 9:
	        continue
      channellabel = '%s%s%02d' % (label, sign, channel) # e.g. "EE+05"
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/00 PN Digi Occupancy' % channellabel,
                 [{'path': 'Ecal%s/%sOccupancyTask/%sOT MEM digi occupancy %s' % (detector, label, label, channellabel),
                   'description': 'Occupancy of PN digis in calibration events.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/01 PN Presample' % channellabel,
                 [{'path': 'Ecal%s/%sPedestalOnlineTask/PN/%sPOT PN pedestal %s G16' % (detector, label, label, channellabel),
                   'description': 'Presample mean of PN signals.'}])
      # Laser ___________
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Laser/00 PN Amplitude L2' % channellabel,
                 [{'path': 'Ecal%s/%sLaserTask/Laser2/PN/Gain16/%sLT PNs amplitude %s G16 L2' % (detector, label, label, channellabel),
                   'description': 'Mean laser pulse amplitude in the PN diodes. In general, a PN channel is filled only when a laser pulse was observed in the crystals that are associated to the diode. When no laser signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the mean to drop.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Laser/00 PN Amplitude L3' % channellabel,
                 [{'path': 'Ecal%s/%sLaserTask/Laser3/PN/Gain16/%sLT PNs amplitude %s G16 L3' % (detector, label, label, channellabel),
                   'description': 'Mean laser pulse amplitude in the PN diodes. In general, a PN channel is filled only when a laser pulse was observed in the crystals that are associated to the diode. When no laser signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the mean to drop.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Laser/00 PN Amplitude L4' % channellabel,
                 [{'path': 'Ecal%s/%sLaserTask/Laser4/PN/Gain16/%sLT PNs amplitude %s G16 L4' % (detector, label, label, channellabel),
                   'description': 'Mean laser pulse amplitude in the PN diodes. In general, a PN channel is filled only when a laser pulse was observed in the crystals that are associated to the diode. When no laser signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the mean to drop.'}])
      # Test Pulse ___________
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Test Pulse/00 PN Amplitude G01' % channellabel,
                 [{'path': 'Ecal%s/%sTestPulseTask/PN/Gain01/%sTPT PNs amplitude %s G01' % (detector, label, label, channellabel),
                   'description': 'Test pulse amplitude in the PN diodes.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Test Pulse/00 PN Amplitude G16' % channellabel,
                 [{'path': 'Ecal%s/%sTestPulseTask/PN/Gain16/%sTPT PNs amplitude %s G16' % (detector, label, label, channellabel),
                   'description': 'Test pulse amplitude in the PN diodes.'}])
      # Pedestal ___________
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Pedestal/00 PN Pedestal G01' % channellabel,
                 [{'path': 'Ecal%s/%sPedestalTask/PN/Gain01/%sPDT PNs pedestal %s G01' % (detector, label, label, channellabel),
                   'description': 'Pedestal distribution of the PN diodes.'}],
		 [{'path': 'Ecal%s/%sPedestalClient/%sPDT PNs pedestal rms %s G01' % (detector, label, label, channellabel),
                   'description': 'Distribution of the pedestal RMS for each PN channel. Channels with entries less than 3 are not considered.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Pedestal/00 PN Pedestal G16' % channellabel,
                 [{'path': 'Ecal%s/%sPedestalTask/PN/Gain16/%sPDT PNs pedestal %s G16' % (detector, label, label, channellabel),
                   'description': 'Pedestal distribution of the PN diodes.'}],
                 [{'path': 'Ecal%s/%sPedestalClient/%sPDT PNs pedestal rms %s G16' % (detector, label, label, channellabel),
                   'description': 'Distribution of the pedestal RMS for each PN channel. Channels with entries less than 3 are not considered.'}])
      if detector == 'Barrel':
	      continue
     # LED ___________
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Led/00 PN Amplitude L1' % channellabel,
                 [{'path': 'Ecal%s/%sLedTask/Led1/PN/Gain16/%sLDT PNs amplitude %s G16 L1' % (detector, label, label, channellabel),
                   'description': 'Mean led pulse amplitude in the PN diodes. In general, a PN channel is filled only when a led pulse was observed in the crystals that are associated to the diode. When no led signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the mean to drop.'}])
      ecallayout(dqmitems,'Ecal/Layouts/12 By SuperModule/%s/Led/00 PN Amplitude L2' % channellabel,
                 [{'path': 'Ecal%s/%sLedTask/Led2/PN/Gain16/%sLDT PNs amplitude %s G16 L2' % (detector, label, label, channellabel),
                   'description': 'Mean led pulse amplitude in the PN diodes. In general, a PN channel is filled only when a led pulse was observed in the crystals that are associated to the diode. When no led signal was observed for longer than 3 lumi sections, the channels start to get filled with 0 amplitude, causing the mean to drop.'}])
