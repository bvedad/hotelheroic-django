from datetime import datetime

from django.db import models


# Create your models here.
class AppSettings(models.Model):
    pass


class AppState(models.Model):
    pass


class GovernmentReceipt(models.Model):
    reservation = models.ForeignKey('reservation.Reservation', on_delete=models.CASCADE,
                                    help_text='Reservation identifier. It, or house_account_id, is necessary.')
    house_account = models.ForeignKey(
        'app.HouseAccount',
        on_delete=models.CASCADE,
        help_text='House Account identifier. It, or reservation_id, is necessary.'
    )
    name = models.CharField(
        max_length=255,
        help_text='Name of the document. Will be used to describe the document in MFD.'
    )
    url = models.CharField(
        max_length=255,
        help_text='URL for the user to download the document.'
    )
    amount = models.FloatField(
        help_text='Value of the posted document.'
    )
    issue_date = models.DateTimeField(
        default=datetime.now,
        help_text='Datetime of document emission. If not sent, the current datetime will be assumed.'
    )


class Webhook(models.Model):
    object = models.CharField(max_length=255, help_text='Event object')
    action = models.CharField(max_length=255, help_text='Event action')
    endpoint_url = models.URLField(max_length=255, help_text='Endpoint URL')
