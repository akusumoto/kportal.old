"""
admin
"""

from django.contrib import admin
from .models import User as us

@admin.register(us)
class User(admin.ModelAdmin):
    """
    User ModelAdmin
    """

