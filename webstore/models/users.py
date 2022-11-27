from django.db import models
from .passwords import Passwords
from typing import Literal

class Users(models.Model):
    CUSTOMER: Literal['CM'] = 'CM'
    ADMIN:  Literal['AD'] = 'AD'
    SUPERUSER: Literal['SU'] = 'SU'
    
    ROLE: list[tuple] = [
        (CUSTOMER, 'Customer'),
        (ADMIN, 'Admin'),
        (SUPERUSER, 'Superuser'),
    ]
    email: models.EmailField = models.EmailField()
    create_time: models.DateTimeField = models.DateTimeField()
    password: models.ForeignKey = models.ForeignKey(Passwords, on_delete=models.CASCADE)
    role: models.CharField = models.CharField(
        max_length=2,
        choices=ROLE,
        default=CUSTOMER,
    )