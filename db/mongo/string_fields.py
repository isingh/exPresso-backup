import re

from db.mongo.fields import BaseField

class StringField(BaseField):
  """String values that can be written to Mongo.
  """
  def __init__(self, min_length=None, max_length=None, *args, **kwargs):
    super(StringField, self).__init__(*args, **kwargs)
    self._max_length = max_length
    if min_length:
      if min_length < 0:
        min_length = 0
    else:
      min_length = 0
    self._min_length = min_length


  def validate(self, new_value):
    length = len(new_value)
    if self._max_length and length > self._max_length:
      raise Exception("String exceeds maximum length of %s" %
          self._max_length)
    if self._min_length and length < self._min_length:
      raise Exception("String must have a minimum length of %s" %
          self._min_length)
    return True

class EmailField(StringField):
  """Email values that can be written to Mongo
  """
  _email_regex = re.compile(
      "^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$")

  def validate(self, new_value):
    super(EmailField, self).validate(new_value)
    if self._email_regex.match(new_value):
      return True
    raise Exception("Invalid email address")
