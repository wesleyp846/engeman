from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('/cria_pas', include('e_passagens.urls'), name='cria_pas'),
]