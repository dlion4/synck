from django.contrib import admin

from .models import Contact


# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name",  "resolved", "phone_number")
    search_fields = ("first_name", "last_name")
    ordering = ["first_name", "last_name"]
    add_fieldsets = ((None, {"fields": ("first_name", "last_name")}),)
    list_display_links = ("first_name", "last_name")
    list_editable = ["resolved"]
