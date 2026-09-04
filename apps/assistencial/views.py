from django.views.generic import ListView, DetailView
from .models import Ubs, Especialidade
# Create your views here.

class Ubss(ListView):
    model = Ubs
    context_object_name = 'ubss'
    template_name = 'assistencial/ubs/ubss.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_ubss'] = self.get_queryset().count()
        return context

class Ubs(DetailView):
    model = Ubs
    context_object_name = 'ubs'
    template_name = 'assistencial/ubs/ubs.html'

class Especialidades(ListView):
    model = Especialidade 
    context_object_name = 'especialidades'
    template_name = 'assistencial/especialidade/especialidades.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_especialidades'] = self.get_queryset().count()
        return context

class Especialidade(DetailView):
    model = Especialidade
    context_object_name = 'especialidade'
    template_name = 'assistencial/especialidade/especialidade.html'
