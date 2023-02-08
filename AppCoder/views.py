from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso

# Create your views here.
def inicio(request):
    return HttpResponse("Vista Inicio")
def cursos(request):
    return HttpResponse("Vista Cursos")
def profesores(request):
    return HttpResponse("Vista Profesores")
def entregables(request):
    return HttpResponse("Vista Entregables")
def estudiantes(request):
    return HttpResponse("Vista Estudiantes")