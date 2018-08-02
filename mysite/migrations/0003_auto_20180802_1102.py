# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-02 03:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20180802_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='jurisdiction',
            field=models.IntegerField(choices=[[1, '普通用户'], [2, '内部用户'], [3, '管理员']], default=1, verbose_name='用户权限'),
        ),
    ]
