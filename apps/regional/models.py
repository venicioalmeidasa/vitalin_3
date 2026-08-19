from django.db import models
from django.utils.text import slugify
# Create your models here.
class Distrito(models.Model):
    cnes = models.CharField(
        primary_key=True,
        max_length=12,
        verbose_name='CNES'
    )
    nome = models.CharField(
        max_length=120,
        verbose_name='Nome'
    )
    email = models.EmailField(
        verbose_name='email'
    )
    ativo = models.BooleanField(
        default=True,
        verbose_name='Ativo'
    )
    slug = models.SlugField(
        unique=True,
        allow_unicode=True,
        help_text='Nome amigável para url'
    )
    class Meta:
        ordering = ['nome']
    
    def __str__(self):
        return f'Ditrito {self.nome} | {self.cnes}'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome, allow_unicode=True)
        self.full_clean()
        super().save(*args, **kwargs)

