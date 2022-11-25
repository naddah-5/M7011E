from django.db import models
from typing import Literal
from .products import Products
from .categories import Categories

class InCategories(models.Model):
    product: models.ForeignKey = models.ForeignKey(Products, on_delete=models.CASCADE)
    category: models.ForeignKey = models.ForeignKey(Categories, on_delete=models.CASCADE)

    class Meta:
        unique_together: tuple[Literal['product'], Literal['category']] = ('product', 'category')