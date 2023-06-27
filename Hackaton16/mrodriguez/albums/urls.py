from django.urls import include, path
from rest_framework import routers
from albums import views

router = routers.DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path(
        "api/albums/<int:id>/delete/", views.AlbumDeleteView, name="album_delete_view"
    ),
]
