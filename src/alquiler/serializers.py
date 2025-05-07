from rest_framework import serializers
from .models import Vehiculo, Cliente, Alquiler, Ubicacion

# --------- Ubicación ---------
class UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = '__all__'

# --------- Cliente ---------
class ClienteReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ClienteWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

# --------- Vehículo ---------
class VehiculoReadSerializer(serializers.ModelSerializer):
    ubicacion_actual = UbicacionSerializer()

    class Meta:
        model = Vehiculo
        fields = '__all__'

class VehiculoWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'

# --------- Alquiler ---------
class AlquilerReadSerializer(serializers.ModelSerializer):
    vehiculo = VehiculoReadSerializer()
    cliente = ClienteReadSerializer()
    ubicacion_recogida = UbicacionSerializer()
    ubicacion_devolucion = UbicacionSerializer()

    class Meta:
        model = Alquiler
        fields = '__all__'

class AlquilerWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alquiler
        fields = '__all__'
