from django import forms
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth import authenticate
from django.contrib.contenttypes.models import ContentType
from .models import Organization, Measurement, Alert

# --- Formulario de Login ---
class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned = super().clean()
        email = cleaned.get("email")
        password = cleaned.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise forms.ValidationError("Credenciales inválidas.")

        # Autenticar usando username real
        auth_user = authenticate(username=user.username, password=password)
        if not auth_user:
            raise forms.ValidationError("Credenciales inválidas.")
        if not auth_user.is_active:
            raise forms.ValidationError("Usuario inactivo.")

        cleaned["user"] = auth_user
        return cleaned


# --- Formulario de Registro ---
class RegisterForm(forms.Form):
    org_name = forms.CharField(label="Company name", max_length=100)
    org_rut = forms.CharField(label="RUT", max_length=12)
    org_address = forms.CharField(label="Address", max_length=200)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe un usuario con ese email.")
        return email

    def save(self):
        # Crear Organization
        org = Organization.objects.create(
            name=self.cleaned_data["org_name"],
            rut=self.cleaned_data["org_rut"],
            address=self.cleaned_data["org_address"],
        )

        # Crear User con create_user (hash de contraseña)
        user = User.objects.create_user(
            username=self.cleaned_data["email"],
            email=self.cleaned_data["email"],
            password=self.cleaned_data["password"],
            is_active=True
        )

        # Crear grupo Usuario Limitado con permisos de solo lectura
        grupo_limitado, created = Group.objects.get_or_create(name="Usuario Limitado")
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