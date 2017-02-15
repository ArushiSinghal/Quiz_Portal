# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B('BoGGlers'),XML('&trade;&nbsp;'),
                  _class="navbar-brand",
                  _id="web2py-logo",_style="font-family:times;font-size:25px;")
response.title = request.application.replace('_',' ').title()
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.description = 'a cool new app'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('default', 'index'), [])
]

DEVELOPMENT_MENU = True

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################

def _():
    # shortcuts
    app = request.application
    ctr = request.controller
    # useful links to internal and external resources
    response.menu += [
        (T('RESUME'), False, URL('QUIZES_OVERLOADED', 'default', 'res')),
         (T('UPLOAD'), False, None, [
             (T('TITLE'), False,
              URL('QUIZES_OVERLOADED', 'default', 'title')),
              (T('QUESTIONS'), False, URL('QUIZES_OVERLOADED', 'default', 'upload_quiz')),

              ]),
          (T('Feedback'), False, URL('QUIZES_OVERLOADED', 'default', 'feedback')),
         (T('Reviews'), False, URL('QUIZES_OVERLOADED', 'default', 'reviews')),
          (T('ABOUT US'), False, None, [
             (T('Facebook'), False,
              'https://www.facebook.com/profile.php?id=100001819333007'),
              (T('Twitter'), False, 'http://twitter.com/web2py'),

              ]),
        ]
if DEVELOPMENT_MENU: _()

if "auth" in locals(): auth.wikimenu()
