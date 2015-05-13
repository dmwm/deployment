#!/bin/bash
rdir={ROOT}/current/apps/DCAFPilot
source $rdir/etc/profile.d/init.sh
export DCAFPILOT_ROOT
export X509_USER_CERT={ROOT}/current/auth/proxy/proxy.cert
export X509_USER_KEY={ROOT}/current/auth/proxy/proxy.cert
export DCAFPILOT_PREDICTIONS={ROOT}/state/dcafpilot/analytics/predictions
export DCAFPILOT_CONFIG=$rdir/etc/dcaf.cfg
