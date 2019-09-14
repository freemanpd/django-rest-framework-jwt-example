from api.models import Movies
from rest_framework import viewsets, permissions
from .serializers import MoviesSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.views import APIView

# Viewset
class MovieViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    queryset = Movies.objects.all()
    permission_class = [
        permissions.AllowAny
    ]
    serializer_class = MoviesSerializer