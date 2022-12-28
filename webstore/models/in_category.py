from django.db import models
from typing import Literal
from .product import Product
from .category import Category

class InCategory(models.Model):
    product: models.ForeignKey = models.ForeignKey(Product, on_delete=models.CASCADE)
    category: models.ForeignKey = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        unique_together: tuple[Literal['product'], Literal['category']] = ('product', 'category')