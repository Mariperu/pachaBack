from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='description',
        ),
    ]
