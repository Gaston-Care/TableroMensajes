from django.db import models

class Mensaje(models.Model):
    texto_del_mensaje = models.TextField()
    remitente = models.CharField(max_length=25)
    destinatario = models.CharField(max_length=25)
    fecha_del_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de {self.remitente} a {self.destinatario} el dia {self.fecha_del_envio}"