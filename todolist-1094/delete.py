import webapp2
import os
import jinja2
from google.appengine.ext import ndb
import base_page
import db_defs

class Delete(base_page.MainHandler):
	def __init__(self, request, response):
		self.initialize(request, response)
		self.template_variables={}

	def get(self):
		
		bug_key = ndb.Key(urlsafe=self.request.get('key'))
		bug_key.delete()

		self.template_variables['delete'] = "success"
		self.render('delete.html', self.template_variables)


				