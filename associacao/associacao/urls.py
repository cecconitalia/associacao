from django.urls import path
from app_associacao import views

urlpatterns = [
    path('', views.home,name='index.html'),

    path('sobre/', views.about,name='about.html'),

    path('cad/', views.usuariocad,name='lugar.html'),   

    path('usuarios/', views.usuarios,name='listagem_usuarios'),

    path('contato/', views.contato,name='contato.html'),

    path('leads/', views.leads,name='listagem_leads')
]