from django.shortcuts import render
from . models import Usuario
from . serializer import UsuarioSerializer
from rest_framework import viewsets

# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset=Usuario.objects.all()
    serializer_class=UsuarioSerializer
    