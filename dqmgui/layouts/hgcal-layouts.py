def hgcallayout(i, p, *rows): i["HGCAL/Layouts/" + p] = DQMItem(layout=rows)

########### define varialbles for frequently used strings #############
hgcallink = "   >>> <a href=https://hgcaldocs.web.cern.ch/>Description</a>"
quality = "summary of module status"
summary = "wafer map for hgcal"
digis = "digis information"

################### Links to TOP Summary Histograms #################################
hgcallayout(dqmitems, "01-econdPayload",
          [{ 'path': "HGCAL/Digis/econdPayload", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "02-econdQualityH",
          [{ 'path': "HGCAL/Digis/econdQualityH", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "03-cbQualityH",
          [{ 'path': "HGCAL/Digis/cbQualityH", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "04-Module0-avgadc",
          [{ 'path': "HGCAL/Modules/hex_avgadc_module_0", 'description': summary + hgcallink }])
hgcallayout(dqmitems, "05-Module1-avgadc",
          [{ 'path': "HGCAL/Modules/hex_avgadc_module_1", 'description': summary + hgcallink }])
hgcallayout(dqmitems, "06-Module2-avgadc",
          [{ 'path': "HGCAL/Modules/hex_avgadc_module_2", 'description': summary + hgcallink }])
hgcallayout(dqmitems, "07-Module3-avgadc",
          [{ 'path': "HGCAL/Modules/hex_avgadc_module_3", 'description': summary + hgcallink }])
hgcallayout(dqmitems, "08-Module4-avgadc",
          [{ 'path': "HGCAL/Modules/hex_avgadc_module_4", 'description': summary + hgcallink }])
hgcallayout(dqmitems, "09-Module5-avgadc",
          [{ 'path': "HGCAL/Modules/hex_avgadc_module_5", 'description': summary + hgcallink }])
hgcallayout(dqmitems, "10-digis0-adc",
          [{ 'path': "HGCAL/Digis/adc_module_0", 'description': digis + hgcallink }])
hgcallayout(dqmitems, "11-digis1-adc",
          [{ 'path': "HGCAL/Digis/adc_module_1", 'description': digis + hgcallink }])
hgcallayout(dqmitems, "12-digis2-adc",
          [{ 'path': "HGCAL/Digis/adc_module_2", 'description': digis + hgcallink }])
hgcallayout(dqmitems, "13-digis3-adc",
          [{ 'path': "HGCAL/Digis/adc_module_3", 'description': digis + hgcallink }])
hgcallayout(dqmitems, "14-digis4-adc",
          [{ 'path': "HGCAL/Digis/adc_module_4", 'description': digis + hgcallink }])
hgcallayout(dqmitems, "15-digis5-adc",
          [{ 'path': "HGCAL/Digis/adc_module_5", 'description': digis + hgcallink }])
