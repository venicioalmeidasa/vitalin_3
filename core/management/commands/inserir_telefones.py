
from django.core.management import BaseCommand, CommandError
from ..models.pessoa import Pessoa, Telefone
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
            nummero_fake = fake.unique.numerify('###########')
            telefone = Telefone(
                fone=nummero_fake,
                pessoa=num,
            )
            numeros.append(telefone)
        Telefone.objects.bulk_create(numeros, ignore_conflicts=True)

        