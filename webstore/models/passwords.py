from django.db import models

class Passwords(models.Model):
    ID: models.BigAutoField = models.BigAutoField(primary_key=True)
    Hash: models.TextField = models.TextField()

    