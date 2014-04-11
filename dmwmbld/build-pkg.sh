#!/bin/bash

ME=$(basename $(dirname $0))
TOP=$(cd $(dirname $0)/../../.. && pwd)
TMP=$TOP/state/$ME/builds/$2
LOG=$TOP/state/$ME/webarea/$2
PKGTOOLS=$TOP/current/apps/pkgtools

# create destination directory if not exists
mkdir -p $LOG
if [ -d $TMP ]; then rm -rf $TMP; fi
mkdir -p $TMP
cd $TMP

git clone https://github.com/geneguvo/cmsdist.git
cd cmsdist
git checkout $3
stg init
stg new -m 'foo' abc --author "A. <foo@fakemail.com>" --authdate ""
echo "Diff URL: $1"
curl -ks -X GET $1 | git apply --whitespace=fix
git add -A
stg refresh
cd ..

echo
echo "Building RPMs..."
# export logs for reports
$PKGTOOLS/cmsBuild -c cmsdist --repository comp.pre -a $4 --builders 8 -j 4 --work-dir w build comp > $LOG/Log.txt
echo $? > $LOG/ReturnCode.txt
echo "Done"
