# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-29 00:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobboard', '0005_operation_tasklist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='job',
        ),
    ]
