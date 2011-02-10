# -*- encoding: utf-8 -*-

from google.appengine.api.mail import EmailMessage
from flaskext.wtf import TextAreaField, TextField, Form, validators
ValidationError = validators.ValidationError
from datetime import datetime

__email__ = 'riquellopes@gmail.com'
validation_engine = []

class Contact(Form):
	nome = TextField()
	email = TextField([
		validators.email()
	])
	mensagem = TextAreaField()

	def __init__(self, *args, **kwargs):
		validation_engine = []
		super(Contact, self).__init__(*args, **kwargs)
		
	def send(self):
		"""Método que envia email para destinatário."""
		email = EmailMessage()
		
		email.sender = '%s <%s>' % ("rlopes-blog", __email__)
		email.subject = 'Fale comigo - rlopes'
		email.to = __email__
		email.body = """
					Nome: %(nome)s
					Data Contato: %(data)s
					Email: %(email)s
					%(messagem)s
										
					""" % {'nome':self.nome.data, 
						   'data':datetime.today().strftime('%d/%m/%Y'),
						   'messagem':self.mensagem.data,
						   'email':self.email.data}
		
		email.send()

	def validate_nome(form, field):
		"""
			Método que valida nome deacordo com as regras do blog.
		"""
		if field.data == "Digite seu nome" or len(field.data) == 0:
			validation_engine.append("['#nome', 'false', 'Digite seu nome']")
			raise ValidationError("Digite seu nome.")

	def validate_mensagem(form, field):
		"""
			Método que valida mensagem deacordo com as regras do blog.
		"""
		if field.data == "Escreva sua mensagem" or len(field.data) == 0:
			validation_engine.append("['#mensagem', 'false', 'Digite sua mensagem']")
			raise ValidationError("Escreva sua mensagem")

	def get_validation_engine(self):
		"""
			Método que cria um string com os campos que não atendem
			os critérios de validação do formulário de contato.
		"""
		return "[%s]" % (",".join(validation_engine))
