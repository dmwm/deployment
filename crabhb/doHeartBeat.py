#!/usr/bin/env python2.6

# for command line options
from optparse import OptionParser

# iinteracting with the os
import os
import subprocess
from subprocess import Popen, PIPE, STDOUT

import sys

import csv

import matplotlib
from matplotlib.figure import Figure
import matplotlib.mlab as mlab


#from pylab import *
from operator import itemgetter, attrgetter

matplotlib.use('Agg')

import matplotlib.pyplot as plt

import numpy as np

# working with time
import time
from time import strftime, gmtime


# - Extend the doNothing.sh script?
# - Analyze time difference between timeStamps and output.txt


def parseParams() :

    # parse the command line options
    optParser = OptionParser()
    optParser.add_option("-s", "--server", dest="server", help="Name of the CRAB server to send the job to (CERN, UCSD_glite, UCSD_glidein, BARI, CERNslc5, UCSDtests_glite or UCSDtests_glidein)")
    optParser.add_option("-w", "--webdir", dest="webdir", help="Directory to copy html to (e.g. /afs/cern.ch/user/d/dlevans/public/www/HeartBeat/)")

    (options, args) = optParser.parse_args()
    if options.server == None or ( options.server != "CERN" and options.server != "UCSD_glite" and \
        options.server != "UCSD_glidein" and options.server != "BARI" and options.server != "CERNslc5" and \
        options.server != "UCSDtests_glite" and options.server != "UCSDtests_glidein" ) :
        pass
        #optParser.error("specify the -s argument! (CERN, UCSD_glite, UCSD_glidein, BARI, CERNslc5, UCSDtests_glite or UCSDtests_glidein)")
    if options.webdir == None:
        optParser.error("specify the -w argument! (e.g. /afs/cern.ch/user/d/dlevans/public/www/HeartBeat/)")

    params = ["", ""]
    params[0] = options.server
    params[1] = options.webdir
 
    print "CRABserver name: ", params[0]
    print "Webdir: ", params[1]
    
    return params


def makeUserScript(scriptFileName, scriptOutputFileName) :

    cmd = 'ls'
    p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    output = p.stdout.read()
    fileListing = output.split('\n')
    
    for file in fileListing :
        if file == scriptFileName :
            print "File", scriptFileName, "exists already and will be removed!"
    
    outFile = open(scriptFileName, 'w')
    
    outFile.write('#!/bin/bash')
    outFile.write('\n\n')
    outFile.write('# Script created by doHeartBeat.py that sleeps for ten minutes')
    outFile.write('\n\n')
    outFile.write('outFile=' + scriptOutputFileName + '\n\n')
    outFile.write('if [ -f $outFile ]; then\n\n')
    outFile.write('\t# outFile exists already, so remove it!\n')
    outFile.write('\trm $outFile\n\n')
    outFile.write('fi\n\n')
    outFile.write('beginTime=`date -u \'+%d%m%Y_%H%M%S\'`\n')
    outFile.write('echo \"Starting Job:  Time=$beginTime \" >> $outFile\n')
    outFile.write('echo \"Sleeping for 600 seconds\" >> $outFile\n')
    outFile.write('sleep 600\n')
    outFile.write('endTime=`date -u \'+%d%m%Y_%H%M%S\'`\n')
    outFile.write('echo \"Job ended:  Time=$endTime \" >> $outFile\n')

    outFile.close()
    
    print "Script", scriptFileName, "created."
    print "Output of this script will be written to", scriptOutputFileName

	

def makeCRABcfg(CRABcfgFileName, serverName, outputFile, UIWorkingDir, userScript) :
    
    outFile = open(CRABcfgFileName, 'w')
    
    outFile.write('[CRAB]\n')
    outFile.write('jobtype = cmssw\n')


    outFile.write('scheduler = glite\n')
    outFile.write('server_name = %s\n'%serverName)

    outFile.write('[CMSSW]\n')
    outFile.write('datasetpath = none\n')
    outFile.write('pset = none\n')
    outFile.write('number_of_jobs = 1\n')
    outFile.write('total_number_of_events = 1\n')
    outFile.write('output_file = ' + outputFile + '\n\n')
    outFile.write('[USER]\n')
    outFile.write('ui_working_dir = ' + UIWorkingDir + '\n')
    outFile.write('return_data = 1\n')
    outFile.write('copy_data = 0\n')
    outFile.write('script_exe = ' + userScript + '\n\n')
    outFile.write('[GRID]\n')
    outFile.write('rb = CERN\n')
    outFile.write('proxy_server = myproxy.cern.ch\n') #myproxy.cnaf.infn.it
    outFile.write('dont_check_proxy = 1\n')
    outFile.write('virtual_organization = cms\n')
    outFile.write('lcg_catalog_type = lfc\n')
    outFile.write('lfc_host = lfc-cms-test.cern.ch\n')
    outFile.write('lfc_home = /grid/cms\n')
    
    outFile.close()
    print "cfg file created", CRABcfgFileName

def submitCRABJob(CRABcfg) :
    
    print "Creating CRAB job:"
    
    cmd = 'crab -create -submit -cfg ' + CRABcfg
    p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    output = p.stdout.read()

    print output
    
    exitCode = p.poll()
    if exitCode != 0 and exitCode != "None":
        print "Error while creating and submitting CRAB job...\nExitCode = ", str(exitCode)


def checkStatus(CRABLogOutput, statusToCheck) :
    
    statusPassed = bool(False)
    
    splitted = CRABLogOutput.split(statusToCheck)
    if len(splitted) > 1 :
        statusPassed = bool(True)
    
    return statusPassed


def analyzeTimeStamps(timeStamps) :

    statusTimes = [-1 for col in range (9)]
    my_tup_status = ()
    my_dict_status = {}
    my_list_status = ['Begin','Created','Submitting','Submitted','Waiting','Ready','Scheduled','Running','Done']

    # statusTimes contains the total time for a given status
    # statusTimes[0] = time before first crab -status
    # statusTimes[1] = time while status is Created
    # statusTimes[2] = time while status is Submitting
    # statusTimes[3] = time while status is Submitted
    # statusTimes[4] = time while status is Waiting
    # statusTimes[5] = time while status is Ready
    # statusTimes[6] = time while status is Scheduled
    # statusTimes[7] = time while status is Running
    # statusTimes[8] = total time
    
    statusTimes[0] = time.mktime(timeStamps[0])
    
    if timeStamps[1] != timeStamps[0] :
        statusTimes[1] = time.mktime(timeStamps[1]) - time.mktime(timeStamps[0])
    
    # BUG: Diff between timeStamps[i] and timeStamps[0] never gets calculated!
    
    if timeStamps[2] != timeStamps[0] :
        for i in range(1, -1, -1) :
            if statusTimes[2] == -1 :
                if timeStamps[i] != timeStamps[0] :
                    statusTimes[2] = time.mktime(timeStamps[2]) - time.mktime(timeStamps[i])
                elif i == 0 :
                    statusTimes[2] = time.mktime(timeStamps[2]) - time.mktime(timeStamps[i])    
    
    if timeStamps[3] != timeStamps[0] :
        for i in range(2, -1, -1) :
            if statusTimes[3] == -1 :
                if timeStamps[i] != timeStamps[0] : 
                    statusTimes[3] = time.mktime(timeStamps[3]) - time.mktime(timeStamps[i])
                elif i == 0 :
                    statusTimes[3] = time.mktime(timeStamps[3]) - time.mktime(timeStamps[i])    
    
    if timeStamps[4] != timeStamps[0] :
        for i in range(3, -1, -1) :
            if statusTimes[4] == -1 :
                if timeStamps[i] != timeStamps[0] :
                    statusTimes[4] = time.mktime(timeStamps[4]) - time.mktime(timeStamps[i])
                elif i == 0 :
                    statusTimes[4] = time.mktime(timeStamps[4]) - time.mktime(timeStamps[i])    
    
    if timeStamps[5] != timeStamps[0] :
        for i in range(4, -1, -1) :
            if statusTimes[5] == -1 :
                if timeStamps[i] != timeStamps[0] :
                    statusTimes[5] = time.mktime(timeStamps[5]) - time.mktime(timeStamps[i])
                elif i == 0 :
                    statusTimes[5] = time.mktime(timeStamps[5]) - time.mktime(timeStamps[i])    
    
    if timeStamps[6] != timeStamps[0] :
        for i in range(5, -1, -1) :
            if statusTimes[6] == -1 :
                if timeStamps[i] != timeStamps[0] :
                    statusTimes[6]    = time.mktime(timeStamps[6]) - time.mktime(timeStamps[i])
                elif i == 0 :
                    statusTimes[6] = time.mktime(timeStamps[6]) - time.mktime(timeStamps[i])    
    
    if timeStamps[7] != timeStamps[0] :
        for i in range(6, -1, -1) :
            if statusTimes[7] == -1 :
                if timeStamps[i] != timeStamps[0] :
                    statusTimes[7]    = time.mktime(timeStamps[7]) - time.mktime(timeStamps[i])
                elif i == 0 :
                    statusTimes[7] = time.mktime(timeStamps[7]) - time.mktime(timeStamps[i])
    
#    print "BUG in totalTime calculation!!!"
#    #print "Due to the Submitting state which shows up twice..."
#    statusTimes[8] = 0
#    for i in range(1, 8) :
#        if statusTimes[i] > 0 :
#            statusTimes[8] = statusTimes[8] + statusTimes[i]
    if timeStamps[8] != timeStamps[0] :
        for i in range(7, -1, -1) :
            if statusTimes[8] == -1 :
                if timeStamps[i] != timeStamps[0] :
                    statusTimes[8]    = time.mktime(timeStamps[8]) - time.mktime(timeStamps[i])
                elif i == 0 :
                    statusTimes[8] = time.mktime(timeStamps[8]) - time.mktime(timeStamps[i])

    for i in range(1, 9) :
        my_tup_status = (i,statusTimes[i],statusTimes[0])
        my_dict_status[my_list_status[i]] =  my_tup_status
  
    return my_dict_status

def writeDataCSVFile(status_time,websitePath) :
    wp = websitePath+"/data.csv"
    f = open(wp, "wb")
    csv.writer(f).writerow(["status","sr#","duration","begin"])
    csv.writer(f).writerows((k,) + v for k, v in status_time.iteritems())
    f.close()

def writeHBCSVFile(hb_data,websitePath) :
    wp = websitePath+"/hb.csv"
    #print "wp :", wp
    fd =open(wp,'wb')
    csv.writer(fd).writerow(["status","sr#","duration","begin"])
    csv.writer(fd).writerows(hb_data)
    fd.close()

def giveUpTask(statusTime,hb_data,websitePath) :
    if statusTime['Created'][1] > 60 :
       writeHBCSVFile(hb_data,websitePath)
       sys.exit("Too long time in Created status CRAB job, so giving up the try")
    elif statusTime['Submitting'][1] > 600 :
       writeHBCSVFile(hb_data,websitePath)
       sys.exit("Too long time in Submitting status CRAB job, so giving up the try")
    elif statusTime['Submitted'][1] > 4500 :
       writeHBCSVFile(hb_data,websitePath)
       sys.exit("Too long time in Submitted status CRAB job, so giving up the try")
    elif statusTime['Waiting'][1] > 1800 :
       writeHBCSVFile(hb_data,websitePath)
       sys.exit("Too long time in Waiting status CRAB job, so giving up the try")
    elif statusTime['Ready'][1] > 600 :
       writeHBCSVFile(hb_data,websitePath)
       sys.exit("Too long time in Ready status CRAB job, so giving up the try")
    elif statusTime['Scheduled'][1] > 4500 :
       writeHBCSVFile(hb_data,websitePath)
       sys.exit("Too long time in Scheduled status CRAB job, so giving up the try")
    elif statusTime['Running'][1] > 4500 :
       writeHBCSVFile(hb_data,websitePath)
       sys.exit("Too long time in Running status CRAB job, so giving up the try")
 
 
def checkUntilDone(UIWorkingDir,websitePath) :    
    # timeStamps contains the time when a certain status showed up for the last time
    # timeStamps[0] = time before first crab -status
    # timeStamps[1] = time when Created shows up last
    # timeStamps[2] = time when Submitting shows up last
    # timeStamps[3] = time when Submitted shows up last
    # timeStamps[4] = time when Waiting shows up last
    # timeStamps[5] = time when Ready shows up last
    # timeStamps[6] = time when Scheduled shows up last
    # timeStamps[7] = time when Running shows up last
    # timeStamps[8] = time when Done shows up last
    
    timeStamps = [gmtime() for col in range (9)]
    jobDone = bool(False)
    
    status_time = {}
    fname=websitePath+"/hb.csv"
    print "fname : ",fname
    if not os.path.isfile(fname) :
       #test_data = np.zeros((0,4))       
       test_data = np.array( [ ('Created','1','-1','4') ] )
       writeHBCSVFile(test_data,websitePath)

    datahb = mlab.csv2rec(fname)
    hb_data = np.zeros((0,4))
 
    while jobDone == False :
        
        currentStatus = "None"
        
        print "Checking status of the job:"
    
        cmd = 'crab -status -c ' + UIWorkingDir + ' | grep -A 2 E_HOST'
        p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
        output = p.stdout.read()
        print output
        
        exitCode = p.poll()
        if exitCode != 0 :
            print "Error while checking the status of the CRAB job...\nExitCode = ", exitCode
    
        if checkStatus(output, 'Created') or checkStatus(output, 'created') or checkStatus(output, 'CREATED') :
            timeStamps[1] = gmtime()
            currentStatus = "Created"
            
        elif checkStatus(output, 'Submitting') or checkStatus(output, 'submitting') or checkStatus(output, 'SUBMITTING') :
            timeStamps[2] = gmtime()
            currentStatus = "Submitting"
            
        elif checkStatus(output, 'Submitted') or checkStatus(output, 'submitted') or checkStatus(output, 'SUBMITTED') :
            timeStamps[3] = gmtime()
            currentStatus = "Submitted"

        elif checkStatus(output, 'Waiting') or checkStatus(output, 'waiting') or checkStatus(output, 'WAITING') :
            timeStamps[4] = gmtime()
            currentStatus = "Waiting"
            
        elif checkStatus(output, 'Ready') or checkStatus(output, 'ready') or checkStatus(output, 'READY') :
            timeStamps[5] = gmtime()
            currentStatus = "Ready"

        elif checkStatus(output, 'Scheduled') or checkStatus(output, 'scheduled') or checkStatus(output, 'SCHEDULED') :
            timeStamps[6] = gmtime()
            currentStatus = "Scheduled"
            
        elif checkStatus(output, 'Running') or checkStatus(output, 'running') or checkStatus(output, 'RUNNING') :
            timeStamps[7] = gmtime()
            currentStatus = "Running"
            
        elif checkStatus(output, 'Done') or checkStatus(output, 'done') or checkStatus(output, 'DONE') :
            timeStamps[8] = gmtime()
            currentStatus = "Done"
            jobDone = bool(True)
        
        else :
            if checkStatus(output, 'Aborted') or checkStatus(output, 'aborted') or checkStatus(output, 'ABORTED') :
               currentStatus = "Aborted"
            elif checkStatus(output, 'Cleaned') or checkStatus(output, 'Cleaned') or checkStatus(output, 'CLEANED') :
               currentStatus = "Cleaned"
            txt = "Wrong status of the current HeartBeat job i-e; ",currentStatus
            hb_data=producePlots(datahb,txt,websitePath)
            writeHBCSVFile(hb_data,websitePath)
            sys.exit("Wrong status of the CRAB job")
           
        status_time = analyzeTimeStamps(timeStamps)
 
        print currentStatus , status_time
        writeDataCSVFile(status_time,websitePath)
        
        txt = "The status of the current HeartBeat job is ",currentStatus
        hb_data=producePlots(datahb,txt,websitePath)
        giveUpTask(status_time,hb_data,websitePath)
   
        if jobDone == False :
            print "Job still busy, sleeping for 30 seconds"
            #txt = "The status of the current HeartBeat job is:",currentStatus
            #txt2 = "This graph was last updated at ", time.localtime()
            #txt = txt1 + txt2 
            #hb_data=producePlots(datahb,txt)
            #giveUpTask(status_time,hb_data)  
            time.sleep(30)   
    print "Job is Done"
    writeHBCSVFile(hb_data,websitePath)

def producePlots(datahb,txt,websitePath) :
    print "Producing Plots"
    fig = plt.figure()
    ax = fig.add_subplot(111)
    fdname=websitePath+"/data.csv"
    datasets = mlab.csv2rec(fdname)
    begin = datasets[0][3]
    to_del=mlab.find(datahb.begin ==begin)
    y=np.delete(datahb,to_del)
    current = time.time()
    limit = current - 24 * 3600;
    lim_del=mlab.find(y.begin<limit) 
    hb=np.delete(y,lim_del)
    alen=datasets.shape[0]
    blen=hb.shape[0]
    datasets.resize(alen+blen)
    datasets[alen:]=hb[:]

    sorted_tup = sorted(datasets, key=itemgetter(3,1))
    print sorted_tup
    my_labels = ['Created', 'Submitting', 'Submitted','Waiting','Ready', 'Scheduled', 'Running','Done']
    colors = ['#000000', "#B3C95A", 'b','c', '#63B8FF', 'g', "#FF3300","#C0C0C0"]
    index = 0
    legendcnt = 0
    y_dur=0
    ysum=0
    ylimit=0
    timechk=0
    flag = bool(False)
    for data in sorted_tup :
      time_diff  = current - data.begin
      diff  = time_diff/(60*60)
      x = 24.0 - diff
      timetup = time.gmtime(data.begin)
      if timetup != timechk :
         timechk=timetup
         ysum=0 
     
      y_dur=data.duration
      if y_dur == -1:
         if flag == False:
           ax.plot(x, data.duration, 'o', c=colors[index], label=my_labels[index])
         else :
           ax.plot(x,data.duration,'o',c=colors[index])
      else :
         ysum=ysum+data.duration
         if ysum > ylimit :
           ylimit = ysum 
         if flag == False:
           ax.plot(x, ysum, 'o', c=colors[index], label=my_labels[index])
         else:
           ax.plot(x, ysum, 'o', c=colors[index])


      index += 1
      if index == 8:
         index=0
         flag = bool(True)

     
    ylimit=ylimit+100
    # Set the title.
    ax.set_title("CrabHeartbeat during last 24 hours",fontsize=14)

    # Set the X Axis label.
    ax.set_xlabel("Last 24 Hours",fontsize=10)

    # Set the Y Axis label.
    ax.set_ylabel("Time(seconds)",fontsize=10)
    plt.setp(ax.get_xticklabels(), rotation='vertical', fontsize=10)
    plt.setp(ax.get_yticklabels(),  fontsize=10)
    ax.set_xlim([0,24])
    ax.set_ylim([-2,ylimit])
    plt.grid(True,which="both",ls="-", color='0.65')
    ax.set_xticks(np.arange(0,24,1))   
    ax.set_yticks(np.arange(0,ylimit,100))
 
    if legendcnt == 0 :
       box = ax.get_position()
       ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
       ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
       legendcnt +=1
    #box1 = ax.get_position()
    #ax.set_position([box1.x0, box1.y0, box1.width , box.height * 0.8])

    fig.text(0.22,0.02,txt,fontsize=10)
    figname=websitePath+"/plot.png" 
    fig.savefig(figname,dpi=300)
    fig.clf()
    plt.close()
    return sorted_tup
 

def analyzeOutput(UIWorkingDir) :
    
    cmd = 'crab -getoutput -c ' + UIWorkingDir
    p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    output = p.stdout.read()
    print output
    
    exitCode = p.poll()
    if exitCode != 0 :
        print "Error while getting output of the CRAB job...\nExitCode =", exitCode
    
    #print "Writing statusTime to a ROOT file"

    #outputProducer.writeRootFile(statusTime)

    #print "Writing output to ROOT file done"


def endJob(outCRABcfg, UIWorkingDir) :

    print "Renewing Credential"
    
    cmd = 'crab -renewCredential -c ' + UIWorkingDir
    p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    exitCode = p.poll()
    output = p.stdout.read()
    
    if(exitCode == 0)    :
        print "Credential succesfully renewed"
    else :
        print "Problem while renewing credential:  ExitCode =", exitCode
        print "Additional output of crab -renewCredential :"
        print output
    
    cmd = 'mv ' + outCRABcfg + ' ' + UIWorkingDir
    p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    output = p.stdout.read()

    exitCode = p.poll()
    
    if exitCode == 0 :
        print "CRAB cfg file moved to UIWorkingDir"
    else :
        print "Problem while moving CRAB cfg file to UIWorkingDir, exitCode = ", exitCode
        print output

    cmd = 'mv ' + UIWorkingDir + ' CRABdirs'
    p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    output = p.stdout.read()
    exitCode = p.poll()

    if exitCode == 0 :
        print "UIWorkingDir moved to CRABdirs"
    else :
        print "Problem while moving UIWorkingDir to CRABdirs, exitCode = ", exitCode
        print output


# start of the script!
print "This script will perform a HeartBeat job"

params = parseParams()
serverName = params[0]
webDir = params[1]
websitePath = webDir+serverName

dateTime = strftime("%m%d%Y_%H%M%S", gmtime()) # everything in UTC time

outCRABcfg = "crabHeartBeat_" + dateTime + "_" + serverName + ".cfg"
print outCRABcfg
UIWorkingDir = "CRABserverHeartBeat_" + dateTime + "_" + serverName
UserScript = "doNothing.sh"
jobOutputFile = "output.txt"
makeUserScript(UserScript, jobOutputFile)

makeCRABcfg(outCRABcfg, serverName, jobOutputFile, UIWorkingDir, UserScript)

submitCRABJob(outCRABcfg)

statusTime = checkUntilDone(UIWorkingDir,websitePath)
#statusTime = checkUntilDone(UIWorkingDir, outputProducer)

analyzeOutput(UIWorkingDir)

endJob(outCRABcfg, UIWorkingDir)

print "doHeartBeat.py finished"
