# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20150809_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(max_length=30),
            #field=models.CharField(default=datetime.datetime(2015, 8, 9, 14, 39, 28, 175148, tzinfo=utc), max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            #field=models.CharField(default=datetime.datetime(2015, 8, 9, 14, 39, 38, 780218, tzinfo=utc), max_length=30),
            field=models.CharField(max_length=30),
            preserve_default=False,
        ),
    ]
