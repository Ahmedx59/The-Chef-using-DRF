from django.shortcuts import render
from rest_framework import viewsets , mixins 
from rest_framework.permissions import AllowAny , IsAdminUser
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend



from core.permissions import IsSeller
from restaurant.models import Restaurant , Table
from .serializers import RestaurantListSerializers ,RestaurantDetailSerializer ,TableListCreateUpdateDeleteSerializer ,RestaurantUpdateSerializers 
from users.models import User

class RestaurantViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet):

    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializers 
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['tag']
    search_fields = ['name','min_price']
    # permission_classes = [AllowAny]

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        
        if self.action in ['update','partial_update','retrieve' , 'create']:
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
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):

    queryset = Table.objects.all()
    serializer_class = TableListCreateUpdateDeleteSerializer


    def get_queryset(self):
        restaurant_id = self.kwargs['restaurant_id']  
        return super().get_queryset().filter(restaurant_id=restaurant_id , available = True )

        
    def get_permissions(self):
        if self.action in ['list','update','partial_update','create','destroy']:
            return [IsSeller()]
        return super().get_permissions()

