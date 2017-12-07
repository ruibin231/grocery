# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from grocery.properties.models import Assets


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.CharField(max_length=256, verbose_name=u'头像',
                              blank=True, null=True)
    mobile = models.CharField(max_length=15,verbose_name=u'手机号')
    nick_name = models.CharField(max_length=32, unique=True,
                                 verbose_name=u'昵称')
    lat = models.FloatField(blank=True, null=True, verbose_name=u'经度')
    lon = models.FloatField(blank=True, null=True, verbose_name=u'纬度')
    detail_address = models.CharField(max_length=128, verbose_name=u'详细地址',
                                      blank=True, null=True)
    open_id = models.CharField(max_length=32)

    class Meta:
        verbose_name = verbose_name_plural = u'用户信息'

    def __unicode__(self):
        return self.nick_name


class BrowseHistory(models.Model):
    assets = models.ForeignKey(Assets, verbose_name=u'访问的资产')
    author = models.ForeignKey(User, verbose_name=u'用户')
    title = models.CharField(max_length=32, verbose_name=u'资产标题')
    time = models.DateTimeField(auto_now_add=True, verbose_name=u'访问时间')

    class Meta:
        verbose_name = verbose_name_plural = u'用户访问历史'

    def __unicode__(self):
        return self.title
