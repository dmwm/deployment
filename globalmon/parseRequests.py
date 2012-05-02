#!/usr/bin/env python2.6

import sys,os,json,subprocess,shlex
from datetime import datetime
current = datetime.utcnow()

dbscmd='dbs search --production --noheader '

requests = json.load(sys.stdin)

good_status = ['new', 'assignment-approved', 'acquired','running']

keys = []
details_keys = []
details2_keys = []
results = {}
slots_assign = {'t1' : 20000, 't1_highprio' : 12000, 'mc' : 20000, 'mc_highprio' : 12000, 'production' : 20000}
site_slots = {'T1_US_FNAL': 10000, 'T1_TW_ASGC': 1500, 'T1_FR_CCIN2P3': 3000, 'T1_IT_CNAF': 2200, 'T1_ES_PIC': 1200, 'T1_DE_KIT': 3000, 'T1_UK_RAL': 2000}

for request in requests:
    status = request['status']
    request_name = request['request_name']
    # print request_name,status
    if status not in good_status: continue
    if 'details' not in request.keys() :
        print 'request',request_name,'does not have a details block'
        continue
    if 'details2' not in request.keys() :
        print 'request',request_name,'does not have a details2 block'
        continue
    for key in request.keys():
        if key not in keys: keys.append(key)
    for key in request['details'].keys():
        if key not in details_keys: details_keys.append(key)
    for key in request['details2'].keys():
        if key not in details2_keys: details2_keys.append(key)

    if 'Assignments' in request['details2'].keys():
        assignments = request['details2']['Assignments']
        if len(assignments) > 0 :
            local_queue = assignments[0]
        else:
            local_queue = None
    elif 'local_queue' in request.keys():
        local_queue = request['local_queue'][0].split('http://')[1].split(':')[0]
    else:
        local_queue = None

    if local_queue not in results.keys(): results[local_queue] = {}

    if status not in results[local_queue].keys(): results[local_queue][status] = {}

    tmp = {}
    t1Sites = request.get('Site Whitelist', [])
    if t1Sites == []: t1Sites = request['details'].get('Site Whitelist', [])
    if t1Sites == []: t1Sites = request['details2'].get('Site Whitelist', [])
    tmp["t1_sites"] = []
    for site in t1Sites:
        if site.startswith('T1'):
            tmp["t1_sites"].append(site)

    priority = int(request['details']['RequestPriority'])
    if priority not in results[local_queue][status].keys(): results[local_queue][status][priority] = []
    tmp["request_name"] = request["request_name"]
    tmp["RequestType"] = request["type"]
    tmp["status"] = request["status"]
    if tmp["RequestType"] == 'MonteCarlo':
        # use input number of events
        tmp["RequestNumEvents"] = int(request['details'].get("RequestNumEvents", -1))
        if tmp["RequestNumEvents"] == -1 : tmp["RequestNumEvents"] = int(request['details'].get("RequestSizeEvents",0))
        # calculate CPUHours assuming 100s per event if not specified
        if 'TimePerEvent' in request['details']:
            tmp["TimePerEvent"] = float(request['details']["TimePerEvent"])
        else :
            tmp["TimePerEvent"] = 100.
        # print 'tmp["TimePerEvent"]',tmp["TimePerEvent"]
        # print 'tmp["RequestNumEvents"]',tmp["RequestNumEvents"]
        tmp["CPUHours"] = tmp["RequestNumEvents"] * tmp["TimePerEvent"] / 3600.
    else:
        # query das for input dataset
        tmp["RequestNumEvents"] = None
        tmp["InputDataset"] = None
        if "InputDataset" in request.keys(): tmp["InputDataset"] = request["InputDataset"]
        if tmp["InputDataset"] == None and "InputDataset" in request['details'].keys(): tmp["InputDataset"] = request['details']["InputDataset"]
        if tmp["InputDataset"] == None and "InputDataset" in request['details2'].keys(): tmp["InputDataset"] = request['details2']["InputDataset"]
        if tmp["InputDataset"] == None :
            print "InputDataset could not be determined for workflow",tmp["request_name"]
            tmp["CPUHours"] = 0.
            tmp["TimePerEvent"] = 0.
            continue
        tmp['BlockWhitelist'] = request['details'].get('BlockWhitelist', None)
        if tmp['BlockWhitelist'] == None : tmp['BlockWhitelist'] =  request['details2'].get('BlockWhitelist', [])
        tmp['RunWhitelist'] = request['details'].get('RunWhitelist', None)
        if tmp['RunWhitelist'] == None : tmp['RunWhitelist'] = request['details2'].get('RunWhitelist', [])
        #commandline = dbscms+'search --query="find dataset,dataset.status,sum(block.numevents) where dataset = '+str(tmp["InputDataset"])
        if len(tmp['BlockWhitelist']) > 0:
            i = 0
            evnts = 0
            while i < len(tmp['BlockWhitelist']):
                j = 1
                commandline = dbscmd+'search --query="find dataset,dataset.status,sum(block.numevents) where dataset = '+ str(tmp["InputDataset"]) + ' and ('
                while j < 20 and i + j < len(tmp['BlockWhitelist']):
                    commandline += ' block = ' + str(tmp['BlockWhitelist'][i + j]) + ' or'
                    j += 1
                commandline += ' block = ' + str(tmp['BlockWhitelist'][i]) + ')" --noheader --production'
                i += j
                localargs = shlex.split(commandline)
                output = subprocess.Popen(localargs, shell=False, stdout=subprocess.PIPE)
                lines = output.communicate()[0].split('\n')
                if len(lines) < 1:
                    print 'something wrong with:',commandline
                    break
                else:
                    evnts += int(lines[0].split()[2])
            else:
                tmp["RequestNumEvents"] = evnts
        elif len(tmp['RunWhitelist']) > 0:
            i = 0
            evnts = 0
            while i < len(tmp['RunWhitelist']):
                j = 1
                commandline = dbscmd+'search --query="find dataset,dataset.status,sum(block.numevents) where dataset = '+ str(tmp["InputDataset"]) + ' and ('
                while j < 30 and i + j < len(tmp['RunWhitelist']):
                    commandline += ' run = ' + str(tmp['RunWhitelist'][i + j]) + ' or'
                    j += 1
                commandline += ' run = ' + str(tmp['RunWhitelist'][i]) + ')" --noheader --production'
                i += j
                localargs = shlex.split(commandline)
                output = subprocess.Popen(localargs, shell=False, stdout=subprocess.PIPE)
                lines = output.communicate()[0].split('\n')
                if len(lines) < 1:
                    print 'something wrong with:',commandline
                    break
                else:
                    evnts += int(lines[0].split()[2])
            else:
                tmp["RequestNumEvents"] = evnts
        else:
            commandline = dbscmd+'search --query="find dataset,dataset.status,sum(block.numevents) where dataset = '+str(tmp["InputDataset"]) + '" --noheader --production'
            localargs = shlex.split(commandline)
            output = subprocess.Popen(localargs, shell=False, stdout=subprocess.PIPE)
            lines = output.communicate()[0].split('\n')
            if len(lines) < 1:
                print 'something wrong with:',commandline
            else:
                tmp["RequestNumEvents"] = int(lines[0].split()[2])
        # das_result = json.loads(get_data('https://cmsweb.cern.ch', 'dataset='+tmp["InputDataset"]+' | grep dataset.nevents',0,0,False))
        # print das_result
        # for item in das_result['data'][0]['dataset']:
        #     if 'nevents' in item.keys():
        #         tmp["RequestNumEvents"] = item['nevents']
        #         break
        if tmp["RequestNumEvents"] == None :
            print "Could not determine number of events for dataset",tmp["InputDataset"]
        else:
            tmp['FilterEfficiency'] = request.get('FilterEfficiency', None)
            if tmp['FilterEfficiency'] == None : tmp['FilterEfficiency'] = request['details'].get('FilterEfficiency', None)
            if tmp['FilterEfficiency'] == None : tmp['FilterEfficiency'] = request['details2'].get('FilterEfficiency', None)
            if tmp['FilterEfficiency'] != None :
                tmp['RequestNumEvents'] *= float(tmp['FilterEfficiency'])
                tmp['RequestNumEvents'] = int(tmp['RequestNumEvents'])
        if tmp["RequestType"] == 'ReDigi':
            tmp["TimePerEvent"] = 30.
        elif tmp["RequestType"] == 'ReReco':
            tmp["TimePerEvent"] = 30.
        elif tmp["RequestType"] == 'MonteCarloFromGEN':
            if 'TimePerEvent' in request['details']:
                tmp["TimePerEvent"] = float(request['details']["TimePerEvent"])
            else :
                tmp["TimePerEvent"] = 100.
        else:
            tmp["TimePerEvent"] = 30.
        tmp["CPUHours"] = tmp["RequestNumEvents"] * tmp["TimePerEvent"] / 3600.
    tmp['OutputDatasets'] = request['OutputDatasets']
    tmp['OutputEvents'] = {}
    tmp['CompletionPercentage'] = {}
    for outputDataset in tmp['OutputDatasets']:
        if tmp["status"] == "running":
            dataTier = str(outputDataset)[1:].split('/')[2]
            acqEra = str(outputDataset)[1:].split('/')[1]
            if acqEra != 'None-None':
                commandline = dbscmd+'search --query="find dataset,dataset.status,sum(block.numevents) where dataset = '+str(outputDataset) + '" --noheader --production'
                localargs = shlex.split(commandline)
                output = subprocess.Popen(localargs, shell=False, stdout=subprocess.PIPE)
                lines = output.communicate()[0].split('\n')
                if len(lines) < 1 or lines == ['']:
                    tmp["OutputEvents"][dataTier] = 0
                else:
                    tmp["OutputEvents"][dataTier] = int(lines[0].split()[2])
            else:
                tmp["OutputEvents"][dataTier] = 0
            tmp["CompletionPercentage"][dataTier] = float(tmp["OutputEvents"][dataTier])/float(tmp["RequestNumEvents"])
    results[local_queue][status][priority].append(tmp)

print '--------------------------------------------------------------------------------'
print 'Report generated on',current,'UTC'
print '--------------------------------------------------------------------------------'

sorted_local_queues = results.keys()
sorted_local_queues.sort()
team_summary = {}
site_summary = {}
for local_queue in sorted_local_queues:
    print ''
    print ''
    print 'team:',local_queue
    print '============================================'
    team_total_CPU = 0.0
    for status in good_status:
        if status not in results[local_queue].keys(): continue
        print ''
        print 'status:',status
        print '--------------------------------------------'
        sorted_priority = results[local_queue][status].keys()
        sorted_priority.sort(reverse=True)
        for priority in sorted_priority:
            for item in results[local_queue][status][priority]:
                dataTiers = '['
                completionPercentage = '['
                for dataTier in item["OutputEvents"].keys():
                    dataTiers += '%s,' % dataTier
                    completionPercentage += '%3.1f,' % (item["CompletionPercentage"][dataTier]*100)
                dataTiers = dataTiers[:-1] + ']'
                completionPercentage = completionPercentage[:-1] + ']'
                assignedT1 = ''
                if len(item["t1_sites"]) > 0:
                    assignedT1 = item["t1_sites"][0]
                    if item["t1_sites"][0] not in site_summary:
                        site_summary[item["t1_sites"][0]] = {'totalCPUHours' : 0, 'workflows': 1}
                    else:
                        site_summary[item["t1_sites"][0]]['workflows'] += 1

                if status == "acquired":
                    print "Priority: %10i Type: %20s InputEvents: %12i TimePerEvent: %5i CPUHours: %12i AssignedT1: %15s Request: %s" % (priority,item["RequestType"],item["RequestNumEvents"],item["TimePerEvent"],item["CPUHours"],assignedT1,item["request_name"])
                elif status == "running":
                    print "Priority: %10i Type: %20s InputEvents: %12i TimePerEvent: %5i CPUHours: %12i DataTiers: %30s CompletionPercentages: %20s AssignedT1: %15s Request: %s" % (priority,item["RequestType"],item["RequestNumEvents"],item["TimePerEvent"],item["CPUHours"],dataTiers,completionPercentage,assignedT1,item["request_name"])
                else:
                    print "Priority: %10i Type: %20s InputEvents: %12i TimePerEvent: %5i CPUHours: %12i Request: %s" % (priority,item["RequestType"],item["RequestNumEvents"],item["TimePerEvent"],item["CPUHours"],item["request_name"])
                if len(item['CompletionPercentage']) == 0:
                    team_total_CPU += item["CPUHours"]
                    if len(item["t1_sites"]) > 0:
                        site_summary[item["t1_sites"][0]]['totalCPUHours'] += item["CPUHours"]
                else:
                    usablePercentages = {}
                    for tier in item['CompletionPercentage'].keys():
                        if tier != 'DQM':
                            usablePercentages[tier] = item['CompletionPercentage'][tier]
                    team_total_CPU += item["CPUHours"]*(1.0 - min(usablePercentages.values()))
                    if len(item["t1_sites"]) > 0:
                        site_summary[item["t1_sites"][0]]['totalCPUHours'] += item["CPUHours"]*(1.0 - min(usablePercentages.values()))
    team_summary[local_queue] = {'cpuHours' : team_total_CPU, 'days' : 0, 'hours' : 0}
    if local_queue in slots_assign.keys():
        total_hours = team_total_CPU/slots_assign[local_queue]
        days = int(total_hours/24)
        hours = total_hours%24
        team_summary[local_queue]['days'] = days
        team_summary[local_queue]['hours'] = hours

print ''
print ''
print 'Team summary:'
print '============================================'
for team in sorted(team_summary.keys(), key = lambda x: team_summary[x]['cpuHours'], reverse=True):
    print 'team: %12s CPU Hours remaining: %12d "Real" time remaining: %3d days %2d hours Approximated slots: %2dk' %  (team, team_summary[team]['cpuHours'], team_summary[team]['days'], team_summary[team]['hours'], slots_assign.get(team, 0)/1000)

print ''
print ''
print 'Custodial T1 Site summary:'
print '============================================'
for site in sorted(site_summary.keys(), key = lambda x: site_summary[x]['totalCPUHours'], reverse=True):
    print 'site: %14s CPU Hours remaining: %12d Workflows assigned: %4d maximum slots: %5d' % (site, site_summary[site]['totalCPUHours'], site_summary[site]['workflows'], site_slots[site])
