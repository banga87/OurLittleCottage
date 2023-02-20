from rest_framework import serializers
from .models import Guest


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['first_name', 'last_name', 'email', 'phone', 'property_owner', 'user']