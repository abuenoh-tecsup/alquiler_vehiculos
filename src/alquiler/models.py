from django.db import models
from django.utils import timezone

class Ubicacion(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Vehiculo(models.Model):
    TIPO_CHOICES = [
        ('sedan', 'Sedán'),
        ('suv', 'SUV'),
        ('pickup', 'Pickup'),
        ('van', 'Van'),
        ('otro', 'Otro'),
    ]

    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    año = models.PositiveIntegerField()
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    disponible = models.BooleanField(default=True)
    ubicacion_actual = models.ForeignKey(Ubicacion, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año})"

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    licencia_conducir = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Alquiler(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    ubicacion_recogida = models.ForeignKey(Ubicacion, related_name='alquileres_recogida', on_delete=models.SET_NULL, null=True)
    ubicacion_devolucion = models.ForeignKey(Ubicacion, related_name='alquileres_devolucion', on_delete=models.SET_NULL, null=True, blank=True)
    costo_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    devuelto = models.BooleanField(default=False)
    observaciones_dano = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.vehiculo} alquilado por {self.cliente}"
