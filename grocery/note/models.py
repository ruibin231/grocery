# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Tags(models.Model):
    name = models.CharField(max_length=16, verbose_name=u'标签名称')
    is_self = models.BooleanField(default=False, verbose_name=u'自定义标签')

    class Mate:
        default_relate_name = u'类型'

    def __unicode__(self):
        return self.name


class Content(models.Model):
    author = models.ForeignKey(User, verbose_name=u'作者')
    tags = models.ManyToManyField(Tags, verbose_name=u'标签')
    title = models.CharField(max_length=72, verbose_name=u'标题',
                             db_index=True)
    context = models.TextField(verbose_name=u'内容')
    keywords = models.CharField(max_length=36, verbose_name=u'关键词',
                                db_index=True, blank=True, null=True)
    desc = models.TextField(verbose_name=u'简介', blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name=u'创建时间')
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name=u'更新时间')
    click_rate = models.IntegerField(default=0, verbose_name='点击量')

    class Mate:
        ordering = ('-update_time', )
        verbose_name = verbose_name_plural = u'笔记／文章'

    def __unicode__(self):
        return self.title
