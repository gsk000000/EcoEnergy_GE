from django import forms
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth import authenticate, login, logout
from django.contrib.contenttypes.models import ContentType
from .models import Organization, Measurement, Alert
from django.contrib import messages
from django.shortcuts import redirect, render

# --- Formulario de Login ---
class LoginForm(forms.Form):
    username = forms.CharField(label="Usuario")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Bienvenido {user.username}!")
                return redirect("dashboard")
            else:
                messages.error(request, "Credenciales inválidas.")
        else:
            messages.error(request, "Formulario inválido.")
    else:
        form = LoginForm()
    return render(request, "dispositivos/login.html", {"form": form})

def logout_view(request):
    logout(request)
    messages.info(request, "Has cerrado sesión correctamente.")
    return redirect("login")


# --- Formulario de Registro ---
class RegisterForm(forms.Form):
    org_name = forms.CharField(label="Nombre de la organización", max_length=100)
    email = forms.EmailField(label="Correo electrónico")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe un usuario con ese correo.")
        return email

    def save(self):
        # Crear organización
        org = Organization.objects.create(
            name=self.cleaned_data["org_name"],
            email=self.cleaned_data["email"],
        )
        org.set_password(self.cleaned_data["password"])
        org.save()

        # Crear usuario Django vinculado
        user = User.objects.create_user(
            username=self.cleaned_data["email"],
            email=self.cleaned_data["email"],
            password=self.cleaned_data["password"],
            is_active=True
        )

        # Grupo Usuario Limitado
        grupo_limitado, _ = Group.objects.get_or_create(name="Usuario Limitado")

        ct_measure = ContentType.objects.get_for_model(Measurement)
        ct_alert = ContentType.objects.get_for_model(Alert)
        permisos = [
            Permission.objects.get(codename="view_measurement", content_type=ct_measure),
            Permission.objects.get(codename="view_alert", content_type=ct_alert),
        ]
        for p in permisos:
            grupo_limitado.permissions.add(p)

        user.groups.add(grupo_limitado)
        user.save()

        return user, org


# --- Password Reset Request Form ---
class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField()