from rest_framework.routers import DefaultRouter
from order.api.views import CartViewSet

router = DefaultRouter()

router.register('cart' , CartViewSet , basename='cart')


urlpatterns = router.urls

app_name = 'order'