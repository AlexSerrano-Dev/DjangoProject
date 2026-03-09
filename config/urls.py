from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users.views import index, inicio, register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('inicio/', inicio, name='inicio'),

    # LOGIN y LOGOUT (del tutorial anterior)
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # REGISTRO (nuevo)
    path('register/', register, name='register'),
]