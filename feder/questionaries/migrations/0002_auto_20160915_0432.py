# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-15 04:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [("questionaries", "0001_initial")]

    operations = [
        migrations.RenameField(
            model_name="question", old_name="blob", new_name="definition"
        )
    ]
