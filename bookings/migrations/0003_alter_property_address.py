# Generated by Django 4.1.7 on 2023-02-20 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_alter_contact_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='address',
            field=models.OneToOneField(blank=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='bookings.address'),
        ),
    ]
