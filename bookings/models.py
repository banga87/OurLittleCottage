from django.db import models
from django.conf import settings

# Create your models here.

class Guest(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    property_owner = models.BooleanField()
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Address(models.Model):
    street_number = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)


class Property(models.Model):
    title = models.CharField(max_length=255)
    beds = models.IntegerField()
    owner = models.ForeignKey(Guest, on_delete=models.PROTECT)
    last_update = models.DateTimeField(auto_now=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, default=None)


# COME BACK TO THIS!
# class PropertyImage(models.Model):
#     property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
#     image = models.ImageField(upload_to='bookings/images')


class Booking(models.Model):
    BOOKING_STATUS_PENDING = 'P'
    BOOKING_STATUS_BOOKED = 'B'
    BOOKING_STATUS_CANCELLED = 'C'
    BOOKING_STATUS_CHOICES = [
        (BOOKING_STATUS_PENDING, 'Pending'),
        (BOOKING_STATUS_BOOKED, 'Booked'),
        (BOOKING_STATUS_CANCELLED, 'Cancelled')
    ]

    property = models.ForeignKey(Property, on_delete=models.PROTECT)
    guest = models.ForeignKey(Guest, on_delete=models.PROTECT)
    guest_quantity = models.PositiveSmallIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.DurationField()
    booking_status = models.CharField(max_length=1, choices=BOOKING_STATUS_CHOICES, default=BOOKING_STATUS_PENDING)


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    property = models.ForeignKey(Property, on_delete=models.PROTECT)
    guest = models.ForeignKey(Guest, on_delete=models.PROTECT)
    guest_quantity = models.PositiveSmallIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.DurationField()