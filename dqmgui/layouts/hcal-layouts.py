#
#	HCAL DQM Layouts
#

if __name__=='__main__':
	class DQMItems:
		def __init__(self, layout):
			print layout
	dqmitems = {}

def hcallayout(i, p, *rows):
	i['Hcal/Layouts/' + p] = DQMItem(layout=rows)

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED1100', [{'path':'/DigiTask/Missing1LS/FED/FED1100', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED1102', [{'path':'/DigiTask/Missing1LS/FED/FED1102', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED1104', [{'path':'/DigiTask/Missing1LS/FED/FED1104', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED1106', [{'path':'/DigiTask/Missing1LS/FED/FED1106', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED1108', [{'path':'/DigiTask/Missing1LS/FED/FED1108', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED1110', [{'path':'/DigiTask/Missing1LS/FED/FED1110', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED1112', [{'path':'/DigiTask/Missing1LS/FED/FED1112', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED1114', [{'path':'/DigiTask/Missing1LS/FED/FED1114', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED1116', [{'path':'/DigiTask/Missing1LS/FED/FED1116', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED1118', [{'path':'/DigiTask/Missing1LS/FED/FED1118', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED1120', [{'path':'/DigiTask/Missing1LS/FED/FED1120', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED1122', [{'path':'/DigiTask/Missing1LS/FED/FED1122', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED1132', [{'path':'/DigiTask/Missing1LS/FED/FED1132', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED724', [{'path':'/DigiTask/Missing1LS/FED/FED724', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED725', [{'path':'/DigiTask/Missing1LS/FED/FED725', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED726', [{'path':'/DigiTask/Missing1LS/FED/FED726', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED727', [{'path':'/DigiTask/Missing1LS/FED/FED727', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED728', [{'path':'/DigiTask/Missing1LS/FED/FED728', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED729', [{'path':'/DigiTask/Missing1LS/FED/FED729', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED730', [{'path':'/DigiTask/Missing1LS/FED/FED730', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/DIGI/FED/FED731', [{'path':'/DigiTask/Missing1LS/FED/FED731', 'description':''}])

hcallayout(dqmitems, 'OccupancyEmul/TP/Electronics/VME', [{'path':'/TPTask/OccupancyEmul/Electronics/VME', 'description':''}])

hcallayout(dqmitems, 'OccupancyEmul/TP/Electronics/uTCA', [{'path':'/TPTask/OccupancyEmul/Electronics/uTCA', 'description':''}])

hcallayout(dqmitems, 'BcnMsm/RAW/Electronics/VME', [{'path':'/RawTask/BcnMsm/Electronics/VME', 'description':'DESC<a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription">Description</a>'}])

hcallayout(dqmitems, 'BcnMsm/RAW/Electronics/uTCA', [{'path':'/RawTask/BcnMsm/Electronics/uTCA', 'description':'DESC<a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription">Description</a>'}])

hcallayout(dqmitems, 'Timing/DIGI/Electronics/VME', [{'path':'/DigiTask/Timing/Electronics/VME', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/Electronics/uTCA', [{'path':'/DigiTask/Timing/Electronics/uTCA', 'description':''}])

hcallayout(dqmitems, 'EtEmul/TP/TTSubdet/HBHE', [{'path':'/TPTask/EtEmul/TTSubdet/HBHE', 'description':''}])

hcallayout(dqmitems, 'EtEmul/TP/TTSubdet/HF', [{'path':'/TPTask/EtEmul/TTSubdet/HF', 'description':''}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED1100', [{'path':'/DigiTask/OccupancyNRCut/FED/FED1100', 'description':''}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED1102', [{'path':'/DigiTask/OccupancyNRCut/FED/FED1102', 'description':''}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED1104', [{'path':'/DigiTask/OccupancyNRCut/FED/FED1104', 'description':''}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED1106', [{'path':'/DigiTask/OccupancyNRCut/FED/FED1106', 'description':''}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED1108', [{'path':'/DigiTask/OccupancyNRCut/FED/FED1108', 'description':''}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED1110', [{'path':'/DigiTask/OccupancyNRCut/FED/FED1110', 'description':''}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED1112', [{'path':'/DigiTask/OccupancyNRCut/FED/FED1112', 'description':''}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED1114', [{'path':'/DigiTask/OccupancyNRCut/FED/FED1114', 'description':''}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED1116', [{'path':'/DigiTask/OccupancyNRCut/FED/FED1116', 'description':''}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED1118', [{'path':'/DigiTask/OccupancyNRCut/FED/FED1118', 'description':''}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED1120', [{'path':'/DigiTask/OccupancyNRCut/FED/FED1120', 'description':''}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED1122', [{'path':'/DigiTask/OccupancyNRCut/FED/FED1122', 'description':''}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED1132', [{'path':'/DigiTask/OccupancyNRCut/FED/FED1132', 'description':''}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED724', [{'path':'/DigiTask/OccupancyNRCut/FED/FED724', 'description':''}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED725', [{'path':'/DigiTask/OccupancyNRCut/FED/FED725', 'description':''}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED726', [{'path':'/DigiTask/OccupancyNRCut/FED/FED726', 'description':''}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED727', [{'path':'/DigiTask/OccupancyNRCut/FED/FED727', 'description':''}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED728', [{'path':'/DigiTask/OccupancyNRCut/FED/FED728', 'description':''}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED729', [{'path':'/DigiTask/OccupancyNRCut/FED/FED729', 'description':''}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED730', [{'path':'/DigiTask/OccupancyNRCut/FED/FED730', 'description':''}])

hcallayout(dqmitems, 'OccupancyNRCut/DIGI/FED/FED731', [{'path':'/DigiTask/OccupancyNRCut/FED/FED731', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1100S1', [{'path':'/DigiTask/Shape/FEDSlot/FED1100S1', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1100S10', [{'path':'/DigiTask/Shape/FEDSlot/FED1100S10', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1100S11', [{'path':'/DigiTask/Shape/FEDSlot/FED1100S11', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1100S12', [{'path':'/DigiTask/Shape/FEDSlot/FED1100S12', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1100S2', [{'path':'/DigiTask/Shape/FEDSlot/FED1100S2', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1100S3', [{'path':'/DigiTask/Shape/FEDSlot/FED1100S3', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1100S4', [{'path':'/DigiTask/Shape/FEDSlot/FED1100S4', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1100S5', [{'path':'/DigiTask/Shape/FEDSlot/FED1100S5', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1100S6', [{'path':'/DigiTask/Shape/FEDSlot/FED1100S6', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1100S7', [{'path':'/DigiTask/Shape/FEDSlot/FED1100S7', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1100S8', [{'path':'/DigiTask/Shape/FEDSlot/FED1100S8', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1100S9', [{'path':'/DigiTask/Shape/FEDSlot/FED1100S9', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1102S1', [{'path':'/DigiTask/Shape/FEDSlot/FED1102S1', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1102S10', [{'path':'/DigiTask/Shape/FEDSlot/FED1102S10', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1102S11', [{'path':'/DigiTask/Shape/FEDSlot/FED1102S11', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1102S12', [{'path':'/DigiTask/Shape/FEDSlot/FED1102S12', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1102S2', [{'path':'/DigiTask/Shape/FEDSlot/FED1102S2', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1102S3', [{'path':'/DigiTask/Shape/FEDSlot/FED1102S3', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1102S4', [{'path':'/DigiTask/Shape/FEDSlot/FED1102S4', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1102S5', [{'path':'/DigiTask/Shape/FEDSlot/FED1102S5', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1102S6', [{'path':'/DigiTask/Shape/FEDSlot/FED1102S6', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1102S7', [{'path':'/DigiTask/Shape/FEDSlot/FED1102S7', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1102S8', [{'path':'/DigiTask/Shape/FEDSlot/FED1102S8', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1102S9', [{'path':'/DigiTask/Shape/FEDSlot/FED1102S9', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1104S1', [{'path':'/DigiTask/Shape/FEDSlot/FED1104S1', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1104S10', [{'path':'/DigiTask/Shape/FEDSlot/FED1104S10', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1104S11', [{'path':'/DigiTask/Shape/FEDSlot/FED1104S11', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1104S12', [{'path':'/DigiTask/Shape/FEDSlot/FED1104S12', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1104S2', [{'path':'/DigiTask/Shape/FEDSlot/FED1104S2', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1104S3', [{'path':'/DigiTask/Shape/FEDSlot/FED1104S3', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1104S4', [{'path':'/DigiTask/Shape/FEDSlot/FED1104S4', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1104S5', [{'path':'/DigiTask/Shape/FEDSlot/FED1104S5', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1104S6', [{'path':'/DigiTask/Shape/FEDSlot/FED1104S6', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1104S7', [{'path':'/DigiTask/Shape/FEDSlot/FED1104S7', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1104S8', [{'path':'/DigiTask/Shape/FEDSlot/FED1104S8', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1104S9', [{'path':'/DigiTask/Shape/FEDSlot/FED1104S9', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1106S1', [{'path':'/DigiTask/Shape/FEDSlot/FED1106S1', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1106S10', [{'path':'/DigiTask/Shape/FEDSlot/FED1106S10', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1106S11', [{'path':'/DigiTask/Shape/FEDSlot/FED1106S11', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1106S12', [{'path':'/DigiTask/Shape/FEDSlot/FED1106S12', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1106S2', [{'path':'/DigiTask/Shape/FEDSlot/FED1106S2', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1106S3', [{'path':'/DigiTask/Shape/FEDSlot/FED1106S3', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1106S4', [{'path':'/DigiTask/Shape/FEDSlot/FED1106S4', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1106S5', [{'path':'/DigiTask/Shape/FEDSlot/FED1106S5', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1106S6', [{'path':'/DigiTask/Shape/FEDSlot/FED1106S6', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1106S7', [{'path':'/DigiTask/Shape/FEDSlot/FED1106S7', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1106S8', [{'path':'/DigiTask/Shape/FEDSlot/FED1106S8', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1106S9', [{'path':'/DigiTask/Shape/FEDSlot/FED1106S9', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1108S1', [{'path':'/DigiTask/Shape/FEDSlot/FED1108S1', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1108S10', [{'path':'/DigiTask/Shape/FEDSlot/FED1108S10', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1108S11', [{'path':'/DigiTask/Shape/FEDSlot/FED1108S11', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1108S12', [{'path':'/DigiTask/Shape/FEDSlot/FED1108S12', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1108S2', [{'path':'/DigiTask/Shape/FEDSlot/FED1108S2', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1108S3', [{'path':'/DigiTask/Shape/FEDSlot/FED1108S3', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1108S4', [{'path':'/DigiTask/Shape/FEDSlot/FED1108S4', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1108S5', [{'path':'/DigiTask/Shape/FEDSlot/FED1108S5', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1108S6', [{'path':'/DigiTask/Shape/FEDSlot/FED1108S6', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1108S7', [{'path':'/DigiTask/Shape/FEDSlot/FED1108S7', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1108S8', [{'path':'/DigiTask/Shape/FEDSlot/FED1108S8', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1108S9', [{'path':'/DigiTask/Shape/FEDSlot/FED1108S9', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1110S1', [{'path':'/DigiTask/Shape/FEDSlot/FED1110S1', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1110S10', [{'path':'/DigiTask/Shape/FEDSlot/FED1110S10', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1110S11', [{'path':'/DigiTask/Shape/FEDSlot/FED1110S11', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1110S12', [{'path':'/DigiTask/Shape/FEDSlot/FED1110S12', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1110S2', [{'path':'/DigiTask/Shape/FEDSlot/FED1110S2', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1110S3', [{'path':'/DigiTask/Shape/FEDSlot/FED1110S3', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1110S4', [{'path':'/DigiTask/Shape/FEDSlot/FED1110S4', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1110S5', [{'path':'/DigiTask/Shape/FEDSlot/FED1110S5', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1110S6', [{'path':'/DigiTask/Shape/FEDSlot/FED1110S6', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1110S7', [{'path':'/DigiTask/Shape/FEDSlot/FED1110S7', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1110S8', [{'path':'/DigiTask/Shape/FEDSlot/FED1110S8', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1110S9', [{'path':'/DigiTask/Shape/FEDSlot/FED1110S9', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1112S1', [{'path':'/DigiTask/Shape/FEDSlot/FED1112S1', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1112S10', [{'path':'/DigiTask/Shape/FEDSlot/FED1112S10', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1112S11', [{'path':'/DigiTask/Shape/FEDSlot/FED1112S11', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1112S12', [{'path':'/DigiTask/Shape/FEDSlot/FED1112S12', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1112S2', [{'path':'/DigiTask/Shape/FEDSlot/FED1112S2', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1112S3', [{'path':'/DigiTask/Shape/FEDSlot/FED1112S3', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1112S4', [{'path':'/DigiTask/Shape/FEDSlot/FED1112S4', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1112S5', [{'path':'/DigiTask/Shape/FEDSlot/FED1112S5', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1112S6', [{'path':'/DigiTask/Shape/FEDSlot/FED1112S6', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1112S7', [{'path':'/DigiTask/Shape/FEDSlot/FED1112S7', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1112S8', [{'path':'/DigiTask/Shape/FEDSlot/FED1112S8', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1112S9', [{'path':'/DigiTask/Shape/FEDSlot/FED1112S9', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1114S1', [{'path':'/DigiTask/Shape/FEDSlot/FED1114S1', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1114S10', [{'path':'/DigiTask/Shape/FEDSlot/FED1114S10', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1114S11', [{'path':'/DigiTask/Shape/FEDSlot/FED1114S11', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1114S12', [{'path':'/DigiTask/Shape/FEDSlot/FED1114S12', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1114S2', [{'path':'/DigiTask/Shape/FEDSlot/FED1114S2', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1114S3', [{'path':'/DigiTask/Shape/FEDSlot/FED1114S3', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1114S4', [{'path':'/DigiTask/Shape/FEDSlot/FED1114S4', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1114S5', [{'path':'/DigiTask/Shape/FEDSlot/FED1114S5', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1114S6', [{'path':'/DigiTask/Shape/FEDSlot/FED1114S6', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1114S7', [{'path':'/DigiTask/Shape/FEDSlot/FED1114S7', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1114S8', [{'path':'/DigiTask/Shape/FEDSlot/FED1114S8', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1114S9', [{'path':'/DigiTask/Shape/FEDSlot/FED1114S9', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1116S1', [{'path':'/DigiTask/Shape/FEDSlot/FED1116S1', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1116S10', [{'path':'/DigiTask/Shape/FEDSlot/FED1116S10', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1116S11', [{'path':'/DigiTask/Shape/FEDSlot/FED1116S11', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1116S12', [{'path':'/DigiTask/Shape/FEDSlot/FED1116S12', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1116S2', [{'path':'/DigiTask/Shape/FEDSlot/FED1116S2', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1116S3', [{'path':'/DigiTask/Shape/FEDSlot/FED1116S3', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1116S4', [{'path':'/DigiTask/Shape/FEDSlot/FED1116S4', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1116S5', [{'path':'/DigiTask/Shape/FEDSlot/FED1116S5', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1116S6', [{'path':'/DigiTask/Shape/FEDSlot/FED1116S6', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1116S7', [{'path':'/DigiTask/Shape/FEDSlot/FED1116S7', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1116S8', [{'path':'/DigiTask/Shape/FEDSlot/FED1116S8', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1116S9', [{'path':'/DigiTask/Shape/FEDSlot/FED1116S9', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1118S1', [{'path':'/DigiTask/Shape/FEDSlot/FED1118S1', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1118S10', [{'path':'/DigiTask/Shape/FEDSlot/FED1118S10', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1118S11', [{'path':'/DigiTask/Shape/FEDSlot/FED1118S11', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1118S12', [{'path':'/DigiTask/Shape/FEDSlot/FED1118S12', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1118S2', [{'path':'/DigiTask/Shape/FEDSlot/FED1118S2', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1118S3', [{'path':'/DigiTask/Shape/FEDSlot/FED1118S3', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1118S4', [{'path':'/DigiTask/Shape/FEDSlot/FED1118S4', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1118S5', [{'path':'/DigiTask/Shape/FEDSlot/FED1118S5', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1118S6', [{'path':'/DigiTask/Shape/FEDSlot/FED1118S6', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1118S7', [{'path':'/DigiTask/Shape/FEDSlot/FED1118S7', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1118S8', [{'path':'/DigiTask/Shape/FEDSlot/FED1118S8', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1118S9', [{'path':'/DigiTask/Shape/FEDSlot/FED1118S9', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1120S1', [{'path':'/DigiTask/Shape/FEDSlot/FED1120S1', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1120S10', [{'path':'/DigiTask/Shape/FEDSlot/FED1120S10', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1120S11', [{'path':'/DigiTask/Shape/FEDSlot/FED1120S11', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1120S12', [{'path':'/DigiTask/Shape/FEDSlot/FED1120S12', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1120S2', [{'path':'/DigiTask/Shape/FEDSlot/FED1120S2', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1120S3', [{'path':'/DigiTask/Shape/FEDSlot/FED1120S3', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1120S4', [{'path':'/DigiTask/Shape/FEDSlot/FED1120S4', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1120S5', [{'path':'/DigiTask/Shape/FEDSlot/FED1120S5', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1120S6', [{'path':'/DigiTask/Shape/FEDSlot/FED1120S6', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1120S7', [{'path':'/DigiTask/Shape/FEDSlot/FED1120S7', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1120S8', [{'path':'/DigiTask/Shape/FEDSlot/FED1120S8', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1120S9', [{'path':'/DigiTask/Shape/FEDSlot/FED1120S9', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1122S1', [{'path':'/DigiTask/Shape/FEDSlot/FED1122S1', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1122S10', [{'path':'/DigiTask/Shape/FEDSlot/FED1122S10', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1122S11', [{'path':'/DigiTask/Shape/FEDSlot/FED1122S11', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1122S12', [{'path':'/DigiTask/Shape/FEDSlot/FED1122S12', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1122S2', [{'path':'/DigiTask/Shape/FEDSlot/FED1122S2', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1122S3', [{'path':'/DigiTask/Shape/FEDSlot/FED1122S3', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1122S4', [{'path':'/DigiTask/Shape/FEDSlot/FED1122S4', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1122S5', [{'path':'/DigiTask/Shape/FEDSlot/FED1122S5', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1122S6', [{'path':'/DigiTask/Shape/FEDSlot/FED1122S6', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1122S7', [{'path':'/DigiTask/Shape/FEDSlot/FED1122S7', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1122S8', [{'path':'/DigiTask/Shape/FEDSlot/FED1122S8', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1122S9', [{'path':'/DigiTask/Shape/FEDSlot/FED1122S9', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED1132S12', [{'path':'/DigiTask/Shape/FEDSlot/FED1132S12', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED724S0', [{'path':'/DigiTask/Shape/FEDSlot/FED724S0', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED724S1', [{'path':'/DigiTask/Shape/FEDSlot/FED724S1', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED724S10', [{'path':'/DigiTask/Shape/FEDSlot/FED724S10', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED724S11', [{'path':'/DigiTask/Shape/FEDSlot/FED724S11', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED724S2', [{'path':'/DigiTask/Shape/FEDSlot/FED724S2', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED724S3', [{'path':'/DigiTask/Shape/FEDSlot/FED724S3', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED724S4', [{'path':'/DigiTask/Shape/FEDSlot/FED724S4', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED724S5', [{'path':'/DigiTask/Shape/FEDSlot/FED724S5', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED724S6', [{'path':'/DigiTask/Shape/FEDSlot/FED724S6', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED724S7', [{'path':'/DigiTask/Shape/FEDSlot/FED724S7', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED724S8', [{'path':'/DigiTask/Shape/FEDSlot/FED724S8', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED724S9', [{'path':'/DigiTask/Shape/FEDSlot/FED724S9', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED725S0', [{'path':'/DigiTask/Shape/FEDSlot/FED725S0', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED725S1', [{'path':'/DigiTask/Shape/FEDSlot/FED725S1', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED725S10', [{'path':'/DigiTask/Shape/FEDSlot/FED725S10', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED725S11', [{'path':'/DigiTask/Shape/FEDSlot/FED725S11', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED725S2', [{'path':'/DigiTask/Shape/FEDSlot/FED725S2', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED725S3', [{'path':'/DigiTask/Shape/FEDSlot/FED725S3', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED725S4', [{'path':'/DigiTask/Shape/FEDSlot/FED725S4', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED725S5', [{'path':'/DigiTask/Shape/FEDSlot/FED725S5', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED725S6', [{'path':'/DigiTask/Shape/FEDSlot/FED725S6', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED725S7', [{'path':'/DigiTask/Shape/FEDSlot/FED725S7', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED725S8', [{'path':'/DigiTask/Shape/FEDSlot/FED725S8', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED725S9', [{'path':'/DigiTask/Shape/FEDSlot/FED725S9', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED726S0', [{'path':'/DigiTask/Shape/FEDSlot/FED726S0', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED726S1', [{'path':'/DigiTask/Shape/FEDSlot/FED726S1', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED726S10', [{'path':'/DigiTask/Shape/FEDSlot/FED726S10', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED726S11', [{'path':'/DigiTask/Shape/FEDSlot/FED726S11', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED726S12', [{'path':'/DigiTask/Shape/FEDSlot/FED726S12', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED726S13', [{'path':'/DigiTask/Shape/FEDSlot/FED726S13', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED726S2', [{'path':'/DigiTask/Shape/FEDSlot/FED726S2', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED726S3', [{'path':'/DigiTask/Shape/FEDSlot/FED726S3', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED726S4', [{'path':'/DigiTask/Shape/FEDSlot/FED726S4', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED726S5', [{'path':'/DigiTask/Shape/FEDSlot/FED726S5', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED726S6', [{'path':'/DigiTask/Shape/FEDSlot/FED726S6', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED726S7', [{'path':'/DigiTask/Shape/FEDSlot/FED726S7', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED726S8', [{'path':'/DigiTask/Shape/FEDSlot/FED726S8', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED726S9', [{'path':'/DigiTask/Shape/FEDSlot/FED726S9', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED727S0', [{'path':'/DigiTask/Shape/FEDSlot/FED727S0', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED727S1', [{'path':'/DigiTask/Shape/FEDSlot/FED727S1', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED727S10', [{'path':'/DigiTask/Shape/FEDSlot/FED727S10', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED727S11', [{'path':'/DigiTask/Shape/FEDSlot/FED727S11', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED727S12', [{'path':'/DigiTask/Shape/FEDSlot/FED727S12', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED727S13', [{'path':'/DigiTask/Shape/FEDSlot/FED727S13', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED727S2', [{'path':'/DigiTask/Shape/FEDSlot/FED727S2', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED727S3', [{'path':'/DigiTask/Shape/FEDSlot/FED727S3', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED727S4', [{'path':'/DigiTask/Shape/FEDSlot/FED727S4', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED727S5', [{'path':'/DigiTask/Shape/FEDSlot/FED727S5', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED727S6', [{'path':'/DigiTask/Shape/FEDSlot/FED727S6', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED727S7', [{'path':'/DigiTask/Shape/FEDSlot/FED727S7', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED727S8', [{'path':'/DigiTask/Shape/FEDSlot/FED727S8', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED727S9', [{'path':'/DigiTask/Shape/FEDSlot/FED727S9', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED728S0', [{'path':'/DigiTask/Shape/FEDSlot/FED728S0', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED728S1', [{'path':'/DigiTask/Shape/FEDSlot/FED728S1', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED728S10', [{'path':'/DigiTask/Shape/FEDSlot/FED728S10', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED728S11', [{'path':'/DigiTask/Shape/FEDSlot/FED728S11', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED728S12', [{'path':'/DigiTask/Shape/FEDSlot/FED728S12', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED728S13', [{'path':'/DigiTask/Shape/FEDSlot/FED728S13', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED728S2', [{'path':'/DigiTask/Shape/FEDSlot/FED728S2', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED728S3', [{'path':'/DigiTask/Shape/FEDSlot/FED728S3', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED728S4', [{'path':'/DigiTask/Shape/FEDSlot/FED728S4', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED728S5', [{'path':'/DigiTask/Shape/FEDSlot/FED728S5', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED728S6', [{'path':'/DigiTask/Shape/FEDSlot/FED728S6', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED728S7', [{'path':'/DigiTask/Shape/FEDSlot/FED728S7', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED728S8', [{'path':'/DigiTask/Shape/FEDSlot/FED728S8', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED728S9', [{'path':'/DigiTask/Shape/FEDSlot/FED728S9', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED729S0', [{'path':'/DigiTask/Shape/FEDSlot/FED729S0', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED729S1', [{'path':'/DigiTask/Shape/FEDSlot/FED729S1', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED729S10', [{'path':'/DigiTask/Shape/FEDSlot/FED729S10', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED729S11', [{'path':'/DigiTask/Shape/FEDSlot/FED729S11', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED729S12', [{'path':'/DigiTask/Shape/FEDSlot/FED729S12', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED729S13', [{'path':'/DigiTask/Shape/FEDSlot/FED729S13', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED729S2', [{'path':'/DigiTask/Shape/FEDSlot/FED729S2', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED729S3', [{'path':'/DigiTask/Shape/FEDSlot/FED729S3', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED729S4', [{'path':'/DigiTask/Shape/FEDSlot/FED729S4', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED729S5', [{'path':'/DigiTask/Shape/FEDSlot/FED729S5', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED729S6', [{'path':'/DigiTask/Shape/FEDSlot/FED729S6', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED729S7', [{'path':'/DigiTask/Shape/FEDSlot/FED729S7', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED729S8', [{'path':'/DigiTask/Shape/FEDSlot/FED729S8', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED729S9', [{'path':'/DigiTask/Shape/FEDSlot/FED729S9', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED730S0', [{'path':'/DigiTask/Shape/FEDSlot/FED730S0', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED730S1', [{'path':'/DigiTask/Shape/FEDSlot/FED730S1', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED730S10', [{'path':'/DigiTask/Shape/FEDSlot/FED730S10', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED730S11', [{'path':'/DigiTask/Shape/FEDSlot/FED730S11', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED730S12', [{'path':'/DigiTask/Shape/FEDSlot/FED730S12', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED730S13', [{'path':'/DigiTask/Shape/FEDSlot/FED730S13', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED730S2', [{'path':'/DigiTask/Shape/FEDSlot/FED730S2', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED730S3', [{'path':'/DigiTask/Shape/FEDSlot/FED730S3', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED730S4', [{'path':'/DigiTask/Shape/FEDSlot/FED730S4', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED730S5', [{'path':'/DigiTask/Shape/FEDSlot/FED730S5', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED730S6', [{'path':'/DigiTask/Shape/FEDSlot/FED730S6', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED730S7', [{'path':'/DigiTask/Shape/FEDSlot/FED730S7', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED730S8', [{'path':'/DigiTask/Shape/FEDSlot/FED730S8', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED730S9', [{'path':'/DigiTask/Shape/FEDSlot/FED730S9', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED731S0', [{'path':'/DigiTask/Shape/FEDSlot/FED731S0', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED731S1', [{'path':'/DigiTask/Shape/FEDSlot/FED731S1', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED731S10', [{'path':'/DigiTask/Shape/FEDSlot/FED731S10', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED731S11', [{'path':'/DigiTask/Shape/FEDSlot/FED731S11', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED731S2', [{'path':'/DigiTask/Shape/FEDSlot/FED731S2', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED731S3', [{'path':'/DigiTask/Shape/FEDSlot/FED731S3', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED731S4', [{'path':'/DigiTask/Shape/FEDSlot/FED731S4', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED731S5', [{'path':'/DigiTask/Shape/FEDSlot/FED731S5', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED731S6', [{'path':'/DigiTask/Shape/FEDSlot/FED731S6', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED731S7', [{'path':'/DigiTask/Shape/FEDSlot/FED731S7', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED731S8', [{'path':'/DigiTask/Shape/FEDSlot/FED731S8', 'description':''}])

hcallayout(dqmitems, 'Shape/DIGI/FEDSlot/FED731S9', [{'path':'/DigiTask/Shape/FEDSlot/FED731S9', 'description':''}])

hcallayout(dqmitems, 'Summary/TP', [{'path':'/TPTask/Summary/Summary', 'description':''}])

hcallayout(dqmitems, 'BadQualityvsBX/RAW', [{'path':'/RawTask/BadQualityvsBX/BadQualityvsBX', 'description':'DESCDESC'}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FEDSlot/FED1118S1', [{'path':'/DigiTask/Q2Q12vsLS/FEDSlot/FED1118S1', 'description':''}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FEDSlot/FED1118S10', [{'path':'/DigiTask/Q2Q12vsLS/FEDSlot/FED1118S10', 'description':''}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FEDSlot/FED1118S11', [{'path':'/DigiTask/Q2Q12vsLS/FEDSlot/FED1118S11', 'description':''}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FEDSlot/FED1118S12', [{'path':'/DigiTask/Q2Q12vsLS/FEDSlot/FED1118S12', 'description':''}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FEDSlot/FED1118S2', [{'path':'/DigiTask/Q2Q12vsLS/FEDSlot/FED1118S2', 'description':''}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FEDSlot/FED1118S3', [{'path':'/DigiTask/Q2Q12vsLS/FEDSlot/FED1118S3', 'description':''}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FEDSlot/FED1118S4', [{'path':'/DigiTask/Q2Q12vsLS/FEDSlot/FED1118S4', 'description':''}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FEDSlot/FED1118S5', [{'path':'/DigiTask/Q2Q12vsLS/FEDSlot/FED1118S5', 'description':''}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FEDSlot/FED1118S6', [{'path':'/DigiTask/Q2Q12vsLS/FEDSlot/FED1118S6', 'description':''}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FEDSlot/FED1118S7', [{'path':'/DigiTask/Q2Q12vsLS/FEDSlot/FED1118S7', 'description':''}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FEDSlot/FED1118S8', [{'path':'/DigiTask/Q2Q12vsLS/FEDSlot/FED1118S8', 'description':''}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FEDSlot/FED1118S9', [{'path':'/DigiTask/Q2Q12vsLS/FEDSlot/FED1118S9', 'description':''}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FEDSlot/FED1120S1', [{'path':'/DigiTask/Q2Q12vsLS/FEDSlot/FED1120S1', 'description':''}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FEDSlot/FED1120S10', [{'path':'/DigiTask/Q2Q12vsLS/FEDSlot/FED1120S10', 'description':''}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FEDSlot/FED1120S11', [{'path':'/DigiTask/Q2Q12vsLS/FEDSlot/FED1120S11', 'description':''}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FEDSlot/FED1120S12', [{'path':'/DigiTask/Q2Q12vsLS/FEDSlot/FED1120S12', 'description':''}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FEDSlot/FED1120S2', [{'path':'/DigiTask/Q2Q12vsLS/FEDSlot/FED1120S2', 'description':''}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FEDSlot/FED1120S3', [{'path':'/DigiTask/Q2Q12vsLS/FEDSlot/FED1120S3', 'description':''}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FEDSlot/FED1120S4', [{'path':'/DigiTask/Q2Q12vsLS/FEDSlot/FED1120S4', 'description':''}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FEDSlot/FED1120S5', [{'path':'/DigiTask/Q2Q12vsLS/FEDSlot/FED1120S5', 'description':''}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FEDSlot/FED1120S6', [{'path':'/DigiTask/Q2Q12vsLS/FEDSlot/FED1120S6', 'description':''}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FEDSlot/FED1120S7', [{'path':'/DigiTask/Q2Q12vsLS/FEDSlot/FED1120S7', 'description':''}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FEDSlot/FED1120S8', [{'path':'/DigiTask/Q2Q12vsLS/FEDSlot/FED1120S8', 'description':''}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FEDSlot/FED1120S9', [{'path':'/DigiTask/Q2Q12vsLS/FEDSlot/FED1120S9', 'description':''}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FEDSlot/FED1122S1', [{'path':'/DigiTask/Q2Q12vsLS/FEDSlot/FED1122S1', 'description':''}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FEDSlot/FED1122S10', [{'path':'/DigiTask/Q2Q12vsLS/FEDSlot/FED1122S10', 'description':''}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FEDSlot/FED1122S11', [{'path':'/DigiTask/Q2Q12vsLS/FEDSlot/FED1122S11', 'description':''}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FEDSlot/FED1122S12', [{'path':'/DigiTask/Q2Q12vsLS/FEDSlot/FED1122S12', 'description':''}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FEDSlot/FED1122S2', [{'path':'/DigiTask/Q2Q12vsLS/FEDSlot/FED1122S2', 'description':''}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FEDSlot/FED1122S3', [{'path':'/DigiTask/Q2Q12vsLS/FEDSlot/FED1122S3', 'description':''}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FEDSlot/FED1122S4', [{'path':'/DigiTask/Q2Q12vsLS/FEDSlot/FED1122S4', 'description':''}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FEDSlot/FED1122S5', [{'path':'/DigiTask/Q2Q12vsLS/FEDSlot/FED1122S5', 'description':''}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FEDSlot/FED1122S6', [{'path':'/DigiTask/Q2Q12vsLS/FEDSlot/FED1122S6', 'description':''}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FEDSlot/FED1122S7', [{'path':'/DigiTask/Q2Q12vsLS/FEDSlot/FED1122S7', 'description':''}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FEDSlot/FED1122S8', [{'path':'/DigiTask/Q2Q12vsLS/FEDSlot/FED1122S8', 'description':''}])

hcallayout(dqmitems, 'Q2Q12vsLS/DIGI/FEDSlot/FED1122S9', [{'path':'/DigiTask/Q2Q12vsLS/FEDSlot/FED1122S9', 'description':''}])

hcallayout(dqmitems, 'EtEmul/TP/Electronics/VME', [{'path':'/TPTask/EtEmul/Electronics/VME', 'description':''}])

hcallayout(dqmitems, 'EtEmul/TP/Electronics/uTCA', [{'path':'/TPTask/EtEmul/Electronics/uTCA', 'description':''}])

hcallayout(dqmitems, 'SumQ/DIGI/SubdetPM/HBM', [{'path':'/DigiTask/SumQ/SubdetPM/HBM', 'description':''}])

hcallayout(dqmitems, 'SumQ/DIGI/SubdetPM/HBP', [{'path':'/DigiTask/SumQ/SubdetPM/HBP', 'description':''}])

hcallayout(dqmitems, 'SumQ/DIGI/SubdetPM/HEM', [{'path':'/DigiTask/SumQ/SubdetPM/HEM', 'description':''}])

hcallayout(dqmitems, 'SumQ/DIGI/SubdetPM/HEP', [{'path':'/DigiTask/SumQ/SubdetPM/HEP', 'description':''}])

hcallayout(dqmitems, 'SumQ/DIGI/SubdetPM/HFM', [{'path':'/DigiTask/SumQ/SubdetPM/HFM', 'description':''}])

hcallayout(dqmitems, 'SumQ/DIGI/SubdetPM/HFP', [{'path':'/DigiTask/SumQ/SubdetPM/HFP', 'description':''}])

hcallayout(dqmitems, 'SumQ/DIGI/SubdetPM/HOM', [{'path':'/DigiTask/SumQ/SubdetPM/HOM', 'description':''}])

hcallayout(dqmitems, 'SumQ/DIGI/SubdetPM/HOP', [{'path':'/DigiTask/SumQ/SubdetPM/HOP', 'description':''}])

hcallayout(dqmitems, 'EtData/TP/TTSubdet/HBHE', [{'path':'/TPTask/EtData/TTSubdet/HBHE', 'description':''}])

hcallayout(dqmitems, 'EtData/TP/TTSubdet/HF', [{'path':'/TPTask/EtData/TTSubdet/HF', 'description':''}])

hcallayout(dqmitems, 'Summary/RAW', [{'path':'/RawTask/Summary/Summary', 'description':''}])

hcallayout(dqmitems, 'OccupancyvsLS/DIGI/Subdet/HB', [{'path':'/DigiTask/OccupancyvsLS/Subdet/HB', 'description':''}])

hcallayout(dqmitems, 'OccupancyvsLS/DIGI/Subdet/HE', [{'path':'/DigiTask/OccupancyvsLS/Subdet/HE', 'description':''}])

hcallayout(dqmitems, 'OccupancyvsLS/DIGI/Subdet/HF', [{'path':'/DigiTask/OccupancyvsLS/Subdet/HF', 'description':''}])

hcallayout(dqmitems, 'OccupancyvsLS/DIGI/Subdet/HO', [{'path':'/DigiTask/OccupancyvsLS/Subdet/HO', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED1100', [{'path':'/RecHitTask/Missing1LS/FED/FED1100', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED1102', [{'path':'/RecHitTask/Missing1LS/FED/FED1102', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED1104', [{'path':'/RecHitTask/Missing1LS/FED/FED1104', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED1106', [{'path':'/RecHitTask/Missing1LS/FED/FED1106', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED1108', [{'path':'/RecHitTask/Missing1LS/FED/FED1108', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED1110', [{'path':'/RecHitTask/Missing1LS/FED/FED1110', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED1112', [{'path':'/RecHitTask/Missing1LS/FED/FED1112', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED1114', [{'path':'/RecHitTask/Missing1LS/FED/FED1114', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED1116', [{'path':'/RecHitTask/Missing1LS/FED/FED1116', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED1118', [{'path':'/RecHitTask/Missing1LS/FED/FED1118', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED1120', [{'path':'/RecHitTask/Missing1LS/FED/FED1120', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED1122', [{'path':'/RecHitTask/Missing1LS/FED/FED1122', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED1132', [{'path':'/RecHitTask/Missing1LS/FED/FED1132', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED724', [{'path':'/RecHitTask/Missing1LS/FED/FED724', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED725', [{'path':'/RecHitTask/Missing1LS/FED/FED725', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED726', [{'path':'/RecHitTask/Missing1LS/FED/FED726', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED727', [{'path':'/RecHitTask/Missing1LS/FED/FED727', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED728', [{'path':'/RecHitTask/Missing1LS/FED/FED728', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED729', [{'path':'/RecHitTask/Missing1LS/FED/FED729', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED730', [{'path':'/RecHitTask/Missing1LS/FED/FED730', 'description':''}])

hcallayout(dqmitems, 'Missing1LS/RECO/FED/FED731', [{'path':'/RecHitTask/Missing1LS/FED/FED731', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/Subdet/HB', [{'path':'/RecHitTask/TimingCut/Subdet/HB', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/Subdet/HE', [{'path':'/RecHitTask/TimingCut/Subdet/HE', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/Subdet/HF', [{'path':'/RecHitTask/TimingCut/Subdet/HF', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/Subdet/HO', [{'path':'/RecHitTask/TimingCut/Subdet/HO', 'description':''}])

hcallayout(dqmitems, 'FGMsm/TP/Electronics/VME', [{'path':'/TPTask/FGMsm/Electronics/VME', 'description':''}])

hcallayout(dqmitems, 'FGMsm/TP/Electronics/uTCA', [{'path':'/TPTask/FGMsm/Electronics/uTCA', 'description':''}])

hcallayout(dqmitems, 'EtCorrRatio/TP', [{'path':'/TPTask/EtCorrRatio/EtCorrRatio', 'description':''}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED1100', [{'path':'/RecHitTask/Occupancy/FED/FED1100', 'description':''}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED1102', [{'path':'/RecHitTask/Occupancy/FED/FED1102', 'description':''}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED1104', [{'path':'/RecHitTask/Occupancy/FED/FED1104', 'description':''}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED1106', [{'path':'/RecHitTask/Occupancy/FED/FED1106', 'description':''}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED1108', [{'path':'/RecHitTask/Occupancy/FED/FED1108', 'description':''}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED1110', [{'path':'/RecHitTask/Occupancy/FED/FED1110', 'description':''}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED1112', [{'path':'/RecHitTask/Occupancy/FED/FED1112', 'description':''}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED1114', [{'path':'/RecHitTask/Occupancy/FED/FED1114', 'description':''}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED1116', [{'path':'/RecHitTask/Occupancy/FED/FED1116', 'description':''}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED1118', [{'path':'/RecHitTask/Occupancy/FED/FED1118', 'description':''}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED1120', [{'path':'/RecHitTask/Occupancy/FED/FED1120', 'description':''}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED1122', [{'path':'/RecHitTask/Occupancy/FED/FED1122', 'description':''}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED1132', [{'path':'/RecHitTask/Occupancy/FED/FED1132', 'description':''}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED724', [{'path':'/RecHitTask/Occupancy/FED/FED724', 'description':''}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED725', [{'path':'/RecHitTask/Occupancy/FED/FED725', 'description':''}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED726', [{'path':'/RecHitTask/Occupancy/FED/FED726', 'description':''}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED727', [{'path':'/RecHitTask/Occupancy/FED/FED727', 'description':''}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED728', [{'path':'/RecHitTask/Occupancy/FED/FED728', 'description':''}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED729', [{'path':'/RecHitTask/Occupancy/FED/FED729', 'description':''}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED730', [{'path':'/RecHitTask/Occupancy/FED/FED730', 'description':''}])

hcallayout(dqmitems, 'Occupancy/RECO/FED/FED731', [{'path':'/RecHitTask/Occupancy/FED/FED731', 'description':''}])

hcallayout(dqmitems, 'EtMsm/TP/Electronics/VME', [{'path':'/TPTask/EtMsm/Electronics/VME', 'description':''}])

hcallayout(dqmitems, 'EtMsm/TP/Electronics/uTCA', [{'path':'/TPTask/EtMsm/Electronics/uTCA', 'description':''}])

hcallayout(dqmitems, 'OccupancyCutData/TP', [{'path':'/TPTask/OccupancyCutData/OccupancyCutData', 'description':''}])

hcallayout(dqmitems, 'Summary/RECO', [{'path':'/RecHitTask/Summary/Summary', 'description':''}])

hcallayout(dqmitems, 'Energy/RECO/Electronics/VME', [{'path':'/RecHitTask/Energy/Electronics/VME', 'description':''}])

hcallayout(dqmitems, 'Energy/RECO/Electronics/uTCA', [{'path':'/RecHitTask/Energy/Electronics/uTCA', 'description':''}])

hcallayout(dqmitems, 'OccupancyEmul/TP', [{'path':'/TPTask/OccupancyEmul/OccupancyEmul', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/RECO/Electronics/VME', [{'path':'/RecHitTask/OccupancyCut/Electronics/VME', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/RECO/Electronics/uTCA', [{'path':'/RecHitTask/OccupancyCut/Electronics/uTCA', 'description':''}])

hcallayout(dqmitems, 'OccupancyCutvsLS/RECO/Subdet/HB', [{'path':'/RecHitTask/OccupancyCutvsLS/Subdet/HB', 'description':''}])

hcallayout(dqmitems, 'OccupancyCutvsLS/RECO/Subdet/HE', [{'path':'/RecHitTask/OccupancyCutvsLS/Subdet/HE', 'description':''}])

hcallayout(dqmitems, 'OccupancyCutvsLS/RECO/Subdet/HF', [{'path':'/RecHitTask/OccupancyCutvsLS/Subdet/HF', 'description':''}])

hcallayout(dqmitems, 'OccupancyCutvsLS/RECO/Subdet/HO', [{'path':'/RecHitTask/OccupancyCutvsLS/Subdet/HO', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1100S1', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1100S1', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1100S10', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1100S10', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1100S11', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1100S11', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1100S12', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1100S12', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1100S2', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1100S2', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1100S3', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1100S3', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1100S4', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1100S4', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1100S5', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1100S5', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1100S6', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1100S6', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1100S7', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1100S7', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1100S8', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1100S8', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1100S9', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1100S9', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1102S1', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1102S1', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1102S10', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1102S10', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1102S11', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1102S11', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1102S12', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1102S12', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1102S2', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1102S2', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1102S3', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1102S3', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1102S4', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1102S4', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1102S5', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1102S5', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1102S6', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1102S6', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1102S7', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1102S7', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1102S8', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1102S8', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1102S9', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1102S9', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1104S1', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1104S1', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1104S10', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1104S10', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1104S11', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1104S11', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1104S12', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1104S12', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1104S2', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1104S2', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1104S3', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1104S3', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1104S4', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1104S4', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1104S5', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1104S5', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1104S6', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1104S6', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1104S7', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1104S7', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1104S8', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1104S8', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1104S9', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1104S9', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1106S1', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1106S1', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1106S10', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1106S10', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1106S11', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1106S11', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1106S12', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1106S12', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1106S2', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1106S2', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1106S3', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1106S3', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1106S4', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1106S4', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1106S5', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1106S5', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1106S6', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1106S6', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1106S7', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1106S7', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1106S8', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1106S8', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1106S9', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1106S9', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1108S1', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1108S1', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1108S10', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1108S10', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1108S11', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1108S11', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1108S12', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1108S12', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1108S2', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1108S2', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1108S3', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1108S3', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1108S4', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1108S4', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1108S5', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1108S5', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1108S6', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1108S6', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1108S7', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1108S7', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1108S8', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1108S8', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1108S9', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1108S9', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1110S1', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1110S1', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1110S10', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1110S10', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1110S11', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1110S11', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1110S12', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1110S12', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1110S2', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1110S2', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1110S3', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1110S3', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1110S4', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1110S4', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1110S5', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1110S5', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1110S6', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1110S6', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1110S7', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1110S7', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1110S8', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1110S8', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1110S9', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1110S9', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1112S1', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1112S1', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1112S10', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1112S10', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1112S11', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1112S11', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1112S12', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1112S12', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1112S2', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1112S2', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1112S3', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1112S3', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1112S4', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1112S4', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1112S5', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1112S5', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1112S6', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1112S6', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1112S7', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1112S7', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1112S8', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1112S8', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1112S9', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1112S9', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1114S1', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1114S1', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1114S10', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1114S10', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1114S11', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1114S11', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1114S12', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1114S12', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1114S2', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1114S2', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1114S3', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1114S3', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1114S4', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1114S4', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1114S5', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1114S5', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1114S6', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1114S6', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1114S7', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1114S7', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1114S8', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1114S8', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1114S9', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1114S9', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1116S1', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1116S1', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1116S10', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1116S10', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1116S11', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1116S11', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1116S12', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1116S12', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1116S2', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1116S2', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1116S3', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1116S3', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1116S4', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1116S4', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1116S5', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1116S5', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1116S6', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1116S6', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1116S7', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1116S7', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1116S8', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1116S8', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1116S9', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1116S9', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1118S1', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1118S1', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1118S10', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1118S10', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1118S11', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1118S11', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1118S12', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1118S12', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1118S2', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1118S2', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1118S3', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1118S3', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1118S4', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1118S4', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1118S5', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1118S5', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1118S6', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1118S6', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1118S7', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1118S7', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1118S8', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1118S8', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1118S9', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1118S9', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1120S1', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1120S1', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1120S10', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1120S10', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1120S11', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1120S11', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1120S12', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1120S12', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1120S2', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1120S2', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1120S3', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1120S3', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1120S4', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1120S4', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1120S5', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1120S5', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1120S6', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1120S6', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1120S7', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1120S7', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1120S8', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1120S8', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1120S9', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1120S9', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1122S1', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1122S1', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1122S10', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1122S10', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1122S11', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1122S11', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1122S12', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1122S12', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1122S2', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1122S2', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1122S3', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1122S3', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1122S4', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1122S4', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1122S5', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1122S5', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1122S6', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1122S6', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1122S7', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1122S7', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1122S8', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1122S8', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1122S9', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1122S9', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED1132S12', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED1132S12', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED724S0', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED724S0', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED724S1', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED724S1', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED724S10', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED724S10', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED724S11', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED724S11', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED724S2', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED724S2', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED724S3', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED724S3', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED724S4', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED724S4', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED724S5', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED724S5', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED724S6', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED724S6', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED724S7', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED724S7', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED724S8', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED724S8', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED724S9', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED724S9', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED725S0', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED725S0', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED725S1', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED725S1', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED725S10', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED725S10', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED725S11', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED725S11', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED725S2', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED725S2', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED725S3', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED725S3', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED725S4', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED725S4', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED725S5', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED725S5', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED725S6', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED725S6', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED725S7', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED725S7', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED725S8', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED725S8', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED725S9', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED725S9', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED726S0', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED726S0', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED726S1', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED726S1', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED726S10', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED726S10', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED726S11', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED726S11', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED726S12', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED726S12', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED726S13', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED726S13', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED726S2', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED726S2', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED726S3', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED726S3', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED726S4', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED726S4', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED726S5', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED726S5', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED726S6', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED726S6', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED726S7', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED726S7', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED726S8', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED726S8', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED726S9', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED726S9', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED727S0', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED727S0', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED727S1', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED727S1', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED727S10', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED727S10', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED727S11', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED727S11', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED727S12', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED727S12', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED727S13', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED727S13', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED727S2', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED727S2', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED727S3', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED727S3', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED727S4', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED727S4', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED727S5', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED727S5', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED727S6', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED727S6', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED727S7', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED727S7', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED727S8', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED727S8', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED727S9', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED727S9', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED728S0', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED728S0', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED728S1', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED728S1', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED728S10', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED728S10', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED728S11', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED728S11', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED728S12', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED728S12', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED728S13', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED728S13', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED728S2', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED728S2', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED728S3', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED728S3', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED728S4', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED728S4', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED728S5', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED728S5', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED728S6', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED728S6', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED728S7', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED728S7', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED728S8', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED728S8', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED728S9', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED728S9', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED729S0', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED729S0', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED729S1', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED729S1', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED729S10', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED729S10', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED729S11', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED729S11', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED729S12', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED729S12', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED729S13', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED729S13', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED729S2', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED729S2', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED729S3', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED729S3', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED729S4', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED729S4', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED729S5', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED729S5', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED729S6', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED729S6', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED729S7', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED729S7', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED729S8', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED729S8', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED729S9', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED729S9', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED730S0', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED730S0', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED730S1', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED730S1', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED730S10', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED730S10', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED730S11', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED730S11', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED730S12', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED730S12', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED730S13', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED730S13', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED730S2', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED730S2', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED730S3', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED730S3', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED730S4', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED730S4', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED730S5', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED730S5', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED730S6', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED730S6', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED730S7', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED730S7', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED730S8', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED730S8', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED730S9', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED730S9', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED731S0', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED731S0', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED731S1', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED731S1', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED731S10', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED731S10', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED731S11', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED731S11', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED731S2', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED731S2', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED731S3', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED731S3', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED731S4', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED731S4', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED731S5', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED731S5', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED731S6', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED731S6', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED731S7', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED731S7', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED731S8', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED731S8', 'description':''}])

hcallayout(dqmitems, 'TimingvsLS/DIGI/FEDSlot/FED731S9', [{'path':'/DigiTask/TimingvsLS/FEDSlot/FED731S9', 'description':''}])

hcallayout(dqmitems, 'EtData/TP/Electronics/VME', [{'path':'/TPTask/EtData/Electronics/VME', 'description':''}])

hcallayout(dqmitems, 'EtData/TP/Electronics/uTCA', [{'path':'/TPTask/EtData/Electronics/uTCA', 'description':''}])

hcallayout(dqmitems, 'Summary/DIGI', [{'path':'/DigiTask/Summary/Summary', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1100S1', [{'path':'/DigiTask/Timing/FEDSlot/FED1100S1', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1100S10', [{'path':'/DigiTask/Timing/FEDSlot/FED1100S10', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1100S11', [{'path':'/DigiTask/Timing/FEDSlot/FED1100S11', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1100S12', [{'path':'/DigiTask/Timing/FEDSlot/FED1100S12', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1100S2', [{'path':'/DigiTask/Timing/FEDSlot/FED1100S2', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1100S3', [{'path':'/DigiTask/Timing/FEDSlot/FED1100S3', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1100S4', [{'path':'/DigiTask/Timing/FEDSlot/FED1100S4', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1100S5', [{'path':'/DigiTask/Timing/FEDSlot/FED1100S5', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1100S6', [{'path':'/DigiTask/Timing/FEDSlot/FED1100S6', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1100S7', [{'path':'/DigiTask/Timing/FEDSlot/FED1100S7', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1100S8', [{'path':'/DigiTask/Timing/FEDSlot/FED1100S8', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1100S9', [{'path':'/DigiTask/Timing/FEDSlot/FED1100S9', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1102S1', [{'path':'/DigiTask/Timing/FEDSlot/FED1102S1', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1102S10', [{'path':'/DigiTask/Timing/FEDSlot/FED1102S10', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1102S11', [{'path':'/DigiTask/Timing/FEDSlot/FED1102S11', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1102S12', [{'path':'/DigiTask/Timing/FEDSlot/FED1102S12', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1102S2', [{'path':'/DigiTask/Timing/FEDSlot/FED1102S2', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1102S3', [{'path':'/DigiTask/Timing/FEDSlot/FED1102S3', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1102S4', [{'path':'/DigiTask/Timing/FEDSlot/FED1102S4', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1102S5', [{'path':'/DigiTask/Timing/FEDSlot/FED1102S5', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1102S6', [{'path':'/DigiTask/Timing/FEDSlot/FED1102S6', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1102S7', [{'path':'/DigiTask/Timing/FEDSlot/FED1102S7', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1102S8', [{'path':'/DigiTask/Timing/FEDSlot/FED1102S8', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1102S9', [{'path':'/DigiTask/Timing/FEDSlot/FED1102S9', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1104S1', [{'path':'/DigiTask/Timing/FEDSlot/FED1104S1', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1104S10', [{'path':'/DigiTask/Timing/FEDSlot/FED1104S10', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1104S11', [{'path':'/DigiTask/Timing/FEDSlot/FED1104S11', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1104S12', [{'path':'/DigiTask/Timing/FEDSlot/FED1104S12', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1104S2', [{'path':'/DigiTask/Timing/FEDSlot/FED1104S2', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1104S3', [{'path':'/DigiTask/Timing/FEDSlot/FED1104S3', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1104S4', [{'path':'/DigiTask/Timing/FEDSlot/FED1104S4', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1104S5', [{'path':'/DigiTask/Timing/FEDSlot/FED1104S5', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1104S6', [{'path':'/DigiTask/Timing/FEDSlot/FED1104S6', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1104S7', [{'path':'/DigiTask/Timing/FEDSlot/FED1104S7', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1104S8', [{'path':'/DigiTask/Timing/FEDSlot/FED1104S8', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1104S9', [{'path':'/DigiTask/Timing/FEDSlot/FED1104S9', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1106S1', [{'path':'/DigiTask/Timing/FEDSlot/FED1106S1', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1106S10', [{'path':'/DigiTask/Timing/FEDSlot/FED1106S10', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1106S11', [{'path':'/DigiTask/Timing/FEDSlot/FED1106S11', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1106S12', [{'path':'/DigiTask/Timing/FEDSlot/FED1106S12', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1106S2', [{'path':'/DigiTask/Timing/FEDSlot/FED1106S2', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1106S3', [{'path':'/DigiTask/Timing/FEDSlot/FED1106S3', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1106S4', [{'path':'/DigiTask/Timing/FEDSlot/FED1106S4', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1106S5', [{'path':'/DigiTask/Timing/FEDSlot/FED1106S5', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1106S6', [{'path':'/DigiTask/Timing/FEDSlot/FED1106S6', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1106S7', [{'path':'/DigiTask/Timing/FEDSlot/FED1106S7', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1106S8', [{'path':'/DigiTask/Timing/FEDSlot/FED1106S8', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1106S9', [{'path':'/DigiTask/Timing/FEDSlot/FED1106S9', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1108S1', [{'path':'/DigiTask/Timing/FEDSlot/FED1108S1', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1108S10', [{'path':'/DigiTask/Timing/FEDSlot/FED1108S10', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1108S11', [{'path':'/DigiTask/Timing/FEDSlot/FED1108S11', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1108S12', [{'path':'/DigiTask/Timing/FEDSlot/FED1108S12', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1108S2', [{'path':'/DigiTask/Timing/FEDSlot/FED1108S2', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1108S3', [{'path':'/DigiTask/Timing/FEDSlot/FED1108S3', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1108S4', [{'path':'/DigiTask/Timing/FEDSlot/FED1108S4', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1108S5', [{'path':'/DigiTask/Timing/FEDSlot/FED1108S5', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1108S6', [{'path':'/DigiTask/Timing/FEDSlot/FED1108S6', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1108S7', [{'path':'/DigiTask/Timing/FEDSlot/FED1108S7', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1108S8', [{'path':'/DigiTask/Timing/FEDSlot/FED1108S8', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1108S9', [{'path':'/DigiTask/Timing/FEDSlot/FED1108S9', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1110S1', [{'path':'/DigiTask/Timing/FEDSlot/FED1110S1', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1110S10', [{'path':'/DigiTask/Timing/FEDSlot/FED1110S10', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1110S11', [{'path':'/DigiTask/Timing/FEDSlot/FED1110S11', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1110S12', [{'path':'/DigiTask/Timing/FEDSlot/FED1110S12', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1110S2', [{'path':'/DigiTask/Timing/FEDSlot/FED1110S2', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1110S3', [{'path':'/DigiTask/Timing/FEDSlot/FED1110S3', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1110S4', [{'path':'/DigiTask/Timing/FEDSlot/FED1110S4', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1110S5', [{'path':'/DigiTask/Timing/FEDSlot/FED1110S5', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1110S6', [{'path':'/DigiTask/Timing/FEDSlot/FED1110S6', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1110S7', [{'path':'/DigiTask/Timing/FEDSlot/FED1110S7', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1110S8', [{'path':'/DigiTask/Timing/FEDSlot/FED1110S8', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1110S9', [{'path':'/DigiTask/Timing/FEDSlot/FED1110S9', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1112S1', [{'path':'/DigiTask/Timing/FEDSlot/FED1112S1', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1112S10', [{'path':'/DigiTask/Timing/FEDSlot/FED1112S10', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1112S11', [{'path':'/DigiTask/Timing/FEDSlot/FED1112S11', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1112S12', [{'path':'/DigiTask/Timing/FEDSlot/FED1112S12', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1112S2', [{'path':'/DigiTask/Timing/FEDSlot/FED1112S2', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1112S3', [{'path':'/DigiTask/Timing/FEDSlot/FED1112S3', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1112S4', [{'path':'/DigiTask/Timing/FEDSlot/FED1112S4', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1112S5', [{'path':'/DigiTask/Timing/FEDSlot/FED1112S5', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1112S6', [{'path':'/DigiTask/Timing/FEDSlot/FED1112S6', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1112S7', [{'path':'/DigiTask/Timing/FEDSlot/FED1112S7', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1112S8', [{'path':'/DigiTask/Timing/FEDSlot/FED1112S8', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1112S9', [{'path':'/DigiTask/Timing/FEDSlot/FED1112S9', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1114S1', [{'path':'/DigiTask/Timing/FEDSlot/FED1114S1', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1114S10', [{'path':'/DigiTask/Timing/FEDSlot/FED1114S10', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1114S11', [{'path':'/DigiTask/Timing/FEDSlot/FED1114S11', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1114S12', [{'path':'/DigiTask/Timing/FEDSlot/FED1114S12', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1114S2', [{'path':'/DigiTask/Timing/FEDSlot/FED1114S2', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1114S3', [{'path':'/DigiTask/Timing/FEDSlot/FED1114S3', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1114S4', [{'path':'/DigiTask/Timing/FEDSlot/FED1114S4', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1114S5', [{'path':'/DigiTask/Timing/FEDSlot/FED1114S5', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1114S6', [{'path':'/DigiTask/Timing/FEDSlot/FED1114S6', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1114S7', [{'path':'/DigiTask/Timing/FEDSlot/FED1114S7', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1114S8', [{'path':'/DigiTask/Timing/FEDSlot/FED1114S8', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1114S9', [{'path':'/DigiTask/Timing/FEDSlot/FED1114S9', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1116S1', [{'path':'/DigiTask/Timing/FEDSlot/FED1116S1', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1116S10', [{'path':'/DigiTask/Timing/FEDSlot/FED1116S10', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1116S11', [{'path':'/DigiTask/Timing/FEDSlot/FED1116S11', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1116S12', [{'path':'/DigiTask/Timing/FEDSlot/FED1116S12', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1116S2', [{'path':'/DigiTask/Timing/FEDSlot/FED1116S2', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1116S3', [{'path':'/DigiTask/Timing/FEDSlot/FED1116S3', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1116S4', [{'path':'/DigiTask/Timing/FEDSlot/FED1116S4', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1116S5', [{'path':'/DigiTask/Timing/FEDSlot/FED1116S5', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1116S6', [{'path':'/DigiTask/Timing/FEDSlot/FED1116S6', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1116S7', [{'path':'/DigiTask/Timing/FEDSlot/FED1116S7', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1116S8', [{'path':'/DigiTask/Timing/FEDSlot/FED1116S8', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1116S9', [{'path':'/DigiTask/Timing/FEDSlot/FED1116S9', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1118S1', [{'path':'/DigiTask/Timing/FEDSlot/FED1118S1', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1118S10', [{'path':'/DigiTask/Timing/FEDSlot/FED1118S10', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1118S11', [{'path':'/DigiTask/Timing/FEDSlot/FED1118S11', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1118S12', [{'path':'/DigiTask/Timing/FEDSlot/FED1118S12', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1118S2', [{'path':'/DigiTask/Timing/FEDSlot/FED1118S2', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1118S3', [{'path':'/DigiTask/Timing/FEDSlot/FED1118S3', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1118S4', [{'path':'/DigiTask/Timing/FEDSlot/FED1118S4', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1118S5', [{'path':'/DigiTask/Timing/FEDSlot/FED1118S5', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1118S6', [{'path':'/DigiTask/Timing/FEDSlot/FED1118S6', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1118S7', [{'path':'/DigiTask/Timing/FEDSlot/FED1118S7', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1118S8', [{'path':'/DigiTask/Timing/FEDSlot/FED1118S8', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1118S9', [{'path':'/DigiTask/Timing/FEDSlot/FED1118S9', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1120S1', [{'path':'/DigiTask/Timing/FEDSlot/FED1120S1', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1120S10', [{'path':'/DigiTask/Timing/FEDSlot/FED1120S10', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1120S11', [{'path':'/DigiTask/Timing/FEDSlot/FED1120S11', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1120S12', [{'path':'/DigiTask/Timing/FEDSlot/FED1120S12', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1120S2', [{'path':'/DigiTask/Timing/FEDSlot/FED1120S2', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1120S3', [{'path':'/DigiTask/Timing/FEDSlot/FED1120S3', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1120S4', [{'path':'/DigiTask/Timing/FEDSlot/FED1120S4', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1120S5', [{'path':'/DigiTask/Timing/FEDSlot/FED1120S5', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1120S6', [{'path':'/DigiTask/Timing/FEDSlot/FED1120S6', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1120S7', [{'path':'/DigiTask/Timing/FEDSlot/FED1120S7', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1120S8', [{'path':'/DigiTask/Timing/FEDSlot/FED1120S8', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1120S9', [{'path':'/DigiTask/Timing/FEDSlot/FED1120S9', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1122S1', [{'path':'/DigiTask/Timing/FEDSlot/FED1122S1', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1122S10', [{'path':'/DigiTask/Timing/FEDSlot/FED1122S10', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1122S11', [{'path':'/DigiTask/Timing/FEDSlot/FED1122S11', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1122S12', [{'path':'/DigiTask/Timing/FEDSlot/FED1122S12', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1122S2', [{'path':'/DigiTask/Timing/FEDSlot/FED1122S2', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1122S3', [{'path':'/DigiTask/Timing/FEDSlot/FED1122S3', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1122S4', [{'path':'/DigiTask/Timing/FEDSlot/FED1122S4', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1122S5', [{'path':'/DigiTask/Timing/FEDSlot/FED1122S5', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1122S6', [{'path':'/DigiTask/Timing/FEDSlot/FED1122S6', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1122S7', [{'path':'/DigiTask/Timing/FEDSlot/FED1122S7', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1122S8', [{'path':'/DigiTask/Timing/FEDSlot/FED1122S8', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1122S9', [{'path':'/DigiTask/Timing/FEDSlot/FED1122S9', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED1132S12', [{'path':'/DigiTask/Timing/FEDSlot/FED1132S12', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED724S0', [{'path':'/DigiTask/Timing/FEDSlot/FED724S0', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED724S1', [{'path':'/DigiTask/Timing/FEDSlot/FED724S1', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED724S10', [{'path':'/DigiTask/Timing/FEDSlot/FED724S10', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED724S11', [{'path':'/DigiTask/Timing/FEDSlot/FED724S11', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED724S2', [{'path':'/DigiTask/Timing/FEDSlot/FED724S2', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED724S3', [{'path':'/DigiTask/Timing/FEDSlot/FED724S3', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED724S4', [{'path':'/DigiTask/Timing/FEDSlot/FED724S4', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED724S5', [{'path':'/DigiTask/Timing/FEDSlot/FED724S5', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED724S6', [{'path':'/DigiTask/Timing/FEDSlot/FED724S6', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED724S7', [{'path':'/DigiTask/Timing/FEDSlot/FED724S7', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED724S8', [{'path':'/DigiTask/Timing/FEDSlot/FED724S8', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED724S9', [{'path':'/DigiTask/Timing/FEDSlot/FED724S9', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED725S0', [{'path':'/DigiTask/Timing/FEDSlot/FED725S0', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED725S1', [{'path':'/DigiTask/Timing/FEDSlot/FED725S1', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED725S10', [{'path':'/DigiTask/Timing/FEDSlot/FED725S10', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED725S11', [{'path':'/DigiTask/Timing/FEDSlot/FED725S11', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED725S2', [{'path':'/DigiTask/Timing/FEDSlot/FED725S2', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED725S3', [{'path':'/DigiTask/Timing/FEDSlot/FED725S3', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED725S4', [{'path':'/DigiTask/Timing/FEDSlot/FED725S4', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED725S5', [{'path':'/DigiTask/Timing/FEDSlot/FED725S5', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED725S6', [{'path':'/DigiTask/Timing/FEDSlot/FED725S6', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED725S7', [{'path':'/DigiTask/Timing/FEDSlot/FED725S7', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED725S8', [{'path':'/DigiTask/Timing/FEDSlot/FED725S8', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED725S9', [{'path':'/DigiTask/Timing/FEDSlot/FED725S9', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED726S0', [{'path':'/DigiTask/Timing/FEDSlot/FED726S0', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED726S1', [{'path':'/DigiTask/Timing/FEDSlot/FED726S1', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED726S10', [{'path':'/DigiTask/Timing/FEDSlot/FED726S10', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED726S11', [{'path':'/DigiTask/Timing/FEDSlot/FED726S11', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED726S12', [{'path':'/DigiTask/Timing/FEDSlot/FED726S12', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED726S13', [{'path':'/DigiTask/Timing/FEDSlot/FED726S13', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED726S2', [{'path':'/DigiTask/Timing/FEDSlot/FED726S2', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED726S3', [{'path':'/DigiTask/Timing/FEDSlot/FED726S3', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED726S4', [{'path':'/DigiTask/Timing/FEDSlot/FED726S4', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED726S5', [{'path':'/DigiTask/Timing/FEDSlot/FED726S5', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED726S6', [{'path':'/DigiTask/Timing/FEDSlot/FED726S6', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED726S7', [{'path':'/DigiTask/Timing/FEDSlot/FED726S7', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED726S8', [{'path':'/DigiTask/Timing/FEDSlot/FED726S8', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED726S9', [{'path':'/DigiTask/Timing/FEDSlot/FED726S9', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED727S0', [{'path':'/DigiTask/Timing/FEDSlot/FED727S0', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED727S1', [{'path':'/DigiTask/Timing/FEDSlot/FED727S1', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED727S10', [{'path':'/DigiTask/Timing/FEDSlot/FED727S10', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED727S11', [{'path':'/DigiTask/Timing/FEDSlot/FED727S11', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED727S12', [{'path':'/DigiTask/Timing/FEDSlot/FED727S12', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED727S13', [{'path':'/DigiTask/Timing/FEDSlot/FED727S13', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED727S2', [{'path':'/DigiTask/Timing/FEDSlot/FED727S2', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED727S3', [{'path':'/DigiTask/Timing/FEDSlot/FED727S3', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED727S4', [{'path':'/DigiTask/Timing/FEDSlot/FED727S4', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED727S5', [{'path':'/DigiTask/Timing/FEDSlot/FED727S5', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED727S6', [{'path':'/DigiTask/Timing/FEDSlot/FED727S6', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED727S7', [{'path':'/DigiTask/Timing/FEDSlot/FED727S7', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED727S8', [{'path':'/DigiTask/Timing/FEDSlot/FED727S8', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED727S9', [{'path':'/DigiTask/Timing/FEDSlot/FED727S9', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED728S0', [{'path':'/DigiTask/Timing/FEDSlot/FED728S0', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED728S1', [{'path':'/DigiTask/Timing/FEDSlot/FED728S1', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED728S10', [{'path':'/DigiTask/Timing/FEDSlot/FED728S10', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED728S11', [{'path':'/DigiTask/Timing/FEDSlot/FED728S11', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED728S12', [{'path':'/DigiTask/Timing/FEDSlot/FED728S12', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED728S13', [{'path':'/DigiTask/Timing/FEDSlot/FED728S13', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED728S2', [{'path':'/DigiTask/Timing/FEDSlot/FED728S2', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED728S3', [{'path':'/DigiTask/Timing/FEDSlot/FED728S3', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED728S4', [{'path':'/DigiTask/Timing/FEDSlot/FED728S4', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED728S5', [{'path':'/DigiTask/Timing/FEDSlot/FED728S5', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED728S6', [{'path':'/DigiTask/Timing/FEDSlot/FED728S6', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED728S7', [{'path':'/DigiTask/Timing/FEDSlot/FED728S7', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED728S8', [{'path':'/DigiTask/Timing/FEDSlot/FED728S8', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED728S9', [{'path':'/DigiTask/Timing/FEDSlot/FED728S9', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED729S0', [{'path':'/DigiTask/Timing/FEDSlot/FED729S0', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED729S1', [{'path':'/DigiTask/Timing/FEDSlot/FED729S1', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED729S10', [{'path':'/DigiTask/Timing/FEDSlot/FED729S10', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED729S11', [{'path':'/DigiTask/Timing/FEDSlot/FED729S11', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED729S12', [{'path':'/DigiTask/Timing/FEDSlot/FED729S12', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED729S13', [{'path':'/DigiTask/Timing/FEDSlot/FED729S13', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED729S2', [{'path':'/DigiTask/Timing/FEDSlot/FED729S2', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED729S3', [{'path':'/DigiTask/Timing/FEDSlot/FED729S3', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED729S4', [{'path':'/DigiTask/Timing/FEDSlot/FED729S4', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED729S5', [{'path':'/DigiTask/Timing/FEDSlot/FED729S5', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED729S6', [{'path':'/DigiTask/Timing/FEDSlot/FED729S6', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED729S7', [{'path':'/DigiTask/Timing/FEDSlot/FED729S7', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED729S8', [{'path':'/DigiTask/Timing/FEDSlot/FED729S8', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED729S9', [{'path':'/DigiTask/Timing/FEDSlot/FED729S9', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED730S0', [{'path':'/DigiTask/Timing/FEDSlot/FED730S0', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED730S1', [{'path':'/DigiTask/Timing/FEDSlot/FED730S1', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED730S10', [{'path':'/DigiTask/Timing/FEDSlot/FED730S10', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED730S11', [{'path':'/DigiTask/Timing/FEDSlot/FED730S11', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED730S12', [{'path':'/DigiTask/Timing/FEDSlot/FED730S12', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED730S13', [{'path':'/DigiTask/Timing/FEDSlot/FED730S13', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED730S2', [{'path':'/DigiTask/Timing/FEDSlot/FED730S2', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED730S3', [{'path':'/DigiTask/Timing/FEDSlot/FED730S3', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED730S4', [{'path':'/DigiTask/Timing/FEDSlot/FED730S4', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED730S5', [{'path':'/DigiTask/Timing/FEDSlot/FED730S5', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED730S6', [{'path':'/DigiTask/Timing/FEDSlot/FED730S6', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED730S7', [{'path':'/DigiTask/Timing/FEDSlot/FED730S7', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED730S8', [{'path':'/DigiTask/Timing/FEDSlot/FED730S8', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED730S9', [{'path':'/DigiTask/Timing/FEDSlot/FED730S9', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED731S0', [{'path':'/DigiTask/Timing/FEDSlot/FED731S0', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED731S1', [{'path':'/DigiTask/Timing/FEDSlot/FED731S1', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED731S10', [{'path':'/DigiTask/Timing/FEDSlot/FED731S10', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED731S11', [{'path':'/DigiTask/Timing/FEDSlot/FED731S11', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED731S2', [{'path':'/DigiTask/Timing/FEDSlot/FED731S2', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED731S3', [{'path':'/DigiTask/Timing/FEDSlot/FED731S3', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED731S4', [{'path':'/DigiTask/Timing/FEDSlot/FED731S4', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED731S5', [{'path':'/DigiTask/Timing/FEDSlot/FED731S5', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED731S6', [{'path':'/DigiTask/Timing/FEDSlot/FED731S6', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED731S7', [{'path':'/DigiTask/Timing/FEDSlot/FED731S7', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED731S8', [{'path':'/DigiTask/Timing/FEDSlot/FED731S8', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FEDSlot/FED731S9', [{'path':'/DigiTask/Timing/FEDSlot/FED731S9', 'description':''}])

hcallayout(dqmitems, 'Energy/RECO/Subdet/HB', [{'path':'/RecHitTask/Energy/Subdet/HB', 'description':''}])

hcallayout(dqmitems, 'Energy/RECO/Subdet/HE', [{'path':'/RecHitTask/Energy/Subdet/HE', 'description':''}])

hcallayout(dqmitems, 'Energy/RECO/Subdet/HF', [{'path':'/RecHitTask/Energy/Subdet/HF', 'description':''}])

hcallayout(dqmitems, 'Energy/RECO/Subdet/HO', [{'path':'/RecHitTask/Energy/Subdet/HO', 'description':''}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED1100', [{'path':'/DigiTask/Occupancy/FED/FED1100', 'description':''}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED1102', [{'path':'/DigiTask/Occupancy/FED/FED1102', 'description':''}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED1104', [{'path':'/DigiTask/Occupancy/FED/FED1104', 'description':''}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED1106', [{'path':'/DigiTask/Occupancy/FED/FED1106', 'description':''}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED1108', [{'path':'/DigiTask/Occupancy/FED/FED1108', 'description':''}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED1110', [{'path':'/DigiTask/Occupancy/FED/FED1110', 'description':''}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED1112', [{'path':'/DigiTask/Occupancy/FED/FED1112', 'description':''}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED1114', [{'path':'/DigiTask/Occupancy/FED/FED1114', 'description':''}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED1116', [{'path':'/DigiTask/Occupancy/FED/FED1116', 'description':''}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED1118', [{'path':'/DigiTask/Occupancy/FED/FED1118', 'description':''}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED1120', [{'path':'/DigiTask/Occupancy/FED/FED1120', 'description':''}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED1122', [{'path':'/DigiTask/Occupancy/FED/FED1122', 'description':''}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED1132', [{'path':'/DigiTask/Occupancy/FED/FED1132', 'description':''}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED724', [{'path':'/DigiTask/Occupancy/FED/FED724', 'description':''}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED725', [{'path':'/DigiTask/Occupancy/FED/FED725', 'description':''}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED726', [{'path':'/DigiTask/Occupancy/FED/FED726', 'description':''}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED727', [{'path':'/DigiTask/Occupancy/FED/FED727', 'description':''}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED728', [{'path':'/DigiTask/Occupancy/FED/FED728', 'description':''}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED729', [{'path':'/DigiTask/Occupancy/FED/FED729', 'description':''}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED730', [{'path':'/DigiTask/Occupancy/FED/FED730', 'description':''}])

hcallayout(dqmitems, 'Occupancy/DIGI/FED/FED731', [{'path':'/DigiTask/Occupancy/FED/FED731', 'description':''}])

hcallayout(dqmitems, 'OccupancyCutData/TP/Electronics/VME', [{'path':'/TPTask/OccupancyCutData/Electronics/VME', 'description':''}])

hcallayout(dqmitems, 'OccupancyCutData/TP/Electronics/uTCA', [{'path':'/TPTask/OccupancyCutData/Electronics/uTCA', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/depth/depth1', [{'path':'/RecHitTask/TimingCut/depth/depth1', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/depth/depth2', [{'path':'/RecHitTask/TimingCut/depth/depth2', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/depth/depth3', [{'path':'/RecHitTask/TimingCut/depth/depth3', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/depth/depth4', [{'path':'/RecHitTask/TimingCut/depth/depth4', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1100S1', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1100S1', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1100S10', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1100S10', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1100S11', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1100S11', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1100S12', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1100S12', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1100S2', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1100S2', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1100S3', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1100S3', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1100S4', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1100S4', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1100S5', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1100S5', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1100S6', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1100S6', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1100S7', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1100S7', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1100S8', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1100S8', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1100S9', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1100S9', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1102S1', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1102S1', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1102S10', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1102S10', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1102S11', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1102S11', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1102S12', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1102S12', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1102S2', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1102S2', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1102S3', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1102S3', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1102S4', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1102S4', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1102S5', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1102S5', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1102S6', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1102S6', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1102S7', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1102S7', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1102S8', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1102S8', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1102S9', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1102S9', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1104S1', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1104S1', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1104S10', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1104S10', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1104S11', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1104S11', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1104S12', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1104S12', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1104S2', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1104S2', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1104S3', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1104S3', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1104S4', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1104S4', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1104S5', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1104S5', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1104S6', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1104S6', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1104S7', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1104S7', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1104S8', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1104S8', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1104S9', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1104S9', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1106S1', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1106S1', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1106S10', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1106S10', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1106S11', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1106S11', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1106S12', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1106S12', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1106S2', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1106S2', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1106S3', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1106S3', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1106S4', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1106S4', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1106S5', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1106S5', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1106S6', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1106S6', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1106S7', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1106S7', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1106S8', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1106S8', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1106S9', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1106S9', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1108S1', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1108S1', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1108S10', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1108S10', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1108S11', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1108S11', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1108S12', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1108S12', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1108S2', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1108S2', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1108S3', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1108S3', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1108S4', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1108S4', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1108S5', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1108S5', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1108S6', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1108S6', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1108S7', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1108S7', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1108S8', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1108S8', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1108S9', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1108S9', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1110S1', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1110S1', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1110S10', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1110S10', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1110S11', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1110S11', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1110S12', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1110S12', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1110S2', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1110S2', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1110S3', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1110S3', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1110S4', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1110S4', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1110S5', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1110S5', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1110S6', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1110S6', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1110S7', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1110S7', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1110S8', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1110S8', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1110S9', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1110S9', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1112S1', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1112S1', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1112S10', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1112S10', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1112S11', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1112S11', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1112S12', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1112S12', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1112S2', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1112S2', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1112S3', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1112S3', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1112S4', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1112S4', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1112S5', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1112S5', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1112S6', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1112S6', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1112S7', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1112S7', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1112S8', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1112S8', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1112S9', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1112S9', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1114S1', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1114S1', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1114S10', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1114S10', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1114S11', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1114S11', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1114S12', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1114S12', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1114S2', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1114S2', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1114S3', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1114S3', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1114S4', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1114S4', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1114S5', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1114S5', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1114S6', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1114S6', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1114S7', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1114S7', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1114S8', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1114S8', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1114S9', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1114S9', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1116S1', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1116S1', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1116S10', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1116S10', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1116S11', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1116S11', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1116S12', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1116S12', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1116S2', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1116S2', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1116S3', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1116S3', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1116S4', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1116S4', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1116S5', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1116S5', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1116S6', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1116S6', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1116S7', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1116S7', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1116S8', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1116S8', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1116S9', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1116S9', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1118S1', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1118S1', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1118S10', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1118S10', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1118S11', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1118S11', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1118S12', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1118S12', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1118S2', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1118S2', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1118S3', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1118S3', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1118S4', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1118S4', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1118S5', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1118S5', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1118S6', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1118S6', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1118S7', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1118S7', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1118S8', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1118S8', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1118S9', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1118S9', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1120S1', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1120S1', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1120S10', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1120S10', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1120S11', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1120S11', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1120S12', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1120S12', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1120S2', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1120S2', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1120S3', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1120S3', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1120S4', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1120S4', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1120S5', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1120S5', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1120S6', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1120S6', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1120S7', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1120S7', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1120S8', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1120S8', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1120S9', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1120S9', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1122S1', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1122S1', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1122S10', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1122S10', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1122S11', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1122S11', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1122S12', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1122S12', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1122S2', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1122S2', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1122S3', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1122S3', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1122S4', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1122S4', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1122S5', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1122S5', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1122S6', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1122S6', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1122S7', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1122S7', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1122S8', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1122S8', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1122S9', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1122S9', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED1132S12', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED1132S12', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED724S0', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED724S0', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED724S1', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED724S1', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED724S10', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED724S10', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED724S11', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED724S11', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED724S2', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED724S2', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED724S3', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED724S3', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED724S4', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED724S4', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED724S5', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED724S5', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED724S6', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED724S6', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED724S7', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED724S7', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED724S8', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED724S8', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED724S9', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED724S9', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED725S0', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED725S0', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED725S1', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED725S1', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED725S10', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED725S10', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED725S11', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED725S11', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED725S2', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED725S2', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED725S3', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED725S3', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED725S4', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED725S4', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED725S5', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED725S5', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED725S6', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED725S6', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED725S7', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED725S7', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED725S8', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED725S8', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED725S9', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED725S9', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED726S0', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED726S0', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED726S1', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED726S1', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED726S10', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED726S10', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED726S11', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED726S11', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED726S12', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED726S12', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED726S13', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED726S13', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED726S2', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED726S2', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED726S3', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED726S3', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED726S4', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED726S4', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED726S5', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED726S5', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED726S6', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED726S6', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED726S7', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED726S7', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED726S8', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED726S8', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED726S9', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED726S9', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED727S0', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED727S0', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED727S1', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED727S1', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED727S10', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED727S10', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED727S11', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED727S11', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED727S12', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED727S12', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED727S13', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED727S13', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED727S2', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED727S2', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED727S3', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED727S3', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED727S4', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED727S4', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED727S5', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED727S5', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED727S6', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED727S6', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED727S7', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED727S7', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED727S8', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED727S8', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED727S9', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED727S9', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED728S0', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED728S0', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED728S1', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED728S1', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED728S10', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED728S10', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED728S11', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED728S11', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED728S12', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED728S12', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED728S13', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED728S13', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED728S2', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED728S2', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED728S3', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED728S3', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED728S4', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED728S4', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED728S5', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED728S5', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED728S6', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED728S6', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED728S7', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED728S7', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED728S8', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED728S8', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED728S9', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED728S9', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED729S0', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED729S0', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED729S1', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED729S1', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED729S10', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED729S10', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED729S11', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED729S11', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED729S12', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED729S12', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED729S13', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED729S13', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED729S2', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED729S2', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED729S3', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED729S3', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED729S4', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED729S4', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED729S5', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED729S5', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED729S6', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED729S6', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED729S7', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED729S7', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED729S8', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED729S8', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED729S9', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED729S9', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED730S0', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED730S0', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED730S1', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED730S1', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED730S10', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED730S10', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED730S11', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED730S11', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED730S12', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED730S12', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED730S13', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED730S13', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED730S2', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED730S2', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED730S3', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED730S3', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED730S4', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED730S4', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED730S5', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED730S5', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED730S6', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED730S6', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED730S7', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED730S7', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED730S8', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED730S8', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED730S9', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED730S9', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED731S0', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED731S0', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED731S1', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED731S1', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED731S10', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED731S10', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED731S11', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED731S11', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED731S2', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED731S2', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED731S3', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED731S3', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED731S4', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED731S4', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED731S5', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED731S5', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED731S6', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED731S6', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED731S7', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED731S7', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED731S8', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED731S8', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FEDSlot/FED731S9', [{'path':'/RecHitTask/TimingCut/FEDSlot/FED731S9', 'description':''}])

hcallayout(dqmitems, 'OccupancyCutEmul/TP', [{'path':'/TPTask/OccupancyCutEmul/OccupancyCutEmul', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/Electronics/VME', [{'path':'/DigiTask/OccupancyCut/Electronics/VME', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/Electronics/uTCA', [{'path':'/DigiTask/OccupancyCut/Electronics/uTCA', 'description':''}])

hcallayout(dqmitems, 'MsnEmul/TP', [{'path':'/TPTask/MsnEmul/MsnEmul', 'description':''}])

hcallayout(dqmitems, 'Occupancy/RECO/depth/depth1', [{'path':'/RecHitTask/Occupancy/depth/depth1', 'description':''}])

hcallayout(dqmitems, 'Occupancy/RECO/depth/depth2', [{'path':'/RecHitTask/Occupancy/depth/depth2', 'description':''}])

hcallayout(dqmitems, 'Occupancy/RECO/depth/depth3', [{'path':'/RecHitTask/Occupancy/depth/depth3', 'description':''}])

hcallayout(dqmitems, 'Occupancy/RECO/depth/depth4', [{'path':'/RecHitTask/Occupancy/depth/depth4', 'description':''}])

hcallayout(dqmitems, 'EvnMsm/RAW/Electronics/VME', [{'path':'/RawTask/EvnMsm/Electronics/VME', 'description':'DESC<a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription">Description</a>'}])

hcallayout(dqmitems, 'EvnMsm/RAW/Electronics/uTCA', [{'path':'/RawTask/EvnMsm/Electronics/uTCA', 'description':'DESC<a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription">Description</a>'}])

hcallayout(dqmitems, 'OccupancyCutvsLS/DIGI/Subdet/HB', [{'path':'/DigiTask/OccupancyCutvsLS/Subdet/HB', 'description':''}])

hcallayout(dqmitems, 'OccupancyCutvsLS/DIGI/Subdet/HE', [{'path':'/DigiTask/OccupancyCutvsLS/Subdet/HE', 'description':''}])

hcallayout(dqmitems, 'OccupancyCutvsLS/DIGI/Subdet/HF', [{'path':'/DigiTask/OccupancyCutvsLS/Subdet/HF', 'description':''}])

hcallayout(dqmitems, 'OccupancyCutvsLS/DIGI/Subdet/HO', [{'path':'/DigiTask/OccupancyCutvsLS/Subdet/HO', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1100S1', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1100S1', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1100S10', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1100S10', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1100S11', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1100S11', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1100S12', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1100S12', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1100S2', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1100S2', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1100S3', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1100S3', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1100S4', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1100S4', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1100S5', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1100S5', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1100S6', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1100S6', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1100S7', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1100S7', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1100S8', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1100S8', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1100S9', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1100S9', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1102S1', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1102S1', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1102S10', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1102S10', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1102S11', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1102S11', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1102S12', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1102S12', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1102S2', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1102S2', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1102S3', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1102S3', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1102S4', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1102S4', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1102S5', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1102S5', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1102S6', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1102S6', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1102S7', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1102S7', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1102S8', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1102S8', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1102S9', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1102S9', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1104S1', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1104S1', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1104S10', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1104S10', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1104S11', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1104S11', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1104S12', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1104S12', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1104S2', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1104S2', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1104S3', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1104S3', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1104S4', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1104S4', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1104S5', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1104S5', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1104S6', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1104S6', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1104S7', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1104S7', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1104S8', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1104S8', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1104S9', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1104S9', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1106S1', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1106S1', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1106S10', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1106S10', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1106S11', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1106S11', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1106S12', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1106S12', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1106S2', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1106S2', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1106S3', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1106S3', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1106S4', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1106S4', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1106S5', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1106S5', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1106S6', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1106S6', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1106S7', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1106S7', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1106S8', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1106S8', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1106S9', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1106S9', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1108S1', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1108S1', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1108S10', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1108S10', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1108S11', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1108S11', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1108S12', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1108S12', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1108S2', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1108S2', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1108S3', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1108S3', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1108S4', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1108S4', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1108S5', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1108S5', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1108S6', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1108S6', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1108S7', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1108S7', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1108S8', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1108S8', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1108S9', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1108S9', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1110S1', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1110S1', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1110S10', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1110S10', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1110S11', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1110S11', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1110S12', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1110S12', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1110S2', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1110S2', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1110S3', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1110S3', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1110S4', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1110S4', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1110S5', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1110S5', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1110S6', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1110S6', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1110S7', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1110S7', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1110S8', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1110S8', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1110S9', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1110S9', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1112S1', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1112S1', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1112S10', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1112S10', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1112S11', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1112S11', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1112S12', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1112S12', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1112S2', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1112S2', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1112S3', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1112S3', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1112S4', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1112S4', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1112S5', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1112S5', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1112S6', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1112S6', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1112S7', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1112S7', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1112S8', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1112S8', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1112S9', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1112S9', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1114S1', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1114S1', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1114S10', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1114S10', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1114S11', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1114S11', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1114S12', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1114S12', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1114S2', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1114S2', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1114S3', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1114S3', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1114S4', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1114S4', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1114S5', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1114S5', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1114S6', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1114S6', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1114S7', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1114S7', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1114S8', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1114S8', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1114S9', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1114S9', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1116S1', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1116S1', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1116S10', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1116S10', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1116S11', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1116S11', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1116S12', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1116S12', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1116S2', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1116S2', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1116S3', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1116S3', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1116S4', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1116S4', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1116S5', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1116S5', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1116S6', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1116S6', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1116S7', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1116S7', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1116S8', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1116S8', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1116S9', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1116S9', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1118S1', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1118S1', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1118S10', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1118S10', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1118S11', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1118S11', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1118S12', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1118S12', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1118S2', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1118S2', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1118S3', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1118S3', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1118S4', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1118S4', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1118S5', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1118S5', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1118S6', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1118S6', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1118S7', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1118S7', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1118S8', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1118S8', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1118S9', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1118S9', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1120S1', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1120S1', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1120S10', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1120S10', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1120S11', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1120S11', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1120S12', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1120S12', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1120S2', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1120S2', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1120S3', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1120S3', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1120S4', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1120S4', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1120S5', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1120S5', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1120S6', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1120S6', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1120S7', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1120S7', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1120S8', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1120S8', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1120S9', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1120S9', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1122S1', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1122S1', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1122S10', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1122S10', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1122S11', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1122S11', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1122S12', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1122S12', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1122S2', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1122S2', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1122S3', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1122S3', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1122S4', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1122S4', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1122S5', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1122S5', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1122S6', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1122S6', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1122S7', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1122S7', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1122S8', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1122S8', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1122S9', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1122S9', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED1132S12', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED1132S12', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED724S0', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED724S0', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED724S1', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED724S1', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED724S10', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED724S10', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED724S11', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED724S11', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED724S2', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED724S2', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED724S3', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED724S3', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED724S4', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED724S4', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED724S5', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED724S5', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED724S6', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED724S6', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED724S7', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED724S7', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED724S8', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED724S8', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED724S9', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED724S9', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED725S0', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED725S0', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED725S1', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED725S1', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED725S10', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED725S10', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED725S11', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED725S11', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED725S2', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED725S2', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED725S3', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED725S3', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED725S4', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED725S4', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED725S5', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED725S5', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED725S6', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED725S6', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED725S7', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED725S7', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED725S8', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED725S8', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED725S9', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED725S9', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED726S0', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED726S0', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED726S1', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED726S1', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED726S10', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED726S10', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED726S11', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED726S11', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED726S12', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED726S12', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED726S13', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED726S13', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED726S2', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED726S2', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED726S3', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED726S3', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED726S4', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED726S4', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED726S5', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED726S5', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED726S6', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED726S6', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED726S7', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED726S7', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED726S8', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED726S8', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED726S9', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED726S9', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED727S0', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED727S0', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED727S1', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED727S1', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED727S10', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED727S10', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED727S11', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED727S11', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED727S12', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED727S12', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED727S13', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED727S13', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED727S2', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED727S2', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED727S3', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED727S3', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED727S4', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED727S4', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED727S5', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED727S5', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED727S6', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED727S6', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED727S7', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED727S7', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED727S8', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED727S8', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED727S9', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED727S9', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED728S0', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED728S0', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED728S1', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED728S1', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED728S10', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED728S10', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED728S11', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED728S11', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED728S12', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED728S12', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED728S13', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED728S13', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED728S2', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED728S2', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED728S3', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED728S3', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED728S4', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED728S4', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED728S5', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED728S5', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED728S6', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED728S6', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED728S7', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED728S7', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED728S8', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED728S8', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED728S9', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED728S9', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED729S0', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED729S0', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED729S1', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED729S1', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED729S10', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED729S10', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED729S11', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED729S11', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED729S12', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED729S12', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED729S13', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED729S13', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED729S2', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED729S2', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED729S3', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED729S3', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED729S4', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED729S4', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED729S5', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED729S5', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED729S6', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED729S6', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED729S7', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED729S7', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED729S8', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED729S8', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED729S9', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED729S9', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED730S0', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED730S0', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED730S1', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED730S1', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED730S10', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED730S10', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED730S11', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED730S11', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED730S12', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED730S12', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED730S13', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED730S13', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED730S2', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED730S2', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED730S3', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED730S3', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED730S4', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED730S4', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED730S5', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED730S5', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED730S6', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED730S6', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED730S7', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED730S7', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED730S8', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED730S8', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED730S9', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED730S9', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED731S0', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED731S0', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED731S1', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED731S1', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED731S10', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED731S10', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED731S11', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED731S11', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED731S2', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED731S2', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED731S3', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED731S3', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED731S4', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED731S4', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED731S5', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED731S5', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED731S6', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED731S6', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED731S7', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED731S7', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED731S8', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED731S8', 'description':''}])

hcallayout(dqmitems, 'SumQvsLS/DIGI/FEDSlot/FED731S9', [{'path':'/DigiTask/SumQvsLS/FEDSlot/FED731S9', 'description':''}])

hcallayout(dqmitems, 'Occupancy/DIGI/depth/depth1', [{'path':'/DigiTask/Occupancy/depth/depth1', 'description':''}])

hcallayout(dqmitems, 'Occupancy/DIGI/depth/depth2', [{'path':'/DigiTask/Occupancy/depth/depth2', 'description':''}])

hcallayout(dqmitems, 'Occupancy/DIGI/depth/depth3', [{'path':'/DigiTask/Occupancy/depth/depth3', 'description':''}])

hcallayout(dqmitems, 'Occupancy/DIGI/depth/depth4', [{'path':'/DigiTask/Occupancy/depth/depth4', 'description':''}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED1100', [{'path':'/DigiTask/OccupancyNR/FED/FED1100', 'description':''}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED1102', [{'path':'/DigiTask/OccupancyNR/FED/FED1102', 'description':''}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED1104', [{'path':'/DigiTask/OccupancyNR/FED/FED1104', 'description':''}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED1106', [{'path':'/DigiTask/OccupancyNR/FED/FED1106', 'description':''}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED1108', [{'path':'/DigiTask/OccupancyNR/FED/FED1108', 'description':''}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED1110', [{'path':'/DigiTask/OccupancyNR/FED/FED1110', 'description':''}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED1112', [{'path':'/DigiTask/OccupancyNR/FED/FED1112', 'description':''}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED1114', [{'path':'/DigiTask/OccupancyNR/FED/FED1114', 'description':''}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED1116', [{'path':'/DigiTask/OccupancyNR/FED/FED1116', 'description':''}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED1118', [{'path':'/DigiTask/OccupancyNR/FED/FED1118', 'description':''}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED1120', [{'path':'/DigiTask/OccupancyNR/FED/FED1120', 'description':''}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED1122', [{'path':'/DigiTask/OccupancyNR/FED/FED1122', 'description':''}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED1132', [{'path':'/DigiTask/OccupancyNR/FED/FED1132', 'description':''}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED724', [{'path':'/DigiTask/OccupancyNR/FED/FED724', 'description':''}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED725', [{'path':'/DigiTask/OccupancyNR/FED/FED725', 'description':''}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED726', [{'path':'/DigiTask/OccupancyNR/FED/FED726', 'description':''}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED727', [{'path':'/DigiTask/OccupancyNR/FED/FED727', 'description':''}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED728', [{'path':'/DigiTask/OccupancyNR/FED/FED728', 'description':''}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED729', [{'path':'/DigiTask/OccupancyNR/FED/FED729', 'description':''}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED730', [{'path':'/DigiTask/OccupancyNR/FED/FED730', 'description':''}])

hcallayout(dqmitems, 'OccupancyNR/DIGI/FED/FED731', [{'path':'/DigiTask/OccupancyNR/FED/FED731', 'description':''}])

hcallayout(dqmitems, 'EtEmul/TP', [{'path':'/TPTask/EtEmul/EtEmul', 'description':''}])

hcallayout(dqmitems, 'TimingvsEnergy/RECO/SubdetPM/HBM', [{'path':'/RecHitTask/TimingvsEnergy/SubdetPM/HBM', 'description':''}])

hcallayout(dqmitems, 'TimingvsEnergy/RECO/SubdetPM/HBP', [{'path':'/RecHitTask/TimingvsEnergy/SubdetPM/HBP', 'description':''}])

hcallayout(dqmitems, 'TimingvsEnergy/RECO/SubdetPM/HEM', [{'path':'/RecHitTask/TimingvsEnergy/SubdetPM/HEM', 'description':''}])

hcallayout(dqmitems, 'TimingvsEnergy/RECO/SubdetPM/HEP', [{'path':'/RecHitTask/TimingvsEnergy/SubdetPM/HEP', 'description':''}])

hcallayout(dqmitems, 'TimingvsEnergy/RECO/SubdetPM/HFM', [{'path':'/RecHitTask/TimingvsEnergy/SubdetPM/HFM', 'description':''}])

hcallayout(dqmitems, 'TimingvsEnergy/RECO/SubdetPM/HFP', [{'path':'/RecHitTask/TimingvsEnergy/SubdetPM/HFP', 'description':''}])

hcallayout(dqmitems, 'TimingvsEnergy/RECO/SubdetPM/HOM', [{'path':'/RecHitTask/TimingvsEnergy/SubdetPM/HOM', 'description':''}])

hcallayout(dqmitems, 'TimingvsEnergy/RECO/SubdetPM/HOP', [{'path':'/RecHitTask/TimingvsEnergy/SubdetPM/HOP', 'description':''}])

hcallayout(dqmitems, 'EtData/TP', [{'path':'/TPTask/EtData/EtData', 'description':''}])

hcallayout(dqmitems, 'EtCorr/TP/TTSubdet/HBHE', [{'path':'/TPTask/EtCorr/TTSubdet/HBHE', 'description':''}])

hcallayout(dqmitems, 'EtCorr/TP/TTSubdet/HF', [{'path':'/TPTask/EtCorr/TTSubdet/HF', 'description':''}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED1100', [{'path':'/RecHitTask/Energy/FED/FED1100', 'description':''}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED1102', [{'path':'/RecHitTask/Energy/FED/FED1102', 'description':''}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED1104', [{'path':'/RecHitTask/Energy/FED/FED1104', 'description':''}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED1106', [{'path':'/RecHitTask/Energy/FED/FED1106', 'description':''}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED1108', [{'path':'/RecHitTask/Energy/FED/FED1108', 'description':''}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED1110', [{'path':'/RecHitTask/Energy/FED/FED1110', 'description':''}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED1112', [{'path':'/RecHitTask/Energy/FED/FED1112', 'description':''}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED1114', [{'path':'/RecHitTask/Energy/FED/FED1114', 'description':''}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED1116', [{'path':'/RecHitTask/Energy/FED/FED1116', 'description':''}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED1118', [{'path':'/RecHitTask/Energy/FED/FED1118', 'description':''}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED1120', [{'path':'/RecHitTask/Energy/FED/FED1120', 'description':''}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED1122', [{'path':'/RecHitTask/Energy/FED/FED1122', 'description':''}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED1132', [{'path':'/RecHitTask/Energy/FED/FED1132', 'description':''}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED724', [{'path':'/RecHitTask/Energy/FED/FED724', 'description':''}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED725', [{'path':'/RecHitTask/Energy/FED/FED725', 'description':''}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED726', [{'path':'/RecHitTask/Energy/FED/FED726', 'description':''}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED727', [{'path':'/RecHitTask/Energy/FED/FED727', 'description':''}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED728', [{'path':'/RecHitTask/Energy/FED/FED728', 'description':''}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED729', [{'path':'/RecHitTask/Energy/FED/FED729', 'description':''}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED730', [{'path':'/RecHitTask/Energy/FED/FED730', 'description':''}])

hcallayout(dqmitems, 'Energy/RECO/FED/FED731', [{'path':'/RecHitTask/Energy/FED/FED731', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/Electronics/VME', [{'path':'/RecHitTask/TimingCut/Electronics/VME', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/Electronics/uTCA', [{'path':'/RecHitTask/TimingCut/Electronics/uTCA', 'description':''}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED1100', [{'path':'/DigiTask/DigiSize/FED/FED1100', 'description':''}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED1102', [{'path':'/DigiTask/DigiSize/FED/FED1102', 'description':''}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED1104', [{'path':'/DigiTask/DigiSize/FED/FED1104', 'description':''}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED1106', [{'path':'/DigiTask/DigiSize/FED/FED1106', 'description':''}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED1108', [{'path':'/DigiTask/DigiSize/FED/FED1108', 'description':''}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED1110', [{'path':'/DigiTask/DigiSize/FED/FED1110', 'description':''}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED1112', [{'path':'/DigiTask/DigiSize/FED/FED1112', 'description':''}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED1114', [{'path':'/DigiTask/DigiSize/FED/FED1114', 'description':''}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED1116', [{'path':'/DigiTask/DigiSize/FED/FED1116', 'description':''}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED1118', [{'path':'/DigiTask/DigiSize/FED/FED1118', 'description':''}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED1120', [{'path':'/DigiTask/DigiSize/FED/FED1120', 'description':''}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED1122', [{'path':'/DigiTask/DigiSize/FED/FED1122', 'description':''}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED1132', [{'path':'/DigiTask/DigiSize/FED/FED1132', 'description':''}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED724', [{'path':'/DigiTask/DigiSize/FED/FED724', 'description':''}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED725', [{'path':'/DigiTask/DigiSize/FED/FED725', 'description':''}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED726', [{'path':'/DigiTask/DigiSize/FED/FED726', 'description':''}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED727', [{'path':'/DigiTask/DigiSize/FED/FED727', 'description':''}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED728', [{'path':'/DigiTask/DigiSize/FED/FED728', 'description':''}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED729', [{'path':'/DigiTask/DigiSize/FED/FED729', 'description':''}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED730', [{'path':'/DigiTask/DigiSize/FED/FED730', 'description':''}])

hcallayout(dqmitems, 'DigiSize/DIGI/FED/FED731', [{'path':'/DigiTask/DigiSize/FED/FED731', 'description':''}])

hcallayout(dqmitems, 'OccupancyCutEmul/TP/Electronics/VME', [{'path':'/TPTask/OccupancyCutEmul/Electronics/VME', 'description':''}])

hcallayout(dqmitems, 'OccupancyCutEmul/TP/Electronics/uTCA', [{'path':'/TPTask/OccupancyCutEmul/Electronics/uTCA', 'description':''}])

hcallayout(dqmitems, 'FGCorr/TP/TTSubdet/HBHE', [{'path':'/TPTask/FGCorr/TTSubdet/HBHE', 'description':''}])

hcallayout(dqmitems, 'FGCorr/TP/TTSubdet/HF', [{'path':'/TPTask/FGCorr/TTSubdet/HF', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/HBHEPartition/HBHEa', [{'path':'/RecHitTask/TimingCut/HBHEPartition/HBHEa', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/HBHEPartition/HBHEb', [{'path':'/RecHitTask/TimingCut/HBHEPartition/HBHEb', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/HBHEPartition/HBHEc', [{'path':'/RecHitTask/TimingCut/HBHEPartition/HBHEc', 'description':''}])

hcallayout(dqmitems, 'ADC/DIGI/SubdetPM/HBM', [{'path':'/DigiTask/ADC/SubdetPM/HBM', 'description':''}])

hcallayout(dqmitems, 'ADC/DIGI/SubdetPM/HBP', [{'path':'/DigiTask/ADC/SubdetPM/HBP', 'description':''}])

hcallayout(dqmitems, 'ADC/DIGI/SubdetPM/HEM', [{'path':'/DigiTask/ADC/SubdetPM/HEM', 'description':''}])

hcallayout(dqmitems, 'ADC/DIGI/SubdetPM/HEP', [{'path':'/DigiTask/ADC/SubdetPM/HEP', 'description':''}])

hcallayout(dqmitems, 'ADC/DIGI/SubdetPM/HFM', [{'path':'/DigiTask/ADC/SubdetPM/HFM', 'description':''}])

hcallayout(dqmitems, 'ADC/DIGI/SubdetPM/HFP', [{'path':'/DigiTask/ADC/SubdetPM/HFP', 'description':''}])

hcallayout(dqmitems, 'ADC/DIGI/SubdetPM/HOM', [{'path':'/DigiTask/ADC/SubdetPM/HOM', 'description':''}])

hcallayout(dqmitems, 'ADC/DIGI/SubdetPM/HOP', [{'path':'/DigiTask/ADC/SubdetPM/HOP', 'description':''}])

hcallayout(dqmitems, 'EtCorrRatio/TP/Electronics/VME', [{'path':'/TPTask/EtCorrRatio/Electronics/VME', 'description':''}])

hcallayout(dqmitems, 'EtCorrRatio/TP/Electronics/uTCA', [{'path':'/TPTask/EtCorrRatio/Electronics/uTCA', 'description':''}])

hcallayout(dqmitems, 'OrnMsm/RAW/Electronics/VME', [{'path':'/RawTask/OrnMsm/Electronics/VME', 'description':'DESCDESC'}])

hcallayout(dqmitems, 'OrnMsm/RAW/Electronics/uTCA', [{'path':'/RawTask/OrnMsm/Electronics/uTCA', 'description':'DESCDESC'}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED1100', [{'path':'/DigiTask/Timing/FED/FED1100', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED1102', [{'path':'/DigiTask/Timing/FED/FED1102', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED1104', [{'path':'/DigiTask/Timing/FED/FED1104', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED1106', [{'path':'/DigiTask/Timing/FED/FED1106', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED1108', [{'path':'/DigiTask/Timing/FED/FED1108', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED1110', [{'path':'/DigiTask/Timing/FED/FED1110', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED1112', [{'path':'/DigiTask/Timing/FED/FED1112', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED1114', [{'path':'/DigiTask/Timing/FED/FED1114', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED1116', [{'path':'/DigiTask/Timing/FED/FED1116', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED1118', [{'path':'/DigiTask/Timing/FED/FED1118', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED1120', [{'path':'/DigiTask/Timing/FED/FED1120', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED1122', [{'path':'/DigiTask/Timing/FED/FED1122', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED1132', [{'path':'/DigiTask/Timing/FED/FED1132', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED724', [{'path':'/DigiTask/Timing/FED/FED724', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED725', [{'path':'/DigiTask/Timing/FED/FED725', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED726', [{'path':'/DigiTask/Timing/FED/FED726', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED727', [{'path':'/DigiTask/Timing/FED/FED727', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED728', [{'path':'/DigiTask/Timing/FED/FED728', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED729', [{'path':'/DigiTask/Timing/FED/FED729', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED730', [{'path':'/DigiTask/Timing/FED/FED730', 'description':''}])

hcallayout(dqmitems, 'Timing/DIGI/FED/FED731', [{'path':'/DigiTask/Timing/FED/FED731', 'description':''}])

hcallayout(dqmitems, 'MsnData/TP/Electronics/VME', [{'path':'/TPTask/MsnData/Electronics/VME', 'description':''}])

hcallayout(dqmitems, 'MsnData/TP/Electronics/uTCA', [{'path':'/TPTask/MsnData/Electronics/uTCA', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/depth/depth1', [{'path':'/DigiTask/OccupancyCut/depth/depth1', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/depth/depth2', [{'path':'/DigiTask/OccupancyCut/depth/depth2', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/depth/depth3', [{'path':'/DigiTask/OccupancyCut/depth/depth3', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/depth/depth4', [{'path':'/DigiTask/OccupancyCut/depth/depth4', 'description':''}])

hcallayout(dqmitems, 'Occupancy/DIGI/Electronics/VME', [{'path':'/DigiTask/Occupancy/Electronics/VME', 'description':''}])

hcallayout(dqmitems, 'Occupancy/DIGI/Electronics/uTCA', [{'path':'/DigiTask/Occupancy/Electronics/uTCA', 'description':''}])

hcallayout(dqmitems, 'fC/DIGI/SubdetPM/HBM', [{'path':'/DigiTask/fC/SubdetPM/HBM', 'description':''}])

hcallayout(dqmitems, 'fC/DIGI/SubdetPM/HBP', [{'path':'/DigiTask/fC/SubdetPM/HBP', 'description':''}])

hcallayout(dqmitems, 'fC/DIGI/SubdetPM/HEM', [{'path':'/DigiTask/fC/SubdetPM/HEM', 'description':''}])

hcallayout(dqmitems, 'fC/DIGI/SubdetPM/HEP', [{'path':'/DigiTask/fC/SubdetPM/HEP', 'description':''}])

hcallayout(dqmitems, 'fC/DIGI/SubdetPM/HFM', [{'path':'/DigiTask/fC/SubdetPM/HFM', 'description':''}])

hcallayout(dqmitems, 'fC/DIGI/SubdetPM/HFP', [{'path':'/DigiTask/fC/SubdetPM/HFP', 'description':''}])

hcallayout(dqmitems, 'fC/DIGI/SubdetPM/HOM', [{'path':'/DigiTask/fC/SubdetPM/HOM', 'description':''}])

hcallayout(dqmitems, 'fC/DIGI/SubdetPM/HOP', [{'path':'/DigiTask/fC/SubdetPM/HOP', 'description':''}])

hcallayout(dqmitems, 'BadQualityvsLS/RAW', [{'path':'/RawTask/BadQualityvsLS/BadQualityvsLS', 'description':'DESCDESC'}])

hcallayout(dqmitems, 'Occupancy/RECO/Electronics/VME', [{'path':'/RecHitTask/Occupancy/Electronics/VME', 'description':''}])

hcallayout(dqmitems, 'Occupancy/RECO/Electronics/uTCA', [{'path':'/RecHitTask/Occupancy/Electronics/uTCA', 'description':''}])

hcallayout(dqmitems, 'Energy/RECO/depth/depth1', [{'path':'/RecHitTask/Energy/depth/depth1', 'description':''}])

hcallayout(dqmitems, 'Energy/RECO/depth/depth2', [{'path':'/RecHitTask/Energy/depth/depth2', 'description':''}])

hcallayout(dqmitems, 'Energy/RECO/depth/depth3', [{'path':'/RecHitTask/Energy/depth/depth3', 'description':''}])

hcallayout(dqmitems, 'Energy/RECO/depth/depth4', [{'path':'/RecHitTask/Energy/depth/depth4', 'description':''}])

hcallayout(dqmitems, 'BadQuality/RAW/depth/depth1', [{'path':'/RawTask/BadQuality/depth/depth1', 'description':'DESCDESC'}])

hcallayout(dqmitems, 'BadQuality/RAW/depth/depth2', [{'path':'/RawTask/BadQuality/depth/depth2', 'description':'DESCDESC'}])

hcallayout(dqmitems, 'BadQuality/RAW/depth/depth3', [{'path':'/RawTask/BadQuality/depth/depth3', 'description':'DESCDESC'}])

hcallayout(dqmitems, 'BadQuality/RAW/depth/depth4', [{'path':'/RawTask/BadQuality/depth/depth4', 'description':'DESCDESC'}])

hcallayout(dqmitems, 'SumQ/DIGI/depth/depth1', [{'path':'/DigiTask/SumQ/depth/depth1', 'description':''}])

hcallayout(dqmitems, 'SumQ/DIGI/depth/depth2', [{'path':'/DigiTask/SumQ/depth/depth2', 'description':''}])

hcallayout(dqmitems, 'SumQ/DIGI/depth/depth3', [{'path':'/DigiTask/SumQ/depth/depth3', 'description':''}])

hcallayout(dqmitems, 'SumQ/DIGI/depth/depth4', [{'path':'/DigiTask/SumQ/depth/depth4', 'description':''}])

hcallayout(dqmitems, 'OccupancyData/TP', [{'path':'/TPTask/OccupancyData/OccupancyData', 'description':''}])

hcallayout(dqmitems, 'OccupancyData/TP/Electronics/VME', [{'path':'/TPTask/OccupancyData/Electronics/VME', 'description':''}])

hcallayout(dqmitems, 'OccupancyData/TP/Electronics/uTCA', [{'path':'/TPTask/OccupancyData/Electronics/uTCA', 'description':''}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED1100', [{'path':'/RawTask/BadQuality/FED/FED1100', 'description':'DESCDESC'}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED1102', [{'path':'/RawTask/BadQuality/FED/FED1102', 'description':'DESCDESC'}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED1104', [{'path':'/RawTask/BadQuality/FED/FED1104', 'description':'DESCDESC'}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED1106', [{'path':'/RawTask/BadQuality/FED/FED1106', 'description':'DESCDESC'}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED1108', [{'path':'/RawTask/BadQuality/FED/FED1108', 'description':'DESCDESC'}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED1110', [{'path':'/RawTask/BadQuality/FED/FED1110', 'description':'DESCDESC'}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED1112', [{'path':'/RawTask/BadQuality/FED/FED1112', 'description':'DESCDESC'}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED1114', [{'path':'/RawTask/BadQuality/FED/FED1114', 'description':'DESCDESC'}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED1116', [{'path':'/RawTask/BadQuality/FED/FED1116', 'description':'DESCDESC'}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED1118', [{'path':'/RawTask/BadQuality/FED/FED1118', 'description':'DESCDESC'}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED1120', [{'path':'/RawTask/BadQuality/FED/FED1120', 'description':'DESCDESC'}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED1122', [{'path':'/RawTask/BadQuality/FED/FED1122', 'description':'DESCDESC'}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED1132', [{'path':'/RawTask/BadQuality/FED/FED1132', 'description':'DESCDESC'}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED724', [{'path':'/RawTask/BadQuality/FED/FED724', 'description':'DESCDESC'}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED725', [{'path':'/RawTask/BadQuality/FED/FED725', 'description':'DESCDESC'}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED726', [{'path':'/RawTask/BadQuality/FED/FED726', 'description':'DESCDESC'}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED727', [{'path':'/RawTask/BadQuality/FED/FED727', 'description':'DESCDESC'}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED728', [{'path':'/RawTask/BadQuality/FED/FED728', 'description':'DESCDESC'}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED729', [{'path':'/RawTask/BadQuality/FED/FED729', 'description':'DESCDESC'}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED730', [{'path':'/RawTask/BadQuality/FED/FED730', 'description':'DESCDESC'}])

hcallayout(dqmitems, 'BadQuality/RAW/FED/FED731', [{'path':'/RawTask/BadQuality/FED/FED731', 'description':'DESCDESC'}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED1100', [{'path':'/DigiTask/OccupancyCut/FED/FED1100', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED1102', [{'path':'/DigiTask/OccupancyCut/FED/FED1102', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED1104', [{'path':'/DigiTask/OccupancyCut/FED/FED1104', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED1106', [{'path':'/DigiTask/OccupancyCut/FED/FED1106', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED1108', [{'path':'/DigiTask/OccupancyCut/FED/FED1108', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED1110', [{'path':'/DigiTask/OccupancyCut/FED/FED1110', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED1112', [{'path':'/DigiTask/OccupancyCut/FED/FED1112', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED1114', [{'path':'/DigiTask/OccupancyCut/FED/FED1114', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED1116', [{'path':'/DigiTask/OccupancyCut/FED/FED1116', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED1118', [{'path':'/DigiTask/OccupancyCut/FED/FED1118', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED1120', [{'path':'/DigiTask/OccupancyCut/FED/FED1120', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED1122', [{'path':'/DigiTask/OccupancyCut/FED/FED1122', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED1132', [{'path':'/DigiTask/OccupancyCut/FED/FED1132', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED724', [{'path':'/DigiTask/OccupancyCut/FED/FED724', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED725', [{'path':'/DigiTask/OccupancyCut/FED/FED725', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED726', [{'path':'/DigiTask/OccupancyCut/FED/FED726', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED727', [{'path':'/DigiTask/OccupancyCut/FED/FED727', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED728', [{'path':'/DigiTask/OccupancyCut/FED/FED728', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED729', [{'path':'/DigiTask/OccupancyCut/FED/FED729', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED730', [{'path':'/DigiTask/OccupancyCut/FED/FED730', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/DIGI/FED/FED731', [{'path':'/DigiTask/OccupancyCut/FED/FED731', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/RECO/depth/depth1', [{'path':'/RecHitTask/OccupancyCut/depth/depth1', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/RECO/depth/depth2', [{'path':'/RecHitTask/OccupancyCut/depth/depth2', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/RECO/depth/depth3', [{'path':'/RecHitTask/OccupancyCut/depth/depth3', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/RECO/depth/depth4', [{'path':'/RecHitTask/OccupancyCut/depth/depth4', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED1100', [{'path':'/RecHitTask/TimingCut/FED/FED1100', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED1102', [{'path':'/RecHitTask/TimingCut/FED/FED1102', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED1104', [{'path':'/RecHitTask/TimingCut/FED/FED1104', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED1106', [{'path':'/RecHitTask/TimingCut/FED/FED1106', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED1108', [{'path':'/RecHitTask/TimingCut/FED/FED1108', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED1110', [{'path':'/RecHitTask/TimingCut/FED/FED1110', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED1112', [{'path':'/RecHitTask/TimingCut/FED/FED1112', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED1114', [{'path':'/RecHitTask/TimingCut/FED/FED1114', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED1116', [{'path':'/RecHitTask/TimingCut/FED/FED1116', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED1118', [{'path':'/RecHitTask/TimingCut/FED/FED1118', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED1120', [{'path':'/RecHitTask/TimingCut/FED/FED1120', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED1122', [{'path':'/RecHitTask/TimingCut/FED/FED1122', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED1132', [{'path':'/RecHitTask/TimingCut/FED/FED1132', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED724', [{'path':'/RecHitTask/TimingCut/FED/FED724', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED725', [{'path':'/RecHitTask/TimingCut/FED/FED725', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED726', [{'path':'/RecHitTask/TimingCut/FED/FED726', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED727', [{'path':'/RecHitTask/TimingCut/FED/FED727', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED728', [{'path':'/RecHitTask/TimingCut/FED/FED728', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED729', [{'path':'/RecHitTask/TimingCut/FED/FED729', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED730', [{'path':'/RecHitTask/TimingCut/FED/FED730', 'description':''}])

hcallayout(dqmitems, 'TimingCut/RECO/FED/FED731', [{'path':'/RecHitTask/TimingCut/FED/FED731', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED1100', [{'path':'/RecHitTask/OccupancyCut/FED/FED1100', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED1102', [{'path':'/RecHitTask/OccupancyCut/FED/FED1102', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED1104', [{'path':'/RecHitTask/OccupancyCut/FED/FED1104', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED1106', [{'path':'/RecHitTask/OccupancyCut/FED/FED1106', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED1108', [{'path':'/RecHitTask/OccupancyCut/FED/FED1108', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED1110', [{'path':'/RecHitTask/OccupancyCut/FED/FED1110', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED1112', [{'path':'/RecHitTask/OccupancyCut/FED/FED1112', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED1114', [{'path':'/RecHitTask/OccupancyCut/FED/FED1114', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED1116', [{'path':'/RecHitTask/OccupancyCut/FED/FED1116', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED1118', [{'path':'/RecHitTask/OccupancyCut/FED/FED1118', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED1120', [{'path':'/RecHitTask/OccupancyCut/FED/FED1120', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED1122', [{'path':'/RecHitTask/OccupancyCut/FED/FED1122', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED1132', [{'path':'/RecHitTask/OccupancyCut/FED/FED1132', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED724', [{'path':'/RecHitTask/OccupancyCut/FED/FED724', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED725', [{'path':'/RecHitTask/OccupancyCut/FED/FED725', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED726', [{'path':'/RecHitTask/OccupancyCut/FED/FED726', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED727', [{'path':'/RecHitTask/OccupancyCut/FED/FED727', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED728', [{'path':'/RecHitTask/OccupancyCut/FED/FED728', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED729', [{'path':'/RecHitTask/OccupancyCut/FED/FED729', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED730', [{'path':'/RecHitTask/OccupancyCut/FED/FED730', 'description':''}])

hcallayout(dqmitems, 'OccupancyCut/RECO/FED/FED731', [{'path':'/RecHitTask/OccupancyCut/FED/FED731', 'description':''}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED1100', [{'path':'/DigiTask/CapId/FED/FED1100', 'description':''}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED1102', [{'path':'/DigiTask/CapId/FED/FED1102', 'description':''}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED1104', [{'path':'/DigiTask/CapId/FED/FED1104', 'description':''}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED1106', [{'path':'/DigiTask/CapId/FED/FED1106', 'description':''}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED1108', [{'path':'/DigiTask/CapId/FED/FED1108', 'description':''}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED1110', [{'path':'/DigiTask/CapId/FED/FED1110', 'description':''}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED1112', [{'path':'/DigiTask/CapId/FED/FED1112', 'description':''}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED1114', [{'path':'/DigiTask/CapId/FED/FED1114', 'description':''}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED1116', [{'path':'/DigiTask/CapId/FED/FED1116', 'description':''}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED1118', [{'path':'/DigiTask/CapId/FED/FED1118', 'description':''}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED1120', [{'path':'/DigiTask/CapId/FED/FED1120', 'description':''}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED1122', [{'path':'/DigiTask/CapId/FED/FED1122', 'description':''}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED1132', [{'path':'/DigiTask/CapId/FED/FED1132', 'description':''}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED724', [{'path':'/DigiTask/CapId/FED/FED724', 'description':''}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED725', [{'path':'/DigiTask/CapId/FED/FED725', 'description':''}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED726', [{'path':'/DigiTask/CapId/FED/FED726', 'description':''}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED727', [{'path':'/DigiTask/CapId/FED/FED727', 'description':''}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED728', [{'path':'/DigiTask/CapId/FED/FED728', 'description':''}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED729', [{'path':'/DigiTask/CapId/FED/FED729', 'description':''}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED730', [{'path':'/DigiTask/CapId/FED/FED730', 'description':''}])

hcallayout(dqmitems, 'CapId/DIGI/FED/FED731', [{'path':'/DigiTask/CapId/FED/FED731', 'description':''}])

hcallayout(dqmitems, 'EtMsm/TP', [{'path':'/TPTask/EtMsm/EtMsm', 'description':''}])

hcallayout(dqmitems, 'OccupancyvsLS/RECO/Subdet/HB', [{'path':'/RecHitTask/OccupancyvsLS/Subdet/HB', 'description':''}])

hcallayout(dqmitems, 'OccupancyvsLS/RECO/Subdet/HE', [{'path':'/RecHitTask/OccupancyvsLS/Subdet/HE', 'description':''}])

hcallayout(dqmitems, 'OccupancyvsLS/RECO/Subdet/HF', [{'path':'/RecHitTask/OccupancyvsLS/Subdet/HF', 'description':''}])

hcallayout(dqmitems, 'OccupancyvsLS/RECO/Subdet/HO', [{'path':'/RecHitTask/OccupancyvsLS/Subdet/HO', 'description':''}])

hcallayout(dqmitems, 'Occupancy/RAW/Electronics/VME', [{'path':'/RawTask/Occupancy/Electronics/VME', 'description':''}])

hcallayout(dqmitems, 'Occupancy/RAW/Electronics/uTCA', [{'path':'/RawTask/Occupancy/Electronics/uTCA', 'description':''}])

hcallayout(dqmitems, 'MsnEmul/TP/Electronics/VME', [{'path':'/TPTask/MsnEmul/Electronics/VME', 'description':''}])

hcallayout(dqmitems, 'MsnEmul/TP/Electronics/uTCA', [{'path':'/TPTask/MsnEmul/Electronics/uTCA', 'description':''}])

hcallayout(dqmitems, 'MsnData/TP', [{'path':'/TPTask/MsnData/MsnData', 'description':''}])

hcallayout(dqmitems, 'Current Summary', [{'path':'/TPTask/Summary/Summary', 'description':''}, {'path':'/RawTask/Summary/Summary', 'description':''}], [{'path':'/RecHitTask/Summary/Summary', 'description':''}, {'path':'/DigiTask/Summary/Summary', 'description':''}])

hcallayout(dqmitems, 'RAW Bad Quality', [{'path':'/RawTask/BadQualityvsBX/BadQualityvsBX', 'description':'DESCDESC'}, {'path':'/RawTask/BadQualityvsLS/BadQualityvsLS', 'description':'DESCDESC'}])

hcallayout(dqmitems, 'RAW Bad Quality by FED', [{'path':'/RawTask/BadQuality/FED/FED1100', 'description':'DESCDESC'}, {'path':'/RawTask/BadQuality/FED/FED1102', 'description':'DESCDESC'}, {'path':'/RawTask/BadQuality/FED/FED1104', 'description':'DESCDESC'}, {'path':'/RawTask/BadQuality/FED/FED1106', 'description':'DESCDESC'}, {'path':'/RawTask/BadQuality/FED/FED1108', 'description':'DESCDESC'}], [{'path':'/RawTask/BadQuality/FED/FED1110', 'description':'DESCDESC'}, {'path':'/RawTask/BadQuality/FED/FED1112', 'description':'DESCDESC'}, {'path':'/RawTask/BadQuality/FED/FED1114', 'description':'DESCDESC'}, {'path':'/RawTask/BadQuality/FED/FED1116', 'description':'DESCDESC'}, {'path':'/RawTask/BadQuality/FED/FED1118', 'description':'DESCDESC'}], [{'path':'/RawTask/BadQuality/FED/FED1120', 'description':'DESCDESC'}, {'path':'/RawTask/BadQuality/FED/FED1122', 'description':'DESCDESC'}, {'path':'/RawTask/BadQuality/FED/FED1132', 'description':'DESCDESC'}, {'path':'/RawTask/BadQuality/FED/FED724', 'description':'DESCDESC'}, {'path':'/RawTask/BadQuality/FED/FED725', 'description':'DESCDESC'}], [{'path':'/RawTask/BadQuality/FED/FED726', 'description':'DESCDESC'}, {'path':'/RawTask/BadQuality/FED/FED727', 'description':'DESCDESC'}, {'path':'/RawTask/BadQuality/FED/FED728', 'description':'DESCDESC'}, {'path':'/RawTask/BadQuality/FED/FED729', 'description':'DESCDESC'}, {'path':'/RawTask/BadQuality/FED/FED730', 'description':'DESCDESC'}], [{'path':'/RawTask/BadQuality/FED/FED731', 'description':'DESCDESC'}])

hcallayout(dqmitems, 'RAW BX Mismatches', [{'path':'/RawTask/BcnMsm/Electronics/VME', 'description':'DESC<a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription">Description</a>'}, {'path':'/RawTask/BcnMsm/Electronics/uTCA', 'description':'DESC<a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription">Description</a>'}])

hcallayout(dqmitems, 'RAW EvN Mismatches', [{'path':'/RawTask/EvnMsm/Electronics/VME', 'description':'DESC<a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription">Description</a>'}, {'path':'/RawTask/EvnMsm/Electronics/uTCA', 'description':'DESC<a href="https://twiki.cern.ch/twiki/bin/view/CMS/HcalDQMRun2TaskDescription">Description</a>'}])

hcallayout(dqmitems, 'DIGI Missing 1LS', [{'path':'/DigiTask/Missing1LS/FED/FED1100', 'description':''}, {'path':'/DigiTask/Missing1LS/FED/FED1102', 'description':''}, {'path':'/DigiTask/Missing1LS/FED/FED1104', 'description':''}, {'path':'/DigiTask/Missing1LS/FED/FED1106', 'description':''}, {'path':'/DigiTask/Missing1LS/FED/FED1108', 'description':''}], [{'path':'/DigiTask/Missing1LS/FED/FED1110', 'description':''}, {'path':'/DigiTask/Missing1LS/FED/FED1112', 'description':''}, {'path':'/DigiTask/Missing1LS/FED/FED1114', 'description':''}, {'path':'/DigiTask/Missing1LS/FED/FED1116', 'description':''}, {'path':'/DigiTask/Missing1LS/FED/FED1118', 'description':''}], [{'path':'/DigiTask/Missing1LS/FED/FED1120', 'description':''}, {'path':'/DigiTask/Missing1LS/FED/FED1122', 'description':''}, {'path':'/DigiTask/Missing1LS/FED/FED1132', 'description':''}, {'path':'/DigiTask/Missing1LS/FED/FED724', 'description':''}, {'path':'/DigiTask/Missing1LS/FED/FED725', 'description':''}], [{'path':'/DigiTask/Missing1LS/FED/FED726', 'description':''}, {'path':'/DigiTask/Missing1LS/FED/FED727', 'description':''}, {'path':'/DigiTask/Missing1LS/FED/FED728', 'description':''}, {'path':'/DigiTask/Missing1LS/FED/FED729', 'description':''}, {'path':'/DigiTask/Missing1LS/FED/FED730', 'description':''}], [{'path':'/DigiTask/Missing1LS/FED/FED731', 'description':''}])

hcallayout(dqmitems, 'DIGI Occupancy', [{'path':'/DigiTask/Occupancy/FED/FED1100', 'description':''}, {'path':'/DigiTask/Occupancy/FED/FED1102', 'description':''}, {'path':'/DigiTask/Occupancy/FED/FED1104', 'description':''}, {'path':'/DigiTask/Occupancy/FED/FED1106', 'description':''}, {'path':'/DigiTask/Occupancy/FED/FED1108', 'description':''}], [{'path':'/DigiTask/Occupancy/FED/FED1110', 'description':''}, {'path':'/DigiTask/Occupancy/FED/FED1112', 'description':''}, {'path':'/DigiTask/Occupancy/FED/FED1114', 'description':''}, {'path':'/DigiTask/Occupancy/FED/FED1116', 'description':''}, {'path':'/DigiTask/Occupancy/FED/FED1118', 'description':''}], [{'path':'/DigiTask/Occupancy/FED/FED1120', 'description':''}, {'path':'/DigiTask/Occupancy/FED/FED1122', 'description':''}, {'path':'/DigiTask/Occupancy/FED/FED1132', 'description':''}, {'path':'/DigiTask/Occupancy/FED/FED724', 'description':''}, {'path':'/DigiTask/Occupancy/FED/FED725', 'description':''}], [{'path':'/DigiTask/Occupancy/FED/FED726', 'description':''}, {'path':'/DigiTask/Occupancy/FED/FED727', 'description':''}, {'path':'/DigiTask/Occupancy/FED/FED728', 'description':''}, {'path':'/DigiTask/Occupancy/FED/FED729', 'description':''}, {'path':'/DigiTask/Occupancy/FED/FED730', 'description':''}], [{'path':'/DigiTask/Occupancy/FED/FED731', 'description':''}])

hcallayout(dqmitems, 'DIGI Occupancy Total', [{'path':'/DigiTask/OccupancyNR/FED/FED1100', 'description':''}, {'path':'/DigiTask/OccupancyNR/FED/FED1102', 'description':''}, {'path':'/DigiTask/OccupancyNR/FED/FED1104', 'description':''}, {'path':'/DigiTask/OccupancyNR/FED/FED1106', 'description':''}, {'path':'/DigiTask/OccupancyNR/FED/FED1108', 'description':''}], [{'path':'/DigiTask/OccupancyNR/FED/FED1110', 'description':''}, {'path':'/DigiTask/OccupancyNR/FED/FED1112', 'description':''}, {'path':'/DigiTask/OccupancyNR/FED/FED1114', 'description':''}, {'path':'/DigiTask/OccupancyNR/FED/FED1116', 'description':''}, {'path':'/DigiTask/OccupancyNR/FED/FED1118', 'description':''}], [{'path':'/DigiTask/OccupancyNR/FED/FED1120', 'description':''}, {'path':'/DigiTask/OccupancyNR/FED/FED1122', 'description':''}, {'path':'/DigiTask/OccupancyNR/FED/FED1132', 'description':''}, {'path':'/DigiTask/OccupancyNR/FED/FED724', 'description':''}, {'path':'/DigiTask/OccupancyNR/FED/FED725', 'description':''}], [{'path':'/DigiTask/OccupancyNR/FED/FED726', 'description':''}, {'path':'/DigiTask/OccupancyNR/FED/FED727', 'description':''}, {'path':'/DigiTask/OccupancyNR/FED/FED728', 'description':''}, {'path':'/DigiTask/OccupancyNR/FED/FED729', 'description':''}, {'path':'/DigiTask/OccupancyNR/FED/FED730', 'description':''}], [{'path':'/DigiTask/OccupancyNR/FED/FED731', 'description':''}])

hcallayout(dqmitems, 'DIGI Occupancy Cut', [{'path':'/DigiTask/OccupancyCut/FED/FED1100', 'description':''}, {'path':'/DigiTask/OccupancyCut/FED/FED1102', 'description':''}, {'path':'/DigiTask/OccupancyCut/FED/FED1104', 'description':''}, {'path':'/DigiTask/OccupancyCut/FED/FED1106', 'description':''}, {'path':'/DigiTask/OccupancyCut/FED/FED1108', 'description':''}], [{'path':'/DigiTask/OccupancyCut/FED/FED1110', 'description':''}, {'path':'/DigiTask/OccupancyCut/FED/FED1112', 'description':''}, {'path':'/DigiTask/OccupancyCut/FED/FED1114', 'description':''}, {'path':'/DigiTask/OccupancyCut/FED/FED1116', 'description':''}, {'path':'/DigiTask/OccupancyCut/FED/FED1118', 'description':''}], [{'path':'/DigiTask/OccupancyCut/FED/FED1120', 'description':''}, {'path':'/DigiTask/OccupancyCut/FED/FED1122', 'description':''}, {'path':'/DigiTask/OccupancyCut/FED/FED1132', 'description':''}, {'path':'/DigiTask/OccupancyCut/FED/FED724', 'description':''}, {'path':'/DigiTask/OccupancyCut/FED/FED725', 'description':''}], [{'path':'/DigiTask/OccupancyCut/FED/FED726', 'description':''}, {'path':'/DigiTask/OccupancyCut/FED/FED727', 'description':''}, {'path':'/DigiTask/OccupancyCut/FED/FED728', 'description':''}, {'path':'/DigiTask/OccupancyCut/FED/FED729', 'description':''}, {'path':'/DigiTask/OccupancyCut/FED/FED730', 'description':''}], [{'path':'/DigiTask/OccupancyCut/FED/FED731', 'description':''}])

hcallayout(dqmitems, 'DIGI Timing', [{'path':'/DigiTask/Timing/FED/FED1100', 'description':''}, {'path':'/DigiTask/Timing/FED/FED1102', 'description':''}, {'path':'/DigiTask/Timing/FED/FED1104', 'description':''}, {'path':'/DigiTask/Timing/FED/FED1106', 'description':''}, {'path':'/DigiTask/Timing/FED/FED1108', 'description':''}], [{'path':'/DigiTask/Timing/FED/FED1110', 'description':''}, {'path':'/DigiTask/Timing/FED/FED1112', 'description':''}, {'path':'/DigiTask/Timing/FED/FED1114', 'description':''}, {'path':'/DigiTask/Timing/FED/FED1116', 'description':''}, {'path':'/DigiTask/Timing/FED/FED1118', 'description':''}], [{'path':'/DigiTask/Timing/FED/FED1120', 'description':''}, {'path':'/DigiTask/Timing/FED/FED1122', 'description':''}, {'path':'/DigiTask/Timing/FED/FED1132', 'description':''}, {'path':'/DigiTask/Timing/FED/FED724', 'description':''}, {'path':'/DigiTask/Timing/FED/FED725', 'description':''}], [{'path':'/DigiTask/Timing/FED/FED726', 'description':''}, {'path':'/DigiTask/Timing/FED/FED727', 'description':''}, {'path':'/DigiTask/Timing/FED/FED728', 'description':''}, {'path':'/DigiTask/Timing/FED/FED729', 'description':''}, {'path':'/DigiTask/Timing/FED/FED730', 'description':''}], [{'path':'/DigiTask/Timing/FED/FED731', 'description':''}])

hcallayout(dqmitems, 'DIGI Total Charge', [{'path':'/DigiTask/SumQ/SubdetPM/HBM', 'description':''}, {'path':'/DigiTask/SumQ/SubdetPM/HBP', 'description':''}, {'path':'/DigiTask/SumQ/SubdetPM/HEM', 'description':''}], [{'path':'/DigiTask/SumQ/SubdetPM/HEP', 'description':''}, {'path':'/DigiTask/SumQ/SubdetPM/HFM', 'description':''}, {'path':'/DigiTask/SumQ/SubdetPM/HFP', 'description':''}], [{'path':'/DigiTask/SumQ/SubdetPM/HOM', 'description':''}, {'path':'/DigiTask/SumQ/SubdetPM/HOP', 'description':''}])

hcallayout(dqmitems, 'DIGI Occupancy vs LS', [{'path':'/DigiTask/OccupancyvsLS/Subdet/HB', 'description':''}, {'path':'/DigiTask/OccupancyvsLS/Subdet/HE', 'description':''}], [{'path':'/DigiTask/OccupancyvsLS/Subdet/HF', 'description':''}, {'path':'/DigiTask/OccupancyvsLS/Subdet/HO', 'description':''}])

hcallayout(dqmitems, 'RECO Energy by Subdet', [{'path':'/RecHitTask/Energy/Subdet/HB', 'description':''}, {'path':'/RecHitTask/Energy/Subdet/HE', 'description':''}], [{'path':'/RecHitTask/Energy/Subdet/HF', 'description':''}, {'path':'/RecHitTask/Energy/Subdet/HO', 'description':''}])

hcallayout(dqmitems, 'RECO Energy by depth', [{'path':'/RecHitTask/Energy/depth/depth1', 'description':''}, {'path':'/RecHitTask/Energy/depth/depth2', 'description':''}], [{'path':'/RecHitTask/Energy/depth/depth3', 'description':''}, {'path':'/RecHitTask/Energy/depth/depth4', 'description':''}])

hcallayout(dqmitems, 'RECO Timing FED', [{'path':'/RecHitTask/TimingCut/FED/FED1100', 'description':''}, {'path':'/RecHitTask/TimingCut/FED/FED1102', 'description':''}, {'path':'/RecHitTask/TimingCut/FED/FED1104', 'description':''}, {'path':'/RecHitTask/TimingCut/FED/FED1106', 'description':''}, {'path':'/RecHitTask/TimingCut/FED/FED1108', 'description':''}], [{'path':'/RecHitTask/TimingCut/FED/FED1110', 'description':''}, {'path':'/RecHitTask/TimingCut/FED/FED1112', 'description':''}, {'path':'/RecHitTask/TimingCut/FED/FED1114', 'description':''}, {'path':'/RecHitTask/TimingCut/FED/FED1116', 'description':''}, {'path':'/RecHitTask/TimingCut/FED/FED1118', 'description':''}], [{'path':'/RecHitTask/TimingCut/FED/FED1120', 'description':''}, {'path':'/RecHitTask/TimingCut/FED/FED1122', 'description':''}, {'path':'/RecHitTask/TimingCut/FED/FED1132', 'description':''}, {'path':'/RecHitTask/TimingCut/FED/FED724', 'description':''}, {'path':'/RecHitTask/TimingCut/FED/FED725', 'description':''}], [{'path':'/RecHitTask/TimingCut/FED/FED726', 'description':''}, {'path':'/RecHitTask/TimingCut/FED/FED727', 'description':''}, {'path':'/RecHitTask/TimingCut/FED/FED728', 'description':''}, {'path':'/RecHitTask/TimingCut/FED/FED729', 'description':''}, {'path':'/RecHitTask/TimingCut/FED/FED730', 'description':''}], [{'path':'/RecHitTask/TimingCut/FED/FED731', 'description':''}])

hcallayout(dqmitems, 'RECO Timing depth', [{'path':'/RecHitTask/TimingCut/depth/depth1', 'description':''}, {'path':'/RecHitTask/TimingCut/depth/depth2', 'description':''}], [{'path':'/RecHitTask/TimingCut/depth/depth3', 'description':''}, {'path':'/RecHitTask/TimingCut/depth/depth4', 'description':''}])

hcallayout(dqmitems, 'RECO HBHEabc Timing', [{'path':'/RecHitTask/TimingCut/HBHEPartition/HBHEa', 'description':''}, {'path':'/RecHitTask/TimingCut/HBHEPartition/HBHEb', 'description':''}], [{'path':'/RecHitTask/TimingCut/HBHEPartition/HBHEc', 'description':''}])

hcallayout(dqmitems, 'RECO Timing vs Energy', [{'path':'/RecHitTask/TimingvsEnergy/SubdetPM/HBM', 'description':''}, {'path':'/RecHitTask/TimingvsEnergy/SubdetPM/HBP', 'description':''}, {'path':'/RecHitTask/TimingvsEnergy/SubdetPM/HEM', 'description':''}], [{'path':'/RecHitTask/TimingvsEnergy/SubdetPM/HEP', 'description':''}, {'path':'/RecHitTask/TimingvsEnergy/SubdetPM/HFM', 'description':''}, {'path':'/RecHitTask/TimingvsEnergy/SubdetPM/HFP', 'description':''}], [{'path':'/RecHitTask/TimingvsEnergy/SubdetPM/HOM', 'description':''}, {'path':'/RecHitTask/TimingvsEnergy/SubdetPM/HOP', 'description':''}])

hcallayout(dqmitems, 'TP Et Correlation', [{'path':'/TPTask/EtCorr/TTSubdet/HBHE', 'description':''}, {'path':'/TPTask/EtCorr/TTSubdet/HF', 'description':''}])

hcallayout(dqmitems, 'TP Et Distribution', [{'path':'/TPTask/EtData/TTSubdet/HBHE', 'description':''}, {'path':'/TPTask/EtData/TTSubdet/HF', 'description':''}, {'path':'/TPTask/EtData/Electronics/VME', 'description':''}, {'path':'/TPTask/EtData/Electronics/uTCA', 'description':''}], [{'path':'/TPTask/EtData/EtData', 'description':''}, {'path':'/TPTask/EtEmul/TTSubdet/HBHE', 'description':''}, {'path':'/TPTask/EtEmul/TTSubdet/HF', 'description':''}, {'path':'/TPTask/EtEmul/Electronics/VME', 'description':''}], [{'path':'/TPTask/EtEmul/Electronics/uTCA', 'description':''}, {'path':'/TPTask/EtEmul/EtEmul', 'description':''}])

hcallayout(dqmitems, 'TP Et Mismatches', [{'path':'/TPTask/EtMsm/Electronics/VME', 'description':''}, {'path':'/TPTask/EtMsm/Electronics/uTCA', 'description':''}], [{'path':'/TPTask/EtMsm/EtMsm', 'description':''}])

hcallayout(dqmitems, 'TP Et Missing', [{'path':'/TPTask/MsnData/Electronics/VME', 'description':''}, {'path':'/TPTask/MsnData/Electronics/uTCA', 'description':''}, {'path':'/TPTask/MsnData/MsnData', 'description':''}], [{'path':'/TPTask/MsnEmul/MsnEmul', 'description':''}, {'path':'/TPTask/MsnEmul/Electronics/VME', 'description':''}, {'path':'/TPTask/MsnEmul/Electronics/uTCA', 'description':''}])

hcallayout(dqmitems, 'TP Et Occupancy', [{'path':'/TPTask/OccupancyData/OccupancyData', 'description':''}, {'path':'/TPTask/OccupancyData/Electronics/VME', 'description':''}, {'path':'/TPTask/OccupancyData/Electronics/uTCA', 'description':''}], [{'path':'/TPTask/OccupancyEmul/Electronics/VME', 'description':''}, {'path':'/TPTask/OccupancyEmul/Electronics/uTCA', 'description':''}, {'path':'/TPTask/OccupancyEmul/OccupancyEmul', 'description':''}])
