from .models import programmer
from .serializer import ProgrammerSerializer
from rest_framework import viewsets
from django.shortcuts import render 
# esta libreria nola usaremos por ahora
# Create your views here.


class Modelo_1_ViewSet(viewsets.ModelViewSet):
# acá creamos una QUERY a nuestra tabla, trayendotodos los campos como un objeto.
    queryset = programmer.objects.all()
# Agregamos la clase ProgrammerSerializer que yatiene el modelo serializado para mostrar
    serializer_class = ProgrammerSerializer
