from django.db import models
from django.contrib.auth import get_user_model
from typing import Literal

class UserProfile(models.Model):
    CUSTOMER: Literal['CM'] = 'CM'
    ADMIN:  Literal['AD'] = 'AD'
    SUPERUSER: Literal['SU'] = 'SU'
    
    ROLE: list[tuple] = [
        (CUSTOMER, 'Customer'),
        (ADMIN, 'Admin'),
        (SUPERUSER, 'Superuser'),
    ]
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='profile'
        )
    role: models.CharField = models.CharField(
        max_length=2,
        choices=ROLE,
        default=CUSTOMER,
    )

    class Meta:
        verbose_name_plural = 'UserProfiles'
        db_table = 'user_profile'

    def __str__(self):
        return self.user.get_username()
