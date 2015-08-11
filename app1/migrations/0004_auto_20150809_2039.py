# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20150809_1739'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name_plural': 'User profiles'},
        ),
        migrations.AddField(
            model_name='userprofile',
            name='activation_key',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2015, 8, 9)),
        ),
    ]
