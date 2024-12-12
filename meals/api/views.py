from django.shortcuts import render
from rest_framework import mixins , viewsets 
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from meals.models import Meals , Chief 
from .serializers import MealsListSerializer , MealsRetrieveCreateUpdateSerializer


class MealsVewSet(viewsets.ModelViewSet):
    queryset = Meals.objects.all()
    serializer_class = MealsListSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['tag']
    search_fields = ['name','price']

    def get_serializer_class(self):
        if self.action in ['retrieve' , 'create' , 'update']:
            return MealsRetrieveCreateUpdateSerializer
        
        return super().get_serializer_class()
    







