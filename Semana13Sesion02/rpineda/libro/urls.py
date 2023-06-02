from django.urls import path
from .views import crear_autor

app_name='libro'
urlpatterns = [
    path('', crear_autor, name='index'),
    
]