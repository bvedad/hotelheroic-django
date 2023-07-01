from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button
from django import forms

from apps.rate.models import RateInterval


class RateIntervalForm(forms.ModelForm):
    class Meta:
        model = RateInterval
        fields = "__all__"
        labels = {
            'enable_monday_price': '',
            'enable_tuesday_price': '',
            'enable_wednesday_price': '',
            'enable_thursday_price': '',
            'enable_friday_price': '',
            'enable_saturday_price': '',
            'enable_sunday_price': '',
            'sunday_price': False,
            'monday_price': False,
            'tuesday_price': False,
            'wednesday_price': False,
            'thursday_price': False,
            'friday_price': False,
            'saturday_price': False,
        }
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
