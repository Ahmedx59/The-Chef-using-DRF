from django.shortcuts import render
from rest_framework import mixins , viewsets , serializers
from rest_framework import filters
# from django_filters.rest_framework import DjangoFilterBackend

from restaurant.models import Restaurant

from core.permissions import IsSeller
from meals.models import Meals , Chief 
from .serializers import MealsListSerializer , MealsRetrieveSerializer , MealsCreateUpdateDeleteSerializer



class MealsVewSet(viewsets.ModelViewSet):
    queryset = Meals.objects.all()
    serializer_class = MealsListSerializer
    filter_backends = [filters.SearchFilter]
    filterset_fields = ['tag']
    search_fields = ['name','price']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return MealsRetrieveSerializer
        if self.action in ['create','update','partial_update','destroy', 'delete']:
            print('/'*100)
            return MealsCreateUpdateDeleteSerializer
        
        return super().get_serializer_class()
    
    def get_queryset(self):
        restaurant_id = self.kwargs['restaurant_id']
        return super().get_queryset().filter(restaurant = restaurant_id)
    

    def get_permissions(self):
        if self.action in ['update','partial_update','create','destroy']:
            return [IsSeller()]
        return super().get_permissions()
    

    def perform_destroy(self, instance):
        user = self.request.user
        restaurant_id = self.kwargs['restaurant_id']
        restaurant = Restaurant.objects.get(id = restaurant_id)
        if user != restaurant.user:
            raise serializers.ValidationError({'detail':'you cant do any action on this restaurant'})
        return super().perform_destroy(instance)






