from django.shortcuts import render, HttpResponse
from django.http import HttpResponse

from familiaapp.models import Familiares, Menues, Ubicaciones
from familiaapp.forms import familiaresformulario, MenuesFormulario

# Create your views here.

    
def familiares (request):
    familias_list = Familiares.objects.all (),
    return render (request,'familiaapp.html', {'familiares' : familias_list})

def inicio (request):
     return render(request, "familiaapp/inicio.html")

def menue (request):
    menues_list = Menues.objects.all (),
    return render(request, 'menues.html' , {'menues' : menues_list})

def ubicación (request):
    ubicación = Ubicaciones.objects.all (),
    return render(request, "familiaapp/ubicaciones.html") 
    
def familiaformulario(request):

    if request.method =='POST':
         miFormulario - familiaresformulario (request.POST)

         print(miFormulario)  


         if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            nombre= Familiares(nombre=informacion['nombre'])

            nombre.save()

            return render (request,"familiaapp/inicio.html")                                                                                                                                                                                                                                                                                                             
        
    else:
        miFormulario= familiaresformulario()

    return render (request,"familiaapp/familiareshformulario.html" , {"miformulario":miFormulario})


