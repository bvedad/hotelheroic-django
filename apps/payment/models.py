from django.db import models

class PaymentMethod(models.Model):
    pass

class Payment(models.Model):
    house_account = models.IntegerField(blank=True, null=True,
                                         help_text='House Account identifier. Necessary if reservationID is not sent')
    # subReservationID = models.CharField(max_length=255, blank=True, null=True,
    #                                     help_text='The Sub Reservation identifier. reservationID is still mandatory if subReservationID is sent')
    type = models.ForeignKey('payment.Payment', on_delete=models.CASCADE, blank=True, null=True)
    amount = models.FloatField(help_text='Amount paid on this transaction')
    # card_type = models.CharField(max_length=255, blank=True, null=True,
    #                             help_text='If type is credit, cardType is necessary. Allowed values are property-based, but possible strings are: "visa","master","amex","aura","diners","hiper","elo","Discover","jcb","maestro","dan","PostCard","Eurocard","union_pay"')
    description = models.TextField(help_text='Note to be added to payment')

# class Transaction(models.Model):
#     pass
