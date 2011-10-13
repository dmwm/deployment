#!/bin/bash

CFGFILE=$1; shift
[ -n "$CFGFILE" ] || { echo "$0: usage $0 <cfgfile> [<minutes>]"; exit 1; }
[ -f "$CFGFILE" ] || { echo "$0: could not find config file $CFGFILE"; exit 2; }
source $CFGFILE

MIN=$(($1)); [ $MIN -lt 1 ] && MIN=129600 # defaults to 3 months
AGE=$(($(date +%s)-$MIN*60));
LASTCLEAN=$(cat $WEB/last_tag_clean 2> /dev/null || echo 0)

for F in $WEB/*history; do
    [ -f $F ] || break;
    for TAG in $(sed -n '$!p' $F | egrep -h -o "bld_.*\>"); do
        TAGAGE=$(echo $TAG | cut -d"_" -f2)
        if [ $TAGAGE -lt $AGE -a $TAGAGE -ge $LASTCLEAN ]; then
            cvs -Q rtag -d $TAG CMSDIST &> /dev/null || exit 1
        fi
    done
done

echo $AGE > $WEB/last_tag_clean
