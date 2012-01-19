"""All the fields
"""

class BaseField(object):
  """Base class for all the fields that can be written to mongodb.
  """
  def __init__(self, required=False, default=None):
    self._required = required
    self._new_value = default
    self._old_value = default


  def validate(self, new_value):
    return True

  def __set__(self, instance, value, validate=True):
    value = "%s" % value
    if self._required and not value:
      raise Exception("Required Field")
    if validate and not self.validate(value):
      raise Exception("Invalid value")
    if value != self._old_value:
      self._new_value = value
    return value

  def __get__(self, instance, owner):
    return self._new_value

  @property
  def value(self):
    return self._new_value

  def to_mongo(self):
    return self.value

