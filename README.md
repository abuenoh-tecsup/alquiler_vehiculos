# Proyecto de Alquiler de Vehículos con Django Rest Framework

Este proyecto es una API RESTful para la gestión de alquileres de vehículos. La aplicación permite gestionar vehículos, clientes, ubicaciones y alquileres a través de una serie de endpoints.

## Requisitos

- Python 3.x
- Django 4.x
- Django REST Framework 3.x
- PostgreSQL (u otra base de datos compatible con Django)
- pip (para instalar dependencias)

## Instalación

1. Clona el repositorio:

   ```bash
   git clone <url-del-repositorio>
   cd <nombre-del-proyecto>
   ```

2. Crea y activa un entorno virtual (opcional pero recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Configura la base de datos en el archivo `settings.py` si es necesario (se recomienda usar PostgreSQL).

5. Realiza las migraciones:

   ```bash
   python manage.py migrate
   ```

6. Crea un superusuario para acceder al panel de administración de Django (opcional):

   ```bash
   python manage.py createsuperuser
   ```

7. Ejecuta el servidor de desarrollo:

   ```bash
   python manage.py runserver
   ```

   Ahora puedes acceder a la API en `http://127.0.0.1:8000/`.

## Endpoints Disponibles

### 1. **Ubicación** (`/ubicaciones/`)

* **GET** `/ubicaciones/`: Obtiene la lista de todas las ubicaciones.
* **POST** `/ubicaciones/`: Crea una nueva ubicación.

### 2. **Vehículo** (`/vehiculos/`)

* **GET** `/vehiculos/`: Obtiene la lista de todos los vehículos.
* **POST** `/vehiculos/`: Crea un nuevo vehículo.
* **GET** `/vehiculos/<id>/`: Obtiene los detalles de un vehículo específico.
* **PUT** `/vehiculos/<id>/`: Actualiza la información de un vehículo.
* **DELETE** `/vehiculos/<id>/`: Elimina un vehículo.
* **GET** `/vehiculos/disponibles/`: Obtiene la lista de vehículos disponibles.

### 3. **Cliente** (`/clientes/`)

* **GET** `/clientes/`: Obtiene la lista de todos los clientes.
* **POST** `/clientes/`: Crea un nuevo cliente.
* **GET** `/clientes/<id>/`: Obtiene los detalles de un cliente específico.
* **PUT** `/clientes/<id>/`: Actualiza la información de un cliente.
* **DELETE** `/clientes/<id>/`: Elimina un cliente.

### 4. **Alquiler** (`/alquileres/`)

* **GET** `/alquileres/`: Obtiene la lista de todos los alquileres.
* **POST** `/alquileres/`: Crea un nuevo alquiler.
* **GET** `/alquileres/<id>/`: Obtiene los detalles de un alquiler específico.
* **PUT** `/alquileres/<id>/`: Actualiza la información de un alquiler.
* **DELETE** `/alquileres/<id>/`: Elimina un alquiler.

#### Endpoints Personalizados en Alquiler

* **POST** `/alquileres/calcular-costo/`: Calcula el costo total del alquiler de un vehículo en función de las fechas proporcionadas. **Campos requeridos**:

  * `vehiculo_id`: ID del vehículo.
  * `fecha_inicio`: Fecha de inicio del alquiler (formato ISO).
  * `fecha_fin`: Fecha de fin del alquiler (formato ISO).

  Ejemplo de solicitud:

  ```json
  {
      "vehiculo_id": 1,
      "fecha_inicio": "2025-05-01T10:00:00",
      "fecha_fin": "2025-05-05T10:00:00"
  }
  ```

  Respuesta:

  ```json
  {
      "costo_total": 200.00
  }
  ```

* **POST** `/alquileres/<id>/devolver/`: Marca un alquiler como devuelto, actualizando el estado del vehículo a disponible. **Campos requeridos**:

  * `observaciones_dano`: Observaciones sobre daños al vehículo (opcional).

  Ejemplo de solicitud:

  ```json
  {
      "observaciones_dano": "Daño en el espejo retrovisor."
  }
  ```

  Respuesta:

  ```json
  {
      "status": "Vehículo devuelto correctamente"
  }
  ```

## Seeder

Para generar datos de prueba (vehículos, clientes, alquileres), puedes utilizar el siguiente comando:

```bash
python manage.py seed_data
```

Este comando crea datos de ejemplo, incluyendo vehículos disponibles y no disponibles, y clientes con sus respectivos alquileres.
