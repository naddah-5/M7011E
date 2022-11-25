from django.db import models

class Products(models.Model):
    ID: models.BigAutoField = models.BigAutoField(primary_key=True)
    Name: models.TextField = models.TextField(max_length=255)
    Description: models.TextField = models.TextField(blank=True, null=True)
    Price: models.DecimalField = models.DecimalField(decimal_places=2, max_digits=14)
    Stock: models.IntegerField = models.IntegerField()
    Thumbnail: models.ImageField = models.ImageField(blank=True, null=True)