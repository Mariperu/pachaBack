from django.contrib import admin

from .models import Question, Choice
# Register your models here.
# admin.site.register(Question)
# admin.site.register(Choice)

# PERSONALIZANDO administrador


# class QuestionAdmin(admin.ModelAdmin):  # Agregando fecha de publicación de Questions
#     fields = ["pub_date", "question_text"]


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # dividir el formulario en grupos de campos:
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    # Añadiendo choices dentro de question
    inlines = [ChoiceInline]

    # Añadiendo campos a mostrar en lista de questions:
    list_display = ["question_text", "pub_date", "was_published_recently"]

    # Anadiendo filtro
    list_filter = ["pub_date"]

    # Añadiendo buscador
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice) #CUANDO VA ANIDADO EN QUESTION (inlines), YA NO VA ESTA LINEA
# Dentro de question se agrega directamente las opciones
