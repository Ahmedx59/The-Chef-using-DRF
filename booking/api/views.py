from rest_framework import mixins , viewsets 

from django.shortcuts import render

from booking.models import Booking
from .serializers import (
    ListBookingSerializer,
    RetrieveBookingSerializer,
    CreateBookingSerializer,
    UpdateBookingSerializer,
                          
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
            print("x"*100)
            return UpdateBookingSerializer
        return super().get_serializer_class()