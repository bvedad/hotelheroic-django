from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models


class Reservation(models.Model):
    source_id = models.IntegerField(
        null=True,
        blank=True,
        help_text='The third-party source ID for this reservation.'
    )
    third_party_identifier = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text='If it was received from a booking channel, this can be an identifier from that channel.'
    )
    start_date = models.DateField(
        help_text='Check-In date.'
    )
    end_date = models.DateField(
        help_text='Check-Out date.'
    )
    guest_first_name = models.CharField(
        max_length=255,
        help_text='First name of the guest'
    )
    guest_last_name = models.CharField(
        max_length=255,
        help_text='Last name of the guest'
    )
    guest_gender = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        choices=[
            ('M', 'Male'),
            ('F', 'Female'),
            ('N/A', 'Not Applicable'),
        ],
        help_text="Allowed values: 'M' (Male), 'F' (Female), 'N/A' (Not Applicable)"
    )
    guest_country = models.CharField(
        max_length=2,
        help_text='Valid ISO-Code for Country (2 characters)'
    )
    guest_zip = models.CharField(
        max_length=255,
        help_text='ZIP Code'
    )
    guest_email = models.CharField(
        max_length=255,
        help_text='Guest email'
    )
    guest_phone = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text='Guest main phone number'
    )
    estimated_arrival_time = models.TimeField(
        null=True,
        blank=True,
        help_text='Estimated Arrival Time, 24-hour format.'
    )
    rooms = models.ManyToManyField('room.Room', help_text='Array with quantity of rooms')
    # adults = models.JSONField(
    #     help_text='Array with number of adults'
    # )
    adults = models.IntegerField()
    # children = models.JSONField(
    #     help_text='Array with number of children'
    # )
    children = models.IntegerField()
    payment_method = models.CharField(
        max_length=50,
        choices=(
            ("cash", "Cash"),
            ("credit", "Credit"),
            ("ebanking", "EBanking"),
            ("pay_pal", "PayPal"),
        ),
        help_text='Payment Method of choice. Allowed values: "cash", "credit", "ebanking", "pay_pal"'
    )
    card_token = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text='Credit Card identifier. Payment Method must be credit. This field should be filled with credit card identifier according to gateway. Only available for Stripe and should send the Customer ID.'
    )
    payment_authorization_code = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text='Transaction identifier. Payment Method must be credit. This field should be filled with transaction identifier according to gateway. Only available for Stripe and it should be filled with Charge ID associated with the Payment Intent.'
    )
    custom_fields = models.ManyToManyField(
        'app.CustomField',
        help_text='Array with custom fields information'
    )
    promo_code = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text='Promotional code. Required for specials and packages that use it. "rateID" parameter required for using "promoCode".'
    )
    allotment_block_code = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text='Allotment block code to add the reservation to the allotment block.'
    )

    class Meta:
        db_table = 'reservation'


# Not a model, just endpoint which returns the reservation data for specific date
# class ReservationAssignment(models.Model):
#     pass


# Not a model, just endpoint which returns the reservation data in invoice format
# class ReservationInvoiceInformation(models.Model):
#     pass


class ReservationNote(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    reservation_note = models.TextField(help_text='Note to be added to reservation')
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)


class ReservationSource(models.Model):
    source_name = models.CharField(max_length=255, help_text='Source Name')
    is_third_party = models.BooleanField(help_text='True if the source is from a third party')
    status = models.BooleanField(help_text='True if the source is active')
    commission = models.FloatField(help_text='How much commission is charged by the source (in %)')
    payment_collect = models.CharField(
        max_length=50,
        choices=[
            ('hotel', 'Hotel'),
            ('channel', 'Channel'),
        ],
        help_text='Type of payment collect practiced by the source. Allowed values: "hotel", "channel"'
    )

    class Meta:
        db_table = 'source_data'


def validate_file_size(value):
    filesize = value.size
    if filesize > 104857600:  # 100MB in bytes
        raise ValidationError('The maximum file size allowed is 100MB.')


class ReservationDocument(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    file = models.FileField(
        upload_to='reservation_documents/',
        help_text='Form-based File Upload',
        validators=[validate_file_size, FileExtensionValidator(
            allowed_extensions=['pdf', 'rtf', 'doc', 'docx', 'txt', 'jpg', 'jpeg', 'png', 'gif', 'csv', 'txt', 'xls',
                                'xlsx'])]
    )
