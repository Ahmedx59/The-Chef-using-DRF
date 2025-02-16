from rest_framework import mixins , viewsets 

from django.shortcuts import render

from booking.models import Booking
from .serializers import (
    ListBookingSerializer,
    RetrieveBookingSerializer,
    CreateUpdateSerializer,
                          
)

class BookingViewSet(mixins.ListModelMixin,
              mixins.RetrieveModelMixin,
              mixins.CreateModelMixin,
    viewsets.GenericViewSet
    ):
    queryset = Booking.objects.all()
    serializer_class = ListBookingSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return RetrieveBookingSerializer
        if self.action == 'create':
            return CreateUpdateSerializer
        return super().get_serializer_class()