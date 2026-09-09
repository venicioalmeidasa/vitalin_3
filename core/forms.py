from django import forms
from .models import Pessoa

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa

        fields = [
            'nome',
            'dn',
            'nome_social',
            'sexo',
            'mae',
            'pai',
            'cpf',
        ]
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'dn': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'cpf': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': '000.000.000-00',
                'maxlength':'14',
                'autocomplete': 'off'
            }),
            'nome_social': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome social *opcional'
            }),
            'sexo': forms.Select(attrs={
                'class': 'form-select'
            }),
            'mae': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome da Mãe'
            }),
            'pai': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome do Pai'
            }),
        }

        def limpa_cpf(self):
            import re
            #Limpa o CPF antes do envio ao model
            cpf = self.cleaned_data('cpf','')
            return re.sub(r'\D', '', str(cpf))