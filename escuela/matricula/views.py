from django.shortcuts import render, redirect, get_object_or_404
from .models import Alumno
from .models import Curso
from .forms import AlumnoForm, CursoForm, altaUser
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

def vista_landing(request):
    return render(request, "landing.html")

def vista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, "lista_alumnos.html", {'alumnos':alumnos})

def vista_cursos(request):
    alumno = Alumno.objects.get(Alumno, usuario=request.user)
    cursos = alumno.curso.all()
    return render(request, "lista_cursos.html", {'cursos':cursos})

def filtro(request, id_cursos):
    lista = Alumno.objects.filter(curso__abrev=id_cursos)
    return render(request, "alumnos_por_cursos.html", {'alumnos':lista})

def alta_alumno(request):
    if request.POST:
        form = altaUser(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            dni = form.cleaned_data['dni']
            nombre = form.cleaned_data['nombre']
            apellidos = form.cleaned_data['apellidos']
            curso = form.cleaned_data['curso']
            user = User.objects.create_user(email=email, username=username, password=password)
            alumno = Alumno.objects.create(user = user, dni=dni, nombre=nombre, apellidos=apellidos, curso=curso)
            alumno.save()
            print(f"Se ha creado a: {alumno}")

            return redirect('/cursos/'+alumno.curso.abrev)
        else:
            return render(request, "alta_alumno.html",{'form':form})
    else:
        form = altaUser()
        return render(request, "alta_alumno.html",{'form':form})

def alta_curso(request):
    if request.POST:
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            nuevo_curso=form.save()
            print(f"Se ha creado a: {nuevo_curso}")
    
            return redirect('/cursos/'+nuevo_curso.abrev)
        else:
            return render(request, "alta_curso.html",{'form':form})
    else:
        form = CursoForm()
        return render(request, "alta_curso.html",{'form':form})

def view_404(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request,'404.html', data)




def altaUsuario(request):
    form = altaUser(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        dni = form.cleaned_data['dni']
        nombre = form.cleaned_data['nombre']
        apellidos = form.cleaned_data['apellidos']
        curso = form.cleaned_data['curso']
        user = User.objects.create_user(email=email, username=username, password=password)
        alumno = Alumno.objects.create(user = user, dni=dni, nombre=nombre, apellidos=apellidos, curso=curso)
        alumno.save()
    else:
        return render(request, "alta_usuario.html",{'form':form})