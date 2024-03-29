from django.db import models

class Category(models.Model):
    name: models.TextField = models.TextField(max_length=255)
    image: models.ImageField = models.ImageField(blank=True, null=True)

    def __str__(self)-> models.TextField:
        return self.name