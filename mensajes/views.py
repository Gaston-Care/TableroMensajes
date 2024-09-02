from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Mensaje

# Create your views here.

def home(request):
    return render(request,'home.html')

def ver_mensajes_recibidos(request):
    mensajes_recibidos = Mensaje.objects.filter(destinatario='Gaston')
    return render(request, 'mensajesRecibidos.html', {'mensajes': mensajes_recibidos})

def ver_mensajes_enviados(request):
    mensajes_enviados = Mensaje.objects.filter(remitente='Gaston')
    return render(request, 'mensajesEnviados.html', {'mensajes': mensajes_enviados})

def crear_mensaje(request):
    contexto = {
        'url': 'http://localhost:8000/nuevoMensaje',
    }
    return render(request, 'crearMensaje.html', contexto)

class TareaView(View):
    def post (self,request):
        texto_del_mensaje = request.POST.get('titulo') 
        remitente = request.POST.get('descripcion') 
        destinatario = request.POST.get('estado') 

        mensaje = Mensaje(texto_del_mensaje=texto_del_mensaje, remitente=remitente, destinatario=destinatario)
        
        if (texto_del_mensaje and remitente and destinatario):
            mensaje.save()
            return HttpResponse("Mensaje Creado Correctamente!", status =201)
        else:
            return HttpResponse("Error al crear el Mensaje!!", status=400)
        