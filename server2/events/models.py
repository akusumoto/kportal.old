"""
Event Models
"""

from django.db import models

class Event(models.Model):
    """
    Event Model
    """
    date = models.DateField()
    place = models.CharField(max_length=1024) 
    station = models.CharField(max_length=1024)
    subject = models.CharField(max_length=1024)
    detail = models.TextField(blank=True)
    owner = models.ForeignKey("User", on_delete=models.SET_NULL, blank=True)

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
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    answer = models.ForeignKey("EventAnswer", on_delete=models.SET_NULL)
    comment = models.CharField(max_length=1024, blank=True)


