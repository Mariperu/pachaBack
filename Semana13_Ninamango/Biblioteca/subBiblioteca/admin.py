from django.contrib import admin
from .models import Autor, Book, Nacionalidad, Sexo, DocumentoIdentidad, UserApp, RegistroLibro
# Register your models here.

admin.site.register(Autor)
admin.site.register(Book)
admin.site.register(Nacionalidad)
admin.site.register(Sexo)
admin.site.register(DocumentoIdentidad)
admin.site.register(UserApp)
admin.site.register(RegistroLibro)
