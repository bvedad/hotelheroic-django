from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django_tables2 import SingleTableView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.app.models import EmailTemplate, EmailSchedule
from apps.settings.forms import HotelForm, EmailTemplateForm, EmailScheduleForm, TaxAndFeeForm
from apps.settings.tables import EmailTemplateTable, EmailScheduleTable, TaxAndFeeTable
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
def settings_property_details_acommodation_types_view(request):
    return render(request, 'home/settings/property-details/acommodation-types.html')


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
        return redirect(
            'settings_taxes_and_fees')
    else:
        # Render the edit form
        form = TaxAndFeeForm(instance=tax_and_fee_base_model)
        context = {'form': form}
        return render(request, 'home/settings/property-configuration/taxes-and-fees/', context)


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
