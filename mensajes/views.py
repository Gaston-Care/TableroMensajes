from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import Mensaje

# Create your views here.
def home(request):
    return render(request,'home.html')

def ver_mensajes_recibidos(request):
    destinatario_buscado = 'Martina'
    mensajes_recibidos = Mensaje.objects.filter(destinatario=destinatario_buscado) # Lista de mensajes 
    url = 'http://localhost:8000/eliminar_mensaje' # Url de la vista a mostrar cuando se envie el formulario.
    contexto = {
        'mensajes': mensajes_recibidos,
        'destinatario': destinatario_buscado,
        'url': url
    }
    return render(request, 'verMensajes.html', contexto)

def ver_mensajes_enviados(request):
    remitente_buscado = 'Ezequiel' 
    mensajes_enviados = Mensaje.objects.filter(remitente=remitente_buscado) # Lista de mensajes 
    url = 'http://localhost:8000/eliminar_mensaje' # Url de la vista a mostrar cuando se envie el formulario.
    contexto = {
        'mensajes': mensajes_enviados,
        'remitente': remitente_buscado,
        'url': url
    }
    return render(request, 'verMensajes.html', contexto)

def crear_mensaje(request):
    contexto = {
        'url': 'http://localhost:8000/nuevoMensaje', # Url de la vista a mostrar cuando se envie el formulario.
    }
    return render(request, 'crearMensaje.html', contexto)

class MensajeView(View):
    def post (self,request):
        # Guardo los valores de los campos ingresados en el formulario.
        texto_del_mensaje = request.POST.get('texto_del_mensaje') 
        remitente = request.POST.get('remitente') 
        destinatario = request.POST.get('destinatario') 
        
        # Instancio el mensaje con sus datos.
        mensaje = Mensaje(texto_del_mensaje=texto_del_mensaje, remitente=remitente, destinatario=destinatario)
        
        if (texto_del_mensaje and remitente and destinatario): # Si estan completos
            mensaje.save() # Guardo el Mensaje en la BDD
            return HttpResponse("Mensaje Creado Correctamente!", status =201)
        else:
            return HttpResponse("Error al crear el Mensaje!!", status=400)

def eliminar_mensaje(request):
    if request.method == 'POST':
        mensaje_id = request.POST.get('mensaje_id') # Guardo la id del mensaje a eliminar
        if not mensaje_id:
            return HttpResponse("Id no obtenido")
        mensaje = get_object_or_404(Mensaje, id=mensaje_id) # Obtengo el Mensaje que coincida con la id en la BDD
        mensaje.delete() # Elimino el mensaje
        return HttpResponse("Mensaje Borrado Correctamente!", status =200)
    