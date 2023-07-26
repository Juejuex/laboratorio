from django.db import models

class Laboratorio(models.Model):
    nombre = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100,default="")
    pais = models.CharField(max_length=100,default="")

    def __str__(self):
        return self.nombre

class Directorgeneral(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.OneToOneField(Laboratorio, models.DO_NOTHING, blank=True, null=True)
    especialidad = models.CharField(max_length=100,default="")

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.OneToOneField(Laboratorio, models.DO_NOTHING, blank=True, null=True)
    f_fabricacion = models.DateField(blank=True, null=True)
    p_costo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    p_venta = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.nombre
