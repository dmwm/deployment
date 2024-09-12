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
      # Find and archive all logs
      find $applogs -type f -name '*.log_*_[0-9]*' -print |
      while read f; do
        # Extract the date from the log filename
        log_date=$(echo "$f" | sed -E 's/.*_([0-9]{8})$/\1/')

        # Skip today's logs
        if [ "$log_date" = "$(date +%Y%m%d)" ]; then
          continue
        fi

        # Name the zip file according to the log file's date
        archive_name="aps-xps_logs_${log_date}.zip"

        # Archive the file and delete it after archiving
        ionice -c3 zip -9Tmjq "${applogs}/${archive_name}" "$f" ||
          { echo "$f: failed to archive logs: $?" 1>&2; exit 4; }
      done

      # Remove zip archives older than 14 days
      find $applogs -name 'aps-xps_logs_*.zip' -mtime +14 -exec rm -f {} \;

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
