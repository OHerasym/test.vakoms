# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups', blank=True, related_name='user_set', to='auth.Group'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_superuser',
            field=models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', help_text='Specific permissions for this user.', verbose_name='user permissions', blank=True, related_name='user_set', to='auth.Permission'),
        ),
    ]
