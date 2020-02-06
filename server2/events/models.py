"""
Event Models
"""

from django.db import models
from member.models import User

class Event(models.Model):
    """
    Event Model
    """
    date = models.DateField()
    subject = models.CharField(max_length=1024)
    place = models.CharField(max_length=1024, null=True) 
    station = models.CharField(max_length=1024, null=True)
    detail = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __repr__(self):
        return "{}".format(self.subject)

    __str__ = __repr__

class EventAnswer(models.Model):
    """
    EventAnswer Model
    """
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
    value = models.CharField(max_length=100)

class EventUser(models.Model):
    """
    EventUser Model
    """
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey("EventAnswer", on_delete=models.SET_NULL, null=True)
    comment = models.CharField(max_length=1024, null=True)

    class Meta:
        unique_together = (("event","user"))

