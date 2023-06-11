from django.contrib import admin

from apps.integration.models import AppSettings, AppState, GovernmentReceipt, Webhook

admin.site.register(AppSettings)
admin.site.register(AppState)
admin.site.register(GovernmentReceipt)
admin.site.register(Webhook)
