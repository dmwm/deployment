def pixellayout(i, p, *rows): i["PixelPhase1Timing/Layouts/" + p] = DQMItem(layout=rows)


### Digis
pixellayout(dqmitems, "01a - Timing_Digi_Barrel",
   [{ 'path': "PixelPhase1Timing/Phase1_MechanicalView/num_digis_per_OnlineBlock_PXBarrel",
      'description': "number of digis per lumisection in barrel",
      'draw': { 'withref': "no" }}
      ] )
pixellayout(dqmitems, "01b - Timing_Digi_Forward",
   [{ 'path': "PixelPhase1Timing/Phase1_MechanicalView/num_digis_per_OnlineBlock_PXForward",
      'description': "number of digis per lumisection in endcap",
      'draw': { 'withref': "no" }}] )

### ADC
pixellayout(dqmitems, "02a - Timing_ADC_Barrel",
    [{ 'path': "PixelPhase1Timing/Phase1_MechanicalView/adc_per_OnlineBlock_PXBarrel",
      'description': "Mean adc value per lumisection in barrel",
      'draw': { 'withref': "no" }}])
pixellayout(dqmitems, "02b - Timing_ADC_Forward",
    [{ 'path': "PixelPhase1Timing/Phase1_MechanicalView/adc_per_OnlineBlock_PXForward",
      'description': "Mean adc value per lumisection in endcap",
      'draw': { 'withref': "no" }}])

### NumCluster
pixellayout(dqmitems, "03a - Timing_num_cluster_Barrel",
   [{ 'path': "PixelPhase1Timing/Phase1_MechanicalView/num_clusters_per_OnlineBlock_PXBarrel",
      'description': "Mean cluster value per lumisection in barrel",
      'draw': { 'withref': "no" }}] )
pixellayout(dqmitems, "03b - Timing_num_cluster_Forward",
    [{ 'path': "PixelPhase1Timing/Phase1_MechanicalView/num_clusters_per_OnlineBlock_PXForward",
      'description': "Mean cluster value per lumisection in endcap",
      'draw': { 'withref': "no" }}])

### Cluster Charge
pixellayout(dqmitems, "04a - Timing_charge_Barrel",
  [{ 'path': "PixelPhase1Timing/Phase1_MechanicalView/charge_per_OnlineBlock_PXBarrel",
      'description': "Mean cluster charge per lumisection in barrel",
      'draw': { 'withref': "no" }} ] )
pixellayout(dqmitems, "04b - Timing_charge_Forward",
    [{ 'path': "PixelPhase1Timing/Phase1_MechanicalView/charge_per_OnlineBlock_PXForward",
      'description': "Mean cluster charge per lumisection in endcap",
      'draw': { 'withref': "no" }}] )

### Size
pixellayout(dqmitems, "05a - Timing_size_Barrel",
    [{ 'path': "PixelPhase1Timing/Phase1_MechanicalView/size_per_OnlineBlock_PXBarrel",
      'description': "Mean cluster size per lumisection in barrel",
      'draw': { 'withref': "no" }}])
pixellayout(dqmitems, "05b - Timing_size_Forward",
    [{ 'path': "PixelPhase1Timing/Phase1_MechanicalView/size_per_OnlineBlock_PXForward",
      'description': "Mean cluster size per lumisection in endcap",
      'draw': { 'withref': "no" }}] )


############################## NON ONLINEBLOCK ##############################################

### ADC
pixellayout(dqmitems, "11a - ADC_Barrel",
    [{ 'path': "PixelPhase1Timing/Phase1_MechanicalView/adc_PXBarrel",
      'description': "Mean adc value per lumisection in barrel",
      'draw': { 'withref': "no" }}])
pixellayout(dqmitems, "11b - ADC_Forward",
    [{ 'path': "PixelPhase1Timing/Phase1_MechanicalView/adc_PXForward",
      'description': "Mean adc value per lumisection in endcap",
      'draw': { 'withref': "no" }}])

### Cluster Charge
pixellayout(dqmitems, "12a - charge_Barrel",
  [{ 'path': "PixelPhase1Timing/Phase1_MechanicalView/charge_PXBarrel",
      'description': "Mean cluster charge per lumisection in barrel",
      'draw': { 'withref': "no" }} ] )
pixellayout(dqmitems, "12b - charge_Forward",
    [{ 'path': "PixelPhase1Timing/Phase1_MechanicalView/charge_PXForward",
      'description': "Mean cluster charge per lumisection in endcap",
      'draw': { 'withref': "no" }}] )

### Size
pixellayout(dqmitems, "13a - size_Forward",
    [{ 'path': "PixelPhase1Timing/Phase1_MechanicalView/size_PXBarrel",
      'description': "Mean cluster size per lumisection in barrel",
      'draw': { 'withref': "no" }}])
pixellayout(dqmitems, "13b - size_Forward",
    [{ 'path': "PixelPhase1Timing/Phase1_MechanicalView/size_PXForward",
      'description': "Mean cluster size per lumisection in endcap",
      'draw': { 'withref': "no" }}] )
