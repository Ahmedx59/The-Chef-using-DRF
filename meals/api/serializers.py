from rest_framework import serializers
from meals.models import Meals , Chief

class MealsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meals
        fields = ['name','image','price']

class MealsRetrieveCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meals
        fields = '__all__'

