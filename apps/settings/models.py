from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from timezone_field import TimeZoneField

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


class SystemSettings(models.Model):
    # General Settings
    APPLICATION_LANGUAGES = [
        ('en', 'English'),
        ('bs', 'Bosnian'),
        # Add more language options here
    ]

    APPLICATION_DATE_FORMATS = [
        ('d/m/Y', 'DD/MM/YYYY'),
        ('Y-m-d', 'YYYY-MM-DD'),
        ('m/d/Y', 'MM/DD/YYYY'),
    ]

    APPLICATION_TIME_FORMATS = [
        ('H:i', '24-hour format'),
        ('h:i A', '12-hour format'),
    ]

    APPLICATION_CURRENCIES = [
        ('EUR', 'Euro'),
        ('USD', 'US Dollar'),
    ]

    application_language = models.CharField(
        max_length=2,
        choices=APPLICATION_LANGUAGES,
        default='en',
        help_text='Select the default language for your property. New user accounts will have this language.',
    )

    application_date_format = models.CharField(
        max_length=10,
        choices=APPLICATION_DATE_FORMATS,
        default='d/m/Y',
        help_text='Select the format in which the date is shown on HotelHeroic PMS.',
    )

    application_time_format = models.CharField(
        max_length=6,
        choices=APPLICATION_TIME_FORMATS,
        default='H:i',
        help_text='Select the format in which the time is shown on HotelHeroic PMS.',
    )

    property_time_zone = TimeZoneField(
        help_text='The time zone of your property.',
        default='Europe/Sarajevo',
    )

    # application_currency_format = models.CharField(
    #     max_length=10,
    #     choices=APPLICATION_CURRENCY_FORMATS,
    #     help_text='Select the format in which the currency is shown on Cloudbeds PMS.',
    # )

    application_currency = models.CharField(
        max_length=50,
        choices=APPLICATION_CURRENCIES,
        default='EUR',
        help_text='The main currency on Cloudbeds PMS.',
    )

    # Automation Preferences
    allow_additional_bookings = models.BooleanField(
        default=False,
        help_text='Enabling this will open availability when your property is at no less than 100% occupancy.'
    )

    auto_change_no_show = models.BooleanField(
        default=True,
        help_text='When a guest does not show up the next day after the arrival date by 2:05 AM, the system will automatically change the status of the reservation to "No Show".'
    )

    auto_checkout_date_extension = models.BooleanField(
        default=True,
        help_text='When a guest does not manually check out until 2:05 AM the next day, the system will automatically extend the reservation date.'
    )

    auto_assign_reservations = models.BooleanField(
        default=False,
        help_text='If enabled, all new reservations will be auto-assigned to the first available accommodation within that room type.'
    )

    use_default_country_for_guest = models.BooleanField(
        default=False,
        help_text='When turned on, the country field in guest details will be pre-filled with your property\'s country.'
    )

    allow_same_day_bookings = models.BooleanField(
        default=False,
        help_text='If enabled, guests will be allowed to book same-day arrivals.'
    )

    same_day_bookings_until = models.TimeField(
        null=True,
        blank=True,
        help_text='Specify until what time the guest is allowed to book for the same-day arrival.'
    )

    # MiscellaneousPreferences
    CUSTOMER_NAME_FORMAT_CHOICES = [
        ('SURNAME_NAME', 'Surname Name'),
        ('NAME_SURNAME', 'Name Surname'),
    ]
    show_estimated_arrival_time = models.BooleanField(
        default=False,
        help_text='Gives you the option to fill in the guest\'s estimated arrival time when creating direct reservations.'
    )

    show_checkouts_in_departure_list = models.BooleanField(
        default=True,
        help_text='If enabled, the property can see guests who have already checked out in their dashboard\'s Departure List.'
    )

    enable_gdpr_compliance = models.BooleanField(
        default=False,
        help_text='If enabled, tools to comply with GDPR such as Guest Data Extraction, Anonymization, and Marketing Opt-In will be available to your property.'
    )

    customer_name_format = models.CharField(
        max_length=50,
        choices=CUSTOMER_NAME_FORMAT_CHOICES,
        default='SURNAME_NAME',
        help_text='Specifies how the customer name is displayed in the calendar.'
    )

    enable_payment_allocation = models.BooleanField(
        default=False,
        help_text='Enabling payment allocation allows users to specify exactly which charge a payment is for.'
    )

    breakfast_included_channel_distribution = models.BooleanField(
        default=False,
        help_text='Tells channels (OTAs) if breakfast pricing is included in your nightly rates.'
    )

    require_full_payment_prior_to_check_in = models.BooleanField(
        default=False,
        help_text='If enabled, reservations with a remaining balance cannot be checked-in until full payment is collected.'
    )


class DepositPolicy(models.Model):
    DEPOSIT_TYPES = [
        ('percentage', 'Percentage'),
        ('fixed_amount', 'Fixed Amount'),
        ('first_day_price', 'First Day Price'),
        ('no_deposit', 'Do not collect deposit'),
    ]

    deposit_type = models.CharField(
        max_length=15,
        choices=DEPOSIT_TYPES,
        default='percentage',
        help_text='Select the type of deposit for your guests.',
    )

    deposit_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True,
        help_text='Specify the required deposit percentage (%).',
    )

    deposit_fixed_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        help_text='Specify the fixed amount that will be charged per accommodation per night.',
    )

    include_taxes_fees = models.BooleanField(
        default=False,
        help_text='Specify whether taxes and fees will be included as part of the deposit.',
    )

    capture_credit_card = models.BooleanField(
        default=False,
        help_text='Select if you would like to capture the guest credit card details to keep on file.',
    )

    def __str__(self):
        return self.deposit_type

    def clean(self):
        if self.deposit_type == 'percentage' and not self.deposit_percentage:
            raise ValidationError({'deposit_percentage': 'This field is required for percentage deposit type.'})
        elif self.deposit_type == 'fixed_amount' and not self.deposit_fixed_amount:
            raise ValidationError({'deposit_fixed_amount': 'This field is required for fixed amount deposit type.'})


class CancellationPolicy(models.Model):
    POLICY_TYPES = [
        ('full_charge', 'Full Charge'),
        ('partial_charge', 'Partial Charge'),
        ('no_charge', 'No Charge'),
    ]
    TYPE_CHOICES = [
        ('full_deposit', 'Full Deposit'),
        ('full_stay', 'Full Stay'),
    ]

    policy_type = models.CharField(max_length=20, choices=POLICY_TYPES)
    charge_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    days_before_arrival = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.get_policy_type_display()} - {self.get_charge_type_display()}"

    class Meta:
        verbose_name_plural = 'Cancellation Policies'


class GeneralCancellationPolicy(models.Model):
    POLICY_CHOICES = [
        ('standardized', 'Use standardized cancellation policy'),
        ('custom', 'Enter my own custom text policy'),
    ]

    policy_type = models.CharField(
        max_length=20,
        choices=POLICY_CHOICES,
        default='standardized',
        help_text='Select the cancellation policy type.'
    )
    custom_content = models.TextField(
        blank=True,
        null=True,
        help_text='Enter your own custom text cancellation policy.',
    )

    def clean(self):
        if self.policy_type == 'custom' and not self.custom_content:
            raise ValidationError('Custom content is required for the selected policy type.')

    def __str__(self):
        return self.get_policy_type_display()

    class Meta:
        verbose_name_plural = 'General Cancellation Policies'


class TermsAndConditions(models.Model):
    language = models.CharField(
        max_length=2,
        choices=SystemSettings.APPLICATION_LANGUAGES,
        default='en',
        help_text='Choose the language for your terms and conditions.',
    )

    content = RichTextField(
        help_text='Enter your terms and conditions. Apply format if needed.',
    )

    class Meta:
        verbose_name_plural = 'Terms and Conditions'

    def __str__(self):
        return self.language


class ArrivalAndDeparture(models.Model):
    check_in_time = models.TimeField(help_text='Set the check-in time for your property.')
    check_out_time = models.TimeField(help_text='Set the check-out time for your property.')
    late_check_out_allowed = models.BooleanField(default=False,
                                                 help_text='Specify whether you offer a late check-out option.')

    late_check_out_time = models.TimeField(
        null=True,
        blank=True,
        help_text='Set the preferred late check-out time for guests.'
    )

    LATE_CHECK_OUT_CHOICES = [
        ('percentage', 'Percentage'),
        ('fixed', 'Fixed'),
    ]
    late_check_out_charge_type = models.CharField(
        max_length=10,
        choices=LATE_CHECK_OUT_CHOICES,
        blank=True,
        help_text='Choose the type of charge for late check-out.'
    )

    late_check_out_charge_amount = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0.00,
        help_text='Set the amount for the late check-out charge.'
    )


class ConfirmationPending(models.Model):
    CONFIRMATION_STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('confirmation_pending', 'Confirmation Pending'),
    ]
    default_confirmation_status = models.CharField(
        max_length=20,
        choices=CONFIRMATION_STATUS_CHOICES,
        default='confirmed',
        help_text='Select your preferred default confirmation status for new reservations.'
    )


class InvoiceDetails(models.Model):
    company_logo = models.ImageField(
        upload_to='company_logo',
        help_text='Upload your company logo. Recommended size: 100x100 pixels.',
    )
    invoice_title = models.CharField(
        max_length=100,
        help_text='Specify the title to be used for the invoice.',
    )
    invoice_prefix = models.CharField(
        max_length=50,
        help_text='Enter any numbers or letters to appear before the sequentially generated invoice number.',
    )
    starting_index_number = models.PositiveIntegerField(
        help_text='Specify the number of the first invoice that gets generated. The subsequent invoices will be sequential.',
    )
    invoice_suffix = models.CharField(
        max_length=50,
        help_text='Enter any numbers or letters to appear after the sequentially generated invoice number.',
    )
    include_company_details = models.BooleanField(
        default=True,
        help_text='Include your Legal Company Name and Tax ID Number in the invoice.',
    )
    custom_fields = models.TextField(
        blank=True,
        help_text='Add any additional text to the invoice, such as payment instructions or policies.',
    )
    credit_note_same_sequence = models.BooleanField(
        default=True,
        help_text='Use the same numbering sequence for credit notes as invoices.',
    )
    credit_note_title = models.CharField(
        max_length=100,
        blank=True,
        help_text='Specify the title to be used for credit notes.',
    )
    credit_note_prefix = models.CharField(
        max_length=50,
        blank=True,
        help_text='Enter any numbers or letters to appear before the sequentially generated credit note number.',
    )
    credit_note_starting_index_number = models.PositiveIntegerField(
        blank=True,
        help_text='Specify the number of the first credit note that gets generated.',
    )
    credit_note_suffix = models.CharField(
        max_length=50,
        blank=True,
        help_text='Enter any numbers or letters to appear after the sequentially generated credit note number.',
    )


class InvoiceSettings(models.Model):
    default_language = models.CharField(
        max_length=50,
        help_text='Select the default language for the invoice.',
    )
    generate_invoice_based_on_country = models.BooleanField(
        default=False,
        help_text='Generate the invoice based on the country the guest is from.',
    )
    generate_invoice_option = models.CharField(
        max_length=20,
        choices=[
            ('reservation_creation', 'At reservation creation'),
            ('check_out', 'At check-out'),
            ('manual', 'Manually'),
        ],
        default='manual',
        help_text='Select when to generate the invoice.',
    )
    default_due_date = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text='Specify the number of days the guest has to pay the invoice from the time it is generated.',
    )
    show_room_number_column = models.BooleanField(
        default=False,
        help_text='Show the room number column on the invoice.',
    )
    show_tax_specifics = models.BooleanField(
        default=False,
        help_text='Show the breakdown of each tax/fee type on the invoice.',
    )
    use_compact_invoices = models.BooleanField(
        default=False,
        help_text='Consolidate common transactions into their own line on the invoice.',
    )


User = get_user_model()


class SystemNotification(models.Model):
    NOTIFICATION_CHOICES = [
        ('new_reservation', 'New Reservation Received'),
        ('reservation_cancelled', 'Reservation Cancelled'),
        ('reservation_modified', 'Reservation Modified (modification from OTA)'),
        ('reservation_unmapped', 'Modification to Reservation with Unmapped Rooms'),
        ('no_show_reported', 'No Shows Auto-Reported to Booking.com'),
        ('payment_success', 'Payment processed successfully'),
        ('payment_failure', 'Unable to process payment'),
        ('chargeback', 'Chargeback Notifications / Resolutions'),
        ('drawer_closure', 'Drawer Closure Summary Notifications'),
    ]

    notification_type = models.CharField(
        max_length=50,
        choices=NOTIFICATION_CHOICES,
        unique=True,
        help_text='Select the type of system notification.'
    )
    recipients = models.ManyToManyField(
        User,
        related_name='system_notifications',
        help_text='Select the recipients for this notification type.',
        blank=True
    )

    is_active = models.BooleanField(default=True)
    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
        related_name='system_notifications',
        help_text='Select the hotel for this notification type.'
    )

    def __str__(self):
        return dict(self.NOTIFICATION_CHOICES).get(self.notification_type, '')


class CreditCard(models.Model):
    CARD_TYPE_CHOICES = [
        ('VISA', 'Visa'),
        ('MASTERCARD', 'Mastercard'),
        ('AMEX', 'American Express'),
        ('DISCOVER', 'Discover'),
    ]

    card_type = models.CharField(max_length=50, choices=CARD_TYPE_CHOICES, unique=True)
    accepted_for_direct_reservations = models.BooleanField(default=False)
    accepted_for_mybookings = models.BooleanField(default=False)


class BankTransfer(models.Model):
    active = models.BooleanField(
        default=False,
        help_text='Switch to activate or deactivate Bank Transfer as a payment option for your property.'
    )
    direct_reservations_allowed = models.BooleanField(
        default=False,
        help_text='Allow Bank Transfer as a payment option for direct/dashboard reservations.'
    )
    booking_engine_allowed = models.BooleanField(
        default=False,
        help_text='Allow Bank Transfer as a payment option for bookings made through the Mybookings Booking Engine.'
    )
    bank_name = models.CharField(
        max_length=100,
        help_text='Enter the name of your bank.'
    )
    bank_address = models.TextField(
        help_text='Enter the address of your bank.'
    )
    property_address = models.TextField(
        help_text='Enter the address of your property where bank transfer details should be listed.'
    )
    instructions = RichTextField(
        help_text='Instructions for completing the transfer.'
    )

    def __str__(self):
        return 'Bank Transfer Payment Option'


class PayPal(models.Model):
    active = models.BooleanField(
        default=False,
        help_text='Switch to activate or deactivate PayPal as a payment option for your guests.'
    )
    email_address = models.EmailField(
        verbose_name='Email Address',
        help_text='Enter the email address associated with your PayPal account.'
    )
    identity_token = models.CharField(
        max_length=100,
        blank=True,
        help_text='Enter the PayPal Identity Token, if necessary.'
    )
    first_name = models.CharField(
        max_length=100,
        verbose_name='First Name',
        help_text='Enter the first name of the person the PayPal account is registered under.'
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='Last Name',
        help_text='Enter the last name of the person the PayPal account is registered under.'
    )

    def __str__(self):
        return 'PayPal Payment Option'


class CustomPaymentMethod(models.Model):
    label = models.CharField(
        max_length=100,
        unique=True,
        help_text='Enter the label/name for your custom payment method.'
    )
    active = models.BooleanField(
        default=True,
        help_text='Switch to activate or deactivate the custom payment method.'
    )

    def __str__(self):
        return self.label


class BookingEngineSettings(models.Model):
    GALLERY_DISPLAY_OPTIONS = [
        ('lowest_price', 'Show Lowest Sales Price'),
        ('accommodation_total', 'Show Accommodation Total Price for Stay')
    ]

    ACCOMMODATION_BOOKING_OPTIONS = [
        ('specific', 'Allow guests to book specific accommodations'),
        ('general', 'General booking for the selected room type')
    ]

    gallery_display_option = models.CharField(max_length=20, choices=GALLERY_DISPLAY_OPTIONS,
                                              default='accommodation_total',
                                              help_text='Select the option for displaying prices in the gallery design.')
    room_types = models.ManyToManyField(RoomType)

    hide_map = models.BooleanField(default=False, help_text='Hide the map on the booking page.')
    opt_in_to_marketing = models.BooleanField(default=False,
                                              help_text='Allow guests to opt-in to marketing emails during the booking process.')
    marketing_content = models.TextField(blank=True, null=True,
                                         help_text='Additional content explaining the marketing emails.')
    opt_in_option = models.CharField(max_length=100, blank=True,
                                     help_text='Text explaining the opt-in marketing option.')
    opt_out_option = models.CharField(max_length=100, blank=True,
                                      help_text='Text explaining the opt-out marketing option.')
    accommodation_booking_option = models.CharField(max_length=20, choices=ACCOMMODATION_BOOKING_OPTIONS,
                                                    default='general',
                                                    help_text='Select the option for accommodation booking.')
    ask_postal_address = models.BooleanField(default=False, help_text='Ask for a postal address.')
    ask_nationality = models.BooleanField(default=False, help_text='Ask for nationality.')
    ask_gender = models.BooleanField(default=False, help_text='Ask for gender.')
    ask_personal_tax_id = models.BooleanField(default=False, help_text='Ask for personal tax ID number.')
    ask_company_name = models.BooleanField(default=False, help_text='Ask for company name.')
    ask_company_tax_id = models.BooleanField(default=False, help_text='Ask for company tax ID name.')
    require_telephone_number = models.BooleanField(default=False, help_text='Require telephone number to book.')
    ask_estimated_arrival_time = models.BooleanField(default=False,
                                                     help_text='Ask for estimated arrival time during booking.')
    require_terms_conditions = models.BooleanField(default=False,
                                                   help_text='Require acceptance of terms and conditions.')
    confirmation_email = models.BooleanField(default=False,
                                             help_text='Send an automatic confirmation email to the guest.')
    redirect_on_confirmation = models.BooleanField(default=False,
                                                   help_text='Redirect guests to a custom URL after completing the booking.')
    redirect_url = models.URLField(blank=True, null=True,
                                   help_text='URL to redirect guests after completing the booking.')
    # allotment_enabled = models.BooleanField(default=False,
    #                                         help_text='Enable allotment to limit the number of rooms available.')
    limit_same_type_accommodations = models.PositiveIntegerField(default=0,
                                                                 help_text='Limit the number of rooms bookable in one reservation.')
    ask_cvv_code = models.BooleanField(default=False, help_text='Ask for CVV code for credit card payments.')

    # language_options = models.ManyToManyField(Language,
    #                                           help_text='Select languages to appear on the booking engine.')

    def __str__(self):
        return f'{self.room_type} - Booking Engine Settings'

    class Meta:
        verbose_name_plural = 'Booking Engine Settings'

    def clean(self):
        if self.redirect_on_confirmation and not self.redirect_url:
            raise ValidationError(
                {'redirect_url': 'Redirect URL is required when redirect_on_confirmation is enabled.'})
