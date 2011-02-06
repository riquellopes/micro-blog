# -*- encoding: utf-8 -*-
"""
	Blog rLopes Forms
	-----------------
"""

from flaskext.wtf import TextField, TextAreaField, Form, validators
from model import Post, TagCategory 
 

class PostForm(Form):
	title = TextField('Titulo:', [
		validators.Length(min=5, max=60, message="O Titulo deve ter entre 5 a 60 caracteres.")
	])
	text =  TextAreaField('Texto:', [
		validators.Length(min=5, message="O Texto deve ter no minimo 5 caracteres.")
	])
	tags = TextField('Tags:',[
		validators.required(message="Informe uma tag.")
	])
		
	def __init__(self, model_instance = None, *args, **kwargs):
		"""Método construtor da classe, preenche model ao criar form."""
		kwargs['csrf_enabled'] = False
		super(PostForm, self).__init__(*args, **kwargs)
		self.model = None
		if model_instance:
			self.title.data = model_instance.title
			self.text.data = model_instance.text
			self.tags.data = self.get_tags( model_instance.tags )
			self.model = model_instance
			 
	def save(self):
		"""Método responsável em salvar post no bigtable."""
		if self.model:
			self.model.title = self.title.data
			self.model.text = self.text.data
			self.model.tags = self.set_tags(self.tags.data)
		else:	
			self.model = Post(
							title = self.title.data,
							text = self.text.data,
							tags = self.set_tags(self.tags.data)
						)
		self.model.put()
		return self.model

	def get_tags(self, tags):
		"""Metodo que recupera valor do atributo tags."""
		tstr = ""
		for tag in tags:
			tstr += "%s," % tag
		return tstr[:-1]

	def set_tags(self, tags):
		"""Método que define valor para o atributo tags."""
		tag = TagCategory()
		return tag.string_to_category( tags )	
