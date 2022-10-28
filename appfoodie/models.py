from django.db import models

class Restaurante(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField()
    rango_precios = models.CharField(max_length=10)
    horario = models.CharField(max_length=50)
    tipo_comida =  models.CharField(max_length=20)
    
def __str__(self):
    return f"{self.nombre}, {self.tipo_comida}, {self.direccion}, {self.telefono}, {self.rango_precios}, {self.horario}, {self.id}"
