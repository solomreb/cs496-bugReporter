#!/usr/bin/env python

import webapp2


application = webapp2.WSGIApplication([
		('/edit', 'edit.Edit'),
		('/update', 'update.Update'),
		('/', 'base_page.MainHandler')
	], debug=True)
