from django.db import models

class Passwords(models.Model):
    id: models.BigAutoField = models.BigAutoField(primary_key=True)
    hash: models.TextField = models.TextField()

    