# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name_plural': 'Blog Enteries', 'ordering': ['-created'], 'verbose_name': 'Blog Entry'},
        ),
        migrations.RemoveField(
            model_name='blog',
            name='posted',
        ),
        migrations.AddField(
            model_name='blog',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 8, 10, 15, 58, 47, 749728, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='modified',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 8, 10, 15, 58, 54, 264101, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='publish',
            field=models.BooleanField(default=True),
        ),
    ]
