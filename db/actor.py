from db.expresso_object import ExpressoObject
from db.mongo.string_fields import EmailField, StringField

class Actor(ExpressoObject):
  pass

class Human(Actor):
  email_address = EmailField()
  access_token = StringField(max_length=40)
