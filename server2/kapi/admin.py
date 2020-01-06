from django.contrib import admin
from .models import User as us, Type as tp, Part as pt, UserStatus as st

# Register your models here.
@admin.register(us)
class User(admin.ModelAdmin):
    pass

@admin.register(pt)
class Part(admin.ModelAdmin):
    pass

@admin.register(tp)
class Type(admin.ModelAdmin):
    pass

@admin.register(st)
class UserStatus(admin.ModelAdmin):
    pass
