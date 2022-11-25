from django.db import models
from typing import Literal
from .products import Products
from .subcategories import Subcategories

class InSubcategory(models.Model):
    product: models.ForeignKey = models.ForeignKey(Products, on_delete=models.CASCADE)
    subcategory: models.ForeignKey = models.ForeignKey(Subcategories, on_delete=models.CASCADE)

    class Meta:
        unique_together: tuple[Literal['product'], Literal['subcategory']] = ('product', 'subcategory')