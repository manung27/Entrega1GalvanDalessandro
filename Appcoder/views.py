
from smtplib import SMTPResponseException
from tkinter.filedialog import Open
from django.shortcuts import render
from django.http import HttpResponse
from .models import Renault
from .models import Ford
from .models import Volkswagen
from django.template import Context, Template
from Appcoder.forms import renault1

def inicio(request):
    return render(request,"Appcoder/inicio.html")

def renault(request):
    renault=Renault(modelo="Kwid", velocidad="127", caballos_fuerza="100")
    renault.save()
    texto=f"Renault: modelo: {renault.modelo} velocidad: {renault.velocidad} caballos_fuerza: {renault.caballos_fuerza}"
def renault(request):
    if request.method=="POST":
        renault=renault1(request.POST)
        print(renault)
        if renault.is_valid():
            info=renault.cleaned_data
            print(info)
            modelo=info.get("modelo")
            velocidad=info.get("velocidad")
            caballos_fuerza=info.get("caballos_fuerza")
            renault=Renault(modelo=modelo,velocidad=velocidad,caballos_fuerza=caballos_fuerza)
            renault.save()
            return render(request,"Appcoder/inicio.html",{"mensaje": "Auto creado"})
        else:
            return render(request, "Appcoder/inicio.html", {"mensaje":"ERROR"})
    else:
        renault=renault1()
        return render(request,"Appcoder/renault.html",{"renault":renault})

def busquedarenault(request):
    return render(request,"Appcoder/inicio.html")  

def buscar(request):
    mode=request.GET["modelo"]
    modelos=Renault.objects.filter(modelo=mode) 
    if len(modelos)!=0:
        return render(request, "Appcoder/resultado.html", {"modelos":modelos})
    else:
        return render(request,"Appcoder/resultado.html", {"mensaje":"No existe su auto"}) 

def volkswagen(request):
    volkswagen=Volkswagen(modelo="Gol", velocidad="127", caballos_fuerza="100")
    volkswagen.save()
    texto=f"Volkswagen: modelo: {volkswagen.modelo} velocidad: {volkswagen.velocidad} caballos_fuerza: {volkswagen.caballos_fuerza}"
    if request.method=="POST":
        modelo=request.POST.get("modelo")
        velocidad=request.POST.get("velocidad")
        caballos_fuerza=request.POST.get("caballos_fuerza")
        volkswagen=Volkswagen(modelo=modelo,velocidad=velocidad,caballos_fuerza=caballos_fuerza)
        volkswagen.save()
        return render(request,"Appcoder/inicio.html",{"mensaje": "Auto creado"})
    return render(request,"Appcoder/volkswagen.html") 
    


def autoford(request): #formulario por html
    return render(request, "Appcoder/autoford.html")
     
def ford(request): #formulario por html
    ford=Ford(modelo="Fiesta", velocidad="127", caballos_fuerza="100")
    ford.save()
    texto=f"Ford: modelo: {ford.modelo} velocidad: {ford.velocidad} caballos_fuerza: {ford.caballos_fuerza}"
    if request.method=="POST":
        modelo=request.POST.get("modelo")
        velocidad=request.POST.get("velocidad")
        caballos_fuerza=request.POST.get("caballos_fuerza")
        ford=Ford(modelo=modelo,velocidad=velocidad,caballos_fuerza=caballos_fuerza)
        ford.save()
        return render(request,"Appcoder/inicio.html",{"mensaje": "Auto creado"})
    return render(request,"Appcoder/ford.html")





    