from rest_framework import serializers
from api.api import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie 
        fields = ('title','realeased','runtime', 'genre', 'rated','plot', 'date_created', 'last_updated', 'creator')



    #         title = models.CharField(blank=False, max_length=100)
    # released = models.IntegerField(blank=False)
    # runtime = models.IntegerField(blank=False)
    # genre = models.CharField(blank=False, max_length=100)
    # rated = models.CharField(blank=False, max_length=10)
    # plot = models.CharField(blank=False, max_length=1000)
    # date_created = models.DateTimeField(auto_now_add=True) 
    # last_updated = models.DateTimeField(auto_now=True)
    # creator = models.ForeignKey('auth.User', on_delete=models.CASCADE)