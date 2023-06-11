from django.urls import path

from . import views


urlpatterns = [
    path("create_item/", views.CreateItemView.as_view(), name="create_item"),
    path("invoice_list/", views.InvoiceListView.as_view(), name="invoice_list"),
    path("invoice_detail/<int:id>/", views.invoice_detail, name="invoice_detail"),
    path(
        "create_invoice/",
        views.CreateInvoiceView.as_view(),
        name="create_invoice",
    ),
]
