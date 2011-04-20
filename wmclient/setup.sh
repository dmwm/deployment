top=$(cd $(dirname $0)/../.. && pwd)
root=$(cd $(dirname $0)/.. && pwd)

. $top/current/apps/wmcore/etc/profile.d/init.sh
. $top/current/apps/py2-httplib2/etc/profile.d/init.sh

export WMCORE_ROOT
export PATH=$PATH:$WMCORE_ROOT/bin
export PYTHONPATH=$PYTHONPATH:$WMCORE_ROOT/src/python
export PYTHONPATH=$PYTHONPATH:$WMCORE_ROOT/test/python
