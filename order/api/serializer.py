from rest_framework import serializers

from order.models import Cart , MealsDetail , Order 
from meals.models import Meals

from django.shortcuts import get_object_or_404

from meals.api.serializers import MealsRetrieveSerializer

class RetrieveCart(serializers.ModelSerializer):
    meal = MealsRetrieveSerializer()
    class Meta:
        model = MealsDetail
        fields = (
            "meal",
            "quantity",
            "price",
            "total",
        )

class RetrieveCartSerializer(serializers.ModelSerializer):
    # meals_detail = serializers.PrimaryKeyRelatedField(queryset = MealsDetail.objects.all() , many = True)
    meals_detail = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields = (
            'user',
            'is_completed',
            'coupon',
            'total',
            'total_after_coupon',
            'meals_detail',
        )

    def get_meals_detail(self, obj):
        qs = obj.cart_detail.all()
        return RetrieveCart(qs, many=True).data
    
class CreateCartSerializer(serializers.Serializer):
    meal = serializers.IntegerField(required = True)
    quantity = serializers.IntegerField(required = True)

    def create(self, validated_data):
        meal = get_object_or_404(Meals, id=validated_data["meal"])
        user = self.context['request'].user
        quantity = validated_data['quantity']

        cart , created = Cart.objects.get_or_create(user = user)
        meals_detail , created = MealsDetail.objects.get_or_create(cart = cart , meal = meal)

        meals_detail.quantity = quantity
        meals_detail.price = meal.price
        meals_detail.total = round(quantity *meal.price , 2)
        meals_detail.save()
        return cart
    
    def to_representation(self, instance):
        return RetrieveCartSerializer(instance).data
    
    
class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"