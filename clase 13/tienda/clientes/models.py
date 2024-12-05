from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cuit = models.CharField(max_length=11)
    email = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)

    def __str__(self): 
        return self.nombre
