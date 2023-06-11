from django import forms
from .models import Customer, Item, Invoice


class CreateCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ("fullname", "id_card_type", "id_card_number")
        labels = {
            "fullname": "Nombre",
            "id_card_type": "Tipo de documento",
            "id_card_number": "Nro. de documento",
        }


class CreateItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("product", "invoice", "quantity")
        labels = {
            "product": "Producto",
            "invoice": "ID Pedido",
            "quantity": "Cantidad",
        }


class CreateInvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ("date", "customer", "cashier")
        labels = {"date": "fecha creación", "customer": "Cliente", "cashier": "Cajero"}


class UpdateInvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ("total", "paid", "cashier")
        labels = {
            "total": "Total",
            "paid": "Pagado",
            "cashier": "Cajero",
        }
