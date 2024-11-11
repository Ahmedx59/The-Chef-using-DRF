from rest_framework import serializers
from .models import Restaurant , Table

class RestaurantListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['name','image','desc']
        

class RestaurantDetailUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'



class TableListSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Table
        fields = '__all__'