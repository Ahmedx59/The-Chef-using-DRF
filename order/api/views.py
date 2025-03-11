from rest_framework import mixins , viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render

from order.models import Cart , Order


from order.api.serializer import (
    RetrieveCartSerializer ,
    CreateCartSerializer,
    OrderListRetrieveSerializer,
    OrderCreateSerializer

)
class CartViewSet(
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
    
    @action(detail=False , methods=['get'])
    def data(self,request , *args, **kwargs):

        user = self.request.user
        cart = Cart.objects.filter(user = user).first()

        if not cart:
            cart = Cart.objects.create(user = user)

        serializer = self.get_serializer(cart)
        return Response(serializer.data)
    

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
