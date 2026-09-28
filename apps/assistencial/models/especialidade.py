from django.db import models
from core.models.base_estabelecimento import UnidadeBase, HorarioFuncionamentoBase


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

class HorarioEspecialidade(HorarioFuncionamentoBase):
    especialidade = models.ForeignKey(
        Especialidade,
        on_delete=models.CASCADE,
        verbose_name='Horários Especialide',
        related_name='horarios'
    )