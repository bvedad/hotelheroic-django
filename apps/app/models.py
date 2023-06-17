from django.db import models
from django.db.models import ForeignKey
# Create your models here.
from apps.reservation.models import Reservation
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError


class Adjustment(models.Model):
    ADJUSTMENT_CHOICES = [
        ('rate', 'Rate'),
        ('product', 'Product'),
        ('fee', 'Fee'),
        ('tax', 'Tax'),
    ]

    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    adjustment_type = models.CharField(max_length=50, choices=ADJUSTMENT_CHOICES)
    amount = models.FloatField()
    notes = models.CharField(max_length=255, blank=True)
    # TODO item_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CurrencySettings(models.Model):
    default_currency = models.CharField(max_length=3, help_text="Default Currency ISO CODE")
    acceptable_currencies = models.JSONField(help_text="Acceptable Currency ISO CODEs")
    decimal_separator = models.CharField(max_length=1)
    thousand_separator = models.CharField(max_length=1)


class CurrencySettingsRate(models.Model):
    currency_settings = models.ForeignKey(CurrencySettings, on_delete=models.CASCADE, related_name='rates')
    currency = models.CharField(max_length=3, help_text="Currency ISO CODE")
    rate = models.FloatField()


class CustomField(models.Model):
    APPLY_CHOICES = [
        ('reservation', 'Reservation'),
        ('guest', 'Guest'),
    ]

    TYPE_CHOICES = [
        ('input', 'Input'),
        ('text', 'Text'),
    ]

    name = models.CharField(max_length=255)
    shortcode = models.CharField(max_length=255,
                                 help_text="Internal reference and is used for integration purposes such as custom links and the API")
    apply_to = models.CharField(max_length=50, choices=APPLY_CHOICES, default='reservation',
                                help_text="Where put this field in reservation or guest section of the booking.")
    required = models.BooleanField(default=False, help_text="Specify whether this field is required to be filled out.")
    max_characters = models.IntegerField(default=40,
                                         help_text="Maximum number of characters allowed to be entered in this field.")
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='input')
    displayed_in_reservation = models.BooleanField(default=True)
    displayed_in_booking = models.BooleanField(default=True)
    displayed_in_card = models.BooleanField(default=True)
    is_personal = models.BooleanField(
        help_text="Specifies if the contents of this field may contain personal information. User's personal information may be removed upon request according to GDPR rules.")


class EmailSchedule(models.Model):
    RESERVATION_STATUS_CHANGE_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('not_confirmed', 'Not confirmed'),
        ('canceled', 'Canceled'),
        ('checked_in', 'Checked in'),
        ('checked_out', 'Checked out'),
        ('no_show', 'No show'),
    ]
    RESERVATION_EVENT_CHOICES = [
        ('after_booking', 'After booking'),
        ('after_check_out', 'After check out'),
        ('after_check_in', 'After check in'),
        ('before_check_out', 'Before check out'),
        ('before_check_in', 'Before check in'),
    ]

    email_template = ForeignKey('EmailTemplate', on_delete=models.CASCADE)
    schedule_name = models.CharField(max_length=255)
    reservation_status_change = models.CharField(
        max_length=50,
        choices=RESERVATION_STATUS_CHANGE_CHOICES,
        null=True,
        blank=True,
        help_text="Specify which reservation status change triggers sending the email"
    )
    reservation_event = models.CharField(
        max_length=50,
        choices=RESERVATION_EVENT_CHOICES,
        null=True,
        blank=True,
        help_text="Specify event that triggers email sending"
    )
    days = models.IntegerField()
    time = models.TimeField()

    def __str__(self):
        return self.schedule_name


class EmailTemplate(models.Model):
    email_type = models.CharField(max_length=50, default='nonMarketing',
                                  choices=[('nonMarketing', 'Non-Marketing'), ('marketing', 'Marketing')],
                                  help_text="Type of the email template: Marketing or Non-Marketing. Only applicable to GDPR compliant properties.")
    name = models.CharField(max_length=255, help_text="Template name")
    from_email = models.EmailField(help_text="Email address from which the email message may be sent")
    from_name = models.CharField(max_length=255,
                                 help_text="Name from which the email message may be sent. If empty email will be used")
    subject = models.TextField()
    body = models.TextField()
    reply_to = models.EmailField(blank=True, null=True,
                                 help_text="Email address to which the email message may be replied. If empty, the value on from parameter will be used.")
    reply_to_name = models.CharField(max_length=255, blank=True, null=True,
                                     help_text="Name to which the email message may be replied. If empty, email will be used.")
    autofill_all_languages = models.BooleanField(default=False,
                                                 help_text="If set, all languages will be set with the value for the property language. If not informed and only one language is sent, it's considered true, if more than one language is sent, it'll be considered false.")
    cc = models.EmailField(blank=True, null=True,
                           help_text="Email address to which the email message may be sent as a Carbon Copy")
    bcc = models.EmailField(blank=True, null=True,
                            help_text="Email address to which the email message may be sent as a Blind Carbon Copy")

    def __str__(self):
        return self.name


class Guest(models.Model):
    GENDER_CHOICES = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('NOT_AVAILABLE', 'Not Available'),
    ]

    DOCUMENT_TYPE_CHOICES = [
        ('IDENTITY_CARD', 'Identity Card'),
        ('DRIVER_LICENSE', 'Driver License'),
        ('NON_SELECTION', 'Non Selection'),
        ('RESIDENCE_PERMIT', 'Residence Permit'),
        ('PASSPORT', 'Passport'),
        ('SOCIAL_SECURITY_CARD', 'Social Security Card'),
        ('STUDENT_ID', 'Student ID'),
    ]

    reservation = models.ForeignKey('reservation.Reservation', on_delete=models.CASCADE)
    guest_first_name = models.CharField(max_length=255)
    guest_last_name = models.CharField(max_length=255)
    guest_email = models.EmailField(max_length=255)
    is_main_guest = models.BooleanField(default=False, help_text="If the guest is the main guest of its reservation")
    is_anonymized = models.BooleanField(default=False,
                                        help_text="Flag indicating the guest data was removed upon request")
    guest_gender = models.CharField(max_length=50, choices=GENDER_CHOICES, blank=True, null=True)
    guest_phone = models.CharField(max_length=255, blank=True, null=True)
    guest_cell_phone = models.CharField(max_length=255, blank=True, null=True)
    guest_address1 = models.CharField(max_length=255, blank=True, null=True)
    guest_address2 = models.CharField(max_length=255, blank=True, null=True)
    guest_city = models.CharField(max_length=255, blank=True, null=True)
    guest_state = models.CharField(max_length=255, blank=True, null=True)
    guest_country = models.CharField(max_length=2, blank=True, null=True,
                                     help_text="ISO-Code for Country (2 characters)")
    guest_zip = models.CharField(max_length=255, blank=True, null=True)
    guest_birth_date = models.DateField(blank=True, null=True)
    guest_document_type = models.CharField(max_length=50, choices=DOCUMENT_TYPE_CHOICES, blank=True, null=True)
    guest_document_number = models.CharField(max_length=255, blank=True, null=True)
    guest_document_issue_date = models.DateField(blank=True, null=True)
    guest_document_issuing_country = models.CharField(max_length=2, blank=True, null=True,
                                                      help_text="Valid ISO-Code for Country (2 characters)")
    guest_document_expiration_date = models.DateField(blank=True, null=True)
    # guest_tax_id = models.CharField(max_length=255, blank=True, null=True, help_text="Guest tax ID")
    guest_company_tax_id = models.CharField(max_length=255, blank=True, null=True, help_text="Guest company tax ID")
    guest_company_name = models.CharField(max_length=255, blank=True, null=True, help_text="Guest company name")
    guest_opt_in = models.BooleanField(default=False,
                                       help_text="If guest has opted-in to marketing communication or not")
    guest_photo = models.ImageField(upload_to='guest_photos', blank=True, null=True)
    guest_document = models.FileField(upload_to='documents/', validators=[FileExtensionValidator(
        ['pdf', 'rtf', 'doc', 'docx', 'txt', 'jpg', 'jpeg', 'png', 'gif', 'csv', 'xls', 'xlsx'])], blank=True,
                                      null=True)

    def clean(self):
        file = self.guest_document
        if file:
            if file.size > 100 * 1024 * 1024:
                raise ValidationError("File size must not exceed 100MB.")
        super().clean()


class GuestNote(models.Model):
    guest = models.ForeignKey('app.Guest', on_delete=models.CASCADE)
    note = models.TextField(blank=True, null=True)


class Currency(models.Model):
    CURRENCY_POSITION_CHOICES = [
        ('BEFORE', 'Before'),
        ('AFTER', 'After'),
    ]
    currency_code = models.CharField(max_length=3, help_text='Currency code')
    currency_name = models.CharField(max_length=255, help_text='Currency name')
    currency_symbol = models.CharField(max_length=255, help_text='Currency symbol')
    currency_position = models.CharField(max_length=50, choices=CURRENCY_POSITION_CHOICES, )
    hotel = models.ForeignKey('settings.Hotel', on_delete=models.CASCADE)


class PropertyImage(models.Model):
    thumb = models.ImageField(upload_to='property_images', help_text='Thumbnail Image')
    image = models.ImageField(upload_to='property_images', help_text='Full Image')
    hotel = models.ForeignKey('settings.Hotel', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.image)


class HotelAmenity(models.Model):
    CATEGORY_CHOICES = [
        ('CHECK_IN_FRONT_DESK_SERVICES', 'Check-in & Front-Desk Services'),
        ('GENERAL_GUEST_SERVICES', 'General Guest Services'),
        ('POOL_SPA_WELLNESS', 'Pool, Spa, & Wellness'),
        ('ENTERTAINMENT_RECREATION', 'Entertainment & Recreation'),
        ('FOOD_BEVERAGE', 'Food & Beverage'),
        ('PARKING_TRANSPORTATION', 'Parking & Transportation'),
        ('FAMILY_SERVICES_ACTIVITIES', 'Family Services & Activities'),
        ('COMMON_AREAS', 'Common Areas'),
        ('CLEANING_SERVICES', 'Cleaning Services'),
        ('BUSINESS_SERVICES', 'Business Services'),
        ('SHOPPING', 'Shopping'),
        ('ACCESSIBILITY', 'Accessibility'),
        ('SAFETY_SECURITY', 'Safety & Security'),
        ('ENVIRONMENT_SUSTAINABILITY', 'Environment & Sustainability'),
        ('SANITATION_HYGIENE_GUEST_HEALTH', 'Sanitation, Hygiene, & Guest Health'),
        ('CUSTOM_AMENITY', 'Custom Amenity'),
    ]

    name = models.CharField(max_length=255, help_text='Amenity name')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, help_text='Amenity category')
    hotel = models.ForeignKey('settings.Hotel', on_delete=models.CASCADE, related_name='amenities')
    is_active = models.BooleanField(default=True, help_text='Whether amenity is active or not')

    def __str__(self):
        return self.name


class HouseAccount(models.Model):
    account_name = models.CharField(max_length=255, help_text='House Account name')
    is_private = models.BooleanField(default=False,
                                     help_text='Whether House Account is available only to the user (optional)')

    class Meta:
        verbose_name_plural = 'House Accounts'

    def __str__(self):
        return self.account_name


class Housekeeper(models.Model):
    name = models.CharField(max_length=255, help_text='Housekeeper name')


class HousekeepingAssignment(models.Model):
    room = models.ForeignKey('room.Room', on_delete=models.CASCADE)
    housekeeper = models.ForeignKey('app.Housekeeper', on_delete=models.CASCADE)


class HousekeepingStatus(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey('room.Room', on_delete=models.CASCADE)
    room_condition = models.CharField(max_length=50, choices=[('CLEAN', 'Clean'), ('DIRTY', 'Dirty')], blank=True,
                                      null=True)
    do_not_disturb = models.BooleanField(default=False)
