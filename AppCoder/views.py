from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso

# Create your views here.
def inicio(request):
    return render(request, "AppCoder/inicio.html")
    #return HttpResponse("Vista Inicio")
def cursos(request):
    return render(request, "AppCoder/cursos.html")
    #return HttpResponse("Vista Cursos")
def profesores(request):
    return render(request, "AppCoder/profesores.html")
    #return HttpResponse("Vista Profesores")
def entregables(request):
    return render(request, "AppCoder/entregables.html")
    #return HttpResponse("Vista Entregables")
def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")
    #return HttpResponse("Vista Estudiantes")