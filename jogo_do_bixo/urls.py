"""jogo_do_bixo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from bixoapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('accounts/', include('bixoapp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path("logout", logout_request, name= "logout"),
    path('sorteio/', sorteio),
    path('apostas/grupo/', apostasGrupo, name='grupo'),
    path('apostas/duque/', apostasDuque, name='duque'),
    path('apostas/terno/', apostasTerno, name='terno'),
    path('apostas/quadra/', apostasQuadra, name='quadra'),
    path('apostas/quina/', apostasQuina, name='quina'),
    path('apostas/resultado/', resultado, name='resultado'),


]
