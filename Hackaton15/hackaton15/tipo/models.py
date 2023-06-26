from django.db import models
from users.models import User

# django-ckeditor
from ckeditor.fields import RichTextField

class Tipo(models.Model):

    nombre = models.CharField(max_length=255)
    descripcion = RichTextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tipo')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} | {self.nombre}'
