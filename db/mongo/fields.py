"""All the fields
"""

from pymongo.objectid import ObjectId

class BaseField(object):
  """Base class for all the fields that can be written to mongodb.
  """
  _object_type = None

  def __init__(self, required=False, default=None):
    self._required = required
    self._new_value = default
    self._old_value = default


  def validate(self, new_value):
    return True

  def check_type(self, new_value):
    if not new_value:
      return True
    if self._object_type is None or isinstance(new_value, self._object_type):
      return True
    return False

  def __set__(self, instance, value, validate=True):
    if self._required and value is None:
      raise Exception("Required Field")
    if not self.check_type(value):
      raise Exception("Please check the type of the object")
    if validate and not self.validate(value):
      raise Exception("Invalid value")
    if value != self._old_value:
      self._new_value = value
    return value

  @property
  def is_valid(self):
    if self._required and not self.value:
      return False
    try:
      return self.validate(self.value)
    except:
      pass
    return False

  def __get__(self, instance, owner):
    return self._new_value

  @property
  def value(self):
    return self._new_value

  def to_mongo(self):
    return self.value

class DbObjectIdField(BaseField):
  """Class to store a reference to another db object.
  """
  _object_type = ObjectId

class IntegerField(BaseField):
  _object_type = int
