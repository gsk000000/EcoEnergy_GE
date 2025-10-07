from django.urls import path
from dispositivos import views
urlpatterns = [
    # Autenticación y sesiones
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('password-reset/', views.password_reset_view, name='password_reset'),

    # Dashboard
    path('dashboard/', views.dashboard_view, name='dashboard'),

    # Dispositivos
    path('devices/', views.device_list_view, name='device_list'),
    path('devices/add/', views.add_device_view, name='add_device'),
    path('devices/<int:device_id>/', views.device_detail_view, name='device_detail'),

    # Categorías y Zonas
    path('categories/add/', views.add_category_view, name='add_category'),
    path('zones/add/', views.add_zone_view, name='add_zone'),

    # Mediciones
    path('measurements/', views.measurement_list_view, name='measurement_list'),

    # Generar datos de ejemplo
    path('generate-sample/', views.generate_sample_data_view, name='generate_sample_data'),
]
