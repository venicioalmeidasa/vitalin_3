from datetime import date
from faker import Faker
from profissionais.models import OcupacaoCBO, Profissionais
#Mapear as conselhos
conselhos = OcupacaoCBO.TIPOS_CONSELHO_CHOICES
sigla_conselho = [conselho[0] for conselho in conselhos]