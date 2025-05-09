# Generated by Django 5.2.1 on 2025-05-07 19:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.CharField(max_length=20)),
                ('licencia_conducir', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('año', models.PositiveIntegerField()),
                ('tipo', models.CharField(choices=[('sedan', 'Sedán'), ('suv', 'SUV'), ('pickup', 'Pickup'), ('van', 'Van'), ('otro', 'Otro')], max_length=20)),
                ('disponible', models.BooleanField(default=True)),
                ('ubicacion_actual', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='alquiler.ubicacion')),
            ],
        ),
        migrations.CreateModel(
            name='Alquiler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
                ('costo_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('devuelto', models.BooleanField(default=False)),
                ('observaciones_dano', models.TextField(blank=True, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alquiler.cliente')),
                ('ubicacion_devolucion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='alquileres_devolucion', to='alquiler.ubicacion')),
                ('ubicacion_recogida', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='alquileres_recogida', to='alquiler.ubicacion')),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alquiler.vehiculo')),
            ],
        ),
    ]
