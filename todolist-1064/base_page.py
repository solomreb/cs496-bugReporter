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

	def render(self, template, template_variables={}):
		template=self.jinja2.get_template(template)
		self.response.write(template.render(template_variables))

	def get(self):
		self.render('index.html')

	def post(self):
		action = self.request.get('action')

		#self.template_variables['form_content'] = {}
		#template = JINJA_ENVIRONMENT.get_template('index.html')
		#for i in self.request.arguments():
		#	self.template_variables['form_content'][i] = self.request.get(i)
		#self.response.write(template.render(self.template_variables))

		
		if action == 'add_bug':
			k = ndb.Key(db_defs.bugEntry, 'base-data')
			bug = db_defs.bugEntry(parent=k)
			bug.bugName = self.request.get('bugName')
			bug.bugClass = self.request.get('bugClass')
			bug.active = True
			bug.put()
			self.render('index.html', {'message': 'Added ' + bug.bugName + ' to database.'})
		else:
			self.render('index.html', {'message': 'Action is unknown.'})





