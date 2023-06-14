from django.db import models


class Item(models.Model):
    item_type = models.CharField(
        max_length=50,
        choices=[
            ('product', 'Product'),
            ('service', 'Service'),
        ],
        help_text='Item type'
    )
    sku = models.CharField(max_length=255, help_text='Item SKU')
    item_code = models.CharField(max_length=255, help_text='Item code')
    name = models.CharField(max_length=255, help_text='Item name')
    category = models.ForeignKey('item.ItemCategory', on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(help_text='Item description')
    price = models.FloatField(help_text='Item price')
    stock_inventory = models.BooleanField(help_text='Track stock inventory for this item')
    item_quantity = models.IntegerField(blank=True, null=True, help_text='Current amount of item available')
    reorder_threshold = models.IntegerField(blank=True, null=True, help_text='Quantity at which to reorder item')
    reorder_needed = models.BooleanField(blank=True, null=True,
                                         help_text='Whether the item is at or below the value set for reorder threshold')
    stop_sell = models.IntegerField(blank=True, null=True, help_text='Quantity at which to stop selling product')
    # Implement it as computed property in serializer
    # stop_sell_met = models.BooleanField(blank=True, null=True,
    #                                   help_text='Whether the item is at or below the value set for stop-sell threshold')

    taxes_and_fees = models.ManyToManyField('taxesandfees.TaxAndFee', blank=True, related_name='items', help_text='Details of the fees applicable')

    price_without_fees_and_taxes = models.FloatField(blank=True, null=True,
                                                     help_text='Item price subtracting the included taxes')
    grand_total = models.FloatField(blank=True, null=True, help_text='Item price with fees and taxes')


class ItemCategory(models.Model):
    category_name = models.CharField(max_length=255, help_text='Category name')
    category_code = models.CharField(max_length=255, help_text='Category code')
    category_color = models.CharField(max_length=255, help_text='Category color (like #3b7be7)')

    def __str__(self):
        return self.category_name


class CustomItem(models.Model):
    reservation = models.ForeignKey('reservation.Reservation', on_delete=models.CASCADE,
                                    help_text='Reservation identifier. Required if no houseAccountID is provided.')
    house_account = models.ForeignKey('app.HouseAccount', on_delete=models.CASCADE,
                                      help_text='House account identifier. Required if no reservationID is provided.')
    # subReservationID = models.CharField(max_length=255, blank=True, null=True, help_text='Sub Reservation identifier.')
    item_quantity = models.IntegerField(help_text='Items quantity')
    item_price = models.CharField(max_length=255, blank=True, null=True,
                                  help_text='Item price. If not sent, the registered price of the item will be used.')
    item_note = models.CharField(max_length=255, blank=True, null=True, help_text='Item note')
    item_paid = models.BooleanField(default=False,
                                    help_text='If the item is already paid. Note: If set to true, a payment in cash will be registered for the total value of the item, taxes, and fees. If this is not the expected behavior, set to false and register the operation manually. If payments are set, itemPaid is ignored.')
    sale_date = models.DateTimeField(blank=True, null=True, auto_now_add=True, help_text='Posting date')
    payments = models.ManyToManyField('payment.Payment', blank=True, related_name='custom_items',
                                      help_text='List of payments if the item is already paid')
