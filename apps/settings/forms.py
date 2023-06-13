from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, HTML

from apps.room.models import RoomType
from apps.settings.models import Hotel


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Property Information',
                Div(
                    Div('property_name', css_class='col-md-6'),
                    Div('property_type', css_class='col-md-6'),
                    Div('property_description', css_class='col-md-12'),
                    Div('property_image', css_class='col-md-6'),
                    Div('property_primary_language', css_class='col-md-6'),
                    Div('property_phone', css_class='col-md-6'),
                    Div('property_email', css_class='col-md-6'),
                    Div('property_website', css_class='col-md-6'),
                    css_class='row'
                ),
            ),
            Fieldset(
                'Property Address',
                Div(
                    Div('property_address1', css_class='col-md-6'),
                    Div('property_address2', css_class='col-md-6'),
                    Div('property_city', css_class='col-md-6'),
                    Div('property_state', css_class='col-md-6'),
                    Div('property_zip', css_class='col-md-6'),
                    Div('property_country', css_class='col-md-6'),
                    Div('property_latitude', css_class='col-md-6'),
                    Div('property_longitude', css_class='col-md-6'),
                    css_class='row'
                ),
            ),
            Fieldset(
                'Property Policy',
                Div(
                    Div('property_check_in_time', css_class='col-md-6'),
                    Div('property_check_out_time', css_class='col-md-6'),
                    Div('property_late_check_out_allowed', css_class='col-md-6'),
                    Div('property_late_check_out_type', css_class='col-md-6'),
                    Div('property_late_check_out_value', css_class='col-md-6'),
                    Div('property_terms_and_conditions', css_class='col-md-12'),
                    css_class='row'
                ),
            ),
            HTML('<button class="btn btn-primary" type="submit">Save</button>')
        )


class RoomTypeForm(forms.ModelForm):
    class Meta:
        model = RoomType
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)