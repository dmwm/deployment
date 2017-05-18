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

#
#####   CTPPS Pixel Layouts
#
def CTPPSTrackingPixelLayout(i, p, *rows): i["CTPPS/TrackingPixel/Layouts/" + p] = DQMItem(layout=rows)

pixstations = [ "sector 45/station 220/", "sector 56/station 220/" ]
planes  = [ "0","1","2" ]
planes2 = [ "3","4","5" ]

for plot in ["planes activity", "hit multiplicity in planes","hit average multiplicity in planes"]:
  rows = list()
  for station in pixstations:
    row = list()
    row.append("CTPPS/TrackingPixel/"+station+plot)
    rows.append(row)

  CTPPSTrackingPixelLayout(dqmitems, plot, *rows)

for plot in ["4 fired ROCs per BX", "5 fired planes per BX","ROCs hits multiplicity per event","number of fired planes per event","max number of fired aligned_ROCs per event"]:
  rows = list()
  for station in pixstations:
    row = list()
    row.append("CTPPS/TrackingPixel/"+station+"fr_hr/"+plot)
    rows.append(row)

  CTPPSTrackingPixelLayout(dqmitems, plot, *rows)

sectors = [ "sector 45", "sector 56" ]
for plot in ["hits position"]:
  for sector in sectors:
    rows = list()
    row = list()
    for plane in planes:
      row.append("CTPPS/TrackingPixel/"+sector+"/station 220/fr_hr/plane_"+plane+"/"+plot)
    rows.append(row)

    row = list()
    for plane in planes2:
      row.append("CTPPS/TrackingPixel/"+sector+"/station 220/fr_hr/plane_"+plane+"/"+plot)
    rows.append(row)

    CTPPSTrackingPixelLayout(dqmitems, plot+":" +sector+" station 220_fr_hr", *rows)

