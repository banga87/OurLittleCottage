from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .models import Contact, Property, Booking, Cart  
from .serializers import ContactSerializer, PropertySerializer, BookingSerializer, CartSerializer

# Create your views here.

class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class PropertyViewSet(ModelViewSet):
    queryset = Property.objects.prefetch_related('address').all()
    serializer_class = PropertySerializer


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer