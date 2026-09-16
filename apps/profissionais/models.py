from django.db import models
from typing import TypedDict
from core.models.timestamp import TimeStampedModel
from django.core.exceptions import ValidationError


class DadosConselho(TypedDict):
    descricao: str
    profissoes: list[tuple[str,str]]
    
class OcupacaoCBO(TimeStampedModel):
    #Caso a profissão possua conselho
    ESTRUTURA_CONSELHOS:dict[str, DadosConselho] = {
        'CRM': {
            'descricao': 'Conselho Regional de Medicina',
            'profissoes': [
                ('Clínico Geral', '225125'),
                ('Psiquiatra', '225133'),
                ('Ginecologista/Obstetra', '225250'),
                ('Pediatra', '225124'),
                ('Urologista', '225285'),
                ('Neurologista', '225112'),
                ('Cardiologista', '225120'),
                ('Angiologista', '225103'),
                ('Endocrinologista', '225135'),
                ('Hematologista', '225121'),
                ('Mastologista', '225260'),
                ('Nefrologista', '225109'),
                ('Neurocirurgião', '225265'),
                ('Pneumologista', '225115'),
                ('Coloproctologista', '225215'),
                ('Reumatologista', '225145'),
                ('Ortopedista/Traumatologista', '225270'),
            ]
        },
        'COREN': {
            'descricao': 'Conselho Regional de Enfermagem',
            'profissoes': [
                ('Enfermeiro', '223505'),
                ('Tec Enfermagem', '322205'),
            ]
        },
        'CRP': {
            'descricao': 'Conselho Regional de Psicologia',
            'profissoes': [
                ('Psicólogo', '251510'),
            ]
        },
        'CRO': {
            'descricao': 'Conselho Regional de Odontologia',
            'profissoes': [
                ('Cirurgião Dentista', '223208'),
            ]
        },
        'CRN': {
            'descricao': 'Conselho Regional de Nutrição',
            'profissoes': [
                ('Nutricionista', '223710'),
            ]
        },
        'CREFITO': {
            'descricao': 'Conselho Reg. de Fisioterapia e Terapia Ocupacional',
            'profissoes': [
                ('Fisioterapeuta', '223605'),
                ('Terapeuta Ocupacional', '223905'),
            ]
        },
        'CRF': {
            'descricao': 'Conselho Regional de Farmácia',
            'profissoes': [
                ('Farmacêutico', '223405'),
            ]
        },
        'CRBM': {
            'descricao': 'Conselho Regional de Biomedicina',
            'profissoes': [
                ('Biomédico', '221205'),
            ]
        },
        'CRBio': {
            'descricao': 'Conselho Regional de Biologia',
            'profissoes': [
                ('Biólogo', '221105'),
            ]
        },
        'CREF': {
            'descricao': 'Conselho Regional de Educação Física',
            'profissoes': [
                ('Educador Física', '224140'),
            ]
        },
        'CRESS': {
            'descricao': 'Conselho Regional de Serviço Social',
            'profissoes': [
                ('Assistente Social', '251605'),
            ]
        },
        'CRMV': {
            'descricao': 'Conselho Regional de Medicina Veterinária',
            'profissoes': [
                ('Veterinário', '223305'),
            ]
        },
        'CREFONO': {
            'descricao': 'Conselho Regional de Fonoaudiologia',
            'profissoes': [
                ('Fonoaudiólogo', '223810'),
            ]
        },
    }
    
    #Conselhos e descrição em si
    TIPOS_CONSELHO_CHOICES:list = [
        (sigla, dados["descricao"]) for sigla, dados in ESTRUTURA_CONSELHOS.items()
        ]
    # Profissões sem conselhos
    PROFISSOES_SEM_CONSELHO:list[tuple[str,str]] = [
        ('Agente Administrativo', 'Agente Administrativo')
    ]
    
    # Extrai o nome de cada profissão dentro dos conselhos (Formato: ('Nome', 'Nome'))
    PROFISSOES_COM_CONSELHO:list[tuple[str,str]] = [
        (tupla_prof[0], tupla_prof[0]) 
        for sigla, dados in ESTRUTURA_CONSELHOS.items() 
        for tupla_prof in dados['profissoes']
    ]
    
    # Unifica as duas listas para o Choices
    PROFISSOES_CHOICES:list[tuple[str,str]] = PROFISSOES_SEM_CONSELHO + PROFISSOES_COM_CONSELHO
    PROFISSOES_CHOICES.sort()
    

    profissao = models.CharField(
        max_length=150,
        verbose_name='Profissão',
        choices=PROFISSOES_CHOICES
    )
    conselho = models.CharField(
        max_length=10,
        verbose_name='Conselho',
        choices=TIPOS_CONSELHO_CHOICES,
        blank=True,
        null=True
    )
    cbo = models.CharField(
        max_length=6,
        primary_key=True,
        verbose_name='CBO'
    )

   
    
    class Meta:
        verbose_name = 'Ocupação CBO'
        verbose_name_plural = 'Ocupações CBOs'
        ordering = ['profissao']
    
    def __str__(self):
        return f"{self.profissao} | {self.cbo}"
    
    def clean(self):
        super().clean()
        # Em branco para profissões sem conselho
        
        if self.profissao and self.conselho:
            raise ValidationError(f'Para {self.profissao} não pode haver conselho')
        
        # Verificando se a profissão pertence ao referido conselho
        if self.profissao and self.conselho:
            dados_conselho = self.ESTRUTURA_CONSELHOS.get(self.conselho, {})
            lista_profissao_cbo = dados_conselho.get('profissoes', [])
            lista_profissao = [prof[0] for prof in lista_profissao_cbo]

            if self.profissao not in lista_profissao:
                raise ValidationError(f'Profissão {self.profissao} não cadastrada no conselho {self.conselho}')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


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

    