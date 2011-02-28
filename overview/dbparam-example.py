import cx_Oracle as oradb

dbparam += [
  { 'name': "Production",
    'label': "prod",
    'class': "all-prod",
    'connect':
      lambda: oradb.connect(user="cms_transfermgmt_reader",
			    password="secret_password_here",
			    dsn="cms_transfermgmt")
  },
  { 'name': "Debug",
    'label': "debug",
    'class': "all-prod",
    'connect':
      lambda: oradb.connect(user="cms_transfermgmt_sc_reader",
			    password="secret_password_here",
			    dsn="cms_transfermgmt_sc")
  },
  { 'name': "Dev",
    'label': "dev",
    'class': "all-dev",
    'connect':
      lambda: oradb.connect(user="cms_transfermgmt_test_reader",
			    password="secret_password_here",
			    dsn="cms_transfermgmt_test")
  },
  { 'name': "Testbed",
    'label': "testbed",
    'class': "all-dev",
    'connect':
      lambda: oradb.connect(user="cms_transfermgmt_testbed",
			    password="secret_password_here",
			    dsn="int2r_lb")
  },
  { 'name': "Testbed2",
    'label': "testbed2",
    'class': "all-dev",
    'connect':
      lambda: oradb.connect(user="cms_transfermgmt_testbed2",
			    password="secret_password_here",
			    dsn="int2r_lb")
  }
 ]
