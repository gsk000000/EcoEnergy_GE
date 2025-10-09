from django.contrib import admin
from .models import Category, Zone, Device, Measurement, Alert, Organization

admin.site.register(Category)
admin.site.register(Zone)
admin.site.register(Measurement)
admin.site.register(Alert)
admin.site.register(Organization)
admin.site.register(Device) 

# --- 1. Inline para ver Mediciones en el Dispositivo ---
class MeasurementInline(admin.TabularInline):
    model = Measurement
    extra = 0  # No queremos formularios vacíos por defecto
    fields = ('value', 'measured_at')
    readonly_fields = ('value', 'measured_at') # Solo lectura, son registros de datos
    can_delete = False # No permitir eliminar mediciones desde aquí

class DeviceAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "zone", "organization")
    list_filter = ("organization", "category", "zone")
    search_fields = ("name",)
    ordering = ("name",)
    list_select_related = ("category", "zone", "organization")
    
    # 2. Asignar el Inline al DeviceAdmin
    inlines = [MeasurementInline] 

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        
        return qs
@admin.action(description='Marcar alertas seleccionadas como revisadas')
def mark_as_reviewed(modeladmin, request, queryset):
    # Asumimos que podemos usar el campo 'deleted_at' para marcar como revisado (soft-delete)
    updated = queryset.update(deleted_at=timezone.now()) 
    modeladmin.message_user(request, f"{updated} alertas marcadas como revisadas.")

class AlertAdmin(admin.ModelAdmin):
    list_display = ("message", "alert_level", "device", "organization", "date")
    list_filter = ("alert_level", "organization")
    search_fields = ("message", "device__name")
    ordering = ("-date",)
    
    # Asignar la acción
    actions = [mark_as_reviewed]
    
    # Asegurar que solo se muestren las alertas NO revisadas
    def get_queryset(self, request):
        return super().get_queryset(request).filter(deleted_at__isnull=True)
    
class ZoneAdmin(admin.ModelAdmin):
    list_display = ("name", "organization")
    list_filter = ("organization",)
    search_fields = ("name",)
    ordering = ("name",)
    inlines = [DeviceAdmin]  # Inline de Devices
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "organization")
    list_filter = ("organization",)
    search_fields = ("name",)
    ordering = ("name",)

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "rut", "address", "created_at")
    search_fields = ("name", "rut")
    ordering = ("name",)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "rut", "address", "created_at")
    search_fields = ("name", "rut")
    ordering = ("name",)