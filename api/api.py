from api.models import Movies
from rest_framework import viewsets, permissions
from .serializers import MoviesSerializer

# Viewset
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    permission_class = [
        permissions.AllowAny
    ]
    serializer_class = MoviesSerializer