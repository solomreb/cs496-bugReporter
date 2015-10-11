#!/usr/bin/env python

import webapp2


application = webapp2.WSGIApplication([
		('/edit', 'edit.Edit'),
		('/', 'base_page.MainHandler')
	], debug=True)
