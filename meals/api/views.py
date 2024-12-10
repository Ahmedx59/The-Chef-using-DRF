from django.shortcuts import render
from rest_framework import mixins , viewsets 


from meals.models import Meals , Chief 
from .serializers import MealsListSerializer , MealsRetrieveCreateUpdateSerializer


class MealsVewSet(viewsets.ModelViewSet):
    
    queryset = Meals.objects.all()
    serializer_class = MealsListSerializer

    def get_serializer_class(self):
        if self.action in ['retrieve' , 'create' , 'update']:
            return MealsRetrieveCreateUpdateSerializer
        
        return super().get_serializer_class()
    







