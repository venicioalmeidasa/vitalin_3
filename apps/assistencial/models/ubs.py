from django.db import models
from core.models.base_estabelecimento import UnidadeBase


# Create your models here.
class Ubs(UnidadeBase):
    #Unidades Básicas de Saúde - atenção primaria
    distrito = models.ForeignKey(
        'regional.Distrito',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='ubss'
    )
    nome_oficial = models.CharField(
        max_length=75,
        verbose_name='Nome Oficial',
    )
    class Meta(UnidadeBase.Meta):
        verbose_name = 'Unidade Básica de Saúde'
        verbose_name_plural = 'Unidades Básicas de Saúde'


