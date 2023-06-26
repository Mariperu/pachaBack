# Generated by Django 4.2.2 on 2023-06-23 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("albunes", "0002_alter_album_song"),
        ("artistas", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="artist",
            name="album",
            field=models.ForeignKey(
                default="",
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="albunes.album",
            ),
        ),
    ]
