from django.db import models
from django_countries.fields import CountryField
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):
    """Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    """RoomType Object Definition"""

    class Meta:
        verbose_name = "RoomType"
        ordering = ["name"]


class Amenity(AbstractItem):
    """Amenity Object Definition"""

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):
    """Facility Object Definition"""

    class Meta:
        verbose_name_plural = "Facilites"


class HouseRule(AbstractItem):
    """HouseRule Object Definition"""

    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampedModel):
    """Photo Object Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Room(core_models.TimeStampedModel):

    """Room Model Definition"""

    # ------------------CONSTANT---------------------

    # ------------------Model---------------------
    name = models.CharField(max_length=140)
    # ForeignKey is relation many to one :) models has just one User
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    guest = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    room_type = models.ForeignKey(
        RoomType, on_delete=models.SET_NULL, null=True, blank=True
    )
    amenity = models.ManyToManyField("Amenity", blank=True)
    facility = models.ManyToManyField("Facility", blank=True)
    houserule = models.ManyToManyField("HouseRule", blank=True)

    def __str__(self):
        return self.name
