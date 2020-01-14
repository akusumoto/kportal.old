"""
models
"""

import hashlib
from django.db import models
from django.utils import timezone

class UserStatus(models.Model):
    """
    UserStatus Model
    """
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=10)

    def __repr__(self):
        return "{}".format(self.name)

    __str__ = __repr__


class Part(models.Model):
    """
    Part Model
    """
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=10)

    def __repr__(self):
        return "{}".format(self.name)

    __str__ = __repr__

class Type(models.Model):
    """
    Type Model
    """
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=10)

    def __repr__(self):
        return "{}".format(self.name)

    __str__ = __repr__

class User(models.Model):
    """
    User Model
    """

    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
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

class AccessToken(models.Model):
    """
    AccessTOken Model
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=40)
    access_datetime = models.DateTimeField()

    @staticmethod
    def create(user: User):
        """
        creat a access token
        """

        if AccessToken.objects.filter(user=user).exists():
            AccessToken.objects.get(user=user).delete()

        now = timezone.now()
        token_str = "THanKS" + user.username + "K!" + user.password + now.strftime("%F%m%d%H%M%S%f")
        token = hashlib.sha1(token_str.encode('utf-8')).hexdigest()

        access_token = AccessToken.objects.create(user=user, token=token, access_datetime=now)

        return access_token

    def __repr__(self):
        time = timezone.localtime(self.access_datetime).strftime("%Y/%m/%d %H:%M:%S")
        return "{} ({}) - {}".format(self.user.username, time, self.token)

    __str__ = __repr__
