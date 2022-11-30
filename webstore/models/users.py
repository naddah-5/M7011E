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

    def create_new_user(self, user_email: str, given_create_time: datetime.datetime, set_role: str) -> bool:
        try:
            Users(email = user_email, create_time = given_create_time, role = set_role).save()
            return True
        except ValueError:
            return False

    def __str__(self) -> models.EmailField:
        return self.email
