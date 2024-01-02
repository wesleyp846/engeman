from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('cria_pas/', include('e_passagens.urls'), name='cria_pas'),
    path('valida_login/', views.valida_login, name='valida_login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('valida_cadastro/', views.valida_cadastro, name='valida_cadastro'),
]