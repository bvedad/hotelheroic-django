from django.contrib import admin

# Register your models here.
from apps.settings.models import Hotel, AddOn

admin.site.register(Hotel)
admin.site.register(AddOn)