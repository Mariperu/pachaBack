from django.db import models
from ckeditor.fields import RichTextField


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    year = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    description = RichTextField()
    image_url = models.CharField(max_length=500, default="", null=True)

    def __str__(self):
        return self.model
