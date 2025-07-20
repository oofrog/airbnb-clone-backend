from django.contrib import admin
from .models import ChattingRoom, Message


# Register your models here.
@admin.register(ChattingRoom)
class ChattingRoomAdmin(admin.ModelAdmin):
    list_display = ("__str__", "created_at", "updated_at")
    list_filter = ("updated_at",)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "text",
        "room",
        "created_at",
    )
    list_filter = ("created_at",)
