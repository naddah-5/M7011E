from django.db import models

from users import Users

class Passwords(models.Model):
    hash: models.TextField = models.TextField()
    user: models.ForeignKey = models.ForeignKey(Users, on_delete=models.CASCADE)
