from rest_framework import serializers
from .models import Contact, Property, Address


class ContactSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    full_name = serializers.CharField(source='__str__', read_only=True)

    class Meta:
        model = Contact
        fields = ['id', 'user_id', 'full_name', 'email', 'phone']


class GuestSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='__str__', read_only=True)

    class Meta:
        model = Contact
        fields = ['id', 'full_name', 'email']


class OwnerSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='__str__', read_only=True)

    class Meta:
        model = Contact
        fields = ['id', 'full_name', 'email']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['street_number', 'street', 'state', 'country']


class PropertySerializer(serializers.ModelSerializer):
    guests = GuestSerializer(many=True)
    owner = OwnerSerializer(many=False)
    address = AddressSerializer(many=False)

    class Meta:
        model = Property
        fields = ['id', 'title', 'beds', 'owner', 'guests', 'address']