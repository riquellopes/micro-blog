# -*- encoding: utf-8 -*-
#! /usr/bin/python

import re
from unicodedata import normalize
import urllib


_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')

def slug(text, delim=u'-'):
	"""
		Code snippets:
		http://flask.pocoo.org/snippets/5/

		Generates an ASCII-only slug.
	"""
	result = []
	for word in _punct_re.split(text.lower()):
		word = normalize('NFKD', word.decode('utf-8')).encode('ASCII', 'ignore')
		if word:
		    result.append(word)
	return unicode(delim.join(result))
    
def to_url(string):
	"""Função responsável em parsear string para url valida."""
	string = normalize('NFKD', string.decode('utf-8')).encode('ASCII', 'ignore')
	string = re.sub(r"[^\w]+", "-", string)
	string = string.lower()
	
	return string

def short_url(url=None):
	"""Função responsável em encurtar tamanho de uma url"""
	short = urllib.urlopen("http://tinyurl.com/api-create.php?url=%s" % urllib.quote( url ) ).read()
	return short
