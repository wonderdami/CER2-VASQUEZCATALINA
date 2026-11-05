from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('catalogo/', views.catalogo_view, name='catalogo'),
    path('mascota/<int:pk>/', views.detalle_mascota_view, name='detalle_mascota'),
    path('gestion/', views.gestion_mascotas_view, name='gestion_mascotas'),
]
