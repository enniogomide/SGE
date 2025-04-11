"""
SGE - Sistema de Gerenciamento de Estoque
Projeto de conclusão de curso
Autor: Ennio Gomide dos Santos
Data: 26/03/2025
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('api/v1/', include('authentication.urls')),

    path('', views.home, name='home'),

    path('', include('brands.urls')),
    path('', include('categories.urls')),
    path('', include('inflow.urls')),
    path('', include('outflow.urls')),
    path('', include('products.urls')),
    path('', include('suppliers.urls')),

]
