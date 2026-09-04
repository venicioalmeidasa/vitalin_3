
from django.db import models
from django.utils.text import slugify
from ..validators import valida_cpf, valida_dn

class Pessoa(models.Model):
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
    data_cadastro = models.DateTimeField(
        verbose_name='Data do Cadastro',
        auto_now_add=True
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
        self.slug = slugify(self.nome, allow_unicode=True)
        self.full_clean() #garante a execução dos validators
        super().save(*args, **kwargs)
