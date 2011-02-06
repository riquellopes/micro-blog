# -*- encoding: utf-8 -*-
"""
	Blog rLopes Hooks
	-----------------
"""
from flask import render_template
from blog import app

@app.errorhandler(404)
def page_not_found(error):
	"""Método responsável em tratar erros. 404"""
	return render_template('404.html', error=error), 404

@app.errorhandler(500)
def internal_server_error(error):
	"""Método responsável em tratar erros. 500"""
	return render_template("500.html", error=error), 500
