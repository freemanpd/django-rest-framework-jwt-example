from rest_framework import serializers
from api.models import Movies

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies 
        fields = '_all_'