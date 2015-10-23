#!/usr/bin/env python

import webapp2


application = webapp2.WSGIApplication([
		('/edit', 'edit.Edit'),
		('/delete', 'delete.Delete'),
		('/', 'base_page.MainHandler')
	], debug=True)
