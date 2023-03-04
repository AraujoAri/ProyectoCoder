from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse

#esto es una prueba de git, no tiene nada importante.

def curso(self):
    curso = Curso(nombre='desarrollo web', camada=12345)
    curso.save()
    documentodetexto = f'--->curso: {curso.nombre} \ncamada: {curso.camada}'

    return HttpResponse(documentodetexto)