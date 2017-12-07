# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from grocery.accounts.models import UserProfile, BrowseHistory
from grocery.properties.models import Assets
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('mobile', 'nick_name', 'open_id')
    search_fields = ('nick_name', 'user')
    # inlines = [AssetsImgline]

# class Assetsline(admin.TabularInline):
#     model = Assets


class BrowseHistoryAdmin(admin.ModelAdmin):
    list_display = ('assets', 'author', 'title', 'time')
    search_fields = ('title', 'time')
    # inlines = [Assetsline]


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(BrowseHistory, BrowseHistoryAdmin)