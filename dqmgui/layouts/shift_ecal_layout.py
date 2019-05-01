def ecallayout(i, p, *rows): i[p] = DQMItem(layout=rows)

ecallayout(dqmitems, '00 Shift/Ecal/00 Summary',[{'path': 'EcalBarrel/EBSummaryClient/EB global summary', 'description': 'Summary of the data quality. A channel is red if it is red in any one of RawData, Integrity, Timing, TriggerPrimitives, and HotCells task. A cluster of bad towers in this plot will cause the ReportSummary for the FED to go to 0 in online DQM.'}],[{'path': 'EcalEndcap/EESummaryClient/EE global summary EE -', 'description': 'Summary of the data quality. A channel is red if it is red in any one of RawData, Integrity, Timing, TriggerPrimitives, and HotCells task. A cluster of bad towers in this plot will cause the ReportSummary for the FED to go to 0 in online DQM.'}, {'path': 'EcalEndcap/EESummaryClient/EE global summary EE +', 'description': 'Summary of the data quality. A channel is red if it is red in any one of RawData, Integrity, Timing, TriggerPrimitives, and HotCells task. A cluster of bad towers in this plot will cause the ReportSummary for the FED to go to 0 in online DQM.'}])
ecallayout(dqmitems, '00 Shift/Ecal/01 FE Status',[{'path': 'EcalBarrel/EBSummaryClient/EBSFT front-end status summary', 'description': 'Summary of the raw data (DCC and front-end) quality. A channel is red if it has nonzero events with FE status that is different from any of ENABLED, DISABLED, SUPPRESSED, FIFOFULL, FIFOFULL_L1ADESYNC, and FORCEDZS. A FED can also go red if its number of L1A desynchronization errors is greater than 1.0 * log10(total entries).'}],[{'path': 'EcalEndcap/EESummaryClient/EESFT EE - front-end status summary', 'description': 'Summary of the raw data (DCC and front-end) quality. A channel is red if it has nonzero events with FE status that is different from any of ENABLED, DISABLED, SUPPRESSED, FIFOFULL, FIFOFULL_L1ADESYNC, and FORCEDZS. A FED can also go red if its number of L1A desynchronization errors is greater than 1.0 * log10(total entries).'}, {'path': 'EcalEndcap/EESummaryClient/EESFT EE + front-end status summary', 'description': 'Summary of the raw data (DCC and front-end) quality. A channel is red if it has nonzero events with FE status that is different from any of ENABLED, DISABLED, SUPPRESSED, FIFOFULL, FIFOFULL_L1ADESYNC, and FORCEDZS. A FED can also go red if its number of L1A desynchronization errors is greater than 1.0 * log10(total entries).'}])
ecallayout(dqmitems, '00 Shift/Ecal/02 Integrity',[{'path': 'EcalBarrel/EBSummaryClient/EBIT integrity quality summary', 'description': 'Summary of the data integrity. A channel is red if more than 0.01 of its entries have integrity errors. Also, an entire SuperModule can show red if there are more than 50 DCC-SRP or DCC-TCC Desync errors.'}],[{'path': 'EcalEndcap/EESummaryClient/EEIT EE - integrity quality summary', 'description': 'Summary of the data integrity. A channel is red if more than 0.01 of its entries have integrity errors. Also, an entire SuperModule can show red if there are more than 50 DCC-SRP or DCC-TCC Desync errors.'}, {'path': 'EcalEndcap/EESummaryClient/EEIT EE + integrity quality summary', 'description': 'Summary of the data integrity. A channel is red if more than 0.01 of its entries have integrity errors. Also, an entire SuperModule can show red if there are more than 50 DCC-SRP or DCC-TCC Desync errors.'}])
ecallayout(dqmitems, '00 Shift/Ecal/03 Occupancy',[{'path': 'EcalBarrel/EBOccupancyTask/EBOT digi occupancy', 'description': 'Digi occupancy.'}],[{'path': 'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE -', 'description': 'Digi occupancy.'}, {'path': 'EcalEndcap/EEOccupancyTask/EEOT digi occupancy EE +', 'description': 'Digi occupancy.'}])
ecallayout(dqmitems, '00 Shift/Ecal/04 Noise',[{'path': 'EcalBarrel/EBSummaryClient/EBPOT pedestal quality summary G12', 'description': 'Summary of the presample data quality. A channel is red if presample mean is off by 25.0 from 200.0 or RMS is greater than 3.0. RMS threshold is 6.0 in the forward region (|eta| > 2.1). Channels with entries less than 6 are not considered.'}],[{'path': 'EcalEndcap/EESummaryClient/EEPOT EE - pedestal quality summary G12', 'description': 'Summary of the presample data quality. A channel is red if presample mean is off by 25.0 from 200.0 or RMS is greater than 3.0. RMS threshold is 6.0 in the forward region (|eta| > 2.1). Channels with entries less than 6 are not considered.'}, {'path': 'EcalEndcap/EESummaryClient/EEPOT EE + pedestal quality summary G12', 'description': 'Summary of the presample data quality. A channel is red if presample mean is off by 25.0 from 200.0 or RMS is greater than 3.0. RMS threshold is 6.0 in the forward region (|eta| > 2.1). Channels with entries less than 6 are not considered.'}])
ecallayout(dqmitems, '00 Shift/Ecal/05 RecHit Energy',[{'path': 'EcalBarrel/EBSummaryClient/EBOT energy summary', 'description': '2D distribution of the mean rec hit energy.'}],[{'path': 'EcalEndcap/EESummaryClient/EEOT EE - energy summary', 'description': '2D distribution of the mean rec hit energy.'}, {'path': 'EcalEndcap/EESummaryClient/EEOT EE + energy summary', 'description': '2D distribution of the mean rec hit energy.'}])
ecallayout(dqmitems, '00 Shift/Ecal/06 Timing',[{'path': 'EcalBarrel/EBSummaryClient/EBTMT timing quality summary', 'description': 'Summary of the timing data quality. A 5x5 tower is red if the mean timing of the tower is off by more than 2.0 or RMS is greater than 6.0 (6.0 and 12.0 in forward region). Towers with total entries less than 3 (or 24 in forward region) are not subject to this evaluation. Since 5x5 tower timings are calculated with a tighter time-window than per-channel timings, a tower can additionally become red if its the sum of per-channel timing histogram entries is greater than per-tower histogram entries by factor 1.66666666667 (significant fraction of events fall outside the tight time-window).'}],[{'path': 'EcalEndcap/EESummaryClient/EETMT EE - timing quality summary', 'description': 'Summary of the timing data quality. A 5x5 tower is red if the mean timing of the tower is off by more than 2.0 or RMS is greater than 6.0 (6.0 and 12.0 in forward region). Towers with total entries less than 3 (or 24 in forward region) are not subject to this evaluation. Since 5x5 tower timings are calculated with a tighter time-window than per-channel timings, a tower can additionally become red if its the sum of per-channel timing histogram entries is greater than per-tower histogram entries by factor 1.66666666667 (significant fraction of events fall outside the tight time-window).'}, {'path': 'EcalEndcap/EESummaryClient/EETMT EE + timing quality summary', 'description': 'Summary of the timing data quality. A 5x5 tower is red if the mean timing of the tower is off by more than 2.0 or RMS is greater than 6.0 (6.0 and 12.0 in forward region). Towers with total entries less than 3 (or 24 in forward region) are not subject to this evaluation. Since 5x5 tower timings are calculated with a tighter time-window than per-channel timings, a tower can additionally become red if its the sum of per-channel timing histogram entries is greater than per-tower histogram entries by factor 1.66666666667 (significant fraction of events fall outside the tight time-window).'}])
ecallayout(dqmitems, '00 Shift/Ecal/07 TriggerPrimitives',[{'path': 'EcalBarrel/EBSummaryClient/EBTTT emulator error quality summary', 'description': 'Summary of emulator matching quality. A tower is red if the number of events with Et emulation error is greater than 0.1 of total events. Towers with entries less than 3 are not considered. Also, an entire SuperModule can show red if its (data) Trigger Primitive digi occupancy is less than 5sigma of the overall SuperModule mean, or if more than 80% of its Trigger Towers are showing any number of TT Flag-Readout Mismatch errors. Finally, if the fraction of towers in a SuperModule that are permanently masked or have TTF4 flag set is greater than 0.1, then the entire supermodule shows red.'}],[{'path': 'EcalEndcap/EESummaryClient/EETTT EE - emulator error quality summary', 'description': 'Summary of emulator matching quality. A tower is red if the number of events with Et emulation error is greater than 0.1 of total events. Towers with entries less than 3 are not considered. Also, an entire SuperModule can show red if its (data) Trigger Primitive digi occupancy is less than 5sigma of the overall SuperModule mean, or if more than 80% of its Trigger Towers are showing any number of TT Flag-Readout Mismatch errors. Finally, if the fraction of towers in a SuperModule that are permanently masked or have TTF4 flag set is greater than 0.1, then the entire supermodule shows red.'}, {'path': 'EcalEndcap/EESummaryClient/EETTT EE + emulator error quality summary', 'description': 'Summary of emulator matching quality. A tower is red if the number of events with Et emulation error is greater than 0.1 of total events. Towers with entries less than 3 are not considered. Also, an entire SuperModule can show red if its (data) Trigger Primitive digi occupancy is less than 5sigma of the overall SuperModule mean, or if more than 80% of its Trigger Towers are showing any number of TT Flag-Readout Mismatch errors. Finally, if the fraction of towers in a SuperModule that are permanently masked or have TTF4 flag set is greater than 0.1, then the entire supermodule shows red.'}])
ecallayout(dqmitems, '00 Shift/Ecal/08 Hot Cells',[{'path': 'EcalBarrel/EBSummaryClient/EBOT hot cell quality summary', 'description': 'Summary of the hot cell monitor. A channel is red if it has more than 100.0 times more entries than phi-ring mean in either digi, rec hit (filtered), or TP digi (filtered). Channels with less than 20 entries are not considered. Channel names of the hot cells are available in (Top) / Ecal / Errors / HotCells. Also, an entire SuperModule can show red if its (filtered) rechit occupancy is less than 5sigma of the overall SuperModule mean.'}],[{'path': 'EcalEndcap/EESummaryClient/EEOT EE - hot cell quality summary', 'description': 'Summary of the hot cell monitor. A channel is red if it has more than 100.0 times more entries than phi-ring mean in either digi, rec hit (filtered), or TP digi (filtered). Channels with less than 20 entries are not considered. Channel names of the hot cells are available in (Top) / Ecal / Errors / HotCells. Also, an entire SuperModule can show red if its (filtered) rechit occupancy is less than 5sigma of the overall SuperModule mean.'}, {'path': 'EcalEndcap/EESummaryClient/EEOT EE + hot cell quality summary', 'description': 'Summary of the hot cell monitor. A channel is red if it has more than 100.0 times more entries than phi-ring mean in either digi, rec hit (filtered), or TP digi (filtered). Channels with less than 20 entries are not considered. Channel names of the hot cells are available in (Top) / Ecal / Errors / HotCells. Also, an entire SuperModule can show red if its (filtered) rechit occupancy is less than 5sigma of the overall SuperModule mean.'}])
ecallayout(dqmitems, '00 Shift/Ecal/09 Laser 3 (Photonics)',[{'path': 'EcalBarrel/EBSummaryClient/EBLT laser quality summary L3', 'description': 'Summary of the laser data quality. A channel is red either if mean / expected < 0.1, or if mean / expected > 2.06, or if RMS / expected > 0.3, or if mean timing is off from expected by 0.5. Expected amplitudes and timings are 1700.0, 1300.0, 1700.0, 1700.0 and 4.2, 4.2, 4.2, 4.2 for lasers 1, 2, 3, and 4 respectively. Channels with less than 3 are not considered.'}],[{'path': 'EcalEndcap/EESummaryClient/EELT EE - laser quality summary L3', 'description': 'Summary of the laser data quality. A channel is red either if mean / expected < 0.1, or if mean / expected > 2.06, or if RMS / expected > 0.3, or if mean timing is off from expected by 0.5. Expected amplitudes and timings are 1700.0, 1300.0, 1700.0, 1700.0 and 4.2, 4.2, 4.2, 4.2 for lasers 1, 2, 3, and 4 respectively. Channels with less than 3 are not considered.'}, {'path': 'EcalEndcap/EESummaryClient/EELT EE + laser quality summary L3', 'description': 'Summary of the laser data quality. A channel is red either if mean / expected < 0.1, or if mean / expected > 2.06, or if RMS / expected > 0.3, or if mean timing is off from expected by 0.5. Expected amplitudes and timings are 1700.0, 1300.0, 1700.0, 1700.0 and 4.2, 4.2, 4.2, 4.2 for lasers 1, 2, 3, and 4 respectively. Channels with less than 3 are not considered.'}])
ecallayout(dqmitems, '00 Shift/Ecal/10 Laser 3 PN',[{'path': 'EcalBarrel/EBSummaryClient/EBLT PN laser quality summary L3', 'description': 'Summary of the laser data quality in the PN diodes. A channel is red if mean / expected < 0.1 or RMS / expected > 1.0. Expected amplitudes are 800.0, 800.0, 800.0, 800.0 for laser 1, 2, 3, and 4 respectively. Channels with less than 3 are not considered.'}],[{'path': 'EcalEndcap/EESummaryClient/EELT PN laser quality summary L3', 'description': 'Summary of the laser data quality in the PN diodes. A channel is red if mean / expected < 0.1 or RMS / expected > 1.0. Expected amplitudes are 800.0, 800.0, 800.0, 800.0 for laser 1, 2, 3, and 4 respectively. Channels with less than 3 are not considered.'}])
ecallayout(dqmitems, '00 Shift/Ecal/11 Test Pulse PN',[{'path': 'EcalBarrel/EBSummaryClient/EBTPT PN test pulse quality G16 summary', 'description': 'Summary of test pulse data quality for PN diodes. A channel is red if mean amplitude is lower than the threshold, or RMS is greater than threshold. The mean and RMS thresholds are 12.5, 200.0 and 20.0, 20.0 for gains 1 and 16 respectively. Channels with entries less than 3 are not considered.'}],[{'path': 'EcalEndcap/EESummaryClient/EETPT PN test pulse quality G16 summary', 'description': 'Summary of test pulse data quality for PN diodes. A channel is red if mean amplitude is lower than the threshold, or RMS is greater than threshold. The mean and RMS thresholds are 12.5, 200.0 and 20.0, 20.0 for gains 1 and 16 respectively. Channels with entries less than 3 are not considered.'}])
ecallayout(dqmitems, '00 Shift/Ecal/12 Led 1',[{'path': 'EcalEndcap/EESummaryClient/EELDT EE - led quality summary L1', 'description': 'Summary of the led data quality. A channel is red either if mean / expected < 0.1, or if RMS / expected > 0.5, or if mean timing is off from expected by 1.0. Expected amplitudes and timings are 200.0, 10.0 and 4.4, 4.5 for leds 1 and 2 respectively. Channels with less than 3 are not considered.'}, {'path': 'EcalEndcap/EESummaryClient/EELDT EE + led quality summary L1', 'description': 'Summary of the led data quality. A channel is red either if mean / expected < 0.1, or if RMS / expected > 0.5, or if mean timing is off from expected by 1.0. Expected amplitudes and timings are 200.0, 10.0 and 4.4, 4.5 for leds 1 and 2 respectively. Channels with less than 3 are not considered.'}])
ecallayout(dqmitems, '00 Shift/Ecal/13 Led 1 PN',[{'path': 'EcalEndcap/EESummaryClient/EELDT PN led quality summary L1', 'description': 'Summary of the led data quality in the PN diodes. A channel is red if mean / expected < 0.1 or RMS / expected > 1.0. Expected amplitudes are 800.0, 800.0 for led 1 and 2 respectively. Channels with less than 3 are not considered.'}])
ecallayout(dqmitems, '00 Shift/Ecal/14 TT Flag-Readout Mismatch',
	   [{'path': 'EcalBarrel/EBSelectiveReadoutTask/EBSRT TT flag mismatch', 'description': 'For events with medium- and high-interest TT flags, this plot maps the occupancy for towers with a mismatch in the number of readouts between the TPs and the Digis.'}],
	   [{'path': 'EcalEndcap/EESelectiveReadoutTask/EESRT TT flag mismatch EE -', 'description': 'For events with medium- and high-interest TT flags, this plot maps the occupancy for towers with a mismatch in the number of readouts between the TPs and the Digis.'},
	    {'path': 'EcalEndcap/EESelectiveReadoutTask/EESRT TT flag mismatch EE +', 'description': 'For events with medium- and high-interest TT flags, this plot maps the occupancy for towers with a mismatch in the number of readouts between the TPs and the Digis.'}])
