from django.contrib import admin

from apps.reservation.models import Reservation, ReservationNote, ReservationSource, ReservationDocument

admin.site.register(Reservation)
admin.site.register(ReservationNote)
admin.site.register(ReservationSource)
admin.site.register(ReservationDocument)
