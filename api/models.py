from django.db import models

class Movie(models.Model):
    title = models.CharField(blank=False, max_length=100)
    realeased = models.IntegerField(blank=False)
    runtime = models.IntegerField(blank=False)
    genre = models.CharField(blank=False, max_length=100)
    rated = models.CharField(blank=False, max_length=10)
    plot = models.CharField(blank=False, max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True, blank=True) 
    last_updated = models.DateTimeField(auto_now=True, blank=True)
    creator = models.ForeignKey('auth.User', blank=True, null=True, on_delete=models.CASCADE)