from django.db import models
from core.models.timestamp import TimeStampedModel
# Create your models here.
class OcupacaoCBO(models.Model):
    TIPOS_CONSELHO_CHOICES = [
        ('CRM', 'Conselho Regional de Medicina'),
        ('COREN', 'Conselho Regional de Enfermagem'),
        ('CRP', 'Conselho Regional de Psicologia'),
        ('CRO', 'Conselho Regional de Odontologia'),
        ('CRN', 'Conselho Regional de Nutrição'),
        ('CREFITO', 'Conselho Reg. de Fisioterapia e Terapia Ocupacional'),
        ('CRF', 'Conselho Regional de Farmácia'),
        ('CRBM', 'Conselho Regional de Biomedicina'),
        ('CRBio', 'Conselho Regional de Biologia'),
        ('CREF', 'Conselho Regional de Educação Física'),
        ('CRESS', 'Conselho Regional de Serviço Social'),
        ('CRMV', 'Conselho Regional de Medicina Veterinária'),
        ('CREFONO', 'Conselho Regional de Fonoaudiologia'),
    ]
    
    cbo = models.CharField(
        max_length=6,
        primary_key=True
    )
    profissao = models.CharField(
        max_length=150,
        verbose_name='Profissão'
    )
    conselho = models.CharField(
        max_length=10,
        verbose_name='Conselho',
        choices=TIPOS_CONSELHO_CHOICES,
        blank=True,
        null=True
    )
    
    def __str__(self):
        return f"{self.cbo} - {self.profissao}"


class Profissionais(TimeStampedModel):
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
        OcupacaoCBO,
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

    