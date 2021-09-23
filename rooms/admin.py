from django.contrib import admin
from django.contrib.admin.options import HORIZONTAL
from django.db.models.aggregates import Count
from . import models


@admin.register(
    models.RoomType,
    models.HouseRule,
    models.Facility,
    models.Amenity,
)
class ItemAdmin(admin.ModelAdmin):
    """Item Admin Definition"""

    list_display = (
        "name",
        "used_by",
    )

    def used_by(self, obj):
        return obj.rooms.count()

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """Room Admin Definition"""

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        (
            "Times",
            {"fields": ("check_in", "check_out", "instant_book")},
        ),
        (
            "Space",
            {"fields": ("beds", "bedrooms", "baths", "guest")},
        ),
        (
            "More About the Space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "houserules"),
            },
        ),
        (
            "Last Details",
            {"fields": ("host",)},
        ),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "beds",
        "beds",
        "bedrooms",
        "baths",
        "guest",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photo",
        "total_rating",
    )

    list_filter = (
        "instant_book",
        "host__super_host",
        "room_type",
        "room_type",
        "amenities",
        "facilities",
        "houserules",
        "city",
        "country",
    )

    """ 
        ^ -> startswith
        = -> iexact
        @ -> search
        None -> icontains
    """
    search_fields = ("^city", "^host__username")

    filter_horizontal = (
        "amenities",
        "facilities",
        "houserules",
    )

    def count_amenities(self, obj):
        return obj.amenities.count()

    count_amenities.short_description = "hello sexy!"

    def count_photo(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo Admin Definition"""

    pass
