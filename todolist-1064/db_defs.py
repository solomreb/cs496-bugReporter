from google.appengine.ext import ndb

class bugEntry(ndb.Model):
	bugName = ndb.StringProperty(required=True)
	bugClass = ndb.StringProperty(required=True)
	active = ndb.BooleanProperty(required=True)