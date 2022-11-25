from django.db import models

class Categories(models.Model):
    name: models.TextField = models.TextField(max_length=255)
    image: models.ImageField = models.ImageField(blank=True)