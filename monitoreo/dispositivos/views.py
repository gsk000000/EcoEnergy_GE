from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from django.db.models import Count, Q
from .models import Organization, Device, Category, Zone, Alert, Measurement
from .forms import RegisterForm, LoginForm, PasswordResetForm, DeviceForm, CategoryForm, ZoneForm

def device_list_view(request):
    org_id = request.session.get("org_id")
    if not org_id:
        messages.error(request, "Necesitas iniciar sesion.")
        return redirect("login")

    # Filtros
    category_id = request.GET.get("category")
    zone_id = request.GET.get("zone")

    devices = Device.objects.filter(organization_id=org_id)

    if category_id and category_id != "all":
        devices = devices.filter(category_id=category_id)

    if zone_id and zone_id != "all":
        devices = devices.filter(zone_id=zone_id)

    categories = Category.objects.filter(organization_id=org_id)
    zones = Zone.objects.filter(organization_id=org_id)

    return render(request, "dispositivos/device_list.html", {
        "devices": devices,
        "categories": categories,
        "zones": zones,
        "selected_category": category_id,
        "selected_zone": zone_id,
    })

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Organizacion registrada de manera exitosa. Ahora puedes logearte.")
            return redirect("login")
    else:
            form = RegisterForm()
    return render(request, "dispositivos/register.html", {"form": form})
    
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            try:
                org = Organization.objects.get(email=email, deleted_at__isnull=True)
                if org.check_password(password):
                    request.session["org_id"] = org.id
                    messages.success(request, f"Bienvenido {org.name}!")
                    return redirect("dashboard")
                else:
                    messages.error(request, "Clave invalida.")
            except Organization.DoesNotExist:
                messages.error(request, "Organizacion no encontrada.")
    else:
        form = LoginForm()
    return render(request, "dispositivos/login.html", {"form": form})

def logout_view(request):
    request.session.flush()
    messages.info(request, "Te desconectaste..")
    return redirect("login")

def password_reset_view(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            try:
                org = Organization.objects.get(email=email)
                messages.success(request, "Las instruciones para reiniciar tu clave se ha enviado al correo (simulado :3).")
                return redirect("login")
            except Organization.DoesNotExist:
                messages.error(request, "Correo no registrado.")
    else:
        form = PasswordResetForm()
    return render(request, "dispositivos/password_reset.html", {"form": form})
    
def dashboard_view(request):
    org_id = request.session.get("org_id")
    if not org_id:
        messages.error(request, "Necesitas iniciar sesion.")
        return redirect("login")
    org = Organization.objects.get(id=org_id)
    return render(request, "dispositivos/dashboard.html", {"org": org})

def dashboard_view(request):
    org_id = request.session.get("org_id")
    if not org_id:
        messages.error(request, "Necesitas iniciar sesion.")
        return redirect("login")
    
    try:
        org = Organization.objects.get(id=org_id)
        
        # Dispositivos por categoría
        devices_by_category = (
            Category.objects.filter(organization_id=org_id)
            .annotate(count=Count("device"))
        )
        
        # Dispositivos por zona
        devices_by_zone = (
            Zone.objects.filter(organization_id=org_id)
            .annotate(count=Count("device"))
        )
        
        # Alertas de la semana
        week_ago = timezone.now() - timedelta(days=7)  # Necesita timezone y timedelta
        alerts_week = Alert.objects.filter(
            organization_id=org_id, 
            triggered_at__gte=week_ago
        )
        
        alerts_count = {
            "Critical": alerts_week.filter(severity="Critical").count(),
            "High": alerts_week.filter(severity="High").count(),
            "Medium": alerts_week.filter(severity="Medium").count(),
        }
        
        # Últimas 10 mediciones
        last_measurements = Measurement.objects.filter(
            organization_id=org_id
        ).select_related('device').order_by("-measured_at")[:10]
        
        # Alertas recientes (últimas 5)
        recent_alerts = Alert.objects.filter(
            organization_id=org_id
        ).select_related('device').order_by("-triggered_at")[:5]
        
        return render(request, "dispositivos/dashboard.html", {
            "org": org,
            "devices_by_category": devices_by_category,
            "devices_by_zone": devices_by_zone,
            "alerts_count": alerts_count,
            "last_measurements": last_measurements,
            "recent_alerts": recent_alerts,
        })
        
    except Organization.DoesNotExist:
        messages.error(request, "Organización no encontrada.")
        return redirect("login")
    
def measurement_list_view(request):
    org_id = request.session.get("org_id")
    if not org_id:
        messages.error(request, "You must login first.")
        return redirect("login")

    # Obtener las últimas 50 mediciones de la organización
    measurements = Measurement.objects.filter(
        organization_id=org_id
    ).select_related('device').order_by("-measured_at")[:50]

    return render(request, "dispositivos/measurement_list.html", {
        "measurements": measurements,
    })

def device_detail_view(request, device_id):
    org_id = request.session.get("org_id")
    if not org_id:
        messages.error(request, "Necesitas iniciar sesión primero.")
        return redirect("login")

    try:
        # Obtener el dispositivo específico de la organización actual
        device = Device.objects.get(id=device_id, organization_id=org_id)
        
        # Obtener las últimas 20 mediciones del dispositivo
        measurements = Measurement.objects.filter(
            device=device, organization_id=org_id
        ).order_by("-measured_at")[:20]
        
        # Obtener todas las alertas del dispositivo
        alerts = Alert.objects.filter(
            device=device, organization_id=org_id
        ).order_by("-triggered_at")
        
        return render(request, "dispositivos/device_detail.html", {
            "device": device,
            "measurements": measurements,
            "alerts": alerts,
        })
        
    except Device.DoesNotExist:
        messages.error(request, "Dispositivo no encontrado.")
        return redirect("device_list")

def add_device_view(request):
    org_id = request.session.get("org_id")
    if not org_id:
        messages.error(request, "You must login first.")
        return redirect("login")

    if request.method == "POST":
        form = DeviceForm(request.POST)
        if form.is_valid():
            device = form.save(commit=False)
            device.organization_id = org_id
            device.save()
            messages.success(request, f"Dispositivo {device.name} añadido exitosamente!")
            return redirect("device_list")
    else:
        form = DeviceForm()
    
    form.fields['category'].queryset = Category.objects.filter(organization_id=org_id)
    form.fields['zone'].queryset = Zone.objects.filter(organization_id=org_id)
    
    return render(request, "dispositivos/add_device.html", {"form": form})

def add_category_view(request):
    org_id = request.session.get("org_id")
    if not org_id:
        messages.error(request, "You must login first.")
        return redirect("login")

    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.organization_id = org_id
            category.save()
            messages.success(request, f"Categoría {category.name} añadida exitosamente!")
            return redirect("add_device")
    else:
        form = CategoryForm()
    
    return render(request, "dispositivos/add_category.html", {"form": form})

def add_zone_view(request):
    org_id = request.session.get("org_id")
    if not org_id:
        messages.error(request, "You must login first.")
        return redirect("login")

    if request.method == "POST":
        form = ZoneForm(request.POST)
        if form.is_valid():
            zone = form.save(commit=False)
            zone.organization_id = org_id
            zone.save()
            messages.success(request, f"Zona {zone.name} añadida exitosamente!")
            return redirect("add_device")
    else:
        form = ZoneForm()
    
    return render(request, "dispositivos/add_zone.html", {"form": form})

def generate_sample_data_view(request):
    org_id = request.session.get("org_id")
    if not org_id:
        messages.error(request, "You must login first.")
        return redirect("login")
    
    try:
        org = Organization.objects.get(id=org_id)
        
        # Crear categorías de ejemplo si no existen
        categories = []
        for cat_name in ["Temperatura", "Humedad", "Energía", "Presión", "Calidad Aire"]:
            category, created = Category.objects.get_or_create(
                name=cat_name,
                organization_id=org_id,
                defaults={'name': cat_name, 'organization_id': org_id}
            )
            categories.append(category)
        
        # Crear zonas de ejemplo si no existen
        zones = []
        for zone_name in ["Oficina Principal", "Sala Servidores", "Área Producción", "Almacén", "Exterior"]:
            zone, created = Zone.objects.get_or_create(
                name=zone_name,
                organization_id=org_id,
                defaults={'name': zone_name, 'organization_id': org_id}
            )
            zones.append(zone)
        
        # Crear 20 dispositivos de ejemplo
        device_names = [
            "Sensor Temp 1", "Sensor Temp 2", "Sensor Hum 1", "Sensor Hum 2",
            "Medidor Energía A", "Medidor Energía B", "Sensor Presión 1",
            "Sensor Calidad Aire 1", "Sensor Temp Exterior", "Sensor Hum Exterior",
            "Monitor Servidor 1", "Monitor Servidor 2", "Sensor Presión 2",
            "Sensor Calidad Aire 2", "Medidor Energía C", "Sensor Temp 3",
            "Sensor Hum 3", "Monitor Almacén", "Sensor Presión 3", "Termostato"
        ]
        
        devices_created = 0
        
        # Eliminar dispositivos, mediciones y alertas existentes
        Device.objects.filter(organization_id=org_id).delete()
        
        for i, name in enumerate(device_names):
            # Crear el dispositivo
            device = Device.objects.create(
                name=name,
                category=categories[i % len(categories)],
                zone=zones[i % len(zones)],
                organization_id=org_id
            )
            devices_created += 1
            
            # Crear mediciones de ejemplo para cada dispositivo
            for j in range(5):  # 5 mediciones por dispositivo
                value = 20 + j * 5  # Valores de ejemplo
                Measurement.objects.create(
                    device=device,
                    value=value,
                    measured_at=timezone.now() - timedelta(hours=j),
                    organization=org
                )
                
                # Crear alertas si el valor es alto
                if value > 30:
                    Alert.objects.create(
                        device=device,
                        message=f"Valor crítico detectado: {value}",
                        severity="High",
                        triggered_at=timezone.now() - timedelta(hours=j),
                        organization=org
                    )
                elif value > 25:
                    Alert.objects.create(
                        device=device,
                        message=f"Valor elevado: {value}",
                        severity="Medium", 
                        triggered_at=timezone.now() - timedelta(hours=j),
                        organization=org
                    )
        
        messages.success(request, f"¡Se crearon {devices_created} dispositivos con datos de ejemplo!")
        return redirect("dashboard")
        
    except Organization.DoesNotExist:
        messages.error(request, "Organización no encontrada.")
        return redirect("device_list")
    except Exception as e:
        messages.error(request, f"Error: {str(e)}")
        return redirect("device_list")