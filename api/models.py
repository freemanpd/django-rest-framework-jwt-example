from django.db import models

class Movie(models.Model):
    title = models.CharField(blank=False, max_length=100)
    released = models.IntegerField(blank=False)
    genre = models.CharField(blank=False, max_length=100)
    creator = models.ForeignKey('auth.User', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
       return self.title