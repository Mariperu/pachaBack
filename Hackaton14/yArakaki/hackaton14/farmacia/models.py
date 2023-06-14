from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.utils import timezone
import uuid
# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_seller = models.BooleanField('Is seller', default=False)

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, null=False, default='')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField(null=True, default=20, validators=[MinValueValidator(0)])
    img_path = models.CharField(max_length=1000, null=False, default='')
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
class Client(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, null=False, default='')
    lastname = models.CharField(max_length=150, null=False, default='')
    dni = models.IntegerField(null=False, default='', validators=[MinValueValidator(0)])
    img_path = models.CharField(max_length=1000, null=False, default='')
    point = models.IntegerField(null=True, default=0, validators=[MinValueValidator(0)])
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Sale(models.Model):
    id_client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    id_product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(null=True, default=0, validators=[MinValueValidator(0)])
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.created)
