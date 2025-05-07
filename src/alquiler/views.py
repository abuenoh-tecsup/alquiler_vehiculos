from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Vehiculo, Cliente, Alquiler, Ubicacion
from .serializers import (
    VehiculoReadSerializer, VehiculoWriteSerializer,
    ClienteReadSerializer, ClienteWriteSerializer,
    AlquilerReadSerializer, AlquilerWriteSerializer,
    UbicacionSerializer,
)
from datetime import timedelta
from decimal import Decimal
from django.utils import timezone


# --------- Ubicación (no necesita distinción GET/POST) ---------
class UbicacionViewSet(ModelViewSet):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer


# --------- Vehículo ---------
class VehiculoViewSet(ModelViewSet):
    queryset = Vehiculo.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve', 'disponibles']:
            return VehiculoReadSerializer
        return VehiculoWriteSerializer

    @action(detail=False, methods=["get"], url_path="disponibles")
    def disponibles(self, request):
        disponibles = Vehiculo.objects.filter(disponible=True)
        serializer = self.get_serializer(disponibles, many=True)
        return Response(serializer.data)


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

    @action(detail=False, methods=['post'], url_path='calcular-costo')
    def calcular_costo(self, request):
        try:
            vehiculo_id = request.data.get('vehiculo_id')
            fecha_inicio = request.data.get('fecha_inicio')
            fecha_fin = request.data.get('fecha_fin')

            if not all([vehiculo_id, fecha_inicio, fecha_fin]):
                return Response({'error': 'Faltan campos obligatorios.'}, status=400)

            # Cálculo del total (ej: 50 por día)
            fecha_inicio = timezone.datetime.fromisoformat(fecha_inicio)
            fecha_fin = timezone.datetime.fromisoformat(fecha_fin)
            dias = (fecha_fin - fecha_inicio).days or 1
            costo_dia = Decimal('50.00')
            total = costo_dia * dias

            return Response({'costo_total': total})
        except Exception as e:
            return Response({'error': str(e)}, status=400)

    @action(detail=True, methods=['post'], url_path='devolver')
    def devolver(self, request, pk=None):
        alquiler = self.get_object()
        observaciones = request.data.get('observaciones_dano', '')

        if alquiler.devuelto:
            return Response({'error': 'Este vehículo ya fue devuelto.'}, status=400)

        alquiler.devuelto = True
        alquiler.observaciones_dano = observaciones
        alquiler.save()

        # Marcar vehículo como disponible
        alquiler.vehiculo.disponible = True
        alquiler.vehiculo.save()

        return Response({'status': 'Vehículo devuelto correctamente'})
