from django.views.generic import ListView, DetailView
from .models import Ubs
# Create your views here.

class Ubss(ListView):
    model = Ubs
    context_object_name = 'ubss'
    template_name = 'assistencial/ubss.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_ubss'] = self.get_queryset().count()
        return context

class Ubs(DetailView):
    model = Ubs
    conext_object_name = 'ubss'
    template_name = 'assistencial/ubs.html'