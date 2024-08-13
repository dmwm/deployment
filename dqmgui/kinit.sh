#!/bin/env bash

# This path is overridden during installation
export keytab=""

# Skip the .service principals
principal=$(klist -k "$keytab" | grep -v '.service' | tail -1 | grep -oE '[[:alnum:]_-]+@CERN\.CH')
kdestroy -A >/dev/null 2>&1

# Try up to # tries times to run kinit.
tries=${1:-2}
while [ $tries -gt 0 ]; do
    if ! kinit $principal -k -t "$keytab" 2>&1 1>&/dev/null; then
        tries=$((tries - 1))
        sleep 4
    else
        break
    fi
done

if [ $tries -eq 0 ]; then
    echo "Unable to perform kinit for ${principal}."
    echo "If you are installing a DQM GUI on lxplus or any other private machine, please comment lines from this block and proceed as usual"
    exit 1
fi
