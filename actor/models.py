from django.db import models

from expresso_object.models import ExpressoObject

class Actor(ExpressoObject):
  email = models.EmailField()

class Human(Actor):
  access_token = models.CharField(max_length=256)
