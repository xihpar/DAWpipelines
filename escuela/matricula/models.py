from django.db import models
from django.core.files.images import get_image_dimensions
from django.contrib.auth.models import User

class Alumno(models.Model):
    #usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    dni = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=60)
    imagen = models.ImageField(null=True, upload_to="fotos/")
    #curso = models.ManyToManyField('Curso', null=True)
    
    def __str__(self):
        return f"{self.apellidos}, {self.nombre}"

    def imgWeight(self):
        w, h = get_image_dimensions(self.imagen)
        return w


class Curso(models.Model):
    abrev = models.CharField(max_length=10, primary_key=True)
    denom = models.CharField(max_length=40)
    imagen = models.ImageField(null=True, upload_to="fotos/")

    def __str__(self):
        return self.denom

    def imgWeight(self):
        w, h = get_image_dimensions(self.imagen)
        return w


