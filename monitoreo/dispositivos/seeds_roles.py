# dispositivos/seed_users_roles.py
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Measurement, Alert

grupo_limitado, created = Group.objects.get_or_create(name="Usuario Limitado")
if created:
    print(" Grupo 'Usuario Limitado' creado")

ct_measure = ContentType.objects.get_for_model(Measurement)
ct_alert = ContentType.objects.get_for_model(Alert)

permisos = [
    Permission.objects.get(codename="view_measurement", content_type=ct_measure),
    Permission.objects.get(codename="view_alert", content_type=ct_alert),
]

for p in permisos:
    grupo_limitado.permissions.add(p)
print("Permisos de lectura asignados al grupo")


if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser(
        username="admin",
        email="admin@ecoenergy.com",
        password="admin123"
    )
    print("Superusuario creado: admin / admin123")


if not User.objects.filter(username="cliente").exists():
    u = User.objects.create_user(
        username="cliente",
        email="cliente@ecoenergy.com",
        password="cliente123",
        is_active=True
    )
    u.groups.add(grupo_limitado)
    u.save()
    print("Usuario limitado creado: cliente / cliente123")
