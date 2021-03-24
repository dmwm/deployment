#!/bin/sh
export keytab=/data/srv/current/auth/wmcore-auth/keytab
principal=`klist -k "$keytab" | tail -1 | awk '{print $2}'`
kinit $principal -k -t "$keytab" 2>&1 1>& /dev/null
if [ $? == 1 ]; then
    echo "Unable to perform kinit."
    exit 1
fi
