from django.core.management import BaseCommand, CommandError
from datetime import date
from faker import Faker
from apps.profissionais.models.rh import Profissional
from core.models.pessoa import Pessoa
from apps.profissionais.models.ocupacoes import OcupacaoCBO, DadosConselho


class Command(BaseCommand):
    help = 'Insere profissionais divididos entre as profissões cadastradas dentro da constante ESTRUTURA_CONSELHOS e ocupacoes.OcupacaoCBO'

    def handle(self, *args, **kwargs):
        fake = Faker('pt_br')

        # 1. Ajuste das chaves para bater exatamente com ESTRUTURA_CONSELHOS do model
        n_profissionais_conselhos: dict[str, int] = {
            'CRM': 600,
            'COREN': 2000,
            'CRP': 300,
            'CRO': 200,
            'CRN': 400,
            'CREFITO': 1200,
            'CRF': 200,
            'CRBM': 100,
            'CRBio': 100,
            'CREF': 200,
            'CRESS': 500,
            'CRMV': 200,
            'CREFONO': 1000
        }    

        #1. Número total de profissionais a serem cadastrados
        # Para agente administrativo 200 inicialmente
   
        total_profissionais:int = sum(n_profissionais_conselhos.values())
        adm = 200

        #2. estrutura consehos
        estrutura_conselhos: dict[str, DadosConselho] = OcupacaoCBO.ESTRUTURA_CONSELHOS

        n_prof_cadastro = total_profissionais+adm+20
        #3.  Pessoas para relacao onetoone com certa margem de segurança
        pessoas_civis:list = list(Pessoa.objects.values_list('pk', flat=True)[:n_prof_cadastro])
        if not pessoas_civis:
            raise CommandError('Cadastre primeiro as pessoas para vinculo com profissionais')
        if len(pessoas_civis) < total_profissionais+20+adm:
            raise CommandError(f'O banco de dados possui {len(pessoas_civis)} e são necessários {n_prof_cadastro} pessoas cadastradas')
        
        #dicionário de relatório final
        relatorio = {}
        #lista para profissionais criados para o bulk_create        
        profissionais_criados = []

        #Abrindo o dicionário estrutural de acordo os conselhos do comando
        data = date(2025,1,20)
        for conselho, n_profissionais in n_profissionais_conselhos.items():
            prof_cbo:list[tuple] = estrutura_conselhos.get(conselho,{}).get('profissoes',[])
            qtde_profissoes = len(prof_cbo)
            #Desempacotando cada tupla prof, cbo
            qte_profissionais, resto = divmod(n_profissionais, qtde_profissoes)
            if resto:
                adm += resto 
            for profissao, cbo in prof_cbo:
                relatorio[profissao] = 0
                #Cadastrando a qtde correspondente de profissionais
                for i in range(qte_profissionais):
                    p = pessoas_civis.pop(0)
                    ocupacao = cbo 
                    profissional = Profissional(
                        pessoa_id=p,
                        matricula=fake.numerify(f'{i}######'),
                        data_contratacao=data,
                        ocupacao_id=ocupacao,
                        num_conselho=fake.unique.numerify(f'#######{i}')
                    )
                    relatorio[profissao] += 1
                    profissionais_criados.append(profissional)
          
        
        #Criação do administrativo
     
        relatorio['AGENTE ADMINISTRATIVO'] = 0
        for i in range(adm):
            p_adm = pessoas_civis.pop(0)
            prof_adm = Profissional(
                pessoa_id=p_adm,
                matricula=fake.numerify(f'{i}0######'),
                data_contratacao=data,
                ocupacao_id='411010',                
            )
            relatorio['AGENTE ADMINISTRATIVO'] += 1
            profissionais_criados.append(prof_adm)

        Profissional.objects.bulk_create(profissionais_criados, ignore_conflicts=True)
        self.stdout.write(self.style.SUCCESS('Profissionais criados com sucesso conforme o relatório abaixo'))

        for prof, v in relatorio.items():
            self.stdout.write(self.style.SUCCESS(F'{prof}: {v} profissionais criados'))

           

               










     
        
