from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Contact, Property, Booking, Cart  
from .serializers import ContactSerializer, PropertySerializer, BookingSerializer, CartSerializer

# Create your views here.

class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    @action(detail=False, methods=['GET', 'PUT'])
    def me(self, request):
        (contact, created) = Contact.objects.get_or_create(user_id=request.user.id)
        if request.method == 'GET':
            serializer = ContactSerializer(contact)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = ContactSerializer(contact, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)


class PropertyViewSet(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer