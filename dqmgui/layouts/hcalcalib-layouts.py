# Dummy check of python syntax within file when run stand-alone
if __name__=="__main__":
    class DQMItem:
        def __init__(self,layout):
            print layout

    dqmitems={}

def hcalcaliblayout(i, p, *rows): i["HcalCalib/Layouts/" + p] = DQMItem(layout=rows)

hcalcaliblayout(dqmitems, "01 HCAL PEDESTAL MEANs",
	[
		{
			'path' : "HcalCalib/PedestalTask/Means/SubDet/HB",
			'description' : "Means"
		},
		{
			'path' : "HcalCalib/PedestalTask/Means/SubDet/HE",
			'description' : "Means"
		}
	],
	[
		{
			'path' : "HcalCalib/PedestalTask/Means/SubDet/HO",
			'description' : "Means"
		},
		{
			'path' : "HcalCalib/PedestalTask/Means/SubDet/HF",
			'description' : "Means"
		}
	]
)
hcalcaliblayout(dqmitems, "02 HCAL PEDESTAL RMSs",
	[
		{
			'path' : "HcalCalib/PedestalTask/PedestalRMSs/SubDet/HB",
			'description' : "RMSs"
		},
		{
			'path' : "HcalCalib/PedestalTask/PedestalRMSs/SubDet/HE",
			'description' : "RMSs"
		}
	],
	[
		{
			'path' : "HcalCalib/PedestalTask/PedestalRMSs/SubDet/HO",
			'description' : "RMSs"
		},
		{
			'path' : "HcalCalib/PedestalTask/PedestalRMSs/SubDet/HF",
			'description' : "RMSs"
		}
	]
)
hcalcaliblayout(dqmitems, "03 HCAL PEDESTAL MEANs 2D",
	[
		{
			'path' : "HcalCalib/PedestalTask/PedestalMeans/depth/depth1",
			'description' : "Means"
		},
		{
			'path' : "HcalCalib/PedestalTask/PedestalMeans/depth/depth2",
			'description' : "Means"
		}
	],
	[
		{
			'path' : "HcalCalib/PedestalTask/PedestalMeans/depth/depth3",
			'description' : "Means"
		},
		{
			'path' : "HcalCalib/PedestalTask/PedestalMeans/depth/depth4",
			'description' : "Means"
		}
	]
)
hcalcaliblayout(dqmitems, "01 HCAL PEDESTAL RMSs",
	[
		{
			'path' : "HcalCalib/PedestalTask/PedestalRMSs/depth/depth1",
			'description' : "RMSs"
		},
		{
			'path' : "HcalCalib/PedestalTask/PedestalRMSs/depth/depth2",
			'description' : "RMSs"
		}
	],
	[
		{
			'path' : "HcalCalib/PedestalTask/PedestalRMSs/depth/depth3",
			'description' : "RMSs"
		},
		{
			'path' : "HcalCalib/PedestalTask/PedestalRMSs/depth/depth4",
			'description' : "RMSs"
		}
	]
)
