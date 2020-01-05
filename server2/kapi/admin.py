from django.contrib import admin
from .models import User as KUser, Type as KType, Part as KPart

# Register your models here.
@admin.register(KUser)
class User(admin.ModelAdmin):
    pass

@admin.register(KPart)
class Part(admin.ModelAdmin):
    pass

@admin.register(KType)
class Type(admin.ModelAdmin):
    pass
