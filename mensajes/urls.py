from django.urls import path
from . import views
urlpatterns = [
    path('mensajesRecibidos', views.ver_mensajes_recibidos, name='ver_mensajes_recibidos'),
    path('mensajesEnviados', views.ver_mensajes_enviados, name='ver_mensajes_enviados'),
    path('crearMensaje', views.crear_mensaje, name='crear_mensaje'),
    path('nuevoMensaje', views.TareaView.as_view(), name='nuevoMensaje'),
]