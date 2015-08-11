# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20150809_2148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='activation_key',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='key_expires',
        ),
    ]
