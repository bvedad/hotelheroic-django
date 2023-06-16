# Generated by Django 3.2.6 on 2023-06-15 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_hotelphoto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='property_image',
        ),
        migrations.AddField(
            model_name='hotel',
            name='property_images',
            field=models.ManyToManyField(help_text='Property images', related_name='hotels', to='settings.HotelPhoto'),
        ),
    ]
