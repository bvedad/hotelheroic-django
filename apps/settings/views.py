from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django_tables2 import SingleTableView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.app.models import EmailTemplate, EmailSchedule
from apps.item.models import ItemCategory, Item
from apps.reservation.models import ReservationSource
from apps.room.models import RoomType
from apps.settings.forms import HotelForm, EmailTemplateForm, EmailScheduleForm, TaxAndFeeForm, ReservationSourceForm, \
    RoomTypeForm, ItemCategoryForm, ItemForm
from apps.settings.tables import EmailTemplateTable, EmailScheduleTable, TaxAndFeeTable, ReservationSourceTable, \
    RoomTypeTable, ItemCategoryTable, ItemTable
from apps.taxesandfees.models import TaxAndFee


@login_required
def settings_property_details_view(request):
    return redirect('settings_property_details_property_profile')


@login_required
def settings_property_details_property_profile_view(request):
    form = HotelForm()
    context = {'form': form}
    return render(request, 'home/settings/property-details/property-profile.html', context)


@login_required
def settings_property_details_property_amenities_view(request):
    return render(request, 'home/settings/property-details/property-amenities.html')


@login_required
def settings_property_configuration_view(request):
    return redirect('settings_taxes_and_fees')


@login_required
def settings_user_management_view(request):
    return render(request, 'home/settings/user-management.html')


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


@login_required
def settings_system_notifications_view(request):
    return render(request, 'home/settings/system-notifications.html')


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
