from django.db import models


class Room(models.Model):
    room_name = models.CharField(max_length=255, help_text="Room Name")
    dorm_room_name = models.CharField(max_length=255,
                                      help_text="Name of the dorm room. Used for the shared dorm beds that are organized into rooms within the same room type")
    room_description = models.TextField(help_text="Room Description")
    room_blocked = models.BooleanField(
        help_text="If room is blocked on calendar during the period selected. If no check-in/out dates are sent, it returns the status for the current day.")
    room_type = models.ForeignKey("room.RoomType", on_delete=models.CASCADE, help_text="Room Type ID")

    class Meta:
        verbose_name_plural = "Rooms"

    def __str__(self):
        return self.room_name


class RoomType(models.Model):
    PRIVACY_CHOICES = (
        (False, 'Shared'),
        (True, 'Private'),
    )

    room_type_name = models.CharField(max_length=255, help_text="Room Type Name")
    room_type_name_short = models.CharField(max_length=255, help_text="Room Type Short Name")
    room_type_description = models.TextField(help_text="Room Type Description")
    is_private = models.BooleanField(choices=PRIVACY_CHOICES, help_text="Whether room is private or shared")
    max_guests = models.IntegerField(help_text="Max number of guests allowed in the room type")
    adults_included = models.IntegerField(help_text="Number of adults included on the basic room rate")
    children_included = models.IntegerField(help_text="Number of children included on the basic room rate")
    room_type_features = models.ManyToManyField('app.HotelAmenity', help_text="List of features for the room type")

    class Meta:
        verbose_name_plural = "Room Type Details"

    def __str__(self):
        return self.room_type_name


class RoomPhoto(models.Model):
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name='room_photos')
    photo = models.ImageField(upload_to='room_photos')

    def __str__(self):
        return f"Photo {self.pk} for {self.room_type.room_type_name}"
