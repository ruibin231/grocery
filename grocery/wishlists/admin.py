# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from grocery.wishlists.models import Wishlist, Price
# Register your models here.

class WishlistAdmin(admin.ModelAdmin):
    list_display = ('assets', 'author', 'time')
    search_fields = ('assets', 'author', 'title')

class PriceAdmin(admin.ModelAdmin):
	list_display = ('author', 'assets', 'price', 'time')
	search_fields = ('assets', 'author', 'price')


admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(Price, PriceAdmin)