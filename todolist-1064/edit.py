from google.appengine.ext import ndb
import base_page
import db_defs

class Edit(base_page.MainHandler):
	def __init__(self, request, response):
		self.initialize(request, response)
		self.template_values={}
	#	self.template_values['edit_url'] = blobstore.create_upload_url( '/edit/channel')

	def get(self):
		bug_key = ndb.Key(urlsafe=self.request.get('key'))
		bug = bug_key.get()
		self.template_values['bug'] = bug
		bugs = db_defs.bugEntry.query(ancestor=ndb.Key(db_defs.bugEntry, 'base-data')).fetch()
		
		self.render('edit.html',self.template_values)