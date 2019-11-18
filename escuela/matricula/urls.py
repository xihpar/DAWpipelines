from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf.urls import handler404

urlpatterns = [
    path('alumnos', views.vista_alumnos, name='Lista de alumnos'),
    path('cursos', views.vista_cursos, name='Lista de cursos'),
    path('cursos/<id_cursos>', views.filtro, name='Lista de alumnos filtrada por cursos'),
    path('nuevo/alumno/', views.alta_alumno, name='Alta alumno'),
    path('nuevo/curso/', views.alta_curso, name='Alta curso'),
    path('', views.vista_landing, name='landing'),
]