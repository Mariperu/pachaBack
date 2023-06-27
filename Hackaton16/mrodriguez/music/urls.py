"""
URL configuration for music project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from albums.views import AlbumViewSet
from songs.views import SongViewSet
from singers.views import SingerViewSet
from playlists.views import PlaylistViewSet
from users.views import UserViewSet


router = routers.DefaultRouter()
router.register("api/albums", AlbumViewSet, basename="albums")
router.register("api/songs", SongViewSet, basename="songs")
router.register("api/singers", SingerViewSet, basename="singers")
router.register("api/playlists", PlaylistViewSet, basename="playlists")
router.register("api/users", UserViewSet, basename="users")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("", include(("albums.urls", "albums"), namespace="albums")),
    path("", include(("songs.urls", "songs"), namespace="songs")),
    path("", include(("singers.urls", "singers"), namespace="singers")),
    path("", include(("playlists.urls", "playlists"), namespace="playlists")),
    path("", include(("users.urls", "users"), namespace="users")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
