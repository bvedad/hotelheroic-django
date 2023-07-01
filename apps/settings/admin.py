from django.contrib import admin

# Register your models here.
from apps.settings.models import Hotel, AddOn, BookingEngineCustomization

admin.site.register(Hotel)
admin.site.register(AddOn)
admin.site.register(BookingEngineCustomization)