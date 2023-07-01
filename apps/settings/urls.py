from django.urls import path

from apps.settings import views

urlpatterns = [
    path('property-details/', views.settings_property_details_view, name='settings_property_details'),
    path('property-details/property-profile/', views.settings_property_details_property_profile_view,
         name='settings_property_details_property_profile'),
    # path('property-details/property-amenities/', views.settings_property_details_property_amenities_view,
    #      name='settings_property_details_property_amenities'),
    path('property-details/room-types/', views.RoomTypeListView.as_view(), name='settings_room_type'),
    path('property-details/room-types/<int:pk>/edit/', views.settings_room_type_edit_view,
         name='settings_room_type_edit'),
    path('property-details/room-types/create/', views.settings_room_type_create_view, name='settings_room_type_create'),
    path('property-configuration/', views.settings_property_configuration_view,
         name='settings_property_configuration'),
    path('property-configuration/system-settings/', views.settings_property_configuration_general_settings_view,
         name='settings_property_configuration_general_settings'),
    path('property-configuration/taxes-and-fees/', views.TaxesAndFeesListView.as_view(),
         name='settings_taxes_and_fees'),
    path('property-configuration/taxes-and-fees/<int:pk>/edit/', views.settings_taxes_and_fees_edit_view,
         name='settings_taxes_and_fees_edit'),
    path('property-configuration/taxes-and-fees/create/', views.settings_taxes_and_fees_create_view,
         name='settings_taxes_and_fees_create'),
    path('property-configuration/policies/deposit-policy/',
         views.settings_property_configuration_deposit_policy_edit_view,
         name='settings_property_configuration_deposit_policy_edit'),
    path('property-configuration/policies/cancellation-policy/', views.cancellation_policy_list_view,
         name='settings_property_configuration_cancellation_policy_index'),
    path('cancellation-policy/create/', views.CancellationPolicyCreateView.as_view(),
         name='create_cancellation_policy'),
    path('cancellation-policy/update/<int:pk>/', views.CancellationPolicyUpdateView.as_view(),
         name='update_cancellation_policy'),
    path('cancellation-policy/delete/<int:pk>/', views.CancellationPolicyDeleteView.as_view(),
         name='delete_cancellation_policy'),
    path('property-configuration/policies/terms-and-conditions/',
         views.settings_property_configuration_terms_and_conditions_edit_view,
         name='settings_property_configuration_terms_and_conditions_edit'),
    path('property-configuration/policies/arrival-and-departure/',
         views.settings_property_configuration_arrival_and_departure_edit_view,
         name='settings_property_configuration_arrival_and_departure_edit'),
    path('property-configuration/policies/confirmation-pending/',
         views.settings_property_configuration_confirmation_pending_edit_view,
         name='settings_property_configuration_confirmation_pending_edit'),
    path('property-configuration/invoicing/invoice-details/',
         views.settings_property_configuration_invoice_details_edit_view,
         name='settings_property_configuration_invoice_details_edit'),
    path('property-configuration/invoicing/invoicing-settings/',
         views.settings_property_configuration_invoicing_settings_edit_view,
         name='settings_property_configuration_invoicing_settings_edit'),
    path('property-configuration/reservation-sources/', views.ReservationSourcesListView.as_view(),
         name='settings_reservation_sources'),
    path('property-configuration/reservation-sources/<int:pk>/edit/', views.settings_reservation_sources_edit_view,
         name='settings_reservation_sources_edit'),
    path('property-configuration/reservation-sources/create/', views.settings_reservation_sources_create_view,
         name='settings_reservation_sources_create'),
    path('property-configuration/payment-options/bank-transfer/',
         views.settings_property_configuration_bank_transfer_edit_view,
         name='settings_property_configuration_bank_transfer_edit'),
    path('property-configuration/payment-options/paypal/', views.settings_property_configuration_paypal_edit_view,
         name='settings_property_configuration_paypal_edit'),
    path('property-configuration/payment-options/credit-card/', views.CreditCardListView.as_view(),
         name='settings_property_configuration_credit_card_index'),
    path('credit-card/create/', views.CreditCardCreateView.as_view(), name='create_credit_card'),
    path('credit-card/update/<int:pk>/', views.CreditCardUpdateView.as_view(), name='update_credit_card'),
    path('credit-card/delete/<int:pk>/', views.CreditCardDeleteView.as_view(), name='delete_credit_card'),
    path('property-configuration/payment-options/custom-payment-method/', views.CustomPaymentMethodListView.as_view(),
         name='settings_property_configuration_custom_payment_method_index'),
    path('custom-payment-method/create/', views.CustomPaymentMethodCreateView.as_view(),
         name='create_custom_payment_method'),
    path('custom-payment-method/update/<int:pk>/', views.CustomPaymentMethodUpdateView.as_view(),
         name='update_custom_payment_method'),
    path('custom-payment-method/delete/<int:pk>/', views.CustomPaymentMethodDeleteView.as_view(),
         name='delete_custom_payment_method'),
    path('property-configuration/item-categories/', views.ItemCategoryListView.as_view(),
         name='settings_item_category_index'),
    path('property-configuration/item-categories/<int:pk>/edit/', views.settings_item_category_edit_view,
         name='settings_item_category_edit'),
    path('property-configuration/item-categories/create/', views.settings_item_category_create_view,
         name='settings_item_category_create'),
    path('property-configuration/items/', views.ItemListView.as_view(), name='settings_item_index'),
    path('property-configuration/items/<int:pk>/edit/', views.settings_item_edit_view, name='settings_item_edit'),
    path('property-configuration/items/create/', views.settings_item_create_view, name='settings_item_create'),
    path('property-configuration/custom-fields/', views.CustomFieldListView.as_view(),
         name='settings_custom_field_index'),
    path('property-configuration/custom-fields/<int:pk>/edit/', views.settings_custom_field_edit_view,
         name='settings_custom_field_edit'),
    path('property-configuration/custom-fields/create/', views.settings_custom_field_create_view,
         name='settings_custom_field_create'),
    path('property-configuration/guest-statuses/', views.GuestStatusListView.as_view(),
         name='settings_guest_status_index'),
    path('property-configuration/guest-statuses/<int:pk>/edit/', views.settings_guest_status_edit_view,
         name='settings_guest_status_edit'),
    path('property-configuration/guest-statuses/create/', views.settings_guest_status_create_view,
         name='settings_guest_status_create'),
    path('property-details/property-amenities/', views.HotelAmenityListView.as_view(),
         name='settings_hotel_amenity_index'),
    path('property-details/property-amenities/<int:pk>/edit/', views.settings_hotel_amenity_edit_view,
         name='settings_hotel_amenity_edit'),
    path('property-details/property-amenities/create/', views.settings_hotel_amenity_create_view,
         name='settings_hotel_amenity_create'),
    path('user-management/users/', views.UserListView.as_view(),
         name='settings_user_index'),
    path('user-management/users/<int:pk>/edit/', views.settings_user_edit_view,
         name='settings_user_edit'),
    path('user-management/users/create/', views.settings_user_create_view,
         name='settings_user_create'),
    # path('user-management/', views.settings_user_management_view, name='settings_user_management'),
    path('channel-distribution/', views.settings_channel_distribution_view,
         name='settings_channel_distribution'),
    path('email-configuration/', views.settings_email_configuration_view, name='settings_email_configuration'),
    path('email-configuration/email-templates/', views.EmailTemplateListView.as_view(),
         name='settings_email_configuration_email_templates'),
    path('email-configuration/email-templates/<int:pk>/edit/',
         views.settings_email_configuration_email_templates_edit_view,
         name='settings_email_configuration_email_templates_edit'),
    path('email-configuration/email-templates/create/', views.settings_email_configuration_email_templates_create,
         name='settings_email_configuration_email_templates_create'),
    path('email-configuration/email-schedules/', views.EmailScheduleListView.as_view(),
         name='settings_email_configuration_email_schedules'),
    path('email-configuration/email-schedules/<int:pk>/edit/',
         views.settings_email_configuration_email_schedules_edit_view,
         name='settings_email_configuration_email_schedules_edit'),
    path('email-configuration/email-schedules/create/', views.settings_email_configuration_email_schedules_create,
         name='settings_email_configuration_email_schedules_create'),
    path('property-configuration/add-ons/', views.AddOnListView.as_view(), name='settings_addon_index'),
    path('property-configuration/add-ons/<int:pk>/edit/', views.settings_addon_edit_view, name='settings_addon_edit'),
    path('property-configuration/add-ons/create/', views.settings_addon_create_view, name='settings_addon_create'),
    path('property-configuration/add-on-intervals/<int:pk>/edit/', views.settings_addon_interval_edit_view,
         name='settings_addon_interval_edit'),
    path('property-configuration/add-on-intervals/create/', views.settings_addon_interval_create_view,
         name='settings_addon_interval_create'),
    path('system-notifications/', views.settings_system_notifications_edit_view,
         name='settings_system_notifications_edit'),
]
