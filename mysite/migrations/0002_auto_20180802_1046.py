# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-02 02:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TradingAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=40, verbose_name='账户')),
                ('port', models.IntegerField(verbose_name='端口')),
                ('license', models.CharField(max_length=30, verbose_name='许可证')),
                ('appid', models.CharField(max_length=20, verbose_name='ApppID')),
                ('userid', models.CharField(max_length=20, verbose_name='用户ID')),
            ],
        ),
        migrations.CreateModel(
            name='WorkLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateField(auto_now_add=True, verbose_name='填写日期')),
                ('date', models.DateField(verbose_name='所属工作日期')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('body', models.TextField(max_length=300, verbose_name='详细内容')),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.AddField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=36, null=True, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='users',
            name='enabled',
            field=models.IntegerField(choices=[[0, '未启用'], [1, '启用']], default=0, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(max_length=20, unique=True, verbose_name='用户名'),
        ),
        migrations.AddField(
            model_name='worklog',
            name='belonged',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Users'),
        ),
        migrations.AddField(
            model_name='tradingaccount',
            name='belonged',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Users'),
        ),
    ]
