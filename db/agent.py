from db.expresso_object import ExpressoObject
from db.mongo.fields import DbObjectIdField
from db.mongo.string_fields import StringField

class Agent(ExpressoObject):
  pass

class Song(Agent):
  album = StringField()
  artist = StringField()

class Book(Agent):
  author = StringField()
  added_by = DbObjectIdField()

