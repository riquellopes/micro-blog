# usr/lib/python

import unittest
from blog.context_processor import admin_logged


class TestContextProcessor(unittest.TestCase):

	def test_verifica_se_admin_esta_deslogado(self):
		self.assertEquals(admin_logged(), dict(admin_loggend=False))
	
if __name__ == '__main__':
	unittest.main()
