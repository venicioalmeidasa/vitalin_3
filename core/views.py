from django.core.checks import model_checks
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models.pessoa import Pessoa
from .forms import PessoaForm
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Página Core configurada')

class PessoaCreateView(LoginRequiredMixin, CreateView):
    model = Pessoa
    form_class = PessoaForm
    template_name = 'core/pessoa_form.html'
    
    #Somente se a get_success_url falhar
    sucess_url = ''

    def get_initial(self):
        initial = super().get_initial()
        return initial
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['usuario']
