# Generated by Django 4.2.2 on 2023-06-16 22:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("extras", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="extra",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="extra_education",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
