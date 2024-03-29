#!/bin/sh

# Automatically archive old logs from all application servers to zip files.
# Scans the application log directories and picks any old files, and packs
# them with maximum compression into a zip archive.
#
# Some projects have a multiple instances and hence subdirectory under their
# log area; pack each instance separately.
#
# The front-end logs are handled specially. The archives are monthly, based
# on the log file name. Old logs are moved to the archive, recent logs are
# updated in the zip file but a copy of the file is kept on disk. An acron
# job then syncs the archived logs to AFS area shortly after this runs.
THRESHOLD=90

#sudo su
echo "start"
# give this /cephfs as parameter to run this script as cron job

BASEDIR=${1-$(cd $(dirname $0)/../../.. && pwd)}

echo $BASEDIR

[ -d $BASEDIR ] || { echo "$BASEDIR: no such directory" 1>&2; exit 1; }

for applogs in $(find $BASEDIR -depth -type d); do
  [ -d $applogs ] || continue
  [ -f $applogs/.noarchive ] && continue
  usage=$(df -P $applogs | tail -1 | awk '{print $5}')
  if [ ${usage%?} -ge $THRESHOLD ]; then
    echo "Warning: available disk space on $applogs is low ($usage used)."
  fi
echo $applogs

case $applogs in
    */frontend-logs )
      # Compress old logs.
      find $applogs -name '*_log_*' -mtime +1 -print |
        while read f; do
          case $f in *.zip ) continue ;; esac
          temp1=$(echo $f | sed 's/_[0-9]*\(.txt\)*$//')
          kind=$(n=1; echo $temp1 | awk -v m="$n" '{print substr($0,m,40);}')
          temp2=$(echo $f | sed 's/.*_log_//; s/..\(\.txt\)*$//')
	  month=$(n=27; echo $temp2 | awk -v m="$n" '{print substr($0,m,6);}')
          ionice -c3 zip -9Trmuoqj ${kind}_${month}.zip $f ||
            { echo "$f: failed to archive logs: $?" 1>&2; exit 3; }
        done

      # Add remaining (new) logs but don't remove them.
      find $applogs -name '*_log_*' -print |
        while read f; do
          case $f in *.zip ) continue ;; esac
          temp1=$(echo $f | sed 's/_[0-9]*\(.txt\)*$//')
          kind=$(n=1; echo $temp1 | awk -v m="$n" '{print substr($0,m,40);}')
          temp2=$(echo $f | sed 's/.*_log_//; s/..\(\.txt\)*$//')
	  month=$(n=27; echo $temp2 | awk -v m="$n" '{print substr($0,m,6);}')
  	  ionice -c3 zip -9Truoqj ${kind}_${month}.zip $f ||
            { echo "$f: failed to archive logs: $?" 1>&2; exit 4; }
        done
      ;;

    * )
      # Standard server directory, archive to bundles of about 500 MB.
      # Pick a ZIP archive. Find the last zip archive that is <500 MB.
      # If there is none, start a new archive, with today's time stamp.
      zip=$(find $applogs -maxdepth 1 -name '*.zip' -size -500M | sort | tail -1)
      [ X"$zip" = X ] && zip=$applogs/old-logs-$(date +%Y%m%d-%H%M).zip

      # Archive away logs that haven't been touched in two days.
      set -e
      FILES=$(find $applogs -maxdepth 1 -type f \
                \( -name '*log*' -o -name '*.txt' -o \
	           -name '*.stdout' -o -name '*.stderr' \) \
	        \! -name '*.zip' \
	        -mtime +1 | sort)
      [ X"$FILES" = X ] || ionice -c3 zip -9Tmojq $zip $FILES
      set +e
      ;;
  esac
done
