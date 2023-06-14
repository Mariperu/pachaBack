from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    ROLES = (
        ('AD', 'Administrador'),
        ('PR', 'Profesor'),
        ('AL', 'Alumno'),
    )
    role = models.CharField(choices=ROLES, max_length=2)
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_name="core_user_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="core_user_set",
        related_query_name="user",
    )

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    profesor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cursos')

class Asistencia(models.Model):
    alumno = models.ForeignKey(User, on_delete=models.CASCADE, related_name='asistencias')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='asistencias')
    fecha = models.DateField()
    presente = models.BooleanField()

class Nota(models.Model):
    alumno = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notas')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='notas')
    fecha = models.DateField()
    nota = models.FloatField()
