from django.urls import include,path
from rest_framework import routers
from .views import TipoViewSet,MarcaViewSet,AutoViewSet,TipoGetView,TipoPostView,TipoPutView,TipoDeleteView,AutoFilterView,AutoFilterViewByYear
router = routers.DefaultRouter()
router.register('api/tipo',TipoViewSet,'tipos')
router.register('api/marca',MarcaViewSet,'marcas')
router.register('api/auto',AutoViewSet,'autos')
urlpatterns=[
    path('',include(router.urls)),
    #filtro de auto
    path('api/auto/get/<str:filter_value>/<str:value>',AutoFilterView,name='auto_get_filter_view'),
    path('api/auto/get/<int:year>',AutoFilterViewByYear,name='auto_get_filter_view_by_year'),

    path('api/tipo/get',TipoGetView,name='tipo_get_view'), #para realizar una peticion GET según el atributo del auto. get-> all_tipos
    path('api/tipo/post',TipoPostView,name='tipo_post_view'), #para realizar una peticion POST según el atributo del auto. post-> att tipo
    path('api/tipo/put',TipoPutView,name='tipo_put_view'), #para realizar una peticion PUT según el atributo del auto. put-> att tipo
    path('api/tipo/delete',TipoDeleteView,name='tipo_delete_view') #para realizar una peticion PUT según el atributo del auto. put-> att tipo
]
