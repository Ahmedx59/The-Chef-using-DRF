from rest_framework import serializers
from meals.models import Meals , Chief

from restaurant.models import Restaurant

class MealsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meals
        fields = ['id','name','image','price']

class MealsRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meals
        fields = '__all__'

class MealsCreateUpdateDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meals
        exclude = ('restaurant',)

    def validate(self, attrs):
        print('/'*100)


        user = self.context['request'].user
        restaurant_id = self.context['view'].kwargs['restaurant_id']
        restaurant = Restaurant.objects.get(id = restaurant_id)

        print('/'*100)

        if not user == restaurant.user:
            print('/'*100)

            raise serializers.ValidationError({'detail':'you cant do any action on this restaurant'}) 
        
        return super().validate(attrs)

    def create(self, validated_data):
        user = self.context['request'].user
        restaurant = Restaurant.objects.get(user = user)
        validated_data['restaurant'] = restaurant
        return super().create(validated_data)
