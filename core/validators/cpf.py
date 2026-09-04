
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def valida_cpf(cpf:str) -> None:
    
    #Limpa CPF
    cpf_limpo = re.sub(r'\D', '',str(cpf or '')).strip()
    #Verifica tamanho e valores numéricos
    if len(cpf_limpo) != 11 or not cpf_limpo.isnumeric():
        raise ValidationError (_('CPF inválido'), code='cpf_invalido')

    #verifica número iguais
    if cpf_limpo[0] * 11 == cpf_limpo:
        raise ValidationError (_('CPF com números iguais é inválido'), code='cpf_digitos_repetidos')

    #Primeiro dígito verificador
    s=0
    for i, n in enumerate(cpf_limpo[:9]):
        s += (int(n)*(10-i))
    resto_div = s % 11
    digito1 = 11 - resto_div if resto_div > 1 else 0
    if digito1 != int(cpf_limpo[-2]):
        raise ValidationError (_('CPF inválido'), code='digito1_invalido')

    #Segundo dígito verificador
    s=0
    for i, n in enumerate(cpf_limpo[:-1]):
        s += (int(n)*(11-i))
    resto_div  = s % 11
    digito2 = 11 - resto_div if resto_div > 1 else 0
    if digito2 != int(cpf_limpo[-1]):
        raise ValidationError (_('CPF inválido'), code='digito2_invalido')



    


