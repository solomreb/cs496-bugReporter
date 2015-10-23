import webapp2
import os
import jinja2
from google.appengine.ext import ndb
import base_page
import db_defs

class Edit(base_page.MainHandler):
	def __init__(self, request, response):
		self.initialize(request, response)
		self.template_variables={}

	def get(self):
		action = self.request.get('action')
		bug_key = ndb.Key(urlsafe=self.request.get('key'))
		bug = bug_key.get()

		if action == 'edit_bug':
			if self.request.get('bugName') == "":
				self.template_variables['message'] = "Title required"
			else:
				bug.bugName = self.request.get('bugName')
				bug.bugClass = self.request.get('bugClass')
				bug.platform = self.request.get('platform')
				bug.reproduce = self.request.get('reproduce')
				bug.description = self.request.get('description')
				bug.put()
		self.template_variables['bug'] = bug
		self.template_variables['bug_key'] = self.request.get('key')
		self.render('edit.html', self.template_variables)




				