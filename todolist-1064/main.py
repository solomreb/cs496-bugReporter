#!/usr/bin/env python

import webapp2


application = webapp2.WSGIApplication([
		('/', 'base_page.MainHandler')
	], debug=True)
