def pixellayout(i, p, *rows): i["PixelPhase1/Layouts/" + p] = DQMItem(layout=rows)
pixellayout(dqmitems, "000 - PixelPhase1 FED Occupancy vs Lumi Sections",
            [{ 'path': "PixelPhase1/num_feddigistrend_per_Lumisection_per_FED",
               'description': "Number of digis per FED and Lumisection",
               'draw': { 'withref': "no" }}]
              )
pixellayout(dqmitems, "00a - PixelPhase1_Error_Summary",
   [{ 'path': "PixelPhase1/FED/nerrors_per_type_per_FED",
      'description': "Number of Errors of each type per FED. Channel 0 is assigned for errors where the channel number is not known.",
      'draw': { 'withref': "no" }}]
   )
pixellayout(dqmitems, "00b - PixelPhase1_Error_Summary",
   [{ 'path': "PixelPhase1/FED/errors_per_LinkInFed_per_FED",
      'description': "Total number of errors in a map of FED channels (y-axis) vs. FED (x-axis). Channel 0 is assigned for errors where the channel number is not known.",
      'draw': { 'withref': "no" }}]
   )

pixellayout(dqmitems, "00c - PixelPhase1_Cluster_Size_Eta",
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/sizeyvseta_PXBarrel",
      'description': "Cluster size along the beamline in pixel length (y-axis) vs the cluster eta position in eta (x-axis)",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}]
   )

pixellayout(dqmitems, "01a - Event_Rate_per_BX",
  [{ 'path': "PixelPhase1/Phase1_MechanicalView/eventrate_per_BX",
     'description': "Event rate per bunch crossing",
     'draw': { 'withref': "no" }}]
  )
pixellayout(dqmitems, "01b - Cluster_Event_Rate_per_BX",
  [{ 'path': "PixelPhase1/Phase1_MechanicalView/clustereventrate_per_BX",
     'description': "Cluster event rate per bunch crossing",
     'draw': { 'withref': "no" }}]
  )

#pixellayout(dqmitems, "01a - Pixel_zeroOccupancy_BarrelROCs", ##TO BE ADDED LATER 
#  [{ 'path': "Pixel/noOccROCsBarrel",
#     'description': "Total number of zero occupancy barrel ROCs vs every 10 LS",
#     'draw': { 'withref': "yes" }}]
#  )
#pixellayout(dqmitems, "01b - Pixel_zeroOccupancy_EndcapROCs",  ##TO BE ADDED LATER 
#  [{ 'path': "Pixel/noOccROCsEndcap",
#     'description': "Total number of zero occupancy endcap ROCs vs every 10 LS",
#     'draw': { 'withref': "yes" }}]
#  )

pixellayout(dqmitems, "02 - Pixel_Digi_Barrel_Summary",
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/num_digis_PXBarrel",
      'description': "Number of digis per event in PXBarrel",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/adc_PXBarrel",
      'description': "Adc distribution of digis per event per barrel module",
      'draw': { 'withref': "no" }}],
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/num_digis_per_Lumisection_PXBarrel",
      'description': "Mean adc value per lumisection",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/adc_per_Lumisection_PXBarrel",
      'description': "Mean adc value per lumisection",
      'draw': { 'withref': "no" }}]
   )

pixellayout(dqmitems, "03 - Pixel_Digi_Endcap_Summary",
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/num_digis_PXForward",
      'description': "Number of digis per event in Forward",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/adc_PXForward",
      'description': "Adc distribution of digis per event per forward module",
      'draw': { 'withref': "no" }}],
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/num_digis_per_Lumisection_PXForward",
      'description': "Mean adc value per lumisection",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/adc_per_Lumisection_PXForward",
      'description': "Mean adc value per lumisection",
      'draw': { 'withref': "no" }}]
   )

pixellayout(dqmitems, "04 - Pixel_Cluster_Number_Summary",
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/num_clusters_PXBarrel",
      'description': "Number of cluster per event in Barrel",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/num_clusters_PXForward",
      'description': "Number of cluster per event in Forward",
      'draw': { 'withref': "no" }}],
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/num_clusters_per_Lumisection_PXBarrel",
      'description': "Mean cluster value per lumisection in barrel",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/num_clusters_per_Lumisection_PXForward",
      'description': "Mean cluster value per lumisection in endcap",
      'draw': { 'withref': "no" }}]
   )

pixellayout(dqmitems, "05 - Pixel_Cluster_Charge_Summary",
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/charge_PXBarrel",
      'description': "Cluster charge in the barrel modules",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/charge_PXForward",
      'description': "Distribution of raw charge for all digis recorded in the Endcap modules - dominant peak should be around 90-100 ADC",
      'draw': { 'withref': "no" }}],
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/charge_per_Lumisection_PXBarrel",
      'description': "Mean cluster charge per lumisection in barrel",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/charge_per_Lumisection_PXForward",
      'description': "Mean cluster charge per lumisection in barrel",
      'draw': { 'withref': "no" }}]
   )

pixellayout(dqmitems, "06 - Pixel_Cluster_Size_Summary",
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/size_PXBarrel",
      'description': "Total cluster size in the barrel modules",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/size_PXForward",
      'description': "Total cluster size in the Endcap modules",
      'draw': { 'withref': "no" }}],
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/size_per_Lumisection_PXBarrel",
      'description': "Mean cluster size per lumisection in barrel",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/size_per_Lumisection_PXForward",
      'description': "Mean cluster size per lumisection in barrel",
      'draw': { 'withref': "no" }}]
   )

#pixellayout(dqmitems, "05 - Pixel_Cluster_Barrel_Summary",
#  [{ 'path': "Pixel/Barrel/SUMCLU_charge_Barrel",
#     'description': "Mean cluster charge in kilo electrons per barrel module",
#     'draw': { 'withref': "yes" }}],
#  [{ 'path': "Pixel/Barrel/SUMCLU_nclusters_Barrel",
#     'description': "Mean number of clusters per event per barrel module",
#     'draw': { 'withref': "yes" }}],
#  [{ 'path': "Pixel/Barrel/SUMCLU_size_Barrel",
#     'description': "Mean cluster size in number of pixels per barrel module",
#     'draw': { 'withref': "yes" }}]
#  )
#pixellayout(dqmitems, "06 - Pixel_Cluster_Endcap_Summary",
#  [{ 'path': "Pixel/Endcap/SUMCLU_charge_Endcap",
#     'description': "Mean cluster charge in kilo electrons per endcap module",
#     'draw': { 'withref': "yes" }}],
#[{ 'path': "Pixel/Endcap/SUMCLU_nclusters_Endcap",
#     'description': "Mean number of clusters per event per endcap module",
#     'draw': { 'withref': "yes" }}],
#  [{ 'path': "Pixel/Endcap/SUMCLU_size_Endcap",
#     'description': "Mean cluster size in number of pixels per barrel module",
#     'draw': { 'withref': "yes" }}]
#  )
#pixellayout(dqmitems, "09 - Pixel Clusters vs LS",
#  [{ 'path': "Pixel/Barrel/totalNumberOfClustersProfile_siPixelClusters_Barrel",
#     'description': "Total # of CLusters in BPIX with event time in Seconds (LS)",
#     'draw': {'withref' : "no" }}],
#  [{ 'path': "Pixel/Endcap/totalNumberOfClustersProfile_siPixelClusters_FPIX+",
#     'description' : "Total # of CLusters in FPIX+ with event time in Seconds (LS)",
#     'draw': {'withref' : "no" }},
#   { 'path': "Pixel/Endcap/totalNumberOfClustersProfile_siPixelClusters_FPIX-",
#     'description' : "Total # of CLusters in FPIX+ with event time in Seconds (LS)",
#     'draw': {'withref' : "no" }}]
#  )
#pixellayout(dqmitems, "20a - Cluster occupancy Barrel Layer 1",
#  [{ 'path': "Pixel/Clusters/OffTrack/position_siPixelClusters_Layer_1",
#     'description': "Cluster occupancy of Barrel Layer 1",
#     'draw': { 'withref': "no" }}]
#  )
#pixellayout(dqmitems, "20b - Cluster occupancy Barrel Layer 2",
#  [{ 'path': "Pixel/Clusters/OffTrack/position_siPixelClusters_Layer_2",
#     'description': "Cluster occupancy of Barrel Layer 2",
#     'draw': { 'withref': "no" }}]
#  )
#pixellayout(dqmitems, "20c - Cluster occupancy Barrel Layer 3",
#  [{ 'path': "Pixel/Clusters/OffTrack/position_siPixelClusters_Layer_3",
#     'description': "Cluster occupancy of Barrel Layer 3",
#     'draw': { 'withref': "no" }}]
#  )
#pixellayout(dqmitems, "20d - Cluster occupancy Endcap -z Disk 1",
#  [{ 'path': "Pixel/Clusters/OffTrack/position_siPixelClusters_mz_Disk_1",
#     'description': "Cluster occupancy of Endcap -z Disk 1",
#     'draw': { 'withref': "no" }}]
#  )
#pixellayout(dqmitems, "20e - Cluster occupancy Endcap -z Disk 2",
#  [{ 'path': "Pixel/Clusters/OffTrack/position_siPixelClusters_mz_Disk_2",
#     'description': "Cluster occupancy of Endcap -z Disk 2",
#     'draw': { 'withref': "no" }}]
#  )
#pixellayout(dqmitems, "20f - Cluster occupancy Endcap +z Disk 1",
#  [{ 'path': "Pixel/Clusters/OffTrack/position_siPixelClusters_pz_Disk_1",
#     'description': "Cluster occupancy of Endcap +z Disk 1",
#     'draw': { 'withref': "no" }}]
#  )
#pixellayout(dqmitems, "20g - Cluster occupancy Endcap +z Disk 2",
#  [{ 'path': "Pixel/Clusters/OffTrack/position_siPixelClusters_pz_Disk_2",
#     'description': "Cluster occupancy of Endcap +z Disk 2",
#     'draw': { 'withref': "no" }}]
#  )
#pixellayout(dqmitems, "21a - Pixel_Noise_Summary",
#  [{ 'path': "Pixel/Barrel/SUMDIG_ndigisFREQ_Barrel",
#     'description': "Total number of events with at least one digi per event per barrel module - spikes show noisy modules or pixels!",
#     'draw': { 'withref': "yes" }}]
#  )
#pixellayout(dqmitems, "21b - Pixel_Noise_Summary",
#  [{ 'path': "Pixel/Endcap/SUMDIG_ndigisFREQ_Endcap",
#     'description': "Total number of events with at least one digi per event per endcap module - spikes show noisy modules or pixels!",
#     'draw': { 'withref': "yes" }}]
#  )
#pixellayout(dqmitems, "30a - Pixel event rates",
#  [{ 'path': "Pixel/pixEventRate",
#     'description': "Rate of events with Pixel activity above noise level (at least 4 modules with digis)",
#     'draw': { 'withref': "no" }}]
#  )
#pixellayout(dqmitems, "30b - Pixel event BX distribution",
#  [{ 'path': "Pixel/pixEvtsPerBX",
#     'description': "Distribution of Pixel events (at least 4 modules with digis) versus bucket number",
#     'draw': { 'withref': "no" }}]
#  )
#pixellayout(dqmitems, "31 - Cluster_y_width_vs_cluster_eta",
#  [{ 'path': "Pixel/Barrel/sizeYvsEta_siPixelClusters_Barrel",
#     'description': "Cluster y width as function of cluster eta",
#     'draw': { 'withref': "no" }}]
#  )
