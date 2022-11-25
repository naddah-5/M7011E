from django.db import models

class Products(models.Model):
    name: models.TextField = models.TextField(max_length=255)
    description: models.TextField = models.TextField(blank=True, null=True)
    price: models.DecimalField = models.DecimalField(decimal_places=2, max_digits=16)
    stock: models.IntegerField = models.IntegerField()
    thumbnail: models.ImageField = models.ImageField(blank=True, null=True)