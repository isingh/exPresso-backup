from pymongo import Connection

from document import Document

DATABASE_NAME = 'expresso_db'

class MongoDocument(Document):
  def __init__(self, db_name=None, collection_name=None, document=None):
    super(MongoDocument, self).__init__()
    self._mongo_object = None
    self._id = None

    self._collection = self.get_collection(db_name, collection_name)

    all_attributes = self.document_attributes
    unique_attributes = self.__class__.__dict__.get('unique_attributes', [])
    self._unique_attributes = [attribute \
        for attribute in unique_attributes if attribute in all_attributes]

    self._load_from_document(document)

  def _load_from_document(self, document):
    if document is None:
      return
    try:
      self._id = document.pop('_id')
    except KeyError:
      pass

    for attribute, value in document.iteritems():
      self._attribute_values[attribute].__set__(self, value, False)

  @property
  def is_new(self):
    return self._id is None

  def save(self):
    self._attribute_values.update(self._new_attributes_values)
    if self._id is not None:
      self._collection.save(self.document_to_write)
    else:
      self._id = self._collection.insert(self.document_to_write)
    self._new_attributes_values = {}

  @property
  def document_to_write(self):
    document = { key: value.to_mongo() \
        for key, value in self._attribute_values.iteritems()}
    if self._id is not None:
      document['_id'] = self._id
    return document

  @classmethod
  def get_collection(cls, db_name=None, collection_name=None):
    db_name = db_name or 'expresso_db'
    collection_name = collection_name or cls.__name__
    return Connection()[db_name][collection_name]

  @classmethod
  def find_one(cls, search_criteria, db_name=None, collection_name=None):
    collection = cls.get_collection(db_name, collection_name)
    return cls(document=collection.find_one(search_criteria))

