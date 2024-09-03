from django.urls import path
from .views import MensajeView, crear_mensaje, home, ver_mensajes_enviados, ver_mensajes_recibidos

urlpatterns = [
    path('', home, name='home'),
    path('mensajesRecibidos', ver_mensajes_recibidos, name='ver_mensajes_recibidos'),
    path('mensajesEnviados', ver_mensajes_enviados, name='ver_mensajes_enviados'),
    path('crearMensaje', crear_mensaje, name='crear_mensaje'),
    path('nuevoMensaje', MensajeView.as_view(), name='nuevoMensaje'),
]