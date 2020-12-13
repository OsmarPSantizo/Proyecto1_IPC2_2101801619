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

def pagosc(request):
    return render(request,'pagosc.html')

def pagose(request):
    return render(request,'pagose.html')

def pagos1(request):
    return render(request,'pagos1.html')

def pagos2(request):
    return render(request,'pagos2.html')

def gestiones(request):
    return render(request,'gestiones.html')

def preauto(request):
    return render (request,'preauto.html')

def prestamos(request):
    return render (request,'prestamo.html')
    
def addcuenta(request):
    return render (request,'addcuenta.html')