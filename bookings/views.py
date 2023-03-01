from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Contact, Property, Address
from .serializers import ContactSerializer, PropertySerializer, AddressSerializer, GuestSerializer, OwnerSerializer

# Create your views here.

class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
        
        
class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    http_method_names = ['get']


# Class used for /my-properties URL to view 'my properties'
class PropertyViewSet(ModelViewSet):
    queryset = Property.objects.prefetch_related('address').all()
    serializer_class = PropertySerializer

    # Overriding get_queryset to return a list of properties based on the user logged in.
    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_authenticated:
    #         return Property.objects.filter(owner=user.contact)
    #     else:
    #         return Property.objects.none()