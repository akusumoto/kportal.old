from django.contrib import admin
from .models import UserInfo as ui, Type as tp, Part as pt, UserStatus as st, AccessToken as at

@admin.register(ui)
class UserInfo(admin.ModelAdmin):
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

@admin.register(at)
class AccessToken(admin.ModelAdmin):
    pass
