# Generated by Django 1.10 on 2016-09-07 15:56

import django.utils.timezone
import model_utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("institutions", "0003_auto_20160822_1724")]

    operations = [
        migrations.RemoveField(model_name="institution", name="address"),
        migrations.AddField(
            model_name="email",
            name="created",
            field=model_utils.fields.AutoCreatedField(
                default=django.utils.timezone.now,
                editable=False,
                verbose_name="created",
            ),
        ),
        migrations.AddField(
            model_name="email",
            name="modified",
            field=model_utils.fields.AutoLastModifiedField(
                default=django.utils.timezone.now,
                editable=False,
                verbose_name="modified",
            ),
        ),
        migrations.AddField(
            model_name="email",
            name="priority",
            field=models.SmallIntegerField(default=0, verbose_name="Priority of usage"),
        ),
    ]
