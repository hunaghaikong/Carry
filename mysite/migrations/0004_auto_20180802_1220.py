# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-02 04:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20180802_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(blank=True, max_length=36, null=True, verbose_name='邮箱'),
        ),
    ]
