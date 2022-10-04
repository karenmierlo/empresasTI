
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home', views.home),
    path('perfil', views.perfil),
    path('curso', views.curso),
    path('empresas/', views.empresas),
    path('beneficios/', views.beneficios),
    path('vagas/', views.vagas),
    path('sobrenos/', views.sobrenos)

]