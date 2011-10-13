#!/bin/bash

CFGFILE=$1; shift
[ -n "$CFGFILE" ] || { echo "$0: usage $0 <cfgfile> [<minutes>]"; exit 1; }
[ -f "$CFGFILE" ] || { echo "$0: could not find config file $CFGFILE"; exit 2; }
source $CFGFILE
source $BUILDFUNCS

MIN=$(($1)); [ $MIN -lt 1 ] && MIN=20160 # defaults to 2 weeks
AGE=$(($(date +%s)-$MIN*60));

LOG_FILES="$LOGDIR/*-*-*_*-*-*"
for FILE in $LOG_FILES; do
    LAST_CHANGE=$(stat $statfmt $FILE 2> /dev/null || date +%s)
    [ $LAST_CHANGE -lt $AGE ] && rm "$FILE"  &> /dev/null
done

exit 0
