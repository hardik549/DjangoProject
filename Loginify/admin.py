from django.contrib import admin
from . import models

admin.site.register(models.UserDetails)
# @admin.register(models.UserDetails)
# class UserDetailsAdmin(admin.ModelAdmin):
#     list_display= ('username', 'email', 'password')
