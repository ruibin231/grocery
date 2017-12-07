# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from grocery.properties.models import Category, Assets, AssetsImg, Comment

# Register your models here.

class AssetsImgline(admin.TabularInline):
    model = AssetsImg

class AssetsAdmin(admin.ModelAdmin):
    list_display = ('title', 'bond_institution', 'contacts', 'guarantee', 'pub_time')
    search_fields = ('title',)
    inlines = [AssetsImgline]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ('name',)

# class AssetsImgAdmin(admin.ModelAdmin):
#     list_display = ('assets', 'id')
#     search_fields = ('assets',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'assets', 'content', 'c_time')
    search_fields = ('assets', 'author', 'c_time')


admin.site.register(Assets, AssetsAdmin)
admin.site.register(Category, CategoryAdmin)
# admin.site.register(AssetsImg, AssetsImgAdmin)
admin.site.register(Comment, CommentAdmin)