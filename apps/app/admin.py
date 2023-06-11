from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Adjustment)
admin.site.register(CurrencySettings)
admin.site.register(CurrencySettingsRate)
admin.site.register(CustomField)
admin.site.register(EmailSchedule)
admin.site.register(EmailTemplate)
admin.site.register(Guest)
admin.site.register(GuestNote)
admin.site.register(Currency)
admin.site.register(PropertyImage)
admin.site.register(HotelAmenity)
admin.site.register(HouseAccount)
admin.site.register(Housekeeper)
admin.site.register(HousekeepingAssignment)
admin.site.register(HousekeepingStatus)
