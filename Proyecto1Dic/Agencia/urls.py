"""Proyecto1Dic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('', views.index),
    path('prueba/',views.prueba),
    path('kpop/', views.paginakpop),
    path('esqueleto/', views.esqueleto),
    path('inicio/', views.inicio),
    path('transferencia/',views.transferencia),
    path('pagosc/',views.pagosc),
    path('pagose/',views.pagose),
    path('pagos1/',views.pagos1),
    path('pagos2/',views.pagos2),
    path('pagos3/',views.pagos3),
    path('gestiones/',views.gestiones),
    path('preauto/',views.preauto),
    path('prestamo/',views.prestamos),
    path('addcuenta/',views.addcuenta),
    path('delcuenta/',views.delcuenta),
    path('consulta/',views.consultas),
    path('estadocuenta/',views.estadocuenta),
    path('addplan/',views.addplan),
    path('acdescuenta/',views.acdescuenta),
    path('estadotarjeta/',views.estadotarjeta),
]
