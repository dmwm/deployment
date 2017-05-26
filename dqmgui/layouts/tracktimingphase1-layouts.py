def pixellayout(i, p, *rows): i["TrackTimingPixelPhase1/Layouts/" + p] = DQMItem(layout=rows)


### Digis
pixellayout(dqmitems, "01a - Digi_Barrel",
   [{ 'path': "TrackTimingPixelPhase1/Phase1_MechanicalView/num_digis_per_OnlineBlock_PXBarrel",
      'description': "Number of digis",
      'draw': { 'withref': "no" }}
      ] )
pixellayout(dqmitems, "01b - Digi_Forward",
   [{ 'path': "TrackTimingPixelPhase1/Phase1_MechanicalView/num_digis_per_OnlineBlock_PXForward",
      'description': "Number of digis",
      'draw': { 'withref': "no" }}] )

### ADC
pixellayout(dqmitems, "02a - ADC_Barrel",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_MechanicalView/adc_per_OnlineBlock_PXBarrel",
      'description': "Mean adc value",
      'draw': { 'withref': "no" }}])
pixellayout(dqmitems, "02b - ADC_Forward",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_MechanicalView/adc_per_OnlineBlock_PXForward",
      'description': "Mean adc value",
      'draw': { 'withref': "no" }}])

pixellayout(dqmitems, "03a - Num_Cluster_Barrel",
   [{ 'path': "TrackTimingPixelPhase1/Phase1_MechanicalView/num_clusters_per_OnlineBlock_PXBarrel",
      'description': "Number of clusters",
      'draw': { 'withref': "no" }}] )
pixellayout(dqmitems, "03b - Num_Cluster_Forward",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_MechanicalView/num_clusters_per_OnlineBlock_PXForward",
      'description': "Number of clusters",
      'draw': { 'withref': "no" }}])

### Cluster Charge
pixellayout(dqmitems, "04a - Cluster_Charge_Barrel",
  [{ 'path': "TrackTimingPixelPhase1/Phase1_MechanicalView/charge_per_OnlineBlock_PXBarrel",
      'description': "Mean cluster charge",
      'draw': { 'withref': "no" }} ] )
pixellayout(dqmitems, "04b - Cluster_Charge_Forward",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_MechanicalView/charge_per_OnlineBlock_PXForward",
      'description': "Mean cluster charge",
      'draw': { 'withref': "no" }}] )

### Size
pixellayout(dqmitems, "05a - Cluster_Size_Barrel",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_MechanicalView/size_per_OnlineBlock_PXBarrel",
      'description': "Mean cluster size",
      'draw': { 'withref': "no" }}])
pixellayout(dqmitems, "05b - Cluster_Size_Forward",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_MechanicalView/size_per_OnlineBlock_PXForward",
      'description': "Mean cluster size",
      'draw': { 'withref': "no" }}] )

### Charge On track
pixellayout(dqmitems, "06a - Charge_ontrack_Barrel",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_Track/charge_per_OnlineBlock_PXBarrel",
      'description': "On track cluster charge",
      'draw': { 'withref': "no" }}])
pixellayout(dqmitems, "06b - Charge_ontrack_Forward",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_Track/charge_per_OnlineBlock_PXForward",
      'description': "On track cluster charge",
      'draw': { 'withref': "no" }}] )

### Number of cluster on track
pixellayout(dqmitems, "07a - Cluster_ontrack_Barrel",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_Track/num_clusters_ontrack_per_OnlineBlock_PXBarrel",
      'description': "Number of on track cluster",
      'draw': { 'withref': "no" }}])
pixellayout(dqmitems, "07b - Cluster_ontrack_Forward",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_Track/num_clusters_ontrack_per_OnlineBlock_PXForward",
      'description': "Number of on track cluster",
      'draw': { 'withref': "no" }}] )

### Residualx
pixellayout(dqmitems, "08a - residualx_Barrel",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_Track/residual_x_per_OnlineBlock_PXBarrel",
      'description': "Track residual x",
      'draw': { 'withref': "no" }}])
pixellayout(dqmitems, "08b - residualx_Forward",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_Track/residual_x_per_OnlineBlock_PXForward",
      'description': "Track residual x",
      'draw': { 'withref': "no" }}] )

### Residualy
pixellayout(dqmitems, "09a - residualy_Barrel",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_Track/residual_y_per_OnlineBlock_PXBarrel",
      'description': "Track residual y",
      'draw': { 'withref': "no" }}])
pixellayout(dqmitems, "09b - residualy_Forward",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_Track/residual_y_per_OnlineBlock_PXForward",
      'description': "Track residual y",
      'draw': { 'withref': "no" }}] )

############################## NON ONLINEBLOCK ##############################################

### ADC
pixellayout(dqmitems, "11a - ADC_Barrel",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_MechanicalView/adc_PXBarrel",
      'description': "Mean adc value per lumisection",
      'draw': { 'withref': "no" }}])
pixellayout(dqmitems, "11b - _ADC_Forward",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_MechanicalView/adc_PXForward",
      'description': "Mean adc value per lumisection",
      'draw': { 'withref': "no" }}])

### Cluster Charge
pixellayout(dqmitems, "12a - Cluster_Charge_Barrel",
  [{ 'path': "TrackTimingPixelPhase1/Phase1_MechanicalView/charge_PXBarrel",
      'description': "Mean cluster charge per lumisection in barrel",
      'draw': { 'withref': "no" }} ] )
pixellayout(dqmitems, "12b - Cluster_Charge_Forward",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_MechanicalView/charge_PXForward",
      'description': "Mean cluster charge per lumisection in barrel",
      'draw': { 'withref': "no" }}] )

### Size
pixellayout(dqmitems, "13a - Cluster_Size_Barrel",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_MechanicalView/size_PXBarrel",
      'description': "Mean cluster size per lumisection in barrel",
      'draw': { 'withref': "no" }}])
pixellayout(dqmitems, "13b - Cluster_Size_Forward",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_MechanicalView/size_PXForward",
      'description': "Mean cluster size per lumisection in barrel",
      'draw': { 'withref': "no" }}] )

### Charge On track
pixellayout(dqmitems, "14a - Charge_ontrack_Barrel",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_Track/charge_PXBarrel",
      'description': "Mean on track cluster charge",
      'draw': { 'withref': "no" }}])
pixellayout(dqmitems, "14b - Charge_ontrack_Forward",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_Track/charge_PXForward",
      'description': "Mean on track cluster charge",
      'draw': { 'withref': "no" }}] )

### Residualx
pixellayout(dqmitems, "15a - residualx_Barrel",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_Track/residual_x_PXBarrel",
      'description': "Track residual x in barrel",
      'draw': { 'withref': "no" }}])
pixellayout(dqmitems, "15b - Timing_residualx_Forward",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_Track/residual_x_PXForward",
      'description': "Track residual x in endcap",
      'draw': { 'withref': "no" }}] )

### Residualy
pixellayout(dqmitems, "16a - residualy_Barrel",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_Track/residual_y_PXBarrel",
      'description': "Track residual y in barrel",
      'draw': { 'withref': "no" }}])
pixellayout(dqmitems, "16b - residualy_Forward",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_Track/residual_y_PXForward",
      'description': "Track residual y in endcap",
      'draw': { 'withref': "no" }}] )
