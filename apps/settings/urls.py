from django.urls import path

from apps.settings import views

urlpatterns = [
    path('property-details/', views.settings_property_details_view, name='settings_property_details'),
    path('property-details/property-profile/', views.settings_property_details_property_profile_view,
         name='settings_property_details_property_profile'),
    path('property-details/property-amenities/', views.settings_property_details_property_amenities_view,
         name='settings_property_details_property_amenities'),
    path('property-details/accommodation-types/', views.settings_property_details_acommodation_types_view,
         name='settings_property_details_accomodation_types'),
    path('property-configuration/', views.settings_property_configuration_view,
         name='settings_property_configuration'),
    path('user-management/', views.settings_user_management_view, name='settings_user_management'),
    path('channel-distribution/', views.settings_channel_distribution_view,
         name='settings_channel_distribution'),
    path('email-configuration/', views.settings_email_configuration_view, name='settings_email_configuration'),
    path('email-configuration/email-templates/', views.EmailTemplateListView.as_view(), name='settings_email_configuration_email_templates'),
    path('email-configuration/email-templates/<int:pk>/edit/', views.settings_email_configuration_email_templates_edit_view, name='settings_email_configuration_email_templates_edit'),
    path('email-configuration/email-templates/create/', views.settings_email_configuration_email_templates_create, name='settings_email_configuration_email_templates_create'),
     path('email-configuration/email-schedules/', views.EmailScheduleListView.as_view(), name='settings_email_configuration_email_schedules'),
    path('email-configuration/email-schedules/<int:pk>/edit/', views.settings_email_configuration_email_schedules_edit_view, name='settings_email_configuration_email_schedules_edit'),
    path('email-configuration/email-schedules/create/', views.settings_email_configuration_email_schedules_create, name='settings_email_configuration_email_schedules_create'),
    path('system-notifications/', views.settings_system_notifications_view,
         name='settings_system_notifications'),
]
