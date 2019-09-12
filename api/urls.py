from rest_framework import routers
from .api import MovieViewSet

router = routers.DefaultRouter()
router.register('api/movies', MovieViewSet, 'movies')

urlpatterns = router.url