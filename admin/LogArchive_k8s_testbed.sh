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
      # Extract the date from the first log file found (for naming the archive)
      log_file=$(find $applogs -name '*.log_*_[0-9]*' -print | head -n 1)

      if [ -n "$log_file" ]; then
        # Extract the date (YYYYMMDD) from the filename
        archive_date=$(echo "$log_file" | sed -E 's/.*_([0-9]{8})$/\1/')
      else
        # Default to today's date if no log file is found
        archive_date=$(date +%Y%m%d)
      fi

      # Name the zip file
      archive_name="aps-xps_logs_${archive_date}.zip"

      # Compress all log files matching the pattern and older than 1 day
      find $applogs -name '*.log_*_[0-9]*' -mtime +1 -print |
        while read f; do
          case $f in *.zip ) continue ;; esac
          ionice -c3 zip -9Trmuoqj "${applogs}/${archive_name}" "$f" ||
            { echo "$f: failed to archive logs: $?" 1>&2; exit 3; }
        done

      # Archive new logs without removing them
      find $applogs -name '*.log_*_[0-9]*' -print |
        while read f; do
          case $f in *.zip ) continue ;; esac
          ionice -c3 zip -9Truoqj "${applogs}/${archive_name}" "$f" ||
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
