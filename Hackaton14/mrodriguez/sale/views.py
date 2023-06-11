from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

from .forms import (
    CreateCustomerForm,
    CreateItemForm,
    CreateInvoiceForm,
    UpdateInvoiceForm,
)
from .models import Product, Invoice, Item


class IndexView(generic.TemplateView):
    template_name = "index.html"


def signin(request):
    if request.method == "GET":
        return render(request, "login.html", {"form": AuthenticationForm})
    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(
                request,
                "login.html",
                {
                    "form": AuthenticationForm,
                    "error": "Username or password is incorrect.",
                },
            )
        else:
            login(request, user)
            return redirect("index")


class ProductListView(ListView):
    model = Product


class CreateCustomerView(CreateView):
    form_class = CreateCustomerForm
    template_name = "customer_form.html"
    success_url = "/"


class CreateItemView(CreateView):
    form_class = CreateItemForm
    template_name = "sale/item_form.html"
    success_url = "/product_list"


class CreateInvoiceView(CreateView):
    form_class = CreateInvoiceForm
    template_name = "sale/invoice_form.html"
    success_url = "/product_list"


class InvoiceListView(ListView):
    model = Invoice


def invoice_detail(request, id):
    if request.method == "GET":
        invoice = get_object_or_404(Invoice, pk=id)
        items = Item.objects.filter(invoice=id)
        form = UpdateInvoiceForm(instance=invoice)
        return render(
            request,
            "sale/invoice_detail.html",
            {"invoice": invoice, "items": items, "form": UpdateInvoiceForm},
        )
    else:
        try:
            invoice = get_object_or_404(Invoice, pk=id)
            form = UpdateInvoiceForm(request.POST, instance=invoice)
            form.save()
            return redirect("index")
        except ValueError:
            return render(
                request,
                "invoice_detail.html",
                {"invoice": invoice, "form": form, "error": "Ocurrió un error."},
            )
