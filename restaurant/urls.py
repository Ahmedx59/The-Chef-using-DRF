from django.urls import path
from rest_framework.routers import DefaultRouter
from .api.views import RestaurantViewSet , TableViewSet

router = DefaultRouter()

router.register('restaurants' , RestaurantViewSet)
router.register(r'restaurants/(?P<restaurant_id>\d+)/tables' ,TableViewSet)

urlpatterns = router.urls
