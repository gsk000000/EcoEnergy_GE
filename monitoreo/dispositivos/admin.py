from django.contrib import admin
from .models import Category, Zone, Device, Measurement, Alert, Organization

admin.site.register(Category)
admin.site.register(Zone)
admin.site.register(Device)
admin.site.register(Measurement)
admin.site.register(Alert)
admin.site.register(Organization)

class MeasurementAdmin(admin.ModelAdmin):
    list_display = ("device", "value", "measured_at", "organization")
    list_filter = ("device__organization", "measured_at")
    search_fields = ("device__name",)
    ordering = ("-measured_at",)
    list_select_related = ("device", "organization")
class DeviceAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "zone", "organization")
    list_filter = ("organization", "category", "zone")
    search_fields = ("name",)
    ordering = ("name",)
    list_select_related = ("category", "zone", "organization")