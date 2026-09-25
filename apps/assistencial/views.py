from django.views.generic import ListView, DetailView
from apps.assistencial.models import Ubs, Especialidade, Ceco
# Create your views here.

class UbssList(ListView):
    model = Ubs
    context_object_name = 'ubss'
    template_name = 'assistencial/ubs/ubss.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_ubss'] = self.get_queryset().count()
        return context

class UbsDetail(DetailView):
    model = Ubs
    context_object_name = 'ubs'
    template_name = 'assistencial/ubs/ubs.html'

class EspecialidadesList(ListView):
    model = Especialidade 
    context_object_name = 'especialidades'
    template_name = 'assistencial/especialidade/especialidades.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_especialidades'] = self.get_queryset().count()
        return context

class EspecialidadeDetail(DetailView):
    model = Especialidade
    context_object_name = 'especialidade'
    template_name = 'assistencial/especialidade/especialidade.html'

class CecosList(ListView):
    model = Ceco
    context_object_name = 'cecos'
    template_name = 'assistencial/ceco/cecos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_cecos'] = self.get_queryset().count()
        return context

class CecoDetail(DetailView):
    pass

