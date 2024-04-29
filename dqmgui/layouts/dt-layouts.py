
DT_TWIKI = f"<a href=https://twiki.cern.ch/twiki/bin/view/CMS/DTDQMPlots>Description and Instructions</a>"

def dtlayout(i, p, *rows): i["DT/Layouts/" + p] = DQMItem(layout=rows)

dtlayout(dqmitems, "00-Summary/00-DataIntegritySummary",
  [{ 'path': "DT/00-DataIntegrity/DataIntegritySummary", 'description': DT_TWIKI }])

dtlayout(dqmitems, "00-Summary/00-ROChannelSummary",
  [{ 'path': "DT/00-ROChannels/ROChannelSummary", 'description': DT_TWIKI }])

dtlayout(dqmitems, "00-Summary/01-OccupancySummary",
  [{ 'path': "DT/01-Digi/OccupancySummary", 'description': DT_TWIKI }])

dtlayout(dqmitems, "00-Summary/02-SegmentSummary",
  [{ 'path': "DT/02-Segments/segmentSummary", 'description': DT_TWIKI }])

dtlayout(dqmitems, "00-Summary/03-TM_TriggerCorrFractionSummaryIn",
  [{ 'path': "DT/03-LocalTrigger-TM/TM_CorrFractionSummaryIn", 'description': DT_TWIKI }])

dtlayout(dqmitems, "00-Summary/04-TM_Trigger2ndFractionSummaryIn",
  [{ 'path': "DT/03-LocalTrigger-TM/TM_2ndFractionSummaryIn", 'description': DT_TWIKI }])

dtlayout(dqmitems, "00-Summary/05-NoiseChannelsSummary",
  [{ 'path': "DT/05-Noise/NoiseSummary", 'description': DT_TWIKI }])

dtlayout(dqmitems, "00-Summary/06-SynchNoiseSummary",
  [{ 'path': "DT/05-Noise/SynchNoise/SynchNoiseSummary", 'description': DT_TWIKI }])

#### OCCUPANCIES #################################################################################

for wheel in range(-2, 3):
    for station in range (1, 5):
        for sector in range (1, 15):
            if station != 4 and (sector == 13 or sector == 14):
                continue
            name = f"01-Occupancy/Wheel{wheel}/St{station}_Sec{sector}"
            histo_name = f"DT/01-Digi/Wheel{wheel}/Sector{sector}/Station{station}/OccupancyAllHits_perCh_W{wheel}_St{station}_Sec{sector}"
            dtlayout(dqmitems, name,[{ 'path': histo_name}])

#### TIME BOXES #################################################################################

for wheel in range(-2, 3):
    for sector in range (1, 15):
        for station in range (1, 5):
            if station != 4 and (sector == 13 or sector == 14):
                continue
            name = f"02-TimeBoxes/Wheel{wheel}/St{station}_Sec{sector}"
            histo_name = f"DT/01-Digi/Wheel{wheel}/Sector{sector}/Station{station}/TimeBox_W{wheel}_St{station}_Sec{sector}"
            histo_name_SL1 = f"{histo_name}_SL1"
            histo_name_SL2 = f"{histo_name}_SL2"
            histo_name_SL3 = f"{histo_name}_SL3"
            if station != 4:
                dtlayout(dqmitems, name,[{ 'path': histo_name_SL1}],
                                        [{ 'path': histo_name_SL2}],
                                        [{ 'path': histo_name_SL3}])
            else:
                dtlayout(dqmitems, name,[{ 'path': histo_name_SL1}],
                                        [{ 'path': histo_name_SL3}])

## EVENT SIZE #################################################################################

for fed in range(1369, 1372):
   name = f"03-FEDEventSize/FED{fed}"
   histo_name = f"DT/00-DataIntegrity/FED{fed}/FED{fed}_EventLength"
   dtlayout(dqmitems, name,[{ 'path': histo_name}])
   for u_ros in range(1, 13):
       name = f"04-ROSEventSize/FED{fed}_uROS{u_ros}"
       histo_name = f"DT/00-DataIntegrity/FED{fed}/uROS{u_ros}/FED{fed}_uROS{u_ros}_EventLength"
       dtlayout(dqmitems, name,[{ 'path': histo_name}])

#### TRIGGER SYNCH ##############################################################################

for wheel in range(-2, 3):
    name = f"05-TriggerSynch/01-CorrectBX_In_Wh{wheel}_TM"
    histo_name = f"DT/03-LocalTrigger-TM/Wheel{wheel}/TM_CorrectBXPhiIn_W{wheel}"
    dtlayout(dqmitems, name,[{ 'path': histo_name}])
    name = f"05-TriggerSynch/Peak-Mean/01-Peak-Mean_In_Wh{wheel}_TM"
    histo_name = f"DT/03-LocalTrigger-TM/Wheel{wheel}/TM_ResidualBXPhiIn_W{wheel}"
    dtlayout(dqmitems, name,[{ 'path': histo_name}])
    name = f"05-TriggerSynch/01-CorrectBX_Out_Wh{wheel}_TM"
    histo_name = f"DT/03-LocalTrigger-TM/Wheel{wheel}/TM_CorrectBXPhiOut_W{wheel}"
    dtlayout(dqmitems, name,[{ 'path': histo_name}])
    name = f"05-TriggerSynch/Peak-Mean/01-Peak-Mean_Out_Wh{wheel}_TM"
    histo_name = f"DT/03-LocalTrigger-TM/Wheel{wheel}/TM_ResidualBXPhiOut_W{wheel}"
    dtlayout(dqmitems, name,[{ 'path': histo_name}])
    name = f"05-TriggerSynch/01-CorrectBX_Theta_Wh{wheel}_TM"
    histo_name = f"DT/03-LocalTrigger-TM/Wheel{wheel}/TM_CorrectBXTheta_W{wheel}"
    dtlayout(dqmitems, name,[{ 'path': histo_name}])


#### TRIGGER BASICS ##############################################################################

for wheel in range(-2, 3):
    name = f"06-TriggerBasics/01-CorrFraction_In_Wh{wheel}_TM"
    histo_name = f"DT/03-LocalTrigger-TM/Wheel{wheel}/TM_CorrFractionPhiIn_W{wheel}"
    dtlayout(dqmitems, name,[{ 'path': histo_name}])
    name = f"06-TriggerBasics/03-2ndFractionPhi_In_Wh{wheel}"
    histo_name = f"DT/03-LocalTrigger-TM/Wheel{wheel}/TM_2ndFractionPhiIn_W{wheel}"
    dtlayout(dqmitems, name,[{ 'path': histo_name}])
    name = f"06-TriggerBasics/01-CorrFraction_Out_Wh{wheel}_TM"
    histo_name = f"DT/03-LocalTrigger-TM/Wheel{wheel}/TM_CorrFractionPhiOut_W{wheel}"
    dtlayout(dqmitems, name,[{ 'path': histo_name}])
    name = f"06-TriggerBasics/03-2ndFractionPhi_Out_Wh{wheel}"
    histo_name = f"DT/03-LocalTrigger-TM/Wheel{wheel}/TM_2ndFractionPhiOut_W{wheel}"
    dtlayout(dqmitems, name,[{ 'path': histo_name}])

## TRIGGER POS LUTs ###########################################################################

for wheel in range(-2, 3):
    for sector in range (1, 13):
        name = f"07-TriggerPosLUTs/Wheel{wheel}/Sec{sector} In"
        histo_name = f"DT/03-LocalTrigger-TM/Wheel{wheel}/Sector{sector}/Station{{station}}/Segment/TM_PhiResidualIn_W{wheel}_Sec{sector}_St{{station}}"
        histo_name_1 = histo_name.format(station = 1)
        histo_name_2 = histo_name.format(station = 2)
        histo_name_3 = histo_name.format(station = 3)
        histo_name_4 = histo_name.format(station = 4)
        dtlayout(dqmitems, name,[{ 'path': histo_name_1},{ 'path': histo_name_2}],
                                [{ 'path': histo_name_3},{ 'path': histo_name_4}])

        name = f"07-TriggerPosLUTs/Wheel{wheel}/Sec{sector} Out"
        histo_name = f"DT/03-LocalTrigger-TM/Wheel{wheel}/Sector{sector}/Station{{station}}/Segment/TM_PhiResidualOut_W{wheel}_Sec{sector}_St{{station}}"
        histo_name_1 = histo_name.format(station = 1)
        histo_name_2 = histo_name.format(station = 2)
        histo_name_3 = histo_name.format(station = 3)
        histo_name_4 = histo_name.format(station = 4)
        dtlayout(dqmitems, name,[{ 'path': histo_name_1},{ 'path': histo_name_2}],
                                [{ 'path': histo_name_3},{ 'path': histo_name_4}])

#### TRIGGER DIR LUTs ###########################################################################

for wheel in range(-2, 3):
    for sector in range (1, 13):
        name = f"08-TriggerDirLUTs/Wheel{wheel}/Sec{sector} In"
        histo_name = f"DT/03-LocalTrigger-TM/Wheel{wheel}/Sector{sector}/Station{{station}}/Segment/TM_PhibResidualIn_W{wheel}_Sec{sector}_St{{station}}"
        histo_name_1 = histo_name.format(station = 1)
        histo_name_2 = histo_name.format(station = 2)
        histo_name_3 = histo_name.format(station = 3)
        histo_name_4 = histo_name.format(station = 4)
        dtlayout(dqmitems, name,[{ 'path': histo_name_1},{ 'path': histo_name_2}],
                                [{ 'path': histo_name_3},{ 'path': histo_name_4}])

        name = f"08-TriggerDirLUTs/Wheel{wheel}/Sec{sector} Out"
        histo_name = f"DT/03-LocalTrigger-TM/Wheel{wheel}/Sector{sector}/Station{{station}}/Segment/TM_PhibResidualOut_W{wheel}_Sec{sector}_St{{station}}"
        histo_name_1 = histo_name.format(station = 1)
        histo_name_2 = histo_name.format(station = 2)
        histo_name_3 = histo_name.format(station = 3)
        histo_name_4 = histo_name.format(station = 4)
        dtlayout(dqmitems, name,[{ 'path': histo_name_1},{ 'path': histo_name_2}],
                                [{ 'path': histo_name_3},{ 'path': histo_name_4}])

#### HITS PER SEGMENT ###########################################################################

for wheel in range(-2, 3):
    for station in range (1, 5):
        for sector in range (1, 15):
            if station != 4 and (sector == 13 or sector == 14):
               continue
            name = f"09-Nhits/Wheel{wheel}/Sector{sector}_Station{station}"
            histo_name = f"DT/02-Segments/Wheel{wheel}/Sector{sector}/Station{station}/h4DSegmNHits_W{wheel}_St{station}_Sec{sector}"
            dtlayout(dqmitems, name,[{ 'path': histo_name}])

#### SEGMENTS RESIDUALS #########################################################################

for wheel in range(-2, 3):
    for station in range (1, 5):
        for sector in range (1, 15):
            if station != 4 and (sector == 13 or sector == 14):
               continue
            for sl in range (1, 4):
                if sl == 2 and (sector == 13 or sector == 14 or station == 4):
                   continue
                name = f"10-Segments/Wheel{wheel}/Sector{sector}_Station{station}_SL{sl}"
                histo_name = f"DT/02-Segments/Wheel{wheel}/Sector{sector}/Station{station}/hResDist_W{wheel}_St{station}_Sec{sector}_SL{sl}"
                dtlayout(dqmitems, name,[{ 'path': histo_name}])

#### QUALITY vs PHI RAD ############################################################################

for wheel in range(-2, 3):
    for station in range (1, 5):
        for sector in range (1, 13):
            name = f"11-TriggerQualityVsPhi/Wheel{wheel}/Sector{sector}_Station{station}"
            histo_name = f"DT/03-LocalTrigger-TM/Wheel{wheel}/Sector{sector}/Station{station}/LocalTriggerPhiIn/TM_QualvsPhirad_In_W{wheel}_Sec{sector}_St{station}"
            dtlayout(dqmitems, name,[{ 'path': histo_name}])

#### TRIGGER THETA #################################################################################

for wheel in range(-2, 3):
    for station in range (1, 4):
        for sector in range (1, 13):
            name = f"12-TriggerTheta/Wheel{wheel}/Sector{sector}_Station{station}"
            histo_name = f"DT/03-LocalTrigger-TM/Wheel{wheel}/Sector{sector}/Station{station}/LocalTriggerTheta/TM_PositionvsQual_W{wheel}_Sec{sector}_St{station}"
            dtlayout(dqmitems, name,[{ 'path': histo_name}])
