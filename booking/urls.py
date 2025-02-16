from rest_framework.routers import DefaultRouter
from booking.api.views import BookingViewSet

router = DefaultRouter()

router.register(r'restaurants/(?P<restaurant_id>\d+)/booking', BookingViewSet, basename='booking')

urlpatterns = router.urls

app_name = 'booking'