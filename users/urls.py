from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet , AuthViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('password' , AuthViewSet , basename='change-password')


urlpatterns = router.urls
