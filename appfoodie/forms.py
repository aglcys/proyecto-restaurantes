from django import forms
from appfoodie.models import Restaurante

class Buscar(forms.Form):
      nombre = forms.CharField(max_length=100)

