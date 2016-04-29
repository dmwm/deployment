def totemlayout(i, p, *rows): i["Totem/Layouts/" + p] = DQMItem(layout=rows)

# layouts with no overlays
for plot in [ "activity in planes (2D)", "vfats with any problem", "active planes", "track XY profile" ]:
  for sector in [ "sector 45", "sector 56" ]:
    totemlayout(dqmitems, sector + "/" + plot,
        [ "Totem/RP/"+sector+"/station 210/nr_tp/"+plot, "Totem/RP/"+sector+"/station 210/fr_tp/"+plot, "Totem/RP/"+sector+"/station 220/nr_tp/"+plot, "Totem/RP/"+sector+"/station 220/fr_tp/"+plot ],
        [ "Totem/RP/"+sector+"/station 210/nr_hr/"+plot, "Totem/RP/"+sector+"/station 210/fr_hr/"+plot, "Totem/RP/"+sector+"/station 220/nr_hr/"+plot, "Totem/RP/"+sector+"/station 220/fr_hr/"+plot ],
        [ "Totem/RP/"+sector+"/station 210/nr_bt/"+plot, "Totem/RP/"+sector+"/station 210/fr_bt/"+plot, "Totem/RP/"+sector+"/station 220/nr_bt/"+plot, "Totem/RP/"+sector+"/station 220/fr_bt/"+plot ]
    )

# layouts with overlays
# TODO: this creates an error when server started
#for plot in [ "active planes projection", "planes contributing to fit", "recognized patterns", "track profile" ]:
#  for sector in [ "sector 45", "sector 56" ]:
#    totemlayout(dqmitems, sector + "/" + plot,
#        [ { "path" : "Totem/RP/"+sector+"/station 210/nr_tp/"+plot+" U", "overlays" : { "Totem/RP/"+sector+"/station 210/nr_tp/"+plot+" V" } } ]
#    )
