# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

## app configuration made easy. Look inside private/appconfig.ini
from gluon.contrib.appconfig import AppConfig
## once in production, remove reload=True to gain full speed
myconf = AppConfig(reload=True)


if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    db = DAL(myconf.take('db.uri'), pool_size=myconf.take('db.pool_size', cast=int), check_reserved=['all'])
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore+ndb')
    ## store sessions and tickets there
    session.connect(request, response, db=db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## choose a style for forms
response.formstyle = myconf.take('forms.formstyle')  # or 'bootstrap3_stacked' or 'bootstrap2' or other
response.form_label_separator = myconf.take('forms.separator')


## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'
## (optional) static assets folder versioning
# response.static_version = '0.0.0'
#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################
db = DAL('sqlite://storage.sqlite')
from gluon.tools import Auth, Service, PluginManager

auth = Auth(db)
service = Service()
plugins = PluginManager()

## create all tables needed by auth if not custom tables
auth.define_tables(username=True)

## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else myconf.take('smtp.server')
mail.settings.sender = myconf.take('smtp.sender')
mail.settings.login = myconf.take('smtp.login')
mail.settings.tls = myconf.get('smtp.tls') or False
mail.settings.ssl = myconf.get('smtp.ssl') or False
## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples foor controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

## after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
db.define_table('titles',
                Field('title_name', unique=True),
                format = '%(title_name)s' )


db.define_table('upload_question',
                Field('title','reference titles',requires=IS_IN_DB(db, db.titles, '%(title_name)s')),
                Field('question','text'),
                Field('option_a'),
                Field('option_b'),
                Field('option_c'),
                Field('option_d'),
                Field('answer_a','boolean'),
                Field('answer_b','boolean'),
                Field('answer_c','boolean'),
                Field('answer_d','boolean'),
                )

db.define_table('checking',
                Field('question_id','reference upload_question'),
                Field('current_user','reference auth_user', default=auth.user_id),
                Field('answer_a','boolean'),
                Field('answer_b','boolean'),
                Field('answer_c','boolean'),
                Field('answer_d','boolean'),
                Field('title','reference titles'),
                Field('count','integer'),
                Field('show','text')
                )

db.define_table('tempstore',
              Field('count','integer'),
              Field('check_ans','text')
)

db.define_table('recipe_likes',
             Field('liked_by','reference auth_user', default=auth.user_id),
             Field('recipe', 'reference titles' ))

db.define_table('feedback',
     Field('name',default=session.auth.user.first_name if session.auth else None,writable=False),
     Field('your_views','text'),
     Field('created_on', 'datetime', default=request.now),
     Field('rating','integer',default=0))
db.feedback.rating.requires=IS_IN_SET(['1','2','3','4','5'])
db.feedback.name.readable = db.feedback.name.writable = False
db.feedback.created_on.readable = db.feedback.created_on.writable = False
