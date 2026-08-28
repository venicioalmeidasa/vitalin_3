from django.utils.text import slugify
from django.db import models

# Create your models here.
class Ubs(models.Model):
    #Unidades Básicas de Saúde - atenção primaria
    cnes = models.CharField(
        max_length=12,
        verbose_name='CNES',
        primary_key=True
    )
    distrito = models.ForeignKey(
        'regional.Distrito',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='ubss'
    )
    nome = models.CharField(
        max_length=75,
        verbose_name='Nome'
    )
    nome_oficial = models.CharField(
        max_length=75,
        verbose_name='Nome Oficial',
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
        verbose_name='email'
    )
    slug = models.SlugField(
        unique=True,
        allow_unicode=True,
        help_text='Nome amigável para url'
    )
    class Meta:
        ordering = ['nome']

    def __str__(self):
        return f'{self.nome} | {self.cnes}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome, allow_unicode=True)
        self.full_clean()
        super().save(*args, **kwargs)
