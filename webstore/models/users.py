from django.db import models
from .passwords import Passwords

class Users(models.Model):
    CUSTOMER = 'CM'
    ADMIN = 'AD'
    SUPERUSER = 'SU'
    
    ROLE = [
        (CUSTOMER, 'Customer'),
        (ADMIN, 'Admin'),
        (SUPERUSER, 'Superuser'),
    ]
    ID = models.BigAutoField(primary_key=True)
    Email = models.EmailField()
    Create_Time = models.DateTimeField()
    Password_ID = models.ForeignKey(Passwords, on_delete=models.CASCADE)
    Role = models.CharField(
        max_length=2,
        choices=ROLE,
        default=CUSTOMER,
    )