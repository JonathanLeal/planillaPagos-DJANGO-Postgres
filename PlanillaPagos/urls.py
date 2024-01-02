"""
URL configuration for PlanillaPagos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from Aplicaciones.Pago.views import home, empleadosVista, registrarEmpleado, editarEmpleado, editandoEmpleado, eliminarEmpleado, irPagar,calcular

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('empleados', empleadosVista),
    path('registrarEmpleado/', registrarEmpleado),
    path('edicionEmpleado/<int:id>', editarEmpleado),
    path('editandoEmpleado/', editandoEmpleado),
    path('eliminarEmpleado/<int:id>', eliminarEmpleado),
    path('pago', irPagar),
    path('calcular', calcular)
]
