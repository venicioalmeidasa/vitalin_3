from .models import Distrito
from django.views.generic import ListView, DetailView
# Create your views here.

class DistritoList(ListView):
    model = Distrito
    context_object_name = 'distritos'
    template_name = 'regional/distritos.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_distritos'] = self.get_queryset().count()

        return context

class DistritoDetail(DetailView):
    model = Distrito
    template_name = 'regional/distrito.html'
    context_obect_name = 'distrito'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ubss'] = self.object.ubss.all()
        context['num_ubss'] = context['ubss'].count()
        return context
        




    
