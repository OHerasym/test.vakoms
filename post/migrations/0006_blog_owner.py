# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20150810_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='owner',
            field=models.CharField(max_length=200, default=datetime.datetime(2015, 8, 10, 20, 19, 48, 272043, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
