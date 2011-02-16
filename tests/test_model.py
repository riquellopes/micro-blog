# -*- encoding:utf-8 -*-

import unittest
from blog.model import Post, TagCategory
from nose.tools import assert_equals, assert_true, assert_raises

class TestPost(unittest.TestCase):

	def setUp(self):
		tag = TagCategory()
		self.post = Post(title='Primeiro post',
						 text='<b>Nose test e fd</b>',
						 tags=tag.string_to_category('python, nose, tdd'))

		self.post.put()
		
	def test_verifica_se_post_foi_salvo_corretamente(self):
		assert_equals(self.post.url, 'primeiro-post')

	def test_verifica_se_texto_foi_salvo_corretamente(self):
		assert_equals(self.post.text, u'<b>Nose test e fd</b>')

	def test_verifica_se_tags_property_criado_corretamente(self):
		tag = TagCategory()
		categories = tag.string_to_category('python, nose, tdd')
		assert_equals(self.post.tags, categories)

	def test_verifica_se_title_foi_salvo_corretamente(self):
		assert_equals(self.post.title, 'Primeiro post')

	def test_apos_salvar_post_put_deve_retornar_a_chave_da_entidade(self):
		tag = TagCategory()
		post = Post(title='Primeiro post',
					text='<b>Nose test e fd</b>',
					tags=tag.string_to_category('python, nose, tdd'))
		
		assert_true(type(post.put().id()).__name__ == 'int')
		post.delete()
				
	def tearDown(self):
		self.post.delete()

class TestTagCategory(unittest.TestCase):

	def test_retorno_string_to_category(self):
		tag = TagCategory()
		assert_equals([u'nose', u'python', u'tdd'], 
					  tag.string_to_category('python, nose, tdd'))

	def test_se_nao_for_passada_string_para_to_category_deve_levantar_uma_exception(self):
		tag = TagCategory()
		assert_raises(ValueError, tag.string_to_category, 123)
