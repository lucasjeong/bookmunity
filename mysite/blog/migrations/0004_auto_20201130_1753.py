# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2020-11-30 08:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201130_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 30, 8, 53, 38, 376476, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 30, 8, 53, 38, 376476, tzinfo=utc)),
        ),
    ]