from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import * #FALTA ALGO

# Create your views here.
def curso(self):
    curso = Curso(nombre="Desarrollo Web", comision=19881)
    curso.save()
    documentodeTexto = f"--> Curso: {curso.nombre} Comision: {curso.comision}"
    return HttpResponse(documentodeTexto)