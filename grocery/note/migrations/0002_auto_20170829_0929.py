# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 01:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='\u6807\u7b7e\u540d\u79f0')),
                ('is_self', models.BooleanField(default=False, verbose_name='\u81ea\u5b9a\u4e49\u6807\u7b7e')),
            ],
        ),
        migrations.RemoveField(
            model_name='content',
            name='category',
        ),
        migrations.AddField(
            model_name='content',
            name='desc',
            field=models.TextField(blank=True, null=True, verbose_name='\u7b80\u4ecb'),
        ),
        migrations.AlterField(
            model_name='content',
            name='keywords',
            field=models.CharField(blank=True, db_index=True, max_length=36, null=True, verbose_name='\u5173\u952e\u8bcd'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='content',
            name='tags',
            field=models.ManyToManyField(to='note.Tags', verbose_name='\u6807\u7b7e'),
        ),
    ]
