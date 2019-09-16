from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Movie
from .serializers import MovieSerializer

# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.views import APIView

# Viewset
class MovieViewSet(viewsets.ModelViewSet):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = (IsAuthenticated)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    # permission_class = [
    #     permissions.AllowAny
    # ]
    