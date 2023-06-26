from django.urls import path
from .views import Home

app_name='cliente'
urlpatterns = [
    path('', Home, name='index'),
    path('')
    
]