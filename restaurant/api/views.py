from django.shortcuts import render
from rest_framework import viewsets , mixins 
from rest_framework.permissions import AllowAny , IsAdminUser

from core.permissions import IsSeller
from restaurant.models import Restaurant , Table
from .serializers import RestaurantListSerializers ,RestaurantDetailSerializer ,TableListSerializer ,RestaurantUpdateSerializers
from users.models import User

class RestaurantViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet):

    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializers 
    # permission_classes = [AllowAny]

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        
        if self.action in ['update','partial_update','retrieve']:
            return [IsSeller()]
        return super().get_permissions()
        



    def get_serializer_class(self):
        if self.action == 'retrieve':
            return RestaurantDetailSerializer
        if self.action in ['update','partial_update']:
            return RestaurantUpdateSerializers
        
        return super().get_serializer_class()
    


class TableViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet):

    queryset = Table.objects.all()
    serializer_class = TableListSerializer