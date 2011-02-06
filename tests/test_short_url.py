# -*- encoding: utf-8 -*-
#! usr/bin/python

import unittest
from blog.util import short_url

class TestShortUrl(unittest.TestCase):

	def test_verifica_se_url_um_retorna_short_url_desejada(self):
		self.assertEquals(short_url('http://code.google.com/p/gaeunit/wiki/Readme'), 'http://tinyurl.com/2egns5f')
		
if __name__ == '__main__':
	unittest.main()
