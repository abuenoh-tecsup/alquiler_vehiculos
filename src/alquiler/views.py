from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Vehiculo, Cliente, Alquiler, Ubicacion
from .serializers import (
    VehiculoReadSerializer, VehiculoWriteSerializer,
    ClienteReadSerializer, ClienteWriteSerializer,
    AlquilerReadSerializer, AlquilerWriteSerializer,
    UbicacionSerializer,
)

# --------- Ubicación (no necesita distinción GET/POST) ---------
class UbicacionViewSet(ModelViewSet):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer


# --------- Vehículo ---------
class VehiculoViewSet(ModelViewSet):
    queryset = Vehiculo.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return VehiculoReadSerializer
        return VehiculoWriteSerializer


# --------- Cliente ---------
class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ClienteReadSerializer
        return ClienteWriteSerializer


# --------- Alquiler ---------
class AlquilerViewSet(ModelViewSet):
    queryset = Alquiler.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return AlquilerReadSerializer
        return AlquilerWriteSerializer
