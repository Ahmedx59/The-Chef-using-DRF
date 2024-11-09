from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet 

router = DefaultRouter()

router.register('restaurants' , RestaurantViewSet)



urlpatterns = router.urls
