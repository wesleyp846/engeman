from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('e_funcionarios.urls')),
    path('', include('e_passagens.urls')),
]