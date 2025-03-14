from rest_framework import serializers

from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404

from datetime import datetime

from booking.models import Booking , Coupon
from restaurant.models import Restaurant

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
