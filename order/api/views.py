from rest_framework import mixins , viewsets

from django.shortcuts import render
 
from order.models import Cart , Order


from order.api.serializer import (
    RetrieveCartSerializer ,
    CreateCartSerializer,
    OrderListRetrieveSerializer,
    OrderCreateSerializer,

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
    
    def get_queryset(self):
        user = self.request.user
        return super().get_queryset().filter(user = user)
    


class OrderViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderListRetrieveSerializer

    def get_queryset(self):
        user = self.request.user
        return super().get_queryset().filter(user = user)
    

    def get_serializer_class(self):
        if self.action == "create":
            return OrderCreateSerializer
        return super().get_serializer_class()
