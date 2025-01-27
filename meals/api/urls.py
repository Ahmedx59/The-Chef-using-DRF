from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MealsVewSet 

router = DefaultRouter()

router.register(r'restaurants/(?P<restaurant_id>\d+)/meals' , MealsVewSet)
urlpatterns = router.urls
