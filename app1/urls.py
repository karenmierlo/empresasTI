
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home', views.home),
    path('alunos', views.alunos),
    path('empresas/', views.empresas),
    path('beneficios/', views.beneficios),
    path('sobrenos/', views.sobrenos)

]

a="abracadabra"