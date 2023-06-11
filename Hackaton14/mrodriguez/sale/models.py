from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.CharField(max_length=200)
    stock = models.IntegerField()

    def __str__(self):
        return str(self.name) + " - " + str(self.price)


class IdCardType(models.Model):
    id = models.AutoField(primary_key=True)
    id_card_type = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id_card_type)


class Cashier(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=200, null=False, default="")
    id_card_type = models.ForeignKey(IdCardType, on_delete=models.CASCADE, null=True)
    id_card_number = models.CharField(max_length=20)

    def __str__(self):
        return str(self.fullname)


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=200, null=False, default="")
    id_card_type = models.ForeignKey(IdCardType, on_delete=models.CASCADE, null=True)
    id_card_number = models.CharField(max_length=20)
    points = models.IntegerField(default=0)
    creation_date = models.DateField(default=timezone.now)

    def __str__(self):
        return str(self.id_card_number)


class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(default=timezone.now)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # subtotal = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    # igv = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    paid = models.BooleanField(default=False)
    cashier = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.id) + "-" + str(self.product.name)
