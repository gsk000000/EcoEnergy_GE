from django.contrib import admin

# Register your models here.
@admin.action(description="Activar dispositivos seleccionados")
def make_active(modeladmin, request, queryset):
    queryset.update(status="ACTIVE")

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ("name", "organization", "zone", "product", "max_power_w", "status")
    actions = [make_active]
    search_fields = ("name", "serial_number", "organization__name", "zone__name", "product__name")
    list_filter = ("organization", "zone", "product", "status")
    list_select_related = ("organization", "zone", "product")
    ordering = ("organization__name", "zone__name", "name")
    list_per_page = 50