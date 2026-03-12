from django.urls import path
from users.views import inicio, acerca_de, list_products, register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cliente/', inicio, name='inicio'),
    path('acerca_de/', acerca_de, name='acerca_de'),
    path('productos/', list_products, name='list_products'),
    # REGISTRO (nuevo)
    path('register/', register, name='register'),
     # Paso 1: Formulario para ingresar email
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='registration/password_reset.html'
        ),
        name='password_reset'
    ),

    # Paso 2: Confirmación de que el email fue enviado
    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html'
        ),
        name='password_reset_done'
    ),

    # Paso 3: Formulario para nueva contraseña (enlace del email)
    path(
        'password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html'
        ),
        name='password_reset_confirm'
    ),

    # Paso 4: Confirmación final
    path(
        'password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),
]