from django.db import models
from .users import Users

class Orders(models.Model):
    PROCESSING = 'PS'
    PACKAGING = 'PG'
    SHIPPING = 'SH'
    PICKUP = 'PU'
    DELIVERED = 'DV'

    STATUS = [
        (PROCESSING, 'Processing'),
        (PACKAGING, 'Packaging'),
        (SHIPPING, 'Shipping'),
        (PICKUP, 'Pickup'),
        (DELIVERED, 'Delivered'),
    ]

    ID = models.BigAutoField(primary_key=True)
    Order_Date = models.DateTimeField()
    Customer_ID = models.ForeignKey(Users, on_delete=models.CASCADE)
    Address = models.TextField()
    Status = models.CharField(
        max_length=2,
        choices=STATUS,
        default=PROCESSING,
    )
    Delivery = models.DateTimeField(blank=True)