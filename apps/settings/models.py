from django.db import models


class Hotel(models.Model):
    property_name = models.CharField(max_length=255, help_text='Property name')
    property_image = models.ImageField(upload_to='property_images')
    property_description = models.TextField(help_text='Property description')
    property_primary_language = models.CharField(max_length=255, help_text='Property primary language')
    property_phone = models.CharField(max_length=20, help_text='Property phone number')
    property_email = models.EmailField(help_text='Property main email address')
    # Property address
    property_address1 = models.CharField(max_length=255, help_text='Property address line 1')
    property_address2 = models.CharField(max_length=255, help_text='Property address line 2')
    property_city = models.CharField(max_length=255, help_text='Property city')
    property_state = models.CharField(max_length=255, help_text='Property state')
    property_zip = models.CharField(max_length=20, help_text='Property ZIP code')
    property_country = models.CharField(max_length=255, help_text='Property country')
    property_latitude = models.CharField(max_length=255, help_text='Property latitude')
    property_longitude = models.CharField(max_length=255, help_text='Property longitude')
    # Property policy
    property_check_in_time = models.TimeField(help_text='Property check-in time')
    property_check_out_time = models.TimeField(help_text='Property check-out time')
    property_late_check_out_allowed = models.BooleanField(help_text='Property allows late check-out')
    property_late_check_out_type = models.CharField(max_length=50, choices=[('value', 'Value'), ('percent', 'Percent')],
                                                    help_text='If the property accepts late check-out, defines if the value is fixed, or a percentage of the daily rate')
    property_late_check_out_value = models.FloatField(
        help_text='The fixed value, or percentage of the daily rate, to be charged on a late check-out')
    property_terms_and_conditions = models.TextField(
        help_text='Text describing the terms and conditions to be displayed to guest')

    def __str__(self):
        return self.property_name
