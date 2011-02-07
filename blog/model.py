# -*- coding: utf-8 -*-
"""
	Blog rlopes Models
	------------------
"""

import string
from google.appengine.ext import db
from util import slug, short_url

class TagCategory:
		
	def string_to_category(self, tag_string):
		"""
		A function to validate a comma-separated list of tags.
	 
		try:
		    tags = validate_category_list("ai, computer science, lisp")
		except ValueError:
		    # Display error to user that the submitted tags were not formated correctly
		    pass
		except:
		    # Something bad happened, handle it
		    pass
	 
		@string list of category items
		@string optional regex for validating each list item
		"""

		# Only accept a parameter of type string or type unicode
		if not type(tag_string) in [unicode, str]:
			raise ValueError("Passed category list must be of type string or unicode.")

		 # Split comma-separated list into an array
		tags = tag_string.split(',')

		# Remove whitespace from each list item
		tags = map(string.strip, tags)

		 # Remove duplicate categories
		tags = {}.fromkeys(tags).keys()

		# When a user enters a comma at the end of a line a blank string is
    		# inserted into the list.
    		# Example: ['ai', 'computer science', 'lisp', '']
    		# This removes that empty string
		try:
			tags.remove(" ")
		except:	pass

		# Sort list alphabetically
		tags.sort()

		# Return list as an array of db.Category items
    		# Example: [db.Category('ai'), db.Category('computer science'), db.Category('lisp')]
		return map(db.Category, tags)
		
class Post(db.Model):
	title = db.StringProperty(required = True)
	text = db.TextProperty(required = True) 
	tags = db.ListProperty(db.Category)
	user = db.UserProperty()
	url = db.StringProperty();
	date_create = db.DateTimeProperty(auto_now_add = True) 
	INDEX_ONLY = ['url', 'title', 'tags']
				
	def put(self):
		"""
			Método responsável em salvar informações no bigtable.
			Após conteúdo ser salvo, url é envida para o twiter,
			informando que existe um novo post no blog.
		"""
		
		self.url = slug(self.title)
		return super(Post, self).put()
