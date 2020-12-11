from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def prueba(request):
    return render(request,'miplantilla.html')

def paginakpop(request):
    return render(request, 'propiedades_ubicación.html')
