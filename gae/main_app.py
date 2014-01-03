from datetime import datetime

import utils

from google.appengine.ext import ndb
from js.bootstrap import bootstrap
import webapp2

import main_api_v1 as api
import main_model as model

class BaseHandler(utils.RequestHandler):
  i18n = True
  i18n_domain = "timecard"

class Index(BaseHandler):
  @utils.head(bootstrap)
  @utils.session_read_only
  def get(self):
    self.render_response("index.html", locals())

class Settings(BaseHandler):
  @utils.head(bootstrap)
  @utils.session
  def get(self):
    user = self.users.get_current_user()
    if user is not None:
      key = ndb.Key(model.User, user.user_id())
      entity = yield key.get_async()
      if entity is not None:
        user.name = entity.name
        user.set_to_session(self.session)
    self.render_response("settings.html", locals())

  @utils.head(bootstrap)
  @utils.session
  def post(self):
    user = self.users.get_current_user()
    if user is not None:
      name = self.request.POST.get("name")
      if name is not None:
        user.name = name
        user.set_to_session(self.session)
    yield api.user_store(user)
    self.render_response("settings.html", locals())

routes = [
  webapp2.Route("/", Index, name="index"),
  webapp2.Route("/settings", Settings, name="settings"),
]
