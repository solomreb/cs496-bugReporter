from google.appengine.ext import ndb

class bugEntry(ndb.Model):
	bugName = ndb.StringProperty(required=True)
	bugClass = ndb.StringProperty(required=True)
	platform = ndb.StringProperty(required=True)
	reproduce = ndb.BooleanProperty(required=True)
	description = ndb.StringProperty(required=True)