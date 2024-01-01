from django.urls import path
from . import views

urlpatterns = [
    path('passagens/', views.passagens, name='passagens'),
]