# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20150810_2111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='category',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='publish',
        ),
        migrations.AddField(
            model_name='blog',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
