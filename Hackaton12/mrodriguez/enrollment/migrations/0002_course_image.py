# Generated by Django 4.2.1 on 2023-05-27 23:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("enrollment", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="image",
            field=models.ImageField(default=0, upload_to="uploads/"),
            preserve_default=False,
        ),
    ]