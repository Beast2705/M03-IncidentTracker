"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# Importamos las vistas que ya tenías
from core.views import busqueda_vulnerable
from core.views import update_email_vulnerable
# NUEVO: Importamos la vista para el ejercicio de IDOR
from core.views import ver_incidente

urlpatterns = [
    path('admin/', admin.site.urls),
    # Añade esta línea para activar el Login:
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Vistas de ejercicios anteriores
    path('buscar/', busqueda_vulnerable),
    path('update-email/', update_email_vulnerable),

    # NUEVO: URL para ver detalles de incidente (Vulnerable a IDOR)
    # <int:id> captura el número que pongas en la URL y se lo pasa a la vista
    path('incidente/<int:id>/', ver_incidente),
]