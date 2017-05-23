def CTPPSTrackingStripLayout(i, p, *rows): i["CTPPS/TrackingStrip/Layouts/" + p] = DQMItem(layout=rows)
def CTPPSTimingDiamondLayout(i, p, *rows): i["CTPPS/TimingDiamond/Layouts/" + p] = DQMItem(layout=rows)

strips_stations = [ "sector 45/station 210", "sector 56/station 210" ]
strips_units = [ "nr", "fr" ]

diamond_stations = [ "sector 45/station 220cyl/cyl_hr", "sector 56/station 220cyl/cyl_hr" ]

# layouts with no overlays
for plot in [ "active planes", "activity in planes (2D)", "vfats with any problem", "track XY profile" ]:
  rows = list()
  for station in strips_stations:
    row = list()
    for unit in strips_units:
      row.append("CTPPS/TrackingStrip/"+station+"/"+unit+"_hr/"+plot)
    rows.append(row)

  CTPPSTrackingStripLayout(dqmitems, plot, *rows)


# layouts with overlays
for plot in [ "active planes", "recognized patterns", "planes contributing to fit" ]:
  rows = list()
  for station in strips_stations:
    row = list()
    for unit in strips_units:
      hist_u = "CTPPS/TrackingStrip/"+station+"/"+unit+"_hr/"+plot + " U"
      hist_v = "CTPPS/TrackingStrip/"+station+"/"+unit+"_hr/"+plot + " V"
      row.append( { "path" : hist_u, "overlays" : [ hist_v ] } )
    rows.append(row)

  CTPPSTrackingStripLayout(dqmitems, plot + " UV", *rows)

# per-BX plots
for suffix in [ "", " (short)" ]:
  plot_list = list()
  for station in strips_stations:
    for unit in strips_units:
      plot_list.append("CTPPS/TrackingStrip/"+station+"/"+unit+"_hr/activity per BX" + suffix)

  base_plot = "CTPPS/events per BX" + suffix
  CTPPSTrackingStripLayout(dqmitems, "activity per BX" + suffix, [ { "path" : base_plot, "overlays" : plot_list } ])

#####
# Diamond detectors layouts
#####

# layouts with no overlays
for plot in [ "activity per BX", "active planes", "leading edges without trailing", "leading edge", "time over threshold", "HPTDC Errors", "hits in planes" ]:
  rows = list()
  for station in diamond_stations:
    row = list()
    row.append("CTPPS/TimingDiamond/"+station+"/"+plot)
    rows.append(row)

  CTPPSTimingDiamondLayout(dqmitems, plot, *rows)

# clocks display for both sectors
rows = list()
for station in diamond_stations:
  row = list()
  for clk in [ 1, 3 ]:
    hist_lead = "CTPPS/TimingDiamond/"+station+"/clock/clock{clock_id} leading edge".format(clock_id=clk)
    hist_trail = "CTPPS/TimingDiamond/"+station+"/clock/clock{clock_id} trailing edge".format(clock_id=clk)
    row.append( { "path": hist_lead, "overlays": [ hist_trail ] } )
  rows.append(row)

  CTPPSTimingDiamondLayout(dqmitems, "clocks edges", *rows)