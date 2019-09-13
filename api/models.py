from django.db import models

class Movies(models.Model):
    name = models.CharField(max_length=100)
    realeased = models.IntegerField()
    runtime = models.IntegerField()
    genre = models.CharField(max_length=100)
    rated = models.CharField(max_length=10)
    plot = models.CharField(max_length=1000)