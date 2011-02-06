# -*- encoding:utf-8 -*-
"""
	Blog rlopes ContextProcessor
	----------------------------
"""
from google.appengine.api import users
from blog import app

@app.context_processor
def admin_logged():
	return dict(admin_loggend=users.is_current_user_admin())
