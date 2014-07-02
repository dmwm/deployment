#!/bin/bash

##H Usage: build.sh [-u] [-p DIFFURL] AREANAME GHOWNER GHBRANCH GHREF ARCH
##H
##H Possible options:
##H  -u             Upload packages if build succeeds.
##H  -p DIFFURL     Apply patch from the provided DIFFURL.
##H  -h             Display this help.

upload=false
while [ $# -ge 1 ]; do
  case $1 in
    -u ) upload=true; shift ;;
    -p ) diffurl="$2"; shift; shift ;;
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
  curl -ks -X GET $diffurl | git apply
fi
cd ..

echo $ref > $BLD/lastcommit
env > $OUT/Log.txt

echo
echo "Building RPMs..."
# Try to build it two times in the same area to workaround some build problems
cmd="$PKGTOOLS/cmsBuild -c cmsdist --repository comp.pre -a $arch --builders 8 -j 4 --work-dir w build comp"
$cmd >> $OUT/Log.txt || $cmd >> $OUT/Log.txt

if $upload; then
  echo "Uploading RPMs..."
  $PKGTOOLS/cmsBuild -c cmsdist --repository comp.pre -a $arch --builders 8 -j 4 --work-dir w upload comp --sync-back >> $OUT/Log.txt
else :; fi

echo "Done"
