# Generated by Django 4.1.7 on 2023-02-21 01:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bookings', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cart',
            name='guest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cart_guests', to='bookings.contact'),
        ),
        migrations.AddField(
            model_name='cart',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cart_host', to='bookings.contact'),
        ),
        migrations.AddField(
            model_name='cart',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookings.property'),
        ),
        migrations.AddField(
            model_name='booking',
            name='guest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='booking_guests', to='bookings.contact'),
        ),
        migrations.AddField(
            model_name='booking',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='booking_host', to='bookings.contact'),
        ),
        migrations.AddField(
            model_name='booking',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookings.property'),
        ),
    ]
