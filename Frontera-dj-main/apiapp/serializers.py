from rest_framework import serializers
from app.models import *
from .serializers import *

#SE ENCARGA DE HACER EL CRUD DESDE EL API
# Serializers define the API representation.

class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DbTipoProducto
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    tipo = TipoProductoSerializer(read_only=True)
    class Meta:
        model = DbProducto
        fields = '__all__'

class TipoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model= AuthGroup
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    tipo = TipoProductoSerializer(read_only=True)
    class Meta:
        model= AuthUser
        fields = '__all__'

class SuscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DbSuscripcion
        fields = '__all__'