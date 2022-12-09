from django.db import models
from django.contrib.auth import get_user_model
from typing import Literal
import datetime

class UserProfiles(models.Model):
    CUSTOMER: Literal['CM'] = 'CM'
    ADMIN:  Literal['AD'] = 'AD'
    SUPERUSER: Literal['SU'] = 'SU'
    
    ROLE: list[tuple] = [
        (CUSTOMER, 'Customer'),
        (ADMIN, 'Admin'),
        (SUPERUSER, 'Superuser'),
    ]
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    role: models.CharField = models.CharField(
        max_length=2,
        choices=ROLE,
        default=CUSTOMER,
    )

    def __str__(self):
        return self.role
