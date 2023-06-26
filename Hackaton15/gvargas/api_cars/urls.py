from django.urls import include, path
from rest_framework import routers
from .api import TipoViewSet, MarcaViewSet, AutoViewSet, TipoGetView, TipoPostView, TipoPutView, TipoDeleteView, AutoFilterView, TipoGetFilterView, AutoGetView, AutoPostView, AutoPutView, AutoDeleteView, MarcaGetView, MarcaPostView, MarcaPutView, MarcaDeleteView

router = routers.DefaultRouter()

router.register('api/tipo', TipoViewSet, 'tipos')
router.register('api/marca', MarcaViewSet, 'marcas')
router.register('api/auto', AutoViewSet, 'autos')

urlpatter = [
    path('', include(router.urls)),
    
    path('api/auto/get/<str:filter_value>/<int:tipo>', AutoFilterView, name='auto_get_filter_view'),
    path('api/auto/marca/<int:marca>/', TipoGetFilterView, name="tipo-getfilter-view"), 

    path('api/tipo/get', TipoGetView, name='tipo_get_view'),
    path('api/tipo/post', TipoPostView, name='tipo_post_view'),
    path('api/tipo/<int:id>/put', TipoPutView, name='tipo_put_view'),
    path('api/tipo/<int:id>/delete', TipoDeleteView, name='tipo_delete_view'),
    path('api/auto/get', AutoGetView, name='auto_get_view'),
    path('api/auto/post', AutoPostView, name='auto_post_view'),
    path('api/auto/<int:id>/put', AutoPutView, name='auto_put_view'),
    path('api/auto/<int:id>/delete', AutoDeleteView, name='auto_delete_view'),
    path('api/marca/get', MarcaGetView, name='marca_get_view'),
    path('api/marca/post', MarcaPostView, name='marca_post_view'),
    path('api/marca/<int:id>/put', MarcaPutView, name='marca_put_view'),
    path('api/marca/<int:id>/delete', MarcaDeleteView, name='marca_delete_view'),
]
