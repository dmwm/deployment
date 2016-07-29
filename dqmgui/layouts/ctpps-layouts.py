def CTPPSTrackingStripLayout(i, p, *rows): i["CTPPS/TrackingStrip/Layouts/" + p] = DQMItem(layout=rows)

stations = [ "sector 45/station 210", "sector 56/station 210" ]
units = [ "nr", "fr" ]


# layouts with no overlays
for plot in [ "active planes", "activity in planes (2D)", "vfats with any problem", "track XY profile" ]:
  rows = list()
  for station in stations:
    row = list()
    for unit in units:
      row.append("CTPPS/TrackingStrip/"+station+"/"+unit+"_hr/"+plot)
    rows.append(row)

  CTPPSTrackingStripLayout(dqmitems, plot, *rows)


# layouts with overlays
for plot in [ "active planes", "recognized patterns", "planes contributing to fit" ]:
  rows = list()
  for station in stations:
    row = list()
    for unit in units:
      hist_u = "CTPPS/TrackingStrip/"+station+"/"+unit+"_hr/"+plot + " U"
      hist_v = "CTPPS/TrackingStrip/"+station+"/"+unit+"_hr/"+plot + " V"
      row.append( { "path" : hist_u, "overlays" : [ hist_v ] } )
    rows.append(row)

  CTPPSTrackingStripLayout(dqmitems, plot + " UV", *rows)


# per-BX plots
for suffix in [ "", " (short)" ]:
  plot_list = list()
  for station in stations:
    for unit in units:
      plot_list.append("CTPPS/TrackingStrip/"+station+"/"+unit+"_hr/activity per BX" + suffix)

  base_plot = "CTPPS/events per BX" + suffix
  CTPPSTrackingStripLayout(dqmitems, "activity per BX" + suffix, [ { "path" : base_plot, "overlays" : plot_list } ])
