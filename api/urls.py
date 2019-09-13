from rest_framework import routers
from .api import MovieViewSet

router = routers.DefaultRouter()
router.register('api/v1', MovieViewSet, 'movies')

urlpatterns = router.urls