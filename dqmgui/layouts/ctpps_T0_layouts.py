def totemlayout(i, p, *rows): i["CTPPS/Layouts/" + p] = DQMItem(layout=rows)

sectors = [ "sector 45", "sector 56" ]
units = [ "station 210/nr", "station 210/fr", "station 220/nr", "station 220/fr" ]
rps = [ "tp", "hr", "bt" ]

# layouts with no overlays
for plot in [ "activity in planes (2D)", "vfats with any problem", "active planes", "track XY profile" ]:
  for sector in sectors:
    rows = list()
    for rp in rps:
      row = list()
      for unit in units:
        row.append("CTPPS/TrackingStrip/"+sector+"/"+unit+"_"+rp+"/"+plot)
      rows.append(row)

    totemlayout(dqmitems, "TrackingStrip/" + sector + "/" + plot, *rows)

# layouts with overlays
for plot in [ "recognized patterns", "planes contributing to fit" ]:
  for sector in sectors:
    rows = list()
    for rp in rps:
      row = list()
      for unit in units:
        hist_u = "CTPPS/TrackingStrip/"+sector+"/"+unit+"_"+rp+"/"+plot + " U"
        hist_v = "CTPPS/TrackingStrip/"+sector+"/"+unit+"_"+rp+"/"+plot + " V"
        row.append( { "path" : hist_u, "overlays" : [ hist_v ] } )
      rows.append(row)

    totemlayout(dqmitems, "TrackingStrip/" + sector + "/" + plot, *rows)

# active planes overlay
for plot in [ "active planes" ]:
  for sector in sectors:
    rows = list()
    for rp in rps:
      row = list()
      for unit in units:
        hist_g = "CTPPS/TrackingStrip/"+sector+"/"+unit+"_"+rp+"/"+plot
        hist_u = "CTPPS/TrackingStrip/"+sector+"/"+unit+"_"+rp+"/"+plot + " U"
        hist_v = "CTPPS/TrackingStrip/"+sector+"/"+unit+"_"+rp+"/"+plot + " V"
        row.append( { "path" : hist_g, "overlays" : [ hist_u, hist_v ] } )
      rows.append(row)

    totemlayout(dqmitems, "TrackingStrip/" + sector + "/" + plot, *rows)
