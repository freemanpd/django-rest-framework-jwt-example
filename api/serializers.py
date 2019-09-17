from rest_framework import serializers
from api.api import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie 
        fields = "__all__"