from django.forms import ModelForm, TextInput

from apps.settings.models import Hotel


class HotelForm(ModelForm):
    class Meta:
        model = Hotel
        fields = '__all__'
