from django.contrib import admin
from .models import Review


# Register your models here.
class Wordfilter(admin.SimpleListFilter):

    title = "Filter by words"

    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        else:
            return reviews


class GoodOrBad(admin.SimpleListFilter):

    title = "Good Or Bad Filter"

    parameter_name = "potato"

    def lookups(self, request, model_admin):
        return [
            ("goodreview", "Goodreview"),
            ("badreview", "Badreview"),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        if word == "goodreview":
            return reviews.filter(rating__gte=3)
        elif word == "badreview":
            return reviews.filter(rating__lt=3)
        else:
            reviews


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "payload",
    )

    list_filter = (
        GoodOrBad,
        Wordfilter,
        "rating",
        "user__is_host",
        "room__category",
    )
