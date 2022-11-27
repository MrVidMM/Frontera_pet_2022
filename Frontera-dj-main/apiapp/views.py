from django.shortcuts import render

from rest_framework import viewsets
from app.models import *
from .serializers import *
# Create your views here.

# ViewSets define the view behavior.
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = DbProducto.objects.all()
    serializer_class = ProductoSerializer

class TipoProductoViewSet(viewsets.ModelViewSet):
    queryset = DbTipoProducto.objects.all()
    serializer_class = TipoProductoSerializer

class TipoUsuarioViewSet(viewsets.ModelViewSet):
    queryset=AuthGroup.objects.all()
    serializer_class= TipoUsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset=AuthUser.objects.all()
    serializer_class= UsuarioSerializer

class SuscripcionViewSet(viewsets.ModelViewSet):
    queryset=DbSuscripcion.objects.all()
    serializer_class= SuscripcionSerializer