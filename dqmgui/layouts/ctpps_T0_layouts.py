def CTPPSTrackingStripLayout(i, p, *rows): i["CTPPS/TrackingStrip/Layouts/" + p] = DQMItem(layout=rows)
def CTPPSTrackingPixelLayout(i, p, *rows): i["CTPPS/TrackingPixel/Layouts/" + p] = DQMItem(layout=rows)
def CTPPSTimingDiamondLayout(i, p, *rows): i["CTPPS/TimingDiamond/Layouts/" + p] = DQMItem(layout=rows)

strips_stations = [ "sector 45/station 210", "sector 56/station 210" ]
strips_units = [ "nr", "fr" ]

pixstations = [ "sector 45/station 220/", "sector 56/station 220/" ]
planes  = [ "0","1","2" ]
planes2 = [ "3","4","5" ]

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
TimingPlots = [ "activity per BX 0 25", "active planes", "event category", "leading edge (le and te)", "time over threshold", "hits in planes", "hits in planes lumisection", "tracks", "HPTDC Errors", "MH in channels" ]
TimingDrawOpt = [{'ytype':"log"}, {'xmax':"10"}, {'drawopts':"colztext"}, {'xmax':"25"}, {'xmin':"0", 'xmax':"25"}, {'withref':"no"}, {'withref':"no"}, {'withref':"no"}, {'xmax':"100"}, {'drawopts':"colztext"}]

for i in range(len(TimingPlots)):
  rows = list()
  for station in diamond_stations:
    row = list()
    path_str = "CTPPS/TimingDiamond/"+station+"/"+TimingPlots[i]
    row.append( { "path" : path_str, 'draw':TimingDrawOpt[i] } )
    rows.append(row)

  CTPPSTimingDiamondLayout(dqmitems, TimingPlots[i], *rows)


#for station in diamond_stations:
#plot = "activity per BX 0 25"
  #CTPPSTimingDiamondLayout(dqmitems, plot, [{'path': "CTPPS/TimingDiamond/"+station+"/"+plot, 'description':'blablabla', 'draw':{'xtype':'log','ymin':0,'ymax':10,'drawopts':"COLZ"} }])

# clocks display for both sectors
rows = list()
for station in diamond_stations:
  row = list()
  for clk in [ 1, 3 ]:
    hist_lead = "CTPPS/TimingDiamond/"+station+"/clock/clock{clock_id} leading edge".format(clock_id=clk)
    row.append( { "path": hist_lead, 'draw':{'xmax':"25"} } )
  rows.append(row)

  CTPPSTimingDiamondLayout(dqmitems, "clocks edges", *rows)
  
###
#####   CTPPS Pixel Layouts
###

for plot in ["planes activity", "hit multiplicity in planes","hit average multiplicity in planes"]:
  rows = list()
  for station in pixstations:
    row = list()
    row.append("CTPPS/TrackingPixel/"+station+plot)
    rows.append(row)

  CTPPSTrackingPixelLayout(dqmitems, plot, *rows)

for plot in ["4 fired ROCs per BX"]:
  rows = list()
  for station in pixstations:
    row = list()
    row.append("CTPPS/TrackingPixel/"+station+"fr_hr/latency/"+plot)
    rows.append(row)

  CTPPSTrackingPixelLayout(dqmitems, plot, *rows)

for plot in ["5 fired planes per BX","ROCs hits multiplicity per event","ROCs_hits_multiplicity_per_event vs LS","number of fired planes per event","number of fired aligned_ROCs per event"]:
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
