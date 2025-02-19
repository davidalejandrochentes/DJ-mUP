# mUP - Sistema de Gestión de Mantenimiento Unificado

## Descripción

mUP es una aplicación web robusta desarrollada en Django que permite a las empresas gestionar de manera eficiente y visual el mantenimiento de sus activos desde un servidor local. Esta herramienta está diseñada para optimizar el seguimiento y control de mantenimientos en diferentes áreas de la empresa.

## Características Principales

- **Gestión de Vehículos**
  - Registro detallado de vehículos
  - Control de mantenimientos preventivos y correctivos
  - Seguimiento de kilometraje
  - Alertas de mantenimiento programado

- **Gestión de Herramientas**
  - Inventario de herramientas
  - Control de estado y ubicación
  - Seguimiento de mantenimientos
  - Registro de responsables

- **Gestión de Áreas de Trabajo**
  - Control de espacios y ubicaciones
  - Registro de capacidad y ocupación
  - Programación de mantenimientos
  - Seguimiento de estado

- **Gestión de Equipos de Cómputo**
  - Inventario de equipos
  - Control de mantenimientos
  - Seguimiento de estado
  - Registro de usuarios responsables

## Tecnologías Utilizadas

- Django 5.1.1
- Python
- SQLite
- Bootstrap
- Pillow (Procesamiento de imágenes)
- OpenPyXL (Exportación de datos)

## Requisitos Previos

- Python 3.x
- pip (Gestor de paquetes de Python)
- Virtualenv (recomendado)

## Instalación

1. Clonar el repositorio:
```bash
git clone [URL_DEL_REPOSITORIO]
```

2. Crear y activar entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Realizar migraciones:
```bash
python manage.py migrate
```

5. Crear superusuario:
```bash
python manage.py createsuperuser
```

6. Iniciar el servidor:
```bash
python manage.py runserver
```

## Capturas de Pantalla

![alt text](static/mUP/1.webp) ![alt text](static/mUP/2.webp) ![alt text](static/mUP/3.webp) ![alt text](static/mUP/4.webp) ![alt text](static/mUP/5.webp) ![alt text](static/mUP/6.webp) ![alt text](static/mUP/7.webp)

## Contribuir

Las contribuciones son bienvenidas. Para contribuir:

1. Fork el proyecto
2. Crea tu rama de características
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

## Contacto

David Alejandro Chentes Ramos