from core.models.timestamp import TimeStampedModel
from django.db import models


class Profissional(TimeStampedModel):
    pessoa = models.OneToOneField(
        'core.Pessoa',
        on_delete=models.PROTECT,
        related_name='profissional',
    )
    matricula = models.CharField(
        primary_key=True,
        max_length=50,
        verbose_name='Matrícula'
    )
    data_contratacao = models.DateField(
        verbose_name='Data da Contratação'
    )
    ocupacao = models.ForeignKey(
        'profissionais.OcupacaoCBO',
        on_delete=models.PROTECT,
        related_name='profissionais',
        verbose_name='Ocupação (CBO)'
    )
    num_conselho = models.CharField(
        max_length=50,
        verbose_name='Número do Conselho',
        blank=True,
        null=True
    )
    
    class Meta:
        verbose_name = 'Profissional'
        verbose_name_plural = 'Profissionais'
        ordering =['pessoa__nome']
    
    def __str__(self):
        return f'{self.pessoa} | {self.ocupacao.profissao} {self.ocupacao.cbo}'
