from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .models import Guest, Property, Booking, Cart  
from .serializers import GuestSerializer, PropertySerializer, BookingSerializer, CartSerializer

# Create your views here.

class GuestViewSet(ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


class PropertyViewSet(ModelViewSet):
    queryset = Property.objects.prefetch_related('address').all()
    serializer_class = PropertySerializer


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer