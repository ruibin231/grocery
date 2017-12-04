# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from grocery.properties.models import Assets


class Wishlist(models.Model):
    assets = models.ForeignKey(Assets, verbose_name=u'资产')
    author = models.ForeignKey(User, verbose_name=u'用户')
    title = models.CharField(max_length=32, verbose_name=u'资产标题')
    time = models.DateTimeField(auto_now_add=True, verbose_name=u'收藏时间')

    class Mate:
        verbose_name = verbose_name_plural = u'收藏'

    def __unicode__(self):
        return self.title


class Price(models.Model):
    author = models.ForeignKey(User, verbose_name=u'出价人')
    assets = models.ForeignKey(Assets, verbose_name=u'报价资产')
    price = models.DecimalField(max_digits=15, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True, verbose_name=u'收藏时间')

    class Mate:
        verbose_name = verbose_name_plural = u'报价'

    def __unicode__(self):
        return self.assets.title

