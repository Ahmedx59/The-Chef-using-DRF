from rest_framework import mixins , viewsets

from django.shortcuts import render
 
from order.models import Cart , Order


from order.api.serializer import (
    RetrieveCartSerializer ,
    CreateCartSerializer,
    OrderListSerializer,

)
class CartViewSet(
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet):

    queryset = Cart.objects.all()
    serializer_class = RetrieveCartSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateCartSerializer
        return super().get_serializer_class()
    


class OrderViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderListSerializer