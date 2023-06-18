# Generated by Django 4.2.2 on 2023-06-10 17:14

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("farmacia", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(default="", max_length=150)),
                ("lastname", models.CharField(default="", max_length=150)),
                (
                    "dni",
                    models.IntegerField(
                        default="",
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                ("img_path", models.CharField(default="", max_length=1000)),
                (
                    "point",
                    models.IntegerField(
                        default=0,
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                ("created", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(default="", max_length=150)),
                ("price", models.DecimalField(decimal_places=2, max_digits=8)),
                (
                    "stock",
                    models.IntegerField(
                        default=20,
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                ("img_path", models.CharField(default="", max_length=1000)),
                ("created", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name="Sale",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("total", models.DecimalField(decimal_places=2, max_digits=8)),
                (
                    "quantity",
                    models.IntegerField(
                        default=0,
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                ("created", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "id_client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="farmacia.client",
                    ),
                ),
                (
                    "id_product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="farmacia.product",
                    ),
                ),
            ],
        ),
    ]
