from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from apps.settings.forms import HotelForm


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
    return render(request, 'home/settings/property-configuration.html')


@login_required
def settings_user_management_view(request):
    return render(request, 'home/settings/user-management.html')


@login_required
def settings_channel_distribution_view(request):
    return render(request, 'home/settings/channel-distribution.html')


@login_required
def settings_email_configuration_view(request):
    return render(request, 'home/settings/email-configuration.html')


@login_required
def settings_system_notifications_view(request):
    return render(request, 'home/settings/system-notifications.html')
