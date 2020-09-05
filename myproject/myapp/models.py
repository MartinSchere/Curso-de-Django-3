from django.db import models


class Mejora(models.Model):
    nombre_de_mejora = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre_de_mejora


class Patente(models.Model):
    codigo_de_patente = models.CharField(max_length=30)

    def __str__(self):
        return self.codigo_de_patente


class Fabrica(models.Model):
    nombre_de_marca = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre_de_marca


class Auto(models.Model):
    # RELACIONES
    fabrica = models.ForeignKey(Fabrica, on_delete=models.SET_NULL, null=True)
    mejoras = models.ManyToManyField(Mejora)
    patente = models.OneToOneField(Patente, on_delete=models.CASCADE)
    #
    nombre = models.CharField(max_length=30)
    kilometraje = models.IntegerField()
    fecha_de_fabricacion = models.DateField()

    def __str__(self):
        return self.nombre
