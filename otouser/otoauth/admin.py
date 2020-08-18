from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import ExtraUserData

class ExtraInline(admin.StackedInline):
    model = ExtraUserData

class MyUserAdmin(UserAdmin):
    def __init__(self, *args, **kwargs):
        super(UserAdmin,self).__init__(*args, **kwargs)
        UserAdmin.list_display = list(UserAdmin.list_display) + ['date_joined',]

    inlines = [
        ExtraInline,
    ]

admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
