
from django.core.management import BaseCommand, CommandError
from core.models.pessoa import Pessoa, Telefone
import random
from faker import Faker

class Command(BaseCommand):
    help = 'Vincula telefone (próprio) a todas as pessoas cadastradas'
    def handle(self, *args, **options):
        fake = Faker('pt_BR')
        self.stdout.write(self.style.NOTICE('Iniciando criação de telefones'))
        pessoas = Pessoa.objects.all().values_list('pk', flat=True)
        if not pessoas:
            raise CommandError('Cadastre as pessoas primeiro através do Command inserir_pessoas')
        numeros = []
        for num in pessoas:
            ddd = f'0{random.randint(a=1, b=9)}{random.randint(a=1, b=9)}'
            nummero_fake = ddd + fake.unique.numerify('#########')
            telefone = Telefone(
                fone=nummero_fake,
                pessoa_id=num,
            )
            numeros.append(telefone)
        Telefone.objects.bulk_create(numeros, ignore_conflicts=True)
        self.stdout.write(self.style.SUCCESS('Telefones vinculados a todos os funcionários com sucesso!'))

        