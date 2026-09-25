from django.utils.text import slugify
from django.db import models
from django.core.exceptions import ValidationError
from .timestamp import TimeStampedModel
from datetime import datetime, timedelta, date

class UnidadeBase(TimeStampedModel):
    #Unidade base para unidades que prestam atenção direta ao usuário
    cnes = models.CharField(
        max_length=12,
        verbose_name='CNES',
        primary_key=True
    )
    nome = models.CharField(
        max_length=120,
        verbose_name='Nome'
    )

    ativo = models.BooleanField(
        default=True,
        verbose_name='Ativo'
    )
    email = models.EmailField(
        verbose_name='email',
        null=True,
        blank=True
    )
    slug = models.SlugField(
        unique=True,
        max_length=120,
        allow_unicode=True,
        help_text='Nome amigável para url'
    )
    class Meta:
        abstract = True
        ordering = ['nome']

    def __str__(self):
        return f'{self.nome} | {self.cnes}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome, allow_unicode=True)
        self.full_clean()
        super().save(*args, **kwargs)
    
class HorarioFuncionamentoBase(TimeStampedModel):
    DIA_CHOICES =[
        (1, 'Segunda-feira'),
        (2, 'Terça-feira'),
        (3, 'Quarta-feira'),
        (4, 'Quinta-feira'),
        (5, 'Sexta-feira'),
        (6, 'Sábado'),
        (0, 'Domingo')
    ]

    dia = models.IntegerField(
        verbose_name='Dia da semana',
        choices=DIA_CHOICES
    )
    hora_abre = models.TimeField(
        verbose_name='Horario de Abertura'
    )
    hora_fecha = models.TimeField(
        verbose_name='Horário de Fechamento'
    )

    class Meta:
        abstract = True
        verbose_name = 'Horário de Funcionamento'
        verbose_name_plural = 'Horários de Funcionamento'

    def clean(self):
        # A unidade deve ficar aberta por um mínimo de 3 horas
        if self.hora_abre and self.hora_fecha:
            hora_abre = datetime.combine(date.today(), self.hora_abre)
            hora_fecha = datetime.combine(date.today(), self.hora_fecha)
            margem_abertura = timedelta(hours=3)
            if hora_fecha < hora_abre:
                raise ValidationError(
                    {
                        'hora_fecha': 'O horário de fechamento não pode ser anterior ao horário de abertura'
                    }
                )
            if hora_fecha <= hora_abre+margem_abertura:
                raise ValidationError(
                    {
                        'hora_fecha': 'O tempo mínimo de abertura do estabelecimento é de 3 horas'
                    }
                )
        super().clean()
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
