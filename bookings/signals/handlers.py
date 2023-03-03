from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from bookings.models import Contact

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_contact_for_new_user(sender, instance, created, **kwargs):
    print('********SIGNAL RECEIVED********')
    if created:
        try:
            # If Contact with User email exists, update the Contact with the new User
            contact = Contact.objects.get(email=instance.email)
            contact.user = instance
            contact.save()
        except Contact.DoesNotExist:
            # If Contact with User email doesn't exist, create a new Contact and associate the new User.
            contact = Contact.objects.create(user=instance, email=instance.email)