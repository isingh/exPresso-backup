from db.mongo.mongo_document import MongoDocument
from db.mongo.string_fields import EmailField, StringField

class Actor(MongoDocument):
  pass

class Human(Actor):
  email_address = EmailField()
  access_token = StringField()
