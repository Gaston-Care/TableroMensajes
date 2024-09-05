from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import Mensaje

# Create your views here.
def home(request):
    return render(request,'home.html')

def ver_mensajes_recibidos(request):
    destinatario_buscado = 'Martina'
    mensajes_recibidos = Mensaje.objects.filter(destinatario=destinatario_buscado)
    url = 'eliminar_mensaje'
    contexto = {
        'mensajes': mensajes_recibidos,
        'destinatario': destinatario_buscado,
        'url': url
    }
    return render(request, 'verMensajes.html', contexto)

def ver_mensajes_enviados(request):
    remitente_buscado = 'Ezequiel' 
    mensajes_enviados = Mensaje.objects.filter(remitente=remitente_buscado)
    url = 'eliminar_mensaje'
    contexto = {
        'mensajes': mensajes_enviados,
        'remitente': remitente_buscado,
        'url': url
    }
    return render(request, 'verMensajes.html', contexto)

def crear_mensaje(request):
    contexto = {
        'url': 'http://localhost:8000/nuevoMensaje',
    }
    return render(request, 'crearMensaje.html', contexto)

class MensajeView(View):
    def post (self,request):
        texto_del_mensaje = request.POST.get('texto_del_mensaje') 
        remitente = request.POST.get('remitente') 
        destinatario = request.POST.get('destinatario') 

        mensaje = Mensaje(texto_del_mensaje=texto_del_mensaje, remitente=remitente, destinatario=destinatario)
        
        if (texto_del_mensaje and remitente and destinatario):
            mensaje.save()
            return HttpResponse("Mensaje Creado Correctamente!", status =201)
        else:
            return HttpResponse("Error al crear el Mensaje!!", status=400)

def eliminar_mensaje(request):
    mensaje_id = request.POST.get('mensaje_id')
    mensaje = get_object_or_404(Mensaje, id=mensaje_id)
    mensaje.delete()
    return HttpResponse("Mensaje Borrado Correctamente!", status =201)
    