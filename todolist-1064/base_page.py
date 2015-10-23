import webapp2
import os
import jinja2
from google.appengine.ext import ndb
import db_defs


class MainHandler(webapp2.RequestHandler):
	
	@webapp2.cached_property
	def jinja2(self):
		return jinja2.Environment(
			loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'),
			extensions=['jinja2.ext.autoescape'],
			autoescape=True
			)

	template_variables = {}


	def __init__(self, request, response):
		self.initialize(request, response)
		self.template_variables = {}

	def render(self, template, template_variables={}):
		template=self.jinja2.get_template(template)
		self.response.write(template.render(template_variables))

	def get(self):
		self.template_variables['bugs'] = [{'name': x.bugName, 'class': x.bugClass, 'platform': x.platform, 'reproduce': x.reproduce, 'description': x.description, 'key': x.key.urlsafe()} for x in db_defs.bugEntry.query(ancestor=ndb.Key(db_defs.bugEntry, 'base-data')).fetch()]
		self.render('index.html', self.template_variables)

	def post(self):
		action = self.request.get('action')
		
		if action == 'add_bug':
			if self.request.get('bugName') == "":
				self.template_variables['message'] = "Title required"
			else:
				k = ndb.Key(db_defs.bugEntry, 'base-data')
				bug = db_defs.bugEntry(parent=k)

				bug.bugName = self.request.get('bugName')
				bug.bugClass = self.request.get('bugClass')
				bug.platform = self.request.get('platform')
				bug.reproduce = self.request.get('reproduce')
				bug.description = self.request.get('description')
				bug.put()

			self.template_variables['bugs'] = [{'name': x.bugName, 'class': x.bugClass, 'platform': x.platform, 'reproduce': x.reproduce, 'description': x.description, 'key': x.key.urlsafe()} for x in db_defs.bugEntry.query(ancestor=ndb.Key(db_defs.bugEntry, 'base-data')).fetch()]
			self.render('index.html', self.template_variables)
	




