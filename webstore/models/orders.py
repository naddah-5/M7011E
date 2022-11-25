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

    ID: models.BigAutoField = models.BigAutoField(primary_key=True)
    Order_Date: models.DateTimeField = models.DateTimeField()
    Customer_ID: models.ForeignKey = models.ForeignKey(Users, on_delete=models.CASCADE)
    Address: models.TextField = models.TextField()
    Status: models.CharField = models.CharField(
        max_length=2,
        choices=STATUS,
        default=PROCESSING,
    )
    Delivery: models.DateTimeField = models.DateTimeField(blank=True)