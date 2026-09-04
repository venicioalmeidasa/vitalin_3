from datetime import date
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def valida_dn(data:date) -> None:
    if data > date.today():
        raise ValidationError (_('A data de nasicmento não pode ser uma data futura'), code='dn_futura')