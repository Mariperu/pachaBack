
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crud_escuela', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=200)),
                ('max_estudiante', models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Ciclo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=200)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('creado_por', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=200)),
                ('descripcion', models.CharField(max_length=200, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('ciclo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='crud_escuela.ciclo')),
                ('creado_por', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=200)),
                ('dni', models.BigIntegerField(default=1111111)),
                ('edad', models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('email', models.CharField(default='', max_length=200)),
                ('descripcion', models.CharField(max_length=200, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('creado_por', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='crud_escuela.curso')),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='crud_escuela.alumno')),
                ('aula', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='crud_escuela.aula')),
                ('ciclo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='crud_escuela.ciclo')),
                ('creado_por', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='crud_escuela.curso')),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='crud_escuela.profesor')),
            ],
        ),
        migrations.AddField(
            model_name='aula',
            name='ciclo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='crud_escuela.ciclo'),
        ),
    ]
