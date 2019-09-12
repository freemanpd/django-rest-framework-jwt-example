from api.models import Movies
from rest_framework import viewset, permissions
from .serializers import MoviesSerializer

# Viewset
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    permission_class = [
        permissions.AllowAny
    ]
    serializer_class = MoviesSerializer