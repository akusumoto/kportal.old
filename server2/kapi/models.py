from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

import hashlib

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

class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
        return "{} ({})".format(self.user.username, self.nickname)

    __str__ = __repr__

class AccessToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=40)
    access_datetime = models.DateTimeField()

    @staticmethod
    def create(user: User):
        if AccessToken.objects.filter(user=user).exists():
            AccessToekn.objects.get(user=user).delete()

        dt = timezone.now()
        str = "THanKS" + user.username + "K!" + user.password + dt.strftime("%F%m%d%H%M%S%f")
        hash = hashlib.sha1(str.encode('utf-8')).hexdigest()

        token = AccessToken.objects.create(
                user = user,
                token = hash,
                access_datetime = dt)

        return token

    def __repr__(self):
        dt = timezone.localtime(self.access_datetime).strftime("%Y/%m/%d %H:%M:%S") 
        return "{} ({}) - {}".forma(self.user.username, dt, self.token)

    __str__ = __repr__
