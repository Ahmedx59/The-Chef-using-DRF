from rest_framework.routers import DefaultRouter
from order.api.views import CartViewSet , OrderViewSet

router = DefaultRouter()

router.register('cart' , CartViewSet , basename='cart')
router.register('order' , OrderViewSet , basename='order')


urlpatterns = router.urls

app_name = 'order'