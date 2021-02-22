from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=64)
    ingredients = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now=True)
    preparation_time = models.IntegerField()
    votes = models.IntegerField(default=0)
    description_short = models.CharField(max_length=128)
