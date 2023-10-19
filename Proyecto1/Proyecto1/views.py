from django.http import HttpResponse #Necesario para crear las vistas
import datetime #Necesario para trabajar con fechas
from django.template import Template, Context #Necesario para trabajar con plantillas
from django.template.loader import get_template #Necesario para poder evitar la forma larga de cargar la plantilla para renderizarla
from django.shortcuts import render #Necesario para renderizar
import random #Necesario para generar numeros random

class Habitante(object):

    def __init__(self, nombre, apellido, nacimiento, ciudad):

        self.nombre=nombre
        self.apellido=apellido
        self.nacimiento=nacimiento
        self.ciudad=ciudad

def saludo(request): #Primera vista

    return HttpResponse("Hola mundo, esta es la primera página con Django")

def despedida(request): #Segunda vista
    return HttpResponse("Me voy a dormir")

def perdidos(request): #Tercera vista
    return HttpResponse("Nos hemos perdido cuando nos ibamos a dormir")

def fecha(request): #Cuarta vista

    fecha_actual=datetime.date.today()

    enddate=datetime.date(fecha_actual.year, 12, 31)

    calculo = enddate-fecha_actual

    document = """
    <html>
    <body>
    <table>
    <tr><td>La fecha de hoy: </td><td><b>%s</b></td></tr>
    </table>
    <p>Faltan %s para acabar</p>
    </body>
    </html>

    """%(fecha_actual,calculo)



    return HttpResponse(document)

def calcularEdad(request, agno): #Quinta vista

    nombre='Beatriz'
    nacimiento=1997

    edad=agno-nacimiento

    documento = """
     <html>
    <body>
    <p>
    Me llamo %s y tengo %s años
    </p>
    </body>
    </html>
    """%(nombre, edad)

    return HttpResponse(documento)

def primeraplantilla(request): #Primera plantilla

    #Datos
    currenttime=datetime.datetime.now()
    alumno=Habitante("Beatriz", "Vélez", "1997", "Badalona")
    subjectsdaw=["entornos de desarrollo", "despliegue de aplicaciones web", "desarrollo de entorno cliente", "desarollo de entorno servidor", "diseño de interfaces web"]
    # newlist=["perritos", "gatitos", "tortugas", "hamsters", "ratas"]
    newlist=[]
    listrandom=range(50) #Generar número aleatorio de 0 a 49

    #Cargar la plantilla para renderizarla
        # doc_externo=open('C:/Users/Administrator/Documents/projectodjango/Proyecto1/Proyecto1/templates/template.html')
        # template=Template(doc_externo.read())
        # doc_externo.close()
        # ctx=Context({"newlist":newlist, "subjectsdaw":subjectsdaw, "currenttime":currenttime, "nombre_alumno":alumno.nombre, "apellido_alumno":alumno.apellido, "nacimiento_alumno":alumno.nacimiento, "ciudad_alumno":alumno.ciudad})
        # documento=template.render(ctx)

    #Nueva forma para cargar plantillas con LOADER  
        # doc_externo=get_template('template.html') #Recuerda que en settings declaraste la ruta donde se almacenan todas las plantillas
        # documento=doc_externo.render({"newlist":newlist, "subjectsdaw":subjectsdaw, "currenttime":currenttime, "nombre_alumno":alumno.nombre, "apellido_alumno":alumno.apellido, "nacimiento_alumno":alumno.nacimiento, "ciudad_alumno":alumno.ciudad})
        # return HttpResponse(documento)

    # Nueva forma para renderizar plantillas con RENDER
    return render(request, "template.html", {"listrandom":listrandom,"newlist":newlist, "subjectsdaw":subjectsdaw, "currenttime":currenttime, "nombre_alumno":alumno.nombre, "apellido_alumno":alumno.apellido, "nacimiento_alumno":alumno.nacimiento, "ciudad_alumno":alumno.ciudad})

def cursoDjango(request):
    
    #Datos
    currenttime=datetime.datetime.now()

    return render(request, "cursoDjango.html", {"currentData": currenttime})

def plantillaExperimento(request):

    return render(request, "experimentos.html")

