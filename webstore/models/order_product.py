from django.db import models
from typing import Literal
from .order import Order
from .product import Product

class OrderProduct(models.Model):
    product: models.ForeignKey = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    order: models.ForeignKey = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    quantity: models.IntegerField = models.IntegerField(default=1)
    price: models.DecimalField = models.DecimalField(decimal_places=2, max_digits=16)
    
    class Meta:
        unique_together: tuple[Literal['product_id'], Literal['order_id']] = ('product_id', 'order_id')