def phase2tkmclayout(i, p, *rows): i["MCLayouts/Phase2Tk/" + p] = DQMItem(layout=rows)

# Loop to create layouts for all EXCEPT L1Track

# These names shouldn't change
top_files = ["TrackerPhase2ITClusterV/",
            "TrackerPhase2ITRecHitV/",
            "TrackerPhase2ITTrackingRecHitV/",
            "TrackerPhase2OTClusterV/",
            "TrackerPhase2OTRecHitV/",
            "TrackerPhase2OTTrackingRecHitV/"]
common_structures = ["Barrel/", "EndCap_Side1/", "EndCap_Side2/"]
IT_structures = ["FPix/", "EPix/"]
OT_structures = ["TEDD_1/", "TEDD_2/"]
TEDD_rings = [15, 12]
layout_name_parts = ["IT ", "OT ", "Clusters ", "RecHit ", "TrackingRecHit ", "L1 Track ",
                     "Barrel ", "Layer ", "MINUS ", "PLUS ", "FPix ", "EPix ", "Ring ", "TEDD1 ", "TEDD2 "]

# If you want to book different values, you'll have to add them here, and then edit the "for histogram in histogram_names[a:b]:" lines
histogram_names = ["Delta_X_Pixel", "Delta_Y_Pixel", "Delta_Y_vs_DeltaX", "Delta_X", "Delta_Y", "Delta_X_Strip", "Delta_Y_Strip"]

for f_index, file in enumerate(top_files): # Loop thru our top folders
    layout = []
    layout_num = 00 # Two digit counter - layouts are numbered with three digits, with the first indicating the top folder
    for s_index, structure in enumerate(common_structures): # Loop thru our "common" tracker structures

        # ----- OUTER TRACKER ------
        if f_index > 2:
            # ----- OUTER TRACKER BARREL -----
            if structure == common_structures[0]:
                layout_desc_template = layout_name_parts[1] + layout_name_parts[f_index-1] + layout_name_parts[6]
                # ---- STRIPS ----
                for histogram in histogram_names[5:7]:
                    layout_name = str(f_index) + f"{layout_num:02}" + " - " + layout_desc_template + histogram
                    for layer in range(6): # One layout = One histogram * 6 layers (for strips)
                        layout.append([{"path":(file + structure + "Layer" + str(layer+1) + "/" + histogram), "description":(layout_desc_template + layout_name_parts[7] + str(layer+1) + " " + histogram)}])
                    phase2tkmclayout(dqmitems, layout_name, (layout[0]+layout[1]), (layout[2]+layout[3]), (layout[4]+layout[5]))
                    layout_num = layout_num + 1
                    layout = []
                    
                # ---- PIXELS ----
                for histogram in histogram_names[0:2]:
                    layout_name = str(f_index) + f"{layout_num:02}" + " - " + layout_desc_template + histogram
                    for layer in range(3): # One layout = One histogram * 3 layers (for pixels)
                        layout.append([{"path":(file + structure + "Layer" + str(layer+1) + "/" + histogram), "description":(layout_desc_template + layout_name_parts[7] + str(layer+1) + " " + histogram)}])
                    phase2tkmclayout(dqmitems, layout_name, (layout[0]+layout[1]), layout[2])
                    layout_num = layout_num + 1
                    layout = []

            # ----- OUTER TRACKER ENDCAPS -----
            else:
                for tedd in range(2):
                    layout_desc_template = layout_name_parts[1] + layout_name_parts[f_index-1] + layout_name_parts[s_index+7] + "Endcap " + layout_name_parts[13+tedd]
                    for layer in range(TEDD_rings[tedd]): # One layout = Four histograms * 1 layer
                        layout_name = OT_structures[tedd] + structure + str(f_index) + f"{layout_num:02}" + " - " + layout_desc_template + histogram # There are a lot of TEDD histos so we put them in a folder
                        # ---- STRIPS ----
                        for histogram in histogram_names[5:7]:
                            layout.append([{"path":(file + structure + OT_structures[tedd] + "Ring" + str(layer+1) + "/" + histogram), "description":(layout_desc_template + layout_name_parts[12] + str(layer+1) + " " + histogram)}])
                        # ---- PIXELS ----
                        if (layer < TEDD_rings[tedd]-5):
                            for histogram in histogram_names[0:2]:
                                layout.append([{"path":(file + structure + OT_structures[tedd] + "Ring" + str(layer+1) + "/" + histogram), "description":(layout_desc_template + layout_name_parts[12] + str(layer+1) + " " + histogram)}])
                            phase2tkmclayout(dqmitems, layout_name, (layout[0]+layout[1]), (layout[2]+layout[3]))
                        else:
                            phase2tkmclayout(dqmitems, layout_name, (layout[0]+layout[1]))
                        layout_num = layout_num + 1
                        layout = []

        # ----- INNER TRACKER -----
        else:
            # For IT, the histogram names change between clust/rechit/tracking
            # So this selects which ones we use based on the top file index
            if f_index == 0: 
                lower = 0
                upper = 2
            elif f_index == 1:
                lower = 2
                upper = 3
            elif f_index == 2:
                lower = 3
                upper = 5
            
            # ----- INNER TRACKER BARREL -----
            if structure == common_structures[0]:
                layout_desc_template = layout_name_parts[0] + layout_name_parts[2+f_index] + layout_name_parts[6]
                for histogram in histogram_names[lower:upper]:
                    layout_name = str(f_index) + f"{layout_num:02}" + " - " + layout_desc_template + histogram
                    for layer in range(4): # One layout = One histogram * 4 layers
                        layout.append([{"path":(file + structure + "Layer" + str(layer+1) + "/" + histogram), "description":(layout_desc_template + layout_name_parts[7] + str(layer+1) + " " + histogram)}])
                    phase2tkmclayout(dqmitems, layout_name, (layout[0]+layout[1]), (layout[2]+layout[3]))
                    layout_num = layout_num + 1
                    layout = []

            # ----- INNER TRACKER ENDCAPS -----  
            else:
                for histogram in histogram_names[lower:upper]:
                    for efpix in range(2):
                        layout_desc_template = layout_name_parts[0] + layout_name_parts[2+f_index] + layout_name_parts[s_index+7] + "Endcap " + layout_name_parts[10+efpix]
                        layout_name = str(f_index) + f"{layout_num:02}" + " - " + layout_desc_template + histogram
                        for layer in range(4+efpix): # One layout = One histogram * 4/5 rings, depending on FPix or EPix
                            layout.append([{"path":(file + structure + IT_structures[efpix] + "Ring" + str(layer+1) + "/" + histogram), "description":(layout_desc_template + layout_name_parts[12] + str(layer+1) + " " + histogram)}])
                        if efpix == 0:
                            phase2tkmclayout(dqmitems, layout_name, (layout[0]+layout[1]), (layout[2]+layout[3]))
                        else:
                            phase2tkmclayout(dqmitems, layout_name, (layout[0]+layout[1]), (layout[2]+layout[3]), layout[4])
                        layout_num = layout_num + 1
                        layout = []

# ----- END LOOP ------
# L1 TRACK
phase2tkmclayout(dqmitems, "600 - OT L1Track Eta Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Nominal_L1TF/FinalEfficiency/EtaEfficiency",
                   'description': "Eta Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/Nominal_L1TF/FinalResolution/EtaResolution",
                   'description': "Eta Resolution"}]
                 )

phase2tkmclayout(dqmitems, "601 - OT L1Track Phi Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Nominal_L1TF/FinalResolution/PhiResolution",
                   'description': "Phi Resolution"}]
                 )

phase2tkmclayout(dqmitems, "602 - OT L1Track Lxy Efficiency",
                 [{'path':"TrackerPhase2OTL1TrackV/Nominal_L1TF/FinalEfficiency/LxyEfficiency",
                   'description': "Lxy Efficiency"}]
                 )

phase2tkmclayout(dqmitems, "603 - OT L1Track d0 Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Nominal_L1TF/FinalEfficiency/d0Efficiency",
                   'description': "d0 Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/Nominal_L1TF/FinalResolution/d0Resolution",
                   'description': "d0 Resolution"}]
                 )

phase2tkmclayout(dqmitems, "604 - OT L1Track z0 Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Nominal_L1TF/FinalEfficiency/z0Efficiency",
                   'description': "z0 Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/Nominal_L1TF/FinalResolution/z0Resolution",
                   'description': "z0 Resolution"}]
                 )

phase2tkmclayout(dqmitems, "605 - OT Extended L1Track Displaced Eta Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Displaced/FinalEfficiency/EtaEfficiency",
                   'description': "Eta Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Displaced/FinalResolution/EtaResolution_displaced",
                   'description': "Eta Resolution"}]
                 )

phase2tkmclayout(dqmitems, "606 - OT Extended L1Track Displaced Phi Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Displaced/FinalResolution/PhiResolution_displaced",
                   'description': "Phi Resolution"}]
                 )

phase2tkmclayout(dqmitems, "607 - OT Extended L1Track Displaced Lxy Efficiency",
                 [{'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Displaced/FinalEfficiency/LxyEfficiency",
                   'description': "Lxy Efficiency"}]
                 )

phase2tkmclayout(dqmitems, "608 - OT Extended L1Track Displaced d0 Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Displaced/FinalEfficiency/d0Efficiency",
                   'description': "d0 Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Displaced/FinalResolution/d0Resolution_displaced",
                   'description': "d0 Resolution"}]
                 )

phase2tkmclayout(dqmitems, "609 - OT Extended L1Track Prompt Eta Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Prompt/FinalEfficiency/EtaEfficiency",
                   'description': "Eta Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Prompt/FinalResolution/EtaResolution_prompt",
                   'description': "Eta Resolution"}]
                 )

phase2tkmclayout(dqmitems, "610 - OT Extended L1Track Prompt Phi Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Prompt/FinalResolution/PhiResolution_prompt",
                   'description': "Phi Resolution"}]
                 )

phase2tkmclayout(dqmitems, "611 - OT Extended L1Track Prompt Lxy Efficiency",
                 [{'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Prompt/FinalEfficiency/LxyEfficiency",
                   'description': "Lxy Efficiency"}]
                 )

phase2tkmclayout(dqmitems, "612 - OT Extended L1Track Prompt d0 Efficiency and Resolution",
                 [{'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Prompt/FinalEfficiency/d0Efficiency",
                   'description': "d0 Efficiency"},
                  {'path':"TrackerPhase2OTL1TrackV/Extended_L1TF/Prompt/FinalResolution/d0Resolution_prompt",
                   'description': "d0 Resolution"}]
                 )


