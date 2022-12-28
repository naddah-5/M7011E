from django.db import models
from .category import Category

class Subcategory(models.Model):
    category: models.ForeignKey = models.ForeignKey(Category, on_delete=models.CASCADE)
    name: models.TextField = models.TextField(max_length=255)
    image: models.ImageField = models.ImageField(blank=True)

    def __str__(self) -> models.TextField:
        return self.name