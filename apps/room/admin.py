from django.contrib import admin

from .models import Room, RoomType, RoomPhoto

admin.site.register(Room)


# admin.site.register(RoomType)
class RoomPhotoInline(admin.TabularInline):
    model = RoomPhoto
    extra = 1


class RoomTypeAdmin(admin.ModelAdmin):
    inlines = [RoomPhotoInline]


admin.site.register(RoomType, RoomTypeAdmin)
