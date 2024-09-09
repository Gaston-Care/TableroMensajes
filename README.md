# TableroMensajes

Es un proyecto Django para gestionar mensajes en un tablero. El cual permite crear Mensajes, ver mensajes recibidos, ver mensajes enviados y eliminar mensajes.

## Descripción

Este proyecto es una aplicación web basada en Django que proporciona las siguientes funcionalidades:
- **Crear mensaje**: Permite a los usuarios crear nuevos mensajes.
- **Ver mensajes recibidos**: Muestra los mensajes que ha recibido un destinatario.
- **Ver mensajes enviados**: Muestra los mensajes enviados por un remitente.
- **Eliminar mensaje**: Permite a los usuarios eliminar mensajes.

## Requisitos

- Python 3.10.14
- Django 4.2(especificado en el archivo 'requirements.txt')

## Instalacion

1. **Clonar el repositorio**:
En la terminal:
   git clone https://github.com/Gaston-Care/TableroMensajes

2. **Navegar al directorio del proyecto**:
    cd TableroMensajes

3. **Crear un entorno virtual**:
    virtualenv -p /usr/bin/python3.10 nombre_del_entorno

4. **Activar el entorno virtual**:
    En Windows: 
    .\nombre_del_entorno\Scripts\activate

    En macOS/Linux:
    source nombre_del_entorno/bin/activate

5. **Instalar las dependencias**:
    pip install -r requirements.txt

6. **Realizar las migraciones a la base de datos**:
    python manage.py migrate

7. **Correr el Servidor**:
    python manage.py runserver

8. **Acceder a la Aplicacion**:
    Abre el navegador y visita http://127.0.0.1:8000/

## Uso y Funcionalidad
- home: Aparecera una barra de navegacion, Seleccione lo que desea hacer.
- Crear mensaje: Navega a la sección correspondiente para crear un nuevo mensaje.
- Ver mensajes recibidos: Ve a la sección de mensajes recibidos para revisar los mensajes recibido por un destinatario en especifico.
- Ver mensajes enviados: Ve a la sección de mensajes enviados para consultar los mensajes enviados por un remitente en especifico.
- Eliminar mensaje: ve a la sección correspondiente para eliminar un mensaje.

## Contacto
    Para preguntas o soporte, contactese a gecare@udc.edu.ar