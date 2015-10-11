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

	#template_variables = {}

	def render(self, template, template_variables={}):
		template=self.jinja2.get_template(template)
		self.response.write(template.render(template_variables))

	def get(self):
		self.render('index.html')

	def post(self):
		action = self.request.get('action')

		#self.template_variables['form_content'] = {}

		#for i in self.request.arguments():
			#self.template_variables['form_content'][i] = self.request.get(i)
		#self.response.write(template.render(self.template_variables))

		#[{'name':x.name, 'key':x.key.urlsafe()} for x in db_defs.bugEntry.query().fetch()]
		if action == 'add_bug':
			k = ndb.Key(db_defs.bugEntry, 'base-data')
			bug = db_defs.bugEntry(parent=k)
			bug.bugName = self.request.get('bugName')
			bug.bugClass = self.request.get('bugClass')
			bug.active = True
			bug.put()
			#self.template_variables['message'] = 'Added ' + {{ bug.bugName }} + ' to database'
		#elif action == 'edit_bug':
		#take to edit page
		#else:
			#self.template_variables['message'] = 'Unknown action.'
			self.render('index.html', {'message': 'Success', 'bugName': bug.bugName, 'bugClass': bug.bugClass, 'active': bug.active})





