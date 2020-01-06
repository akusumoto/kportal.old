from django.db import models

# Create your models here.

class UserStatus(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=10)

    def __repr__(self):
        return "{}".format(self.name)

    __str__ = __repr__


class Part(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=10)

    def __repr__(self):
        return "{}".format(self.name)

    __str__ = __repr__

class Type(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=10)

    def __repr__(self):
        return "{}".format(self.name)

    __str__ = __repr__

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=256)
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=100)
    status = models.ForeignKey("UserStatus", on_delete=models.SET_NULL, null=True)
    home_address = models.CharField(max_length=256, null=True)
    work_address = models.CharField(max_length=256, null=True)
    part = models.ForeignKey("Part", on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey("Type", on_delete=models.SET_NULL, null=True)
    emergency_phone = models.CharField(max_length=15, null=True)
    note = models.TextField(null=True)

    def __repr__(self):
        return "{} ({})".format(self.username, self.nickname)

    __str__ = __repr__
