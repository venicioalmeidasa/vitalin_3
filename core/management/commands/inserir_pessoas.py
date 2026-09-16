from faker import Faker
import random
from django.utils.text import slugify
import re
import uuid
from core.models.pessoa import Pessoa
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Popula o banco de dados de pessoas cível - N: 20000'
    
    def handle(self, *args, **options):
        fake = Faker('pt_BR')
        self.stdout.write('Iniciando criação de pessoas')
        pessoas = []
        for _ in range(20000):
            sexo_fake = random.choice(Pessoa.Sexo.values)
            nome_fake = fake.name_male() if sexo_fake.casefold() == 'm' else fake.name_female()
            #Limpa CPF
            cpf_fake = fake.unique.cpf()
            cpf_limpo = re.sub(r'\D', '',cpf_fake)

            novapessoa = Pessoa(
                nome=nome_fake,
                mae=fake.name_female(),
                pai=fake.name_male(),
                sexo=sexo_fake,
                cpf=cpf_limpo,
                dn=fake.date_of_birth(minimum_age=18, maximum_age=60),
                cadastrante='Desenvolvimento',
                slug=slugify(f'{nome_fake}-{uuid.uuid4()}', allow_unicode=True)
            )
            pessoas.append(novapessoa)
        pessoas_criadas = Pessoa.objects.bulk_create(pessoas, ignore_conflicts=True)
        self.stdout.write(self.style.SUCCESS('20000 pessoas criadas no BD com sucesso!'))

        pessoas_nome_social = []
        for _ in range(800):
            pessoa_escolhida = random.choice(pessoas_criadas)
            sexo = pessoa_escolhida.sexo
            pessoa_escolhida.nome_social = fake.name_male() if sexo.casefold() == 'f' else fake.name_female()
            pessoas_nome_social.append(pessoa_escolhida)
        Pessoa.objects.bulk_update(pessoas_nome_social, fields=['nome_social'])
        
        self.stdout.write(self.style.SUCCESS('Atribuidos 800 nomes sociais a pessoas de forma aleatória!'))

        self.stdout.write(self.style.SUCCESS('Operação finalida!'))
        
            