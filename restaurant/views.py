from django.shortcuts import render
from rest_framework import viewsets , mixins 
from .models import Restaurant
from .serializers import RestaurantListSerializers ,RestaurantDetailUpdateSerializer
class RestaurantViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet):

    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializers 


    def get_serializer_class(self):
        if self.action == 'retrieve':
            return RestaurantDetailUpdateSerializer
        return super().get_serializer_class()