# -*- encoding:utf-8 -*-

"""
	Blog rlopes Views
	----------------- 

	rLopes - Blog Engine. A blog engine written with Flask and Gae.
	
"""
from blog import app
from flask import render_template, request, flash, url_for, redirect,\
 session, abort

from model import Post
from forms import PostForm
from decorators import login_required
from context_processor import admin_logged
from hooks import page_not_found, internal_server_error
from send import Contact

@app.route('/')
@app.route('/<name>')
def get(name=None):
	if name == None:
		posts = Post.all()
		posts.order('-date_create')
		return render_template('index.html', posts=posts)
	else:
		try:
			post = Post.all().filter('url', name).get()
			return render_template('read_post.html', post=post)
		except:
			abort(404)
			
@app.route('/tag/<name>')
def tag(name):
	"""Método responsável em buscar post com a hash tag informada."""
	posts = Post.all()
	posts.filter('tags', name)
	posts.order('-date_create')
	return render_template('index.html', posts=posts)

	
@app.route('/contact', methods=['POST'])
def contact():
	"""Metodo responsável em solicitar envio de email."""
	contact = Contact()

	if contact.validate_on_submit():
		contact.send()
		return 'true'					   
	return contact.get_validation_engine()
	
@app.route('/form')
@app.route('/<int:id>/form')
@login_required
def form_post(id=None):
	"""Método responsável em criar form para o blog."""
	if id :
		form = PostForm( Post.get_by_id(id) )
		title = 'Update - %s' % form.title.data
		action = '%i/update' % id
	else:
		form = PostForm()
		title = 'Criar post'
		action = 'create'
		
	return render_template('form_post.html', form=form, title=title, action=action);
	
@app.route('/<int:id>/update', methods=['POST'])
@login_required
def update_post(id):
	post = Post.get_by_id(id)
	form = PostForm()
	if form.validate_on_submit():
		form.model = post
		form.save()
		flash('Poste atualizado.')
		return redirect(url_for('get'))
	return render_template('form_post.html', form=form)

@app.route('/create', methods=['POST'])
@login_required
def create_post():
	"""Método responsável em salvar informações do blog."""
	form = PostForm()
	if form.validate_on_submit():
		form.save()
		flash('Post foi salvo no banco de dados.')
		return redirect(url_for('get'))
	return render_template('form_post.html', form=form)
			
@app.route('/<int:id>/delete', methods=['GET'])
@login_required
def delete_post(id):
	"""Método responsável em remover um post do blog."""
	post = Post.get_by_id(id)
	if post:
		post.delete()
		flash("Post foi removido com sucesso.")
	else:
		flash("Erro ao tentar remover post.")
	return redirect(url_for('get'))
