from django.shortcuts import render
from rest_framework import viewsets , mixins 
from .models import Restaurant
from .serializers import RestaurantListSerializers ,RestaurantDetailSerializer
class RestaurantViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet):

    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializers 

