from rest_framework import mixins , viewsets 
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render
from django.db.models.aggregates import Sum


from booking.models import Booking , Coupon
from restaurant.models import Restaurant , Table
from order.admin import Order , OrderItem
from meals.models import Meals , Chief

from .serializers import (
    ListBookingSerializer,
    RetrieveBookingSerializer,
    CreateBookingSerializer,
    UpdateBookingSerializer,
    CouponSerializer,
    DashUserSerializer,
    # DashboardSerializer,
                          
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
    serializer_class = DashUserSerializer

    @action(detail=False , methods=['get'])
    def count(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data)



















        # user = self.request.user
        # restaurant = Restaurant.objects.filter(user=user).first()
        # meals = Meals.objects.filter(restaurant = restaurant)
        # booking = Booking.objects.filter(restaurant = restaurant)
        
        # order_detail = OrderItem.objects.filter(meal__in = meals)
        # order = Order.objects.filter(order_item__in=order_detail).distinct().count()
        # total_orders_price = Order.objects.filter(order_item__in=order_detail).aggregate(total = Sum("total_price"))["total"]

        # if not total_orders_price:
        #     total_orders_price = 0

        # # total_order_price = 0
        # # for obj in orders:
        # #     total_order_price += obj.total_price

        # total_booking = booking.count()
        # booking_active = booking.filter(status = Booking.BookingStatus.ACTIVE).count()
        # booking_ended = booking.filter(status = Booking.BookingStatus.ENDED).count()
        # booking_canceled = booking.filter(status = Booking.BookingStatus.CANCELED).count()

        # total_meals = meals.count()
        # new_meals = meals.filter(tag=Meals.TagChoices.NEW).count()
        # feature_meals = meals.filter(tag=Meals.TagChoices.FEATURE).count()
        # discount_meals = meals.filter(tag=Meals.TagChoices.DISCOUNT).count()

        # total_chief = Chief.objects.filter(meals_chief__in = meals).distinct().count()
        # total_table = Table.objects.filter(restaurant = restaurant).count()

        # return Response({
        #     "total_price":total_orders_price,
        #     "total_table":total_table,

        #     "total_chief":total_chief,

        #     "total_order":order,

        #     "total_booking":total_booking,
        #     "total_booking_active":booking_active,
        #     "total_booking_ended":booking_ended,
        #     "total_booking_canceled":booking_canceled,

        #     "total_meals":total_meals,
        #     "total_meals_new":new_meals,
        #     "total_meals_feature":feature_meals,
        #     "total_meals_discount":discount_meals
        #     }
        # )
    