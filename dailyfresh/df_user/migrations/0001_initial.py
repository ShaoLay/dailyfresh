# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-06-17 06:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20, verbose_name='用户名')),
                ('password', models.CharField(max_length=40, verbose_name='密码')),
                ('email', models.CharField(max_length=20, verbose_name='邮箱')),
                ('phone', models.CharField(max_length=11, verbose_name='电话')),
                ('recv_name', models.CharField(max_length=20, verbose_name='收件人')),
                ('you_bian', models.CharField(max_length=6, verbose_name='邮政编码')),
                ('address', models.CharField(max_length=100, verbose_name='收货地址')),
            ],
        ),
    ]
