import django
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("cases", "0001_initial"), ("institutions", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="case",
            name="institution",
            field=models.ForeignKey(
                verbose_name="Institution",
                on_delete=django.db.models.deletion.CASCADE,
                to="institutions.Institution",
            ),
        )
    ]
