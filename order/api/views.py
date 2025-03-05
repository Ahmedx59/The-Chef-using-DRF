from django.shortcuts import render
 
from rest_framework import mixins , viewsets

from order.models import Cart
from order.api.serializer import (
    RetrieveCartSerializer ,
    CreateCartSerializer,

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