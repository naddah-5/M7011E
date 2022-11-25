from django.db import models
from .categories import Categories

class Subcategories(models.Model):
    category: models.ForeignKey = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name: models.TextField = models.TextField(max_length=255)
    image: models.ImageField = models.ImageField(blank=True)