from django.db import models
from django.contrib.auth import get_user_model
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

    order_date: models.DateTimeField = models.DateTimeField()
    customer: models.ForeignKey = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
    address: models.TextField = models.TextField()
    status: models.CharField = models.CharField(
        max_length=2,
        choices=STATUS,
        default=PROCESSING,
    )
    delivery: models.DateTimeField = models.DateTimeField(blank=True)