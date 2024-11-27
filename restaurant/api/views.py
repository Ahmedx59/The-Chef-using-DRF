from django.shortcuts import render
from rest_framework import viewsets , mixins 
from ..models import Restaurant , Table
from .serializers import RestaurantListSerializers ,RestaurantDetailSerializer ,TableListSerializer ,RestaurantUpdateSerializers
from rest_framework.permissions import AllowAny , IsAdminUser
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