from django.shortcuts import render
from appfoodie.models import Restaurante

def index(request):
    return render(request, "appfoodie/home.html")

def mostrar_restaurantes(request):
  lista_restaurantes = Restaurante.objects.all()
  return render(request, "appfoodie/restaurantes.html", {"lista_restaurantes": lista_restaurantes})