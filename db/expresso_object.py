from db.mongo.mongo_document import MongoDocument
from db.mongo.string_fields import StringField

class ExpressoObject(MongoDocument):
  name = StringField(max_length=256, required=True)
