# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 11:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_merge_20161125_1122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogger',
            name='birthdate',
        ),
    ]
