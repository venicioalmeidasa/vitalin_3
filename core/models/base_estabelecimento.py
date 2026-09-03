from django.utils.text import slugify
from django.db import models

class UnidadeBase(models.Model):
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
    data_cadastro = models.DateField(
        verbose_name='Data do Cadastro',
        auto_now_add=True
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