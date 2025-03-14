from rest_framework import mixins , viewsets 

from django.shortcuts import render

from booking.models import Booking , Coupon

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