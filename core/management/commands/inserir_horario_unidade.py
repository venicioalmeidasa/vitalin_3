
from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
from typing import Type
from django.db.models import Model
import random
from datetime import time


class Command(BaseCommand):
    help = 'Insere horários para unidades de saúde | regionais e assistenciais.'
    def handle(self, *args, **options):
        modelos = [
            ('regional', 'Distrito'),
            ('assistencial', 'Ubs'),
            ('assistencial', 'Especialidade'),
            ('assistencial', 'Ceco')
        ]
        self.stdout.write(self.style.NOTICE('Iniciando cadastro de horários para unidades'))
        for app_model in modelos:
            dias = [1, 2, 3, 4, 5]
            lista_horarios = []
            #classe do estabelcimento
            app, model = app_model
            modelo: Type[Model] = apps.get_model(app, model)
            nome_modelo:str = modelo.__name__.casefold()

            #Probabilidade para abrir no sábado
            prob_sabado = 0.2 if app == 'regional' else 0.35
            if random.random() <= prob_sabado:
                dias.append(6)

            #Chaves das instâncias
            unidades_pks = modelo.objects.values_list('pk', flat=True)
            if not unidades_pks:
                raise CommandError(f'Não há nenhum {nome_modelo} inserido na base de dados. Insira para cadastrar o referido horário')

            #classe do horario do estabelecimento
            modelo_horario: Type[Model] = apps.get_model(app, f'Horario{model}')
            
            #Para cada unidade
            for pk in unidades_pks:
                #para cada dia da semana
                for dia in dias:
                    #dicionario_criado
                    dados_horario:dict = {
                        'dia': dia,
                        'hora_abre': time(hour=8, minute=0)  if dia != 6 else time(hour=9, minute=0),
                        'hora_fecha': time(hour=17, minute=0)  if dia != 6 else time(hour=16, minute=0),
                        f'{nome_modelo}_id': pk
                    }
                    horario_criado = modelo_horario(**dados_horario)
                    lista_horarios.append(horario_criado)
            
            modelo_horario.objects.bulk_create(lista_horarios)

            self.stdout.write(self.style.SUCCESS(f'Todos os horários cadastrados para {nome_modelo}'))

        self.stdout.write(self.style.SUCCESS('Todos os horários para unidades cadastrados com sucesso'))



                  