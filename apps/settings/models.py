from django.db import models

from apps.item.models import Item
from apps.room.models import RoomType


class Hotel(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('hotel', 'Hotel'),
        ('motel', 'Motel'),
        ('resort', 'Resort'),
        ('guesthouse', 'Guest House'),
        ('bed_breakfast', 'Bed and Breakfast'),
        ('apartment', 'Apartment'),
        ('villa', 'Villa'),
        ('cottage', 'Cottage'),
        ('hostel', 'Hostel'),
        ('inn', 'Inn'),
    ]
    property_name = models.CharField(max_length=255, help_text='Property name')
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPE_CHOICES, help_text='Property type')
    property_description = models.TextField(help_text='Property description')
    property_primary_language = models.CharField(max_length=255, help_text='Property primary language')
    property_phone = models.CharField(max_length=20, help_text='Property phone number')
    property_email = models.EmailField(help_text='Property main email address')
    property_website = models.URLField(max_length=200, help_text='Property website URL', blank=True)
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


class HotelPhoto(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_photos')
    photo = models.ImageField(upload_to='hotel_photos')


class GuestStatus(models.Model):
    name = models.CharField(max_length=255, help_text='Guest status')
    description = models.TextField(help_text='Guest status description')
    guests = models.ManyToManyField('app.Guest', blank=True)
    is_active = models.BooleanField(default=True, help_text='Guest status is active')

    def __str__(self):
        return self.name


class AddOn(models.Model):
    name = models.CharField(max_length=255, help_text='This will be displayed on the booking engine mybookings')
    inventory_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    CHARGE_TYPES = [
        ('reservation', 'Per Reservation'),
        ('night', 'Per Night'),
        ('room_bed', 'Per Room/Bed'),
        ('room_bed_night', 'Per Room/Bed Per Night'),
        ('guest', 'Per Guest'),
        ('guest_night', 'Per Guest Per Night'),
        ('quantity', 'Per Quantity'),
    ]
    charge_type = models.CharField(max_length=20, choices=CHARGE_TYPES, help_text='Select the type of charge')
    transaction_code = models.CharField(max_length=255, blank=True, null=True,
                                        help_text='Internal transaction code (optional)')
    availability_choices = [
        ('arrival', 'Arrival'),
        ('departure', 'Departure'),
        ('both', 'Both Arrival and Departure'),
        ('na', 'Not Applicable'),
    ]
    availability = models.CharField(max_length=20, choices=availability_choices,
                                    help_text='Select when the add-on will be available')
    post_choices = [
        ('immediate', 'Immediately when receiving the reservation'),
        ('checkin', 'When checking-in the reservation'),
        ('daily', 'Post Add-On daily'),
    ]
    post_transaction = models.CharField(max_length=20, choices=post_choices,
                                        help_text='Select when the transaction should be posted')
    keep_posted_on_cancellation = models.BooleanField(default=True,
                                                      help_text='Choose whether to keep or void the transaction on cancellation/no show')
    calculate_revenue_choices = [
        ('proportional', 'Adjust its price proportionally to the other package inclusions'),
        ('full_price', 'Calculate based on the full price'),
    ]
    calculate_revenue = models.CharField(max_length=20, choices=calculate_revenue_choices,
                                         help_text='Choose how add-on values will be calculated for revenue allocation')
    image = models.ImageField(upload_to='add_ons', null=True, blank=True,
                              help_text='Upload an image (recommended: 150px x 75px)')

    def __str__(self):
        return self.name


class AddOnInterval(models.Model):
    add_on = models.ForeignKey(AddOn, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, help_text='Interval name (internal only)')
    start_date = models.DateField(help_text='Set the start date of the interval')
    end_date = models.DateField(help_text='Set the end date of the interval')
    min_overlap = models.PositiveIntegerField(
        help_text='Set the minimum number of consecutive reservation days the add-on must be available')
    max_overlap = models.PositiveIntegerField(
        help_text='Set the maximum number of consecutive reservation days the add-on must be available')
    room_types = models.ManyToManyField(RoomType,
                                        help_text='Select the room types for which this add-on will be available')
    monday_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
                                       help_text='Enter the price for Monday')
    tuesday_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
                                        help_text='Enter the price for Tuesday')
    wednesday_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
                                          help_text='Enter the price for Wednesday')
    thursday_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
                                         help_text='Enter the price for Thursday')
    friday_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
                                       help_text='Enter the price for Friday')
    saturday_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
                                         help_text='Enter the price for Saturday')
    sunday_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
                                       help_text='Enter the price for Sunday')

    def __str__(self):
        return f"Interval for {self.add_on.name}"
