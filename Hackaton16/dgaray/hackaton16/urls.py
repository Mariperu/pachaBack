from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework import routers

from artistas.views import ArtistViewSet
from canciones.views import SongViewSet
from usuarios.views import UserViewSet
from playlist.views import PlaylistViewSet
from albunes.views import AlbumViewSet


router = routers.DefaultRouter()

router.register(r'artistas', ArtistViewSet, basename='artistas' )
router.register(r'canciones', SongViewSet, basename='canciones' )
router.register(r'usuarios', UserViewSet, basename='usuarios' )
router.register(r'playlist', PlaylistViewSet, basename='playlist' )
router.register(r'album', AlbumViewSet, basename='album' )

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
]
