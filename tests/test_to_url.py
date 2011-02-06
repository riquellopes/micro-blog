# -*- encoding: utf-8 -*-
#! usr/bin/python

import unittest 
from blog.util import slug

class TestToUrl(unittest.TestCase):

	def test_verifica_string_um_retorna_url_desejada(self):
		self.assertEquals(slug('Henrique Lopes'), 'henrique-lopes')

	def test_verifica_string_dois_retorna_url_desejada(self):
		self.assertEquals(slug('Carol Marques'), 'carol-marques')

	def test_verifica_string_tres_retorna_url_desejada(self):
		self.assertEquals(slug('Henrique'), 'henrique')

	def test_verifica_string_quatro_retorna_url_desejada(self):
		self.assertEquals(slug('Caçador de tecnologia'), 'cacador-de-tecnologia')

	def test_verifica_string_cinco_retorna_url_desejada(self):
		self.assertEquals(slug('Primeiro post sobre python.'), 'primeiro-post-sobre-python')

	def test_verifica_string_seis_retorna_url_desejada(self):
		self.assertEquals(slug('Ser ágil eis a questão. Você é ?'), 'ser-agil-eis-a-questao-voce-e')
	
if __name__ == '__main__':
	unittest.main()
