from django.db import models
from django.contrib.auth import get_user_model
from .products import Products

class Reviews(models.Model):
    user: models.ForeignKey = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product: models.ForeignKey = models.ForeignKey(Products, on_delete=models.CASCADE)
    rating: models.IntegerField = models.IntegerField()
    text: models.TextField = models.TextField(blank=True)
    create_time: models.DateTimeField = models.DateTimeField()