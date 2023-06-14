from django.contrib import admin
from .models import User, Product, Sale, Client
# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(Client)
