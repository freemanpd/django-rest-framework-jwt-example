from django.urls import path, include
from rest_framework import routers
from .api import MovieViewSet

router = routers.DefaultRouter()
router.register('api/v1', MovieViewSet, 'movie')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]