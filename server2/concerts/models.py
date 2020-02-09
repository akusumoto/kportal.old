from django.db import models

from member.models import User
from events.models import Event

class Concert(models.Model):
    """
    Concert Model
    """

    STATUS = [
        ('active', '進行中'),
        ('finished', '終了')
    ]

    title = models.CharField(max_length=1024)
    date = models.DateField(null=True)
    open_time = models.TimeField(null=True)
    start_time = models.TimeField(null=True)
    place = models.CharField(max_length=1024, null=True)
    detail = models.TextField(null=True)
    status = models.CharField(max_length=8, choices=STATUS, default='active')

    events = models.ManyToManyField(Event, blank=True)

    def __repr__(self):
        return "{}".format(self.title)

    __str__ = __repr__