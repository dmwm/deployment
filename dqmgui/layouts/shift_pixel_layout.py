def shiftpixellayout(i, p, *rows): i["00 Shift/Pixel/" + p] = DQMItem(layout=rows)
shiftpixellayout(dqmitems, "00 - Pixel Summary Map",
  [{ 'path': "Pixel/EventInfo/reportSummaryMap",
     'description': "Pixel Report Summary Map: FED data vs. lumisections",
     'draw': { 'withref': "no" }}]
  )
shiftpixellayout(dqmitems, "01 - Total number of errors",
  [{ 'path': "Pixel/AdditionalPixelErrors/FedChNErr",
     'description': "Total number of errors in a map of FED channels (y-axis) vs. FED (x-axis). Look for channels with thousands of errors!",
     'draw': { 'withref': "no" }}]
  )
shiftpixellayout(dqmitems, "02 - Error types",
  [{ 'path': "Pixel/AdditionalPixelErrors/FedETypeNErr",
     'description': "Total number of errors per error type (y-axis) vs. FED (x-axis). Large amounts (hundreds)of errors other than Timeout, EventNumber, and Dcol,Pixel values would be unusual!",
     'draw': { 'withref': "no" }}]
  )
shiftpixellayout(dqmitems, "03 - Cluster occupancy Barrel Layer 1",
  [{ 'path': "Pixel/Clusters/OffTrack/position_siPixelClusters_Layer_1",
     'description': "Cluster occupancy of Barrel Layer 1. Look for new holes compared to the example plot.",
     'draw': { 'withref': "no" }}]
  )
shiftpixellayout(dqmitems, "04 - Cluster occupancy Barrel Layer 2",
  [{ 'path': "Pixel/Clusters/OffTrack/position_siPixelClusters_Layer_2",
     'description': "Cluster occupancy of Barrel Layer 2. Look for new holes compared to the example plot.",
     'draw': { 'withref': "no" }}]
  )
shiftpixellayout(dqmitems, "05 - Cluster occupancy Barrel Layer 3",
  [{ 'path': "Pixel/Clusters/OffTrack/position_siPixelClusters_Layer_3",
     'description': "Cluster occupancy of Barrel Layer 3. Look for new holes compared to the example plot.",
     'draw': { 'withref': "no" }}]
  )
shiftpixellayout(dqmitems, "06 - Cluster occupancy Endcap -z Disk 1",
  [{ 'path': "Pixel/Clusters/OffTrack/position_siPixelClusters_mz_Disk_1",
     'description': "Cluster occupancy of Endcap -z Disk 1. Look for new holes compared to the example plot.",
     'draw': { 'withref': "no" }}]
  )
shiftpixellayout(dqmitems, "07 - Cluster occupancy Endcap -z Disk 2",
  [{ 'path': "Pixel/Clusters/OffTrack/position_siPixelClusters_mz_Disk_2",
     'description': "Cluster occupancy of Endcap -z Disk 2. Look for new holes compared to the example plot.",
     'draw': { 'withref': "no" }}]
  )
shiftpixellayout(dqmitems, "08 - Cluster occupancy Endcap +z Disk 1",
  [{ 'path': "Pixel/Clusters/OffTrack/position_siPixelClusters_pz_Disk_1",
     'description': "Cluster occupancy of Endcap +z Disk 1. Look for new holes compared to the example plot.",
     'draw': { 'withref': "no" }}]
  )
shiftpixellayout(dqmitems, "09 - Cluster occupancy Endcap +z Disk 2",
  [{ 'path': "Pixel/Clusters/OffTrack/position_siPixelClusters_pz_Disk_2",
     'description': "Cluster occupancy of Endcap +z Disk 2. Look for new holes compared to the example plot.",
     'draw': { 'withref': "no" }}]
  )
shiftpixellayout(dqmitems, "10 - Pixel_Charge_Summary",
  [{ 'path': "Pixel/Barrel/ALLMODS_chargeCOMB_Barrel",
     'description': "Distribution of gain corrected cluster charge for all clusters in the Barrel - dominant peak should be around 21 ke-",
     'draw': { 'withref': "yes" }},
   { 'path': "Pixel/Endcap/ALLMODS_chargeCOMB_Endcap",
     'description': "Distribution of gain corrected cluster charge for all clusters in the Endcaps - dominant peak should be around 21 ke-",
     'draw': { 'withref': "yes" }}]
  )
