from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import UserViewSet, ProductViewSet

router = SimpleRouter()
router.register("users", UserViewSet, basename='users')
router.register("", ProductViewSet, basename='posts')


urlpatterns = router.urls