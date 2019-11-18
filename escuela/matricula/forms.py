from django.forms import ModelForm
from django import forms
from .models import Alumno, Curso

class altaUser(forms.Form):
    email = forms.CharField(max_length=50)
    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput)
    dni = forms.CharField(max_length=9)
    nombre = forms.CharField(max_length=20)
    apellidos = forms.CharField(max_length=60)
    class Meta:
        model = Alumno
        fields = ['imagen', 'curso']

class AlumnoForm(ModelForm):
    class Meta:
        model = Alumno
        fields = ['dni', 'nombre', 'apellidos', 'imagen', 'curso']

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = ['abrev', 'denom', 'imagen']