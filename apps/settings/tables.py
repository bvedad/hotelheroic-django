import django_tables2 as tables
from django.urls import reverse
from django.utils.html import format_html

from apps.app.models import EmailTemplate, EmailSchedule, CustomField, HotelAmenity
from apps.item.models import ItemCategory, Item
from apps.reservation.models import ReservationSource
from apps.room.models import RoomType
from apps.settings.models import GuestStatus, AddOn, AddOnInterval
from apps.taxesandfees.models import TaxAndFee


class EmailTemplateTable(tables.Table):
    def render_name(self, value, record):
        edit_url = reverse('settings_email_configuration_email_templates_edit', args=[record.pk])
        return format_html('<a href="{}">{}</a>', edit_url, value)

    class Meta:
        model = EmailTemplate
        fields = ('name', 'created_date', 'email_type', 'subject')


class EmailScheduleTable(tables.Table):
    def render_schedule_name(self, value, record):
        edit_url = reverse('settings_email_configuration_email_schedules_edit', args=[record.pk])
        return format_html('<a href="{}">{}</a>', edit_url, value)

    class Meta:
        model = EmailSchedule
        fields = ('schedule_name', 'email_template')


class TaxAndFeeTable(tables.Table):
    def render_name(self, value, record):
        edit_url = reverse('settings_taxes_and_fees_edit', args=[record.pk])
        return format_html('<a href="{}">{}</a>', edit_url, value)

    class Meta:
        model = TaxAndFee
        fields = ('name', 'inclusive_or_exclusive', 'amount')


class ReservationSourceTable(tables.Table):
    def render_source_name(self, value, record):
        edit_url = reverse('settings_reservation_sources_edit', args=[record.pk])
        return format_html('<a href="{}">{}</a>', edit_url, value)

    class Meta:
        model = ReservationSource
        fields = ('source_name', 'is_third_party', 'status')


class RoomTypeTable(tables.Table):
    def render_room_type_name(self, value, record):
        edit_url = reverse('settings_room_type_edit', args=[record.pk])
        return format_html('<a href="{}">{}</a>', edit_url, value)

    class Meta:
        model = RoomType
        fields = ('room_type_name', 'is_private', 'max_guests', 'room_type_features')


class ItemCategoryTable(tables.Table):
    def render_category_name(self, value, record):
        edit_url = reverse('settings_item_category_edit', args=[record.pk])
        return format_html('<a href="{}">{}</a>', edit_url, value)

    class Meta:
        model = ItemCategory
        fields = (
            'category_name',
            'category_code',
            'category_color',
        )


class ItemTable(tables.Table):
    def render_name(self, value, record):
        edit_url = reverse('settings_item_edit', args=[record.pk])
        return format_html('<a href="{}">{}</a>', edit_url, value)

    class Meta:
        model = Item
        fields = ('sku', 'name', 'item_type', 'description', 'price')


class CustomFieldTable(tables.Table):
    def render_name(self, value, record):
        edit_url = reverse('settings_custom_field_edit', args=[record.pk])
        return format_html('<a href="{}">{}</a>', edit_url, value)

    class Meta:
        model = CustomField
        fields = ('name', 'type', 'required', 'apply_to')


class GuestStatusTable(tables.Table):
    def render_name(self, value, record):
        edit_url = reverse('settings_guest_status_edit', args=[record.pk])
        return format_html('<a href="{}">{}</a>', edit_url, value)

    class Meta:
        model = GuestStatus
        fields = ('is_active', 'name', 'description')


class HotelAmenityTable(tables.Table):
    def render_name(self, value, record):
        edit_url = reverse('settings_hotel_amenity_edit', args=[record.pk])
        return format_html('<a href="{}">{}</a>', edit_url, value)

    class Meta:
        model = HotelAmenity
        fields = ('is_active', 'name', 'category')


class AddOnTable(tables.Table):
    def render_name(self, value, record):
        edit_url = reverse('settings_addon_edit', args=[record.pk])
        return format_html('<a href="{}">{}</a>', edit_url, value)

    class Meta:
        model = AddOn
        fields = ("name", "inventory_item")


class AddOnIntervalTable(tables.Table):
    def render_name(self, value, record):
        edit_url = reverse('settings_addon_interval_edit', args=[record.pk])
        return format_html('<a href="{}">{}</a>', edit_url, value)

    class Meta:
        model = AddOnInterval
        fields = ("name", "start_date", "end_date", "room_types")
