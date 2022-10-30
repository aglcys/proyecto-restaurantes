from django.shortcuts import render
from appfoodie.models import Restaurante
from django.views import View
from appfoodie.forms import Buscar


def index(request):
    return render(request, "appfoodie/home.html")

def mostrar_restaurantes(request):
  lista_restaurantes = Restaurante.objects.all()
  return render(request, "appfoodie/restaurantes.html", {"lista_restaurantes": lista_restaurantes})

class BuscarRestaurante(View):

    form_class = Buscar
    template_name = 'appfoodie/buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_restaurantes = Restaurante.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_restaurantes':lista_restaurantes})
        return render(request, self.template_name, {"form": form})

    def index(request):
        return render(request, 'appfoodie/index.html')