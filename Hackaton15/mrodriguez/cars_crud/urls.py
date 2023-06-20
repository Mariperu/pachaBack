from django.urls import include, path
from rest_framework import routers
from cars_crud import views

router = routers.DefaultRouter()

router.register("api/brands", views.BrandViewSet, basename="brands")
router.register("api/types", views.TypeViewSet, basename="types")
router.register("api/cars", views.CarViewSet, basename="cars")


urlpatterns = [
    path("", include(router.urls)),
    # FILTER/SEARCH
    path(
        "api/car/brand/<int:brand>/",
        views.BrandGetFilterView,
        name="brand_getfilter_view",
    ),
    path(
        "api/car/model/<str:model>/",
        views.ModelGetFilterView,
        name="model_getfilter_view",
    ),
    # CRUD
    path("api/type/get/", views.TypeGetView, name="type_get_view"),
    path("api/type/post/", views.TypePostView, name="type_post_view"),
    path("api/type/<int:id>/put/", views.TypeUpdateView, name="type_update_view"),
    path("api/type/<int:id>/delete/", views.TypeDeleteView, name="type_delete_view"),
    path("api/brand/get/", views.BrandGetView, name="brand_get_view"),
    path("api/brand/post/", views.BrandPostView, name="brand_post_view"),
    path("api/brand/<int:id>/put/", views.BrandUpdateView, name="brand_update_view"),
    path("api/brand/<int:id>/delete/", views.BrandDeleteView, name="brand_delete_view"),
    path("api/car/get/", views.CarGetView, name="car_get_view"),
    path("api/car/<int:id>/delete/", views.CarDeleteView, name="car_delete_view"),
]
