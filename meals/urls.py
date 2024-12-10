from django.urls import path
from rest_framework.routers import DefaultRouter
from meals.api.views import MealsVewSet 

router = DefaultRouter()
router.register('meals-viewset' , MealsVewSet)
urlpatterns = router.urls
