from rest_framework import serializers
from .models import Restaurant

class RestaurantListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['name','image','desc']
        

class RestaurantDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'