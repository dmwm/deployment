#!/bin/bash

##H Usage: build.sh [-u] [-p DIFFURL] [-l LOGFILE] AREANAME GHOWNER GHBRANCH GHREF ARCH
##H
##H Possible options:
##H  -u             Upload packages if build succeeds.
##H  -p DIFFURL     Apply patch from the provided DIFFURL.
##H  -l LOGFILE     Set log file.
##H  -h             Display this help.

upload=false
logfile="Log.txt"
while [ $# -ge 1 ]; do
  case $1 in
    -u ) upload=true; shift ;;
    -p ) diffurl="$2"; shift; shift ;;
    -l ) logfile="$2"; shift; shift ;;
    -h ) perl -ne '/^##H/ && do { s/^##H ?//; print }' < $0 1>&2; exit 1 ;;
    -* ) echo "$0: unrecognised option $1, use -h for help" 1>&2; exit 1 ;;
    *  ) break ;;
  esac
done

if [ $# -ne 5 ]; then
  perl -ne '/^##H/ && do { s/^##H ?//; print }' < $0 1>&2
  exit 1
fi

set -e
areaname=$1 owner=$2 branch=$3 ref=$4 arch=$5
TOP=$(cd $(dirname $0)/../../.. && pwd)
ME=$(basename $(dirname $0))
PKGTOOLS=$TOP/current/apps/pkgtools
BLD=$TOP/state/$ME/builds/$areaname
OUT=$TOP/state/$ME/webarea/$areaname
AUTHDIR=$TOP/current/auth/dmwmbld

# create destination directory if not exists
mkdir -p $OUT
[ ! -d $BLD ] || rm -rf $BLD
mkdir -p $BLD

cd $BLD
git clone -b $branch https://github.com/$owner/cmsdist.git
cd cmsdist
git reset --hard $ref

if [ -z "$diffurl" ]; then :; else
  echo "Applying diff from URL: $diffurl"
  curl -ksL -X GET $diffurl | git apply
fi
cd ..

echo $ref > $BLD/lastcommit
env > $OUT/$logfile

echo
echo "Building RPMs..."
case $arch in slc6_amd64_gcc493) repo=comp;; *) repo=comp.pre ;; esac
cmd="$PKGTOOLS/cmsBuild -c cmsdist --repository $repo -a $arch --builders 8 -j 4 --work-dir w build comp"
# Try to build it two times in the same area to workaround some build problems
$cmd >> $OUT/$logfile || $cmd >> $OUT/$logfile

if $upload; then
  echo "Uploading RPMs..."
  $PKGTOOLS/cmsBuild -c cmsdist --repository $repo  -a $arch --builders 8 -j 4 --work-dir w upload comp --sync-back >> $OUT/$logfile
else :; fi

echo "Done"
