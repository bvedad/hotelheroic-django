from django.urls import reverse
from django.utils.html import format_html
from django_tables2 import tables

from apps.rate.models import RateInterval


class RateIntervalTable(tables.Table):
    def render_interval_name(self, value, record):
        edit_url = reverse('rate_interval_edit', args=[record.pk])
        return format_html('<a href="{}">{}</a>', edit_url, value)

    class Meta:
        model = RateInterval
        fields = ("interval_name", "start_date", "end_date", "min_length_of_stay", "max_length_of_stay")
