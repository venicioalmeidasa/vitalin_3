from django.db import models
from core.models.base_estabelecimento import UnidadeBase


class Especialidade(UnidadeBase):
    # Atenção secundária referenciada
    vinculo = models.CharField(
        max_length=120,
        verbose_name='Vínculo'
    )
    sigla = models.CharField(
        max_length=30,
        verbose_name='Sigla',
        null=True,
        blank=True
    )
    class Meta(UnidadeBase.Meta):
        verbose_name = 'Especialidade'
        verbose_name_plural = 'Especialidades'
    