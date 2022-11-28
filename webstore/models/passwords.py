from django.db import models

class Passwords(models.Model):
    hash: models.TextField = models.TextField()
