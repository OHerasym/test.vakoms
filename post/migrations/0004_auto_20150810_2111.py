# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20150810_2017'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name_plural': 'Blog Enteries', 'verbose_name': 'Blog Entry', 'ordering': ['-pub_date']},
        ),
        migrations.RemoveField(
            model_name='blog',
            name='created',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='modified',
        ),
        migrations.AddField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 10, 18, 11, 55, 630947, tzinfo=utc), verbose_name='date published'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
