"""
models
"""

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, _user_has_perm
)
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, request_data, **_kwargs):
        now = timezone.now()
        if not request_data['username']:
            raise ValueError('Users must have an username.')

        user = self.model(
            username=request_data['username'],
            email=self.normalize_email(request_data['email']),
            is_active=True,
            last_login=now,
            date_joined=now
        )

        user.set_password(request_data['password'])
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **_extra_fields):
        request_data = {
            'username': username,
            'email': email,
            'password': password
        }
        user = self.create_user(request_data)
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    '''User Model'''

    username = models.CharField(max_length=100, unique=True)
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
    is_active   = models.BooleanField(default=True)
    is_staff    = models.BooleanField(default=False)
    is_admin    = models.BooleanField(default=False)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', 'name', 'nickname']

    def user_has_perm(self, user, perm, obj):
        return _user_has_perm(user, perm, obj)

    def has_perm(self, perm, obj=None):
        return _user_has_perm(self, perm, obj=obj)

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin

    def __repr__(self):
        return "[{}] {} ({})".format(self.id, self.username, self.nickname)

    __str__ = __repr__

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

