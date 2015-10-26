import webapp2 
from google.appengine.ext import ndb
import db_defs
import json

class Bug(webapp2.RequestHandler):
	#Make a new bug
	def post(self):			
		"""Creates a Bug entity
		
		POST variables:
		bugName - required	
		bugClass 
		platform 
		reproduce
		description
		"""
		
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not acceptable: Need a json"
			return

		new_bug = db_defs.Bug()
		bugName = self.request.get('bugName', default_value=None)
		if bugName:
			new_bug.bugName = bugName
		else:
			self.response.status = 400
			self.response.status_message = "Invalid request: bug name required"
		key = new_bug.put()
		out = new_bug.to_dict()
		self.response.write(json.dumps(out))
		

	#returns all or a specified bug(s)
	def get(self, **kwargs):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not acceptable: json required"
			return
		if 'id' in kwargs:
			out = ndb.Key(db_defs.Bug, int(kwargs['id'])).get().to_dict()
			self.response.write(json.dumps(out))
		else:
			q = db_defs.Bug.query()
			keys = q.fetch(keys_only=True)
			results = { 'keys' : [x.id() for x in keys]}
			self.response.write(json.dumps(results))


	#Update name of specified bug
	def put(self, **kwargs):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not acceptable: json required"
			return
		if 'id' not in kwargs:
			self.response.status = 400
			self.response.status_message = "Not acceptable: id required"
			return

		bug = ndb.Key(db_defs.Bug, int(kwargs['id'])).get()
		if not bug:
			self.response.status = 404
			self.response.status_message = "Bug Not Found"
			return

		updatedName = self.request.get('bugName', default_value=None)
		bug.bugName = updatedName
		
		bug.put()
		self.response.write(json.dumps(bug.to_dict()))
		return

	#Delete a specified bug
	def delete(self, **kwargs):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not acceptable: json required"
			return
		if 'id' not in kwargs:
			self.response.status = 400
			self.response.status_message = "Not acceptable: id required"
			return		
		
		bug_key = ndb.Key(db_defs.Bug, int(kwargs['id']))
		if not bug_key:
			self.response.status = 404
			self.response.status_message = "Bug Not Found"
			return

		bug_key.delete()
		self.response.status = 200	#ok
		self.response.status_message = "Bug Deleted"
		return




