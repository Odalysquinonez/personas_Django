from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Bienvenido (request):
    return render(request,"bienvenido.html")

def Contacto (request):
    return HttpResponse("Mi nombre es Odalys y mi telefono es 0967605159")

def Chao (request):
    return HttpResponse("Chao Mundo")