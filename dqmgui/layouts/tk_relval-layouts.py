def trackervalidationlayout(i, p, *rows): i["DataLayouts/Tk/" + p] = DQMItem(layout=rows)

trackervalidationlayout(dqmitems, "01 - TEC-",
                        [{ 'path':"SiStrip/MechanicalView/TEC/side_1/Summary_ClusterStoNCorr_OnTrack__TEC__side__1",
                           'description': "Signal-to-Noise (corrected for the angle) for On-Track clusters"},
                         {'path':"SiStrip/MechanicalView/TEC/side_1/Summary_TotalNumberOfClusters_OnTrack__TEC__side__1",
                          'description': "Number of clusters"}],
                        [{'path':"SiStrip/MechanicalView/TEC/side_1/Summary_ClusterCharge_OffTrack__TEC__side__1",
                          'description': "OffTrack cluster charge"},
                         {'path':"SiStrip/MechanicalView/TEC/side_1/Summary_TotalNumberOfClusters_OffTrack__TEC__side__1",
                          'description': "Number of clusters"}])
                         
trackervalidationlayout(dqmitems, "02 - TEC+",
                        [{ 'path':"SiStrip/MechanicalView/TEC/side_2/Summary_ClusterStoNCorr_OnTrack__TEC__side__2",
                           'description': "Signal-to-Noise (corrected for the angle) for On-Track clusters"},
                         {'path':"SiStrip/MechanicalView/TEC/side_2/Summary_TotalNumberOfClusters_OnTrack__TEC__side__2",
                          'description': "Number of clusters"}],
                        [{'path':"SiStrip/MechanicalView/TEC/side_2/Summary_ClusterCharge_OffTrack__TEC__side__2",
                          'description': "OffTrack cluster charge"},
                         {'path':"SiStrip/MechanicalView/TEC/side_2/Summary_TotalNumberOfClusters_OffTrack__TEC__side__2",
                          'description': "Number of clusters"}])

trackervalidationlayout(dqmitems, "03 - TIB",
                        [{ 'path':"SiStrip/MechanicalView/TIB/Summary_ClusterStoNCorr_OnTrack__TIB",
                           'description': "Signal-to-Noise (corrected for the angle) for On-Track clusters"},
                         {'path':"SiStrip/MechanicalView/TIB/Summary_TotalNumberOfClusters_OnTrack__TIB",
                          'description': "Number of clusters"}],
                        [{'path':"SiStrip/MechanicalView/TIB/Summary_ClusterCharge_OffTrack__TIB",
                          'description': "OffTrack cluster charge"},
                         {'path':"SiStrip/MechanicalView/TIB/Summary_TotalNumberOfClusters_OffTrack__TIB",
                          'description': "Number of clusters"}])

trackervalidationlayout(dqmitems, "04 - TID-",
                        [{ 'path':"SiStrip/MechanicalView/TID/side_1/Summary_ClusterStoNCorr_OnTrack__TID__side__1",
                           'description': "Signal-to-Noise (corrected for the angle) for On-Track clusters"},
                         {'path':"SiStrip/MechanicalView/TID/side_1/Summary_TotalNumberOfClusters_OnTrack__TID__side__1",
                          'description': "Number of clusters"}],
                        [{'path':"SiStrip/MechanicalView/TID/side_1/Summary_ClusterCharge_OffTrack__TID__side__1",
                          'description': "OffTrack cluster charge"},
                         {'path':"SiStrip/MechanicalView/TID/side_1/Summary_TotalNumberOfClusters_OffTrack__TID__side__1",
                          'description': "Number of clusters"}])


trackervalidationlayout(dqmitems, "05 - TID+",
                        [{ 'path':"SiStrip/MechanicalView/TID/side_2/Summary_ClusterStoNCorr_OnTrack__TID__side__2",
                           'description': "Signal-to-Noise (corrected for the angle) for On-Track clusters"},
                         {'path':"SiStrip/MechanicalView/TID/side_2/Summary_TotalNumberOfClusters_OnTrack__TID__side__2",
                          'description': "Number of clusters"}],
                        [{'path':"SiStrip/MechanicalView/TID/side_2/Summary_ClusterCharge_OffTrack__TID__side__2",
                          'description': "OffTrack cluster charge"},
                         {'path':"SiStrip/MechanicalView/TID/side_2/Summary_TotalNumberOfClusters_OffTrack__TID__side__2",
                          'description': "Number of clusters"}])


trackervalidationlayout(dqmitems, "06 - TOB",
                        [{ 'path':"SiStrip/MechanicalView/TOB/Summary_ClusterStoNCorr_OnTrack__TOB",
                           'description': "Signal-to-Noise (corrected for the angle) for On-Track clusters"},
                         {'path':"SiStrip/MechanicalView/TOB/Summary_TotalNumberOfClusters_OnTrack__TOB",
                          'description': "Number of clusters"}],
                        [{'path':"SiStrip/MechanicalView/TOB/Summary_ClusterCharge_OffTrack__TOB",
                          'description': "OffTrack cluster charge"},
                         {'path':"SiStrip/MechanicalView/TOB/Summary_TotalNumberOfClusters_OffTrack__TOB",
                          'description': "Number of clusters"}])

trackervalidationlayout(dqmitems, "07 - Pixel RecHits Barrel",
                        [{ 'path':"Pixel/Barrel/SUMOFF_ClustX_Barrel",
                           'description': ""},
                         {'path':"Pixel/Barrel/SUMOFF_ClustY_Barrel",
                          'description': ""}],
                        [{'path':"Pixel/Barrel/SUMOFF_ErrorX_Barrel",
                          'description': ""},
                         {'path':"Pixel/Barrel/SUMOFF_ErrorY_Barrel",
                          'description': ""}])

trackervalidationlayout(dqmitems, "08 - Pixel RecHits Endcap",
                        [{ 'path':"Pixel/Endcap/SUMOFF_ClustX_Endcap",
                           'description': ""},
                         {'path':"Pixel/Endcap/SUMOFF_ClustY_Endcap",
                          'description': ""}],
                        [{'path':"Pixel/Endcap/SUMOFF_ErrorX_Endcap",
                          'description': ""},
                         {'path':"Pixel/Endcap/SUMOFF_ErrorY_Endcap",
                          'description': ""}])

trackervalidationlayout(dqmitems, "09 - Pixel Occupancy",
                        [{ 'path':"Pixel/Barrel/SUMOFF_ndigis_Barrel",
                           'description': ""},
                         {'path':"Pixel/Endcap/SUMOFF_ndigis_Endcap",
                          'description': ""}],
                        [{ 'path':"Pixel/Barrel/SUMOFF_nclusters_Barrel",
                           'description': ""},
                         {'path':"Pixel/Endcap/SUMOFF_nclusters_Endcap",
                          'description': ""}],
                        [{ 'path':"Pixel/Barrel/SUMOFF_nRecHits_Barrel",
                           'description': ""},
                         {'path':"Pixel/Endcap/SUMOFF_nRecHits_Endcap",
                          'description': ""}])

trackervalidationlayout(dqmitems, "10 - Pixel Clusters Barrel",
                        [{ 'path':"Pixel/Clusters/OnTrack/charge_siPixelClusters_Barrel",
                           'description': ""},
                         {'path':"Pixel/Clusters/OnTrack/size_siPixelClusters_Barrel",
                          'description': ""}],
                        [{'path':"Pixel/Clusters/OffTrack/charge_siPixelClusters_Barrel",
                          'description': ""},
                         {'path':"Pixel/Clusters/OffTrack/size_siPixelClusters_Barrel",
                          'description': ""}])

trackervalidationlayout(dqmitems, "11 - Pixel Clusters Endcap",
                        [{ 'path':"Pixel/Clusters/OnTrack/charge_siPixelClusters_Endcap",
                           'description': ""},
                         {'path':"Pixel/Clusters/OnTrack/size_siPixelClusters_Endcap",
                          'description': ""}],
                        [{'path':"Pixel/Clusters/OffTrack/charge_siPixelClusters_Endcap",
                          'description': ""},
                         {'path':"Pixel/Clusters/OffTrack/size_siPixelClusters_Endcap",
                          'description': ""}])
