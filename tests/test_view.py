# /usr/bin/env python
import unittest
from nose.tools import assert_true, assert_equals
import mocker
from lxml import html
from blog import app
from blog.model import Post, TagCategory
from blog.util import slug

class TestView(unittest.TestCase):

	def setUp(self):
		self.app  = app.test_client()
		tag = TagCategory()
		self.post = Post(title='Primeiro post',
						 text='<b>Nose test e fd</b>',
						 tags=tag.string_to_category('python, nose, tdd'))

		self.post.put() 
		self.mocker = mocker.Mocker()
		
	def tearDown(self):
		self.post.delete()
		self.mocker.restore()
		
	def test_index(self):
		response =  self.app.get('/')
		assert_true('<title> rlopes | Henrique Lopes</title>' in str(response.data) )

	def test_read_post(self):
		response = self.app.get("/post/%s" % self.post.url)
		title = '<h3><span><a href="/post/%s">%s</a></span></h3>' % (self.post.url, self.post.title)
		assert_true(title in str(response.data))

	def test_read_post_that_not_exist(self):
		response = self.app.get("/post/meu-primeiro-post")
		assert_true('<title> Ops! Error 404 | Henrique Lopes</title>' in str(response.data))
		
	def admin_loggend(self, times=1):
		loggend = self.mocker.replace('google.appengine.api.users.is_current_user_admin')
		loggend()
		self.mocker.result(True)
		self.mocker.count(times)
		self.mocker.replay()

	def test_form_insert(self):
		self.admin_loggend(10)
		response = self.app.get("/form")
		assert_true('<title> Criar post | Henrique Lopes</title>' in str(response.data))	

	def test_form_update(self):
		self.admin_loggend(5)
		url = "/%i/form" % self.post.key().id()
		response = self.app.get(url)
		title = '<title> Update - %s | Henrique Lopes</title>' % self.post.title
		assert_true(title in str(response.data))
		
	def test_create_post(self):
		self.admin_loggend(10)
		data = {
			'title':"My first post. bla bla bla",
			'tags':"python,tdd",
			'text':"bla bla bla bla bla bla bla bla"
		}
		response = self.app.post("/create", data=data, follow_redirects=True)
		post = Post.all().filter('url', slug(data['title'])).get()			
		assert_equals(post.title, data['title'])
		post.delete()

	def test_create_post_validate(self):
		self.admin_loggend(10)
		data={}
		response = self.app.post("/create", data=data, follow_redirects=True)
		assert_true("O Titulo deve ter entre 5 a 60 caracteres." in str(response.data))

	def test_update_post(self):
		self.admin_loggend(10)
		data={
			'title':"My uppdates.",
			'tags':"python, nose, tdd, dojo",
			'text':"<b>Nose test e fd</b>"
		}
		url = "%i/update" % self.post.key().id()
		response = self.app.post(url, data=data, follow_redirects=True)
		post = Post.get_by_id( self.post.key().id() )
		assert_equals(post.title, data['title'] )

	def test_update_post_validate(self):
		self.admin_loggend(10)
		data={
			'title':"My uppdates.",
			'tags':"python, nose, tdd, dojo",
			'text':""
		}
		url = "%i/update" % self.post.key().id()
		response = self.app.post(url, data=data, follow_redirects=True)
		assert_true("O Texto deve ter no minimo 5 caracteres." in str(response.data))

	def tags_to_string(self, tags):
		tstr = ""
		for tag in tags:
			tstr += "%s," % tag
		return tstr[:-1]
		
	def test_form_populate(self):
		self.admin_loggend(10)
		url = "%i/form" % self.post.key().id()
		response = self.app.get(url)
		dom = html.fromstring(response.data)
		input_title = dom.xpath('//input[@type="text" and @name="title"]')[0]
		input_tags = dom.xpath('//input[@type="text" and @name="tags"]')[0]
		textare_text = dom.xpath('//textarea[@name="text"]')[0]
		assert_equals(input_title.value, self.post.title)
		assert_equals(input_tags.value, self.tags_to_string(self.post.tags))
		assert_equals(textare_text.value, self.post.text) 
					
	def test_delete_post(self):
		self.admin_loggend(5)
		tag = TagCategory()
		post = Post(title='Primeiro post',
					text='<b>Nose test e fd</b>',
					tags=tag.string_to_category('python, nose, tdd'))
		post.put()
		url="%i/delete" % post.key().id()			
		self.app.get(url)
		post = Post.get_by_id( post.key().id() )
		assert_true(post is None)	

	def test_send_email(self):
		data = {
			'nome':"Henrique",
			'email':"riquellopes@gmail.com",
			'mensagem':"O blog esta ficando bom."
		}
		response = self.app.post('/contact', data=data, follow_redirects=True)
		assert_true("True", str(response.data))

	def test_send_email_error(self):
		data={
			'nome':"",
			'email':"riquellopes@gmail.com",
			'text':""
		}
		response= self.app.post('/contact', data=data, follow_redirects=True)
		assert_true("[['#mensagem', 'false', 'Digite sua mensagem'],\
					 ['#nome', 'false', 'Digite seu nome']]", str(response.data))
