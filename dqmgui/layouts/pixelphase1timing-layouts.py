def pixellayout(i, p, *rows): i["PixelPhase1Timing/Layouts/" + p] = DQMItem(layout=rows)


### Digis
pixellayout(dqmitems, "01a - Digi_Barrel",
   [{ 'path': "PixelPhase1Timing/Phase1_MechanicalView/num_digis_per_OnlineBlock_PXBarrel",
      'description': "Mean adc value per lumisection",
      'draw': { 'withref': "no" }}
      ] )

pixellayout(dqmitems, "01b - Digi_Forward",
   [{ 'path': "PixelPhase1Timing/Phase1_MechanicalView/num_digis_per_OnlineBlock_PXForward",
      'description': "Mean adc value per lumisection",
      'draw': { 'withref': "no" }}] )

### ADC
pixellayout(dqmitems, "02a - ADC_Barrel",
    [{ 'path': "PixelPhase1Timing/Phase1_MechanicalView/adc_per_OnlineBlock_PXBarrel",
      'description': "Mean adc value per lumisection",
      'draw': { 'withref': "no" }}])
pixellayout(dqmitems, "02b - ADC_Forward",
    [{ 'path': "PixelPhase1Timing/Phase1_MechanicalView/adc_per_OnlineBlock_PXForward",
      'description': "Mean adc value per lumisection",
      'draw': { 'withref': "no" }}])

### NumCluster
pixellayout(dqmitems, "03a - Cluster_Barrel",
   [{ 'path': "PixelPhase1Timing/Phase1_MechanicalView/num_clusters_per_OnlineBlock_PXBarrel",
      'description': "Number of clusters per lumisection",
      'draw': { 'withref': "no" }}] )
pixellayout(dqmitems, "03b - Cluster_Forward",
    [{ 'path': "PixelPhase1Timing/Phase1_MechanicalView/num_clusters_per_OnlineBlock_PXForward",
      'description': "Number of clusters per lumisection",
      'draw': { 'withref': "no" }}])

### Cluster Charge
pixellayout(dqmitems, "04a - Cluster_Charge_Barrel",
  [{ 'path': "PixelPhase1Timing/Phase1_MechanicalView/charge_per_OnlineBlock_PXBarrel",
      'description': "Mean cluster charge per lumisection",
      'draw': { 'withref': "no" }} ] )
pixellayout(dqmitems, "04b - Cluster_Charge_Forward",
    [{ 'path': "PixelPhase1Timing/Phase1_MechanicalView/charge_per_OnlineBlock_PXForward",
      'description': "Mean cluster charge per lumisection",
      'draw': { 'withref': "no" }}] )

### Size
pixellayout(dqmitems, "05a - Size_Barrel",
    [{ 'path': "PixelPhase1Timing/Phase1_MechanicalView/size_per_OnlineBlock_PXBarrel",
      'description': "Mean cluster size per lumisection",
      'draw': { 'withref': "no" }}])
pixellayout(dqmitems, "05b - Size_Forward",
    [{ 'path': "PixelPhase1Timing/Phase1_MechanicalView/size_per_OnlineBlock_PXForward",
      'description': "Mean cluster size per lumisection",
      'draw': { 'withref': "no" }}] )


############################## NON ONLINEBLOCK ##############################################

### ADC
pixellayout(dqmitems, "11a - ADC_Barrel",
    [{ 'path': "PixelPhase1Timing/Phase1_MechanicalView/adc_PXBarrel",
      'description': "Mean adc value",
      'draw': { 'withref': "no" }}])
pixellayout(dqmitems, "11b - ADC_Forward",
    [{ 'path': "PixelPhase1Timing/Phase1_MechanicalView/adc_PXForward",
      'description': "Mean adc value",
      'draw': { 'withref': "no" }}])

### Cluster Charge
pixellayout(dqmitems, "12a - Cluster_Charge_Barrel",
  [{ 'path': "PixelPhase1Timing/Phase1_MechanicalView/charge_PXBarrel",
      'description': "Mean cluster charge",
      'draw': { 'withref': "no" }} ] )
pixellayout(dqmitems, "12b - Cluster_Charge_Forward",
    [{ 'path': "PixelPhase1Timing/Phase1_MechanicalView/charge_PXForward",
      'description': "Mean cluster charge",
      'draw': { 'withref': "no" }}] )

### Size
pixellayout(dqmitems, "13a - Size_Forward",
    [{ 'path': "PixelPhase1Timing/Phase1_MechanicalView/size_PXBarrel",
      'description': "Mean cluster size",
      'draw': { 'withref': "no" }}])
pixellayout(dqmitems, "13b - Size_Forward",
    [{ 'path': "PixelPhase1Timing/Phase1_MechanicalView/size_PXForward",
      'description': "Mean cluster size",
      'draw': { 'withref': "no" }}] )
