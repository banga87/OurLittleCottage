from rest_framework import serializers
from .models import Contact, Property, Address


class ContactSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Contact
        fields = ['id', 'user_id', 'email', 'phone']
        

class GuestSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    full_name = serializers.CharField(source='__str__', read_only=True)

    class Meta:
        model = Contact
        fields = ['id', 'full_name', 'email']


class OwnerSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    full_name = serializers.CharField(source='__str__', read_only=True)

    class Meta:
        model = Contact
        fields = ['id', 'full_name', 'email']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['street_number', 'street', 'state', 'country']


class PropertySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    guests = GuestSerializer(many=True, required=False, read_only=True)
    owner = OwnerSerializer(many=False)
    address = AddressSerializer(many=False, required=False, read_only=True)

    class Meta:
        model = Property
        fields = ['id', 'title', 'beds', 'owner', 'guests', 'address']

    def create(self, validated_data):
        owner_data = validated_data.pop('owner')
        owner = Contact.objects.create(**owner_data)
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)
        property = Property.objects.create(owner=owner, address=address, **validated_data)
        return property



# Adds a Guest to a Property
class AddGuestSerializer(serializers.ModelSerializer):
    pass