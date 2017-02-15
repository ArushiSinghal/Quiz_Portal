# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    rows=db().select(db.titles.ALL,orderby=db.titles.title_name)
    
    #print type(value)
    
    coloms=db().select(db.titles.ALL,orderby=db.titles.title_name)
    #print coloms
    return dict(rows=rows,coloms=coloms)
@auth.requires_login()
def show():
    value = request.vars.value
    b = auth.user_id
    cols = db((db.checking.title == value) & (db.checking.current_user == b)).select(db.checking.ALL)
    if cols:
        session.flash=T('You Paused a Quiz ,  choose from here')
        redirect(URL('res'))
    else :    
        rows = db(db.upload_question.title == value).select(db.upload_question.ALL)
        i=1
        for row in rows:
            #print type(row.id)
            #print type(auth.user_id)
            #print "row.id",row.id
            #print auth.user_id
            #db.executesql("INSERT INTO checking (question_id,current_user) VALUES ('%d','%d')" % (row.id,auth.user_id))
            db.executesql("INSERT INTO checking (question_id,current_user,answer_a,answer_b,answer_c,answer_d,title,count,show) VALUES ('{0}','{1}','False','False','False','False','{2}','{3}','UnAttempted')" .format(row.id,auth.user_id,value,i))
            i = i + 1
        #print "id",b
        cols = db((db.checking.title == value) & (db.checking.current_user == b)).select(db.checking.ALL)
        return dict(rows=rows,value=value,b=b,cols=cols)
def show1():
    a = request.vars.id1
    b = request.vars.id2
    #print "a",a
    #print "b",b
    db((db.checking.question_id == a) & (db.checking.current_user == auth.user_id)).update(answer_a = 'True')
    
    
def show2():
    a = request.vars.id1
    b = request.vars.id2
    #print "a",a
    #print "b",b
    db((db.checking.question_id == a)& (db.checking.current_user == auth.user_id)).update(answer_b = 'True')
def show3():
    a = request.vars.id1
    b = request.vars.id2
    #print "a",a
    #print "b",b
    db((db.checking.question_id == a)& (db.checking.current_user == auth.user_id)).update(answer_c = 'True')
def show4():
    a = request.vars.id1
    b = request.vars.id2
    #print "a",a
    #print "b",b
    db((db.checking.question_id == a)& (db.checking.current_user == auth.user_id)).update(answer_d = 'True')

def finish():
    value=request.args(0)
    user=request.args(1)
    #print "user",user
    i = 1
    rows = db((db.checking.title == value) & (db.checking.current_user == user)).select(db.checking.ALL)
    for row in rows:
        db.executesql("INSERT INTO tempstore (count,check_ans) VALUES ('{0}','Incorrect')" .format(i))
        i = i + 1
    slct = db().select(db.upload_question.ALL)
    val = 0
    for row in rows:
        choose = db(db.upload_question.id == row.question_id).select(db.upload_question.ALL)
        for chose in choose :
            if (row.answer_a == chose.answer_a and row.answer_b == chose.answer_b and row.answer_c == chose.answer_c and row.answer_d == chose.answer_d ) :
                db((db.tempstore.count == row.count)).update(check_ans = 'Correct')
                val = val + 10
    usr = db(db.auth_user.id == user).select(db.auth_user.ALL)
    temps = db().select(db.tempstore.ALL)
    rows = db(db.upload_question.title == value).select(db.upload_question.ALL)
    likes = db(db.recipe_likes.recipe == value).count()
    if auth.user_id:
        liked = db((db.recipe_likes.recipe == value) & (db.recipe_likes.liked_by == auth.user_id)).select()
        liked = True if len(liked) == 1 else False
    else:
        liked = False
    return dict(val=val,usr=usr,value=value,user=user,rows=rows,temps=temps,likes=likes,liked=liked)

def home():
    value=request.args(0)
    user=request.args(1)
    db((db.checking.title == value) & (db.checking.current_user == user)).delete()
    db.tempstore.truncate()
    redirect(URL('index'))
@auth.requires_login()
def resume():
    value = request.vars.value
    b = auth.user_id
    cols = db((db.checking.title == value) & (db.checking.current_user == b)).select(db.checking.ALL)
    if not cols:
        session.flash=T('You Never Paused a Quiz , thus choose from here')
        redirect(URL('index'))
    else:    
        rows = db(db.upload_question.title == value).select(db.upload_question.ALL)
        return dict(rows=rows,value=value,b=b,cols=cols)
@auth.requires_login()
def res():
    rows=db().select(db.titles.ALL,orderby=db.titles.title_name)
    
    #print type(value)
    
    coloms=db().select(db.titles.ALL,orderby=db.titles.title_name)
    #print coloms
    return dict(rows=rows,coloms=coloms)
@auth.requires_login()
def title():
    form = SQLFORM(db.titles).process()
    return locals()
@auth.requires_login()
def upload_quiz():
    form = SQLFORM(db.upload_question).process()
    return locals()

def like():
    value = request.args(0)
    liked = db((db.recipe_likes.recipe == value)& (db.recipe_likes.liked_by == auth.user_id)).count()
    liked = True if liked == 1 else False
    if not liked:
        db.recipe_likes.insert(recipe=value, liked_by=auth.user_id)
    redirect(URL('finish', args=request.args))
    return dict()

def unlike():
    value = request.args(0)
    liked = db((db.recipe_likes.recipe == value) & (db.recipe_likes.liked_by == auth.user_id)).select().first()
    if liked:
        del db.recipe_likes[liked.id]
    redirect(URL('finish', args=request.args))
    return dict()
@auth.requires_login()
def feedback():
    hello = SQLFORM(db.feedback).process()
    return dict(hello=hello)

@auth.requires_login()
def reviews():
    rows=db().select(db.feedback.ALL,orderby=~db.feedback.created_on)
    return dict(rows=rows)
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
