from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
