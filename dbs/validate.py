#!/usr/bin/env python
import sys, json, re
if len(sys.argv) < 2:
  print >> sys.stderr, "Must have one of the input arguments: def, reader, writer or migration "
  sys.exit(1)
try:
  d=json.load(sys.stdin)
except:
  print >> sys.stderr, "Data is not a valid json."
  raise

if set(d.keys()) != set(["default", "dev", "preprod", "prod"]):
  print >> sys.stderr, "Must have configuration for default, dev, preprod and prod, nothing else."
  sys.exit(1)
for v in d.values():
  if not isinstance(v,dict):
    print >> sys.stderr, "'%s' is not a viewname -> list of instances map." % v
    sys.exit(1)
  if sys.argv[1] == "reader":
    if set(v.keys()) != set(["DBSReader"]):
      print >> sys.stderr, "Must have view names for 'DBSReader', nothing else."
      sys.exit(1)
  elif sys.argv[1] == "writer":
    if set(v.keys()) != set(["DBSWriter"]):
      print >> sys.stderr, "Must have view names for 'DBSWriter' , nothing else."
      sys.exit(1)
  elif sys.argv[1] == "reader&writer":
    if set(v.keys()) != set(["DBSReader", "DBSWriter"]):
      print >> sys.stderr, "Must have view names for 'DBSReader'and 'DBSWriter', nothing else."
      sys.exit(1)
  else:
    if set(v.keys()) != set(["DBSReader", "DBSWriter", "DBSMigrate"]):
      print >> sys.stderr, "Must have view names for 'DBSReader', 'DBSWriter' and 'DBSMigrate', nothing else."
      sys.exit(1)
  for t in v.values():
    if not isinstance(t,list):
      print >> sys.stderr, "'%s' is not a list of instance names." % t
      sys.exit(1)
    for i in t:
      if not re.match('^(prod|int|dev)/(global|phys0[123]|test)$', i):
        print >> sys.stderr, "'%s' is an invalid instance name." % i
        sys.exit(1)
sys.exit(0)
