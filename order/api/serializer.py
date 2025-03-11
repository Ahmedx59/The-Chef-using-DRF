from rest_framework import serializers

from django.shortcuts import get_object_or_404
from django.utils.crypto import get_random_string
from datetime import datetime ,timedelta

from order.models import Cart , CartItem , Order , OrderItem
from meals.api.serializers import MealsRetrieveSerializer
from meals.models import Meals



class RetrieveCart(serializers.ModelSerializer):
    meal = MealsRetrieveSerializer()
    class Meta:
        model = CartItem
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
            'coupon',
            'total',
            'total_after_coupon',
            'meals_detail',
        )

    def get_meals_detail(self, obj):
        qs = obj.cart_item.all()
        return RetrieveCart(qs, many=True).data
    
class CreateCartSerializer(serializers.Serializer):
    meal = serializers.IntegerField(required = True)
    quantity = serializers.IntegerField(required = True)

    def create(self, validated_data):
        
        meal = get_object_or_404(Meals, id=validated_data["meal"])
        user = self.context['request'].user
        quantity = validated_data['quantity']
        
        cart , created = Cart.objects.get_or_create(user = user)
        meals_detail , created = CartItem.objects.get_or_create(cart = cart , meal = meal)
        
        meals_detail.quantity = quantity
        meals_detail.price = meal.price
        meals_detail.total = round(quantity *meal.price , 2)
        meals_detail.save()
        return cart
    
    def to_representation(self, instance):
        return RetrieveCartSerializer(instance).data
    

class OrderItemSerializer(serializers.ModelSerializer):
    meal = MealsRetrieveSerializer()

    class Meta:
        model = OrderItem
        fields = (
            "meal",
            "quantity",
            "price",
            "total",
        )
    

class OrderListRetrieveSerializer(serializers.ModelSerializer):
    order_item = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = "__all__"

    def get_order_item(self, obj):
        qs = obj.order_item.all()
        return OrderItemSerializer(qs, many=True).data


class OrderCreateSerializer(serializers.Serializer):

    def create(self, validated_data):
        user = self.context['request'].user
        cart = Cart.objects.get(user = user)
        cart_item = CartItem.objects.filter(cart = cart)

        order = Order.objects.create(
            user=user,
            code = get_random_string(8),
            coupon = cart.coupon,
            total_after_coupon = cart.total_after_coupon,
            total_price = cart.total,
            delivery_location = user.address,
            delivery_time = timedelta(days=3) + datetime.now(),
            )
        for item in cart_item:
            order_item = OrderItem.objects.create(
                order = order,
                meal = item.meal,
                quantity = item.quantity,
                price = item.price,
                total = item.total,
            )
   
        cart.cart_item.all().delete()
        cart.coupon = None
        cart.total = 0
        cart.total_after_coupon = None
        cart.save()

        return order
