from django.core.management.base import BaseCommand
from alquiler.models import Vehiculo, Cliente, Alquiler, Ubicacion
from decimal import Decimal
from datetime import datetime

class Command(BaseCommand):
    help = 'Seeder para crear datos de prueba'

    def handle(self, *args, **kwargs):
        # Crear algunas ubicaciones
        ubicacion1 = Ubicacion.objects.create(nombre='Oficina Central', direccion='Av. Principal 123')
        ubicacion2 = Ubicacion.objects.create(nombre='Aeropuerto', direccion='Av. del Aeropuerto 456')

        # Crear algunos vehículos
        vehiculo1 = Vehiculo.objects.create(marca='Toyota', modelo='Corolla', año=2020, tipo='sedan', disponible=True, ubicacion_actual=ubicacion1)
        vehiculo2 = Vehiculo.objects.create(marca='Honda', modelo='Civic', año=2021, tipo='sedan', disponible=False, ubicacion_actual=ubicacion2)
        vehiculo3 = Vehiculo.objects.create(marca='Ford', modelo='F-150', año=2022, tipo='pickup', disponible=True, ubicacion_actual=ubicacion1)
        vehiculo4 = Vehiculo.objects.create(marca='Chevrolet', modelo='Tahoe', año=2021, tipo='suv', disponible=False, ubicacion_actual=ubicacion2)
        vehiculo5 = Vehiculo.objects.create(marca='Nissan', modelo='Rogue', año=2022, tipo='suv', disponible=True, ubicacion_actual=ubicacion1)

        # Crear algunos clientes
        cliente1 = Cliente.objects.create(nombre='Juan Pérez', email='juan.perez@example.com', telefono='987654321', licencia_conducir='A123456')
        cliente2 = Cliente.objects.create(nombre='Ana López', email='ana.lopez@example.com', telefono='912345678', licencia_conducir='B987654')

        # Crear algunos alquileres
        Alquiler.objects.create(
            vehiculo=vehiculo1, cliente=cliente1, 
            fecha_inicio=datetime(2025, 5, 1, 10, 0), fecha_fin=datetime(2025, 5, 5, 10, 0), 
            ubicacion_recogida=ubicacion1, ubicacion_devolucion=ubicacion2, 
            costo_total=Decimal('200.00')
        )
        Alquiler.objects.create(
            vehiculo=vehiculo3, cliente=cliente2, 
            fecha_inicio=datetime(2025, 5, 3, 9, 0), fecha_fin=datetime(2025, 5, 7, 9, 0), 
            ubicacion_recogida=ubicacion2, ubicacion_devolucion=ubicacion1, 
            costo_total=Decimal('250.00')
        )
        Alquiler.objects.create(
            vehiculo=vehiculo5, cliente=cliente1, 
            fecha_inicio=datetime(2025, 5, 10, 12, 0), fecha_fin=datetime(2025, 5, 15, 12, 0), 
            ubicacion_recogida=ubicacion1, ubicacion_devolucion=ubicacion2, 
            costo_total=Decimal('300.00')
        )

        self.stdout.write(self.style.SUCCESS('Datos de prueba creados exitosamente'))
