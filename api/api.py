from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Movie
from .serializers import MovieSerializer

# Viewset
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
