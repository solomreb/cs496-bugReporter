import webapp2
import os
import jinja2
from google.appengine.ext import ndb
import base_page
import db_defs

class Update(base_page.MainHandler):
	def __init__(self, request, response):
		self.initialize(request, response)
		self.template_values={}

	def get(self):
		#get unique key from the url
		bug_key = ndb.Key(urlsafe=self.request.get('key'))
		#get entity/bug that corresponds to that key
		bug = bug_key.get()
		#populate bug attributes from form data
		bug.bugName = self.request.get('bugName')
		bug.bugClass = self.request.get('bugClass')
		bug.platform = self.request.get('platform')
		bug.reproduce = self.request.get('reproduce')
		bug.description = self.request.get('description')
		#save entity to ndb datastore
		bug.put()
		#pass bug to template
		self.template_variables['bug'] = bug
		#redirect to edit page
		self.redirect('/edit?key=' + bug_key.urlsafe())