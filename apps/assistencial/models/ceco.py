from django.db import models
from core.models.base_estabelecimento import UnidadeBase

class Ceco(UnidadeBase):
    distrito = models.ForeignKey(
        'regional.Distrito',
        on_delete=models.SET_NULL,
        related_name='cecos',
        verbose_name='Distrito',
        null=True
    )

    class Meta:
        verbose_name = 'Centro de Convivência e Oficina'
        verbose_name_plural = 'Centros de Convivência e Oficinas'


