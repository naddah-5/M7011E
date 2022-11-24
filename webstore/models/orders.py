from django.db import models
from .users import Users

class Orders(models.Model):
    ID = models.BigAutoField(primary_key=True)
    Order_Date = models.DateTimeField()
    Customer_ID = models.ForeignKey(Users, on_delete=models.CASCADE)
