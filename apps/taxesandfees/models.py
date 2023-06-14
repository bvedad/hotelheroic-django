from django.db import models


class TaxAndFee(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=8, decimal_places=5)
    type = models.CharField(max_length=50, choices=[("tax", "Tax"), ("fee", "Fee")])
    amount_adult = models.DecimalField(max_digits=8, decimal_places=5, null=True,
                                       help_text="Amount charged per adult. Only applicable if amountType = fixed_per_person (Per Person Per Night)")
    amount_child = models.DecimalField(max_digits=8, decimal_places=5, null=True,
                                       help_text="Amount charged per children. Only applicable if amountType = fixed_per_person (Per Person Per Night)")
    # amount_rate_based = models.JSONField()

    amount_type = models.CharField(
        max_length=50,
        choices=[
            ('fixed', 'Fixed'),
            ('percentage', 'Percentage'),
            ('fixed_per_person', 'Fixed per person'),
            ('percentage_rate_based', 'Percentage rate based')
        ],
    )
    # available_for = models.JSONField()
    inclusive_or_exclusive = models.CharField(
        max_length=50,
        choices=[("inclusive", "Inclusive"), ("exclusive", "Exclusive")],
    )
    is_deleted = models.BooleanField()

    def __str__(self):
        return self.name
