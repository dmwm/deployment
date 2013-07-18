#!/bin/bash

# check number of input arguments
usage="Usage: `basename $0` <URL|file_name> <validator_script>"
helpmsg="  This script fetch, validate and upload DAS maps into MongoDB"
E_BADARGS=65
if [ $# -eq 1 ]; then
    if  [ "$1" == "-h" ] || [ "$1" == "-help" ] || [ "$1" == "--help" ]; then
        echo $usage
        echo $helpmsg
    else
        echo $usage
    fi
    exit
elif [ $# -eq 2 ]; then
    DAS_MAP_URI=$1
    DAS_VALIDATOR_SCRIPT=$2
else
    echo $usage
    exit $E_BADARGS
fi

# settings
domain=`hostname -f | awk '{z=split($1,a,"."); print ""a[z-1]"."a[z]""}'`
if [ "$domain" == "cern.ch" ]; then
    # settings for CERN domain (VMs and production nodes)
    WDIR=/data/state/mongodb/das
    STAGEDIR=/data/state/mongodb/das
else
    # local testing outside of CERN domain
    WDIR=/tmp/das
    STAGEDIR=/tmp/das
fi
mkdir -p $WDIR
mkdir -p $STAGEDIR

# Fetch DAS map JSON file from given URL
regex='(https|http)://[-A-Za-z0-9\+&@#/%?=~_|!:,.;]*[-A-Za-z0-9\+&@#/%=~_|]'
if  [ -f $DAS_MAP_URI ]; then
    dasmaps=$DAS_MAP_URI
elif [[ $DAS_MAP_URI =~ $regex ]]; then
    curl -s $DAS_MAP_URI > $WDIR/das_cms_maps.js
    dasmaps=$WDIR/das_cms_maps.js
else
    echo "Invalid DAS map input, please provide either URL or full file name"
fi

# Calculate MD5 checksum, compare it to existing one
stamp=$(cat $dasmaps | md5sum)

# Validate DAS map JSON file
$DAS_VALIDATOR_SCRIPT $dasmaps
validator_status=$?
if  [ "$validator_status" -ne "0" ]; then
    echo "Fail DAS map validation"
    exit 1
fi

# Clean-up DAS databases and prepare for deployment
cat > $WDIR/cleaner.js << EOF
parser = db.getSisterDB("parser");
parser.db.drop();
das = db.getSisterDB("das");
das.dropDatabase();
mapping = db.getSisterDB("mapping");
mapping.dropDatabase();
EOF

# Deploy DAS map JSON file into MongoDB
oldstamp=$(cat $STAGEDIR/mapping_db-schema-stamp 2>/dev/null)
if [ ! -f $STAGEDIR/mapping_db-schema-stamp ] || [ X"$oldstamp" != X"$stamp" ]; then
    set -e
    mongo --port 8230 $WDIR/cleaner.js
#    echo "Update DAS mapping DB"
    mongoimport --port 8230 --db mapping --collection db --file $dasmaps
    echo "$stamp" > $STAGEDIR/mapping_db-schema-stamp
    set +e
fi
