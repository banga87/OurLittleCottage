from django.contrib import admin
from .models import Contact, Property, Booking, Cart
from django import forms

# Register your models here.
class PropertyForm(forms.ModelForm):
    owner = forms.ModelChoiceField(queryset=Contact.objects.all())

    class Meta:
        model = Property
        fields = '__all__'


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'user']
    list_per_page = 20
    

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['title', 'beds', 'owner', 'address']
    form = PropertyForm


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['property', 'guest', 'guest_quantity', 'host', 'start_date', 'end_date', 'duration', 'booking_status']


@admin.register(Cart)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['property', 'guest', 'guest_quantity', 'host', 'start_date', 'end_date', 'duration']