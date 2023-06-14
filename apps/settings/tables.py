import django_tables2 as tables
from django.urls import reverse
from django.utils.html import format_html

from apps.app.models import EmailTemplate, EmailSchedule
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
