from datetime import timedelta
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import LoginForm, RegisterForm, PasswordResetRequestForm
from .models import Alert, Category, Device, Measurement, Zone


# Utilidad
def _current_org(request):
    return request.session.get("org_id")


# Traducción de severidades
TRANSLATE_LEVELS = {
    "High": "Grave",
    "Low": "Mediano",       
    "Medium": "Alto",
}


# Dashboard
def dashboard(request):
    org_id = _current_org(request)

    if org_id:
        # Mostrar datos solo de la organización logueada
        latest_measurements = (
            Measurement.objects
            .select_related("device")
            .filter(organization_id=org_id, deleted_at__isnull=True)
            .order_by("-date")[:10]
        )

        device_by_category = (
            Category.objects
            .filter(organization_id=org_id, deleted_at__isnull=True)
            .annotate(count=Count("device"))
        )

        device_by_zone = (
            Zone.objects
            .filter(organization_id=org_id, deleted_at__isnull=True)
            .annotate(count=Count("device"))
        )

        now = timezone.now()
        week_start = now - timedelta(days=7)
        alerts_week_qs = (
            Alert.objects
            .filter(organization_id=org_id, deleted_at__isnull=True, date__gte=week_start)
            .order_by("-date")
        )

        alerts_by_level_week = (
            alerts_week_qs
            .values("alert_level")
            .annotate(count=Count("id"))
            .order_by()
        )


        alerts_summary = {"Grave": 0, "Alto": 0, "Mediano": 0}
        for item in alerts_by_level_week:
            translated = TRANSLATE_LEVELS.get(item["alert_level"], item["alert_level"])
            if translated in alerts_summary:
                alerts_summary[translated] = item["count"]

        recent_alerts = list(alerts_week_qs.select_related("device")[:5])
        for a in recent_alerts:
            a.alert_level = TRANSLATE_LEVELS.get(a.alert_level, a.alert_level)
    else:
        latest_measurements = []
        device_by_category = []
        device_by_zone = []
        alerts_summary = {"Grave": 0, "Alto": 0, "Mediano": 0}
        recent_alerts = []

    return render(request,"dispositivos/dashboard.html", {
            "latest_measurements": latest_measurements,
            "device_by_category": device_by_category,
            "device_by_zone": device_by_zone,
            "alerts_summary": alerts_summary, 
            "recent_alerts": recent_alerts,
        },
    )

# Alertas de la semana (HU5)

@login_required
def alerts_week(request):
    org_id = _current_org(request)
    now = timezone.now()
    week_start = now - timedelta(days=7)

    alerts = list(
        Alert.objects
        .select_related("device")
        .filter(organization_id=org_id, deleted_at__isnull=True, date__gte=week_start)
        .order_by("-date")
    )

    
    for a in alerts:
        a.alert_level = TRANSLATE_LEVELS.get(a.alert_level, a.alert_level)

    return render(request, "dispositivos/alerts_week.html", {"alerts": alerts})



# Devices
@login_required
def device_detail(request, device_id):
    org_id = _current_org(request)
    device = get_object_or_404(
        Device, id=device_id, organization_id=org_id, deleted_at__isnull=True
    )
    measurements = (
        Measurement.objects.filter(device=device, deleted_at__isnull=True).order_by("-date")
    )
    alerts = Alert.objects.filter(device=device, deleted_at__isnull=True).order_by("-date")

    return render(
        request,
        "dispositivos/device_detail.html",
        {"device": device, "measurements": measurements, "alerts": alerts},
    )


@login_required
def device_list(request):
    org_id = _current_org(request)
    category_id = request.GET.get("category")
    categories = Category.objects.filter(organization_id=org_id, deleted_at__isnull=True)

    devices = Device.objects.filter(organization_id=org_id, deleted_at__isnull=True)
    if category_id:
        devices = devices.filter(category_id=category_id)

    return render(
        request,
        "dispositivos/device_list.html",
        {"devices": devices, "categories": categories, "selected_category": category_id},
    )


@login_required
def measurement_list(request):
    # Tomamos el parámetro GET (default = desc)
    sort = request.GET.get("sort", "desc")

    if sort == "asc":
        measurements = Measurement.objects.select_related('device').order_by('date')
    else:
        measurements = Measurement.objects.select_related('device').order_by('-date')

    paginator = Paginator(measurements, 50)  # 50 por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'dispositivos/measurement_list.html', {
        'page_obj': page_obj,
        'sort': sort,  # lo pasamos al template para mantener la selección
    })


# --- Login ---
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get("user")
            org = form.cleaned_data["org"]
            if user is not None:
                login(request, user)
                request.session["org_id"] = org.id  # guarda sesión
                messages.success(request, f"Bienvenido {org.name}!")
                return redirect("dashboard")
            else:
                messages.error(request, "Error en las credenciales.")
        else:
            messages.error(request, "Error en las credenciales.")
    else:
        form = LoginForm()

    return render(request, "dispositivos/login.html", {"form": form})

# --- Registro ---
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, "Registro exitoso. Ya puedes iniciar sesión.")
            return redirect("login")
        else:
            messages.error(request, "Por favor corrige los errores del formulario.")
    else:
        form = RegisterForm()

    return render(request, "dispositivos/register.html", {"form": form})

def password_reset_request(request):
    if request.method == "POST":
        form = PasswordResetRequestForm(request.POST)
        if form.is_valid():
            messages.info(
                request,
                "Si el email existe, enviamos instrucciones a tu correo (simulado).",
            )
            return redirect("login")
    else:
        form = PasswordResetRequestForm()
    return render(request, "dispositivos/password_reset.html", {"form": form})

# --- Logout ---
@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Has cerrado sesión.")
    return redirect("login")