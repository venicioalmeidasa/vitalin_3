from django.db import models


class TimeStampedModel(models.Model):
    datetime = models.DateTimeField(
        verbose_name='Datetime cadastro',
        auto_now_add=True
    )
    cadastrante = models.CharField(
        max_length=150,
        verbose_name='Cadastrante',
        default='Desenvolvimento'
    )

    class Meta:
        abstract = True
        ordering = ['datetime']
    
    def __str__(self):
        return f'{self.cadastrante} - {self.datetime}'