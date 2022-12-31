from django.db import models
from typing import Literal
from django.contrib.auth import get_user_model
from .product import Product

class CartProduct(models.Model):
    user: models.ForeignKey = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product: models.ForeignKey = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity: models.IntegerField = models.IntegerField(default=1)

    class Meta:
        unique_together: tuple[Literal['user_id'], Literal['product_id']] = ('user_id', 'product_id')

    def getProducts(self):
        for item in self.product:
            print(item)
        return None