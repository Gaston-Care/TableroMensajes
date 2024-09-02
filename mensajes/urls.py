from django.urls import path
from . import views
urlpatterns = [
    path('mensajes/Recibidos', views.ver_mensajes_recibidos, name='ver_mensajes_recibidos'),
    path('mensajes/enviados', views.ver_mensajes_enviados, name='ver_mensajes_enviados'),
    path('crearMensaje', views.crear_mensaje, name='crear_mensaje'),
    path('nuevoMensaje', views.TareaView.as_view(), name='nuevoMensaje'),
]