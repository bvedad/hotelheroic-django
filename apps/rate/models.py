from django.core.exceptions import ValidationError
from django.db import models


class RateInterval(models.Model):
    interval_name = models.CharField(max_length=100, help_text='Enter the name of the rate interval')
    room_type = models.ForeignKey(
        'room.RoomType', on_delete=models.CASCADE, help_text='Select the room type for the rate interval'
    )
    start_date = models.DateField(help_text='Start date of the rate interval')
    end_date = models.DateField(help_text='End date of the rate interval')
    min_length_of_stay = models.PositiveIntegerField(
        blank=True, null=True, help_text='Minimum length of stay for the interval'
    )
    max_length_of_stay = models.PositiveIntegerField(
        blank=True, null=True, help_text='Maximum length of stay for the interval'
    )
    closed_to_arrival = models.BooleanField(
        default=False, help_text='Specify if the interval is closed to arrival'
    )
    closed_to_departure = models.BooleanField(
        default=False, help_text='Specify if the interval is closed to departure'
    )
    additional_adult_fee = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True,
        help_text='Additional fee for each additional adult'
    )
    additional_child_fee = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True,
        help_text='Additional fee for each additional child'
    )
    enable_monday_price = models.BooleanField(
        default=True
    )
    enable_tuesday_price = models.BooleanField(
        default=True
    )
    enable_wednesday_price = models.BooleanField(
        default=True
    )
    enable_thursday_price = models.BooleanField(
        default=True
    )
    enable_friday_price = models.BooleanField(
        default=True
    )
    enable_saturday_price = models.BooleanField(
        default=True
    )
    enable_sunday_price = models.BooleanField(
        default=True
    )
    sunday_price = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True
    )
    monday_price = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True
    )
    tuesday_price = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True
    )
    wednesday_price = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True
    )
    thursday_price = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True
    )
    friday_price = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True
    )
    saturday_price = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True
    )

    def clean(self):
        if self.start_date and self.end_date and self.start_date > self.end_date:
            raise ValidationError('Start date cannot be higher than end date.')
        if self.enable_monday_price and self.monday_price is None:
            raise ValidationError('Monday price is enabled, but no price has been provided.')
        if self.enable_tuesday_price and self.tuesday_price is None:
            raise ValidationError('Tuesday price is enabled, but no price has been provided.')
        if self.enable_wednesday_price and self.wednesday_price is None:
            raise ValidationError('Wednesday price is enabled, but no price has been provided.')
        if self.enable_thursday_price and self.thursday_price is None:
            raise ValidationError('Thursday price is enabled, but no price has been provided.')
        if self.enable_friday_price and self.friday_price is None:
            raise ValidationError('Friday price is enabled, but no price has been provided.')
        if self.enable_saturday_price and self.saturday_price is None:
            raise ValidationError('Saturday price is enabled, but no price has been provided.')
        if self.enable_sunday_price and self.sunday_price is None:
            raise ValidationError('Sunday price is enabled, but no price has been provided.')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class RatePlan(models.Model):
    pass
