import copy
from collections import deque
from fields import BaseField

class Document(object):
  """A document is a collection of fields (which are descriptors).
  It has a list of available attributes, and keeps their values.
  """
  def __init__(self):
    """Constructor to create a Document.
    """
    # Dictionary containing all the attributes, and their values
    # Initialized to None for all valid attributes.
    self._attribute_values = {}

    # Attributes whose values have changed are kept here.
    self._new_attributes_values = {}

    self._attributes_initialized = False
    self._all_classes = self._get_all_classes()
    self._init_attributes()

  def _get_all_classes(self):
    """Get a list of all the classes that compose the current object.

    Returns:
      A list of all classes, which includes the current class, and all
      its parent classes.
    """
    classes_remaining = deque([self.__class__])
    all_classes = []
    while True:
      try:
        current_class = classes_remaining.popleft()
        all_classes.append(current_class)
        for base in current_class.__bases__:
          classes_remaining.append(base.__mro__[0])
      except IndexError:
        break
    return all_classes

  def _init_attributes(self):
    """Initialize the attributes that are to be used in the document.
    """
    if self._attributes_initialized:
      raise Exception("The attributes are already initialized")
    for current_class in self._all_classes:
      for attribute, value in current_class.__dict__.iteritems():
        if isinstance(value, BaseField):
          self._attribute_values[attribute] = copy.deepcopy(value)
    self._attributes_initialized = True

  def __setattr__(self, attribute, value):
    if hasattr(self, '_attribute_values') and \
        attribute in self._attribute_values and attribute != '_id':
      self._new_attributes_values[attribute] = \
          copy.deepcopy(self._attribute_values[attribute])
      self._new_attributes_values[attribute].__set__(self, value)
    else:
      self.__dict__[attribute] = value

  def __getattribute__(self, name):
    try:
      if name in object.__getattribute__(self, '_new_attributes_values'):
        return object.__getattribute__(self,
            '_new_attributes_values')[name].value
      if name in object.__getattribute__(self, '_attribute_values'):
        return object.__getattribute__(self,
            '_attribute_values')[name].value
    except AttributeError:
      pass
    return object.__getattribute__(self, name)

  @property
  def document_attributes(self):
    return self._attribute_values.keys()

