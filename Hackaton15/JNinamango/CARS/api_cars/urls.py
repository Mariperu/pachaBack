from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('api/tipo/', TipoViewSet, 'tipos')
router.register('api/marca/', MarcaViewSet, 'marcas')
router.register('api/auto/', AutoViewSet, 'autos')
        

urlpatterns = [
    path('', include(router.urls)),
    ###
    path('api/auto/get/<int:filter_value><int:id>', AutoFilterView, name='auto_get_filter_view'),


    path('api/tipo/get', TipoGetView, name='tipo_get_view'),
    path('api/tipo/post', TipoPostView, name='tipo_post_view'),
    path('api/tipo/put/<int:id>', TipoPutView, name='tipo_put_view'),
    path('api/tipo/delete/<int:id>', TipoDeleteView, name='tipo_delete_view'),

]

