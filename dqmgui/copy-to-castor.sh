#!/bin/sh

set -e # exit on errors
ME=$(basename $(dirname $0))
STATEDIR=$(cd $(dirname $0)/../../../state/$ME && pwd)
dst=$(cat $STATEDIR/backup/copy-to-castor.next)

echo "Copying next tar file volume to $dst ..."
rfcp $STATEDIR/backup/partial.tar $dst
rm $STATEDIR/backup/partial.tar # clean up the temporary tape file on disk

# Increment the volume number for the next tape file
echo "${dst%.*}.$((${dst##*.}+1))" > $STATEDIR/backup/copy-to-castor.next
