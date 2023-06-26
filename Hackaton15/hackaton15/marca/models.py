from django.db import models
from users.models import User

# django-ckeditor
from ckeditor.fields import RichTextField

class Marca(models.Model):

    nombre = models.CharField(max_length=255)
    descripcion = RichTextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='marca')

    def __str__(self):
        """Return company and first_name and last_name."""
        return f'{self.user.first_name} {self.user.last_name} | {self.nombre}'
