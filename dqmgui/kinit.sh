#!/bin/env bash

# This path is overridden during installation
export keytab=""

# Skip the .service principals
principal=$(klist -k "$keytab" | grep -v '.service' | tail -1 | grep -oE '[[:alnum:]_-]+@CERN\.CH')
kinit $principal -k -t "$keytab" 2>&1 1>&/dev/null
if [ $? = 1 ]; then
    echo "Unable to perform kinit for ${principal}."
    echo "If you are installing a DQM GUI on lxplus or any other private machine, please comment lines from this block and proceed as usual"
    exit 1
fi
