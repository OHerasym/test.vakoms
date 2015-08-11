# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20150809_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_active',
            field=models.BooleanField(default=datetime.datetime(2015, 8, 10, 9, 28, 4, 757900, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2015, 8, 10)),
        ),
    ]
