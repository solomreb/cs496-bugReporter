from google.appengine.ext import ndb

class Model(ndb.Model):
	def to_dict(self):
		d = super(Model, self).to_dict()
		d['key'] = self.key.id()
		return d

class Bug(ndb.Model):
	bugName = ndb.StringProperty(required=True)
	bugClass = ndb.StringProperty(required=False)
	platform = ndb.StringProperty(required=False)
	reproduce = ndb.StringProperty(required=False)
	description = ndb.StringProperty(required=False)
	users = ndb.KeyProperty(repeated=True)

	def to_dict(self):
		d = super(Bug, self).to_dict()
		d['users'] = [x.id for x in d['users']]
		return d

class User(Model):
	name = ndb.StringProperty(required=True)
	email = ndb.StringProperty(required=True)
	bugId = ndb.IntegerProperty(required=True)

	def to_dict(self):
		d = super(User, self).to_dict()
		d['name'] = str(d['name'])
		d['bugid'] = d['bugid'].id()
		return d