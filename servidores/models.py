from django.db import models

class Servidor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion_ip = models.CharField(max_length=15)
    sistema_operativo = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre