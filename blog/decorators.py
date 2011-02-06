# -*- encoding:utf-8 -*-
"""
	Blog rLopes Decorators
	----------------------
"""
from functools import wraps
from google.appengine.api import users
from flask import redirect, request

def login_required(func):
	@wraps(func)
	def decorated_view(*args, **kwargs):
		if users.is_current_user_admin() == False:
			return redirect(users.create_login_url(request.url))
		return func(*args, **kwargs)
	return decorated_view
