from django.shortcuts import render
from .models import Distrito
from django.views.generic import ListView, DetailView
# Create your views here.

class DistritoView(ListView):
    model = Distrito
    context_object_name = 'distritos'
    template_name = 'regional/distritos.html'

    
