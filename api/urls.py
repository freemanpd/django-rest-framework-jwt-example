from django.urls import path, include
from rest_framework import routers
from .api import MovieViewSet

router = routers.DefaultRouter()
router.register('api/v1', MovieViewSet, 'movie')

urlpatterns = [
    path('', include(router.urls))
]