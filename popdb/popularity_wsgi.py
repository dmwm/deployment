import os
import sys
print sys.version_info

import django.core.handlers.wsgi

paths = ['@CONFIG@/','@POPDB_ROOT@/popdb/lib']
for path in paths:
    if path not in sys.path:
        sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

application = django.core.handlers.wsgi.WSGIHandler()
