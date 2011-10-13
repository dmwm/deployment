#!/bin/bash
#
# This script needs to run with a valid Kerberos Token (i.e acron job)
#
# Why auto-killing ?
# - It uses cmsBuild and other tools that may hang in many different ways.
# - If the process is stuck for a long time, it is very improbable it will
# do progress after somehow being unlocked:
#   o The AFS token will be expired. No status info would be updated;
#   o The build may never complete because of bugs in spec files;
#   o The upload may hang when it is not able to SSH to the repository;
# - If the script don't kills itself, someone will need to do it. We
# lack manpower for that. Additionally, it will be hard for the operator
# to judge what it is better to be done. The script itself knows the
# critical stuff and kills itself only when the risk is low.
# - There is a very small change of corrupting stuff when killing
# appropriately. There are twiki instructions on how to recover, and
# nobody would care about possible lost data.
#
# In case you want to manage its execution, send one of these signals:
# - SIGTERM
# - SIGINT
# Don't send SIGKILL unless you know what you are doing.
#
# This script was designed to run concurrently. It protects resources with
# locks and avoid inconsistent states. You can call it many times
# without worring about stopping running instances (so, cronjobs can overlap).
# Doing so will actually speed up the building process because more than one
# project will be being built at the same time.
#
# For uploading packages to the repository, you need to setup
# a ssh key to be able to log into cmsbuild@cmsrep.cern.ch.
# - generate a dsa key pair with ssh-keygen
# - request Andreas Pfifer to add the pub key into cmsbuild@cmsrep
# authorized keys
# - leave the private key without password, in the 'private' dir
# of the AFS area. The pub key goes to the 'public' AFS dir
# - in case of using a non-standard key name, set links in ~/.ssh
# and put the following (for example) into ~/.ssh/config:
# Host cmsrep.cern.ch
#        IdentityFile ~/.ssh/id_dsa_autobuild
#
# These instructions and full documentation will be provided in twiki
# pages when time permits me to write then. The current resource available
# for that is https://twiki.cern.ch/twiki/bin/view/CMS/DMWMBuildsTutorial

#
# Global configuration
#
CFGFILE=$1; shift
[ -n "$CFGFILE" ] || { echo "$0: usage $0 <cfgfile>"; exit 1; }
[ -f "$CFGFILE" ] || { echo "$0: could not find config file $CFGFILE"; exit 2; }
source $CFGFILE
#
# End of config
#

# Build functions to use
source $BUILDFUNCS

job_watchdog() {
    local TIMEOUT=$1;
    trap "" EXIT RETURN
    trap 'echo "WATCHDOG: counted $c seconds. Still running..."' SIGINT SIGTERM
    for (( c=1; c<=$TIMEOUT; c++ )); do
	sleep 1
    done
    echo "WATCHDOG: timeout reached. Sending group SIGTERM..."
    kill -SIGTERM 0 # last chance to terminate
    sleep 5
    echo "WATCHDOG: will SIGKILL everybody!"
    kill -SIGKILL 0 # kills everybody (including itself)
}

main_exit_trap() {
    echo "MAIN: waiting for $MAIN_JOBS"
    wait $MAIN_JOBS &> /dev/null
    kill -SIGKILL $WATCHDOG &> /dev/null
    wait $WATCHDOG &> /dev/null
    echo "MAIN: Main builder-agent exiting..."
}

main_term_trap() {
    echo "MAIN: SIGTERM to $MAIN_JOBS"
    kill -SIGTERM 0 &> /dev/null
    echo "MAIN: waiting for $MAIN_JOBS"
    wait $MAIN_JOBS &> /dev/null
    kill -SIGKILL $WATCHDOG &> /dev/null
    wait $WATCHDOG &> /dev/null
    echo "MAIN: Main builder-agent terminating..."
    exit 1 # May not be executed if it was already there when interrupted
}

#
# Main
#
exec &> $LOG_FILE  # Redirects stdout and stderr to log file

MAIN_JOBS=""
WATCHDOG=""
# Be aware that "Trapped signals that are not being ignored are reset to their
# original values in a child process when it is created."
# So the following traps will not be inherited by created jobs
trap 'main_term_trap' SIGINT SIGTERM # Send the signal to everybody
trap 'main_exit_trap' EXIT # Do never exit if there is stuff running

# The watchdog must be the first job to be started
job_watchdog $TIMEOUT & # the watchdog will group SIGKILL if timeout reached
WATCHDOG=$!

# Build and upload pre-releases
job_process_file comp.pre &
MAIN_JOBS=$!
wait %

# Build and upload releases
job_process_file comp &
MAIN_JOBS+=" $!"
wait %

exit 0 # will also trigger the EXIT trap

#
# End of script
#
