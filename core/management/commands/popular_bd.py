
from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Executa comandos existentes para popular o banco de dados'
    def handle(self, *args, **options):
        
        FIXTURES = [
            'distrito.json',
            'especialidade.json',
            'ubs.json',
            'ocupacoes.json'
        ]
        
        COMANDANDOS = [
            'inserir_pessoas',
            'inserir_telefones',
            'inserir_profissionais'
        ]

        for fixture in FIXTURES:
            self.stdout.write(self.style.NOTICE('Iniciando carregamento das fixtures'))
            try:
                call_command('loaddata', fixture)
            except Exception as e:
                self.stdout.write(self.style.WARNING(f'Não foi possível executar a fixture {fixture} para preenchimento do bd. ERRO: {e}')) 
                self.stdout.write(self.style.WARNING('Procedimento interrompido'))
                return
            self.stdout.write(self.style.SUCCESS(f'Fixture {fixture} executada com sucesso'))
       

        for comando in COMANDANDOS:
            self.stdout.write(self.style.NOTICE('Iniciando o carregamento do BD com dados FAKE'))
            try:
                call_command(comando)
            except Exception as e:
                self.stdout.write(self.style.WARNING(f'Não foi possível executar o comando {comando} para preenchimento do bd. ERRO: {e}'))
                self.stdout.write(self.style.WARNING('Procedimento interrompido'))
                return
            self.stdout.write(self.style.SUCCESS(f'Comando {comando} executado com sucesso'))
            
        
            
