from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet , PasswordViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('password' , PasswordViewSet , basename='change-password')


urlpatterns = router.urls
