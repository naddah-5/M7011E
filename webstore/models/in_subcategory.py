from django.db import models
from typing import Literal
from .product import Product
from .subcategory import Subcategory

class InSubcategory(models.Model):
    product: models.ForeignKey = models.ForeignKey(Product, on_delete=models.CASCADE)
    subcategory: models.ForeignKey = models.ForeignKey(Subcategory, on_delete=models.CASCADE)

    class Meta:
        unique_together: tuple[Literal['product'], Literal['subcategory']] = ('product', 'subcategory')