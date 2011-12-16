from django.db import models

from expresso_object.models import ExpressoObject

class Activity(ExpressoObject):
  num_locations = models.IntegerField()
