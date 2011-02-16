# usr/lib/python

import unittest
from flask import url_for
from blog.context_processor import admin_logged, rss_url, admin_logout_url


class TestContextProcessor(unittest.TestCase):

	def test_verifica_se_admin_esta_deslogado(self):
		self.assertEquals(admin_logged(), dict(admin_loggend=False))

	def test_verifica_se_url_para_logout_existe(self):
		pass
	
	def test_url_para_rss(self):
		self.assertEquals(rss_url(), dict(rss_url="http://twitter.com/statuses/user_timeline/riquellopes.atom"))
