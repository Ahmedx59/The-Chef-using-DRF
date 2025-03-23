from rest_framework.routers import DefaultRouter
from booking.api.views import BookingViewSet , CouponViewSet ,DashboardViewSet

router = DefaultRouter()

router.register(r'restaurants/(?P<restaurant_id>\d+)/booking', BookingViewSet, basename='booking')
router.register("coupon",CouponViewSet , basename="coupon")
router.register("dashboard",DashboardViewSet , basename="dashboard")


urlpatterns = router.urls

app_name = 'booking'