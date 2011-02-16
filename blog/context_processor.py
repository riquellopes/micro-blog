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

@app.context_processor
def admin_logout_url():
	return dict(admin_logout_url=users.create_logout_url)

@app.context_processor
def admin_login_url():
	return dict(admin_login_url=users.create_login_url)

@app.context_processor
def rss_url():
	return dict(rss_url="http://twitter.com/statuses/user_timeline/riquellopes.atom")
