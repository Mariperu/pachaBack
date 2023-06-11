"""
URL configuration for pharmacy project.

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
from django.views.generic import RedirectView

from sale import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("sale/", include("sale.urls")),
    path("logout/", RedirectView.as_view(url="/admin/logout")),
    path("login/", views.signin, name="login"),
    path("", views.IndexView.as_view(), name="index"),
    path(
        "create_customer/",
        views.CreateCustomerView.as_view(),
        name="create_customer",
    ),
    path(
        "product_list/",
        views.ProductListView.as_view(),
        name="product_list",
    ),
]
