# Generated by Django 4.2.2 on 2023-06-27 06:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("albums", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="album",
            old_name="song",
            new_name="song_id",
        ),
    ]
