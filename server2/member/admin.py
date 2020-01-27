"""
admin
"""

from django.contrib import admin
from .models import User as us, Type as tp, Part as pt, UserStatus as st

@admin.register(us)
class User(admin.ModelAdmin):
    """
    User ModelAdmin
    """

@admin.register(pt)
class Part(admin.ModelAdmin):
    """
    Part ModelAdmin
    """

@admin.register(tp)
class Type(admin.ModelAdmin):
    """
    Type ModelAdmin
    """

@admin.register(st)
class UserStatus(admin.ModelAdmin):
    """
    User ModelAdmin
    """
