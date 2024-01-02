from django.urls import path
from . import views

urlpatterns = [
    path('passagens/', views.passagens, name='passagens'),
    path('cria_pas/', views.cria_pas, name='cria_pas'),
    path('pega_mes/', views.pega_mes, name='pega_mes'),
]