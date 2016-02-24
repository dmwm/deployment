# Dummy check of python syntax within file when run stand-alone
if __name__=="__main__":
    class DQMItem:
        def __init__(self,layout):
            print layout

    dqmitems={}

def shifthcallayout(i, p, *rows): i["00 Shift/Hcal/" + p] = DQMItem(layout=rows)

# Report Summary Map
shifthcallayout(dqmitems, '01 HCAL  Summary', [{'path' : 'Hcal/RawTask/Summary/Summary', 'description' : 'HCAL RAW Format Summary per FED'},{'path' : 'Hcal/RecHitTask/Summary/Summary', 'description' : 'HCAL REC HIT Format Summary per SubDetetor'}],[{'path' : 'Hcal/DigiTask/Summary/Summary', 'description' : 'HCAL DIGI Format Summary per SubDetetor'},{'path' : 'Hcal/TPTask/Summary/Summary', 'description' : 'HCAL Trigger Primitive Format Summary per SubDetetor'}])

shifthcallayout(dqmitems, '02 HCAL DIGI Occupancy vs LS', [{'path' : 'Hcal/DigiTask/Occupancy/vsLS_SubDet/OccupancyvsLS_HB', 'description' : 'HB Occupancy vs LS'},{'path' : 'Hcal/DigiTask/Occupancy/vsLS_SubDet/OccupancyvsLS_HE', 'description' : 'HE Occupancy vs LS'}],[{'path' : 'Hcal/DigiTask/Occupancy/vsLS_SubDet/OccupancyvsLS_HF', 'description' : 'HF Occupancy vs LS'},{'path' : 'Hcal/DigiTask/Occupancy/vsLS_SubDet/OccupancyvsLS_HO', 'description' : 'HO Occupancy vs LS'}])

shifthcallayout(dqmitems, '03 HCAL DIGI Missing Channels per 1LS', [{'path' : 'Hcal/DigiTask/Missing/1LS_depth/Missing_Depth1', 'description' : 'Depth 1 Missing channels per 1LS. Updated each 10LS'},{'path' : 'Hcal/DigiTask/Missing/1LS_depth/Missing_Depth2', 'description' : 'Depth 2 Missing channels per 1LS. Updated each 10LS'}],[{'path' : 'Hcal/DigiTask/Missing/1LS_depth/Missing_Depth3', 'description' : 'Depth 3 Missing channels per 1LS. Updated each 10LS'},{'path' : 'Hcal/DigiTask/Missing/1LS_depth/Missing_Depth4', 'description' : 'Depth 4 Missing channels per 1LS. Updated each 10LS'}])

shifthcallayout(dqmitems, '04 HCAL DIGI Missing Channels per 1LS vs LS', [{'path' : 'Hcal/DigiTask/Missing/1LSvsLS_SubDet/Missing_HB', 'description' : 'Number of HB missing channels per 1LS.'},{'path' : 'Hcal/DigiTask/Missing/1LSvsLS_SubDet/Missing_HE', 'description' : 'Number of HE missing channels per 1LS.'}],[{'path' : 'Hcal/DigiTask/Missing/1LSvsLS_SubDet/Missing_HF', 'description' : 'Number of HF missing channels per 1LS.'},{'path' : 'Hcal/DigiTask/Missing/1LSvsLS_SubDet/Missing_HO', 'description' : 'Number of HO missing channels per 1LS.'}])

shifthcallayout(dqmitems, '06 HCAL RECHIT Timing 2D', [{'path' : 'Hcal/RecHitTask/Timing/depth_EHBHE5HO5HF5/Timing_Depth1', 'description' : 'Depth 1 Timing.'},{'path' : 'Hcal/RecHitTask/Timing/depth_EHBHE5HO5HF5/Timing_Depth2', 'description' : 'Depth 2 Timing.'}],[{'path' : 'Hcal/RecHitTask/Timing/depth_EHBHE5HO5HF5/Timing_Depth3', 'description' : 'Depth 3 Timing.'},{'path' : 'Hcal/RecHitTask/Timing/depth_EHBHE5HO5HF5/Timing_Depth4', 'description' : 'Depth 4 Timing.'}])
