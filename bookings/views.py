from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Contact, Property, Booking, Cart, Address
from .serializers import ContactSerializer, PropertySerializer, BookingSerializer, CartSerializer, AddressSerializer

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
        
class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    http_method_names = ['get']


class PropertyViewSet(ModelViewSet):
    queryset = Property.objects.prefetch_related('address').all()
    serializer_class = PropertySerializer


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


# Class used for /my-properties URL to view 'my properties'
class OwnerPropertyViewSet(PropertyViewSet):
    # Overriding get_queryset to return a list of properties based on the user logged in.
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Property.objects.filter(owner=user.contact)
        else:
            return Property.objects.none()
        
    
class GuestPropertyViewSet(PropertyViewSet):
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Property.objects.filter(guest=user.contact)
        else:
            return Property.objects.none()