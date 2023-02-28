from rest_framework import serializers
from .models import Contact, Property, Booking, Cart, Address


class ContactSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Contact
        fields = ['id', 'user_id',  'email', 'phone']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['street_number', 'street', 'state', 'country']


class PropertySerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=False, read_only=True)
    
    class Meta:
        model = Property
        fields = ['id', 'title', 'beds', 'owner', 'guest', 'last_update', 'address']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'property', 'guest', 'guest_quantity', 'host', 'start_date', 'end_date', 'duration', 'booking_status']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'created_at', 'property', 'guest', 'guest_quantity', 'start_date', 'end_date', 'duration']
