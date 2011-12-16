from django.db import models

from expresso_object.models import ExpressoObject

class Agent(ExpressoObject):
  class Meta:
    abstract = True

class Weather(Agent):
  temperature = models.IntegerField()

class Emotion(Agent):
  description = models.TextField()
