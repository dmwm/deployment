#!/bin/bash
if [[ ( $@ == "--help") ||  $@ == "-h" || $# -ne 1 ]]
then
	echo "Usage: This helper script is used for renewing th proxy in testbed and prodction VMs. Please use the ./renewVMProxy.sh <username>"
	exit 0
fi
admin_username=$1
BHOSTS="vocms0731 vocms0132 vocms0136 vocms0738 vocms0739 vocms0841 vocms0842 vocms0843 vocms0844"
for host in $BHOSTS
do
  echo "Operating on node $host.."
  ssh $host -l cmsweb /bin/sh -s "$admin_username" << "EOF"
    cd /data/srv/current/auth/proxy
    admin_username=$1
    if [ -f "seed-$admin_username.cert" ]; then
      mv seed-$admin_username.cert proxy-$admin_username.cert
    fi
    /data/srv/current/config/admin/ProxyRenew /data/certs /data/srv/current/auth/proxy cmsweb_backends cms
    echo "Done. Verifying if the proxy is valid.."
    openssl x509 -enddate -noout -in /data/srv/current/auth/proxy/proxy.cert
    exit
EOF
done
