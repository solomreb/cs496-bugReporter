#!/usr/bin/env python

import webapp2


application = webapp2.WSGIApplication([
        #('/edit', 'edit.Edit'),
        #('/delete', 'delete.Delete'),
        #('/', 'base_page.MainHandler')
        ('/bug', 'bug.Bug')
    ], debug=True)

#delete bug, update bug, get one bug
application.router.add(webapp2.Route(r'/bug/<id:[0-9]+><:/?>', 'bug.Bug'))

#make a User associated with a bug
application.router.add(webapp2.Route(r'/bug/<bugid:[0-9]+>/user', 'user.User'))

#get a single User, update a User, delete a User
application.router.add(webapp2.Route(r'/user/<id:[0-9]+><:/?>', 'user.User'))