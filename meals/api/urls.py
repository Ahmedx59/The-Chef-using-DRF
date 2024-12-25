from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MealsVewSet 

router = DefaultRouter()

router.register('meals-viewsets' , MealsVewSet)
urlpatterns = router.urls
