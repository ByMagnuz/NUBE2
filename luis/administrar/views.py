from django.shortcuts import render
from django.http import HttpResponse

def hola(request):
    return HttpResponse("Hola Luis al mundo Django")

# Otras funciones de vista según sea necesario
