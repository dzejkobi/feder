# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-17 13:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0004_case_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='case',
            options={'get_latest_by': 'created', 'ordering': ['created'], 'verbose_name': 'Case', 'verbose_name_plural': 'Case'},
        ),
    ]
