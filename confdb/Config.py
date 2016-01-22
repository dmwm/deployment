# -*- coding: utf-8 -*-

import os
import tempfile

# configuration for ConfDB authentication
from ConfDBAuth import *

# confguration for CherryPy
cpconfig = {
  'server.socket_host': '0.0.0.0',
  'server.socket_port': 8340,
  'server.thread_pool': 30
}

# base URL of the application on the server (e.g. use "/confdb" for "http://cmsweb.cern.ch/confdb"
base_url = "/confdb"

# local directory with read-write access for temporary files
state_dir = tempfile.gettempdir()
if 'STATEDIR' in os.environ:
    state_dir = os.environ.get('STATEDIR')
