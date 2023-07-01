from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalDeleteView
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django_tables2 import SingleTableView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.app.models import EmailTemplate, EmailSchedule, CustomField, HotelAmenity
from apps.authentication.forms import UserForm
from apps.item.models import ItemCategory, Item
from apps.reservation.models import ReservationSource
from apps.room.models import RoomType
from apps.settings.forms import HotelForm, EmailTemplateForm, EmailScheduleForm, TaxAndFeeForm, ReservationSourceForm, \
    RoomTypeForm, ItemCategoryForm, ItemForm, CustomFieldForm, HotelPhotoFormSet, GuestStatusForm, HotelAmenityForm, \
    AddOnForm, AddOnIntervalForm, SystemSettingsForm, DepositPolicyForm, TermsAndConditionsForm, \
    ArrivalAndDepartureForm, ConfirmationPendingForm, InvoiceDetailsForm, InvoiceSettingsForm, \
    generate_formset, SystemNotificationFormSet, CreditCardForm, BankTransferForm, PayPalForm, CustomPaymentMethodForm, \
    CancellationPolicyForm, GeneralCancellationPolicyForm
from apps.settings.models import Hotel, GuestStatus, AddOn, AddOnInterval, SystemSettings, DepositPolicy, \
    TermsAndConditions, ArrivalAndDeparture, ConfirmationPending, InvoiceDetails, InvoiceSettings, CreditCard, \
    BankTransfer, PayPal, CustomPaymentMethod, CancellationPolicy, GeneralCancellationPolicy
from apps.settings.tables import EmailTemplateTable, EmailScheduleTable, TaxAndFeeTable, ReservationSourceTable, \
    RoomTypeTable, ItemCategoryTable, ItemTable, CustomFieldTable, GuestStatusTable, HotelAmenityTable, AddOnTable, \
    AddOnIntervalTable, UserTable, CreditCardTable, CustomPaymentMethodTable, CancellationPolicyTable
from apps.taxesandfees.models import TaxAndFee

User = get_user_model()


@login_required
def settings_property_details_view(request):
    return redirect('settings_property_details_property_profile')


@login_required
def settings_property_details_property_profile_view(request):
    hotel = Hotel.objects.first()
    if request.method == 'POST':
        hotel_form = HotelForm(request.POST, instance=hotel)
        photo_formset = HotelPhotoFormSet(request.POST, request.FILES, instance=hotel)
        if hotel_form.is_valid() and photo_formset.is_valid():
            hotel = hotel_form.save()
            photo_formset.save()
            photo_formset = HotelPhotoFormSet(instance=hotel)
    else:
        hotel_form = HotelForm(instance=hotel)
        photo_formset = HotelPhotoFormSet(instance=hotel)
    return render(request, 'home/settings/property-details/property-profile.html',
                  {'form': hotel_form
                      , 'photo_formset': photo_formset
                   })


@login_required
def settings_property_configuration_view(request):
    return redirect('settings_taxes_and_fees')


@login_required
def settings_channel_distribution_view(request):
    return render(request, 'home/settings/channel-distribution.html')


@login_required
def settings_email_configuration_view(request):
    return redirect('settings_email_configuration_email_templates')


@login_required
def settings_email_configuration_email_templates_edit_view(request, pk):
    email_template = get_object_or_404(EmailTemplate, pk=pk)

    if request.method == 'POST':
        form = EmailTemplateForm(request.POST, instance=email_template)
        if form.is_valid():
            form.save()
        return redirect(
            'settings_email_configuration_email_templates')  # Replace 'roomtype_list' with the actual URL name for the room type list view
    else:
        # Render the edit form
        form = EmailTemplateForm(instance=email_template)
        context = {'form': form}
        return render(request, 'home/settings/email-configuration/email-template-edit.html', context)


class EmailTemplateListView(LoginRequiredMixin, SingleTableView):
    model = EmailTemplate
    table_class = EmailTemplateTable
    template_name = 'home/settings/email-configuration/email-templates.html'


@login_required
def settings_email_configuration_email_templates_create(request):
    if request.method == 'POST':
        form = EmailTemplateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('settings_email_configuration_email_templates')
    else:
        form = EmailTemplateForm()
        context = {'form': form}
        return render(request, 'home/settings/email-configuration/email-template-create.html', context)


@login_required
def settings_email_configuration_email_schedules_edit_view(request, pk):
    email_template = get_object_or_404(EmailSchedule, pk=pk)

    if request.method == 'POST':
        form = EmailScheduleForm(request.POST, instance=email_template)
        if form.is_valid():
            form.save()
        return redirect(
            'settings_email_configuration_email_schedules')
    else:
        # Render the edit form
        form = EmailScheduleForm(instance=email_template)
        context = {'form': form}
        return render(request, 'home/settings/email-configuration/email-schedule-edit.html', context)


class EmailScheduleListView(LoginRequiredMixin, SingleTableView):
    model = EmailSchedule
    table_class = EmailScheduleTable
    template_name = 'home/settings/email-configuration/email-schedules.html'


@login_required
def settings_email_configuration_email_schedules_create(request):
    if request.method == 'POST':
        form = EmailScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('settings_email_configuration_email_schedules')
    else:
        form = EmailScheduleForm()
    context = {'form': form}
    return render(request, 'home/settings/email-configuration/email-schedule-create.html', context)


class TaxesAndFeesListView(LoginRequiredMixin, SingleTableView):
    model = TaxAndFee
    table_class = TaxAndFeeTable
    template_name = 'home/settings/property-configuration/taxes-and-fees/index.html'


@login_required
def settings_taxes_and_fees_edit_view(request, pk):
    tax_and_fee_base_model = get_object_or_404(TaxAndFee, pk=pk)

    if request.method == 'POST':
        form = TaxAndFeeForm(request.POST, instance=tax_and_fee_base_model)
        if form.is_valid():
            form.save()
        return redirect(
            'settings_taxes_and_fees')
    else:
        # Render the edit form
        form = TaxAndFeeForm(instance=tax_and_fee_base_model)
        context = {'form': form}
        return render(request, 'home/settings/property-configuration/taxes-and-fees/edit.html', context)


@login_required
def settings_taxes_and_fees_create_view(request):
    if request.method == 'POST':
        form = TaxAndFeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('settings_taxes_and_fees')
    else:
        form = TaxAndFeeForm()
    context = {'form': form}
    return render(request, 'home/settings/property-configuration/taxes-and-fees/create.html', context)


class ReservationSourcesListView(LoginRequiredMixin, SingleTableView):
    model = ReservationSource
    table_class = ReservationSourceTable
    template_name = 'home/settings/property-configuration/reservation-source/index.html'


@login_required
def settings_reservation_sources_edit_view(request, pk):
    reservation_source = get_object_or_404(ReservationSource, pk=pk)

    if request.method == 'POST':
        form = ReservationSourceForm(request.POST, instance=reservation_source)
        if form.is_valid():
            form.save()
        return redirect(
            'settings_reservation_sources')
    else:
        # Render the edit form
        form = ReservationSourceForm(instance=reservation_source)
        context = {'form': form}
        return render(request, 'home/settings/property-configuration/reservation-source/edit.html', context)


@login_required
def settings_reservation_sources_create_view(request):
    if request.method == 'POST':
        form = ReservationSourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('settings_reservation_sources')
    else:
        form = ReservationSourceForm()
    context = {'form': form}
    return render(request, 'home/settings/property-configuration/reservation-source/create.html', context)


class RoomTypeListView(LoginRequiredMixin, SingleTableView):
    model = RoomType
    table_class = RoomTypeTable
    template_name = 'home/settings/property-details/room-type/index.html'


@login_required
def settings_room_type_edit_view(request, pk):
    room_type = get_object_or_404(RoomType, pk=pk)

    if request.method == 'POST':
        form = RoomTypeForm(request.POST, instance=room_type)
        if form.is_valid():
            form.save()
        return redirect(
            'settings_room_type')
    else:
        # Render the edit form
        form = RoomTypeForm(instance=room_type)
        context = {'form': form}
        return render(request, 'home/settings/property-details/room-type/edit.html', context)


@login_required
def settings_room_type_create_view(request):
    if request.method == 'POST':
        form = RoomTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('settings_room_type')
    else:
        form = RoomTypeForm()
    context = {'form': form}
    return render(request, 'home/settings/property-details/room-type/create.html', context)


class ItemCategoryListView(LoginRequiredMixin, SingleTableView):
    model = ItemCategory
    table_class = ItemCategoryTable
    template_name = 'home/settings/property-configuration/item-category/index.html'


@login_required
def settings_item_category_edit_view(request, pk):
    item_category = get_object_or_404(ItemCategory, pk=pk)

    if request.method == 'POST':
        form = ItemCategoryForm(request.POST, instance=item_category)
        if form.is_valid():
            form.save()
        return redirect(
            'settings_item_category_index')
    else:
        # Render the edit form
        form = ItemCategoryForm(instance=item_category)
        context = {'form': form}
        return render(request, 'home/settings/property-configuration/item-category/edit.html', context)


@login_required
def settings_item_category_create_view(request):
    if request.method == 'POST':
        form = ItemCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('settings_item_category_index')
    else:
        form = ItemCategoryForm()
    context = {'form': form}
    return render(request, 'home/settings/property-configuration/item-category/create.html', context)


class ItemListView(LoginRequiredMixin, SingleTableView):
    model = Item
    table_class = ItemTable
    template_name = 'home/settings/property-configuration/item/index.html'


@login_required
def settings_item_edit_view(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        return redirect(
            'settings_item_index')
    else:
        # Render the edit form
        form = ItemForm(instance=item)
        context = {'form': form}
        return render(request, 'home/settings/property-configuration/item/edit.html', context)


@login_required
def settings_item_create_view(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('settings_item_index')
    else:
        form = ItemForm()
    context = {'form': form}
    return render(request, 'home/settings/property-configuration/item/create.html', context)


class CustomFieldListView(LoginRequiredMixin, SingleTableView):
    model = CustomField
    table_class = CustomFieldTable
    template_name = 'home/settings/property-configuration/custom-field/index.html'


@login_required
def settings_custom_field_edit_view(request, pk):
    item = get_object_or_404(CustomField, pk=pk)

    if request.method == 'POST':
        form = CustomFieldForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        return redirect(
            'settings_custom_field_index')
    else:
        # Render the edit form
        form = CustomFieldForm(instance=item)
        context = {'form': form}
        return render(request, 'home/settings/property-configuration/custom-field/edit.html', context)


@login_required
def settings_custom_field_create_view(request):
    if request.method == 'POST':
        form = CustomFieldForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('settings_custom_field_index')
    else:
        form = CustomFieldForm()
    context = {'form': form}
    return render(request, 'home/settings/property-configuration/custom-field/create.html', context)


class GuestStatusListView(LoginRequiredMixin, SingleTableView):
    model = GuestStatus
    table_class = GuestStatusTable
    template_name = 'home/settings/property-configuration/guest-status/index.html'


@login_required
def settings_guest_status_edit_view(request, pk):
    item = get_object_or_404(GuestStatus, pk=pk)

    if request.method == 'POST':
        form = GuestStatusForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        return redirect(
            'settings_guest_status_index')
    else:
        form = GuestStatusForm(instance=item)
        context = {'form': form}
        return render(request, 'home/settings/property-configuration/guest-status/edit.html', context)


@login_required
def settings_guest_status_create_view(request):
    if request.method == 'POST':
        form = GuestStatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('settings_guest_status_index')
    else:
        form = GuestStatusForm()
    context = {'form': form}
    return render(request, 'home/settings/property-details/hotel-amenity/create.html', context)


class HotelAmenityListView(LoginRequiredMixin, SingleTableView):
    model = HotelAmenity
    table_class = HotelAmenityTable
    template_name = 'home/settings/property-details/hotel-amenity/index.html'


@login_required
def settings_hotel_amenity_edit_view(request, pk):
    item = get_object_or_404(HotelAmenity, pk=pk)

    if request.method == 'POST':
        form = HotelAmenityForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        return redirect(
            'settings_hotel_amenity_index')
    else:
        form = HotelAmenityForm(instance=item)
        context = {'form': form}
        return render(request, 'home/settings/property-details/hotel-amenity/edit.html', context)


@login_required
def settings_hotel_amenity_create_view(request):
    if request.method == 'POST':
        form = HotelAmenityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('settings_hotel_amenity_index')
    else:
        form = HotelAmenityForm()
    context = {'form': form}
    return render(request, 'home/settings/property-details/hotel-amenity/create.html', context)


class AddOnListView(LoginRequiredMixin, SingleTableView):
    model = AddOn
    table_class = AddOnTable
    template_name = 'home/settings/property-configuration/addon/index.html'


@login_required
def settings_addon_edit_view(request, pk):
    item = get_object_or_404(AddOn, pk=pk)

    if request.method == 'POST':
        form = AddOnForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        return redirect(
            'settings_addon_index')
    else:
        form = AddOnForm(instance=item)
        table = AddOnIntervalTable(AddOnInterval.objects.filter(add_on=item))
        context = {'form': form, 'table': table}
        return render(request, 'home/settings/property-configuration/addon/edit.html', context)


@login_required
def settings_addon_create_view(request):
    if request.method == 'POST':
        form = AddOnForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('settings_addon_index')
    else:
        form = AddOnForm()
    context = {'form': form}
    return render(request, 'home/settings/property-configuration/addon/create.html', context)


@login_required
def settings_addon_interval_edit_view(request, pk):
    item = get_object_or_404(AddOnInterval, pk=pk)

    if request.method == 'POST':
        form = AddOnIntervalForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        return redirect(
            'settings_addon_edit', pk=item.add_on.pk)
    else:
        form = AddOnIntervalForm(instance=item)
        context = {'form': form}
        return render(request, 'home/settings/property-configuration/addon-interval/edit.html', context)


@login_required
def settings_addon_interval_create_view(request):
    if request.method == 'POST':
        form = AddOnIntervalForm(request.POST)
        add_on = get_object_or_404(AddOn, pk=request.POST.get('add_on'))
        if form.is_valid():
            instance = form.save(commit=False)
            instance.add_on = add_on
            instance.save()
            return redirect('settings_addon_interval_edit', pk=add_on.pk)
    else:
        add_on = get_object_or_404(AddOn, pk=request.GET.get('add_on'))
        form = AddOnIntervalForm(initial={'add_on': add_on})
    context = {'form': form}
    return render(request, 'home/settings/property-configuration/addon-interval/create.html', context)


@login_required
def settings_property_configuration_general_settings_view(request):
    system_settings = SystemSettings.objects.first()
    if system_settings is None:
        system_settings = SystemSettings.objects.create()
    if request.method == 'POST':
        form = SystemSettingsForm(request.POST, instance=system_settings)
        if form.is_valid():
            system_settings = form.save()
    else:
        form = SystemSettingsForm(instance=system_settings)
    return render(request, 'home/settings/property-configuration/system-settings.html',
                  {'form': form
                   })


@login_required
def settings_property_configuration_deposit_policy_edit_view(request):
    deposit_policy = DepositPolicy.objects.first()
    if deposit_policy is None:
        deposit_policy = DepositPolicy.objects.create()
    if request.method == 'POST':
        form = DepositPolicyForm(request.POST, instance=deposit_policy)
        if form.is_valid():
            form.save()
    else:
        form = DepositPolicyForm(instance=deposit_policy)
    return render(request, 'home/settings/property-configuration/system-settings.html',
                  {'form': form
                   })


@login_required
def settings_property_configuration_terms_and_conditions_edit_view(request):
    terms_and_conditions = TermsAndConditions.objects.first()
    if terms_and_conditions is None:
        terms_and_conditions = TermsAndConditions.objects.create()
    if request.method == 'POST':
        form = TermsAndConditionsForm(request.POST, instance=terms_and_conditions)
        if form.is_valid():
            form.save()
    else:
        form = TermsAndConditionsForm(instance=terms_and_conditions)
    return render(request, 'home/settings/property-configuration/terms-and-conditions.html',
                  {'form': form
                   })


@login_required
def settings_property_configuration_arrival_and_departure_edit_view(request):
    arrival_and_departure = ArrivalAndDeparture.objects.first()
    if arrival_and_departure is None:
        arrival_and_departure = ArrivalAndDeparture()
    if request.method == 'POST':
        form = ArrivalAndDepartureForm(request.POST, instance=arrival_and_departure)
        if form.is_valid():
            form.save()
    else:
        form = ArrivalAndDepartureForm(instance=arrival_and_departure)
    return render(request, 'home/settings/property-configuration/arrival-and-departure.html',
                  {'form': form
                   })


@login_required
def settings_property_configuration_confirmation_pending_edit_view(request):
    confirmation_pending = ConfirmationPending.objects.first()
    if confirmation_pending is None:
        confirmation_pending = ConfirmationPending()
    if request.method == 'POST':
        form = ConfirmationPendingForm(request.POST, instance=confirmation_pending)
        if form.is_valid():
            form.save()
    else:
        form = ConfirmationPendingForm(instance=confirmation_pending)
    return render(request, 'home/settings/property-configuration/arrival-and-departure.html',
                  {'form': form
                   })


@login_required
def settings_property_configuration_invoice_details_edit_view(request):
    invoice_details = InvoiceDetails.objects.first()
    if invoice_details is None:
        invoice_details = InvoiceDetails()
    if request.method == 'POST':
        form = InvoiceDetailsForm(request.POST, instance=invoice_details)
        if form.is_valid():
            form.save()
    else:
        form = InvoiceDetailsForm(instance=invoice_details)
    return render(request, 'home/settings/property-configuration/arrival-and-departure.html',
                  {'form': form
                   })


@login_required
def settings_property_configuration_invoicing_settings_edit_view(request):
    invoicing_settings = InvoiceSettings.objects.first()
    if invoicing_settings is None:
        invoicing_settings = InvoiceSettings()
    if request.method == 'POST':
        form = InvoiceSettingsForm(request.POST, instance=invoicing_settings)
        if form.is_valid():
            form.save()
    else:
        form = InvoiceSettingsForm(instance=invoicing_settings)
    return render(request, 'home/settings/property-configuration/arrival-and-departure.html',
                  {'form': form
                   })


@login_required
def settings_system_notifications_edit_view(request):
    formset, helper = generate_formset()

    if request.method == 'POST':
        formset = SystemNotificationFormSet(request.POST)
        if formset.is_valid():
            formset.save()

    context = {
        'formset': formset,
        'helper': helper,
    }
    return render(request, 'home/settings/system-notifications.html', context)


@login_required
def settings_user_management_view(request):
    return redirect('settings_user_index')


class UserListView(LoginRequiredMixin, SingleTableView):
    model = User
    table_class = UserTable
    template_name = 'home/settings/user-management/user/index.html'


@login_required
def settings_user_edit_view(request, pk):
    item = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        return redirect(
            'settings_user_index')
    else:
        form = UserForm(instance=item)
        context = {'form': form}
        return render(request, 'home/settings/user-management/user/edit.html', context)


@login_required
def settings_user_create_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('settings_user_index')
    else:
        form = UserForm()
    context = {'form': form}
    return render(request, 'home/settings/user-management/user/create.html', context)


class CreditCardListView(LoginRequiredMixin, SingleTableView):
    model = CreditCard
    table_class = CreditCardTable
    template_name = 'home/settings/property-configuration/credit-card/index.html'


class CreditCardCreateView(BSModalCreateView):
    template_name = 'home/settings/property-configuration/credit-card/create.html'
    form_class = CreditCardForm
    success_message = 'Success: Credit Card was created.'
    success_url = reverse_lazy('settings_property_configuration_credit_card_index')


class CreditCardUpdateView(BSModalUpdateView):
    model = CreditCard
    template_name = 'home/settings/property-configuration/credit-card/edit.html'
    form_class = CreditCardForm
    success_message = 'Success: Credit Card was updated.'
    success_url = reverse_lazy('settings_property_configuration_credit_card_index')


class CreditCardDeleteView(BSModalDeleteView):
    model = CreditCard
    template_name = 'home/settings/property-configuration/credit-card/delete.html'
    success_message = 'Success: Credit Card was deleted.'
    success_url = reverse_lazy('settings_property_configuration_credit_card_index')


@login_required
def settings_property_configuration_bank_transfer_edit_view(request):
    bank_transfer = BankTransfer.objects.first()
    if bank_transfer is None:
        bank_transfer = BankTransfer()
    if request.method == 'POST':
        form = BankTransferForm(request.POST, instance=bank_transfer)
        if form.is_valid():
            form.save()
    else:
        form = BankTransferForm(instance=bank_transfer)
    return render(request, 'home/settings/property-configuration/bank-transfer.html',
                  {'form': form
                   })


@login_required
def settings_property_configuration_paypal_edit_view(request):
    paypal = PayPal.objects.first()
    if paypal is None:
        paypal = PayPal()
    if request.method == 'POST':
        form = PayPalForm(request.POST, instance=paypal)
        if form.is_valid():
            form.save()
    else:
        form = PayPalForm(instance=paypal)
    return render(request, 'home/settings/property-configuration/paypal.html',
                  {'form': form
                   })


class CustomPaymentMethodListView(LoginRequiredMixin, SingleTableView):
    model = CustomPaymentMethod
    table_class = CustomPaymentMethodTable
    template_name = 'home/settings/property-configuration/custom-payment-method/index.html'


class CustomPaymentMethodCreateView(BSModalCreateView):
    template_name = 'home/settings/property-configuration/custom-payment-method/create.html'
    form_class = CustomPaymentMethodForm
    success_message = 'Success: Custom Payment Method was created.'
    success_url = reverse_lazy('settings_property_configuration_custom_payment_method_index')


class CustomPaymentMethodUpdateView(BSModalUpdateView):
    model = CustomPaymentMethod
    template_name = 'home/settings/property-configuration/custom-payment-method/edit.html'
    form_class = CustomPaymentMethodForm
    success_message = 'Success: Custom Payment Method was updated.'
    success_url = reverse_lazy('settings_property_configuration_custom_payment_method_index')


class CustomPaymentMethodDeleteView(BSModalDeleteView):
    model = CustomPaymentMethod
    template_name = 'home/settings/property-configuration/custom-payment-method/delete.html'
    success_message = 'Success: Custom Payment Method was deleted.'
    success_url = reverse_lazy('settings_property_configuration_custom_payment_method_index')


def cancellation_policy_list_view(request):
    table = CancellationPolicyTable(CancellationPolicy.objects.all())
    general_cancellation_policy = GeneralCancellationPolicy.objects.first()
    if general_cancellation_policy is None:
        general_cancellation_policy = GeneralCancellationPolicy()

    if request.method == 'POST':
        form = GeneralCancellationPolicyForm(request.POST, instance=general_cancellation_policy)
        if form.is_valid():
            form.save()
    else:
        form = GeneralCancellationPolicyForm(instance=general_cancellation_policy)

    return render(request, "home/settings/property-configuration/cancellation-policy/index.html", {
        "table": table,
        'form': form
    })


class CancellationPolicyCreateView(BSModalCreateView):
    template_name = 'home/settings/property-configuration/cancellation-policy/create.html'
    form_class = CancellationPolicyForm
    success_message = 'Success: Cancellation Policy was created.'
    success_url = reverse_lazy('settings_property_configuration_cancellation_policy_index')


class CancellationPolicyUpdateView(BSModalUpdateView):
    model = CancellationPolicy
    template_name = 'home/settings/property-configuration/cancellation-policy/edit.html'
    form_class = CancellationPolicyForm
    success_message = 'Success: Cancellation Policy was updated.'
    success_url = reverse_lazy('settings_property_configuration_cancellation_policy_index')


class CancellationPolicyDeleteView(BSModalDeleteView):
    model = CancellationPolicy
    template_name = 'home/settings/property-configuration/cancellation-policy/delete.html'
    success_message = 'Success: Cancellation Policy was deleted.'
    success_url = reverse_lazy('settings_property_configuration_cancellation_policy_index')
