from rest_framework import mixins , viewsets 
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render

from booking.models import Booking , Coupon
from restaurant.models import Restaurant
from order.admin import Order
from meals.models import Meals

from .serializers import (
    ListBookingSerializer,
    RetrieveBookingSerializer,
    CreateBookingSerializer,
    UpdateBookingSerializer,
    CouponSerializer,
                          
)

class BookingViewSet(mixins.ListModelMixin,
              mixins.RetrieveModelMixin,
              mixins.CreateModelMixin,
              mixins.UpdateModelMixin,
    viewsets.GenericViewSet
    ):
    queryset = Booking.objects.all()
    serializer_class = ListBookingSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return RetrieveBookingSerializer
        if self.action == 'create':
            return CreateBookingSerializer
        if self.action in ('update','partial_update'):
            return UpdateBookingSerializer
        return super().get_serializer_class()
    
class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer


class DashboardViewSet(viewsets.GenericViewSet):
    queryset = Booking.objects.all()
    serializer_class = ""

    @action(detail=False , methods=['get'])
    def count(self,*args, **kwargs):
        user = self.request.user
        restaurant = Restaurant.objects.filter(user=user).first()

        total_booking = Booking.objects.filter(restaurant = restaurant).count()
        total_meals = Meals.objects.filter(restaurant = restaurant).count()

        booking_active = Booking.objects.filter(status = Booking.BookingStatus.ACTIVE , restaurant = restaurant).count()
        booking_ended = Booking.objects.filter(status = Booking.BookingStatus.ENDED , restaurant = restaurant).count()
        booking_canceled = Booking.objects.filter(status = Booking.BookingStatus.CANCELED , restaurant = restaurant).count()

        new_meals = Meals.objects.filter(tag=Meals.TagChoices.NEW , restaurant = restaurant).count()
        feature_meals = Meals.objects.filter(tag=Meals.TagChoices.FEATURE , restaurant = restaurant).count()
        discount_meals = Meals.objects.filter(tag=Meals.TagChoices.DISCOUNT , restaurant = restaurant).count()

        return Response({"total_booking":total_booking,
                         "total_booking_active":booking_active,
                         "total_booking_ended":booking_ended,
                         "total_booking_canceled":booking_canceled,
                         "total_meals":total_meals,
                         "total_meals_new":new_meals,
                         "total_meals_feature":feature_meals,
                         "total_meals_discount":discount_meals}
                    )
    
    # @action(detail=False , methods=['get'])
    # def count_order(self,*args, **kwargs):
    #     user = self.request.user
    #     restaurant = Restaurant.objects.filter(user=user).first()
    #     total_order = Order.objects.filter(restaurant = restaurant)

    # @action(detail=False , methods=['get'])
    # def count_meals(self,*args, **kwargs):
    #     user = self.request.user
    #     restaurant = Restaurant.objects.filter(user = user).first()
    #     total_meals = Meals.objects.filter(restaurant = restaurant).count()
    #     new_meals = Meals.objects.filter(tag=Meals.TagChoices.NEW , restaurant = restaurant).count()
    #     feature_meals = Meals.objects.filter(tag=Meals.TagChoices.FEATURE , restaurant = restaurant).count()
    #     discount_meals = Meals.objects.filter(tag=Meals.TagChoices.DISCOUNT , restaurant = restaurant).count()

    #     return Response({"total_meals":total_meals,
    #                      "total_meals_new":new_meals,
    #                      "total_meals_feature":feature_meals,
    #                      "total_meals_discount":discount_meals}
    #                 )


    




        
