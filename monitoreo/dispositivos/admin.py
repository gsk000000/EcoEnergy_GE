from django.contrib import admin
from .models import Organization, Category, Zone, Device, Measurement, Alert
from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = '__all__'

    def clean_value(self):
        val = self.cleaned_data.get("value")
        if val < 0:
            raise ValidationError("El valor de la medición no puede ser negativo.")
        return val

# --- Inline example ---
class DeviceInline(admin.TabularInline):
    model = Device
    extra = 0

# --- Admins ---
@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email")
    ordering = ("name",)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "organization")
    list_filter = ("organization",)
    search_fields = ("name",)
    ordering = ("name",)

@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ("name", "organization")
    list_filter = ("organization",)
    search_fields = ("name",)
    ordering = ("name",)
    inlines = [DeviceInline]

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "zone", "organization")
    list_filter = ("organization", "category", "zone")
    search_fields = ("name",)
    ordering = ("name",)

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    form = MeasurementForm
    list_display = ("device", "value", "measured_at", "organization")
    list_filter = ("device__organization", "measured_at")
    search_fields = ("device__name",)
    ordering = ("-measured_at",)

    actions = ["mark_as_checked"]

    def mark_as_checked(self, request, queryset):
        count = queryset.update(updated_at=timezone.now())
        self.message_user(request, f"{count} mediciones actualizadas.")
    mark_as_checked.short_description = "Actualizar fecha de revisión"

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ("device", "severity", "triggered_at", "organization")
    list_filter = ("severity", "organization")
    search_fields = ("device__name", "message")
    ordering = ("-triggered_at",)
