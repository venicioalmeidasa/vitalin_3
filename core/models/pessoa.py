
from django.core.exceptions import ValidationError
from django.db import models
import uuid
from .timestamp import TimeStampedModel
from django.utils.text import slugify
from core.validators import valida_dn, valida_cpf, valida_fone

class Pessoa(TimeStampedModel):
    class Sexo(models.TextChoices):
        MASCULINO = 'm', 'Masculino'
        FEMININO = 'f', 'Feminino'

    #Entidade para pessoa cível
    nome = models.CharField(
        max_length=150,
        verbose_name='Nome completo'
    )
    nome_social = models.CharField(
        max_length=150,
        verbose_name='Nome Social',
        null=True,
        blank=True
    )
    mae = models.CharField(
        max_length=150,
        verbose_name='Nome da Mãe',
        blank=True,
        null=True
    )
    pai = models.CharField(
        max_length=150,
        verbose_name='Nome do Pai',
        blank=True,
        null=True
    )
    sexo = models.CharField(
        max_length=1,
        choices=Sexo.choices,
        verbose_name='Sexo'
    )
    cpf = models.CharField(
        max_length=11,
        verbose_name='CPF',
        primary_key=True,
        validators=[valida_cpf]
    )
    dn = models.DateField(
        verbose_name='Data de Nascimento',
        validators=[valida_dn]
    )
    slug = models.SlugField(
        unique=True,
        max_length=200,
        allow_unicode=True
    )
   

    class Meta:
        ordering = ['nome']
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
    
    def __str__(self):
        return self.nome_social if self.nome_social else self.nome
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.nome}-{str(uuid.uuid4())[:8]}', allow_unicode=True)
        self.full_clean() #garante a execução dos validators
        super().save(*args, **kwargs)


class Telefone(models.Model):
    class Vinculo(models.TextChoices):
        PROPRIO = 'proprio', 'Próprio'
        PAI = 'pai', 'Pai'
        MAE = 'mae', 'Mãe'
        FILHO = 'filho', 'Filho' 
        CONJUGE = 'conjuge', 'Cônjuge'

    fone = models.CharField(
        max_length=15,
        primary_key=True,
        verbose_name='Número do telefone',
        validators=[valida_fone],
        help_text='(DDD)123456789'
    )
    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        verbose_name=Pessoa
    )
    nome_contato = models.CharField(
        max_length=100,
        verbose_name='Nome do contato',
        null=True,
        blank=True
    )
    vinculo = models.CharField(
        max_length=15,
        choices=Vinculo.choices,
        default=Vinculo.PROPRIO,
        verbose_name='Vinculo',
        null=True,
        blank=True
    )
    wa = models.BooleanField(
        verbose_name='Whatsapp',
        default=True
    )

    def clean(self):
        super().clean()
        #Caso vinculo diferente de prório o nome_contato é obrigatório
        if self.vinculo != self.Vinculo.PROPRIO and not self.nome_contato:
            raise ValidationError({
                'nome_contato': 'O nome do contato é obrigatório!'
            })
        if self.vinculo == self.Vinculo.PROPRIO and (self.nome_contato and self.nome_contato.strip()):
            raise ValidationError({
                'nome_contato': 'O telefone está cadastrado como próprio, esse campo deve estar vazio'
            })
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

        
