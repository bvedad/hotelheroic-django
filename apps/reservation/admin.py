from django.contrib import admin

from apps.reservation.models import Reservation, ReservationNote, Source, ReservationDocument

admin.site.register(Reservation)
admin.site.register(ReservationNote)
admin.site.register(Source)
admin.site.register(ReservationDocument)
