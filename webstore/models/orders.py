from django.db import models
from .users import Users
from typing import Literal

class Orders(models.Model):
    PROCESSING: Literal['PS'] = 'PS'
    PACKAGING: Literal['PG'] = 'PG'
    SHIPPING: Literal['SH'] = 'SH'
    PICKUP: Literal['PU'] = 'PU'
    DELIVERED: Literal['DV'] = 'DV'

    STATUS: list[tuple] = [
        (PROCESSING, 'Processing'),
        (PACKAGING, 'Packaging'),
        (SHIPPING, 'Shipping'),
        (PICKUP, 'Pickup'),
        (DELIVERED, 'Delivered'),
    ]

    id: models.BigAutoField = models.BigAutoField(primary_key=True)
    order_date: models.DateTimeField = models.DateTimeField()
    customer: models.ForeignKey = models.ForeignKey(Users, on_delete=models.CASCADE)
    address: models.TextField = models.TextField()
    status: models.CharField = models.CharField(
        max_length=2,
        choices=STATUS,
        default=PROCESSING,
    )
    delivery: models.DateTimeField = models.DateTimeField(blank=True)