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
    """
    UserManager
    """
    def create_user(self, request_data, **_kwargs):
        #print(request_data)
        now = timezone.now()
        if not request_data['username']:
            raise ValueError('Users must have an username.')

        user = self.model(
            username=request_data['username'],
            email=self.normalize_email(request_data['email']),
            name=request_data['name'],
            nickname=request_data['nickname'],
            is_active=True,
            last_login=now,
            date_joined=now
        )

        user.set_password(request_data['password'])
        if 'part' in request_data:
            user.part = request_data['part']
        if 'type' in request_data:
            user.type = request_data['type']
        if 'status' in request_data:
            user.status = request_data['status']
        if 'home_address' in request_data:
            home_address = request_data['home_address']
        if 'work_address' in request_data:
            work_address = request_data['work_address']
        if 'emergency_phone' in request_data:
            emergency_phone = request_data['emergency_phone']
        if 'note' in request_data:
            note = request_data['note']

        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        request_data = {
            'username': username,
            'email': email,
            'password': password,
            'name': extra_fields['name'],
            'nickname': extra_fields['nickname'],
        }
        user = self.create_user(request_data)
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user

PART = [
    ('vn1', '1st Violin'),
    ('vn2', '2nd Violin'),
    ('va', 'Viola'),
    ('vc', 'Cello'),
    ('cb', 'Contrabass'),
    ('fl', 'Flute'),
    ('cl', 'Clarinet'),
    ('sax', 'Saxophone'),
    ('ob', 'Oboe'),
    ('fg', 'Fagotto'),
    ('tp', 'Trumpet'),
    ('tb', 'Trombone'),
    ('tu', 'Tuba'),
    ('gt', 'Guitar'),
    ('pf', 'Piano'),
    ('syn', 'Synchesizer'),
    ('bs', 'Electric Bass'),
    ('cho-sp', 'Chorus Soprano'),
    ('cho-al', 'Chorus Alto'),
    ('cho-tn', 'Chorus Tenor'),
    ('cho-bs', 'Chorus Bass'),
    ('cond', 'Conductor'),
    ('staff', 'Staff'),
]

TYPE = [
    ('adult', '社会人'),
    ('student', '学生'),
]

STATUS = [
    ('active', '在籍中'),
    ('rest', '休団中'),
    ('left', '退団'),
    ('ghost', '幽霊団員'),
]

class User(AbstractBaseUser):
    '''User Model'''

    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=256)
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=100)
    home_address = models.CharField(max_length=256, null=True)
    work_address = models.CharField(max_length=256, null=True)
    status = models.CharField(max_length=6, choices=STATUS, default='active')
    part = models.CharField(max_length=6, choices=PART, default='staff')
    type = models.CharField(max_length=7, choices=TYPE, default='adult')
    emergency_phone = models.CharField(max_length=15, null=True)
    note = models.TextField(null=True)
    is_active   = models.BooleanField(default=True)
    is_staff    = models.BooleanField(default=False)
    is_admin    = models.BooleanField(default=False)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', 'name', 'nickname', 'email']

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

