from rest_framework import serializers
from ..models import Restaurant , Table

class RestaurantListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id','user','name','image','desc']
        

class RestaurantDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class RestaurantUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if instance.user != user:
            raise serializers.ValidationError("You don't have permission to update this.")
        return super().update(instance, validated_data)
    








class TableListSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Table
        fields = '__all__'