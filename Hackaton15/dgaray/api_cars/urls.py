from django.urls import include, path
from rest_framework import routers
from .api import MarcaViewSet, AutoViewSet, TipoViewSet, TipoDeleteView, TipoUpdateView, TipoGetView, TipoPostView, TipoGetFilterView

router = routers.DefaultRouter()

router.register('api/marcas', MarcaViewSet, 'marcas' )

router.register('api/tipos', TipoViewSet, 'tipos' )

router.register('api/autos', AutoViewSet, 'autos' )


urlpatterns = [
    path('', include(router.urls)),
    
    path('api/auto/marca/<int:marca>/', TipoGetFilterView, name="tipo-getfilter-view"), 

    path('api/tipo/get/', TipoGetView, name="tipo-get-view"),
    path('api/tipo/post/', TipoPostView, name="tipo-post-view"),
    path('api/tipo/<int:id>/put/', TipoUpdateView, name="tipo-update-view"),
    path('api/tipo/<int:id>/delete/', TipoDeleteView, name="tipo-delete-view"),
]