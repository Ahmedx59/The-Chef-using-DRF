from rest_framework import serializers
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404

from booking.models import Booking
from restaurant.models import Restaurant

class ListBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['user','table']


class RetrieveBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class CreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('start_date','end_date','coupon','table')

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
        coupon_discount = validated_data.get('coupon')

        send_mail(
            "Booking Confirmation",
            f"Dear {user} \n"
            f"restaurant : {restaurant.name} \n"
            f"table : { table} \n"
            f"start_date : {start_date} \n"
            f"end_date : {end_date} \n"
            f"coupon discount : {coupon_discount} \n"
            f"code : {code} \n",
            'Company_mail@mail.com',
            [user.email]   
        )


        return super().create(validated_data)
