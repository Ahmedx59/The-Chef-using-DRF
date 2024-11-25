from django.shortcuts import render
from rest_framework import viewsets , mixins 
from .models import Restaurant , Table
from .serializers import RestaurantListSerializers ,RestaurantDetailSerializer ,TableListSerializer ,RestaurantUpdateSerializers
class RestaurantViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet):

    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializers 


    def get_serializer_class(self):
        if self.action == 'retrieve':
            return RestaurantDetailSerializer
        if self.action == 'update':
            return RestaurantUpdateSerializers
        
        return super().get_serializer_class()
    


class TableViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet):

    queryset = Table.objects.all()
    serializer_class = TableListSerializer