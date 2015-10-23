from google.appengine.ext import ndb

class bugEntry(ndb.Model):
	bugName = ndb.StringProperty(required=True)
	bugClass = ndb.StringProperty(required=False)
	platform = ndb.StringProperty(required=False)
	reproduce = ndb.StringProperty(required=False)
	description = ndb.StringProperty(required=False)