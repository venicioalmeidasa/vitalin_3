
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def valida_fone(numero:str):
    #Verifica existência de letras
    if re.search(r'[^\d\(\)\-\s]', numero):
        raise ValidationError(
            _('O número do telefone não deve conter letras!'),
            code='letra_fone'
        )
    #Retira qualquer caracter não numérico
    num = re.sub(r'\D','', numero).strip()
    num = num if num.startswith('0') else '0' + num

    #Verifica se há zero no segundo e o terceiro dígico
    if '0' in num[1:3]:
        raise ValidationError(
            _('DDD inválido'),
            code='ddd_fone'
        )
        
    #Tamanho exclusivo numérico de 12 dígitos
    if len(num) != 12:
        raise ValidationError(
            _('O número deve conter 12 dígitos'),
            code='tamanho_fone'
        )
