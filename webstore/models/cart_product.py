from django.db import models
from typing import Literal
from .users import Users
from .products import Products

class CartProducts(models.Model):
    user: models.ForeignKey = models.ForeignKey(Users, on_delete=models.CASCADE)
    product: models.ForeignKey = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity: models.IntegerField = models.IntegerField(default=1)

    class Meta:
        unique_together: tuple[Literal['user_id'], Literal['product_id']] = ('user_id', 'product_id')