from django.db import models
from typing import Literal
import datetime

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
    role: models.CharField = models.CharField(
        max_length=2,
        choices=ROLE,
        default=CUSTOMER,
    )

    def __str__(self) -> models.EmailField:
        return self.email
