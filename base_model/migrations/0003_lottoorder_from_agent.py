# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-21 11:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_model', '0002_auto_20171117_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='lottoorder',
            name='from_agent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_model.UserRecommend'),
        ),
    ]
