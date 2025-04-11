from rest_framework import serializers

from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.db.models.aggregates import Sum
from datetime import datetime

from booking.models import Booking , Coupon
from meals.models import Meals , Chief
from order.models import Order, OrderItem
from restaurant.models import Restaurant, Table 

class ListBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['user','table']


class RetrieveBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class CreateBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            'start_date',
            'end_date',
            'table'
            )

    def create(self, validated_data):
        user = self.context['request'].user
        restaurant_id = self.context['view'].kwargs['restaurant_id']
        restaurant = get_object_or_404(Restaurant , id=restaurant_id)
        code = get_random_string(10)

        validated_data['user']= user
        validated_data['restaurant']= restaurant
        validated_data['code']= code
        validated_data['user']=user

        table = validated_data['table'].title
        start_date = validated_data['start_date']
        end_date = validated_data['end_date']

        send_mail(
            "Booking Confirmation",
            f"Dear {user} \n"
            f"restaurant : {restaurant.name} \n"
            f"table : { table} \n"
            f"start_date : {start_date} \n"
            f"end_date : {end_date} \n"
            f"code : {code} \n",
            'Company_mail@mail.com',
            [user.email]   
        )
        
        return super().create(validated_data)
    
class UpdateBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            'start_date',
            'end_date',
            'table'
            )

    def update(self, instance, validated_data):
        # print(validated_data['start_date'])
        # print(datetime.now())
        # deadline = validated_data['start_date'] - datetime.now()
        # print(deadline,"X"*100)
        # # if validated_data['start_date'] - datetime.now():
        # #     raise x
        return super().update(instance, validated_data)
    
class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = "__all__"


# class DashboardSerializer(serializers.Serializer):
#     total_order = serializers.SerializerMethodField()
#     total_orders_price = serializers.SerializerMethodField()

#     total_table = serializers.SerializerMethodField()
#     total_chief = serializers.SerializerMethodField()


#     total_booking = serializers.SerializerMethodField()
#     total_booking_active = serializers.SerializerMethodField()
#     total_booking_ended = serializers.SerializerMethodField()
#     total_booking_canceled = serializers.SerializerMethodField()

#     total_meals = serializers.SerializerMethodField()
#     total_meals_new = serializers.SerializerMethodField()
#     total_meals_feature = serializers.SerializerMethodField()
#     total_meals_discount = serializers.SerializerMethodField()

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         user = self.instance
#         self.restaurant = Restaurant.objects.filter(user=user).first()
#         self.booking = Booking.objects.filter(restaurant = self.restaurant)      
#         self.meals = Meals.objects.filter(restaurant = self.restaurant)
#         self.order_detail = OrderItem.objects.filter(meal__in = self.meals)
        



#     def get_total_booking(self,*args, **kwargs):
#         return self.booking.count()

#     def get_total_booking_active(self, *args, **kwargs):
#         return self.booking.filter(status = Booking.BookingStatus.ACTIVE).count()

#     def get_total_booking_ended(self, *args, **kwargs):
#         return self.booking.filter(status = Booking.BookingStatus.ENDED).count()


#     def get_total_booking_canceled(self, *args, **kwargs):
#         return self.booking.filter(status = Booking.BookingStatus.CANCELED).count()



#     def get_total_meals(self, *args, **kwargs):
#         return self.meals.count()

#     def get_total_meals_new(self, *args, **kwargs):
#         return self.meals.filter(tag = Meals.TagChoices.NEW).count()

#     def get_total_meals_feature(self, *args, **kwargs):
#         return self.meals.filter(tag = Meals.TagChoices.FEATURE).count()

#     def get_total_meals_discount(self, *args, **kwargs):
#         return self.meals.filter(tag = Meals.TagChoices.DISCOUNT).count()



#     def get_total_table(self, *args, **kwargs):
#         return Table.objects.filter(restaurant = self.restaurant).count()

#     def get_total_chief(self, *args, **kwargs):
#         return Chief.objects.filter(meals_chief__in = self.meals).count()

#     def get_total_order(self, *args, **kwargs):
#         return Order.objects.filter(order_item__in = self.order_detail).distinct().count()
    
#     def get_total_orders_price(self, *args, **kwargs):
#         return Order.objects.filter(order_item__in = self.order_detail).aggregate(total = Sum("total_price"))["total"]


class DashUserSerializer(serializers.Serializer):
    total_booking = serializers.SerializerMethodField()
    total_booking_active = serializers.SerializerMethodField()
    total_booking_ended = serializers.SerializerMethodField()
    total_booking_canceled = serializers.SerializerMethodField()
    
    total_meals = serializers.SerializerMethodField()
    total_meals_new = serializers.SerializerMethodField()
    total_meals_feature = serializers.SerializerMethodField()
    total_meals_discount = serializers.SerializerMethodField()

    total_order = serializers.SerializerMethodField()
    total_price_order = serializers.SerializerMethodField()
    
    total_chief = serializers.SerializerMethodField()
    total_table = serializers.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user = self.instance
        self.restaurant = Restaurant.objects.filter(user = user).first()
        self.booking = Booking.objects.filter(restaurant = self.restaurant)
        self.meal = Meals.objects.filter(restaurant = self.restaurant)
        self.order_item = OrderItem.objects.filter(meal__in = self.meal)
        self.order = Order.objects.filter(order_item__in = self.order_item)
        

        


    def get_total_booking(self , *args, **kwargs):
        return self.booking.count()
    
    def get_total_booking_active(self , *args, **kwargs):
        return self.booking.filter(status = Booking.BookingStatus.ACTIVE).count()
    
    def get_total_booking_ended(self , *args, **kwargs):
        return self.booking.filter(status = Booking.BookingStatus.ENDED).count()
    
    def get_total_booking_canceled(self , *args, **kwargs):
        return self.booking.filter(status = Booking.BookingStatus.CANCELED).count()
    


    def get_total_meals(self , *args, **kwargs):
        return self.meal.count()
    
    def get_total_meals_new(self , *args, **kwargs):
        return self.meal.filter(tag = Meals.TagChoices.NEW).count()
    
    def get_total_meals_feature(self , *args, **kwargs):
        return self.meal.filter(tag = Meals.TagChoices.FEATURE).count()
    
    def get_total_meals_discount(self , *args, **kwargs):
        return self.meal.filter(tag = Meals.TagChoices.DISCOUNT).count()
    


    def get_total_order(self , *args, **kwargs):
        return self.order.distinct().count()

    def get_total_price_order(self , *args, **kwargs):
        return self.order.aggregate(total = Sum("total_price"))["total"]
    


    def get_total_chief(self , *args, **kwargs):
        return Chief.objects.filter(meals_chief__in = self.meal).distinct().count()
    


    def get_total_table(self , *args, **kwargs):
        return Table.objects.filter(restaurant = self.restaurant).count()
        