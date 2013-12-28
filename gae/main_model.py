#-* coding: utf-8 -*-
from google.appengine.ext import ndb

class User(ndb.Model):
  #key
  #user_id = ndb.StringProperty(indexed=True, required=True)

  name = ndb.StringProperty(indexed=False)
  #not_do_today = list of Issue

class Project(ndb.Model):
  #key auto

  name = ndb.StringProperty(indexed=False, required=True)
  description = ndb.TextProperty(indexed=False)
  is_public = ndb.BooleanProperty(indexed=False, default=True)
  closed = ndb.BooleanProperty(indexed=False, default=False)
  archive = ndb.BooleanProperty(indexed=False, default=False)
  admin = ndb.KeyProperty(indexed=True, kind=User, repeated=True) #required=True
  member = ndb.KeyProperty(indexed=False, kind=User, repeated=True)
  #github
  #ruffnote

class ArchivedComment(ndb.Model):
  datetime = ndb.DateTimeProperty(indexed=False, required=True)
  author = ndb.StringProperty(indexed=False, required=True)
  body = ndb.TextProperty(indexed=False, required=True)

class Issue(ndb.Model):
  #key
  #project = ndb.KeyProperty(indexed=True, kind=Project, required=True)
  #will_start_at = ndb.DateTimeProperty(indexed=False, auto_now_add=True)
  #author = ndb.StringProperty(indexed=False)

  subject = ndb.StringProperty(indexed=False, required=True)
  description = ndb.TextProperty(indexed=False)
  closed_on = ndb.DateTimeProperty(indexed=True)
  assignee = ndb.KeyProperty(indexed=True, kind=User)
  comment = ndb.LocalStructuredProperty(ArchivedComment, indexed=False, repeated=True, compressed=True)
  #closedしたらCommentを格納する

class WorkLoad(ndb.Model):
  #ユーザーは同時に複数のWorkLoadを作れない
  #key
  #project = ndb.KeyProperty(indexed=True, kind=Project, required=True)
  #issue = ndb.KeyProperty(indexed=True, kind=Issue, required=True)
  #start_at = ndb.DateTimeProperty(indexed=False, auto_now_add=True)

  end_at = ndb.DateTimeProperty(indexed=False)
  user = ndb.KeyProperty(indexed=True, kind=User, required=True)
  active = ndb.BooleanProperty(indexed=True, default=True)

class Comment(ndb.Model):
  #key
  #issue = ndb.KeyProperty(indexed=True, kind=Issue, required=True)
  #datetime = ndb.DateTimeProperty(indexed=False, auto_now_add=True)
  #author = ndb.StringProperty(indexed=False, required=True)

  body = ndb.TextProperty(indexed=False, required=True)
  project = ndb.KeyProperty(indexed=True, kind=Project, required=True)
