from rest_framework import mixins , viewsets 

from django.shortcuts import render

from booking.models import Booking
from .serializers import (
    ListBookingSerializer,
                          
)

class booking(mixins.ListModelMixin,
    viewsets.GenericViewSet
    ):
    queryset = Booking.objects.all()
    serializer_class = ListBookingSerializer

    