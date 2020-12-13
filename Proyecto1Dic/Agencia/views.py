from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def prueba(request):
    return render(request,'miplantilla.html')

def paginakpop(request):
    return render(request, 'propiedades_ubicación.html')

def esqueleto(request):
    return render(request,'esqueleto.html')

def inicio(request):
    return render(request,'inicio.html')

def transferencia(request):
    return render(request,'transferencia.html')


def pagos(request):
    return render(request,'pagos.html')
