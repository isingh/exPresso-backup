from django.db import models

class ExpressoObject(models.Model):
  """Abstract base class for expresso objects.
  This class should not be instantiated directly and will not have a
  table associated with it in the database.
  """
  name = models.CharField(max_length=512)

  class Meta:
    abstract = True
