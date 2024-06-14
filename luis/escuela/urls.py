from django.contrib import admin
from django.urls import path, include
from alumnos.views import hola  # Asegúrate de que la importación esté correcta

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', hola),
    path('', hola),
    path('alumnos/', include('alumnos.urls')),
]
