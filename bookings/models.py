from django.db import models
from django.conf import settings
from django.contrib import admin
import datetime

# Create your models here.

class Contact(models.Model):
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, default=None, blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
    # Pulls "first_name" from User AUTH_USER_MODEL found in core.models.py
    # Adds ability to sort by first_name in admin panel
    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name
    
    # Pulls "last_name" from User AUTH_USER_MODEL found in core.models.py
    # Adds ability to sort by last_name in admin panel
    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name
    
    class Meta:
        ordering = ['user__first_name', 'user__last_name']


class Address(models.Model):
    street_number = models.CharField(max_length=255, null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)


class Property(models.Model):
    title = models.CharField(max_length=255)
    beds = models.IntegerField(null=True, blank=True)
    owner = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True, blank=True)
    last_update = models.DateTimeField(auto_now=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.title


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
    guest = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='booking_guests')
    guest_quantity = models.PositiveSmallIntegerField(null=True, blank=True)
    host = models.ForeignKey(Contact  , on_delete=models.PROTECT, related_name='booking_host')
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.DurationField(null=True, blank=True)
    booking_status = models.CharField(max_length=1, choices=BOOKING_STATUS_CHOICES, default=BOOKING_STATUS_PENDING)

    # Override save() method of models.Model to calculate and save the duration field
    def save(self, *args, **kwargs):
        self.duration = self.end_date - self.start_date
        super().save(*args, **kwargs)


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    property = models.ForeignKey(Property, on_delete=models.PROTECT)
    guest = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='cart_guests')
    guest_quantity = models.PositiveSmallIntegerField(null=True, blank=True)
    host = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='cart_host')
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.DurationField(null=True, blank=True)

    # Override save() method of models.Model to calculate and save the duration field
    def save(self, *args, **kwargs):
        self.duration = self.end_date - self.start_date
        super().save(*args, **kwargs)