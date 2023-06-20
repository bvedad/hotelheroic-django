from bootstrap_modal_forms.forms import BSModalModelForm
from crispy_forms.bootstrap import Modal
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Submit, Button, Field, HTML
from django.forms import inlineformset_factory, formset_factory, BaseModelFormSet, modelformset_factory

from apps.app.models import EmailTemplate, EmailSchedule, CustomField, HotelAmenity
from apps.item.models import ItemCategory, Item
from apps.reservation.models import ReservationSource
from apps.room.models import RoomType
from apps.settings.models import Hotel, HotelPhoto, GuestStatus, AddOn, AddOnInterval, SystemSettings, DepositPolicy, \
    TermsAndConditions, ArrivalAndDeparture, ConfirmationPending, InvoiceDetails, InvoiceSettings, SystemNotification, \
    CreditCard
from apps.taxesandfees.models import TaxAndFee

HotelPhotoFormSet = inlineformset_factory(
    Hotel,
    HotelPhoto,
    fields=('photo',),
    extra=8,
    can_delete=True,
    max_num=8,
    labels={'photo': ''}
)


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset(
                'Property Information',
                Div(
                    Div('property_name', css_class='col-md-6'),
                    Div('property_type', css_class='col-md-6'),
                    Div('property_description', css_class='col-md-12'),
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
        )


class EmailTemplateForm(forms.ModelForm):
    class Meta:
        model = EmailTemplate
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save', css_class='btn btn-primary'))
        self.helper.add_input(
            Button('cancel', 'Cancel', css_class='btn btn-secondary', onclick="window.history.back();"))


class EmailScheduleForm(forms.ModelForm):
    class Meta:
        model = EmailSchedule
        fields = '__all__'
        widgets = {
            'time': forms.TimeInput(attrs={'type': 'time'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save', css_class='btn btn-primary'))
        self.helper.add_input(
            Button('cancel', 'Cancel', css_class='btn btn-secondary', onclick="window.history.back();"))


class TaxAndFeeForm(forms.ModelForm):
    class Meta:
        model = TaxAndFee
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save', css_class='btn btn-primary'))
        self.helper.add_input(
            Button('cancel', 'Cancel', css_class='btn btn-secondary', onclick="window.history.back();"))


class ReservationSourceForm(forms.ModelForm):
    class Meta:
        model = ReservationSource
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save', css_class='btn btn-primary'))
        self.helper.add_input(
            Button('cancel', 'Cancel', css_class='btn btn-secondary', onclick="window.history.back();"))


class RoomTypeForm(forms.ModelForm):
    class Meta:
        model = RoomType
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save', css_class='btn btn-primary'))
        self.helper.add_input(
            Button('cancel', 'Cancel', css_class='btn btn-secondary', onclick="window.history.back();"))


class ItemCategoryForm(forms.ModelForm):
    class Meta:
        model = ItemCategory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save', css_class='btn btn-primary'))
        self.helper.add_input(
            Button('cancel', 'Cancel', css_class='btn btn-secondary', onclick="window.history.back();"))


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save', css_class='btn btn-primary'))
        self.helper.add_input(
            Button('cancel', 'Cancel', css_class='btn btn-secondary', onclick="window.history.back();"))


class CustomFieldForm(forms.ModelForm):
    class Meta:
        model = CustomField
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save', css_class='btn btn-primary'))
        self.helper.add_input(
            Button('cancel', 'Cancel', css_class='btn btn-secondary', onclick="window.history.back();"))


class GuestStatusForm(forms.ModelForm):
    class Meta:
        model = GuestStatus
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save', css_class='btn btn-primary'))
        self.helper.add_input(
            Button('cancel', 'Cancel', css_class='btn btn-secondary', onclick="window.history.back();"))


class HotelAmenityForm(forms.ModelForm):
    class Meta:
        model = HotelAmenity
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save', css_class='btn btn-primary'))
        self.helper.add_input(
            Button('cancel', 'Cancel', css_class='btn btn-secondary', onclick="window.history.back();"))


class AddOnForm(forms.ModelForm):
    class Meta:
        model = AddOn
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save', css_class='btn btn-primary'))
        self.helper.add_input(
            Button('cancel', 'Cancel', css_class='btn btn-secondary', onclick="window.history.back();"))


class AddOnIntervalForm(forms.ModelForm):
    class Meta:
        model = AddOnInterval
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'})
        }
        exclude = ['add_on']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save', css_class='btn btn-primary'))
        self.helper.add_input(
            Button('cancel', 'Cancel', css_class='btn btn-secondary', onclick="window.history.back();"))


class SystemSettingsForm(forms.ModelForm):
    class Meta:
        model = SystemSettings
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Fieldset(
                'General Settings',
                Div(
                    Div('application_language', css_class='col-md-6'),
                    Div('application_date_format', css_class='col-md-6'),
                    Div('application_time_format', css_class='col-md-6'),
                    Div('application_currency', css_class='col-md-6'),
                    css_class='row'
                ),
            ),
            Fieldset(
                'Automation Preferences',
                Div(
                    Div('allow_additional_bookings', css_class='col-md-6'),
                    Div('auto_change_no_show', css_class='col-md-6'),
                    Div('auto_checkout_date_extension', css_class='col-md-6'),
                    Div('auto_assign_reservations', css_class='col-md-6'),
                    Div('use_default_country_for_guest', css_class='col-md-6'),
                    Div('allow_same_day_bookings', css_class='col-md-6'),
                    Div('same_day_bookings_until', css_class='col-md-6'),
                    css_class='row'
                ),
            ),
            Fieldset(
                'Miscellaneous Preferences',
                Div(
                    Div('show_estimated_arrival_time', css_class='col-md-6'),
                    Div('show_checkouts_in_departure_list', css_class='col-md-6'),
                    Div('enable_gdpr_compliance', css_class='col-md-6'),
                    Div('customer_name_format', css_class='col-md-6'),
                    Div('enable_payment_allocation', css_class='col-md-6'),
                    Div('breakfast_included_channel_distribution', css_class='col-md-6'),
                    Div('require_full_payment_prior_to_check_in', css_class='col-md-6'),
                    css_class='row'
                ),
            ),
        )
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save', css_class='btn btn-primary'))


class DepositPolicyForm(forms.ModelForm):
    class Meta:
        model = DepositPolicy
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save', css_class='btn btn-primary'))


class TermsAndConditionsForm(forms.ModelForm):
    class Meta:
        model = TermsAndConditions
        fields = "__all__"
        labels = {
            'content': '',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                Div('language', css_class='col-md-3'),
                Div('content', css_class='col-md-9'),
                css_class='row'
            ),
        )
        self.helper.add_input(Submit('submit', 'Save', css_class='btn btn-primary'))


class ArrivalAndDepartureForm(forms.ModelForm):
    class Meta:
        model = ArrivalAndDeparture
        fields = "__all__"
        widgets = {
            'check_in_time': forms.TimeInput(attrs={'type': 'time'}),
            'check_out_time': forms.TimeInput(attrs={'type': 'time'}),
            'late_check_out_time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save', css_class='btn btn-primary'))


class ConfirmationPendingForm(forms.ModelForm):
    class Meta:
        model = ConfirmationPending
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save', css_class='btn btn-primary'))


class InvoiceDetailsForm(forms.ModelForm):
    class Meta:
        model = InvoiceDetails
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                'Invoice Logo',
                'company_logo',
            ),
            Fieldset(
                'Invoice Title And Sequence',
                'invoice_title',
                'invoice_prefix',
                'starting_index_number',
                'invoice_suffix',
            ),
            Fieldset(
                'Credit Note Title And Sequence',
                'credit_note_same_sequence',
                'credit_note_title',
                'credit_note_prefix',
                'credit_note_starting_index_number',
                'credit_note_suffix',
            ),
            Fieldset(
                'Company Details',
                'include_company_details',
            ),
            Fieldset(
                'Custom Field',
                'custom_fields',
            ),
        )
        self.helper.add_input(Submit('submit', 'Save', css_class='btn btn-primary'))


class InvoiceSettingsForm(forms.ModelForm):
    class Meta:
        model = InvoiceSettings
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save', css_class='btn btn-primary'))


class SystemNotificationForm(forms.ModelForm):
    notification_type = forms.ChoiceField(choices=SystemNotification.NOTIFICATION_CHOICES, disabled=True)

    class Meta:
        model = SystemNotification
        fields = ('notification_type', 'is_active', 'recipients',)
        widgets = {
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        help_texts = {
            'notification_type': '',
        }


SystemNotificationFormSet = modelformset_factory(SystemNotification, SystemNotificationForm, extra=0,
                                                 fields=('notification_type', 'is_active', 'recipients',))


def generate_formset():
    system_notifications = SystemNotification.objects.filter()

    formset = SystemNotificationFormSet(queryset=system_notifications)

    helper = FormHelper()
    helper.template = 'bootstrap5/table_inline_formset.html'
    helper.form_method = 'post'
    helper.add_input(Submit('submit', 'Save'))

    return formset, helper


class CreditCardForm(BSModalModelForm):
    class Meta:
        model = CreditCard
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
