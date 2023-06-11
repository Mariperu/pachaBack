from django.contrib import admin
from .models import Product, IdCardType, Cashier, Customer, Invoice, Item


# class ItemInline(admin.StackedInline):
#     model = Item
#     extra = 1


class InvoiceAdmin(admin.ModelAdmin):
    # inlines = [ItemInline]
    list_display = ("id", "date", "total")
    list_filter = ["date"]


class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "price", "stock")


class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "invoice", "product", "quantity")
    list_filter = ["invoice"]


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id_card_number", "fullname", "points")


admin.site.register(Product, ProductAdmin)
admin.site.register(IdCardType)
admin.site.register(Cashier)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Item, ItemAdmin)
