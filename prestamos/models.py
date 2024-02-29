from django.db import models

# Create your models here.


class Persona(models.Model):
    name = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    secondname = models.CharField(max_length=50)


class Prestamo(models.Model):
    amount = models.FloatField()

class Solicitud(models.Model):
    persona_id = models.ForeignKey(Persona, on_delete=models.CASCADE)
    prestamo_id = models.ForeignKey(Prestamo, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class RawSolicitud(models.Model):
    raw_data = models.CharField(max_length=500)
    origin = models.CharField(max_length=20)
    solicitud_id = models.ForeignKey(Solicitud, on_delete=models.CASCADE)
