from django.db import models
from typing import Literal
from .orders import Orders
from .products import Products

class OrderProducts(models.Model):
    product: models.ForeignKey = models.ForeignKey(Products, on_delete=models.CASCADE)
    order: models.ForeignKey = models.ForeignKey(Orders, on_delete=models.CASCADE)
    quantity: models.IntegerField = models.IntegerField(default=1)
    price: models.DecimalField = models.DecimalField(decimal_places=2, max_digits=16)
    
    class Meta:
        unique_together: tuple[Literal['product_id'], Literal['order_id']] = ('product_id', 'order_id')