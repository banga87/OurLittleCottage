from rest_framework import serializers
from .models import Guest, Property, Booking, Cart


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['first_name', 'last_name', 'email', 'phone', 'property_owner', 'user']


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['title', 'beds', 'owner', 'last_update', 'address']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['property', 'guest', 'guest_quantity', 'start_date', 'end_date', 'duration', 'booking_status']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['created_at', 'property', 'guest', 'guest_quantity', 'start_date', 'end_date', 'duration']
