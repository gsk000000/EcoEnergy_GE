from django.contrib import admin
from django.urls import path
from dispositivos.views import dashboard, device_list, device_detail, measurement_list, alerts_week, login_view, logout_view, register_view, password_reset_request
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('devices/device_list/', device_list, name='device_list'),
    path('devices/<int:device_id>/', device_detail, name='device_detail'),
    path('devices/measurements/', measurement_list, name='measurement_list'),
    path('alerts/week/', alerts_week, name="alerts_week"),

    # auth
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('register/', register_view, name="register"),
    path('password-reset/', password_reset_request, name="password_reset"),
   


    path("password/change/", auth_views.PasswordChangeView.as_view(
        template_name="accounts/password_change_form.html",
        success_url="/accounts/password/change/done/"
    ), name="password_change"),
    path("password/change/done/", auth_views.PasswordChangeDoneView.as_view(
        template_name="accounts/password_change_done.html"
    ), name="password_change_done"),

    # Reset password (flujo por email)
    path("password/reset/", auth_views.PasswordResetView.as_view(
        template_name="accounts/password_reset_form.html",
        email_template_name="accounts/email/password_reset_email.txt",
        subject_template_name="accounts/email/password_reset_subject.txt",
        success_url="/accounts/password/reset/done/"
    ), name="password_reset"),
    path("password/reset/done/", auth_views.PasswordResetDoneView.as_view(
        template_name="accounts/password_reset_done.html"
    ), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        template_name="accounts/password_reset_confirm.html",
        success_url="/accounts/reset/complete/"
    ), name="password_reset_confirm"),
    path("reset/complete/", auth_views.PasswordResetCompleteView.as_view(
        template_name="accounts/password_reset_complete.html"
    ), name="password_reset_complete"),]