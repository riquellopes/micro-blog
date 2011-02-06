# -*- encoding: utf-8 -*-
"""
	Blog rLopes Main
	----------------
"""

import os
import sys

# add lib in PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))

from google.appengine.ext.webapp.util import run_wsgi_app
from blog import app


run_wsgi_app(app)
