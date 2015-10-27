import webapp2
import datetime
from google.appengine.ext import ndb
import db_defs
import json

class User(webapp2.RequestHandler):
	#make a User associated with a single bug
	def post(self, **kwargs):
		"""Creates a User entity

		POST Body Variables:
		name- Required
		email- Required
		bugid- Required
		"""	

		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not acceptable: Need a json"
			return	
		if 'bugid' not in kwargs:
			self.response.status = 400
			self.response.status_message = "Not acceptable: Need a bug ID"
			return
		bugKey = ndb.Key(db_defs.Bug, int(kwargs['bugid']))
		if not bugKey:
			self.response.status = 404
			self.response.status_message = "Bug not Found"
			return
	

		new_user = db_defs.User()
		new_user.bugid = bugKey
		
		
		name = self.request.get('name', default_value=None)
		email = self.request.get('email', default_value=None)
		if name:
			new_user.name = name
		else:
			self.response.status = 400
			self.response.status_message = "Not acceptable: Need a Name"

		if email:
			new_user.email = email
		else:
			self.response.status = 400
			self.response.status_message = "Not acceptable: Need an Email"

		key = new_user.put()
		out = new_user.to_dict()
		self.response.write(json.dumps(out))
		
		#Add this User to the bug's users
		bug = ndb.Key(db_defs.Bug, int(kwargs['bugid'])).get()
		user.append(key)

		bkey = bug.put()
		return

	def get(self, **kwargs):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not acceptable: Need a json"
			return
		
		#Get all Users associated with a specified bug
		if 'bugid' in kwargs:
			bug = ndb.Key(db_defs.Bug, int(kwargs['bugid'])).get()
			if not bug:
				self.response.status = 404
				self.response.status_message = "bug not Found"
				return				
			bug_users= {'keys' : [x.id() for x in bug.users]}
			self.response.write(json.dumps(bug_Users))
			return

		#Get specified User
		if 'id' in kwargs:
			out = ndb.Key(db_defs.Users, int(kwargs['id'])).get().to_dict()
			self.response.write(json.dumps(out))
			return	

	def put(self, **kwargs):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not acceptable: Need a json"
			return
		if 'id' not in kwargs:
			self.response.status = 400
			self.response.status_message = "Not acceptable: Need an id to update a User"
			return		

		user = ndb.Key(db_defs.Users, int(kwargs['id'])).get()
		if not User:
			self.response.status = 404
			self.response.status_message = "User not Found"
			return
		new_name = self.request.get('name', default_value=None)
		new_email = self.request.get('email', default_value=None)

		if new_name:
			user.name = new_name
		if new_email:
			user.email = new_email

		user.put()
		self.response.write(json.dumps(user.to_dict()))

	def delete(self, **kwargs):
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not acceptable: Need a json"
			return
		if 'id' not in kwargs:
			self.response.status = 400
			self.response.status_message = "Not acceptable: Need an id to delete a User"
			return		

		user = ndb.Key(db_defs.User, int(kwargs['id'])).get()
		if not user:
			self.response.status = 404
			self.response.status_message = "User not Found"
			return


		"""Ideas for why this isnt working:
		-User is actually deleted from User table, so this isn't being hit anymore?
			-Therefore, cannot delete it from ski table??
		"""

		#Save bugid before delete User entity
		bug = ndb.Key(db_defs.Bug, int(user.bugid)).get()

		#Delete User entity from Users table
		user.key.delete()

		#Delete User from bug's User list
		#Get bug entity
		bug = bug.get()
		
		bug_users = [x.id() for x in bug.users]
		bug_users.remove(UserKey)

		bug.users = bug_users

		bug.put()

		return













		
