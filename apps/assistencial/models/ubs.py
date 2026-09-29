from django.db import models
from core.models.base_estabelecimento import UnidadeBase, HorarioFuncionamentoBase


# Create your models here.
class Ubs(UnidadeBase):
    #Unidades Básicas de Saúde - atenção primaria
    distrito = models.ForeignKey(
        'regional.Distrito',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='ubss',
        verbose_name='Distrito'
    )
    nome_oficial = models.CharField(
        max_length=75,
        verbose_name='Nome Oficial',
    )
    class Meta(UnidadeBase.Meta):
        verbose_name = 'Unidade Básica de Saúde'
        verbose_name_plural = 'Unidades Básicas de Saúde'
       

class HorarioUbs(HorarioFuncionamentoBase):
    ubs = models.ForeignKey(
        Ubs,
        on_delete=models.CASCADE,
        verbose_name='Unidade Básica de Saúde',
        related_name='horarios'
    )
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['ubs', 'dia'],
                name='unique_ubs_dia',
                violation_error_message='Já existe horario cadastrado para este dia na referida UBS'
            )
        ]