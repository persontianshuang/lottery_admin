# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-15 00:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_model', '0007_auto_20171114_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(choices=[(0, '普通用户'), (1, '省'), (2, '市'), (3, '管理员'), (4, '一级代理'), (5, '二级代理')], default=0),
        ),
    ]
